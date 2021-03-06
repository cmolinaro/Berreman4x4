#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# Example of a 90° twisted nematic liquid crystal

import numpy, Berreman4x4
from numpy import sin, sqrt, abs
from Berreman4x4 import c, pi
import matplotlib.pyplot as pyplot

"""
Consider the following situation:
- twisted liquid crystal with 90° twist between z=0 and z=d
- liquid crystal aligned along x at z=0.
- output polarizer aligned parallel to x

Gooch-Tarry law gives: T_pp = sin²(pi/2·√(1+u²)) / (1+u²),
with u = 2dΔn/λ. 
The transmission minima are given by u = ((2m)²-1)^{-1/2} = √(3),√(15),√(35),…

We consider a birefringence Δn = 0.10 and a thickness d = 4.33 µm. The first
minimum should be at λ = 500 nm, or k0 = 1.257e7 m⁻¹.

Note: Gooch-Tarry law does not take into account interferences between the two
glass substrates. A glass with n = 1.55 minimizes the interferences.
"""

# Materials
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.55)
front = back = Berreman4x4.IsotropicHalfSpace(glass)

# Liquid crystal oriented along the x direction
(no, ne) = (1.5, 1.6)
Dn = ne-no
LC = Berreman4x4.UniaxialNonDispersiveMaterial(no, ne)
R = Berreman4x4.rotation_v_theta([0,1,0], pi/2)
LC = LC.rotated(R)
d = 4.33e-6
TN = Berreman4x4.TwistedMaterial(LC, d)

# Inhomogeneous layer
IL = Berreman4x4.InhomogeneousLayer(TN)
# IL.setMethod("symplectic","Padé",3)

# Structure
s = Berreman4x4.Structure(front, [IL], back)

# Normal incidence: 
Kx = 0.0

# Calculation
lbda_min, lbda_max = 200e-9, 1   # (m)
k0_list = numpy.linspace(2*pi/lbda_max, 2*pi/lbda_min)
data = [s.getJones(Kx,k0) for k0 in k0_list]
data = numpy.array(data)

t_pp = Berreman4x4.extractCoefficient(data, 't_pp')

# Plotting
fig = pyplot.figure()
ax = fig.add_subplot("111")
ax.plot(k0_list, abs(t_pp)**2, 'o', label="Berreman4x4")

# Verification with Gooch-Tarry law:
u = 2*d*Dn*k0_list/(2*pi)
T_GT = sin(pi/2*sqrt(1+u**2))**2 / (1+u**2)
ax.plot(k0_list, T_GT, label="Gooch-Tarry")

ax.set_title(u"Transmission of a 90° twisted nematic liquid crystal")
ax.set_xlabel(r"Wavenumber $k_0$ (m$^{-1}$)")
ax.set_ylabel(r"Power transmission, $T$")
ax.legend()
pyplot.show()

