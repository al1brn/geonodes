#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:52:10 2023

@author: alain
"""

import sys
sys.path.insert(1, "/Users/alain/Documents/blender/scripts/modules")


import shapefile
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from pathlib import Path

from geopy.gis.tiles import Tiles
from geopy.core.noise3 import smooth

# ====================================================================================================
# Constants

RAMA_X       = 28672 #  7 * 4096
RAMA_Y       = 49152 # 12 * 4096

SOUTH_CENTER = (1028389.0, 6293931)
SOUTH_ANGLE  = 130.6
SOUTH_TRANSLATION = (2500 + RAMA_X/2, 0)

NORTH_CENTER = (528683.0, 6961315.0)
NORTH_ANGLE  = -248.8
NORTH_TRANSLATION = (-35000 + RAMA_X/2, 0)


# ====================================================================================================
# Folder

root = Path("/Users/alain/temp/")
source_sub = "BDFORET/1_DONNEES_LIVRAISON/BDF_2-0_SHP_LAMB93_D076/FORMATION_VEGETALE.shp"

source_76 = root / ("Forets/Seine Maritime/BDFORET/1_DONNEES_LIVRAISON/BDF_2-0_SHP_LAMB93_D076/FORMATION_VEGETALE.shp")
source_06 = root / ("Forets/Alpes Maritimes/BDFORET/1_DONNEES_LIVRAISON/BDF_2-0_SHP_LAMB93_D006/FORMATION_VEGETALE.shp")
source_83 = root / ("Forets/Var/BDFORET/1_DONNEES_LIVRAISON/BDF_2-0_SHP_LAMB93_D083/FORMATION_VEGETALE.shp")

target_folder = root / "Rama/Common"

# ====================================================================================================
# Scatter trees in a shape

def scatter(points, density=.1, debug=False):
    
    p0, p1 = np.min(points, axis=0), np.max(points, axis=0)
    sx, sy = p1[0] - p0[0], p1[1] - p0[1]
    if max(sx, sy) < 16000:
        resol = 1
    else:
        resol = 10
        
    imx, imy = int(sx/resol) + 2, int(sy/resol) + 2
    
    def to_ij(points):
        return [(int((point[0] - p0[0])/resol)+1, int((point[1] - p0[1])/resol + 1)) for point in points]
    
    # ----- Draw a white image of the area
    
    img  = Image.new('1', (imx, imy), 0)
    draw = ImageDraw.Draw(img)
    
    draw.polygon(to_ij(points), 1)
    
    if False:
        img.show()
        
    # ----- Number of locations
    
    count = np.random.default_rng().poisson(density*(sx*sy))
    
    # Generate random locations in the whole rectangle
    
    verts = np.empty((count, 2), float)
    verts[:, 0] = np.random.default_rng().uniform(p0[0], p1[0], count)
    verts[:, 1] = np.random.default_rng().uniform(p0[1], p1[1], count)
    
    # Convert into image coordinates
    
    # Keep the locations with the "good" color
    
    keep = [pt for pt, ipt in zip(verts, to_ij(verts)) if img.getpixel(ipt) == 1]
    
    if debug:
        ikeep = [ipt for pt, ipt in zip(verts, to_ij(verts)) if img.getpixel(ipt) == 1]
        
        img  = Image.new('1', (imx, imy), 0)
        for ipt in ikeep:
            img.putpixel(ipt, 1)
            
        img.show()
        
    # ----- Done
    
    return np.array(keep)


# ====================================================================================================
# Build the trees locations

def create_trees(sources, center, angle, translation, altitudes):
    
    ag = np.radians(angle)
    M  = np.array( ( (np.cos(ag), -np.sin(ag)), (np.sin(ag), np.cos(ag)) ) )
    
    x_min = -RAMA_X//2
    x_max =  RAMA_X//2
    y_min = -RAMA_Y//2
    y_max =  RAMA_Y//2
    
    locations = np.zeros((0, 2), float)
    
    def trans_shape(shape):
        points = np.array(shape.points) - center
        return np.matmul(M, points.T).T
    
    for source in sources:
        
        sf = shapefile.Reader(str(source))
        print("Reading...")
        print(sf)
        
        for i_shape, shape in enumerate(sf.shapes()):
            
            if i_shape%1000 == 0:
                print(f"Shape {i_shape//1000} k /{len(sf.shapes())}")
            
            points = trans_shape(shape)
            p0, p1 = np.min(points, axis=0), np.max(points, axis=0)
            
            if p0[0] > x_max:
                continue
            if p1[0] < x_min:
                continue
            if p0[1] > y_max + 4096:
                continue
            if p1[1] < y_min:
                continue
            
            # ----- Scatter trees
                
            locs = scatter(points, density=.1, debug=False)
            
            # ----- Exclude the ones out of the bounds
            
            locs = locs[np.logical_and(
                np.logical_and(locs[:, 0] > x_min, locs[:, 0] < x_max),
                np.logical_and(locs[:, 1] > y_min, locs[:, 1] < y_max + 4096),
                )]
            
            # ----- Seaming
            
            if True:
                if p0[1] < y_min + 4096 or p1[1] > y_max:
                    
                    sel = np.ones(len(locs), bool)
                    
                    for i, loc in enumerate(locs):
                        if loc[1] < y_min + 4096:
                            if np.random.uniform(0, 1) > smooth(0, 1, (loc[1] - y_min)/4096):
                                sel[i] = False
                            
                        if loc[1] > y_max:
                            if np.random.uniform(0, 1) < smooth(0, 1, (loc[1] - y_max)/4096):
                                sel[i] = False
                            else:
                                locs[i, 1] -= RAMA_Y
                                
                    locs = locs[sel]
        
            # ----- Add to the global result
            
            locations = np.append(locations, locs, axis=0)
            
    # ------ Altitudes and translation
    
    locations = np.insert(locations, 2, 0, axis=-1)
    
    locations[:, 2] = altitudes.values(locations[:, :2] + (RAMA_X/2, RAMA_Y/2))
        
    locations += (translation[0], translation[1], 0)
            
    return locations


# ----------------------------------------------------------------------------------------------------
# Build the two forests

def build_forest():

    print("North forest...")
                
    alts = Tiles(root / "Rama/North/altitudes", (RAMA_X, RAMA_Y))
    verts = create_trees([source_76], NORTH_CENTER, -NORTH_ANGLE, NORTH_TRANSLATION, alts)
    del alts
    
    print(f"{len(verts)} trees.")
    
    forest = verts
    
    print("South forest...")
                
    alts = Tiles(root / "Rama/South/altitudes", (RAMA_X, RAMA_Y))
    verts = create_trees([source_06, source_83], SOUTH_CENTER, -SOUTH_ANGLE, SOUTH_TRANSLATION, alts)
    del alts
    
    print(f"{len(verts)} trees.")
    
    print("Save the forest")
    
    forest = np.append(forest, verts, axis=0)
    np.save(target_folder / "forest", forest)


build_forest()
