#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:22:32 2022

@author: alain
"""

import mathutils


COLORS = {
    'white'   : (0., 0., 1.00),
    'silver'  : (0., 0., 0.75),
    'gray'    : (0., 0., 0.50),
    'black'   : (0., 0., 0.00),
    
    'red'     : ( 0/12, 1., 1.),
    'orange'  : ( 1/12, 1., 0.5),
    'yellow'  : ( 2/12, 1., 1.),
    'olive'   : ( 3/12, 1., 0.5),
    'lime'    : ( 4/12, 1., 1.),
    'green'   : ( 5/12, 1., 0.5),
    'cyan'    : ( 6/12, 1., 1.),
    'azure'   : ( 7/12, 1., 0.5),
    'blue'    : ( 8/12, 1., 1.),
    'violet'  : ( 9/12, 1., 0.5),
    'magenta' : (10/12, 1., 1.),
    'rose'    : (11/12, 1., 0.5),
}

def color(name, saturation=None, value=None):
    
    if isinstance(name, tuple):
        sname, sat, val = name
        if type(sname) is str:
            return color(sname, sat, val)
        else:
            hsv = name
    else:
        try:
            hsv = list(COLORS[name.lower()])
        except:
            return mathutils.Color((0., 0., 0.))
        
        if saturation is not None:
            hsv[1] = saturation
        if value is not None:
            hsv[2] = value
        
    c = mathutils.Color()
    c.hsv = hsv
        
    return c

white       = color('white')
light_gray  = color('gray', 0.75)
gray        = color('gray', 0.50)
dark_gray   = color('gray', 0.25)
silver      = color('silver')
black       = color('black')

def red(saturation=None, value=None):
    return color('red', saturation=saturation, value=value)

def orange(saturation=None, value=None):
    return color('orange', saturation=saturation, value=value)

def yellow(saturation=None, value=None):
    return color('yellow', saturation=saturation, value=value)

def olive(saturation=None, value=None):
    return color('olive', saturation=saturation, value=value)

def lime(saturation=None, value=None):
    return color('lime', saturation=saturation, value=value)

def green(saturation=None, value=None):
    return color('green', saturation=saturation, value=value)

def cyan(saturation=None, value=None):
    return color('cyan', saturation=saturation, value=value)

def azure(saturation=None, value=None):
    return color('azure', saturation=saturation, value=value)

def blue(saturation=None, value=None):
    return color('blue', saturation=saturation, value=value)

def violet(saturation=None, value=None):
    return color('violet', saturation=saturation, value=value)

def magenta(saturation=None, value=None):
    return color('magenta', saturation=saturation, value=value)

def rose(saturation=None, value=None):
    return color('rose', saturation=saturation, value=value)

