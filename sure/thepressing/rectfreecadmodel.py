import FreeCAD as App
import Draft
import Part
import Sketcher
import Mesh
from FreeCAD import Document
from Part import Feature

import os

import freecadcupcalc
import freecadfluidandpunchdie
import rectfloatmodel
from rectfloatmodel import RectFloatModel, RectFloatInput, die_box_wall_thickness, scale
import math
from stl2img import stl2img
from util import filename_output_genetic
from rectcalc import overlap


class RectFreecadModel:

    def __init__(self,
                 float_model: RectFloatModel
                 ):
        self.float_model = float_model

    # General note on default vs userprovided values.
    # First we use defaults to get the constraints right.
    # Then we set up constraints pointing to parameter on the model
    # Then we update the parameter on the model with the user provided value
    def generate(self, fc=True, stp=True, stl=True, img=True, filename='thepressing', view_box=False,
                 inverted_die=False):
        output_filename = filename_output_genetic + os.sep + filename
        stepfile = output_filename + '.step'
        stlfile = output_filename + '.stl'
        fcfile = output_filename + '.FCStd'
        imgfile = output_filename + '.png'
        if os.path.exists(fcfile):
            os.remove(fcfile)
        if os.path.exists(stepfile):
            os.remove(stepfile)
        if os.path.exists(stlfile):
            os.remove(stlfile)
        if os.path.exists(imgfile):
            os.remove(imgfile)

        doc, pressing = self.create_model(filename, inverted_die)

        if view_box:
            add_view_box(doc, pressing)

        if fc:
            print('Exporting FreeCAD file ' + fcfile)
            doc.saveAs(fcfile)
        if stp:
            print('Exporting step file ' + stepfile)
            pressing.Shape.exportStep(stepfile)
        if stl or img:
            if stl:
                print('Exporting stl file ' + stlfile)
            Mesh.export([pressing], stlfile, 3, False)
        if img:
            print('Exporting img file ' + imgfile)
            stl2img(output_filename)
            if not stl:
                os.remove(stlfile)

        App.closeDocument(filename)

    def create_model(self, filename='thepressing', inverted_die=False):
        fi = self.float_model.float_input

        cup_rad = fi.cup_rad
        cup_lip = fi.cup_lip
        cup_depth = fi.cup_depth
        cup_angle = fi.cup_angle
        alu_thick = fi.alu_thick
        rect_calc = self.float_model.rect_calc

        fcc = freecadcupcalc.calc_cup(fi.cup_rad, fi.cup_lip, fi.cup_depth, fi.cup_angle, fi.cup_tip)

        cup_ellipsoid_x = fcc['e_x']
        cup_ellipsoid_y = fcc['e_x'] * fi.cup_y_to_x
        cup_depth_ellipsoid = fcc['e_h']
        cup_angle_tip = fcc['t_a']
        tip_height = fcc['t_h']
        die_pipe_rad = 2.
        die_pipe_thickness = 1.
        die_bottom_bed_height = 1.
        die_bottom_inject_cyl_inner_diam = 13.
        die_bottom_inject_cyl_inner_height = 22.
        die_bottom_inject_cyl_outer_diam = 17.3
        die_bottom_inject_cyl_outer_height = 2.
        die_bottom_inject_cyl_horizontal_offset = .6
        die_bottom_inject_cyl_vertical_offset = .1

        doc = App.newDocument(filename)

        props = doc.addObject('App::FeaturePython', 'props')
        props.addProperty('App::PropertyFloat', 'scale').scale = scale
        props.addProperty('App::PropertyFloat', 'panel_width').panel_width = fi.width
        props.setExpression('panel_width', u'scale * ' + str(fi.width))
        props.addProperty('App::PropertyFloat', 'panel_length').panel_length = fi.length
        props.setExpression('panel_length', u'scale * ' + str(fi.length))
        props.addProperty('App::PropertyFloat', 'cup_ellipsoid_x').cup_ellipsoid_x = cup_ellipsoid_x
        props.setExpression('cup_ellipsoid_x', u'scale * ' + str(cup_ellipsoid_x))
        props.addProperty('App::PropertyFloat', 'cup_ellipsoid_y').cup_ellipsoid_y = cup_ellipsoid_y
        props.setExpression('cup_ellipsoid_y', u'scale * ' + str(cup_ellipsoid_y))
        props.addProperty('App::PropertyFloat', 'cup_depth_ellipsoid').cup_depth_ellipsoid = cup_depth_ellipsoid
        props.setExpression('cup_depth_ellipsoid', u'scale * ' + str(cup_depth_ellipsoid))
        props.addProperty('App::PropertyFloat', 'tip_height').tip_height = tip_height
        props.setExpression('tip_height', u'scale * ' + str(tip_height))
        props.addProperty('App::PropertyFloat', 'cup_rad').cup_rad = cup_rad
        props.setExpression('cup_rad', u'scale * ' + str(cup_rad))
        props.addProperty('App::PropertyFloat', 'cup_depth').cup_depth = cup_depth
        props.setExpression('cup_depth', u'scale * ' + str(cup_depth))
        props.addProperty('App::PropertyFloat', 'cup_lip').cup_lip = cup_lip
        props.setExpression('cup_lip', u'scale * ' + str(cup_lip))
        props.addProperty('App::PropertyFloat', 'cup_angle').cup_angle = cup_angle
        props.setExpression('cup_angle', u'scale * ' + str(cup_angle))
        props.addProperty('App::PropertyFloat', 'alu_thick').alu_thick = alu_thick
        props.setExpression('alu_thick', u'scale * ' + str(alu_thick))
        props.addProperty('App::PropertyFloat', 'die_pipe_rad').die_pipe_rad = die_pipe_rad
        props.setExpression('die_pipe_rad', u'scale * ' + str(die_pipe_rad))
        props.addProperty('App::PropertyFloat', 'die_pipe_thickness').die_pipe_thickness = die_pipe_thickness
        props.setExpression('die_pipe_thickness', u'scale * ' + str(die_pipe_thickness))
        props.addProperty('App::PropertyFloat',
                          'die_box_wall_thickness').die_box_wall_thickness = die_box_wall_thickness
        props.setExpression('die_box_wall_thickness', u'scale * ' + str(die_box_wall_thickness))
        props.addProperty('App::PropertyFloat', 'die_bottom_bed_height').die_bottom_bed_height = die_bottom_bed_height
        props.setExpression('die_bottom_bed_height', u'scale * ' + str(die_bottom_bed_height))
        props.addProperty('App::PropertyFloat',
                          'die_bottom_inject_cyl_inner_rad').die_bottom_inject_cyl_inner_rad = die_bottom_inject_cyl_inner_diam/2.
        props.setExpression('die_bottom_inject_cyl_inner_rad', u'scale * ' + str(die_bottom_inject_cyl_inner_diam/2.))
        props.addProperty('App::PropertyFloat',
                          'die_bottom_inject_cyl_horizontal_offset').die_bottom_inject_cyl_horizontal_offset = die_bottom_inject_cyl_horizontal_offset
        props.setExpression('die_bottom_inject_cyl_horizontal_offset',
                            u'scale * ' + str(die_bottom_inject_cyl_horizontal_offset))
        props.addProperty('App::PropertyFloat',
                          'die_bottom_inject_cyl_vertical_offset').die_bottom_inject_cyl_vertical_offset = die_bottom_inject_cyl_vertical_offset
        props.setExpression('die_bottom_inject_cyl_vertical_offset',
                            u'scale * ' + str(die_bottom_inject_cyl_vertical_offset))
        props.addProperty('App::PropertyFloat',
                          'die_bottom_inject_cyl_inner_height').die_bottom_inject_cyl_inner_height = die_bottom_inject_cyl_inner_height
        props.setExpression('die_bottom_inject_cyl_inner_height',
                            u'scale * ' + str(die_bottom_inject_cyl_inner_height))
        props.addProperty('App::PropertyFloat',
                          'die_bottom_inject_cyl_outer_height').die_bottom_inject_cyl_outer_height = die_bottom_inject_cyl_outer_height
        props.setExpression('die_bottom_inject_cyl_outer_height',
                            u'scale * ' + str(die_bottom_inject_cyl_outer_height))

        cups = []
        cup_thicks = []

        if inverted_die:
            die_top_pipes = []
            die_top_tubes = []

        rad_scale = 1.
        tip_fillet, cup_fillet = freecadfluidandpunchdie.create_tip_fillet(doc, cup_ellipsoid_x, cup_ellipsoid_y,
                                                                           cup_depth_ellipsoid,
                                                                           cup_angle, cup_angle_tip, tip_height,
                                                                           cup_depth, rad_scale,
                                                                           cup_rad, scale * cup_lip,
                                                                           expr_prefix='props.')

        cup_around_fillet_facebinder = Draft.make_facebinder(
            [(cup_fillet, 'Face1'), (tip_fillet, 'Face1'), (tip_fillet, 'Face2'), (tip_fillet, 'Face3'),
             (tip_fillet, 'Face4')],
            'cup_around_fillet_facebinder')

        cup0 = doc.addObject('Part::Extrusion', 'cup0')
        cup0.Base = cup_around_fillet_facebinder
        cup0.LengthFwd = alu_thick
        cup0.setExpression('LengthFwd', u'props.alu_thick')

        cup_thick0 = doc.addObject('Part::Extrusion', 'cup_thick0')
        cup_thick0.Base = cup_around_fillet_facebinder
        cup_thick0.LengthFwd = die_box_wall_thickness
        cup_thick0.setExpression('LengthFwd', u'props.die_box_wall_thickness')

        body_plate = doc.addObject('PartDesign::Body', 'body_plate')
        body_plate.Visibility = False
        body_plate.Label = 'body_plate'

        plate_sketch = body_plate.newObject('Sketcher::SketchObject', 'plate_sketch')
        plate_sketch.Visibility = False
        plate_sketch.Support = (body_plate.Origin.OriginFeatures[3], [''])
        plate_sketch.MapMode = 'FlatFace'

        plate_sketch_line_top = plate_sketch.addGeometry(
            Part.LineSegment(App.Vector(-fi.width / 2., fi.length / 2., 0),
                             App.Vector(fi.width / 2., fi.length / 2., 0)), False)
        plate_sketch_line_right = plate_sketch.addGeometry(
            Part.LineSegment(App.Vector(fi.width / 2., fi.length / 2., 0),
                             App.Vector(fi.width / 2., -fi.length / 2., 0)), False)
        plate_sketch_line_bottom = plate_sketch.addGeometry(
            Part.LineSegment(App.Vector(fi.width / 2., -fi.length / 2., 0),
                             App.Vector(-fi.width / 2., -fi.length / 2., 0)), False)
        plate_sketch_line_left = plate_sketch.addGeometry(
            Part.LineSegment(App.Vector(-fi.width / 2., -fi.length / 2., 0),
                             App.Vector(-fi.width / 2., fi.length / 2., 0)), False)
        plate_sketch_constraint_line_top = plate_sketch.addConstraint(
            Sketcher.Constraint('DistanceX', 0, 1, 0, 2, fi.width))
        plate_sketch.setExpression('Constraints[' + str(plate_sketch_constraint_line_top) + ']', u'props.panel_width')
        plate_sketch_constraint_line_right = plate_sketch.addConstraint(
            Sketcher.Constraint('DistanceY', 1, 2, 0, 2, fi.length))
        plate_sketch.setExpression('Constraints[' + str(plate_sketch_constraint_line_right) + ']',
                                   u'props.panel_length')
        plate_sketch_constraint_line_bottom = plate_sketch.addConstraint(
            Sketcher.Constraint('DistanceX', 2, 2, 1, 2, fi.width))
        plate_sketch.setExpression('Constraints[' + str(plate_sketch_constraint_line_bottom) + ']',
                                   u'props.panel_width')
        plate_sketch_constraint_line_left = plate_sketch.addConstraint(
            Sketcher.Constraint('DistanceY', 2, 2, 0, 1, fi.length))
        plate_sketch.setExpression('Constraints[' + str(plate_sketch_constraint_line_left) + ']', u'props.panel_length')

        plate_sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, 3, 2))
        plate_sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 2))
        plate_sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
        plate_sketch.addConstraint(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
        plate_sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))
        plate_sketch.addConstraint(Sketcher.Constraint('Vertical', 3))
        plate_sketch_constraint_origo_to_upper_right_x = plate_sketch.addConstraint(
            Sketcher.Constraint('DistanceX', -1, 1, 0, 2, fi.width / 2.))
        plate_sketch.setExpression('Constraints[' + str(plate_sketch_constraint_origo_to_upper_right_x) + ']',
                                   u'props.panel_width/2.0')
        plate_sketch_constraint_origo_to_upper_right_y = plate_sketch.addConstraint(
            Sketcher.Constraint('DistanceY', -1, 1, 0, 2, fi.length / 2.))
        plate_sketch.setExpression('Constraints[' + str(plate_sketch_constraint_origo_to_upper_right_y) + ']',
                                   u'props.panel_length/2.0')

        if inverted_die:
            die_top_pipe = doc.addObject('Part::Cylinder', 'die_top_pipe')
            die_top_pipe.Label = 'die_top_pipe'
            die_top_pipe.Radius = die_pipe_rad
            die_top_pipe.setExpression('Radius', u'props.die_pipe_rad')
            die_top_pipe.Height = die_box_wall_thickness
            die_top_pipe.setExpression('Height', u'props.die_box_wall_thickness')

            die_pipe_inner = doc.addObject('Part::Cylinder', 'die_pipe_inner')
            die_pipe_inner.Label = 'die_pipe_inner'
            die_pipe_inner.Radius = die_pipe_rad + die_pipe_thickness
            die_pipe_inner.setExpression('Radius', u'props.die_pipe_rad')
            die_pipe_inner.Height = cup_depth + die_box_wall_thickness
            die_pipe_inner.setExpression('Height', u'props.cup_depth + props.die_box_wall_thickness')

            die_pipe_outer = doc.addObject('Part::Cylinder', 'die_pipe_outer')
            die_pipe_outer.Label = 'die_pipe_outer'
            die_pipe_outer.Radius = die_pipe_rad + die_pipe_thickness
            die_pipe_outer.setExpression('Radius', u'props.die_pipe_rad + props.die_pipe_thickness')
            die_pipe_outer.Height = cup_depth + die_box_wall_thickness
            die_pipe_outer.setExpression('Height', u'props.cup_depth + props.die_box_wall_thickness')

            die_top_tube = doc.addObject('Part::Cut', 'die_top_tube')
            die_top_tube.Label = 'die_top_tube'
            die_top_tube.Base = die_pipe_outer
            die_top_tube.Tool = die_pipe_inner

        # cups_group, holes in plate, and filled cups_group if inverted_die is True
        for i, (x, y) in enumerate(rect_calc.cup_points):
            istr = str(i)
            if 0 == i:
                cup_i = cup0
                if inverted_die:
                    die_top_pipe_i = die_top_pipe
                    die_top_tube_i = die_top_tube
                    cup_thick_i = cup_thick0
            else:
                cup_i = doc.addObject('App::Link', 'cup' + istr)
                cup_i.setLink(cup0)
                if inverted_die:
                    cup_thick_i = doc.addObject('App::Link', 'cup_thick' + istr)
                    cup_thick_i.setLink(cup_thick0)

                    die_top_pipe_i = doc.addObject('App::Link', 'die_top_pipe' + istr)
                    die_top_pipe_i.setLink(die_top_pipe)

                    die_top_tube_i = doc.addObject('App::Link', 'die_top_tube' + istr)
                    die_top_tube_i.setLink(die_top_tube)

            cups.append(cup_i)
            cup_i.Placement = App.Placement(App.Vector(x, y, 0), App.Rotation(App.Vector(0, 0, 1), 0))
            cup_i.setExpression('.Placement.Base.x', u'props.scale * ' + str(x))
            cup_i.setExpression('.Placement.Base.y', u'props.scale * ' + str(y))
            cup_i.Visibility = False

            if inverted_die:
                cup_thicks.append(cup_thick_i)
                cup_thick_i.Placement = App.Placement(App.Vector(x, y, 0), App.Rotation(App.Vector(0, 0, 1), 0))
                cup_thick_i.setExpression('.Placement.Base.x', u'props.scale * ' + str(x))
                cup_thick_i.setExpression('.Placement.Base.y', u'props.scale * ' + str(y))

                die_top_pipe_i.setExpression('.Placement.Base.x', u'props.scale * ' + str(x))
                die_top_pipe_i.setExpression('.Placement.Base.y', u'props.scale * ' + str(y))
                die_top_pipes.append(die_top_pipe_i)
                die_top_pipe_i.Visibility = False

                die_top_tube_i.setExpression('.Placement.Base.x', u'props.scale * ' + str(x))
                die_top_tube_i.setExpression('.Placement.Base.y', u'props.scale * ' + str(y))
                die_top_tube_i.setExpression('.Placement.Base.z',
                                             u'props.alu_thick - (props.cup_depth + props.die_box_wall_thickness)')
                die_top_tubes.append(die_top_tube_i)
                die_top_tube_i.Visibility = False

            plate_sketch.addGeometry(Part.Circle(App.Vector(x, y, 0), App.Vector(0, 0, 1), cup_rad), False)
            plate_sketch_cup_constraint_x = plate_sketch.addConstraint(
                Sketcher.Constraint('DistanceX', -1, 1, plate_sketch.GeometryCount - 1, 3, x))
            plate_sketch.setExpression('Constraints[' + str(plate_sketch_cup_constraint_x) + ']',
                                       u'props.scale * ' + str(x))
            plate_sketch_cup_constraint_y = plate_sketch.addConstraint(
                Sketcher.Constraint('DistanceY', -1, 1, plate_sketch.GeometryCount - 1, 3, y))
            constraint_id = plate_sketch.addConstraint(
                Sketcher.Constraint('Radius', plate_sketch.GeometryCount - 1, cup_rad))
            plate_sketch.setExpression('Constraints[' + str(plate_sketch_cup_constraint_y) + ']',
                                       u'props.scale * ' + str(y))
            plate_sketch.setExpression('Constraints[' + str(constraint_id) + ']', u'props.cup_rad')

        union_cups = doc.addObject('Part::MultiFuse', 'union_cups')
        union_cups.Label = 'union_cups'
        union_cups.Shapes = cups

        plate_pad = doc.addObject('Part::Extrusion', 'plate_pad')
        plate_pad.Label = 'plate_pad'
        plate_pad.Base = doc.getObject('plate_sketch')
        plate_pad.LengthFwd = alu_thick
        plate_pad.setExpression('LengthFwd', u'props.alu_thick')
        plate_pad.Solid = True
        plate_pad.Placement = App.Placement(App.Vector(0, 0, cup_depth), App.Rotation(App.Vector(0, 0, 1), 0))
        plate_pad.setExpression('.Placement.Base.z', u'props.cup_depth')
        plate_pad.Visibility = False

        pressing = doc.addObject('Part::MultiFuse', 'pressing')
        pressing.Label = 'pressing'
        pressing.Shapes = [union_cups, plate_pad]

        doc.recompute()

        if inverted_die:
            # top die

            die_top_union_cup_thicks = doc.addObject('Part::MultiFuse', 'die_top_union_cup_thicks')
            die_top_union_cup_thicks.Label = 'die_top_union_cup_thicks'
            die_top_union_cup_thicks.Shapes = cup_thicks

            die_top_plate_thick_pad = doc.addObject('Part::Extrusion', 'die_top_plate_thick_pad')
            die_top_plate_thick_pad.Label = 'die_top_plate_thick_pad'
            die_top_plate_thick_pad.Base = plate_sketch
            die_top_plate_thick_pad.LengthFwd = die_box_wall_thickness
            die_top_plate_thick_pad.setExpression('LengthFwd', u'props.die_box_wall_thickness')
            die_top_plate_thick_pad.Solid = True
            die_top_plate_thick_pad.Placement = App.Placement(App.Vector(0, 0, cup_depth),
                                                              App.Rotation(App.Vector(0, 0, 1), 0))
            die_top_plate_thick_pad.setExpression('.Placement.Base.z', u'props.cup_depth')
            die_top_plate_thick_pad.Visibility = False

            die_top_pressing_thick = doc.addObject('Part::MultiFuse', 'die_top_pressing_thick')
            die_top_pressing_thick.Label = 'die_top_pressing_thick'
            die_top_pressing_thick.Shapes = [die_top_union_cup_thicks, die_top_plate_thick_pad]

            die_top_union_die_pipes = doc.addObject('Part::MultiFuse', 'die_top_union_die_pipes')
            die_top_union_die_pipes.Label = 'die_top_union_die_pipes'
            die_top_union_die_pipes.Shapes = die_top_pipes

            pressing_thick_with_die_pipes = doc.addObject('Part::Cut', 'pressing_thick_with_die_pipes')
            pressing_thick_with_die_pipes.Label = 'pressing_thick_with_die_pipes'
            pressing_thick_with_die_pipes.Base = die_top_pressing_thick
            pressing_thick_with_die_pipes.Tool = die_top_union_die_pipes

            wall_inner = doc.addObject('Part::Box', 'wall_inner')
            wall_inner.Label = 'wall_inner'
            wall_inner.setExpression('Length', u'props.panel_width')
            wall_inner.setExpression('Width', u'props.panel_length')
            wall_inner.setExpression('Height', u'2*props.cup_depth+props.die_box_wall_thickness')
            wall_inner.setExpression('.Placement.Base.x',
                                     u'-props.panel_width / 2')
            wall_inner.setExpression('.Placement.Base.y',
                                     u'-props.panel_length / 2')
            wall_inner.setExpression('.Placement.Base.z', u'-props.cup_depth')

            wall_outer = doc.addObject('Part::Box', 'wall_outer')
            wall_outer.Label = 'wall_outer'
            wall_outer.setExpression('Length', u'props.panel_width+2*props.die_box_wall_thickness')
            wall_outer.setExpression('Width', u'props.panel_length+2*props.die_box_wall_thickness')
            wall_outer.setExpression('Height', u'2*props.cup_depth+props.die_box_wall_thickness')
            wall_outer.setExpression('.Placement.Base.x',
                                     u'-(props.panel_width / 2 + props.die_box_wall_thickness)')
            wall_outer.setExpression('.Placement.Base.y',
                                     u'-(props.panel_length / 2 + props.die_box_wall_thickness)')
            wall_outer.setExpression('.Placement.Base.z', u'-props.cup_depth')

            wall = doc.addObject('Part::Cut', 'wall')
            wall.Label = 'wall'
            wall.Base = wall_outer
            wall.Tool = wall_inner

            union_die_tubes = doc.addObject('Part::MultiFuse', 'union_die_tubes')
            union_die_tubes.Label = 'union_die_tubes'
            union_die_tubes.Shapes = die_top_tubes
            union_die_tubes.Visibility = False

            die_top_die = doc.addObject('Part::MultiFuse', 'die_top_die')
            die_top_die.Label = 'die_top_die'
            die_top_die.Shapes = [pressing_thick_with_die_pipes, wall, union_die_tubes]
            die_top_die.Placement = App.Placement(App.Vector(0., 0., 0.), App.Rotation(App.Vector(0., 1., 0.), 180.))
            die_top_die.Visibility = False

            body_view_hinge = doc.addObject('PartDesign::Body', 'body_view_hinge')
            body_view_hinge.Visibility = False
            body_view_hinge.Label = 'body_view_hinge'

            sketch_view_hinge_top_z = cup_depth + die_box_wall_thickness
            sketch_view_hinge_top_rad = overlap / 3.
            sketch_view_hinge_top, bulb_top_x = create_sketch_view_hinge(body_view_hinge,
                                                                         sketch_view_hinge_top_rad,
                                                                         'top',
                                                                         z=sketch_view_hinge_top_z)

            sketch_view_hinge_bottom_rad = overlap / 4.
            sketch_view_hinge_bottom_x = (
                                                 sketch_view_hinge_bottom_rad + sketch_view_hinge_top_rad) / 4.
            sketch_view_hinge_bottom_z = -(cup_depth + die_box_wall_thickness)
            sketch_view_hinge_bottom, bulb_bottom_x = create_sketch_view_hinge(body_view_hinge,
                                                                               sketch_view_hinge_bottom_rad,
                                                                               'bottom',
                                                                               sketch_view_hinge_bottom_x,
                                                                               sketch_view_hinge_bottom_z)

            die_top_loft_view_hinge = doc.addObject('Part::Loft', 'die_top_loft_view_hinge')
            die_top_loft_view_hinge.Sections = [sketch_view_hinge_bottom, sketch_view_hinge_top]
            die_top_loft_view_hinge.Solid = True
            die_top_loft_view_hinge.Visibility = False

            # bottom die
            die_bottom_frame_inner = doc.addObject('Part::Box', 'die_bottom_frame_inner')
            die_bottom_frame_inner.Label = 'die_bottom_frame_inner'
            die_bottom_frame_inner.setExpression('Length', u'props.panel_width-2*props.die_box_wall_thickness')
            die_bottom_frame_inner.setExpression('Width', u'props.panel_length-2*props.die_box_wall_thickness')
            die_bottom_frame_inner.setExpression('Height', u'props.die_bottom_bed_height')
            die_bottom_frame_inner.setExpression('.Placement.Base.x',
                                                 u'-(props.panel_width / 2 - props.die_box_wall_thickness)')
            die_bottom_frame_inner.setExpression('.Placement.Base.y',
                                                 u'-(props.panel_length / 2 - props.die_box_wall_thickness)')
            die_bottom_frame_inner.setExpression('.Placement.Base.z',
                                                 u'props.die_bottom_inject_cyl_inner_height-(3*props.die_box_wall_thickness+props.cup_depth+props.alu_thick)')

            die_bottom_fillet_frame_inner = doc.addObject('Part::Fillet', 'die_bottom_fillet_frame_inner')
            die_bottom_fillet_frame_inner.Base = die_bottom_frame_inner
            die_bottom_fillet_frame_inner_fillets = [
                (4, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.),
                (8, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.),
                (9, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.),
                (11, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.)
            ]
            die_bottom_fillet_frame_inner.Edges = die_bottom_fillet_frame_inner_fillets
            del die_bottom_fillet_frame_inner_fillets

            die_bottom_frame_outer = doc.addObject('Part::Box', 'die_bottom_frame_outer')
            die_bottom_frame_outer.Label = 'die_bottom_frame_outer'
            die_bottom_frame_outer.setExpression('Length', u'props.panel_width')
            die_bottom_frame_outer.setExpression('Width', u'props.panel_length')
            die_bottom_frame_outer.setExpression('Height', u'props.die_bottom_inject_cyl_inner_height+props.die_bottom_bed_height')
            die_bottom_frame_outer.setExpression('.Placement.Base.x',
                                                 u'-(props.panel_width / 2)')
            die_bottom_frame_outer.setExpression('.Placement.Base.y',
                                                 u'-(props.panel_length / 2)')
            die_bottom_frame_outer.setExpression('.Placement.Base.z',
                                                 u'-(3*props.die_box_wall_thickness+props.cup_depth+props.alu_thick)')

            die_bottom_cut_frame = doc.addObject('Part::Cut', 'die_bottom_cut_frame')
            die_bottom_cut_frame.Label = 'die_bottom_cut_frame'
            die_bottom_cut_frame.Base = die_bottom_frame_outer
            die_bottom_cut_frame.Tool = die_bottom_fillet_frame_inner

            die_bottom_fillet_cut_frame = doc.addObject('Part::Fillet', 'die_bottom_fillet_cut_frame')
            die_bottom_fillet_cut_frame.Base = die_bottom_cut_frame
            die_bottom_fillet_cut_frame_fillets = [
                (10, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.),
                (11, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.),
                (12, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.),
                (13, scale * die_bottom_bed_height / 3., scale * die_bottom_bed_height / 3.)
            ]
            die_bottom_fillet_cut_frame.Edges = die_bottom_fillet_cut_frame_fillets
            del die_bottom_fillet_cut_frame_fillets

            die_bottom_inject_inner_cyl = doc.addObject('Part::Cylinder', 'die_bottom_inject_inner_cyl')
            die_bottom_inject_inner_cyl.Label = 'die_bottom_inject_inner_cyl'
            die_bottom_inject_inner_cyl.Radius = die_bottom_inject_cyl_inner_diam/2.
            die_bottom_inject_inner_cyl.setExpression('Radius', u'props.die_bottom_inject_cyl_inner_rad')
            die_bottom_inject_inner_cyl.Height = die_bottom_inject_cyl_inner_height
            #die_bottom_inject_inner_cyl.Height = 2. * die_box_wall_thickness - die_bottom_bed_height
            die_bottom_inject_inner_cyl.setExpression('.Placement.Base.z',
                                                      u'-(3*props.die_box_wall_thickness+props.cup_depth+props.alu_thick)')

            die_bottom_inject_outer_cyl = doc.addObject('Part::Cylinder', 'die_bottom_inject_outer_cyl')
            die_bottom_inject_outer_cyl.Label = 'die_bottom_inject_outer_cyl'
            die_bottom_inject_outer_cyl.Radius = die_bottom_inject_cyl_outer_diam/2.
            die_bottom_inject_outer_cyl.Height = die_bottom_inject_cyl_outer_height
            die_bottom_inject_outer_cyl.setExpression('.Placement.Base.z',
                                                      u'props.die_bottom_inject_cyl_inner_height - (props.die_bottom_inject_cyl_outer_height + 3 * props.die_box_wall_thickness + props.cup_depth + props.alu_thick)')

            die_bottom_inject_cyl0 = doc.addObject('Part::MultiFuse', 'die_bottom_inject_cyl0')
            die_bottom_inject_cyl0.Label = 'die_bottom_inject_cyl0'
            die_bottom_inject_cyl0.Shapes = [die_bottom_inject_inner_cyl, die_bottom_inject_outer_cyl]
            die_bottom_inject_cyl0.setExpression('.Placement.Base.x',
                                                      u'-props.panel_width/2 + props.panel_width*' + str(
                                                          die_bottom_inject_cyl_horizontal_offset))
            die_bottom_inject_cyl0.setExpression('.Placement.Base.y',
                                                      u'-props.panel_length/2 + props.panel_length*' + str(
                                                          die_bottom_inject_cyl_vertical_offset))

            die_bottom_inject_cyl1 = doc.addObject('App::Link', 'die_bottom_inject_cyl1')
            die_bottom_inject_cyl1.setLink(die_bottom_inject_cyl0)
            die_bottom_inject_cyl1.Label = 'die_bottom_inject_cyl1'
            die_bottom_inject_cyl1.setExpression('.Placement.Base.x',
                                                      u'props.panel_width/2 - props.panel_width*' + str(
                                                          die_bottom_inject_cyl_horizontal_offset))
            die_bottom_inject_cyl1.setExpression('.Placement.Base.y',
                                                      u'props.panel_length/2 - props.panel_length*' + str(
                                                          die_bottom_inject_cyl_vertical_offset))

            die_bottom_inject_cyl = doc.addObject('Part::MultiFuse', 'die_bottom_inject_cyl')
            die_bottom_inject_cyl.Label = 'die_bottom_inject_cyl'
            die_bottom_inject_cyl.Shapes = [die_bottom_inject_cyl0, die_bottom_inject_cyl1]

            die_bottom_cut_frame_cyl = doc.addObject('Part::Cut', 'die_bottom_cut_frame_cyl')
            die_bottom_cut_frame_cyl.Label = 'die_bottom_cut_frame_cyl'
            die_bottom_cut_frame_cyl.Base = die_bottom_fillet_cut_frame
            die_bottom_cut_frame_cyl.Tool = die_bottom_inject_cyl

            die_bottom_die_frame = doc.addObject('Part::Box', 'die_bottom_die_frame')
            die_bottom_die_frame.Label = 'die_bottom_die_frame'
            die_bottom_die_frame.setExpression('Length', u'props.panel_width+2*props.die_box_wall_thickness')
            die_bottom_die_frame.setExpression('Width', u'props.panel_length+2*props.die_box_wall_thickness')
            die_bottom_die_frame.setExpression('Height', u'props.die_box_wall_thickness + props.die_bottom_inject_cyl_inner_height + props.die_bottom_bed_height')
            die_bottom_die_frame.setExpression('.Placement.Base.x',
                                               u'-(props.panel_width / 2 + props.die_box_wall_thickness)')
            die_bottom_die_frame.setExpression('.Placement.Base.y',
                                               u'-(props.panel_length / 2 + props.die_box_wall_thickness)')
            die_bottom_die_frame.setExpression('.Placement.Base.z',
                                               u'-(3*props.die_box_wall_thickness+props.cup_depth+props.alu_thick)')

            die_bottom_die = doc.addObject('Part::Cut', 'die_bottom_die')
            die_bottom_die.Label = 'die_bottom_die'
            die_bottom_die.Base = die_bottom_die_frame
            die_bottom_die.Tool = die_bottom_cut_frame_cyl
            die_bottom_die.Placement = App.Placement(App.Vector(0., 0., 0.),
                                                     App.Rotation(App.Vector(0., 1., 0.), 180.))

            die_bottom_die.setExpression('.Placement.Base.z',
                                         u'-2 * (props.cup_depth + props.alu_thick + 2 * props.die_box_wall_thickness)')

            for i, ((w_i, h_i), (x, y)) in enumerate(rect_calc.view_centers):
                istr = str(i)
                if 0 == i:
                    die_top_view_box = doc.addObject('Part::Box', 'die_top_view_box')
                    die_top_view_box_i = die_top_view_box
                    die_top_view_box.Length = scale * rect_calc.view_width
                    die_top_view_box.setExpression('Length', u'props.scale*' + str(rect_calc.view_width))
                    die_top_view_box.Width = rect_calc.view_length
                    die_top_view_box.setExpression('Width', u'props.scale*' + str(rect_calc.view_length))
                    die_top_view_box.Height = scale * (
                            sketch_view_hinge_top_z - sketch_view_hinge_bottom_z)
                    die_top_view_box.setExpression('Height', u'props.scale*' + str(
                        sketch_view_hinge_top_z - sketch_view_hinge_bottom_z))

                else:
                    die_top_view_box_i = doc.addObject('App::Link', 'die_top_view_box' + istr)
                    die_top_view_box_i.setLink(die_top_view_box)

                die_top_view_box_i.Label = 'die_top_view_box' + istr
                die_top_view_box_i.Placement = App.Placement(
                    App.Vector(x - rect_calc.view_width / 2., y - rect_calc.view_length / 2.,
                               sketch_view_hinge_bottom_z),
                    App.Rotation(App.Vector(0., 0., 1.), 0.))
                die_top_view_box_i.setExpression('.Placement.Base.x',
                                                 u'props.scale * ' + str(x - rect_calc.view_width / 2.))
                die_top_view_box_i.setExpression('.Placement.Base.y',
                                                 u'props.scale * ' + str(y - rect_calc.view_length / 2.))
                die_top_view_box_i.setExpression('.Placement.Base.z',
                                                 u'props.scale * ' + str(sketch_view_hinge_bottom_z))
                die_top_view_box_hinges_i = die_top_view_box_i

                if 0 < w_i:
                    left_hinge_i = doc.addObject('App::Link', 'left_hinge' + istr)
                    left_hinge_i.Label = 'left_hinge' + istr
                    left_hinge_i.setLink(die_top_loft_view_hinge)
                    left_hinge_i.Placement = App.Placement(
                        App.Vector(x - rect_calc.view_width / 2., y + bulb_top_x, 0.),
                        App.Rotation(App.Vector(0., 0., 1.), math.degrees(-math.pi / 2.)))
                    left_hinge_i.setExpression('.Placement.Base.x',
                                               u'props.scale * ' + str(x - rect_calc.view_width / 2.))
                    left_hinge_i.setExpression('.Placement.Base.y',
                                               u'props.scale * ' + str(y + bulb_top_x))
                    die_top_cut_hinges_i = left_hinge_i

                if h_i < rect_calc.view_chunks_y - 1:
                    top_hinge_i = doc.addObject('App::Link', 'top_hinge' + istr)
                    top_hinge_i.Label = 'top_hinge' + istr
                    top_hinge_i.setLink(die_top_loft_view_hinge)
                    top_hinge_i.Placement = App.Placement(
                        App.Vector(x + bulb_top_x, y + rect_calc.view_length / 2., 0.),
                        App.Rotation(App.Vector(0., 0., 1.), math.degrees(math.pi)))
                    top_hinge_i.setExpression('.Placement.Base.x',
                                              u'props.scale * ' + str(x + bulb_top_x))
                    top_hinge_i.setExpression('.Placement.Base.y',
                                              u'props.scale * ' + str(y + rect_calc.view_length / 2.))
                    die_top_cut_hinges_i = top_hinge_i

                if 0 < w_i and h_i < rect_calc.view_chunks_y:
                    die_top_left_top_hinges_i = doc.addObject('Part::MultiFuse', 'left_top_hinges' + istr)
                    die_top_left_top_hinges_i.Label = 'left_top_hinges' + istr
                    die_top_left_top_hinges_i.Shapes = [left_hinge_i, top_hinge_i]
                    die_top_cut_hinges_i = die_top_left_top_hinges_i

                if 0 < w_i or h_i < rect_calc.view_chunks_y:
                    die_top_view_box_hinges_i = doc.addObject('Part::Cut', 'die_top_view_box_cut' + istr)
                    die_top_view_box_hinges_i.Label = 'die_top_view_box_cut' + istr
                    die_top_view_box_hinges_i.Base = die_top_view_box_i
                    die_top_view_box_hinges_i.Tool = die_top_cut_hinges_i

                die_top_right_bottom = [die_top_view_box_hinges_i]

                if w_i < rect_calc.view_chunks_x - 1:
                    die_top_right_hinge_i = doc.addObject('App::Link', 'die_top_right_hinge' + istr)
                    die_top_right_hinge_i.Label = 'die_top_right_hinge' + istr
                    die_top_right_hinge_i.setLink(die_top_loft_view_hinge)
                    die_top_right_hinge_i.Placement = App.Placement(
                        App.Vector(x + rect_calc.view_width / 2., y + bulb_top_x, 0.),
                        App.Rotation(App.Vector(0., 0., 1.), math.degrees(-math.pi / 2.)))
                    die_top_right_hinge_i.setExpression('.Placement.Base.x',
                                                        u'props.scale * ' + str(x + rect_calc.view_width / 2.))
                    die_top_right_hinge_i.setExpression('.Placement.Base.y',
                                                        u'props.scale * ' + str(y + bulb_top_x))
                    die_top_right_bottom.append(die_top_right_hinge_i)

                if 0 < h_i:
                    die_top_bottom_hinge_i = doc.addObject('App::Link', 'die_top_bottom_hinge' + istr)
                    die_top_bottom_hinge_i.Label = 'die_top_bottom_hinge' + istr
                    die_top_bottom_hinge_i.setLink(die_top_loft_view_hinge)
                    die_top_bottom_hinge_i.Placement = App.Placement(
                        App.Vector(x + bulb_top_x, y - rect_calc.view_length / 2., 0.),
                        App.Rotation(App.Vector(0., 0., 1.), math.degrees(math.pi)))
                    die_top_bottom_hinge_i.setExpression('.Placement.Base.x',
                                                         u'props.scale * ' + str(x + bulb_top_x))
                    die_top_bottom_hinge_i.setExpression('.Placement.Base.y',
                                                         u'props.scale * ' + str(y - rect_calc.view_length / 2.))
                    die_top_right_bottom.append(die_top_bottom_hinge_i)

                if w_i < rect_calc.view_chunks_x - 1 or 0 < h_i:
                    die_top_view_box_hinges_i = doc.addObject('Part::MultiFuse', 'die_top_view_box_hinges' + istr)
                    die_top_view_box_hinges_i.Label = 'die_top_view_box_hinges' + istr
                    die_top_view_box_hinges_i.Shapes = die_top_right_bottom

                die_top_view_box_hinges_i.Label = 'die_top_view_box_hinges' + istr
                die_top_view_box_hinges_i.Visibility = False

                die_top_view_i = doc.addObject('Part::MultiCommon', 'die_top_view' + istr)
                die_top_view_i.Shapes = [die_top_die, die_top_view_box_hinges_i]

                # bottom die
                die_bottom_view_box_hinges_i = doc.addObject('App::Link', 'die_bottom_view_box_hinges' + istr)
                die_bottom_view_box_hinges_i.Label = 'die_bottom_view_box_hinges' + istr
                die_bottom_view_box_hinges_i.setLink(die_top_view_box_hinges_i)
                die_bottom_view_box_hinges_i.setExpression('.Placement.Base.z',
                                                           u'-(props.die_box_wall_thickness + props.alu_thick + props.die_bottom_inject_cyl_inner_height + props.die_bottom_inject_cyl_outer_height)')

                die_bottom_view_i = doc.addObject('Part::MultiCommon', 'die_bottom_view' + istr)
                die_bottom_view_i.Shapes = [die_bottom_die, die_bottom_view_box_hinges_i]

        doc.recompute()

        return doc, pressing


