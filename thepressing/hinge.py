props = App.ActiveDocument.addObject("App::FeaturePython", "Props")
props.addProperty('App::PropertyFloat', 'buoy_thickness').buoy_thickness = 3.
props.addProperty('App::PropertyFloat', 'helix_height').helix_height = 150.
props.addProperty('App::PropertyFloat', 'helix_inner_rad').helix_inner_rad = 10.
props.addProperty('App::PropertyFloat', 'helix_outer_rad').helix_outer_rad = 25.
props.addProperty('App::PropertyFloat', 'helix_pitch').helix_pitch = 20.
props.addProperty('App::PropertyFloat', 'grove_rad').grove_rad = 5.1
props.addProperty('App::PropertyFloat', 'tip_ellipsisity').tip_ellipsisity = 0.7
#<<Props>>.helix_inner_rad + <<Props>>.grove_rad / <<Props>>.tip_ellipsisity
#sphere v params: atan(<<Props>>.helix_height / 2 / (<<Props>>.helix_inner_rad + <<Props>>.grove_rad / <<Props>>.tip_ellipsisity))
#sphere radius: sqrt(pow(<<Props>>.helix_height / 2, 2) +  pow(<<Props>>.helix_inner_rad + <<Props>>.grove_rad / <<Props>>.tip_ellipsisity, 2))
# helix height: <<Props>>.helix_height - 2 * <<Props>>.grove_rad


App.ActiveDocument.removeObject("Props001")