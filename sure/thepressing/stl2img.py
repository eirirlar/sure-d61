import vtkplotlib as vpl
from stl.mesh import Mesh

def stl2img(filename_base='thepressing', image_type='png'):
    path = filename_base + '.stl'
    mesh = Mesh.from_file(path)
    vpl.mesh_plot(mesh)
    vpl.view(camera_position=(0.05, -1, 1.2))
    vpl.save_fig(filename_base + '.' + image_type, magnification=10, off_screen=True)
    vpl.close()
