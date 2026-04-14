import json

import FreeCAD as App
import Draft
import Part
import Sketcher
import Mesh
from FreeCAD import Document
from Part import Feature
from FreeCAD import Part

import os
import itertools
import subprocess
from statistics import mean
from typing import Callable, List, Dict, Tuple

import freecadcupcalc
import normalfloatinput
from floatstats import FloatStats
from fluidneural import predict_pressure, predict_press_fault
from util import filename_output_simulate_current, tail

import cupcalc
import fluidio
from hexfloatinput import HexFloatInput
import hexfloatmodel
from hexfloatmodel import HexFloatModel
import math
from neuralcommon import filename_collect, filename_collect_full
from stl2img import stl2img
import pybars
import re
import shutil

# pressure_mul_max = 3.
filename_fluid_die = 'fluid_die'
filename_punch_die = 'punch_die'
suffix_cfile_hbs = '.cfile.hbs'
suffix_kfile_hbs = '.k.hbs'
filename_die_kfile_hbs = 'die.k.hbs'
filename_sheet_lip_kfile_hbs = 'sheet_lip.k.hbs'
filename_lsrun_out = 'lsrun.out.txt'
filename_nodout = 'nodout'
regex_sci_notation = r'[+\-]?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+\-]?\d+)?'
regex_float = r'(\-?\d+(\.\d*)?)'
kfile_coords = r'\$#\s*nid\s*x\s*y\s*z\s*tc\s*rc'
kfile_coord_line = '\s*' + regex_float + '\s*' + regex_float + '\s*' + regex_float + '\s*' + regex_float
kfile_sheet_nodes = 'sheet_set_shell'
kfile_edge_nodes = 'sheet_set_edge'
kfile_sheet_node_line = r'\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)'
n_lines_tail_nodout = 50000
nodout_time = 'n o d a l   p r i n t   o u t   f o r   t i m e  s t e p'
nodout_coord_line = r'\s*(\d+)\s*(' + regex_sci_notation + '\s*){11,11}(' + regex_sci_notation + ')'
n_curve_points_per_second = 50
tool_buffer = 0.1
regex_message_failed_time = 'f a i l e d\s*e l e m e n t\s*r e p o r t\s*time=\s*(' + regex_sci_notation + ')\n'
regex_message_number_of_failed = '\s*number\s*of\s*failed\s*'
regex_message_number_of_failed_whatever = regex_message_number_of_failed + '[\w\s=\d]*\n'
regex_message_number_of_failed_shells_1 = regex_message_number_of_failed + 'shell\s*elements\s*=\s*1\n'
regex_message_failed_time_full = regex_message_failed_time + '(' + regex_message_number_of_failed_whatever + ')+' + regex_message_number_of_failed_shells_1
filename_message = 'messag'
datetime_format = '%Y-%m-%d %H:%M:%S'
nodes_per_line = 8
lip_nearness = 0.1
runtime_default = 0.4


