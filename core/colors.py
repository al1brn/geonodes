#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:22:32 2022

@author: alain
"""

import numpy as np
import mathutils

# ----------------------------------------------------------------------------------------------------
# Create color from hsv

def Hsv(h, s, v):
    col = mathutils.Color()
    col.hsv = h, s, v
    return col

AUTO_LABEL = Hsv(.1, .9, .4) # Color for auto label nodes
LABEL      = Hsv(.1, .9, .6) # Color for nodes with label

# ----------------------------------------------------------------------------------------------------
# Layout colors

ADMIN_COLORS = {
    'UTIL':  Hsv(.1, .95, .2),
    'GENE':  Hsv(.2, .95, .2),
    'AUTO':  Hsv(.9, .95, .2),
    'ERROR': Hsv(1., .95, .2),
    }



count = 10
layout_colors = np.zeros((count, 3), float)
layout_colors[:, 0] = np.linspace(.4, .8, count)
layout_colors[:, 1] = .95
layout_colors[:, 2] = .2
layout_index = 0

def reset():
    global layout_index
    layout_index = 0

def next_color():
    global layout_index
    c = color(layout_colors[layout_index])
    layout_index += 1
    return c

def sub_color(color):
    c = mathutils.Color(color)
    c.v *= 1.3
    return c

def admin_color(key):
    try:
        return ADMIN_COLORS[key.upper()]
    except:
        return None


# ----------------------------------------------------------------------------------------------------
# OLD Version

np.random.seed = 0
count = 1000
color_stack = np.zeros((count, 3), float)
color_stack[:, 0] = np.random.uniform(0. , 1. , count)
color_stack[:, 1] = np.random.uniform(0.3, 1. , count)
color_stack[:, 2] = np.random.uniform(0.3, 0.9, count)
color_stack_index = 0

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

def gen():
    for col in COLORS:
        print(f"light_{col:7s} = color('{col}', 0.25)")
        print(f"mid_{col:7s}   = color('{col}', 0.50)")
        print(f"dark_{col:7s}  = color('{col}', 0.75)")
        print(f"{col:7s}       = color('{col}')")
        print()

def color(name, saturation=None, value=None):
    
    if isinstance(name, (tuple, list, np.ndarray)):
        sname, sat, val = name
        if type(sname) is str:
            return color(sname, sat, val)
        else:
            hsv = name
            
    elif type(name) is str:
        
        if name.upper() in ADMIN_COLORS:
            return ADMIN_COLORS[name.upper()]

        name  = name.lower().replace(' ', '_')
        
        comps = name.split('_')
        if len(comps) > 1:
            name = comps[1]
            change = comps[0]
        else:
            change = ""
            
        try:
            hsv = list(COLORS[name])
        except:
            return mathutils.Color((0., 0., 0.))
        
        if change == "light":
            hsv[1] = 0.25
        elif change == "mid":
            hsv[1] = 0.50
        elif change == "dark":
            hsv[1] = 0.75
            
    elif type(name) is mathutils.Color:
        return name
    
    else:
        raise RuntimeError(f"Unknown color : {name} ({type(name).__name__}).")
        
    if saturation is not None:
        hsv[1] = saturation
    if value is not None:
        hsv[2] = value
        
    c = mathutils.Color()
    c.hsv = hsv
        
    return c


white         = color('white')
black         = color('black')

light_gray    = color('gray', 0.25)
gray          = color('gray', 0.50)
dark_gray     = color('gray', 0.75)
silver        = color('silver')

light_red     = color('red', 0.25)
mid_red       = color('red', 0.50)
dark_red      = color('red', 0.75)
red           = color('red')

light_orange  = color('orange', 0.25)
mid_orange    = color('orange', 0.50)
dark_orange   = color('orange', 0.75)
orange        = color('orange')

light_yellow  = color('yellow', 0.25)
mid_yellow    = color('yellow', 0.50)
dark_yellow   = color('yellow', 0.75)
yellow        = color('yellow')

light_olive   = color('olive', 0.25)
mid_olive     = color('olive', 0.50)
dark_olive    = color('olive', 0.75)
olive         = color('olive')

light_lime    = color('lime', 0.25)
mid_lime      = color('lime', 0.50)
dark_lime     = color('lime', 0.75)
lime          = color('lime')

light_green   = color('green', 0.25)
mid_green     = color('green', 0.50)
dark_green    = color('green', 0.75)
green         = color('green')

light_cyan    = color('cyan', 0.25)
mid_cyan      = color('cyan', 0.50)
dark_cyan     = color('cyan', 0.75)
cyan          = color('cyan')

light_azure   = color('azure', 0.25)
mid_azure     = color('azure', 0.50)
dark_azure    = color('azure', 0.75)
azure         = color('azure')

light_blue    = color('blue', 0.25)
mid_blue      = color('blue', 0.50)
dark_blue     = color('blue', 0.75)
blue          = color('blue')

light_violet  = color('violet', 0.25)
mid_violet    = color('violet', 0.50)
dark_violet   = color('violet', 0.75)
violet        = color('violet')

light_magenta = color('magenta', 0.25)
mid_magenta   = color('magenta', 0.50)
dark_magenta  = color('magenta', 0.75)
magenta       = color('magenta')

light_rose    = color('rose', 0.25)
mid_rose      = color('rose', 0.50)
dark_rose     = color('rose', 0.75)
rose          = color('rose')



