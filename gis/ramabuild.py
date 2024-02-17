#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:42:04 2023

@author: alain
"""

import numpy as np
from pathlib import Path

                
# ====================================================================================================
# Rama specific

# OLD VERSION : Kept for reference
# To bue used with newversion sat_tiles : SatTiles rather than WMTSTiles

# ----------------------------------------------------------------------------------------------------
# Load the Alpes (South Hemisphere)
    
def load_alpes():

    folder    = "/Users/alain/temp/Satellite/Alpes"
    
    for matrix in range(10, 18):
        tiles = WMTSTiles(folder, matrix)
        
        tiles.download_region(center=SOUTH_CENTER, size=(7*4096, 14*4096), angle=-SOUTH_ANGLE)
    
        if matrix < 15:
            tiles.area(None, None).show()
    
# ----------------------------------------------------------------------------------------------------
# Load the regiion of Etretat (North Hemisphere)
    
def load_etretat():

    folder = "/Users/alain/temp/Satellite/Etretat"
    
    for matrix in range(10, 18):
        tiles = WMTSTiles(folder, matrix)
        
        tiles.download_region(center=NORTH_CENTER, size=(7*4096, 14*4096), angle=-NORTH_ANGLE)
    
        if matrix < 15:
            tiles.area(None, None).show()

# ----------------------------------------------------------------------------------------------------
# Build Hemisphere texture

def build_textures(folder="/Users/alain/temp", hemi="North", seam=True):
    
    if hemi == 'South':
        source_folder = Path(folder) / "Satellite/Alpes"
        target_folder = Path(folder) / "Rama/South/images"
        
        CENTER = SOUTH_CENTER
        ANGLE  = SOUTH_ANGLE
    else:
        source_folder = Path(folder) / "Satellite/Etretat"
        target_folder = Path(folder) / "Rama/North/images"

        CENTER = NORTH_CENTER
        ANGLE  = NORTH_ANGLE

    wtiles = WMTSTiles(source_folder, 13)
    
    # ----- Test
    
    if False:
        wtiles.matrix = 13
        wtiles.area(None, None).show()
        
    corner = CENTER[0] - RAMA_X/2, CENTER[1] + RAMA_Y/2
    size   = RAMA_X, RAMA_Y
    
    # ----------------------------------------------------------------------------------------------------
    # ----- Matrix 13 full texture
        
    if False:
        
        wtiles.matrix = 13
        image = wtiles.extract(corner, (size[0], size[1]), pivot=CENTER, angle=ANGLE)

        print(f"Image matrix {wtiles.matrix}: {image.width} x {image.height}")

        if seam:
            print("   seaming...")
            band = wtiles.extract((corner[0], corner[1] + 4096), (size[0], 4096), pivot=CENTER, angle=ANGLE)
            image = seam_image(image, band)
            
        image.show()
        image.save(target_folder / f"{hemi} 13.png")
    
    
    # ----------------------------------------------------------------------------------------------------
    # ----- Matrix 14 full texture
    
    if False:
    
        wtiles.matrix = 14
    
        image = wtiles.extract(corner, size, pivot=CENTER, angle=ANGLE)
    
        print(f"Saving image matrix {wtiles.matrix}: {image.width} x {image.height}")
    
        if seam:
            print("   seaming...")
            band = wtiles.extract((corner[0], corner[1] + 4096), (size[0], 4096), pivot=CENTER, angle=ANGLE)
            image = seam_image(image, band)
    
        image.show()
        image.save(target_folder / f"{hemi} 14.png")
    
    # ----- Matrix 15 full texture
    
    if True:
        wtiles.matrix = 15
        image = wtiles.extract(corner, size, pivot=CENTER, angle=ANGLE)
        if True:
            image.show()
        image.save(target_folder / f"{hemi} 15.png")


#load_alpes()
#load_etretat()
#build_textures(hemi="South")
#build_textures(hemi="South")

    
    
# ----- Load a rotated area
    
def test():
    for matrix in range(10, 18):
        tiles = WMTSTiles("/Users/alain/temp/test", matrix)
        tiles.download_region(center=(1028247.0, 6294357), size=(30000, 60000), angle=45)
    
        if matrix < 15:
            tiles.area(None, None).show()


    
# =====

def test():
    root = "/Users/alain/temp/Satellite/Alpes"

    tiles = WMTSTiles(Path(root), 15)
    print(tiles)
    
    #img = tiles.area(None, None, show_tiles=True)
    
    
    
    img = tiles.extract(corner=SOUTH_CENTER, size=(5000, 5000), pivot=SOUTH_CENTER, angle=30, show_tiles=True)
    
    
    img.show()

    
    