class FreecadFluidAndPunchDie:

    def __init__(self,
                 float_model: HexFloatModel
                 ):
        self.float_model = float_model

    def generate_lsrun_failtime(self, fc=True, stp=True, stl=True, img=True, lsdyn=True, bottom=False, stats=True,
                                runtime: float = runtime_default):
        print('generate_lsrun_failtime with float: ', self.float_model.float_input.__dict__)
        if os.path.exists(filename_output_simulate_current):
            shutil.rmtree(filename_output_simulate_current)
        os.makedirs(filename_output_simulate_current, exist_ok=True)

        lip_nodes, edge_nodes0 = self.generate(fc, stp, stl, img, lsdyn, bottom, stats, runtime)
        self.lsrun(bottom)
        time_to_crack = self.time_to_crack_normed(runtime)
        lip_z, edge_z = lip_edge_zvalues_at_end(lip_nodes)
        die_lip_mean = cupcalc.lip_height_mean(
            self.float_model.cup_calc.lip_x.tangent_r,
            self.float_model.cup_calc.lip_x.circle_r,
            self.float_model.cup_calc.lip_y.tangent_r,
            self.float_model.cup_calc.lip_y.circle_r,
            self.float_model.float_input.cup_depth,
            self.float_model.float_input.cup_lip
        )
        lip_mean = 0.
        if 0 < len(lip_z):
            lip_mean = mean(lip_z.values()) / die_lip_mean
        edge_mean = 0.
        if 0 < len(edge_z):
            edge_mean = mean(edge_z.values()) / self.float_model.float_input.cup_depth
        try:
            write_headings = False
            if not os.path.exists(filename_collect):
                write_headings = True
            fio_str = fluidio.FluidInputOutput(fluidio.from_float(self.float_model.float_input.__dict__),
                                               fluidio.FluidOutput(time_to_crack, lip_mean, edge_mean)).to_str()
            with open(filename_collect, 'a') as collect_file:
                if write_headings:
                    collect_file.write(fluidio.params_str)
                collect_file.write(fio_str)
            try:
                with open(filename_collect_full, 'a') as collect_file:
                    collect_file.write(fio_str)
            except Exception as e:
                print('freecadfluidandpunchdie: Could not write to', filename_collect_full, e)
        except Exception as e:
            print('Could not open output file ', filename_collect, ' for writing: ', e)

    # General note on default vs userprovided values.
    # First we use defaults to get the constraints right.
    # Then we set up constraints pointing to parameter on the model
    # Then we update the parameter on the model with the user provided value
    # If lsdyn is True, return the list of mesh node ids for the cup lip and the edge, as they're needed in the
    # simulation evaluation later.
    def generate(self, fc=True, stp=True, stl=True, img=True, lsdyn=True, bottom=False, stats=True,
                 runtime: float = runtime_default):
        print('Generate fluid / punch die')
        filename = filename_fluid_die
        if bottom:
            filename = filename_punch_die
        filename_cfile_hbs = filename + suffix_cfile_hbs
        filename_kfile_hbs = filename + suffix_kfile_hbs
        filename_output = filename_output_simulate_current + os.sep + filename
        filename_step = filename + '.step'
        filename_output_step = filename_output + '.step'
        filename_stl = filename_output + '.stl'
        filename_fc = filename_output + '.FCStd'
        filename_img = filename_output + '.png'
        filename_cfile = filename_output + '.cfile'
        filename_kfile = filename + '.k'
        filename_output_kfile = filename_output + '.k'
        filename_stats = filename_output + '_stats.json'
        runtime_pad10 = '{0: >10}'.format(runtime)
        if os.path.exists(filename_fc):
            os.remove(filename_fc)
        if os.path.exists(filename_output_step):
            os.remove(filename_output_step)
        if os.path.exists(filename_stl):
            os.remove(filename_stl)
        if os.path.exists(filename_img):
            os.remove(filename_img)
        if os.path.exists(filename_cfile):
            os.remove(filename_cfile)
        if os.path.exists(filename_output_kfile):
            os.remove(filename_output_kfile)

        fi = self.float_model.float_input
        fi.cup_y_to_x
        fcc = freecadcupcalc.calc_cup(fi.cup_rad, fi.cup_lip, fi.cup_depth, fi.cup_angle, fi.cup_tip)

        cup_rad = fi.cup_rad
        cup_lip = fi.cup_lip
        cup_depth = fi.cup_depth
        cup_angle = fi.cup_angle
        alu_thick = fi.alu_thick
        tool_displace = alu_thick / 2 + tool_buffer

        cup_ellipsoid_x = fcc['e_x']
        cup_ellipsoid_y = fcc['e_x'] * fi.cup_y_to_x
        cup_depth_ellipsoid = fcc['e_h']
        cup_angle_tip = fcc['t_a']
        tip_height = fcc['t_h']
        cup_cyl_rad = cup_rad + fi.space / 2 - fi.gripper

        punch_velocity_constant = math.pi * (cup_depth + tool_buffer) / (
                runtime - runtime * math.cos(math.pi * runtime))
        pressure_time_constant = 1. / 3.
        pressure_time_curve_end = (1. - pressure_time_constant)

        doc = App.newDocument(filename)

        container = doc.addObject('App::Part', filename)
        container.Visibility = False
        container.Label = filename
        top_label = 'top'
        rad_scale = 1.1
        top_tip_fillet, top_cup_fillet = create_tip_fillet(doc, cup_ellipsoid_x, cup_ellipsoid_y,
                                                           cup_depth_ellipsoid,
                                                           cup_angle, cup_angle_tip, tip_height, cup_depth, rad_scale,
                                                           cup_cyl_rad, cup_lip, top_label, container)

        top_face = Draft.make_facebinder(
            [(top_cup_fillet, 'Face1'), (top_tip_fillet, 'Face1'), (top_tip_fillet, 'Face2'), (top_tip_fillet, 'Face3'),
             (top_tip_fillet, 'Face4')],
            'top_face')
        top_face.Placement = App.Placement(
            App.Vector(0., 0., tool_displace), App.Rotation(App.Vector(0., 0., 1.), 0.))
        top_face.Visibility = True
        container.addObject(top_face)

        bottom_part = None
        if bottom:
            (bottom_cup_ellipsoid, bottom_cup_cyl, bottom_cup_cyl_ellipsoid, bottom_cup_fillet) = \
                self.create_cup_fillet_all(doc, cup_ellipsoid_x + alu_thick / 2, cup_ellipsoid_y + alu_thick / 2,
                                           cup_depth_ellipsoid,
                                           cup_angle, cup_angle_tip, tip_height, cup_depth,
                                           cup_cyl_rad, cup_lip, 'bottom', container)
            doc.recompute()

            bottom_face = Draft.make_facebinder(
                [(bottom_cup_fillet, 'Face1'), (bottom_cup_fillet, 'Face2'), (bottom_cup_fillet, 'Face4')],
                'bottom_face')
            bottom_face.Placement = App.Placement(
                App.Vector(0.00, 0.00, -tool_displace - cup_depth), App.Rotation(App.Vector(0.00, 0.00, 1.00), 0.00))
            bottom_face.Visibility = True
            container.addObject(bottom_face)

        doc.recompute()

        lip_nodes = None
        edge_nodes0 = None

        if fc:
            print('Exporting FreeCAD file ' + filename_fc)
            doc.saveAs(filename_fc)
        if stp or lsdyn:
            print('Exporting step files ' + filename_output_step)
            container.Shape.exportStep(filename_output_step)
        if stl or img:
            if stl:
                print('Exporting stl file ' + filename_stl)
            stl_exports = [container]
            if bottom:
                stl_exports.append(bottom_part)
            Mesh.export(stl_exports, filename_stl, 3, False)
        if img:
            print('Exporting img file ' + filename_img)
            stl2img(filename_output)
            if not stl:
                os.remove(filename_stl)
        if lsdyn:
            print('Exporting ls dyna command file ' + filename_cfile)
            pressure_max = fi.pressure
            pressure_min = pressure_max * pressure_time_constant

            def fluid_curve(time: float, runtime: float) -> float:

                time_runtime = time / runtime
                if time_runtime <= 0.:
                    return pressure_min
                else:
                    if pressure_time_curve_end <= time_runtime:
                        return pressure_max
                    else:
                        return pressure_min + (pressure_max - pressure_min) / pressure_time_curve_end * time_runtime

            def punch_curve(time: float, runtime: float) -> float:
                return math.sin(math.pi * time / runtime) * punch_velocity_constant

            compiler = pybars.Compiler()
            try:
                with open(filename_cfile_hbs, 'r') as cfile_hbs, \
                        open(filename_cfile, 'w') as cfile:
                    cfile_template = compiler.compile(cfile_hbs.read())
                    cfile_output = cfile_template({
                        'stepfile': filename_step,
                        'cup_cyl_rad': cup_cyl_rad,
                        'n_smooths': [0] * 8,
                        'kfile': filename_kfile
                    })
                    cfile.write(cfile_output)
                    cfile.flush()
                    lspp_cfile = ['C:\Program Files\LS-DYNA Suite R13 Student\lspp\lsprepost4.10_x64.exe',
                                  'c=' + filename + '.cfile', '-nographics']
                    lspp_process = subprocess.Popen(lspp_cfile, shell=True, stdout=subprocess.PIPE,
                                                    cwd=filename_output_simulate_current)
                    lspp_process.wait()
                    if 0 != lspp_process.returncode:
                        print('something wrong while running ls prepost')
                    else:
                        try:
                            with open(filename_kfile_hbs, 'r') as kfile_hbs, \
                                    open(filename_die_kfile_hbs, 'r') as die_kfile_hbs, \
                                    open(filename_sheet_lip_kfile_hbs, 'r') as sheet_lip_kfile_hbs, \
                                    open(filename_output_kfile, 'r+') as kfile:
                                combined_kfile_hbs_content = kfile_hbs.read() + os.linesep + die_kfile_hbs.read() + os.linesep + sheet_lip_kfile_hbs.read()
                                kfile_hbs_template = compiler.compile(combined_kfile_hbs_content)
                                alu_thick_pad10 = f'{alu_thick:1.8f}'
                                curve_func = fluid_curve
                                if bottom: curve_func = punch_curve
                                kfile_content = kfile.read()
                                lip_nodes_kfile, lip_nodes, edge_nodes0 = self.lip_kfile_content_and_nodes(
                                    kfile_content, not bottom)

                                kfile_hbs_compiled = kfile_hbs_template({
                                    'runtime_pad10': runtime_pad10,
                                    'nodes_lines': lip_nodes_kfile,
                                    'curve_lines': curve_lines(n_curve_points_per_second, curve_func,
                                                               runtime),
                                    'alu_thick_pad10': alu_thick_pad10
                                })
                                kfile_content = '*KEYWORD' + os.linesep + \
                                                kfile_hbs_compiled + \
                                                kfile_content[kfile_content.find('*ELEMENT_SHELL'):]
                                kfile.seek(0)
                                kfile.truncate()
                                kfile.write(kfile_content)
                                kfile.flush()
                        except Exception as e:
                            print('Could not open k file cfile_template or open k file')
                            print(e)
            except Exception as e:
                print('Could not open command file cfile_template or open command file')
                print(e)
            if not stp:
                os.remove(filename_output_step)
        if stats:
            print('Exporting stats file ' + filename_stats)
            fm = hexfloatmodel.create(fi)
            fo = fm.calc_fitness()
            fio = fluidio.FluidInputOutput(normalfloatinput.normalize_fluid_input(fluidio.from_float(fi.__dict__)))
            fo.press_fault = predict_press_fault(fio.values())
            fd = fm.calc_float_data()
            fs = FloatStats(fi, fo, fd)
            with open(filename_stats, 'w') as statsfile:
                json.dump(fs.dict(), statsfile, indent=2)
        App.closeDocument(filename)
        return lip_nodes, edge_nodes0

    def lsrun(self, bottom=True) -> bool:
        print('Run ls-run and log results')
        filename = filename_fluid_die
        if bottom:
            filename = filename_punch_die
        kfile = filename + '.k'
        lsr_cmd = [
            'C:\Program Files\LS-DYNA Suite R13 Student\lsdyna\ls-dyna_smp_d_R13.1.1_27-g8731a0d8c5_winx64_ifort190.exe',
            'i=' + kfile, 'ncpu=4', 'memory=128m']
        with open(filename_output_simulate_current + os.sep + filename_lsrun_out, 'w') as lsrun_out:
            lspp_process = subprocess.Popen(lsr_cmd, shell=True, stdout=lsrun_out.fileno(),
                                            cwd=filename_output_simulate_current)
            lspp_process.wait()
            if 0 != lspp_process.returncode:
                print('something wrong while running ls-run')
                return False
            else:
                print('Simulation done')
                return True

    def time_to_crack_normed(self, runtime: float):
        with open(filename_output_simulate_current + os.sep + filename_message, 'r') as message:
            msg_lines = message.read()
            error_match = re.search(regex_message_failed_time_full, msg_lines)
            if error_match:
                time_to_crack = float(msg_lines[error_match.regs[1][0]:error_match.regs[1][1]])
                normed = time_to_crack / runtime
                return normed
            return 1.

    def lip_kfile_content_and_nodes(self, kfile_content: str, include_edge_nodes: bool = True):
        kfile_lines = kfile_content.splitlines()
        lip_nodes = self.lip_nodes(kfile_lines)
        edge_nodes0 = []
        if include_edge_nodes:
            edge_nodes0 = edge_nodes(kfile_lines)
        lip_nodes_pad10 = list(map(lambda n: '{0: >10}'.format(n), lip_nodes))
        content = [lip_nodes_pad10[i:i + nodes_per_line] for i in range(0, len(lip_nodes_pad10), nodes_per_line)]
        return content, lip_nodes, edge_nodes0

    def lip_nodes(self, kfile_lines: List[str]) -> List[int]:
        node_coords0: Dict[int, Tuple[float, float, float]] = node_coords(kfile_lines)
        sheet_nodes0: List[int] = sheet_nodes(kfile_lines)
        sheet_coords0 = {key: node_coords0[key] for key in sheet_nodes0}
        a0 = self.float_model.cup_calc.lip_x.tangent_r
        a1 = self.float_model.cup_calc.lip_x.circle_r
        # a_buf = (a1 - a0) * lip_nearness
        # a0 = a0 - a_buf
        # a1 = a1 + a_buf
        b0 = self.float_model.cup_calc.lip_y.tangent_r
        b1 = self.float_model.cup_calc.lip_y.circle_r

        # b_buf = (b1 - b0) * lip_nearness
        # b0 = b0 - b_buf
        # b1 = b1 + b_buf

        def tween(x: float, y: float) -> bool:
            return cupcalc.between_ellipses(a0, b0, a1, b1, x, y)

        lip_nodes = list({k for k, v in sheet_coords0.items() if tween(v[0], v[1])})
        lip_nodes.sort()
        return lip_nodes


