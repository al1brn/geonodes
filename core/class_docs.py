#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 11:31:25 2022

@author: alain
"""

# A Fake python module used to provide class documentation
# It is read by build_geonodes_auto_doc in nodes_gen

class Mesh:
    """ > **Mesh** sub class of [Geometry](Geometry.md)
    
    ### Constructors
    
    Constructors come from the Blender menu *Mesh primitives*:        
    - [Cone](#Cone), returns the quadruplet: (cone(Mesh), top, bottom, side)
    - [Cube](#Cube)
    - [Cylinder](#Cylinder), returns the quadruplet: (cone(Mesh), top, bottom, side)
    - [Grid](#Grid)
    - [IcoSphere](#IcoSphere)
    - [Circle](#Circle)
    - [Line](#Line)
    - [UVSphere](#UVSphere)
             
    The `Line` constructor is also available with the different ways to initialize a line:
    - [LineEndPoints](#LineEndPoints):  line is defined by its end points, the number of points is provided
    - [LineEndPointsResolution](#LineEndPointsResolution): same as previous but resolution is given rather than the number of points
    - [LineOffset](#LineOffset): line is defined by a starting point, a direction and a number of points
    """
    
class Curve:
    """ > **Curve** sub class of [Geometry](Geometry.md)
    
    ### Constructors
    
    Constructors come from the Blender menu *Curve primitives*:        
    - [Arc](#Arc), arc from center and radius
    - [ArcFromPoints](#ArcFromPoints), arc from 3 points, return a node with sockets curve, center, normal and radius
    - [BezierSegment](#BezierSegment)
    - [Circle](#Circle), circle from center and radius
    - [CircleFromPoints](#CircleFromPoints), corcme from 3 points, return a couple of sockets (circle, center)
    - [Line](#Line), line from points
    - [LineDirection](#LineDirection), line from a starting point, a direction and a length
    - [Spiral](#Spiral)
    - [QuadraticBezier](#QuadraticBezier)
    - [Quadrilateral](#Quadrilateral)
    - [Star](#Star)
    """
    