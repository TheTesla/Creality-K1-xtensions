#!/usr/bin/env python3

from xyzcad import render
from numba import njit #jit
import math
import numpy as np
import sys



@njit
def fuzzCylInfH(p):
    x, y = p[:2]
    return (x**2 + y**2)**0.5

p = 0.2

@njit
def f(x,y,z):
    if z < 0:
        return False
    if ((abs(x)-22)**2+y**2)**0.5 < 1.6:
        return False
    if z > 2 and z < 10:
        rp = (x**2+(abs(y)-22)**2)**0.5
        if rp < 1.5:
            return False
        if rp < 2.0:
            return True
    if z > 3:
        return False

    r = (x**2 + y**2)**0.5
    ang = -math.atan2(y,x)
    if r > 18 + 7.5*((math.cos(ang*4)+1)/2)**4:
        return False
    if r < 9:
        return False

    if r < 16  + 7.5*((math.cos(ang*2+math.pi)+1)/2)**20 and r > 11 \
    and z > 1 and z < 2:
        return False

    return True

render.renderAndSave(f, f'extruder_motor_cooler_{p*1000:04.0f}u.stl', p)