def create_cup_ellipsoid(
        doc: Document,
        cup_ellipsoid_x: float,
        cup_ellipsoid_y: float,
        cup_depth_ellipsoid: float,
        cup_angle: float,
        cup_angle_tip: float,
        tip_height: float,
        label: str = None,
        parent: Part = None,
        expr_prefix: str = ''
) -> Feature:
    name = 'cup_ellipsoid'
    if label is not None:
        name = label + '_' + name
    elif parent is not None:
        name = parent.Label + '_' + name
    cup_ellipsoid = doc.addObject('Part::Ellipsoid', name)
    if parent is not None:
        parent.addObject(cup_ellipsoid)
    cup_ellipsoid.addProperty('App::PropertyFloat', 'cup_ellipsoid_x')
    cup_ellipsoid.cup_ellipsoid_x = cup_ellipsoid_x
    cup_ellipsoid.addProperty('App::PropertyFloat', 'cup_ellipsoid_y')
    cup_ellipsoid.cup_ellipsoid_y = cup_ellipsoid_y
    cup_ellipsoid.addProperty('App::PropertyFloat', 'cup_depth_ellipsoid')
    cup_ellipsoid.cup_depth_ellipsoid = cup_depth_ellipsoid
    cup_ellipsoid.addProperty('App::PropertyFloat', 'tip_height')
    cup_ellipsoid.tip_height = tip_height
    cup_ellipsoid.Radius1 = cup_depth_ellipsoid
    cup_ellipsoid.setExpression('Radius1', expr_prefix + u'cup_depth_ellipsoid')
    cup_ellipsoid.Radius2 = cup_ellipsoid_x
    cup_ellipsoid.setExpression('Radius2', expr_prefix + u'cup_ellipsoid_x')
    cup_ellipsoid.Radius3 = cup_ellipsoid_y
    cup_ellipsoid.setExpression('Radius3', expr_prefix + u'cup_ellipsoid_y')
    cup_ellipsoid.Angle1 = -cup_angle_tip
    cup_ellipsoid.Angle2 = -cup_angle
    cup_ellipsoid.Angle3 = 360
    cup_ellipsoid.Placement = App.Placement(App.Vector(0, 0, cup_depth_ellipsoid - tip_height),
                                            App.Rotation(App.Vector(0, 0, 0), 0))
    cup_ellipsoid.setExpression('.Placement.Base.z',
                                expr_prefix + u'cup_depth_ellipsoid - ' + expr_prefix + u'tip_height')
    cup_ellipsoid.Label = name
    cup_ellipsoid.Visibility = False
    return cup_ellipsoid


