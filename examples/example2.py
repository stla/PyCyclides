# -*- coding: utf-8 -*-
import pyvista as pv
from pycyclides.cyclide import linkedCyclides

plotter = pv.Plotter(shape=(2, 3))

plotter.subplot(0, 0)
lcs = linkedCyclides(1, 1.2)
for c in lcs:
    plotter.add_mesh(c, smooth_shading=True, color="orange", specular=5)
plotter.camera.position=(0,29,0)

plotter.subplot(0, 1)
lcs = linkedCyclides(2, 1.2)
for c in lcs:
    plotter.add_mesh(c, smooth_shading=True, color="orange", specular=5)
plotter.camera.position=(0,29,0)

plotter.subplot(0, 2)
lcs = linkedCyclides(3, 1.2)
for c in lcs:
    plotter.add_mesh(c, smooth_shading=True, color="orange", specular=5)
plotter.camera.position=(0,29,0)

plotter.subplot(1, 0)
lcs = linkedCyclides(4, 1.2)
for c in lcs:
    plotter.add_mesh(c, smooth_shading=True, color="orange", specular=5)
plotter.camera.position=(0,29,0)

plotter.subplot(1, 1)
lcs = linkedCyclides(5, 1.2)
for c in lcs:
    plotter.add_mesh(c, smooth_shading=True, color="orange", specular=5)
plotter.camera.position=(0,29,0)
#plotter.enable_shadows()

plotter.subplot(1, 2)
lcs = linkedCyclides(6, 1.2)
for c in lcs:
    plotter.add_mesh(c, smooth_shading=True, color="orange", specular=5)
plotter.camera.position=(0,29,0)


# Display the window
plotter.show()    