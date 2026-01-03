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
- update :   2025/12/08 # V5

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
from geonodes import macros


# ====================================================================================================
# Create a cylinder with UV
# ====================================================================================================

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
    with GeoNodes("Arrows"):
        
        # ---------------------------------------------------------------------------
        # Different heads
        # ---------------------------------------------------------------------------
        
        with Layout("Head factory"):
            
            # Simple Cone
            
            with Closure() as cone_cl:
                scale = 4
                
                radius = Float(0.05, "Radius")
                aspect = Float(0.5, "Aspect")*scale
                height = radius*scale
                cone = Mesh.Cone(
                    vertices        = Input("Resolution", default_value = 12),
                    side_segments   = 2,
                    radius_top      = 0.0,
                    radius_bottom   = radius*(1 + aspect),
                    depth           = height,
                )
                macros.move_coordinate(cone, height/2, -height/2 + 0.002, summit=height)
                cone.out("Head")
                height.out("Height")
                
            head_sig = cone_cl.get_signature()
            
            # Sphere

            with Closure() as sphere_cl:
                scale = 2.5
                
                radius = Float(0.05, "Radius")
                aspect = Float(0.5, "Aspect")*scale
                resol  = Integer(12, "Resolution")
                sphere = Mesh.UVSphere(
                    segments = resol*2,
                    rings    = resol,
                    radius   = radius*(1 + aspect),
                )
                sphere.transform(translation=(0, 0, radius*.9))
                sphere.out("Head")
                (radius*1.9).out("Height")
                
            # Cylinder
            
            with Closure() as cyl_cl:
                scale = 2.
                
                radius = Float(0.05, "Radius")*scale
                aspect = Float(0.5, "Aspect")
                resol  = Integer(12, "Resolution")
                height = radius*0.5
                cyl = Mesh.Cylinder(
                    vertices = resol,
                    radius = radius*(1 + aspect),
                    depth = height
                )
                cyl.transform(translation=(0, 0, height/2))
                cyl.out("Head")
                height.out("Height")
                
            # None
            with Closure() as nul_cl:
                # Input are connected to avoid warnings
                a  = Float(0.05, "Radius")
                a += Float(.55, "Aspect")
                a += Integer(12, "Resolution")

                Geometry.Switch().out("Head")
                Float(a*0.).out("Height")
        
        # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        # Group input
        
        cloud = Cloud()
        
        vectors = Vector((0, 0, 1), name="Vectors")
        
        with Panel("Shaft"):
            radius  = Float(.05, "Radius", shape="Single")
            resol   = Integer(12, "Resolution")
            mat     = Material(None, "Material")
            
        # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        
        with Layout("Preparation"):

            vec = cloud.points.capture(vectors)
            nvec = vec.normalize()
            lens = vec.length()
            rot = Rotation().align_z_to_vector(vec)
            
            shaft_len = lens
            max_head_height = lens/4
            pivot = cloud.points.sample_index(nd.position, nd.index)
            
        # ---------------------------------------------------------------------------
        # Twice the same code for bottom and top head
        # ---------------------------------------------------------------------------
        
        for ihead, (panel, default) in enumerate([
            ('Top',     'Cone'), 
            ('Bottom',  'None')
            ]):
            
            # Inputs
            
            with Layout(panel):

                with Panel(panel):
                    with Closure.MenuSwitch() as cl:
                        nul_cl.out("None")
                        cone_cl.out("Cone")
                        sphere_cl.out("Sphere")
                        cyl_cl.out("Flat")
                        
                    cl.node.menu = Input("Head", default_value=default)
                
                    head = cl.evaluate(signature=head_sig, 
                        radius=radius, 
                        resolution=resol,
                        aspect = Float.Factor(.5, "Aspect", 0, 1))
                    height = head.height
                    has_head = height.greater_than(0)
                
                    head.material = Material(None, "Material")
                    
                    # Rotate 180° if bottom
                    if ihead == 1:
                        head.transform(rotation=(0, pi, 0), translation=(0, 0, height))
                    
                # Actual head heigh cant' be greater that one 4th
                heights = gnmath.min(height, max_head_height)
                shaft_len = shaft_len.switch(has_head, shaft_len - heights)
                
                heads = cloud.points[lens.greater_than(0.001)].instance_on(
                    instance = head,
                    rotation = rot,
                    scale = (1, 1, heights/height),
                ).instances_
                
                # Top specific
                if ihead == 0:
                    heads.offset = nvec.scale(lens - heights)
                    the_heads = heads
                
                # Bottom specific
                else:
                    shaft_offset = Float.Switch(has_head, 0., heights)                    
                    the_heads += heads
                
        # ---------------------------------------------------------------------------
        # Shafts
        # ---------------------------------------------------------------------------

        with Layout("Shaft"):
            cyl = Mesh.Cylinder(
                vertices        = resol,
                side_segments   = 3, 
                radius          = radius, 
                depth           = 1,
                ).transform(translation=(0, 0, .5))
            cyl.material = mat
            macros.move_coordinate(cyl, 1/3, -1/3 + 0.002)
            macros.move_coordinate(cyl, 2/3, 1/3 - 0.002)
            
            cyls = cloud.points[lens.greater_than(0.001)].instance_on(
                instance = cyl,
                #rotation = rot,
                scale = Vector.CombineXYZ(1, 1, shaft_len),
            )
            cyls.offset = Vector.CombineXYZ(0, 0, shaft_offset)
            cyls.rotate(rot, pivot_point=pivot, local_space=False)
            
        with Layout("Finalize"):
            mesh = Mesh(cyls + the_heads)
            mesh.faces.shade_smooth = Boolean(True, "Smooth")
            mesh.enable_output(Boolean(True, "Show"))
            
        mesh.out()
        
    # ===========================================================================
    # Single Arrow
    # ===========================================================================

    with GeoNodes("Arrow"):
        
        pos = Vector(name="Position", shape="Single")
        
        with Panel("Vector"):
        
            with Vector.MenuSwitch(default_menu="XYZ", menu=Input("Vector")) as vec:
                
                Vector((0, 0, 1), "Vector").out("XYZ")
                
                v = G().combine_cylindrical()
                v.node.link_inputs()
                v.out("Cylindrical")
                
                v = G().combine_spherical()
                v.node.link_inputs()
                v.out("Spherical")
            
        cloud = Cloud.Points(1, position=pos)
        
        arr = Group("Arrows", cloud=cloud, vectors=vec).link_inputs()._out
        
        arr.out()
