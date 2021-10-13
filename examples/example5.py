# -*- coding: utf-8 -*-
import pyvista as pv
from pycyclides.cyclide import linkedCyclides

import pyvista as pv
pl = pv.Plotter()
actors = []
ncyclides = 3
phi = 1.2
def create_mesh_n(value):
    global actors
    global ncyclides
    global phi
    for actor in actors:
        pl.remove_actor(actor)
    actors = []
    ncyclides = round(value)
    lcs = linkedCyclides(ncyclides, phi)
    for i,c in enumerate(lcs):
        actor = f"actor{str(i)}"
        actors.append(actor)
        pl.add_mesh(c, smooth_shading=True, color="orange", specular=5, name=actor)
def create_mesh_phi(value):
    global actors
    global ncyclides
    global phi
    phi = value
    for actor in actors:
        pl.remove_actor(actor)
    actors = []
    lcs = linkedCyclides(ncyclides, phi)
    for i,c in enumerate(lcs):
        actor = f"actor{str(i)}"
        actors.append(actor)
        pl.add_mesh(c, smooth_shading=True, color="orange", specular=5, name=actor)
slider1 = pl.add_slider_widget(
    create_mesh_n,
    [1, 10],
    value = 3,
    title="Cyclides",
    title_opacity=0.5,
    title_color="red",
    fmt="%.0f",
    title_height=0.05,
    pointa=(.025, .93), pointb=(.31, .93),
)
slider2 = pl.add_slider_widget(
    create_mesh_phi,
    [1, 1.4],
    value = 1.2,
    title="phi",
    title_opacity=0.5,
    title_color="red",
    fmt="%.2f",
    title_height=0.05,
    pointa=(.35, .93), pointb=(.64, .93),
    style=None
)
pl.camera.position = (0,34,0)
pl.show()