def create_cup_cyl(
        doc: Document,
        cup_rad: float,
        cup_depth: float,
        rad_scale: float = 1.,
        label: str = None,
        parent: Part = None,
        expr_prefix: str = ''
) -> Feature:
    name = 'cup_cyl'
    if label is not None:
        name = label + '_' + name
    elif parent is not None:
        name = parent.Label + '_' + name
    cup_cyl = doc.addObject('Part::Cylinder', name)
    if parent is not None:
        parent.addObject(cup_cyl)
    cup_cyl.Label = name
    cup_cyl.addProperty('App::PropertyFloat', 'cup_rad')
    cup_cyl.cup_rad = cup_rad
    cup_cyl.addProperty('App::PropertyFloat', 'cup_depth')
    cup_cyl.cup_depth = cup_depth
    cup_cyl.Radius = cup_rad * rad_scale
    cup_cyl.setExpression('Radius', expr_prefix + u'cup_rad * ' + str(rad_scale))
    cup_cyl.Height = cup_depth
    cup_cyl.setExpression('Height', expr_prefix + u'cup_depth')
    cup_cyl.Visibility = False
    return cup_cyl


def create_cup_cyl_ellipsoid(
        doc: Document,
        cup_cyl: Feature,
        cup_ellipsoid: Feature,
        label: str = None,
        parent: Part = None
) -> Feature:
    name = 'cup_cyl_ellipsoid'
    if label is not None:
        name = label + '_' + name
    elif parent is not None:
        name = parent.Label + '_' + name
    cup_cyl_ellipsoid = doc.addObject('Part::Cut', name)
    if parent is not None:
        parent.addObject(cup_cyl_ellipsoid)
    cup_cyl_ellipsoid.Label = name
    cup_cyl_ellipsoid.Base = cup_cyl
    cup_cyl_ellipsoid.Tool = cup_ellipsoid
    cup_cyl_ellipsoid.Visibility = False
    return cup_cyl_ellipsoid


