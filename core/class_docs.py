#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 11:31:25 2022

@author: alain
"""

# A Fake python module used to provide class documentation
# It is read by build_geonodes_auto_doc in nodes_gen

# ----------------------------------------------------------------------------------------------------
# Data sockets

class Mesh:
    """ > **Mesh** sub class of [Geometry](Geometry.md)
    
    A **Mesh** has four domains:
    - `verts` of type [Vertex](Vertex.md)
    - `edges` of type [Edge](Edge.md)
    - `faces` of type [Face](Face.md)
    - `corners` of type [Corner](Corner.md)
    
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
    
    A **Curve** has two domains:
    - `points` of type [ControlPoint](ControlPoint.md)
    - `splines` of type [Spline](Spline.md)
    
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
    
class Instances:
    """ > **Instances** sub class of [Geometry](Geometry.md)
    
    A **Instances** has one domain:
    - `insts` of type [Instance](Instance.md)
    
    """

class Points:
    """ > **Points** sub class of [Geometry](Geometry.md)
    
    **Points** is the class for Blender **Cloud Points**. It has one domain:
    - `points` of type [CloudPoint](CloudPoint.md)        
    """
    
class Volume:
    """ > **Volume** sub class of [Geometry](Geometry.md)
    
    **Volume** has no [Domain](Domain.md)
    """
    
# ----------------------------------------------------------------------------------------------------
# Domains

class Vertex:
    """ > **Vertex** is one of the four [domains](Domain.md) of [Mesh](Mesh.md).
    
    It uses the *'POINT'* string domain.
    """
    
class Edge:
    """ > **Edge** is one of the four [domains](Domain.md) of [Mesh](Mesh.md).
    
    It uses the *'EDGE'* string domain.
    """
    
class Face:
    """ > **Face** is one of the four [domains](Domain.md) of [Mesh](Mesh.md).
    
    It uses the *'FACE'* string domain.
    """
    
class Corner:
    """ > **Corner** is one of the four [domains](Domain.md) of [Mesh](Mesh.md).
    
    It uses the *'CORNER'* string domain.
    """
    
class ControlPoint:
    """ > **Vertex** is one of the two [domains](Domain.md) of [Curve](Curve.md).
    
    It uses the *'POINT'* string domain.
    """
    
class Spline:
    """ > **Spline** is one of the two [domains](Domain.md) of [Curve](Curve.md).
    
    It uses the *'SPLINE'* string domain. (*'CURVE'* for some nodes)
    """
    
class CloudPoint:
    """ > **CloudPoint** is the unique [domain](Domain.md) of [Points](Points.md).
    
    It uses the *'POINT'* string domain.
    """

class Instance:
    """ > **Instance** is the unique [domain](Domain.md) of [Instances](Instances.md).
    
    It uses the *'INSTANCE'* string domain.
    """

    
    
    