# -*- coding: utf-8 -*-
import os
from math import pi, cos, sin
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

for i, matrix in enumerate(matrices):
    pl = pv.Plotter(window_size=[512,512], off_screen=True)
    pl.set_background("#363940")
    for j, c in enumerate(lcs):
        pl.add_mesh(
            c, smooth_shading=True, color=colors[j], specular=15
        )
    pl.set_position((0,25,-25))
    pl.camera.azimuth = i*2
    pl.set_focus((0, 0, 0))
    pl.camera.zoom(2)
    pngname = "zpic%03d.png" % i
    pl.show(screenshot=pngname)
    
os.system(
    "magick convert -dispose previous -loop 0 -delay 5 zpic*.png example6.gif"    
)
