# -*- coding: utf-8 -*-
import pyvista as pv
import numpy as np
from pycyclides.cyclide import linkedCyclides

palettes = ["viridis", "magma", "inferno", "plasma", "cividis"]
lcs = linkedCyclides(5, 1.1)
pl = pv.Plotter()
for i,c in enumerate(lcs):
    c.point_data["distance"] = np.linalg.norm(c.points, axis=1)
    pl.add_mesh(
        c, smooth_shading=True, cmap=palettes[i], specular=5, 
        show_scalar_bar=False
    )
pl.camera.position = (0,25,0)
pl.show()
    