def create_cup_fillet(
        doc: Document,
        cup_lip: float,
        cup_cyl_ellipsoid: Feature,
        label: str = None,
        parent: Part = None
) -> Feature:
    name = 'cup_fillet'
    if label is not None:
        name = label + '_' + name
    elif parent is not None:
        name = parent.Label + '_' + name
    cup_fillet = doc.addObject('Part::Fillet', name)
    if parent is not None:
        parent.addObject(cup_fillet)
    cup_fillet.Label = name
    cup_fillet.Visibility = False
    cup_fillet.addProperty('App::PropertyFloat', 'cup_lip')
    cup_fillet.cup_lip = cup_lip
    cup_fillet.Base = cup_cyl_ellipsoid
    cup_fillets = [(5, cup_lip, cup_lip)]
    cup_fillet.Edges = cup_fillets
    del cup_fillets
    return cup_fillet


def create_punch(
        doc: Document,
        cup_cyl: Feature,
        cup_fillet: Feature,
        label: str = None,
        parent: Part = None
) -> Feature:
    name = 'punch'
    if label is not None:
        name = label + '_' + name
    elif parent is not None:
        name = parent.Label + '_' + name
    punch = doc.addObject('Part::Cut', name)
    punch.Visibility = False
    if parent is not None:
        parent.addObject(punch)
    punch.Label = name
    punch.Base = cup_cyl
    punch.Tool = cup_fillet
    return punch


