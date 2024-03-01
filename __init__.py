#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:21:18 2022

@author: alain.bernard
"""

PI   = 3.141592653589793
TAU  = 6.283185307179586

from .core import blender
from .core import engine

if True:

    # ----- Reload
    
    from importlib import reload
    
    from .maths import splinesmaths
    from .maths import distribs
    from .maths import functions
    from .maths import noise
    from .maths import primes
    from .maths import transformations
    
    reload(blender)
    reload(engine)
    
    reload(splinesmaths)
    reload(distribs)
    reload(functions)
    reload(noise)
    reload(primes)
    reload(transformations)
    
# =============================================================================================================================
# Nodes generator

from .nodes.tree import GeoNodes, Shader, Compositor
from .nodes.treestack import Trees
from .nodes.zones import Simulation, Repeat
from .nodes.constants import current_tree, dump_stack

# =============================================================================================================================
# Python geometry

    
# ----- Maths
    
# Maths modules

from .maths import splinesmaths, distribs

# Maths classes

from .maths.functions import Easing, Function, keyed
from .maths.noise import Noise
from .maths.transformations import normalize, axis_vector, get_plane, rotation_to, tracker, axis_index, angle_with, Transformations

# ----- Core

if True:
    from .core import camera

    from .core import domain
    from .core import geometry
    from .core import cloud
    from .core import mesh
    from .core import curve
    from .core import text
    from .core import instances
    from .core import shapekeys
    from .core import parameters

    from .core import bingrid
    from .core import simulation
    from .core import kinematics
    
    reload(camera)

    reload(domain)
    reload(geometry)
    reload(cloud)
    reload(mesh)
    reload(curve)
    reload(text)
    reload(instances)
    reload(shapekeys)
    reload(parameters)
    
    reload(bingrid)
    reload(simulation)
    reload(kinematics)


from .core.camera import Camera

from .core.geometry import Geometry
from .core.cloud import Cloud
from .core.mesh import Mesh
from .core.curve import Curve
from .core.text import Text
from .core.instances import Instances
from .core.shapekeys import ShapeKeys
from .core.parameters import new_param_group, param_group

from .core.bingrid import BinGrid
from .core.simulation import Simulation
from .core.kinematics import Kinematics
    

if False:
    from geopy.core.noise import lerp, smooth, smoother, maprange, SNoise, BNoise, noise
    
    from geopy.core.transformations import Vectors, Rotations, Matrices, Eulers, Quaternions, TMatrices, Instances
    from geopy.core.meshbuilder import MeshBuilder
    from geopy.core.curvebuilder import CurveBuilder, PolyBuilder, BezierBuilder, NurbsBuilder
    from geopy.core.points import Points
    from geopy.core.functions import Function
    from geopy.core.shapekeys import ShapeKeys, MeshShapeKeys, CurveShapeKeys
    from geopy.core.treenodes import GeoNodes, Shader











