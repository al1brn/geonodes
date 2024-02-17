#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:47:51 2023

@author: alain
"""

# =============================================================================================================================
# Relief builder principle
#
# 1) Download relief from https://geoservices.ign.fr/rgealti at resolution 1 meter
#    Seine Maritime : 60 Go
# 
# 2) Use RgePack class to manipulate these data
#    2.1) transform each Dalle in a npy. This step is optional but allows better performances for next steps with RGE
#         > rgepack.to_arrays(rge_folder)
#         Seine Maritime : 53 Go
#    2.2) delete the downloaded data
#    2.3) extract a rectangular zone to build a Tiles array
#         > a = RgePack(rge_folder).merge(key0, key1, scale=1)
#         > Tiles.create_from_array(a, zone_folder)
#         Extraction for North hemisphere : 22 Go
#
#   use dalles_to_object and zone_to_object methods to visualize the dalles
#   use owning_key method to get the dalle key from Blender coordinates
#
# 3) Use Tiles to extract a rectangular Zone arbitrary rotated
#    3.1) Adjust the parameters with Tiles.rect_coords())
#    3.2) Final extraction with Tiles.extract())
#
# 4) Proceed to seams and additional process with the Tiles
#
# NOTE : THIS VERSION IS NOT UP TO DATE: it doesn't take into account the last changes of RgePack
# But it case of need, updating shouldn't be that complex (event easier)


import bpy
import numpy as np
from pathlib import Path

from geopy.core import mesh
from geopy.core import multiresgrid
from geopy.gis import rgealti
from geopy.gis import tiles

from importlib import reload

reload(mesh)
reload(multiresgrid)
reload(rgealti)
reload(tiles)

from geopy.core import blender
from geopy.core.mesh import Mesh
from geopy.core.multiresgrid import MultiResGrid
from geopy.core.camera import Camera

from geopy.gis.rgealti import RgePack
from geopy.gis.tiles import Tiles

root = Path("/Users/alain/temp")
north_folder = root / "Alpes Maritimes"
south_folder = root / "Seine Maritime"
sat_folder   = root / "cache"

print('-'*100)


# ====================================================================================================
# Migrate from RGE source livraison to npy tiles which offers better performance

def migrate(source_folder, target_folder):
    RgePack(source_folder, mode='NATIVE').to_arrays(target_folder)
    
# ====================================================================================================
# Extract zone

def extract_zone():
    
    key0 = "0487_6931"
    key1 = "0554_6986"

    a = RgePack(rge_npy).merge(key0, key1, scale=1)
    print("Merged", np.shape(a)) 
    Tiles.create_from_array(a, zone_folder, shape=(65000, 55000), tile_size=5000)
    
# ====================================================================================================
# Adjust

def adjust(corner, size, rotation, pivot, height=50000, seam=5000, scale=100, final=False):
    
    # ----- Load the tiles of the zone

    zone = Tiles(zone_folder)
    print(zone)
    
    # ----- Final
    
    if final:

        # ----- Extraction
        
        print("Extraction...")
        if True:
            zone.extract(band_folder, 
                center   = corner, 
                size     = size, 
                rotation = np.radians(rotation),
                pivot    = pivot,
                )
                
        # ----- Seam

        band = Tiles(band_folder)
        
        print("Seam...")
        if True:
            band.seam_y(0, height, seam)
            
        # ----- Final
        
        band.read_written = True

        print("Final...")
        if True:
            band.copy_tiles(final_folder,
                0, 0, band.count_i, 10)
                
        final = Tiles(final_folder)
        final.to_object("Final")
    
    
    else:

        # ----- Coordinates of the zone to extract
        
        nx = min(size[0], size[1])//scale
        
        coords = zone.rect_coords(
            nx       = nx, 
            corner   = corner, 
            size     = size, 
            centered = True, 
            rotation = np.radians(rotation), 
            pivot    = pivot,
            )
            
        print("coords x:", np.min(coords[..., 0]), "-->", np.max(coords[..., 0]))
        print("coords y:", np.min(coords[..., 1]), "-->", np.max(coords[..., 1]))
            
        a = zone.values(coords)
        
        band = Tiles(a, resolution=scale)
        print(band)

        band.to_object("Rotated band", nx)
            
        # ----- Slope
        
        if True:
            band.seam_y(0, height//scale, seam//scale)
            
            band.to_object("Seamed", nx)    
    
# ====================================================================================================
# Adjust the band to extract
# Used to fine tune to extraction parameters

def adjust_rotate():
    
    # ----- Shape of the extract zone

    zone_shape = (65000, 55000)
    
    # ----- Load the tiles of the zone

    tiles = Tiles(zone_folder, shape=zone_shape)
    print(tiles)
    
    # ----- Coordinates of the zone to extract
    
    coords = tiles.rect_coords(nx=300, 
        corner   = (29000, 28000), 
        size     = (25000, 60000), 
        centered = True, 
        rotation = np.radians(-58), 
        pivot    = (32500, 27500),
        )
        
    a = tiles.values(coords)
    
    grid = Mesh.HeightGrid(a, scale=1, unit_size=25000/300)
    obj = blender.create_mesh_object("Rotated")
    grid.to_object(obj)

# ====================================================================================================
# South extraction (Seine Maritime)

if False:
    adjust(
        corner   = (29000, 28000), 
        size     = (25000, 60000), 
        rotation = -53.4,
        pivot    = (32500, 27500),
        height   = 50000,
        seam     = 5000,
        scale    = 100,
        final    = True,
        )

# ====================================================================================================
# North extraction (Alpes Maritimes + Var)

if False:
    adjust(
        corner   = (37500, 32000), 
        size     = (30000, 60000), 
        rotation = -51, 
        pivot    = (37500, 32500),
        height   = 50000,
        seam     = 5000,
        scale    = 100,
        final    = True,
    )   
    
    
    
    
    
    

    
    

    
    
     

