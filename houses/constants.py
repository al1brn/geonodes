#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:13:54 2023

@author: alain
"""

# ====================================================================================================
# Build detail

DETAIL_LEVELS = 3
LOW_DETAIL  = 0
MID_DETAIL  = 1
HIGH_DETAIL = 2

# ====================================================================================================
# Materials

WALL         = 0
ROOF         = 1
FLAT_ROOF    = 2
TERRACE      = 3
FENCE        = 4
ROOF_BORDER  = 5

HOUSE_MATERIALS = ['S Wall', 'S Roof', 'S Flat Roof', 'S Terrace', 'S Fence', 'S Roof Border']
MATERIALS = ['Wall', 'Roof', 'Flat Roof', 'Terrace', 'BalcFence', 'Roof Border']


# ====================================================================================================
# Wall options

WALL_FLOOR0  = 0X01
WALL_DOOR    = 0x02
WALL_TERRACE = 0x04
WALL_SHOP    = 0x08
WALL_GARAGE  = 0x10

# ====================================================================================================
# Store types

STORE_TYPES    = [0, 1]
STORE_INTERNAL = 0
STORE_EXTERNAL = 1


#WINDOW  = 0
#BAY     = 1
#DOOR    = 2
#BALCONY = 3

# ====================================================================================================
# Storey types

#STOREY = 0
#EMBEL  = 1

# ====================================================================================================
# Standard dimensions

WIN_TOP = 2.15

# ----------------------------------------------------------------------------------------------------
# Window / Bay standard dimensions : (0: panels, 1: height, 2: width, 3: (0: win, 1: bay 2: door))

WIN_DIMS = [
    (1, 0.75, 0.60, 0),
    (2, 1.15, 1.00, 0), (2, 1.25, 1.00, 0), (2, 1.35, 1.00, 0), (2, 1.25, 1.20, 0), (2, 1.35, 1.20, 0),
    ]
    
BAY_DIMS = [
    (1, 2.15, 0.60, 1), (1, 2.15, 0.80, 1),
    (2, 2.15, 1.00, 1), (2, 2.15, 1.20, 1), (2, 2.15, 1.80, 1), (2, 2.15, 2.10, 1), (2, 2.15, 2.40, 1),
]

DOOR_DIMS = [
    (1, 2.15, 1.00, 2), (1, 2.15, 1.20, 2),
]

WIN_BAY_DIMS = WIN_DIMS + BAY_DIMS