def create_cup_fillet_all(
        doc: Document,
        cup_ellipsoid_x: float,
        cup_ellipsoid_y: float,
        cup_depth_ellipsoid: float,
        cup_angle: float,
        cup_angle_tip: float,
        tip_height: float,
        cup_depth: float,
        rad_scale: float,
        cup_rad: float,
        cup_lip: float,
        label: str = None,
        parent: Part = None,
        expr_prefix: str = ''
):
    cup_ellipsoid = create_cup_ellipsoid(doc, cup_ellipsoid_x, cup_ellipsoid_y, cup_depth_ellipsoid,
                                         cup_angle,
                                         cup_angle_tip, tip_height, label, parent, expr_prefix)
    cup_cyl = create_cup_cyl(doc, cup_rad, cup_depth, rad_scale, label, parent, expr_prefix)
    cup_cyl_ellipsoid = create_cup_cyl_ellipsoid(doc, cup_cyl, cup_ellipsoid, label, parent)
    cup_fillet = create_cup_fillet(doc, cup_lip, cup_cyl_ellipsoid, label, parent)
    return (cup_ellipsoid, cup_cyl, cup_cyl_ellipsoid, cup_fillet)


def create_tip_fillet(
        doc: Document,
        cup_ellipsoid_x: float,
        cup_ellipsoid_y: float,
        cup_depth_ellipsoid: float,
        cup_angle: float,
        cup_angle_tip: float,
        tip_height: float,
        cup_depth: float,
        rad_scale: float,
        cup_rad: float,
        cup_lip: float,
        label: str = None,
        parent: Part = None,
        expr_prefix: str = ''
):
    (cup_ellipsoid, cup_cyl, cup_cyl_ellipsoid, cup_fillet) = \
        create_cup_fillet_all(doc, cup_ellipsoid_x, cup_ellipsoid_y,
                              cup_depth_ellipsoid,
                              cup_angle, cup_angle_tip, tip_height, cup_depth, rad_scale,
                              cup_rad, cup_lip, label, parent, expr_prefix)
    top_punch = create_punch(doc, cup_cyl, cup_fillet, label, parent)
    name = 'tip_fillet'
    if label is not None:
        name = label + '_' + name
    tip_fillet = doc.addObject('Part::Fillet', name)
    tip_fillet.Base = top_punch
    tip_fillets = []
    tip_fillets.append((1, cup_lip, cup_lip))
    tip_fillet.Edges = tip_fillets
    del tip_fillets
    doc.recompute()

    return tip_fillet, cup_fillet


