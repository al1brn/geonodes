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

!!! note
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
from .shaders import arrow_shader


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

    # ====================================================================================================
    # Default Shader for Arrow
    # ====================================================================================================

    arrow_shader()

    # ====================================================================================================
    # Spherical to arrow
    # ====================================================================================================

    with GeoNodes("Vector Input", is_group=True):

        xyz = Vector((1, 0, 0), "Vector")

        r = Float(1.0, "Radius")
        theta = Float.Angle(0, "Theta")
        phi = Float.Angle(0, "Phi")
        z = Float(0.0, "z")

        with Vector.MenuSwitch(menu=Input("Type")) as V:
            xyz.out("XYZ")

        with V:
            cp, sp = phi.cos(), phi.sin()
            ct, st = theta.cos(), theta.sin()
            rp = cp*r
            Vector((rp*ct, rp*st, r*sp)).out("Spherical")

        with V:
            Vector((r*ct, r*st, z)).out("Cylindrical")

        V.out()


    # ====================================================================================================
    # Field of arrows
    # ====================================================================================================

    with GeoNodes("Arrows"):
        
        # ---------------------------------------------------------------------------
        # Different heads
        # ---------------------------------------------------------------------------
        
        with Layout("Head factory"):
            
            # Simple Cone
            
            with Closure() as cone_cl:
                bot_size = 3.4
                height_scale = 20
                height_min = 2
                
                radius = Float(0.05, "Radius")
                aspect = (Float(0.5, "Aspect")*height_scale + height_min)._lc("Aspect")
                height = (radius*aspect)._lc("Height")
                cone = Mesh.Cone(
                    vertices        = Input("Resolution", default_value = 12),
                    side_segments   = 2,
                    radius_top      = 0.0,
                    radius_bottom   = radius*bot_size,
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
        col     = Color("Blue", "Color")
        
        with Panel("Shaft"):
            radius  = Float(.05, "Radius", shape="Single")
            resol   = Integer(12, "Resolution")
            mat     = Material("Arrow", "Material")
            
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
                
                    head.material = Material("Arrow", "Material")
                    
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
                    #heads.offset = nvec.scale(lens - heights)
                    heads.offset = nvec.scale(lens)
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
                scale = Vector.CombineXYZ(1, 1, shaft_len),
            )
            cyls.offset = Vector.CombineXYZ(0, 0, shaft_offset)
            cyls.rotate(rot, pivot_point=pivot, local_space=False)
            
        with Layout("Finalize"):
            mesh = Mesh(cyls + the_heads)
            mesh.faces.Color = col
            mesh.faces.shade_smooth = Boolean(True, "Smooth")
            mesh.enable_output(Boolean(True, "Show"))
            
        mesh.out()
        
    # ===========================================================================
    # Single Arrow
    # ===========================================================================

    with GeoNodes("Arrow"):
        
        pos = Vector(name="Position", shape="Single")
        
        with Panel("Vector"):

            if True:
                vec = G().vector_input().link_inputs()
            else:
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

    # ===========================================================================
    # Screw
    # ===========================================================================

    with GeoNodes("Screw"):
        
        show = Boolean(True, "Show")
        
        pos    = Vector(0,         "Positition")
        vec    = Vector((0, 0, 1), "Vector")
        rot    = Float.Angle(0,    "Rotation")
        
        with Panel("Shape"):
            radius = Float(0.1,        "Radius")
            thread = Float(0.6,        "Thread", 0.01)
            aspect = Float.Factor(0.5, "Aspect", 0, 1)
            
        with Panel("Appearance"):
            resol  = Integer(30,       "Resolution", 10, 500)
            mat    = Material("Arrow", "Material")
            color  = Color("blue",     "Color")
            transp = Float(0,          "Transparency", 0, 1)
            
        with Layout("Base Line"):
            
            line = Curve.Line(pos, pos + vec).resample(count = resol)
            
            with Layout("Tilt"):
                line.tilt = (nd.spline_parameter().length/thread)*tau + rot
                
            with Layout("Radius"):
                t = 1.0 - nd.spline_parameter().factor
                exp = aspect.map_range(to_min=.3, to_max=1)
                line.radius = (t**exp)*radius
                
        with Layout("Profile"):
            
            prof = Curve.Circle(resolution=32).transform(scale=(1, .2, 0))
            
            
        with Layout("Screw"):
            
            screw = line.to_mesh(profile_curve=prof, scale=nd.radius, fill_caps=True)
            
            screw.faces.material = mat
            screw.faces.Color = color
            screw.faces.Transparency = transp
            
        screw.switch_false(show & (vec.length() > 0.001) & (transp < 0.999)).out()


    # ===========================================================================
    # 2D arrow
    # ===========================================================================

    with GeoNodes("2D Arrow"):

        pos = Vector(None, "Position")
        V = Vector((1, 0, 0), "Vector", dimensions=2)
        use_arrow = Boolean(True, "Head")
        size = Float(0.05, "Size")
        mat = Material("Arrow", "Material")
        col = Color("Blue", "Color")
        transp = Float.Factor(0.0, "Transparency")

        with Layout("Preparation"):
            s2 = (size/2)._lc("Half Size")
            V *= (1, 1, 0)
            l = V.length()._lc("Length")

            head_length = gnmath.min(l, size*5)._lc("Head Length")
            head_width  = (size*3)._lc("Head Width")
            head_back   = gnmath.min(head_length*0.2)._lc("Head Back")

        with Mesh.Switch(use_arrow) as arrow:

                x0, y0 = 0.0, -s2
                x2, y2 = l - head_length, -head_width/2
                x1, y1 = x2 + head_back, y0
                x3, y3 = l, 0.0

                circle = Mesh.Circle(vertices=7, fill_type="N-Gon")
                circle[0].position = (x0,  y0, 0)
                circle[1].position = (x1,  y1, 0)
                circle[2].position = (x2,  y2, 0)
                circle[3].position = (x3,  y3, 0)
                circle[4].position = (x2, -y2, 0)
                circle[5].position = (x1, -y1, 0)
                circle[6].position = (x0, -y0, 0)

                circle.out("True")

        with arrow:
            mesh = Mesh.Grid(size_x=l, size_y=size, vertices_x=2, vertices_y=2)
            mesh.offset = (l/2, 0, 0)
            mesh.out("False")

        with Layout("Finalize"):
            arrow = Mesh(arrow)
            arrow.faces.material = mat
            arrow.faces.Color = col
            arrow.faces.Transparency = transp

            arrow.transform(translation=pos, rotation=Rotation().align_to_vector(vector=V, axis='X'))

        arrow.out()









        
            
                    
