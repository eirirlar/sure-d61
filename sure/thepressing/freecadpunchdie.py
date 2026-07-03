import FreeCAD as App
import Draft
import Part
import Sketcher
import Mesh
from FreeCAD import Document
from Part import Feature

import os
import cupcalc
import freecadcupcalc
from cupcalc import CupCalc
from hexfloatinput import HexFloatInput

from stl2img import stl2img
from util import filename_output


class FreecadPunchDie:

    def __init__(self,
                 float_input: HexFloatInput,
                 cup_calc: CupCalc
                 ):
        self.float_input = float_input
        self.cup_calc = cup_calc

    # General note on default vs userprovided values.
    # First we use defaults to get the constraints right.
    # Then we set up constraints pointing to parameter on the model
    # Then we update the parameter on the model with the user provided value
    def generate(self, fc=True, stp=True, stl=True, img=True, filename='punch_die'):
        output_filename = filename_output + os.sep + filename
        stepfile_top = output_filename + '_top.step'
        stepfile_bottom = output_filename + '_bottom.step'
        stlfile = output_filename + '.stl'
        fcfile = output_filename + '.FCStd'
        imgfile = output_filename + '.png'
        if os.path.exists(fcfile):
            os.remove(fcfile)
        if os.path.exists(stepfile_top):
            os.remove(stepfile_top)
        if os.path.exists(stepfile_bottom):
            os.remove(stepfile_bottom)
        if os.path.exists(stlfile):
            os.remove(stlfile)
        if os.path.exists(imgfile):
            os.remove(imgfile)

        fi = self.float_input
        fcc = freecadcupcalc.calc_cup(fi.cup_rad, fi.cup_lip, fi.cup_depth, fi.cup_angle, fi.cup_tip)

        cup_rad = fi.cup_rad
        cup_lip = fi.cup_lip
        cup_depth = fi.cup_depth
        cup_angle = fi.cup_angle
        alu_thick = fi.alu_thick
        tool_displace = alu_thick / 2 + 0.1

        cup_ellipsoid_x = fcc['e_x']
        cup_ellipsoid_y = fcc['e_x'] * fi.cup_y_to_x
        cup_depth_ellipsoid = fcc['e_h']
        cup_angle_tip = fcc['t_a']
        cup_cyl_rad = cup_rad + fi.space / 2 - fi.gripper
        print('cup_cyl_rad: ', cup_cyl_rad)

        doc = App.newDocument(filename)

        bottom = doc.addObject('App::Part', 'bottom')
        bottom.Visibility = True
        bottom.Label = 'bottom'
        bottom.Placement = App.Placement(
            App.Vector(0.00, 0.00, -cup_depth - tool_displace), App.Rotation(App.Vector(0.00, 0.00, 1.00), 0.00))
        (bottom_cup_ellipsoid, bottom_cup_cyl, bottom_cup_cyl_ellipsoid, bottom_cup_fillet) = \
            self.create_cup_fillet_all(doc, cup_ellipsoid_x, cup_ellipsoid_y, cup_depth_ellipsoid, cup_angle,
                                       cup_angle_tip, cup_depth, cup_cyl_rad, cup_lip, bottom)
        bottom_cup_fillet.Visibility = True

        top = doc.addObject('App::Part', 'top')
        top.Visibility = True
        top.Label = 'top'
        (top_cup_ellipsoid, top_cup_cyl, top_cup_cyl_ellipsoid, top_cup_fillet) = \
            self.create_cup_fillet_all(doc, cup_ellipsoid_x, cup_ellipsoid_y, cup_depth_ellipsoid, cup_angle,
                                       cup_angle_tip, cup_depth, cup_cyl_rad, cup_lip, top)
        top.Placement = App.Placement(
            App.Vector(0.00, 0.00, tool_displace), App.Rotation(App.Vector(0.00, 0.00, 1.00), 0.00))

        top_punch = doc.addObject('Part::Cut', 'top_punch')
        top.addObject(top_punch)
        top_punch.Label = 'top_punch'
        top_punch.Base = top_cup_cyl
        top_punch.Tool = top_cup_fillet

        doc.recompute()

        if fc:
            print('Exporting FreeCAD file ' + fcfile)
            doc.saveAs(fcfile)
        if stp:
            print('Exporting step files ' + stepfile_top + ', ' + stepfile_bottom)
            top.Shape.exportStep(stepfile_top)
            bottom.Shape.exportStep(stepfile_bottom)
        if stl or img:
            if stl:
                print('Exporting stl file ' + stlfile)
            Mesh.export([top, bottom], stlfile, 3, False)
        if img:
            print('Exporting img file ' + imgfile)
            stl2img(output_filename)
            if not stl:
                os.remove(stlfile)

        App.closeDocument(filename)

    def create_cup_ellipsoid(self,
                             doc: Document,
                             cup_ellipsoid_x: float,
                             cup_ellipsoid_y: float,
                             cup_depth_ellipsoid: float,
                             cup_angle: float,
                             cup_angle_tip: float,
                             cup_depth: float,
                             parent: Part = None
                             ) -> Feature:
        name = 'cup_ellipsoid'
        if parent is not None:
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
        cup_ellipsoid.Radius1 = cup_depth_ellipsoid
        cup_ellipsoid.setExpression('Radius1', u'cup_depth_ellipsoid')
        cup_ellipsoid.Radius2 = cup_ellipsoid_x
        cup_ellipsoid.setExpression('Radius2', u'cup_ellipsoid_x ')
        cup_ellipsoid.Radius3 = cup_ellipsoid_y
        cup_ellipsoid.setExpression('Radius3', u'cup_ellipsoid_y')
        cup_ellipsoid.Angle1 = cup_angle_tip
        cup_ellipsoid.Angle2 = -cup_angle
        cup_ellipsoid.Angle3 = 360
        cup_ellipsoid.Placement = App.Placement(App.Vector(0, 0, cup_depth),
                                                App.Rotation(App.Vector(0, 0, 0), 0))
        cup_ellipsoid.setExpression('.Placement.Base.z', u'cup_depth_ellipsoid')
        cup_ellipsoid.Label = name
        cup_ellipsoid.Visibility = False
        return cup_ellipsoid

    def create_cup_cyl(self,
                       doc: Document,
                       cup_cyl_rad: float,
                       cup_depth: float,
                       parent: Part = None
                       ) -> Feature:
        name = 'cup_cyl'
        if parent is not None:
            name = parent.Label + '_' + name
        cup_cyl = doc.addObject('Part::Cylinder', name)
        if parent is not None:
            parent.addObject(cup_cyl)
        cup_cyl.Label = name
        cup_cyl.addProperty('App::PropertyFloat', 'cup_cyl_rad')
        cup_cyl.cup_cyl_rad = cup_cyl_rad
        cup_cyl.addProperty('App::PropertyFloat', 'cup_depth')
        cup_cyl.cup_depth = cup_depth
        cup_cyl.Radius = cup_cyl_rad
        cup_cyl.setExpression('Radius', u'cup_cyl_rad')
        cup_cyl.Height = cup_depth
        cup_cyl.setExpression('Height', u'cup_depth')
        cup_cyl.Visibility = False
        return cup_cyl

    def create_cup_cyl_ellipsoid(self,
                                 doc: Document,
                                 cup_cyl: Feature,
                                 cup_ellipsoid: Feature,
                                 parent: Part = None
                                 ) -> Feature:
        name = 'cup_cyl_ellipsoid'
        if parent is not None:
            name = parent.Label + '_' + name
        cup_cyl_ellipsoid = doc.addObject('Part::Cut', name)
        if parent is not None:
            parent.addObject(cup_cyl_ellipsoid)
        cup_cyl_ellipsoid.Label = name
        cup_cyl_ellipsoid.Base = cup_cyl
        cup_cyl_ellipsoid.Tool = cup_ellipsoid
        cup_cyl_ellipsoid.Visibility = False
        return cup_cyl_ellipsoid

    def create_cup_fillet(self,
                          doc: Document,
                          cup_lip: float,
                          cup_cyl_ellipsoid: Feature,
                          parent: Part = None
                          ) -> Feature:
        name = 'cup_fillet'
        if parent is not None:
            name = parent.Label + '_' + name
        cup_fillet = doc.addObject('Part::Fillet', name)
        if parent is not None:
            parent.addObject(cup_fillet)
        cup_fillet.Label = name
        cup_fillet.Visibility = False
        cup_fillet.addProperty('App::PropertyFloat', 'cup_lip')
        cup_fillet.cup_lip = cup_lip
        cup_fillet.Base = cup_cyl_ellipsoid
        cup_fillets = [(4, cup_lip, cup_lip)]
        cup_fillet.Edges = cup_fillets
        del cup_fillets
        return cup_fillet

    def create_cup_fillet_all(self,
                              doc: Document,
                              cup_ellipsoid_x: float,
                              cup_ellipsoid_y: float,
                              cup_depth_ellipsoid: float,
                              cup_angle: float,
                              cup_angle_tip: float,
                              cup_depth: float,
                              cup_cyl_rad: float,
                              cup_lip: float,
                              parent: Part = None
                              ):
        cup_ellipsoid = self.create_cup_ellipsoid(doc, cup_ellipsoid_x, cup_ellipsoid_y, cup_depth_ellipsoid, cup_angle,
                                                  cup_angle_tip, cup_depth, parent)
        cup_cyl = self.create_cup_cyl(doc, cup_cyl_rad, cup_depth, parent)
        cup_cyl_ellipsoid = self.create_cup_cyl_ellipsoid(doc, cup_cyl, cup_ellipsoid, parent)
        cup_fillet = self.create_cup_fillet(doc, cup_lip, cup_cyl_ellipsoid, parent)
        return cup_ellipsoid, cup_cyl, cup_cyl_ellipsoid, cup_fillet


def create(float_input: HexFloatInput = HexFloatInput()) -> FreecadPunchDie:
    return FreecadPunchDie(float_input, cupcalc.calc_cup(float_input))
