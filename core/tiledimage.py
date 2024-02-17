#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Dec  1 05:40:55 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

U Dim textures
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


# ====================================================================================================
# Name of a tile image

def image_tile_file_name(tex_folder, name, u, v, ext='png'):
    
    if u >= 10 or v >= 10:
        raise Exception(f"Tile image coordinates are not valid: {u=}, {v=} must be < 10")
        
    return Path(tex_folder) / f"{name}/tile.u{u+1}_v{v+1}.{ext}"

# ====================================================================================================
# Create an image tile

def save_image_tile(image, tex_folder, name, u, v, ext='png'):
    folder = Path(tex_folder) / name
    if not folder.exists():
        folder.mkdir()
        
    image.save(image_tile_file_name(tex_folder, name, u, v, ext=ext))
    
# ====================================================================================================
# Load an UDim image

def load_tiled_image(tex_folder, name):
    import bpy
    
    image = bpy.data.images.load(str(Path(tex_folder) / f"{name}/tile.<UVTILE>.png"), check_existing=True)
    image.source = 'TILED'
    image.name = name
    
    return image


# ====================================================================================================
# Test
    
if __name__ == '__main__':
    tex_folder = "/Users/alain/temp/textest"
    
    def demo_tile(u, v):
        image = Image.new("RGB", (1024, 1024), (160, 120, 80))
        
        draw = ImageDraw.Draw(image)
        police = ImageFont.load_default(64)
        draw.text((400, 500), f"{u=} {v=}", font=police, fill=(0, 0, 0))
            
        draw.rectangle((10, 10, 1014, 1014), outline=(0, 0, 0), width=2)    
        
        return image
    
    for u, v in zip([0, 1, 3, 5], [0, 2, 3, 4]):
        save_image_tile(demo_tile(u, v), tex_folder, "demo", u, v)
        
    
        
        
    
    
    
    
    
    
    
    