def f20(f: float) -> str: return '{0: >20}'.format(f'{f:1.3f}')


def curve_line(t: float, n: int, lam: Callable[[float, float], float], rt: float):
    tn = t / n
    if rt < tn: tn = rt
    return f20(tn) + f20(lam(tn, rt))


def curve_lines(n: int, lam: Callable[[float, float], float], rt: float):
    return list(map(lambda t: curve_line(t, n, lam, rt), range(0, int(n * rt) + 1)))


def kfile_lines(bottom: bool = False):
    filename = filename_fluid_die
    if bottom:
        filename = filename_punch_die
    filename_output_kfile = filename_output_simulate_current + os.sep + filename + '.k'
    try:
        with open(filename_output_kfile, 'r') as kfile:
            return kfile.readlines()
    except Exception as e:
        print('Could not access kfile: ', e)
        raise e


def node_coords(kfile_lines: List[str]) -> Dict[int, Tuple[float, float, float]]:
    after_kfile_coords = kfile_lines[
                         next(i for i, s in enumerate(kfile_lines) if
                              re.search(kfile_coords, s) is not None) + 1:]
    return dict(coords_from_chunk(after_kfile_coords))


def coords_from_chunk(chunk: List[str]):
    for s in chunk:
        r = re.search(kfile_coord_line, s)
        if None is not r:
            yield int(r.group(1)), (float(r.group(3)), float(r.group(5)), float(r.group(7)))
        else:
            break


def sheet_nodes(kfile_full: List[str]) -> List[int]:
    after_kfile_sheet_nodes = kfile_full[next(
        i for i, s in enumerate(kfile_full) if re.search(kfile_sheet_nodes, s) is not None) + 4:]
    return list(itertools.chain.from_iterable(nodes_from_kfile_chunk(after_kfile_sheet_nodes)))


def edge_nodes(kfile_full: List[str]) -> List[int]:
    after_kfile_edge_nodes = kfile_full[next(
        i for i, s in enumerate(kfile_full) if re.search(kfile_edge_nodes, s) is not None) + 4:]
    return list(itertools.chain.from_iterable(nodes_from_kfile_chunk(after_kfile_edge_nodes)))


def nodes_from_kfile_chunk(chunk):
    for s in chunk:
        r = re.search(kfile_sheet_node_line, s)
        if None is not r:
            def g():
                for i in range(1, 9):
                    yield int(r.group(i))

            yield g()
        else:
            break


def lip_edge_zvalues_at_end(lip_nodes: List[int]):
    return split_nodes_z_values_by_nodeset(nodes_zvalues_at_end(), lip_nodes)


def nodes_zvalues_at_end() -> Dict[int, float]:
    last_n = tail(filename_output_simulate_current + os.sep + filename_nodout, n_lines_tail_nodout).decode('ascii')
    heading_matches = list(re.finditer(nodout_time, last_n))
    last_node_lines = last_n[heading_matches[-2].start():heading_matches[-1].start()].splitlines(False)[3:]
    return dict(nodes_coords_from_nodout_chunk(last_node_lines))


def split_nodes_z_values_by_nodeset(nodes_zvalues: Dict[int, float], nodeset: List[int]):
    present = {}
    not_present = {}
    for k, v in nodes_zvalues.items():
        if k in nodeset:
            present[k] = v
        else:
            not_present[k] = v
    return present, not_present


def nodes_coords_from_nodout_chunk(chunk):
    for s in chunk:
        r = re.search(nodout_coord_line, s)
        if None is not r:
            yield int(r.group(1)), float(r.group(3))
            # def g():
            #    for i in range(1, 9):
            #        yield int(r.group(i))
            # yield g()
        else:
            break


def create(float_input: HexFloatInput = HexFloatInput()) -> FreecadFluidAndPunchDie:
    return FreecadFluidAndPunchDie(hexfloatmodel.create(float_input))
