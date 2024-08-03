#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : demos/arrows
---------------------
Generates modifiers which build a single arrow or a field of arrows

The field of arrows make use of 'Vectors' named attribute
Parameters for shader are passed through attributes:
    - Color
    - Transparency
    - Negative

Geometry Nodes
--------------
    - Arrows : a field of vectors
    - Arrow  : a single vector definef by cartesian components
    - Polar Arrow : a single vector defined by cylindrical components
    - Spherical Arrow : a single vector defined by cylindrical components

updates
-------
- creation : 2024/08/02
"""

from geonodes.script import *

def demo():

    print("\nCreate Arrows nodes...")

    # ====================================================================================================
    # Arrows field
    #
    # Take points as input geometry

    with GeoNodes("Arrows"):

        points     = Cloud()

        scale      = Float(     1,  "Scale", 0, tip = "Vectors multiplicator")
        resol      = Integer(  12,  "Resolution",  3, 64, tip = "Arrows shaft resolution")
        section    = Float(   .02,  "Section", 0., 1., tip = "Arrows shaft radius")
        use_sphere = Boolean(False, "Sphere", tip="Use a sphere for the head rather than a cone")
        color      = Color((0., 0., 1., 1.), "Color",  tip="Color to pass as 'Color' named attribute for shader")
        transp     = Float.Factor(0, "Transparency", 0, 1, tip="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = Float.Factor(0, "Negative",     0, 1, tip="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = Material("Arrow", "Shaft", tip="Material for the shaft")
        head_mat   = Material("Arrow", "Head", tip="Material for the head")
        show_arrow = Boolean(True, "Show", tip="Show / hide flag")

        vectors = Vector.Named("Vectors")

        with Layout("Length and rotation"):
            length = vectors.length*scale
            rot    = Rotation.AlignZToVector(vectors)

        with Layout("Arrow Heads"):

            with Layout("Cone"):
                cone_height = section*7
                cone = Mesh.Cone(vertices=2*resol, radius_bottom=section*3., depth=cone_height)
                cone.corners.store("UV Map", cone.uv_map_)

            with Layout("Sphere"):
                radius = section*4
                sphere_height = radius
                sphere = Mesh.UVSphere(segments=2*resol, rings=resol, radius=radius)
                sphere.corners.store("UV Map", sphere.uv_map_)

            head = cone.switch(use_sphere, sphere)
            head_height = cone_height.switch(use_sphere, sphere_height)
            ratio = length/(length + head_height)
            head.faces.material = head_mat

            with Layout("Instanciate heads"):
                heads = points.points.instance_on(instance=head, scale=(1, 1, ratio))
                heads.insts.rotation = rot
                heads.insts.translate(translation=vectors.scale((length*ratio)/vectors.length), local_space=False)

        with Layout("Arrow shafts"):
            shaft = Mesh.Cylinder(vertices=resol, radius=section, depth=1.)
            shaft.corners.store("UV Map", shaft.uv_map_)

            shaft = shaft.transform(translation=(0, 0, .5))
            shaft.faces.material = shaft_mat
            shafts = points.points.instance_on(instance=shaft, scale=(1, 1, length*ratio))
            shafts.insts.rotation = rot

        with Layout("Finalize"):

            shafts.insts[length.equal(0)].delete_geometry()
            heads.insts[length.equal(0)].delete_geometry()

            arrows = Mesh((shafts + heads).realize())
            arrows.faces.smooth = True

            arrows.points.store("Color",         color)
            arrows.points.store( "Transparency", transp)
            arrows.points.store( "Negative",     negative)

        arrows.switch((-show_arrow) | transp.equal(1)).out()

    # ----------------------------------------------------------------------------------------------------
    # Single Arrow defined by its cartesian components

    with GeoNodes("Arrow"):

        location   = Vector(0, "Location", tip="Vector location")
        vector     = Vector((1, 0, 0), "Vector", tip="Vector components")

        # ----- Create the points at the given location with Vectors attribute

        with Layout("One point with Vectors attribute"):
            points = Cloud.Points(count=1, position=location)
            points.points.store("Vectors", vector)

        # ----- Call the group with the same parameters

        group_node = Group("Arrows", {'Geometry': points})
        group_node.plug_node_into(exclude=['Geometry'], create=True)

        group_node.geometry.out()

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by cylindrical components

    with GeoNodes("Polar Arrow"):

        location   = Vector(0, "Location", tip="Vector location")
        length     = Float(1, "Length", 0, tip="Vector length")
        angle      = Float.Angle(0, "Angle", tip="Polar angle in plane XY")
        z          = Float(0, "z", tip="z component")

        # ----- Create the points at the given location with Vectors attribute

        with Layout("One point with Vectors attribute"):
            vector = Vector((length*gnmath.cos(angle), length*gnmath.sin(angle), z))
            points = Cloud.Points(count=1, position=location)
            points.points.store("Vectors", vector)

        # ----- Call the group with the same parameters

        group_node = Group("Arrows", {'Geometry': points})
        group_node.plug_node_into(exclude=['Geometry'], create=True)

        group_node.geometry.out()

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by its spherical components

    with GeoNodes("Spherical Arrow"):

        location   = Vector(0,      "Location",  tip="Vector location")
        length     = Float(1,       "Length",    0, tip="Vector length")
        theta      = Float.Angle(0, "Longitude", tip="Longitude : angle in XY plane")
        phi        = Float.Angle(0, "Latitude",  tip="Latitude : angle from XY plane to Z axis")

        # ----- Create the points at the given location with Vectors attribute

        with Layout("One point with Vectors attribute"):
            cos_phi = gnmath.cos(phi)
            vector = length*Vector((cos_phi*gnmath.cos(theta), cos_phi*gnmath.sin(theta), gnmath.sin(phi)))

            points = Cloud.Points(count=1, position=location)
            points.points.store("Vectors", vector)

        # ----- Call the group with the same parameters

        group_node = Group("Arrows", {'Geometry': points})
        group_node.plug_node_into(exclude=['Geometry'], create=True)

        group_node.geometry.out()
