"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demo arrows
--------------------

Building arrows

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/01/25 # UV Cylinder

$ DOC START

[Source Code](../demos/arrows.py)

This demo provides four modifiers:
- Arrows :
  Display a field of arrows on the geometry points
- Arrow :
  A single arrows defined by its cartesian coordinates
- Polar Arrow :
  A single arrows defined by its polar coordinates
- Spherical Arrow :
  A single arrows defined by its spherical coordinates

In addition, the "Arrows Show Case" gives an example on the use or Arrows modifier.

> [!NOTE]
> Modifiers:
> - Arrows
> - Arrow
> - Polar Arrow
> - Spherical Arrows
> - Arrows Show Case

``` python
from geonodes.demos import arrows

arrows.demo()
```
"""

from geonodes import *

def uv_cylinder():
    with GeoNodes("UV Cylinder"):

        curve       = Curve(None, "Curve")
        profile     = Curve(None, "Profile Curve")
        fill_caps   = Boolean(False, "Fill Caps", tip="Caps are flagged with 'Cap', Boolean named attribute")
        true_length = Boolean(False, "True Length UV", tip="UV Mapped is mapped in true length")

        with Layout("Replace the profile curve by aline"):
            count = profile.points.count
            line = Curve.LinePoints().resample(count+1)
            line.points._T_u = Spline.parameter_factor

        with Layout("Curve to Mesh with open line"):
            t_curve = Curve(curve)
            t_curve.points._T_v = Spline.parameter_factor

            mesh = t_curve.to_mesh(profile_curve=line, fill_caps=False)
            uv = Vector((Float("T u"), Float("T v"), 0))

        with Layout("Curve to mesh with true profile and possible caps"):
            final = curve.to_mesh(profile_curve=profile, fill_caps=fill_caps)
            uv_map = mesh.corners.sample_index(uv, index=nd.index)
            uv_map = uv_map.switch(true_length, uv_map*(profile.length(), curve.length(), 1))
            final.corners[:mesh.corners.count].store_uv("UV Map", uv_map)

        with Layout("Cap faces if any"):
            final.faces._Cap = Boolean.Switch(fill_caps, False, nd.index >= final.faces.count - 2)

        final.out()



def demo():

    print("\nCreate Arrows nodes...")

    uv_cylinder()

    with ShaderNodes("Arrow"):

        pos_color = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        negative  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Negative").factor
        transp    = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        neg_color = pos_color.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        color = pos_color.mix(negative, neg_color)

        ped = Shader.Principled(
            base_color = color,
            roughness  = negative.map_range(to_min=.1, to_max=.9),
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)

        shader.out()

    with ShaderNodes("Arrow Helix"):

        color0    = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color 0").color)
        color1    = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color 1").color)
        negative  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Negative").factor
        transp    = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        neg_color0 = color0.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        neg_color1 = color1.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        color0 = color0.mix(neg_color0, negative)
        color1 = color1.mix(neg_color1, negative)

        uv = snd.texture_coordinate().uv
        x, y, _ = uv.xyz

        color = color0.mix(color1, (x + y) % .5)

        ped = Shader.Principled(
            base_color = color,
            roughness  = negative.map_range(to_min=.1, to_max=.9),
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)

        shader.out()


    # ====================================================================================================
    # Arrows field
    #
    # Take points as input geometry

    with GeoNodes("Arrows"):

        cloud   = Cloud(name='Geometry')
        vectors = Vector( 0, "Vector", tip="Vector at each point")

        with Panel("Arrows"):
            scale      = Float(     1,           "Scale", 0,            tip="Vectors multiplicator")
            use_log    = Boolean(False,          "Logarithm",           tip="Use a logarithm of vector lengths", single_value=True)
            negative   = Float.Factor(0,         "Negative",     0, 1,  tip="Negative factor to pass as 'Negative', named attribute for shader")

        with Panel("Appearance"):
            resol      = Integer(  12,           "Resolution",  3, 64,  tip="Arrows shaft resolution", single_value=True)
            section    = Float(   .02,           "Section", 0., 1.,     tip="Arrows shaft radius", single_value=True)
            use_sphere = Boolean(False,          "Sphere",              tip="Use a sphere for the head rather than a cone", single_value=True)
            color      = Color((0., 0., 1., 1.), "Color",               tip="Color to pass as 'Color' named attribute for shader", single_value=True)

            shaft_mat  = Material("Arrow",       "Shaft",               tip="Material for the shaft")
            head_mat   = Material("Arrow",       "Head",                tip="Material for the head")
            show_arrow = Boolean(True,           "Show",                tip="Show / hide flag")

        with Layout("Vectors"):
            vectors = cloud.points.capture(vectors)

        with Layout("Length and rotation"):
            vect_len = vectors.length()._lc("Vector length")
            length   = (vect_len*scale).switch(use_log, gnmath.log(1 + vect_len, base=(1.001 + scale)))
            rot      = Rotation.AlignZToVector(vector=vectors)

        with Layout("Arrow Heads"):

            with Layout("Cone"):
                cone_height = section*7
                cone = Mesh.Cone(vertices=2*resol, radius_bottom=section*3., depth=cone_height)
                cone.corners.store_uv("UV Map", cone.uv_map_)

            with Layout("Sphere"):
                radius = section*4
                sphere_height = radius
                sphere = Mesh.UVSphere(segments=2*resol, rings=resol, radius=radius)
                sphere.corners.store_uv("UV Map", sphere.uv_map_)

            head = cone.switch(use_sphere, sphere)
            head_height = cone_height.switch(use_sphere, sphere_height)
            ratio = length/(length + head_height)

            head.material = head_mat

            with Layout("Instanciate heads"):
                heads = cloud.instance_on(instance=head, scale=(1, 1, ratio))
                heads.insts.rotation = rot
                heads.translate(translation=vectors * ((length*ratio)/vect_len), local_space=False)

        with Layout("Arrow shafts"):
            shaft = Mesh.Cylinder(vertices=resol, radius=section, depth=1.)
            shaft.corners.store_uv("UV Map", shaft.uv_map_)

            shaft = shaft.transform(translation=(0, 0, .5))
            shaft.material = shaft_mat
            shafts = cloud.instance_on(instance=shaft, scale=(1, 1, length*ratio))
            shafts.insts.rotation = rot

        with Layout("Finalize"):

            shafts = shafts.insts[length.equal(0)].delete_geometry()
            heads  = heads.insts[length.equal(0)].delete_geometry()

            arrows = Mesh((shafts + heads).realize())
            arrows.faces.smooth = True

            arrows.points._Color        = (color.red, color.green, color.blue)
            arrows.points._Transparency = 1 - color.alpha
            arrows.points._Negative     = negative

        arrows.switch((-show_arrow) | color.alpha.equal(0)).out()

    # ----------------------------------------------------------------------------------------------------
    # Single Arrow defined by its cartesian components

    with GeoNodes("Arrow"):

        location = Vector(0, "Location", tip="Vector location")
        vector   = Vector((1, 0, 0), "Vector", tip="Vector components", single_value=True)

        # ----- Create the points at the given location with Vectors attribute

        with Layout("One point with Vectors attribute"):
            cloud = Cloud.Points(count=1, position=location)

        # ----- Call the group with the same parameters

        Group("Arrows", {'Geometry': cloud}, link_from='TREE').out()

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by cylindrical components

    with GeoNodes("Polar Arrow"):

        location = Vector(0, "Location", tip="Vector location")
        length   = Float(1, "Length", 0, tip="Vector length")
        angle    = Float.Angle(0, "Angle", tip="Polar angle in plane XY")
        z        = Float(0, "z", tip="z component")

        # ----- Create the points at the given location with Vectors attribute

        with Layout("One point with Vectors attribute"):
            vector = Vector((length*gnmath.cos(angle), length*gnmath.sin(angle), z))
            cloud = Cloud.Points(count=1, position=location)

        # ----- Call the group with the same parameters

        Group("Arrows", {'Geometry': cloud, 'Vector': vector}, link_from='TREE').out()

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by its spherical components

    with GeoNodes("Spherical Arrow"):

        location = Vector(0,      "Location",  tip="Vector location")
        length   = Float(1,       "Length",    0, tip="Vector length")
        theta    = Float.Angle(0, "Longitude", tip="Longitude : angle in XY plane")
        phi      = Float.Angle(0, "Latitude",  tip="Latitude : angle from XY plane to Z axis")

        # ----- Create the points at the given location with Vectors attribute

        with Layout("One point with Vectors attribute"):
            cos_phi = gnmath.cos(phi)
            vector = length*Vector((cos_phi*gnmath.cos(theta), cos_phi*gnmath.sin(theta), gnmath.sin(phi)))

            cloud = Cloud.Points(count=1, position=location)

        # ----- Call the group with the same parameters

        group_node = Group("Arrows", {'Geometry': cloud, 'Vector': vector}, link_from='TREE').out()

    # ----------------------------------------------------------------------------------------------------
    # Any Arrow

    with GeoNodes("Curve to Arrow"):

        curve = Curve()

        show_start = Boolean(False,          "Arrow at curve start")
        show_end   = Boolean(True,           "Arrow at curve end")

        trim0      = Float.Factor(0,         "Trim Sart", 0, 1,     tip="Curve trim start")
        trim1      = Float.Factor(1,         "Trim End", 0, 1,      tip="Curve trim end")
        resamp     = Integer(32,             "Resample", 10)
        resol      = Integer(  12,           "Resolution",  3, 64,  tip="Arrows shaft resolution", single_value=True)
        section    = Float(   .02,           "Section", 0., 1.,     tip="Arrows shaft radius", single_value=True)
        color0     = Color((0., 0., 1., 1.), "Color 0",             tip="First color to pass as 'Color 0' named attribute for shader", single_value=True)
        color1     = Color((1., 0., 0., 1.), "Color 1",             tip="Second color to pass as 'Color 1' named attribute for shader", single_value=True)

        shaft_mat  = Material("Arrow",       "Shaft",               tip="Material for the shaft")
        head_mat   = Material("Arrow",       "Head",                tip="Material for the head")
        show_arrow = Boolean(True,           "Show",                tip="Show / hide flag")

        with Layout("Prepare curve"):
            curve = curve.resample(resamp)
            curve.trim_factor(start=trim0, end=trim1)

        with Layout("Shaft"):

            shaft = Mesh(G().uv_cylinder(curve, Curve.Circle(radius=section, resolution=resol), fill_caps=True))
            shaft.faces.material = shaft_mat

        with Layout("Cone"):
            cone_height = section*7
            cone = Mesh.Cone(vertices=2*resol, radius_bottom=section*3., depth=cone_height)
            cone.corners.store_uv("UV Map", cone.uv_map_)
            cone.faces.material = head_mat

        with Layout("Ends"):

            node0 = curve.sample_factor(factor=0).node
            head = Mesh(cone).transform(translation=node0.position, rotation=Rotation.AlignZToVector(-node0.tangent))
            geo = head.switch_false(show_start)

            node1 = curve.sample_factor(factor=1).node
            head = Mesh(cone).transform(translation=node1.position, rotation=Rotation.AlignZToVector(node1.tangent))
            geo += head.switch_false(show_end)

        geo += shaft
        geo.faces.smooth = True
        geo.faces._Color   = color0
        geo.faces._Color_1 = color1


        show_arrow &= trim1 > trim0
        geo.switch_false(show_arrow).out()


        node0.position.out("Start")
        node1.position.out("End")
        node0.tangent.out("Start Tangent")
        node1.tangent.out("End Tangent")



    # ----------------------------------------------------------------------------------------------------
    # Show case

    with GeoNodes("Arrows Show Case"):

        count = Integer(100, "Count", 10, single_value=True)
        seed = Integer(0, "Seed", single_value=True)

        cloud = Cloud.Points(count=count, position=Vector.Random(-10, 10, seed=seed))

        Group("Arrows", geometry=cloud, vector=Vector.Random(-1, 1, seed=seed + 1), link_from='TREE').out()
