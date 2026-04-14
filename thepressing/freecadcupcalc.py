import math

import FreeCAD as App
import Part
import Mesh
import Sketcher
from FreeCAD import Document
from Part import Feature

from floatinput import FloatInput


def calc_cup(cup_rad: float, cup_lip: float, cup_depth: float, cup_angle: float, cup_tip: float):
    cup = cup_rad - cup_lip
    angle = math.radians(cup_angle)
    tip = cup_tip - cup_lip
    height = cup_depth
    print('cup', cup)
    print('angle', angle)
    print('tip', tip)
    print('height', height)
    # cup = 38.37290758
    # angle = 1.2722276452030172
    # tip = 10.811872274
    # height = 24.4691106
    ellipse_height_est = height / (1 - math.sin(angle))
    doc = App.newDocument('cupcalc')
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = body.newObject('Sketcher::SketchObject', 'Sketch')
    sketch.Support = (doc.getObject('XZ_Plane'), [''])
    sketch.MapMode = 'FlatFace'
    sketch.addGeometry(Part.Ellipse(App.Vector(0, 0, 0), App.Vector(5, 30, 0), App.Vector(0, 30, 0)), False)
    sketch.exposeInternalGeometry(0)
    sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 1, -1, 1))
    sketch.addConstraint(Sketcher.Constraint('Vertical', 0, 3, 1, 1))
    sketch.addGeometry(Part.Point(App.Vector(4, 12, 0)))
    sketch.addConstraint(Sketcher.Constraint('PointOnObject', 5, 1, 0))
    sketch.addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0, 30, 0), App.Vector(0, 0, 1), 30), -math.pi / 2, 0),
                       True)
    sketch.addConstraint(Sketcher.Constraint('Coincident', 6, 3, 0, 3))
    sketch.addConstraint(Sketcher.Constraint('Coincident', 6, 1, 1, 1))
    sketch.addConstraint(Sketcher.Constraint('Horizontal', 6, 2, 0, 3))
    sketch.addGeometry(Part.LineSegment(App.Vector(0, 30, 0), App.Vector(24, 12.5, 0)), True)
    sketch.addConstraint(Sketcher.Constraint('Coincident', 7, 1, 0, 3))
    sketch.addConstraint(Sketcher.Constraint('PointOnObject', 7, 2, 6))
    sketch.addGeometry(Part.LineSegment(App.Vector(24, 12.5, 0), App.Vector(4, 12, 0)), True)
    sketch.addConstraint(Sketcher.Constraint('Coincident', 8, 1, 7, 2))
    sketch.addConstraint(Sketcher.Constraint('Coincident', 8, 2, 5, 1))
    sketch.addConstraint(Sketcher.Constraint('Horizontal', 8))
    sketch.addGeometry(Part.LineSegment(App.Vector(0, 30, 0), App.Vector(18, 6, 0)), True)
    sketch.addConstraint(Sketcher.Constraint('Coincident', 9, 1, 0, 3))
    sketch.addConstraint(Sketcher.Constraint('PointOnObject', 9, 2, 6))
    sketch.addGeometry(Part.LineSegment(App.Vector(18, 6, 0), App.Vector(3, 6, 0)), True)
    sketch.addConstraint(Sketcher.Constraint('Coincident', 10, 1, 9, 2))
    sketch.addConstraint(Sketcher.Constraint('PointOnObject', 10, 2, 0))
    sketch.addConstraint(Sketcher.Constraint('Horizontal', 10))
    sketch.addConstraint(Sketcher.Constraint('Angle', 7, 1, 2, 2, angle))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', 1, 1, 10, 2, tip))
    sketch.addConstraint(Sketcher.Constraint('DistanceX', 1, 1, 5, 1, cup))
    sketch.addConstraint(Sketcher.Constraint('DistanceY', 10, 2, 5, 1, height))
    doc.recompute()
    e_x = sketch.Geometry[2].StartPoint[0]
    e_h = sketch.Geometry[2].StartPoint[1]
    t_x = sketch.Geometry[10].StartPoint[0]
    t_h = sketch.Geometry[10].StartPoint[1]
    t_a = -math.degrees(math.atan2(t_h - e_h, t_x))

    def d():
        e_x, e_h, t_a, t_h
        return {**locals()}

    return d()
