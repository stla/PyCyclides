# -*- coding: utf-8 -*-
import pyvista as pv
import numpy as np
import seaborn as sb
from pycyclides.cyclide import linkedCyclides

ncyclides = 19

colors = sb.color_palette(palette="viridis", n_colors=(ncyclides+1)//2)
colors_copy = colors.copy()
colors_copy.reverse()
colors = colors + colors_copy
    
lcs = linkedCyclides(ncyclides, 1.5)
pl = pv.Plotter(window_size=[512,512])
pl.set_background("#363940")
for i,c in enumerate(lcs):
    pl.add_mesh(
        c, smooth_shading=True, color=colors[i], specular=15
    )
pl.camera.position = (0,25,-25)
pl.camera.zoom(2)
pl.show()
    
