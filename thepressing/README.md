dependencies (todo populate requirements.txt):
local install of freecad (for 3d-models, pictures)
scipy ?
numpy
numpy-stl
pybars3
tensorflow 2.13
scikit-learn
deap
keras-tuner
vtkplotlib

Development:
FreeCAD version 0.20.2 (newer versions botch the stl export but are otherwise ok)

Best divisors l=2384,w=1303,plug_diff=6
   Divisor  Deviation
--------------------
    27.720      0.009
    37.250      0.020
    44.980      0.033
    72.250      0.038
    22.080      0.042
    56.760      0.045
    99.340      0.118
    82.200      0.151
    91.700      0.212
    64.440      0.225
    51.760      0.233

Part names:
float: the assembled float with bottom plate of alu, solar panel with frame, junction box, cable (may be simplified), plugs/hinges on all sides.
plug: top view of a single PU hinge.
neck: the section of the plug that has the void (not used as of now)
void: the extrusion of the plug to create a buffer and more elasticity
bracket: the PU cast around the alu frame of the solar panel


Important contants:
panel_elev = tan(panel_angle) * (panel_width + 2 * bracket_back)
//this gives a sun_angle of ~34 degrees
panel_length_min = panel_elev + frame_height
panel_length_max = 2 * panel_elev

ISO 4394-1 / DIN EN 10305
radiuser: 
[10,11,12.5,14,15,16,17.5,19,20,21,22.5,24,25,26,27,27.5,28.5,30,31.5,32.5,34,35,36,38,40,42.5,44.5,45,47.5,50]


Min max
bracket_back < thickness
0 < panel_angle < 7
30 <  sun_angle < 45



2 problems:
high accuracy (2mm): plugs top connection to bracket becomes very thin, and some plugs disappear


TODO
find_closed_circular_edge_groups:
reduce a at the end of each level if it didn't match anything
Don't create point clouds for each new group, just compare center, radius and plane.