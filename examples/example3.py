# -*- coding: utf-8 -*-
import pyvista as pv
import vtk
from pycyclides.cyclide import linkedCyclides

lcs = linkedCyclides(6, 1.2)
pl = pv.Plotter(notebook=False)
for c in lcs:
    pl.add_mesh(c, smooth_shading=True, color="orange", specular=5)

def my_cpos_callback():
    pl.add_text(str(pl.camera.position), name="cpos")
    return

pl.add_key_event("p", my_cpos_callback)
#pl.store_image = True
#iren = vtk.vtkRenderWindowInteractor()
#pl.iren.AddObserver(vtk.vtkCommand.EndInteractionEvent, my_cpos_callback)
pl.camera.position = (0,32,0)
pl.show()
#zval = pl.get_image_depth()
    