def create_sketch_view_hinge(body_view_hinge, rad: float, label: str, x: float = 0., z: float = 0.):
    name = 'sketch_view_hinge_' + label
    sketch_view_hinge = body_view_hinge.newObject('Sketcher::SketchObject', name)
    sketch_view_hinge.Label = name
    sketch_view_hinge.Visibility = False
    sketch_view_hinge.Support = (body_view_hinge.Origin.OriginFeatures[3], [''])
    sketch_view_hinge.MapMode = 'FlatFace'
    sketch_view_hinge.addGeometry(
        Part.ArcOfCircle(Part.Circle(App.Vector(0., rad, 0), App.Vector(0, 0, 1), rad), -math.pi / 2.,
                         math.pi / 6.), False)
    sketch_view_hinge.addConstraint(Sketcher.Constraint('PointOnObject', 0, 3, -2))
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Angle', 0, math.pi * 2. / 3.))
    c4 = sketch_view_hinge.addConstraint(Sketcher.Constraint('DistanceY', 0, 1, 0, 3, rad))
    sketch_view_hinge.setExpression('Constraints[' + str(c4) + ']', u'props.scale * ' + str(rad))
    top_bulb_x = 2. * rad * math.cos(math.pi / 6.)
    top_bulb_y = rad + 2. * rad * math.sin(math.pi / 6.)
    sketch_view_hinge.addGeometry(
        Part.ArcOfCircle(Part.Circle(App.Vector(top_bulb_x, top_bulb_y, 0), App.Vector(0, 0, 1), rad),
                         math.pi * 11. / 6.,
                         math.pi * 7. / 6.), False)
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Tangent', 1, 2, 0, 2))
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Angle', 1, math.pi * 4. / 3.))
    c7 = sketch_view_hinge.addConstraint(Sketcher.Constraint('Distance', 1, 3, 0, 2, rad))
    sketch_view_hinge.setExpression('Constraints[' + str(c7) + ']', u'props.scale * ' + str(rad))
    sketch_view_hinge.addGeometry(
        Part.ArcOfCircle(Part.Circle(App.Vector(2. * top_bulb_x, rad, 0), App.Vector(0, 0, 1), rad), math.pi * 5. / 6.,
                         math.pi * 3. / 2.), False)
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Tangent', 2, 1, 1, 1))
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Angle', 2, math.pi * 2. / 3.))
    c10 = sketch_view_hinge.addConstraint(Sketcher.Constraint('DistanceY', 2, 2, 2, 3, rad))
    sketch_view_hinge.setExpression('Constraints[' + str(c10) + ']', u'props.scale * ' + str(rad))

    sketch_view_hinge.addGeometry(Part.LineSegment(App.Vector(0., 0., 0.), App.Vector(2. * top_bulb_x, 0., 0.)), False)
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Coincident', 3, 1, 0, 1))
    sketch_view_hinge.addConstraint(Sketcher.Constraint('Coincident', 3, 2, 2, 2))

    sketch_view_hinge.AttachmentOffset = App.Placement(App.Vector(x, 0., z), App.Rotation(App.Vector(0., 0., 1.), 0.))
    sketch_view_hinge.setExpression('.AttachmentOffset.Base.x', u'props.scale*' + str(x))
    sketch_view_hinge.setExpression('.AttachmentOffset.Base.z', u'props.scale*' + str(z))

    return sketch_view_hinge, top_bulb_x


def add_view_box(doc: Document, pressing: Feature):
    view_box = doc.addObject('Part::Box', 'view_box')
    view_box.Label = 'view_box'
    view_box.setExpression('Length', u'props.print_view')
    view_box.setExpression('Width', u'props.print_view')
    view_box.setExpression('Height', u'props.print_view')
    view_box.setExpression('.Placement.Base.z', u'-props.print_view / 2')
    view_box.setExpression('.Placement.Base.x', u'-props.panel_width / 2 + props.print_x * props.print_view')
    view_box.setExpression('.Placement.Base.y', u'-props.panel_length / 2 + props.print_y * props.print_view')

    view_cut = doc.addObject('Part::MultiCommon', 'view_cut')
    view_cut.Shapes = [view_box, pressing]
    view_cut.Placement = App.Placement(App.Vector(0., 0., 0.), App.Rotation(App.Vector(0., 1., 0.), 180.))


def create(float_input: RectFloatInput = RectFloatInput()) -> RectFreecadModel:
    return RectFreecadModel(rectfloatmodel.create(float_input))
