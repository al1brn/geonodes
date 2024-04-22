#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Wed Apr  3 18:33:10 2024

@author: alain.bernard
@email: alain@ligloo.net

-----

Display overlay
"""

import bpy
import blf

import numpy as np

class Overlay(dict):
    
    OVERLAYS = []
    
    def __init__(self, corner=(0, 0), font_size=20, font_color=(1., 1., 1.), clear=True):
        
        if clear:
            Overlay.hide_all()
        
        self.corner     = corner
        self.font_size  = font_size
        self.font_color = font_color
        self.handler    = None
        
        Overlay.OVERLAYS.append(self)

    # ----------------------------------------------------------------------------------------------------
    # Clean
    
    @staticmethod
    def hide_all():
        a = list(Overlay.OVERLAYS)
        for ovl in a:
            ovl.hide()
        
    # ----------------------------------------------------------------------------------------------------
    # Show / Hide
        
    def show(self):
        if self.handler is None:
            self.handler = bpy.types.SpaceView3D.draw_handler_add(
                Overlay.draw, (self,), 'WINDOW', 'POST_PIXEL'
            )
        
    def hide(self):
        if self.handler is not None:
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
        self.handler = None
        Overlay.OVERLAYS.remove(self)
        
    # ----------------------------------------------------------------------------------------------------
    # Add / update an item to display

    def display(self, name, value=None):
        self[name] = None if value is None else str(value)
        
    def display_vector(self, name, vector, prec=2):
        comps = [f"{v:.{prec}f}" for v in vector]
        self[name] = "[" + ", ".join(comps) + "]"
        
    def display_array(self, name, a, prec=2):
        self[name] = f"min: {np.min(a):.{prec}f}, avg: {np.average(a):.{prec}f}, max: {np.max(a):.{prec}f}"
        
    def display_line(self, name, line):
        self[name + "_LINE"] = line
        
    # ----------------------------------------------------------------------------------------------------
    # Draw
            
    #@staticmethod
    def draw(self):

        if len(self) == 0:
            return

        font_id      = 0
        blf.size(font_id, self.font_size)

        left_margin = self.corner[0] + blf.dimensions(font_id, ' '*5)[0]
        left_size   = max([blf.dimensions(font_id, name + "   ")[0] for name in self.keys()])
        line_height = blf.dimensions(font_id, "LINE")[1]*2
        
        blf.color(font_id, *self.font_color, 1)
        y = self.corner[1] + (len(self)+1)*line_height
        
        val_size = max([blf.dimensions(font_id, value)[0] for value in self.values() if value is not None])
        
        for name, value in self.items():
            
            # ----- Just a string
            
            if name[-5:] == '_LINE':
                blf.position(font_id, left_margin, y, 0)
                blf.draw(font_id, value)
                continue
            
            # ----- Couple (name, value)
            
            blf.position(font_id, left_margin, y, 0)
            blf.draw(font_id, name)
            
            if value is not None:

                # ----- Right align

                d = value.find(".")
                if d >= 0:
                    if (value[:d] + value[d+1:]).isnumeric():
                        d -= 1
                    else:
                        d = -1
                size, _ = blf.dimensions(font_id, value[:d])
                
                # ----- Draw
                    
                blf.position(font_id, left_margin + left_size + val_size - size, y, 0)
                blf.draw(font_id, value)
            
            y -= line_height
            
 
def clear():
    Overlay.hide_all()
    
    
def demo():
    ov = Overlay(corner=(0, 0), font_size=32)
    
    ov.display("String", "My value string")
    ov.display("A very long name to display", "The value")
    ov.display("Just some text")
    ov.display("Integer", 12)
    ov.display("Float", 123.45)
    ov.display_vector("Vector", (123.4578, -7990.799, 687.568))
    ov.display_array("Array", np.random.uniform(-100, 100, 100))
    
    ov.show()



    




