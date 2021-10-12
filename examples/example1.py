# -*- coding: utf-8 -*-
import pyvista as pv
from pycyclides.cyclide import linkedCyclides

lcs = linkedCyclides(3, 1.2)
pl = pv.Plotter()
for c in lcs:
    pl.add_mesh(c, smooth_shading=True, color="orange", specular=5)
pl.set_position([0,25,0])
pl.show()
    