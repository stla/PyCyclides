# -*- coding: utf-8 -*-
import os
import random
import pyvista as pv
from flask import Flask, render_template, request
from pycyclides.cyclide import linkedCyclides


static_image_path = os.path.join("static", "images")
if not os.path.isdir(static_image_path):
    os.makedirs(static_image_path)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getimage")
def get_img():
    """Generate a screenshot of a simple pyvista mesh.

    Returns
    -------
    str
        Local path within the static directory of the image.

    """
    # get the user selected mesh options
    phi = float(request.args.get("phi"))
    ncyclides = request.args.get("ncyclides")
    color = request.args.get("color")
    meshes = linkedCyclides(int(ncyclides), phi)

    # generate screenshot
    filename = f"Cyclides-phi{int(100*phi)}-n{ncyclides}-{color[1:6]}.png"
    filepath = os.path.join(static_image_path, filename)
    plotter = pv.Plotter(window_size=(500, 500), off_screen=True)
    for mesh in meshes:
        plotter.add_mesh(mesh, smooth_shading=True, color=color, specular=5)
    plotter.set_position([0, 26, 0])
    plotter.show(screenshot=filepath)
    return filename  # os.path.join("images", filename)
