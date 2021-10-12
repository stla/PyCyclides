# -*- coding: utf-8 -*-
import numpy as np
import pyvista as pv

# Hopf fiber
def HopfInverse(p, phi):
    return (
        np.array(
            [
                p[0] * np.cos(phi) + p[1] * np.sin(phi),
                (1 + p[2]) * np.sin(phi),
                (1 + p[2]) * np.cos(phi),
                p[0] * np.sin(phi) - p[1] * np.cos(phi)
            ]
        )
        / np.sqrt(2 * (1 + p[2]))
    )


# stereographic projection
def Stereo(q):
    return q[0:3] / (1 - q[3])


# rotation in 4D space (right-isoclinic)
def rotate4d(alpha, beta, xi, vec):
    a = np.cos(xi)
    b = np.sin(alpha) * np.cos(beta) * np.sin(xi)
    c = np.sin(alpha) * np.sin(beta) * np.sin(xi)
    d = np.cos(alpha) * np.sin(xi)
    p = vec[0]
    q = vec[1]
    r = vec[2]
    s = vec[3]
    return np.array(
        [
            a * p - b * q - c * r - d * s,
            a * q + b * p + c * s - d * r,
            a * r - b * s + c * p + d * q,
            a * s + b * r - c * q + d * p
        ]
    )

# cyclide parameterization
def f(phi, theta, t): # -pi/2 < phi < pi/2
    cosphi = np.cos(phi)
    p = [np.cos(theta)*cosphi, np.sin(theta)*cosphi, np.sin(phi)]
    h = HopfInverse(p, t)
    hr = rotate4d(np.pi/2, 0, 1, h)
    return Stereo(hr)

# cyclide mesh
def cyclideMesh(phi, nu=200, nv=300):
    angle_u = np.linspace(0, 2*np.pi, nu)
    angle_v = np.linspace(0, 2*np.pi, nv)   
    u, v = np.meshgrid(angle_u, angle_v)
    x, y, z = f(phi, u, v)
    grid = pv.StructuredGrid(x, y, z)
    return grid.extract_geometry().clean(tolerance=1e-6)

def linkedCyclides(n, phi, nu=200, nv=300):
    cyclide = cyclideMesh(phi, nu, nv)
    cyclides = [cyclide.copy()]
    beta = 360.0 / n
    for _ in range(n-1):
        cyclide.rotate_y(beta);
        cyclides.append(cyclide.copy())
    return cyclides


    