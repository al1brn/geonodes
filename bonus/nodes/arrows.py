#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul  5 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : arrows
---------------

Generates Geometry Nodes to generate arrows. Arrows have the exact size. They can be generated
from points to generate a field of vectors.
They can also be generated individually, either from cartesian, cylindrical or spherical coordinates.


The field of arrows make use of 'Vectors' named attribute
Parameters for shader are passed through attributes:
    - Color
    - Transparency
    - Negative

Default material name is Arrow with is generated by this module

Shaders
-------
    - Arrow

Geometry Nodes
--------------
    - Arrows : a field of vectors
    - Arrow  : a single vector definef by cartesian components
    - Polar Arrow : a single vector defined by cylindrical components
    - Spherical Arrow : a single vector defined by cylindrical components

    - Intensity to Raidus : convert the curve 'Intensity' attribute to radius
    - To Lines of Field : transform curve to lines
    - Field Curve to Mesh : transform a field curve to mesh combining lines and arrows
"""

import bpy
import geonodes as gn

def build_arrows(create_shaders=False):

    print("\nCreate Arrows shaders and nodes...")

    # ====================================================================================================
    # Default Shader for Arrow

    if not gn.Shader.tree_exists("Arrow") or create_shaders:
        with gn.Shader("Arrow") as tree:

            pos_color = tree.Attribute(attribute_type='GEOMETRY', attribute_name="Color").vector
            negative  = tree.Attribute(attribute_type='GEOMETRY', attribute_name="Negative").fac
            transp    = tree.Attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

            neg_color = tree.HueSaturationValue(color=pos_color, hue=.5, saturation=.9, value=.9).color
            color = pos_color.mix(negative, neg_color).result

            ped = tree.PrincipledBSDF(
                base_color = color,
                roughness  = negative.map_range(to_min=.1, to_max=.9),
            ).bsdf

            shader = tree.MixShader(fac=transp, shader=ped, shader_1=tree.TransparentBSDF().bsdf).shader

            tree.surface = shader

    # ====================================================================================================
    # Geometry Nodes

    # ----------------------------------------------------------------------------------------------------
    # Arrows field

    with gn.GeoNodes("Arrows", fake_user=True) as tree:

        points     = tree.geometry

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vectors multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrows shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrows shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show / hide flag")

        vectors = points.POINT.named_vector("Vectors")

        with tree.layout("Length and rotation"):
            length = vectors.length()*scale
            rot    = tree.AlignEulerToVector(axis='Z', vector=vectors).rotation

        with tree.layout("Arrow Heads"):

            with tree.layout("Cone"):
                cone_height = section*7
                cone = tree.Cone(vertices=2*resol, radius_bottom=section*3., depth=cone_height).mesh

            with tree.layout("Sphere"):
                radius = section*4
                sphere_height = radius
                sphere = tree.UVSphere(segments=2*resol, rings=resol, radius=radius).mesh
                #sphere.transform_geometry(translation=(0, 0, radius))

            head = cone.switch(use_sphere, sphere)
            head_height = cone_height.switch(use_sphere, sphere_height)
            ratio = length/(length + head_height)
            head.set_material(head_mat)

            with tree.layout("Instanciate heads"):
                heads = points.instance_on_points(instance=head, scale=(1, 1, ratio))
                heads.rotate_instances(rotation=rot)
                heads.translate_instances(translation=vectors.scale((length*ratio)/vectors.length()), local_space=False)

        with tree.layout("Arrow shafts"):
            cyl_node = tree.Cylinder(vertices=resol, radius=section, depth=1.)
            shaft = cyl_node.mesh
            shaft.CORNER.store_named_float2("uvmap", cyl_node.uv_map)

            shaft.transform_geometry(translation=(0, 0, .5))
            shaft.set_material(shaft_mat)
            shafts = points.instance_on_points(instance=shaft, scale=(1, 1, length*ratio))
            shafts.rotate_instances(rotation=rot)

        with tree.layout("Finalize"):

            shafts.INSTANCE[length.equal(0)].delete_geometry()
            heads.INSTANCE[length.equal(0)].delete_geometry()

            arrows = (shafts + heads).realize_instances()
            arrows.FACE.set_shade_smooth()

            arrows.POINT.store_named_vector("Color",  color)
            arrows.POINT.store_named_float( "Transparency", transp)
            arrows.POINT.store_named_float( "Negative",     negative)


        tree.geometry = arrows.switch(-show_arrow | transp.equal(1))


    # ----------------------------------------------------------------------------------------------------
    # Single Arrow defined by its cartesian components

    with gn.GeoNodes("Arrow", fake_user=True) as tree:

        location   = tree.vector_input(      "Location", description="Vector location")
        vector     = tree.vector_input(      "Vector",       (1, 0, 0), description="Vector components")

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vector multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrow shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrow shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show +/ hide flag")

        points = tree.Points(count=1, position=location).points
        points.POINT.store_named_vector("Vectors", vector)

        tree.geometry = tree.group("Arrows", points,
            scale        = scale,
            resolution   = resol,
            section      = section,
            sphere       = use_sphere,
            color        = color,
            transparency = transp,
            negative     = negative,
            shaft        = shaft_mat,
            head         = head_mat,
            show         = show_arrow,
            ).geometry

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by cylindrical components

    with gn.GeoNodes("Polar Arrow", fake_user=True) as tree:

        location   = tree.vector_input(      "Location", description="Vector location")
        length     = tree.float_input(       "Length",   1., min_value=0, description="Vector length")
        angle      = tree.angle_input(       "Angle",    0., description="Polar angle in plane XY")
        z          = tree.float_input(       "z",        0., description="z component")

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vector multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrow shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrow shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show +/ hide flag")

        vector = tree.vector((length*tree.cos(angle), length*tree.sin(angle), z))

        points = tree.Points(count=1, position=location).points
        points.POINT.store_named_vector("Vectors", vector)

        tree.geometry = tree.group("Arrows", points,
            scale        = scale,
            resolution   = resol,
            section      = section,
            sphere       = use_sphere,
            color        = color,
            transparency = transp,
            negative     = negative,
            shaft        = shaft_mat,
            head         = head_mat,
            show         = show_arrow,
            ).geometry

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by its spherical components

    with gn.GeoNodes("Spherical Arrow", fake_user=True) as tree:

        location   = tree.vector_input(      "Location",  description="Vector location")
        length     = tree.float_input(       "Length",    1., min_value=0, description="Vector length")
        theta      = tree.angle_input(       "Longitude", 0., description="Longitude : angle in XY plane")
        phi        = tree.angle_input(       "Latitude",  0., description="Latitude : angle from XY plane to Z axis")

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vector multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrow shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrow shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show +/ hide flag")

        cos_phi = tree.cos(phi)
        vector = length*tree.vector((cos_phi*tree.cos(theta), cos_phi*tree.sin(theta), tree.sin(phi)))

        points = tree.Points(count=1, position=location).points
        points.POINT.store_named_vector("Vectors", vector)

        tree.geometry = tree.group("Arrows", points,
            scale        = scale,
            resolution   = resol,
            section      = section,
            sphere       = use_sphere,
            color        = color,
            transparency = transp,
            negative     = negative,
            shaft        = shaft_mat,
            head         = head_mat,
            show         = show_arrow,
            ).geometry

    # ====================================================================================================
    # Lines

    # ----------------------------------------------------------------------------------------------------
    # Convert 'Intensity' to curve radius

    with gn.GeoNodes("Intensity to Radius") as tree:

        curve = tree.geometry

        min_radius = tree.float_input("Min Radius", .001)
        max_radius = tree.float_input("Max Radius", .1)
        factor     = tree.float_input("Factor",      1., min_value=0)

        intensity = curve.named_float("Intensity")

        node = curve.POINT.attribute_statistic_float(attribute=intensity)

        min_int, max_int = node.min, node.max
        ampl = max_int - min_int

        radius = min_radius + (max_radius - min_radius)*tree.exp(-factor*(intensity - min_int)**(-2))

        curve.POINT.radius=radius

        tree.geometry = curve

    # ----------------------------------------------------------------------------------------------------
    # Convert lines of field to mesh
    # Uses the 'intensity' attribute to compute the section

    with gn.GeoNodes("To Lines of Field", fake_user=True) as tree:

        resol      = tree.int_input(       "Resolution",       12, min_value=3, max_value=64, description="Lines geometry resolution")
        radius     = tree.float_input(     "Radius",           .02, min_value=0., max_value=1., description="Lines radius")
        min_radius = tree.float_input(     "Min Radius",       0, min_value=0., max_value=1., description="Minimum lines radius")
        int_fac    = tree.factor_input(    "Intensity factor", 0., min_value=0., max_value=1., description="Radius proportional to 'Intensity' named attribute")

        transp = tree.factor_input(     "Transparency",     0., min_value=0., max_value=1., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        color  = tree.color_input(      "Color",            (.7, .2, .2, 1.), description = "Color to pass as 'Color' named attribute for shader")
        mat    = tree.material_input(   "Material", description="Lines material")
        show   = tree.bool_input(       "Show",             True, description="Show / Hide flag")

        # ----------------------------------------------------------------------------------------------------
        # Main

        with tree.layout("Curves"):
            comps_node = tree.geometry.separate_components()
            curves = comps_node.curve + comps_node.mesh.mesh_to_curve()

        curves.store_named_vector("Color", color)
        curves.store_named_float("Transparency", transp)

        with tree.layout("Intensity"):
            curves = tree.group("Intensity to Radius",
                geometry   = curves,
                min_radius = min_radius,
                max_radius = radius,
                factor     = int_fac,
            ).geometry

            mesh = curves.curve_to_mesh(profile_curve=tree.CurveCircle(radius=1, resolution=resol).curve)

        mesh.FACE.material     = mat
        mesh.FACE.shade_smooth = True

        # ----- Done

        tree.geometry = mesh.switch(-show)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Field curve as lines or set of vectors

    with gn.GeoNodes("Field Curve to Mesh") as tree:

        show_lines   = tree.bool_input(     "Show Lines",           True)
        line_int_fac = tree.factor_input(   "Intensity",            1., min_value=0., max_value=1.)
        line_section = tree.float_input(    "Lines Section",        .02, min_value=0., max_value=1.)
        min_line_sec = tree.float_input(    "Min Lines Section",     0, min_value=0., max_value=1.)
        line_color   = tree.color_input(    "Lines Color",          (0, 1, 0, 1))
        line_transp  = tree.factor_input(   "Lines Transparency",   0., min_value=0., max_value=1.)
        line_mat     = tree.material_input( "Lines Material",       "Arrow")

        show_arrows  = tree.bool_input(     "Show Arrows",          True)
        ar_scale     = tree.float_input(    "Scale",                1., min_value=0.)
        ar_dist      = tree.float_input(    "Distance",             .5, min_value=.1)
        ar_section   = tree.float_input(    "Section",              .02, min_value=0., max_value=1.)
        ar_color     = tree.color_input(    "Color",                (0, 1, 0, 1))
        ar_transp    = tree.factor_input(   "Transparency",         0., min_value=0., max_value=1.)
        ar_mat       = tree.material_input( "Material",             "Arrow")

        with tree.layout("Lines of field"):

            line_curves = tree.group("Intensity to Radius",
                        geometry   = tree.geometry,
                        min_radius = min_line_sec,
                        max_radius = line_section,
                        factor     = line_int_fac,
                        ).geometry

            line_mesh = line_curves.curve_to_mesh(profile_curve = tree.CurveCircle(radius=1., resolution=12).curve)
            line_mesh.FACE.shade_smooth = True
            line_mesh.FACE.material     = line_mat
            line_mesh.store_named_vector("Color", line_color)
            line_mesh.store_named_float( "Transparency", line_transp)
            line_mesh = line_mesh.switch(-show_lines)

        with tree.layout("Arrows"):

            curves = tree.geometry
            node = curves.curve_to_points(length=ar_dist, mode='LENGTH')
            points = node.points
            points.POINT.store_named_vector("Vectors", node.tangent*points.POINT.named_float("Intensity"))

            arrows = tree.group("Arrows",
                geometry     = points,
                scale        = ar_scale,
                section      = ar_section,
                color        = ar_color,
                transparency = ar_transp,
                shaft        = ar_mat,
                head         = ar_mat,
                show         = show_arrows,
                ).geometry


        tree.geometry = line_mesh + arrows