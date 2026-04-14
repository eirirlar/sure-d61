import FreeCAD as App
import Draft
import Part
import Sketcher
import Mesh
import os

import hexfloatinput
import shouldercalc
import floatinput
import hexfloatmodel
from hexfloatmodel import HexFloatModel
from hexfloatinput import HexFloatInput
import math
from stl2img import stl2img
from util import filename_output_genetic


class HexFreecadModel:

    def __init__(self,
                 float_model: HexFloatModel
                 ):
        self.float_model = float_model

    # General note on default vs userprovided values.
    # First we use defaults to get the constraints right.
    # Then we set up constraints pointing to parameter on the model
    # Then we update the parameter on the model with the user provided value
    def generate(self, fc=True, stp=True, stl=True, img=True, filename='thepressing'):
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

        fi = self.float_model.float_input
        cup_rad_default = floatinput.cup_rad_default
        cup_lip_default = floatinput.cup_lip_default
        cup_depth_default = floatinput.cup_depth_default
        alu_thick_default = floatinput.alu_thick_default
        shoulder_angle_default = hexfloatinput.shoulder_angle_default

        cup_rad = fi.cup_rad
        cup_lip = fi.cup_lip
        cup_depth = fi.cup_depth
        cup_angle = fi.cup_angle
        alu_thick = fi.alu_thick
        shoulder_angle = fi.shoulder_angle
        side = fi.side
        hex_calc = self.float_model.hex_calc
        cc = self.float_model.cup_calc
        cup_ellipsoid_x = cc.cup_ellipsoid_x
        cup_ellipsoid_y = cc.cup_ellipsoid_y
        cup_depth_ellipsoid = cc.cup_depth_ellipsoid

        sinPiDiv3 = math.sin(math.pi / 3)

        shoulder_calc_default = shouldercalc.calc_shoulder(HexFloatInput())
        shoulder_calc = self.float_model.shoulder_calc

        side_diff = side - hex_calc.cup_max_x - shoulder_calc.edge
        plate_fillet_rad = side_diff * sinPiDiv3

        doc = App.newDocument(filename)

        pressing = doc.addObject('App::Part', 'pressing')
        pressing.Visibility = True
        pressing.Label = 'pressing'

        # original cup with sketch
        cups = doc.addObject('App::DocumentObjectGroup', 'cups')
        cups.Visibility = False
        cups.Label = 'cups'
        cups.adjustRelativeLinks(cups)
        pressing.addObject(cups)

        cup_ellipsoid = doc.addObject('Part::Ellipsoid', 'cup_ellipsoid')
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
        cup_ellipsoid.Angle1 = -90
        cup_ellipsoid.Angle2 = -cup_angle
        cup_ellipsoid.Angle3 = 360
        cup_ellipsoid.Placement = App.Placement(App.Vector(0, 0, cup_depth),
                                                App.Rotation(App.Vector(0, 0, 0), 0))
        cup_ellipsoid.setExpression('.Placement.Base.z', u'cup_depth_ellipsoid')
        cup_ellipsoid.Label = 'cup_ellipsoid'
        cup_ellipsoid.Visibility = False

        cup_cyl = doc.addObject('Part::Cylinder', 'cup_cyl')
        cup_cyl.Label = 'cup_cyl'
        cup_cyl.addProperty('App::PropertyFloat', 'cup_rad')
        cup_cyl.cup_rad = cup_rad
        cup_cyl.addProperty('App::PropertyFloat', 'cup_depth')
        cup_cyl.cup_depth = cup_depth
        cup_cyl.Radius = cup_rad
        cup_cyl.setExpression('Radius', u'cup_rad')
        cup_cyl.Height = cup_depth
        cup_cyl.setExpression('Height', u'cup_depth')
        cup_cyl.Visibility = False

        cup_cyl_ellipsoid = doc.addObject('Part::Cut', 'cup_cyl_ellipsoid')
        cup_cyl_ellipsoid.Base = cup_cyl
        cup_cyl_ellipsoid.Tool = cup_ellipsoid
        cup_cyl_ellipsoid.Visibility = False

        cup_fillet = doc.addObject('Part::Fillet', 'cup_fillet')
        cup_fillet.addProperty('App::PropertyFloat', 'cup_lip')
        cup_fillet.cup_lip = cup_lip
        cup_fillet.Base = cup_cyl_ellipsoid
        cup_fillets = []
        cup_fillets.append((4, cup_lip, cup_lip))
        cup_fillet.Edges = cup_fillets
        del cup_fillets
        cup_fillet.Visibility = False

        cup_whole = doc.addObject('Part::Cut', 'cup_whole')
        cup_whole.Base = cup_cyl
        cup_whole.Tool = cup_fillet
        cup_whole.Visibility = False

        doc.recompute()
        cup_around_fillet_facebinder = Draft.make_facebinder([(cup_fillet, 'Face1')], 'cup_around_fillet_facebinder')
        cup_around_fillet_extrude = doc.addObject('Part::Extrusion', 'cup_around_fillet_extrude')
        cup_around_fillet_extrude.addProperty('App::PropertyFloat', 'alu_thick')
        cup_around_fillet_extrude.alu_thick = alu_thick
        cup_around_fillet_extrude.Base = cup_around_fillet_facebinder
        cup_around_fillet_extrude.LengthFwd = alu_thick
        cup_around_fillet_extrude.setExpression('LengthFwd', u'alu_thick')
        cup_around_fillet_facebinder.Visibility = False

        cup_facebinder = Draft.make_facebinder([(cup_whole, 'Face1')], 'cup_facebinder')
        cup_facebinder.Visibility = False
        cup_top_extrude = doc.addObject('Part::Extrusion', 'cup_top_extrude')
        cup_top_extrude.addProperty('App::PropertyFloat', 'alu_thick')
        cup_top_extrude.alu_thick = alu_thick
        cup_top_extrude.Base = cup_facebinder
        cup_top_extrude.LengthFwd = alu_thick
        cup_top_extrude.setExpression('LengthFwd', u'alu_thick')
        cup_top_extrude.Visibility = False

        cup_whole_extrude = doc.addObject('Part::Fuse', 'cup_whole_extrude')
        cup_whole_extrude.Base = cup_whole
        cup_whole_extrude.Tool = cup_top_extrude
        cup_whole_extrude.Visibility = False

        cup_whole_clone = doc.addObject('PartDesign::FeatureBase', 'cup_whole_clone')
        cup_whole_clone.BaseFeature = cup_whole
        cup_whole_clone.Placement = cup_whole.Placement
        cup_whole_clone.setEditorMode('Placement', 0)
        cup_whole_clone.Visibility = False

        cup_whole_shiftup = doc.addObject('PartDesign::Body', 'cup_whole_shiftup')
        cup_whole_shiftup.addProperty('App::PropertyFloat', 'alu_thick')
        cup_whole_shiftup.alu_thick = alu_thick
        cup_whole_shiftup.Group = [cup_whole_clone]
        cup_whole_shiftup.Tip = cup_whole_clone
        cup_whole_shiftup.Placement = App.Placement(App.Vector(0, 0, alu_thick), App.Rotation(App.Vector(0, 0, 1), 0))
        cup_whole_shiftup.setExpression('.Placement.Base.z', u'alu_thick')
        cup_whole_shiftup.Visibility = False

        cup_extruded = doc.addObject('Part::Cut', 'cup_extruded')
        cup_extruded.Base = cup_whole_extrude
        cup_extruded.Tool = cup_whole_shiftup
        cup_extruded.Visibility = False

        cup0 = doc.addObject('Part::Fuse', 'cup0')
        cup0.Visibility = True
        cup0.Base = cup_around_fillet_extrude
        cup0.Tool = cup_extruded
        cup0.adjustRelativeLinks(cups)
        cups.addObject(cup0)

        plate = doc.addObject('PartDesign::Body', 'plate')
        plate.Visibility = True
        plate.Origin.Label = 'plate_orig'
        plate.adjustRelativeLinks(pressing)
        pressing.addObject(plate)

        plate_sketch = plate.newObject('Sketcher::SketchObject', 'plate_sketch')
        plate_sketch.Visibility = False
        plate_sketch.Support = (plate.Origin.OriginFeatures[3], [''])
        plate_sketch.MapMode = 'FlatFace'
        plate_sketch.addProperty('App::PropertyFloat', 'inner_side')
        plate_sketch.inner_side = hex_calc.inner_side
        plate_sketch.addProperty('App::PropertyFloat', 'cup_depth')
        plate_sketch.cup_depth = cup_depth
        plate_sketch.addProperty('App::PropertyFloat', 'alu_thick')
        plate_sketch.alu_thick = alu_thick
        plate_sketch.addProperty('App::PropertyFloat', 'cup_max_x')
        plate_sketch.cup_max_x = hex_calc.cup_max_x
        plate_sketch.addProperty('App::PropertyFloat', 'cup_max_y')
        plate_sketch.cup_max_y = hex_calc.cup_max_y

        plate.Placement = App.Placement(App.Vector(0, 0, cup_depth + alu_thick), App.Rotation(App.Vector(0, 0, 1), 0))
        plate.setExpression('.Placement.Base.z', u'<<plate_sketch>>.cup_depth + <<plate_sketch>>.alu_thick')

        for i in range(0, 6):
            angle_rad_first = math.pi / 3 * i
            angle_rad_second = math.pi / 3 * (i + 1)
            corner_cup_first_x = hex_calc.cup_max_x * math.cos(angle_rad_first)
            corner_cup_first_y = hex_calc.cup_max_x * math.sin(angle_rad_first)
            corner_cup_second_x = hex_calc.cup_max_x * math.cos(angle_rad_second)
            corner_cup_second_y = hex_calc.cup_max_x * math.sin(angle_rad_second)
            corner_edge_first_x = corner_cup_first_x + plate_fillet_rad * math.cos(angle_rad_first + math.pi / 6)
            corner_edge_first_y = corner_cup_first_y + plate_fillet_rad * math.sin(angle_rad_first + math.pi / 6)
            corner_edge_second_x = corner_cup_second_x + plate_fillet_rad * math.cos(angle_rad_second - math.pi / 6)
            corner_edge_second_y = corner_cup_second_y + plate_fillet_rad * math.sin(angle_rad_second - math.pi / 6)
            plate_sketch.addGeometry(
                Part.ArcOfCircle(Part.Circle(App.Vector(corner_cup_first_x, corner_cup_first_y, 0), App.Vector(0, 0, 1),
                                             plate_fillet_rad),
                                 angle_rad_first - math.pi / 6, angle_rad_first + math.pi / 6), False)
            plate_sketch.addGeometry(
                Part.LineSegment(App.Vector(corner_edge_first_x, corner_edge_first_y, 0),
                                 App.Vector(corner_edge_second_x, corner_edge_second_y, 0)), False)
            plate_sketch.addConstraint(Sketcher.Constraint('Tangent', 2 * i, 2, 2 * i + 1, 1))
            if 0 < i:
                plate_sketch.addConstraint(Sketcher.Constraint('Tangent', 2 * i - 1, 2, 2 * i, 1))
            if 5 == i:
                plate_sketch.addConstraint(Sketcher.Constraint('Tangent', 2 * i + 1, 2, 0, 1))
            plate_sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 2 * i, 3, corner_cup_first_x))
            plate_sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 2 * i, 3, corner_cup_first_y))
            if 0 == i:
                plate_sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 2 * i, 2, corner_edge_first_x))
                plate_sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 2 * i, 2, corner_edge_first_y))
            if i < 4:
                plate_sketch.addConstraint(Sketcher.Constraint('Angle', 2 * i, math.pi / 3))

        # cups and holes in plate
        i = 0
        for x, y in hex_calc.cup_points:
            if 0 != x or 0 != y:
                i += 1
                istr = str(i)
                cup_c = doc.addObject('App::Link', 'cup' + istr)
                cup_c.setLink(cup0)
                cup_c.adjustRelativeLinks(cups)
                cups.addObject(cup_c)
                cup_c.Placement = App.Placement(App.Vector(x, y, 0), App.Rotation(App.Vector(0, 0, 1), 0))
                cup_c.Visibility = True
            plate_sketch.addGeometry(Part.Circle(App.Vector(x, y, 0), App.Vector(0, 0, 1), cup_rad), False)
            plate_sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, plate_sketch.GeometryCount - 1, 3, x))
            plate_sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, plate_sketch.GeometryCount - 1, 3, y))
            plate_sketch.addConstraint(Sketcher.Constraint('Radius', plate_sketch.GeometryCount - 1, cup_rad))

        # plate thickness
        plate_pad = plate.newObject('PartDesign::Pad', 'plate_pad')
        plate_pad.Visibility = True
        plate_pad.Profile = plate_sketch
        plate_pad.Length = alu_thick
        plate_pad.ReferenceAxis = (plate_sketch, ['N_Axis'])
        plate_pad.Reversed = 1

        # shoulders group
        shoulders = doc.addObject('App::DocumentObjectGroup', 'shoulders')
        shoulders.Visibility = False
        shoulders.Label = 'shoulders'
        shoulders.adjustRelativeLinks(pressing)
        pressing.addObject(shoulders)

        # shoulder
        shoulder0 = doc.addObject('PartDesign::Body', 'shoulder0')
        shoulder0.Visibility = True
        shoulder0.Origin.Label = 'shoulder_orig'
        shoulder0.adjustRelativeLinks(shoulders)
        shoulders.addObject(shoulder0)
        shoulder_sketch = shoulder0.newObject('Sketcher::SketchObject', 'shoulder_sketch')
        shoulder_sketch.Support = (shoulder0.Origin.OriginFeatures[5], [''])
        shoulder_sketch.MapMode = 'FlatFace'

        shoulder_sketch.addProperty('App::PropertyFloat', 'inner_side')
        shoulder_sketch.inner_side = hex_calc.inner_side
        shoulder_sketch.addProperty('App::PropertyFloat', 'cup_rad')
        shoulder_sketch.cup_rad = cup_rad_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'cup_depth')
        shoulder_sketch.cup_depth = cup_depth_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'cup_lip')
        shoulder_sketch.cup_lip = cup_lip_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'alu_thick')
        shoulder_sketch.alu_thick = alu_thick_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'shoulder_width')
        shoulder_sketch.shoulder_width = hexfloatinput.shoulder_width_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'shoulder_depth')
        shoulder_sketch.shoulder_depth = hexfloatinput.shoulder_depth_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'float_lip')
        shoulder_sketch.float_lip = hexfloatinput.float_lip_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'shoulder_angle')
        shoulder_sketch.shoulder_angle = shoulder_angle_default
        shoulder_sketch.addProperty('App::PropertyFloat', 'cup_max_x')
        shoulder_sketch.cup_max_x = hex_calc.cup_max_x
        shoulder_sketch.addProperty('App::PropertyFloat', 'cup_max_y')
        shoulder_sketch.cup_max_y = hex_calc.cup_max_y

        shoulder0.Placement = App.Placement(App.Vector(hex_calc.cup_max_x / 2, hex_calc.cup_max_y, 0),
                                            App.Rotation(App.Vector(0, 0, 1), 0))
        shoulder0.setExpression('.Placement.Base.x', u'<<shoulder_sketch>>.cup_max_x / 2')
        shoulder0.setExpression('.Placement.Base.y', u'<<shoulder_sketch>>.cup_max_y')

        shoulder_sketch.AttachmentOffset = App.Placement(
            App.Vector(hex_calc.inner_side * sinPiDiv3 - hex_calc.cup_max_y, 0, 0),
            App.Rotation(App.Vector(1, 0, 0), 0))
        shoulder_sketch.setExpression('.AttachmentOffset.Base.x', u'inner_side * sin(60) - cup_max_y')

        # leftmost part of sketch, alu_thick height, meets with plate
        shoulder_inner_edge_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(0, cup_depth_default + alu_thick_default, 0),
                             App.Vector(0, cup_depth_default, 0)), False)

        # first small arc down from plate
        shoulder_first_arc_upper_id = shoulder_sketch.addGeometry(Part.ArcOfCircle(
            Part.Circle(App.Vector(0, cup_depth_default - alu_thick_default / 2, 0),
                        App.Vector(0, 0, 1), shoulder_calc_default.large_arc_radius),
            shoulder_calc_default.angle_inv_rad,
            math.pi / 2), False)
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, 1, 2))
        shoulder_first_arc_lower_id = shoulder_sketch.addGeometry(Part.ArcOfCircle(
            Part.Circle(App.Vector(0, cup_depth_default - alu_thick_default / 2, 0),
                        App.Vector(0, 0, 1), alu_thick_default / 2), shoulder_calc_default.angle_inv_rad,
            math.pi / 2), False)
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 2, 2))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Vertical', 1, 3, -1, 1))

        # first short drop, straight line with angle shoulder_angle
        shoulder_short_drop_upper_id = shoulder_sketch.addGeometry(
            Part.LineSegment(
                App.Vector(shoulder_calc_default.large_arc_x,
                           cup_depth_default + alu_thick_default - shoulder_calc_default.large_arc_y, 0),
                App.Vector(shoulder_calc_default.large_arc_x + shoulder_calc_default.short_drop_x,
                           cup_depth_default + alu_thick_default - hexfloatinput.shoulder_depth_default + shoulder_calc_default.small_arc_y,
                           0)),
            False)

        shoulder_short_drop_lower_id = shoulder_sketch.addGeometry(
            Part.LineSegment(
                App.Vector(shoulder_calc_default.first_lower_arc_end_x,
                           shoulder_calc_default.first_lower_arc_end_y, 0),
                App.Vector(shoulder_calc_default.short_drop_end_x,
                           shoulder_calc_default.short_drop_end_y, 0)),
            False)
        shoulder_sketch.addConstraint(Sketcher.Constraint('Tangent', 1, 1, shoulder_short_drop_upper_id, 1))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Tangent', 2, 1, shoulder_short_drop_lower_id, 1))

        # bottom of first drop, bend into top of shoulder
        shoulder_second_arc_upper_id = shoulder_sketch.addGeometry(
            Part.ArcOfCircle(
                Part.Circle(
                    App.Vector(shoulder_calc_default.second_arc_center_x,
                               shoulder_calc_default.second_arc_center_y, 0),
                    App.Vector(0, 0, 1), alu_thick_default / 2), shoulder_calc_default.angle_3q_rad,
                math.pi * 3 / 2), False)
        shoulder_second_arc_lower_id = shoulder_sketch.addGeometry(
            Part.ArcOfCircle(Part.Circle(
                App.Vector(shoulder_calc_default.second_arc_center_x,
                           shoulder_calc_default.second_arc_center_y, 0),
                App.Vector(0, 0, 1), shoulder_calc_default.large_arc_radius), shoulder_calc_default.angle_3q_rad,
                math.pi * 3 / 2), False)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_short_drop_upper_id, 2, shoulder_second_arc_upper_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_short_drop_lower_id, 2, shoulder_second_arc_lower_id, 1))

        # long straight line ca shoulder_width
        shoulder_long_drop_upper_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(shoulder_calc_default.second_arc_center_x,
                                        shoulder_calc_default.second_upper_arc_end_y, 0),
                             App.Vector(shoulder_calc_default.third_arc_center_x,
                                        shoulder_calc_default.second_upper_arc_end_y, 0)), False)
        shoulder_long_drop_lower_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(shoulder_calc_default.second_arc_center_x,
                                        shoulder_calc_default.second_lower_arc_end_y, 0),
                             App.Vector(shoulder_calc_default.third_arc_center_x,
                                        shoulder_calc_default.second_lower_arc_end_y, 0)), False)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_second_arc_upper_id, 2, shoulder_long_drop_upper_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_second_arc_lower_id, 2, shoulder_long_drop_lower_id, 1))

        # bend down from shoulder
        shoulder_third_arc_upper_id = shoulder_sketch.addGeometry(
            Part.ArcOfCircle(Part.Circle(
                App.Vector(shoulder_calc_default.third_arc_center_x,
                           shoulder_calc_default.third_arc_center_y, 0),
                App.Vector(0, 0, 1), shoulder_calc_default.large_arc_radius), shoulder_calc_default.angle_inv_rad,
                math.pi / 2), False)
        shoulder_third_arc_lower_id = shoulder_sketch.addGeometry(
            Part.ArcOfCircle(Part.Circle(
                App.Vector(shoulder_calc_default.third_arc_center_x,
                           shoulder_calc_default.third_arc_center_y, 0),
                App.Vector(0, 0, 1), alu_thick_default / 2), shoulder_calc_default.angle_inv_rad,
                math.pi / 2), False)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_long_drop_upper_id, 2, shoulder_third_arc_upper_id, 2))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_long_drop_lower_id, 2, shoulder_third_arc_lower_id, 2))

        # long drop down from shoulder, straight line
        shoulder_long_drop_upper_id = shoulder_sketch.addGeometry(
            Part.LineSegment(
                App.Vector(shoulder_calc_default.long_drop_upper_start_x,
                           shoulder_calc_default.long_drop_upper_start_y,
                           0),
                App.Vector(
                    shoulder_calc_default.long_drop_upper_end_x,
                    shoulder_calc_default.long_drop_upper_end_y, 0)), False)
        shoulder_long_drop_lower_id = shoulder_sketch.addGeometry(
            Part.LineSegment(
                App.Vector(shoulder_calc_default.long_drop_lower_start_x,
                           shoulder_calc_default.long_drop_lower_start_y, 0),
                App.Vector(
                    shoulder_calc_default.long_drop_lower_end_x,
                    shoulder_calc_default.large_arc_y, 0)), False)

        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_third_arc_upper_id, 1, shoulder_long_drop_upper_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_third_arc_lower_id, 1, shoulder_long_drop_lower_id, 1))

        # bend from long drop onto flat lower part of shoulder
        shoulder_forth_arc_upper_id = shoulder_sketch.addGeometry(
            Part.ArcOfCircle(Part.Circle(App.Vector(
                shoulder_calc_default.forth_arc_center_x,
                shoulder_calc_default.large_arc_radius, 0), App.Vector(0, 0, 1), alu_thick_default / 2),
                shoulder_calc_default.angle_3q_rad,
                math.pi * 3 / 2), False)
        shoulder_forth_arc_lower_id = shoulder_sketch.addGeometry(
            Part.ArcOfCircle(Part.Circle(App.Vector(
                shoulder_calc_default.forth_arc_center_x,
                shoulder_calc_default.large_arc_radius, 0), App.Vector(0, 0, 1),
                shoulder_calc_default.large_arc_radius),
                shoulder_calc_default.angle_3q_rad,
                math.pi * 3 / 2), False)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_long_drop_upper_id, 2, shoulder_forth_arc_upper_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_long_drop_lower_id, 2, shoulder_forth_arc_lower_id, 1))

        # the lip of the pressing, straight line float_lip long
        shoulder_float_lip_upper_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(
                shoulder_calc_default.forth_arc_center_x,
                alu_thick_default, 0), App.Vector(
                shoulder_calc_default.float_lip_end_x,
                alu_thick_default,
                0)), False)
        shoulder_float_lip_lower_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(
                shoulder_calc_default.forth_arc_center_x,
                0, 0), App.Vector(
                shoulder_calc_default.float_lip_end_x,
                0, 0)), False)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_forth_arc_upper_id, 2, shoulder_float_lip_upper_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Tangent', shoulder_forth_arc_lower_id, 2, shoulder_float_lip_lower_id, 1))

        # pressing lip vertical edge
        shoulder_float_lip_edge_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(
                shoulder_calc_default.float_lip_end_x,
                alu_thick_default, 0), App.Vector(
                shoulder_calc_default.float_lip_end_x,
                0, 0)), False)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_float_lip_edge_id, 1, shoulder_float_lip_upper_id, 2))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_float_lip_edge_id, 2, shoulder_float_lip_lower_id, 2))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Vertical', shoulder_float_lip_edge_id))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 3, 2, 3))
        shoulder_con0 = shoulder_sketch.addConstraint(Sketcher.Constraint('DistanceY', 0, 2, 0, 1, alu_thick_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con0) + ']', u'alu_thick')
        shoulder_sketch.addConstraint(Sketcher.Constraint('Vertical', 0, 2, 1, 3))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Vertical', 0, 2, 0, 1))
        shoulder_con1 = shoulder_sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 0, 2, cup_depth_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con1) + ']', u'cup_depth')

        # shoulder short drop support line
        shoulder_short_drop_support_left_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(0, cup_depth_default - alu_thick_default / 2, 0),
                             App.Vector(shoulder_calc_default.small_arc_x,
                                        cup_depth_default - shoulder_calc_default.small_arc_y,
                                        0)),
            True)
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', shoulder_short_drop_support_left_id, 1, 1, 3))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', shoulder_short_drop_support_left_id, 2, 2, 1))
        shoulder_short_drop_support_right_id = shoulder_sketch.addGeometry(
            Part.LineSegment(
                App.Vector(shoulder_calc_default.small_arc_x, cup_depth_default - shoulder_calc_default.small_arc_y, 0),
                App.Vector(shoulder_calc_default.large_arc_x,
                           cup_depth_default + alu_thick_default - shoulder_calc_default.large_arc_y, 0)),
            True)
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', shoulder_short_drop_support_right_id, 2, 1, 1))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Coincident', shoulder_short_drop_support_right_id, 1, 2, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Parallel', shoulder_short_drop_support_right_id, shoulder_short_drop_support_left_id))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_second_arc_upper_id, 3, shoulder_second_arc_lower_id, 3))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Vertical', shoulder_second_arc_upper_id, 3, shoulder_second_arc_upper_id, 2))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Vertical', shoulder_second_arc_upper_id, 2, shoulder_second_arc_lower_id, 2))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_third_arc_upper_id, 3, shoulder_third_arc_lower_id, 3))
        shoulder_long_drop_support_left_id = shoulder_sketch.addGeometry(
            Part.LineSegment(App.Vector(shoulder_calc_default.third_arc_center_x,
                                        shoulder_calc_default.third_arc_center_y, 0),
                             App.Vector(
                                 shoulder_calc_default.long_drop_lower_start_x,
                                 shoulder_calc_default.long_drop_lower_start_y, 0)), True)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_long_drop_support_left_id, 1, shoulder_third_arc_upper_id, 3))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_long_drop_support_left_id, 2, shoulder_third_arc_lower_id, 1))
        shoulder_long_drop_support_right_id = shoulder_sketch.addGeometry(
            Part.LineSegment(
                App.Vector(shoulder_calc_default.long_drop_lower_start_x,
                           shoulder_calc_default.long_drop_lower_start_y, 0),
                App.Vector(shoulder_calc_default.long_drop_upper_start_x,
                           shoulder_calc_default.long_drop_upper_start_y,
                           0)), True)
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_long_drop_support_right_id, 1, shoulder_third_arc_lower_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_long_drop_support_right_id, 2, shoulder_third_arc_upper_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Parallel', shoulder_long_drop_support_left_id, shoulder_long_drop_support_right_id))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Coincident', shoulder_forth_arc_lower_id, 3, shoulder_forth_arc_upper_id, 3))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Vertical', shoulder_forth_arc_upper_id, 3, shoulder_forth_arc_lower_id, 2))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Vertical', shoulder_forth_arc_lower_id, 2, shoulder_forth_arc_upper_id, 2))
        shoulder_sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, shoulder_float_lip_lower_id, 2, 0))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Parallel', 7, 8))
        shoulder_sketch.addConstraint(Sketcher.Constraint('Equal', shoulder_second_arc_lower_id, 1))
        shoulder_sketch.addConstraint(
            Sketcher.Constraint('Equal', shoulder_third_arc_lower_id, shoulder_forth_arc_upper_id))
        shoulder_con2 = shoulder_sketch.addConstraint(
            Sketcher.Constraint('DistanceY', shoulder_second_arc_upper_id, 2, 0, 1, hexfloatinput.shoulder_depth_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con2) + ']', u'shoulder_depth')
        shoulder_con3 = shoulder_sketch.addConstraint(
            Sketcher.Constraint('DistanceX', 3, 2, 7, 2, hexfloatinput.shoulder_width_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con3) + ']', u'shoulder_width')
        shoulder_con4 = shoulder_sketch.addConstraint(
            Sketcher.Constraint('DistanceX', shoulder_forth_arc_upper_id, 2, shoulder_float_lip_upper_id, 2,
                                hexfloatinput.float_lip_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con4) + ']', u'float_lip')
        shoulder_con5 = shoulder_sketch.addConstraint(
            Sketcher.Constraint('Angle', shoulder_long_drop_lower_id, shoulder_angle_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con5) + ']', u'shoulder_angle')
        shoulder_con6 = shoulder_sketch.addConstraint(Sketcher.Constraint('Angle', 3, shoulder_angle_default))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con6) + ']', u'shoulder_angle')
        shoulder_con7 = shoulder_sketch.addConstraint(
            Sketcher.Constraint('DistanceY', 1, 3, 0, 2, alu_thick_default / 2))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con7) + ']', u'alu_thick / 2')
        shoulder_con8 = shoulder_sketch.addConstraint(
            Sketcher.Constraint('DistanceY', shoulder_third_arc_upper_id, 3, 8, 2, alu_thick_default / 2))
        shoulder_sketch.setExpression('Constraints[' + str(shoulder_con8) + ']', u'alu_thick / 2')

        shoulder_sketch.cup_rad = cup_rad
        shoulder_sketch.cup_depth = cup_depth
        shoulder_sketch.cup_lip = cup_lip
        shoulder_sketch.alu_thick = alu_thick
        shoulder_sketch.shoulder_width = fi.shoulder_width
        shoulder_sketch.shoulder_depth = fi.shoulder_depth
        shoulder_sketch.float_lip = fi.float_lip
        shoulder_sketch.shoulder_angle = shoulder_angle

        shoulder_pad = shoulder0.newObject('PartDesign::Pad', 'shoulder_pad')
        shoulder_pad.Visibility = True
        shoulder_pad.Profile = shoulder_sketch
        shoulder_pad.Length = hex_calc.cup_max_x
        shoulder_pad.ReferenceAxis = (shoulder_sketch, ['N_Axis'])
        shoulder_pad.setExpression('Length', u'<<shoulder_sketch>>.cup_max_x')
        shoulder_pad.TaperAngle = 0
        shoulder_pad.UseCustomVector = 0
        shoulder_pad.Direction = (1, -0, 0)
        shoulder_pad.AlongSketchNormal = 1
        shoulder_pad.Type = 0
        shoulder_pad.UpToFace = None
        shoulder_pad.Reversed = 1
        shoulder_pad.Midplane = 0
        shoulder_pad.Offset = 0

        shoulder_rev = shoulder0.newObject('PartDesign::Revolution', 'shoulder_rev')
        shoulder_rev.Visibility = True
        shoulder_rev.Profile = shoulder_sketch
        shoulder_rev.ReferenceAxis = shoulder0.Origin.OriginFeatures[2]
        shoulder_rev.Angle = 60
        shoulder_rev.Reversed = 1
        shoulder_rev.Midplane = 0

        for i in range(1, 6):
            istr = str(i)
            shoulder_c = doc.addObject('App::Link', 'shoulder' + istr)
            shoulder_c.Visibility = True
            shoulder_c.setLink(shoulder0)
            shoulder_c.addProperty('App::PropertyFloat', 'cup_max_x')
            shoulder_c.cup_max_x = hex_calc.cup_max_x
            shoulder_c.addProperty('App::PropertyFloat', 'angle')
            shoulder_c.angle = 60 * i
            shoulder_c.adjustRelativeLinks(shoulders)
            shoulders.addObject(shoulder_c)
            a = math.pi / 3 * (i + 1)
            shoulder_c.Placement = App.Placement(
                App.Vector(hex_calc.cup_max_x * math.cos(a), hex_calc.cup_max_x * math.sin(a), 0),
                App.Rotation(App.Vector(0, 0, 1), shoulder_c.angle))
            shoulder_c.setExpression('.Placement.Base.x', u'cup_max_x * cos(angle + 60)')
            shoulder_c.setExpression('.Placement.Base.y', u'cup_max_x * sin(angle + 60)')
            shoulder_c.setExpression('.Placement.Rotation.Angle', u'angle')

        doc.recompute()

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


def create(float_input: HexFloatInput = HexFloatInput()) -> HexFreecadModel:
    return HexFreecadModel(hexfloatmodel.create(float_input))
