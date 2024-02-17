#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 19:17:04 2023

@author: alain
"""

# =============================================================================================================================
# Bake the building locations for Rama
#
# Input a pbf file read by osmium module through osm_data module
#
# Buildings locations are:
# - scaled
# - rotated
# - translated to fit on the Rama lands
#
# The altitudes are read in the tiles
#
# Buildings outside the the land rectangle are exluded
#
#
# MAIN STEPS
#
# ----- STEP 1 : Conversion from native format (shape file, gps) to np (pickl + numpy, Lambert 93)
#
# - departement.pbf --> dsepartment.pkl, departement.npz
#
# ----- STEP 2 : extraction rotation
#
# - extract and rotate a zone: extracted_osm.pkl, extracted_osm.npz per Land
#
# Note: no seam is performed since the file contains everything
# The extractiion is RAMA_X, RAMA_Y + 4096 (seam length)
#
# ----- STEP 3 : Extract big buildings
#
# - Big and specific building are extracted for complex treatments
# - Format: VArrays
#   - info:
#     0    : items size
#     1    ; type (building, church, retail...)
#     2    : height (in cm)
#   - items
#     shape
# - file: Rama/Common/big_buildings.npz // Buildings
#
# ----- STEP 4 : Extract far houses
#
# - Small houses are instantiated as rectangular houses when seen from far
# - Format: an array of int and an array of vectors
#   - array of ints
#     0   : neighbours count
#     1   : rotation rz in radians * 1000
#     2   : seed for default_rng
#     3   : ways index (for reuse if required)
#   - array of vectors
#     0   : location
#     1   : scale
# - file: Rama/land/rect_houses.npz // Buildings
#
# ----- STEP 5 : Extract non rectangular houses
#
# - Non rectangular houses must be extruded dynamically when seen closely. A non rectangular
#   house is in two files: rect_house for far instantiation and shaped_houses for close
#   extrusion. Rectangular houses (the majority) are present only in rect_houses.
# - Format: VArrays
#   - info:
#     0   : sys (size of the shape)
#     1   : model id
#     2   : random seed
#   - items:
#     shape
# - file: Rama/land/shaped_houses.npz // Buildings
#
# Note that house id is used to generate visual parameter such as roof, colors, levels...


# =============================================================================================================================

import sys
sys.path.insert(1, "/Users/alain/Documents/blender/scripts/modules")


import numpy as np
import osmium as osm
from pprint import pprint
import matplotlib.pyplot as plt
from pathlib import Path

from geopy.core.varrays import VArrays
from geopy.core.noise3 import smooth

from geopy.gis.tiles import Tiles
from geopy.gis import lamb93
from geopy.gis.ways import Ways

# =============================================================================================================================
# Transformation constants for Rama

RAMA_X       = 28672 #  7 * 4096
RAMA_Y       = 49152 # 12 * 4096

SOUTH_CENTER = (1028389.0, 6293931)
SOUTH_ANGLE  = 130.6
NORTH_CENTER = (528683.0, 6961315.0)
NORTH_ANGLE  = -248.8

SOUTH_TRANSLATION = (2500 + RAMA_X/2, 0, 0)
NORTH_TRANSLATION = (-35000 + RAMA_X/2, 0, 0)

Y_MIN = -RAMA_Y/2
Y_MAX = +RAMA_Y/2



# =============================================================================================================================
# STEP 1 - Convert OSM data bases longitude latitudes into numpy version in Lmabert 93 coordinates

def convert():

    bases = ["/Users/alain/temp/osm/alpes_maritimes",
             "/Users/alain/temp/osm/seine_maritime",
             "/Users/alain/temp/osm/var",
             ]
    
    for i_base, base in enumerate(bases):
        
        if i_base != 2:
            continue
    
        osm_file = base + ".osm.pbf"
        py_file  = base
        
        print("Converting", base)

        Ways.convert(osm_file, py_file, limit=None)
        
        print("Done. Result:")

        ways = Ways.load(py_file)
        print(ways)
        print()
        
# =============================================================================================================================
# STEP 2 - Extract shapes for a Rama land

def extract(ways, center, angle, to_file):

    ag = np.radians(angle)
    M = np.array( ( (np.cos(ag), np.sin(ag)), (-np.sin(ag), np.cos(ag)) ) )
    
    # ----- Rotate the vertices
    
    ways.nodes = np.matmul(M, (ways.nodes - center).T).T

    # ----- Zone limits
    
    x_min = -RAMA_X/2
    x_max =  RAMA_X/2
    y_min = -RAMA_Y/2
    y_max =  RAMA_Y/2
    
    # ----- Test if the shape must be kept
    
    def test_shape(verts):
        
        v_min = np.min(verts, axis=0)
        v_max = np.max(verts, axis=0)
        
        if v_min[0] < x_min:
            return False
        if v_max[0] > x_max:
            return False
        if v_min[1] < y_min:
            return False
        if v_max[1] > y_max + 4096:
            return False
        
        return True
    
    ways.extract_to(to_file, ways_selection=None, verts_selection=test_shape)

if False:
    convert()

if False:
    ways = Ways.load("/Users/alain/temp/osm/seine_maritime")
    extract(ways, NORTH_CENTER, NORTH_ANGLE, "/Users/alain/temp/Rama/North/extracted_osm")

if False:
    ways = Ways.load("/Users/alain/temp/osm/alpes_maritimes")
    extract(ways, SOUTH_CENTER, SOUTH_ANGLE, "/Users/alain/temp/Rama/South/temp1_osm")

if False:
    ways = Ways.load("/Users/alain/temp/osm/var")
    extract(ways, SOUTH_CENTER, SOUTH_ANGLE, "/Users/alain/temp/Rama/South/temp2_osm")

if False:
    ways  = Ways.load("/Users/alain/temp/Rama/South/temp1_osm")
    ways2 = Ways.load("/Users/alain/temp/Rama/South/temp2_osm")
    ways.merge_with(ways2)
    ways.save("/Users/alain/temp/Rama/South/extracted_osm")
    
# =============================================================================================================================
# Seaming
#
# Return None is the shape is not selected

def seam_shape(verts, rng):
    
    loc = verts[0]
    
    # ----- Exclusion probability if in the seam band
    
    if loc[1] < Y_MIN + 4096:
        if rng.uniform(0, 1) > smooth(0, 1, (loc[1] - Y_MIN)/4096):
            return None
        
    if loc[1] > Y_MAX:
        if np.random.uniform(0, 1) < smooth(0, 1, (loc[1] - Y_MAX)/4096):
            return None
        else:
            return verts - (0, RAMA_Y)
        
    return verts
    
# =============================================================================================================================
# STEP 3 - Extract Big Buildings
#
# info: building type

def make_big_buildings(root="/Users/alain/temp/Rama"):
    
    bigs = VArrays()
    
    # ----------------------------------------------------------------------------------------------------
    # Common
    
    def get_verts(ways, i_way, altitudes, translation, rng):

        verts = seam_shape(ways.way_verts(i_way), rng)
        if verts is None:
            return None
        
        alts  = altitudes.values(verts + (RAMA_X/2, RAMA_Y/2))
        verts = np.insert(verts, 2, np.min(alts), axis=-1)
        
        bigs.items = np.append(bigs.items, verts + translation, axis=0)
        
        return verts
    
    
    bigs._info = np.zeros((0, 3), int)
    bigs.items = np.zeros((0, 3), float)
    info = []
    
    rng = np.random.default_rng()
    
    
    # ----------------------------------------------------------------------------------------------------
    # Loop on the two lands
    
    apartments_count = 0
    terrace_count    = 0
    retail_count     = 0
    church_count     = 0
    chapel_count     = 0
    instit_count     = 0
    plant_count      = 0
    sport_count      = 0
    
    
    for land, translation in zip(["South", "North"], [SOUTH_TRANSLATION, NORTH_TRANSLATION]):
        
        altitudes = Tiles(Path(root) / f"{land}/altitudes", (RAMA_X, RAMA_Y))
        ways = Ways.load(Path(root) / f"{land}/extracted_osm")
        
        # ----- apartments
        
        for i_way in ways.get_ways(building='apartments'):

            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            apartments_count += 1
            
            levels = np.clip(int(round(rng.normal(10, 4))), 4, 20)
            
            info.append([len(verts), 1, levels])
            
        # ----- terrace
        
        for i_way in ways.get_ways(building='terrace'):

            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            terrace_count += 1
            
            levels = np.clip(int(round(rng.normal(3, 1))), 1, 5)
            
            info.append([len(verts), 2, levels])
            
        # ----- commercial
            
        for i_way in ways.get_ways(building=['retail', 'commercial']):
            
            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            retail_count += 1
            
            height = int(round(rng.normal(12, 3)))
            
            info.append([len(verts), 3, height])
            
        # ----- church
            
        for i_way in ways.get_ways(building='church'):
            
            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            church_count += 1
            
            #height = int(round(rng.normal(12, 3)))
            
            info.append([len(verts), 4, 0])
            
        # ----- chapel
            
        for i_way in ways.get_ways(building='chapel'):
            
            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            chapel_count += 1
            
            #height = int(round(rng.normal(12, 3)))
            
            info.append([len(verts), 5, 0])

        # ----- Institutions
            
        for i_way in ways.get_ways(building=['government', 'hospital', 'hotel', 'monastery', 'public', 'school']):
            
            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            instit_count += 1
            
            #height = int(round(rng.normal(12, 3)))
            
            info.append([len(verts), 6, 0])
            
        # ----- Industry
            
        for i_way in ways.get_ways(building=['industrial', 'manufacture']):
            
            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            plant_count += 1
            
            height = int(round(rng.normal(20, 5)))
            
            info.append([len(verts), 7, 0])
            
            
        # ----- Sport
            
        for i_way in ways.get_ways(building=['sports_center', 'sports_hall']):
            
            verts = get_verts(ways, i_way, altitudes, translation, rng)
            if verts is None:
                continue
            
            sport_count += 1
            
            height = int(round(rng.normal(20, 5)))
            
            info.append([len(verts), 7, 0])
            
            
    bigs._info = np.array(info)
    bigs.save(Path(root) / "Common/big_buildings")
    
    print("Big building extracted:")
    print("   Apartments:", apartments_count)
    print("   Terrace:   ", terrace_count)
    print("   Retail:    ", retail_count)
    print("   Church:    ", church_count)
    print("   Chapel:    ", chapel_count)
    print("   Instit:    ", instit_count)
    print("   Industrial:", plant_count)
    print("   Sport:     ",  sport_count)
    
# =============================================================================================================================
# Stats

def rect_stats(root):

    ars = np.load(Path(root) / "Common/rect_houses.npz")
    info = ars['info']
    del ars
    
    print("Rectangular houses")
    print("Neighbourhood")
    print(f"   Count           : {len(info)}")
    print(f"   Min Average max : {np.min(info[:, 3])}, {np.average(info[:, 3]):.1f}, {np.max(info[:, 3])}")
    print(f"   Median          : {np.median(info[:, 3]):.1f}")
    print(f"   Std dev         : {np.std(info[:, 3]):.1f}")    
    
    print()
    print("Shaped")
    print(f"   Rectangular: {np.sum(info[:, 1] == -1)}")
    print(f"   Shaped:      {np.sum(info[:, 1] != -1)}")
    

# =============================================================================================================================
# STEP 4 & 5 - Extract houses
#
# Big or complex houses are also written in shaped_house file
#
# models: dict of
# - 'index'     : model index
# - 'city'      : True / False city model or not
# - 'size'      : size of the model
# - 'levels min': min levels
# - 'levels max': max levels
    

def make_houses(root, seed=None):
    
    i_rects = []
    v_rects = []
    
    shapeds = VArrays()
    sh_info = []
    shapeds.items = np.zeros((0, 3), float)
    
    if seed is None:
        rng = np.random.default_rng()
    else:
        rng = np.random.default_rng(seed)
    
    for land, translation in zip(["South", "North"], [SOUTH_TRANSLATION, NORTH_TRANSLATION]):
        
        print("-"*30)
        print(f"Land {land}")
        print()
        
        altitudes = Tiles(Path(root) / f"{land}/altitudes", (RAMA_X, RAMA_Y))
        ways = Ways.load(Path(root) / f"{land}/extracted_osm")
        
        # ----- loop
        
        selection = ways.get_ways(building=['pavillion', 'residential', 'house', 'yes'])
        counter = 0
        
        for i_way in selection:
            
            counter += 1
            if counter % 10000 == 0:
                print(f"   house {counter//1000} k / {len(selection)}")
            
            # ---------------------------------------------------------------------------
            # Get the shape and normalize it plus get the altitude
            
            shape = seam_shape(ways.way_verts(i_way), rng)
            if shape is None:
                continue
            
            ns = ways.normalize_shape(shape)
            alt = np.min(altitudes.values(shape + (RAMA_X/2, RAMA_Y/2)))
            
            # ---------------------------------------------------------------------------
            # Neighbourhood
            
            if True: # False = DEBUG
                neighbours = len(ways.close_buildings(i_way, distance=500))
            else:
                neighbours = 5
                
            # ---------------------------------------------------------------------------
            # Let's generate a random seed specific to this house
            # By using it in the same order, we can regenrate house levels
            
            house_seed = rng.integers(np.iinfo(int).max)
            
            #house_rng = np.random.default_rng(house_seed)
            
            # ---------------------------------------------------------------------------
            # Blind sides shared with neighbours
            
            blind_sides = ways.blind_sides(i_way, epsilon=.5)
                
            # ---------------------------------------------------------------------------
            # Size
            
            size = (ns['size'][0], ns['size'][1], 1)
            
            # ---------------------------------------------------------------------------
            # New entry in the rectangular houses file
            # info:
            # 0: rz*1000
            # 1: index of shaped house when not a rect (-1 if rect)
            # 2: i_way
            # 3: neighbours count
            # 4: house seed
            # 5: blind sides
            
            location = (ns['center'][0] + translation[0], ns['center'][1] + translation[1], alt)
            is_rect  = len(ns['points']) <= 5
            
            i_rects.append((
                int(round(ns['angle']*1000)),     # Rotation z * 1000
                -1 if is_rect else len(sh_info),  # Index in shaped houses
                i_way,                            # way index for detailed reference
                neighbours,                       # Neighbourhood for house style (city, countryside)
                house_seed,                       # Random seed
                blind_sides,                      # Blind sides
                ))
            v_rects.append((location, size))
            
            # It is a rectangular house: we are done
            
            # ---------------------------------------------------------------------------
            # Let's create an entry for shaped houses
            # info: rect house index

            if True or not is_rect: # All are writtent as shape houses because we need the blind sides
                sh_info.append((
                    len(shape)-1,
                    len(i_rects)-1, # Index in rect house
                ))
                
                verts = np.insert(shape[:-1], 2, alt, axis=-1)
                shapeds.items = np.append(shapeds.items, verts + translation, axis=0)
            
        print(f"Land {land} done")
        print()
            
    # ----------------------------------------------------------------------------------------------------
    # Done
            
    shapeds._info = np.array(sh_info)
    print("SHAPE", np.shape(shapeds._info))
    shapeds.save(Path(root) / "Common/shaped_houses")
    
    np.savez(Path(root) / "Common/rect_houses", info=np.array(i_rects), loc_scale=np.array(v_rects))
    
    del shapeds, sh_info, i_rects, v_rects
    
    vas = VArrays.load(Path(root) / "Common/shaped_houses.npz")
    print("Shaped houses:")
    print(vas)
    print()
    del vas
    
    ars = np.load(Path(root) / "Common/rect_houses.npz")
    print("Rectangular houses:")
    print("   info     :", np.shape(ars['info']))
    print("   loc scale:", np.shape(ars['loc_scale']))
    print()
    
    rect_stats(root)

    
#make_big_buildings()
make_houses("/Users/alain/temp/Rama", seed=0)
rect_stats("/Users/alain/temp/Rama")

    




