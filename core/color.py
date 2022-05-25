#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:22:32 2022

@author: alain
"""

import mathutils

# ====================================================================================================
# Display color

class Color:

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
    
    @classmethod
    def Color(cls, name, saturation=None, value=None):
        
        if isinstance(name, tuple):
            sname, sat, val = name
            if type(sname) is str:
                return cls.Color(sname, sat, val)
            else:
                hsv = name
        else:
            try:
                hsv = list(cls.COLORS[name.lower()])
            except:
                return mathutils.Color((0., 0., 0.))
            
            if saturation is not None:
                hsv[1] = saturation
            if value is not None:
                hsv[2] = value
            
        c = mathutils.Color()
        c.hsv = hsv
            
        return c
    
    @classmethod
    def white(cls):
        return cls.Color('white')
    
    @classmethod
    def silver(cls):
        return cls.Color('silver')
    
    @classmethod
    def gray(cls, value=.5):
        return cls.Color('gray', value=value)
    
    @classmethod
    def black(cls):
        return cls.Color('black')


    @classmethod
    def red(cls, saturation=None, value=None):
        return cls.Color('red', saturation=saturation, value=value)
    
    @classmethod
    def orange(cls, saturation=None, value=None):
        return cls.Color('orange', saturation=saturation, value=value)
    
    @classmethod
    def yellow(cls, saturation=None, value=None):
        return cls.Color('yellow', saturation=saturation, value=value)
    
    @classmethod
    def olive(cls, saturation=None, value=None):
        return cls.Color('olive', saturation=saturation, value=value)
    
    @classmethod
    def lime(cls, saturation=None, value=None):
        return cls.Color('lime', saturation=saturation, value=value)
    
    @classmethod
    def green(cls, saturation=None, value=None):
        return cls.Color('green', saturation=saturation, value=value)
    
    @classmethod
    def cyan(cls, saturation=None, value=None):
        return cls.Color('cyan', saturation=saturation, value=value)
    
    @classmethod
    def azure(cls, saturation=None, value=None):
        return cls.Color('azure', saturation=saturation, value=value)
    
    @classmethod
    def blue(cls, saturation=None, value=None):
        return cls.Color('blue', saturation=saturation, value=value)
    
    @classmethod
    def violet(cls, saturation=None, value=None):
        return cls.Color('violet', saturation=saturation, value=value)
    
    @classmethod
    def magenta(cls, saturation=None, value=None):
        return cls.Color('magenta', saturation=saturation, value=value)
    
    @classmethod
    def rose(cls, saturation=None, value=None):
        return cls.Color('rose', saturation=saturation, value=value)