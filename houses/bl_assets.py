#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:47:06 2023

@author: alain
"""

import pickle
import numpy as np
from pathlib import Path

from geopy.core import blender
from geopy.houses.asset import Asset, Assets


def from_current_blender():
    
    assets = Assets()
    
    assets.add_collection('store',         blender.get_collection("Stores"))
    assets.add_collection('panel',         blender.get_collection("Panels"))
    assets.add_collection('bay_panel',     blender.get_collection("Bays"))
    assets.add_collection('frame_in',      blender.get_collection("Frames In"))
    assets.add_collection('frame_out',     blender.get_collection("Frames Out"))
    assets.add_collection('door',          blender.get_collection("Doors"))
    assets.add_collection('door_in',       blender.get_collection("Doors In"))
    assets.add_collection('balcony',       blender.get_collection("Balcony"))
    assets.add_collection('shop',          blender.get_collection("Shops"))
    
    return assets

        
        
        
        
        
        

        
    
    
    
    
    
