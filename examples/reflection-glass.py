#!/usr/bin/python
# encoding: utf-8

# Berreman4x4 example
# Author: O. Castany

# The simplest example: a homogeneous glass layer in air

print("\n*** Air / glass interface ***\n")

import numpy, Berreman4x4
from Berreman4x4 import c, pi

# Materials:
air = Berreman4x4.IsotropicNonDispersiveMaterial(1.0)
glass = Berreman4x4.IsotropicNonDispersiveMaterial(1.5)

# Half-spaces:
front = Berreman4x4.IsotropicHalfSpace(air)
back = Berreman4x4.IsotropicHalfSpace(glass)

# Structure:
s = Berreman4x4.Structure(front, [], back)

# Incidence angle (Kx = n sin(Φ):
Kx = 0.0

(Jr, Jt) = s.getJones(Kx, k0=1e6)
"""
(matrix([[-0.2,  0. ],     matrix([[ 0.8,  0. ],
        [ 0. , -0.2]]),           [ 0. ,  0.8]]))
"""
print("Jones matrix for reflection:")
print(Jr)
print("Jones matrix for transmission:")
print(Jt)

