"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2026 Alain Bernard.

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

module : demo book
------------------

Animated open book made from curve profiles. The demo builds the geometry node
groups used to describe sheet shapes, place them along a binding, animate page
turns, and convert the result to renderable meshes with page and cover materials.

updates
-------
- creation : 2026/05/25
- update :   2026/05/26 # animated sheets, cover mesh and page shaders
- update :   2026/05/27 # profile bundles and book demo modifier

This demo provides shader helpers and the following modifiers / groups:

> Shaders:
> - Image Selector
> - Page {i}
>
> Modifiers:
> - Binding
> - Binding Closure
> - Profile Parameters
> - Profile Parameters Change
> - Profile Parameters Mix
> - Sheet Profile
> - Sheets On To
> - Book Sheets
> - Curve to Chain
> - Sheet Interpolate
> - Book Sheets Animated
> - Book Extrude
> - Set Sheet Material
> - Book Demo

Principle:

1. A book is structured as **n sheets**. Sheet 0 is the front cover and sheet
   n-1 is the back cover.
2. The n sheets are attached to one **Binding** curve.
3. Sheets are first described as curves in profile view, then extruded along
   the book height by **Book Extrude**.
4. The cover and back are special sheets: they are merged with the binding,
   then extruded with a thickness.
5. Regular sheets, excluding cover and back, receive random ``Page xxx``
   materials. These materials must be created beforehand with
   :func:`page_shaders`.
6. Precise page material assignment can be done afterward with the
   **Set Sheet Material** modifier.

Animation:

1. The binding is animated with **Binding Closure**.
2. Two opening states are defined by the number of sheets on the left side
   (opened sheets).
3. A factor animates the turn, moving sheets from right to left between the two
   opening states. **Book Sheets Animated** creates the animated sheet curves.

Profiles:

1. Page shapes are defined by **Profile Parameters**, stored as a bundle. This
   makes the whole shape easy to pass around.
2. **Profile Parameters Mix** blends two profile bundles.
3. **Profile Parameters Change** offsets selected values in an existing bundle.
4. Cover and back have their own profile bundles.
5. The first visible page on the left and the first visible page on the right
   also have their own profile bundles.

Example:

``` python
from geonodes.demos import book


# Folder containing pages images
folder = "images/pages"

# Create the image selector with default name
book.image_selector(folder)

# Create the page shaders (odd, even = odd + 1)
book.page_shaders(0,
    ("Page 1", "Page 2"),
    ("Page 3", "Page 4"),
    ("Page 5", "Page 6"),
    ("Page 7", "Page 8"),
    ("Page 9", "Page 2"),
    )

# Build the modifiers and groups
book.demo()
```

To animate a book, use the "Book Demo" modifier. Internally, it calls
"Book Sheets Animated" and "Book Extrude".
"""

from geonodes import *
import math
import re
from pathlib import Path

# ====================================================================================================
# Shaders
# ====================================================================================================

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".exr", ".webp"}


def _natural_key(text):
    """Return a key sorting page_2 before page_10."""
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]

# ----------------------------------------------------------------------------------------------------
# Image selector
#
# Images are taken from a folder and can be selected using a menu switch
# ----------------------------------------------------------------------------------------------------

def image_selector(folder, name="Image Selector"):
    """Create a shader group selecting one image color from a folder.

    Parameters
    ----------
    folder : str | Path
        Directory containing page images. Files are sorted naturally by name.

    name : str, default="Image Selector"
        Name of the shader node group to create.

    Notes
    -----
    Each image file becomes one menu item. The item label is the file name
    without extension.
    """

    import bpy

    folder = Path(folder).expanduser()
    files = sorted(
        [path for path in folder.iterdir() if path.suffix.lower() in IMAGE_EXTENSIONS],
        key=lambda path: _natural_key(path.name),
    )

    if not files:
        raise ValueError(f"No image found in {folder}")

    with ShaderNodes(name, is_group=True):

        vector = Vector(None, "Vector")
        used_labels = set()

        with Color.MenuSwitch() as color:
            for path in files:
                label = path.stem
                if label in used_labels:
                    i = 2
                    while f"{label} {i}" in used_labels:
                        i += 1
                    label = f"{label} {i}"
                used_labels.add(label)

                image = bpy.data.images.get(path.name)
                if image is None:
                    image = bpy.data.images.load(str(path))

                vector.image_texture(image=image).out(label)

        color.node.menu = Input("Menu", default_value=files[0].stem)
        color.out("Color")

# ----------------------------------------------------------------------------------------------------
# Page material
#
# Uses two pages from page selector
# ----------------------------------------------------------------------------------------------------

def page_shaders(first_index, *page_pairs, selector_name="Image Selector"):
    """Create paper materials named ``Page {i}`` from odd/even image labels.

    Parameters
    ----------
    first_index : int
        First material number. The generated materials are named
        ``Page {first_index}``, ``Page {first_index + 1}``, and so on.

    *page_pairs : tuple[str, str]
        Pairs of image selector labels: ``(odd_page, even_page)``. The shader
        uses the two labels on opposite sides of the sheet.

    selector_name : str, default="Image Selector"
        Name of the shader group created by :func:`image_selector`.
    """

    for offset, pair in enumerate(page_pairs):
        if len(pair) != 2:
            raise ValueError("Each page pair must be (odd_page_label, even_page_label).")

        odd_label, even_label = pair
        shader_index = first_index + offset

        with ShaderNodes(f"Page {shader_index}", replace_material=True):

            uv = snd.texture_coordinate().uv

            even_color = Group(selector_name, vector=uv, menu=odd_label).color
            odd_color = Group(selector_name, vector=uv*(-1, 1, 0), menu=even_label).color
            color = odd_color.mix(even_color, factor=snd.geometry().backfacing)

            Shader.Principled(
                base_color=color,
                metallic=0,
                roughness=1,
                diffuse_roughness=1,
                specular_ior_level=0,
                coat_weight=0,
            ).out()

    with ShaderNodes("Cover", replace_material=False):
        uv = snd.texture_coordinate().uv
        img = uv.image_texture()

        cover = Shader.Principled(
            base_color = img,
            roughness = 0.7,
            )
            
        inside = Shader.Principled(
            base_color = (0.8, 0.8, 0.8),
            roughness = 0.0,
        )

        thick = Shader.Principled(
            base_color = (0.8, 0.8, 0.8),
            roughness = 0.0,
        )
            
        side = snd.attribute("Side").factor
        
        shader = cover.mix(inside, factor=side.compare(0, epsilon=0.1))
        shader = shader.mix(thick, factor=side.compare(2, epsilon=0.1))
            
        shader.out()


def demo():


    """Build all shader-independent node groups and geometry modifiers."""


    # ====================================================================================================
    # Binding curve
    #
    # Animated spine curve used to attach sheet profiles.
    # ====================================================================================================

    with GeoNodes("Binding", is_group=True):

        factor = Float.Factor(0.5, "Factor", 0, 1)
        count = Integer(100, "Sheet Count")
        thickness = Float(1, "Thickness", 0.01, 10)/10000
        swiftness = Float.Factor(0.75, "Swiftness", 0, 1)
        bend = Float.Factor(0.5, "Bending", 0, 1)

        with Layout("Dims"):
            length = thickness*count
            x = length/2
            hl = x*bend.map_range(to_min=0, to_max=0.5)

        with Layout("3 phases"):
            f0 = swiftness.map_range(to_min=0.5, to_max=0.1)
            top_ag  = factor.map_range(0.0, f0, 0., pi/2)
            bot_ag  = factor.map_range(1 - f0, 1., 0., pi/2)

        with Layout("Bezier Segment"):
            top_pos = Vector((x - length*top_ag.sin(), 0, length*top_ag.cos()))
            bot_pos = Vector((-x + length*bot_ag.cos(), 0, length*bot_ag.sin()))

            top_handle = Rotation((0, -2*top_ag, 0)) @ Vector((0, 0, -hl))
            bot_handle = Rotation((0, -2*bot_ag, 0)) @ Vector((0, 0, hl))

            curve = Curve.BezierSegment(
                start = top_pos,
                start_handle = top_pos + top_handle,
                end_handle = bot_pos + bot_handle,
                end = bot_pos,
            )

        curve.splines.Count = count
        curve.splines.Thickness = thickness

        curve.out("Binding")
        bot_pos.out("Bottom")
        top_pos.out("Top")

    # ----------------------------------------------------------------------------------------------------
    # Read the binding parameters
    # ----------------------------------------------------------------------------------------------------

    def get_binding_params(binding, thickness=False):
        with Layout("Binding parameters"):
            count = gnmath.imax(2, binding.splines.sample_index(Integer("Count"), index=0))
            if not thickness:
                return count
            
            thickness = binding.length()/(count - 1)
            return count, thickness
    
    def get_binding_position(binding, count, index, tangent=False):
        with Layout("Binding index position"):
            node = binding.sample_factor(factor=index/(count-1)).node
            if tangent:
                return node.position, node.tangent
            else:
                return node.position

    # ====================================================================================================
    # Animated Closure
    #
    # Dynamic binding with a deformation factor
    # ====================================================================================================

    with GeoNodes("Binding Closure", is_group=True):

        count = Integer(100, "Sheet Count")
        thickness = Float(1, "Thickness", 0.01, 10)
        bending = Float.Factor(0.5, "Bending", 0, 1)
        factor0 = Float.Factor(0.5, "From Factor", 0, 1)
        factor1 = Float.Factor(0.5, "To Factor", 0, 1)

        with Closure() as cl:

            factor = Float(0.5, "Factor").clamp(0, 1)
            opening_factor = factor.map_range(to_min=factor0, to_max=factor1)
            
            binding = G().binding(
                sheet_count=count,
                thickness=thickness,
                factor=opening_factor,
                bending=bending,
            )

            binding.out("Bending")
            count.out("Count")
            thickness.out("Thickness")

            # Chaining
            opening_factor.out("Factor")

        binding_signature = cl.get_signature()
        cl.out("Bending")


    # ====================================================================================================
    # Profile parameters entry
    #
    # Create a bundle with sheet profile parameters
    # ====================================================================================================

    PARAMETERS = {
        "Opening" : {'type': 'ANGLE', 'def': 0.0, 'mm': (-pi/2, 3*pi/2)},
        "Root Angle" : {'type': 'ANGLE', 'def': 0.0, 'mm': (-pi/2, pi/2)},
        "Tip Angle" : {'type': 'ANGLE', 'def': 0.0, 'mm': (-pi/2, pi/2)},
        "Root Intensity" : {'type': 'FLOAT', 'def': 0.35, 'mm': (0, 2)},
        "Tip Intensity" : {'type': 'FLOAT', 'def': 0.35, 'mm': (0, 2)},
        "Stick" : {'type': 'FLOAT', 'def': 1.0, 'mm': (0, 1)},
        }

    with GeoNodes("Profile Parameters", is_group=True):

        sockets = {}
        for name, d in PARAMETERS.items():
            if d['type'] == 'ANGLE':
                inp = Float.Angle(d['def'], name, *d['mm'])
            else:
                inp = Float(d['def'], name, *d['mm'])

            sockets[name] = inp

        with Bundle() as bdl:
            for name, inp in sockets.items():
                inp.out(name)

        profile_signature = bdl.get_signature()

        bdl.out("Parameters")

    # ====================================================================================================
    # Profile parameters change
    #
    # Change profile parameters
    # ====================================================================================================

    with GeoNodes("Profile Parameters Change", is_group=True):

        old_bdl = Bundle(None, "Parameters")

        sockets = {}
        for name, d in PARAMETERS.items():

            set_inp = Boolean(False, f"Set {name}")
            if d['type'] == 'ANGLE':
                inp = Float.Angle(0.0, name)
            else:
                inp = Float(0.0, name)

            sockets[name] = (set_inp, inp)

        params = old_bdl.separate(signature=profile_signature)

        with Bundle() as bdl:
            for name, (set_inp, inp) in sockets.items():
                v = inp.switch_false(set_inp, params[name] + inp).out(name)

        bdl.out("Parameters")

    # ====================================================================================================
    # Profile parameters symmetrize
    #
    # Parameters are defined for right sides,, symmetrize make them useable for left side
    # ====================================================================================================

    with GeoNodes("Profile Parameters Symmetrize", is_group=True):

        old_bdl = Bundle(None, "Parameters")

        params = old_bdl.separate(signature=profile_signature)

        with Bundle() as bdl:
            (pi - params.opening).out("Opening")
            (-params.root_angle).out("Root Angle")
            (-params.tip_angle).out("Tip Angle")
            params.root_intensity.out("Root Intensity")
            params.tip_intensity.out("Tip Intensity")
            params.stick.out("Stick")

        bdl.out("Parameters")


    # ====================================================================================================
    # Profile parameters change
    #
    # Combine profile parameters
    # ====================================================================================================

    with GeoNodes("Profile Parameters Mix", is_group=True):

        factor = Float.Factor(.5, "Factor", 0, 1)
        A_bundle = Bundle(None, "A")
        B_bundle = Bundle(None, "B")

        A = A_bundle.separate(profile_signature)
        B = B_bundle.separate(profile_signature)

        with Bundle() as bdl:

            for name in PARAMETERS:
                factor.map_range(to_min=A[name], to_max=B[name]).out(name)

        bdl.out("Parameters")

    # ====================================================================================================
    # Profile parameters standard
    #
    # Default profile parameters
    # ====================================================================================================

    with GeoNodes("Profile Parameters Standard", is_group=True):

        curvature = Float.Factor(0.5, "Curvature", 0, 1)
        s_shape = Float.Factor(0.0, "S Shape", 0, 1)
        stick = Float.Factor(1.0, "Stick", 0, 1)
        flat_def = Boolean(False, "Flat Deformed")

        root_angle = curvature.map_range(to_min=0.0, to_max=pi/2)
        tip_angle = s_shape.map_range(to_min=-root_angle/3, to_max=0)

        with Bundle() as params:
            Float(0.0).out("Opening")
            root_angle.out("Root Angle")
            tip_angle.out("Tip Angle")
            Float(0.35).out("Root Intensity")
            Float(0.35).out("Tip Intensity")
            stick.out("Stick")

        def_angle = curvature.map_range(to_max=0.05)
        with Bundle() as deformed:
            def_angle.out("Opening")
            Float(0.0).out("Root Angle")
            (def_angle*4).out("Tip Angle")
            Float(0.35).out("Root Intensity")
            Float(0.35).out("Tip Intensity")
            Float(0.0).out("Stick")

        params.switch(flat_def, deformed)

        params.out("Parameters")

    # ====================================================================================================
    # Sheet Profile
    #
    # Bezier profile of one sheet from binding to free edge.
    # ====================================================================================================

    with GeoNodes("Sheet Profile", is_group=True):

        binding = Curve(name="Binding")

        width = Float.Distance(0.14, "Width", 0.05, 0.8)
        resolution = Integer(32, "Resolution", 2, 128)
        index = Integer(0, "Index", 0, 1000)
        parameters = Bundle(None, "Parameters")

        sheet_count = get_binding_params(binding)
        start_position = get_binding_position(binding, sheet_count, index, False)

        with Layout("Base Sheet"):
            params = parameters.separate(profile_signature)

            profile_angle = params.root_angle
            open_factor = gnmath.sin(params.root_angle.abs()/2)
            edge_distance = width*(1 - 0.35*open_factor)

            left_handle = width*params.root_intensity*(gnmath.cos(profile_angle), 0, gnmath.sin(profile_angle))
            right_handle = width*params.tip_intensity*(params.tip_angle.cos(), 0, params.tip_angle.sin())

            curve = Curve.BezierSegment(
                start=(0, 0, 0),
                start_handle=left_handle,
                end_handle=(edge_distance, 0, 0) - right_handle,
                end=(edge_distance, 0, 0),
            )

            scale = width/curve.length()
            curve.transform(translation=start_position, rotation=(0, -params.opening, 0), scale=(scale, 1, scale))

        with Layout("Finalize"):
            curve.resample(mode='Count', count=resolution)
            curve.splines.Index = index

        with Layout("Rotation to stick the end on z=0"):
                end_pos = curve.sample_factor(factor=1).position
                x, _, z = end_pos.xyz
                hrz = x - start_position.x
                ag_max = gnmath.arctangent(z/hrz)
                ag = params.stick.map_range(to_max=ag_max)
                curve.offset = -start_position
                curve.transform(rotation=(0, ag, 0))
                curve.offset = start_position

        curve.out("Sheet")
        binding.out("Binding")



    # =============================================================================================================================
    # Sheet Length
    #
    # Adjusts a sheet length by moving only its last point.
    # =============================================================================================================================

    with GeoNodes("Sheet Length", is_group=True):

        sheet = Curve()
        new_length = Float.Distance(0.14, "New Length")

        with Layout("Parameters"):
            curve = Curve(sheet)
            count = curve.points.count
            current_length = curve.length()

        with Curve.Switch(current_length < new_length) as res:
            last_index = count - 1
            prev_pos = curve.points.sample_index(nd.position, index=last_index - 1)
            last_pos = curve.points.sample_index(nd.position, index=last_index)
            last_vec = last_pos - prev_pos
            last_length = last_vec.length()
            new_last_length = new_length - current_length + last_length
            curve.points[nd.index == last_index].position = prev_pos + last_vec.normalize().scale(new_last_length)
            curve.out("True")

        with res:
            curve = curve.trim_length(end=new_length).resample(count=count)
            curve.out("False")


        res.out("Curve")

    # =============================================================================================================================
    # Sheet Clearance
    #
    # Pushes one sheet outside another one while preserving its length.
    # =============================================================================================================================

    with GeoNodes("Sheet Clearance", is_group = True):

        # ----------------------------------------------------------------------------------------------------
        # Resample smooth
        # ----------------------------------------------------------------------------------------------------

        def smooth_curve(c):
            with Layout("Resample smooth"):
                c.splines.type = 'BEZIER'
                c.handle_type = 'AUTO'

            return c
        
        # ----------------------------------------------------------------------------------------------------
        # Normals to a curve
        # ----------------------------------------------------------------------------------------------------
        
        def calc_normals(curve, sign, d=1.0):
            """ Normals to a curve
            """
            
            with Layout("Normals"):
                tg = curve.sample_factor(factor=nd.index/(count - 1)).tangent
                normal = tg.cross((0, sign, 0)).scale(d)
                
            return normal
        
        # ----------------------------------------------------------------------------------------------------
        # Main
        # ----------------------------------------------------------------------------------------------------

        sheet_below = Curve(name="Sheet Below")
        sheet_over = Curve(name="Sheet Over")
        width = Float.Distance(.14, "Width")
        thickness = Float.Distance(0.0001, "Thickness")

        with Layout("Prepare"):
            count = sheet_below.points.count._lc("Count")
            
            dx = sheet_below.sample_factor(factor=1).position.x - sheet_below.sample_factor(factor=0).position.x
            sign = Float.Switch(dx < 0, 1, -1)._lc("Sign")

        with Layout("Base curve is longer and shifted upward"):
            base_curve = G().sheet_length(sheet_below, 1.1*width)
            base_curve = smooth_curve(base_curve)

            delta = calc_normals(base_curve, sign, d=thickness)
            base_curve.offset = delta
            
            faces = base_curve.to_mesh(profile_curve=Curve.Line((-0.1, 0, 0), (0.1, 0, 0)))
            
        with Layout("Raycast"):
            raycast = nd.raycast(
                target_geometry = faces,
                source_position = nd.position,
                ray_direction = calc_normals(sheet_over, sign),
            ).node
            
            
            shifted = Curve(smooth_curve(sheet_over))
            shifted.points[raycast.is_hit & (nd.index != 0)].position = raycast.hit_position
            shifted = G().sheet_length(shifted, width)
            shifted = shifted.resample(count=count)
            
        shifted.out()

    # =============================================================================================================================
    # Create a new sheet on to an existing sheet
    #
    # Creates one sheet profile shifted by a normal offset normal on to the curve.
    # =============================================================================================================================

    with GeoNodes("Sheets On To", is_group=True):

        sheets = Curve(name="Sheets")
        binding = Curve(name="Binding")

        index = Integer(0, "Index", 0, 1000)
        left_side = Boolean(False, "Left Side")
        count = Integer(0, "Count", 0, 1000)
        width = Float(0, "Width")

        with Layout("Book parameters"):

            curve = Curve(Curve(sheets).splines[Integer("Index")==index].separate())
            width.switch(width < 0.1, curve.length())

            sheet_count, thickness = get_binding_params(binding, True)
            index_fac = Integer.Switch(left_side, -1, 1)

            length = curve.length()
            resol = curve.points.count

        for rep in repeat(count, sheets=sheets, curve=curve):

            base = Curve(G().sheet_length(rep.curve, new_length=1.1*length))
            shifted = Curve(base)
            source_factor = nd.index/(resol - 1)

            tangent = base.sample_factor(factor=source_factor).tangent
            pos = tangent.position_
            tangent = tangent.normalize()
            normal = tangent.cross((0, 1, 0)).normalize()
            normal = normal.scale(Float.Switch(left_side, 1, -1))

            new_index = index + index_fac*(rep.iteration + 1)
            start_position = binding.sample_factor(factor=new_index/(sheet_count-1)).position
            shifted.points.position = (pos + normal.scale(thickness)).switch(nd.index == 0, start_position)

            shifted = Curve(G().sheet_length(shifted, new_length=width))
            shifted.splines.Index = new_index

            rep.sheets += shifted
            rep.curve = shifted

        rep.sheets.out("Sheets")
        binding.out("Binding")

    # ====================================================================================================
    # A book profile
    #
    # Create book sheets
    # ====================================================================================================

    with GeoNodes("Book Sheets", is_group=True):

        binding = Curve(name="Binding")

        with Panel("Sheets", create_layout=True):
            width = Float.Distance(0.14, "Width", 0.05, 0.8)
            resolution = Integer(32, "Resolution", 2, 128)

            sheet_count, thickness = get_binding_params(binding, True)

            left_count = Integer(30, "Left Sheets", 0, 1000)
            left_count = gnmath.imin(left_count, sheet_count)

        with Panel("Left"):
            left_cover = Bundle(name="Cover")
            left_bottom = Bundle(name="Sheet")
            left_back = Bundle(name="Back")

        with Panel("Right"):
            right_back = Bundle(name="Back")
            right_bottom = Bundle(name="Sheet")
            right_cover = Bundle(name="Cover")

        with Layout("Covers and back positions"):
            cover_is_left = (left_count > 0)._lc("Cover is Left")
            has_left_bottom = (left_count > 1)._lc("Has left bottom")
            back_is_left = (left_count == sheet_count)._lc("Back is left")

            n_lefts = gnmath.imax(0, left_count - 2)
            n_lefts.switch(back_is_left, n_lefts - 1)._lc("Left stack")

            right_count = sheet_count - left_count
            back_is_right = back_is_left.bnot()._lc("Back is right")
            cover_is_right = cover_is_left.bnot()._lc("Cover is right")
            has_right_bottom = (right_count > 1)._lc("Has right bottom")

            n_rights = gnmath.imax(0, right_count - 2)
            n_rights.switch(cover_is_right, n_rights - 1)._lc("Right stack")

            back_index = sheet_count - 1

        with Layout("Left Pages"):

            left_cover = G().profile_parameters_symmetrize(left_cover)
            left_bottom = G().profile_parameters_symmetrize(left_bottom)
            left_back = G().profile_parameters_symmetrize(left_back)

            # Cover on left
            book = G().sheet_profile(
                binding = binding,
                width = width,
                resolution = resolution,
                index = 0,
                parameters = left_cover,
            )
            book.switch_false(cover_is_left)

            # Bottom left sheet
            curve = G().sheet_profile(
                binding = binding,
                width = width,
                resolution = resolution,
                index = 1,
                parameters = left_bottom,
            )
            curve = G().sheet_clearance(sheet_below=book, sheet_over=curve, width=width, thickness=thickness)

            curve.switch_false(has_left_bottom)
            book += curve

            # Stack sheets on to
            book = G().sheets_on_to(
                sheets = book,
                binding = binding,
                index = 1,
                left_side = True,
                count = n_lefts,
                width = width,
            )

            # Back on left
            curve = G().sheet_profile(
                binding = binding,
                width = width,
                resolution = resolution,
                index = back_index,
                parameters = left_back,
            )
            curve.switch_false(back_is_left)
            book += curve

        with Layout("Right Pages"):

            # Back on right
            back = G().sheet_profile(
                binding = binding,
                width = width,
                resolution = resolution,
                index = back_index,
                parameters = right_back,
            )
            back.switch_false(back_is_right)
            book += back

            # Right bottom sheet
            curve = G().sheet_profile(
                binding = binding,
                width = width,
                resolution = resolution,
                index = back_index - 1,
                parameters = right_bottom,
            )
            curve = G().sheet_clearance(sheet_below=back, sheet_over=curve, width=width, thickness=thickness)

            curve.switch_false(has_right_bottom)
            book += curve

            # Stack sheets on right
            book = G().sheets_on_to(
                sheets = book,
                binding = binding,
                index = back_index - 1,
                left_side = False,
                count = n_rights,
                width = width,
            )

            # Cover on right
            curve = G().sheet_profile(
                binding = binding,
                width = width,
                resolution = resolution,
                index = 0,
                parameters = right_cover,
            )
            curve.switch_false(cover_is_right)
            book += curve


        book.out("Sheets")
        binding.out("Binding")

    # ====================================================================================================
    # Curve to Chain
    #
    # Stores segment lengths and relative angles on a curve.
    # ====================================================================================================

    with GeoNodes("Curve to Chain", is_group=True):

        curve = Curve()

        with Layout("Segments"):
            P0 = curve.points.sample_index(nd.position, index=nd.index)
            P1 = curve.points.sample_index(nd.position, index=nd.index + 1)

            v = P1 - P0
            rho = v.length()
            u = v.normalize()

            curve.points.Rho = rho
            curve.points.Segment = u

        with Layout("Relative Rotation"):
            seg0 = curve.points.sample_index(Vector("Segment"), index=nd.index - 1)
            seg1 = curve.points.sample_index(Vector("Segment"), index=nd.index)

            ag = gnmath.asin(seg0.cross(seg1).y)
            curve.points.Angle = ag

        with Layout("First angle is absolute"):
            seg0 = curve.points.sample_index(Vector("Segment"), index=0)
            x, _, z = seg0.xyz
            ag = gnmath.atan2(z, x)

            curve.points[nd.index==0].Angle = ag

        curve.out()

    # ====================================================================================================
    # Sheets Interpolate
    #
    # Interpolates two set of sheets while preserving segment lengths.
    # ====================================================================================================

    with GeoNodes("Sheet Interpolate", is_group=True):

        with Panel("Sheets"):
            start_sheet = Curve(name="Start")
            end_sheet = Curve(name="End")

        with Panel("Turn"):
            factor = Float.Factor(0, "Factor", 0, 1)
            use_start = Boolean(False, "Use Start Position")
            start_position = Vector(0, "Start Position")

        with Layout("Prepare Curves"):
            sheet = Curve(start_sheet)
            start_sheet = G().curve_to_chain(start_sheet)
            end_sheet = G().curve_to_chain(end_sheet)

        with Layout("Move initial point"):
            sheet.points[use_start & (nd.index == 0)].position = start_position
            start_position = sheet.points.sample_index(nd.position, index=0)

        with Layout("Rotate initial segment"):
            start_angle = start_sheet.points.sample_index(Vector("Angle"), index=0)
            end_angle = end_sheet.points.sample_index(Vector("Angle"), index=0)
            rho = start_sheet.points.sample_index(Float("Rho"), index=0)

            ag = factor.map_range(to_min=start_angle, to_max=end_angle)
            seg = Vector((ag.cos(), 0, ag.sin()))
            pos1 = start_position + seg.scale(rho)

            sheet.points[nd.index == 1].position = pos1

        for rep in repeat(sheet.points.count - 2, sheet=sheet, pos=pos1, seg=seg):

            index = rep.iteration + 1

            rho = start_sheet.points.sample_index(Float("Rho"), index=index)

            ag0 = start_sheet.points.sample_index(Float("Angle"), index=index)
            ag1 = end_sheet.points.sample_index(Float("Angle"), index=index)
            ag = factor.map_range(to_min=ag0, to_max=ag1)

            seg = Rotation((0, ag, 0)) @ rep.seg
            pos = rep.pos + seg.scale(rho)

            rep.sheet.points[nd.index==index + 1].position = pos

            rep.pos = pos
            rep.seg = seg

        sheet = rep.sheet
        sheet.out()

    # ====================================================================================================
    # A book
    # ====================================================================================================

    with GeoNodes("Book Sheets Animated", is_group=True):

        prev_sheets = Curve(name="Sheets")
        replace = Boolean(True, "Replace")
        factor = Float.Factor(0.5, "Factor", 0, 1)

        with Layout("Binding"):
            use_binding_curve = Boolean(True, "Use Binding Curve")
            binding_cl = Closure(None, "Binding")
            binding = Curve(None, "Binding")

            cl_bld = binding_cl.evaluate(factor=factor, signature=binding_signature)
            binding.switch_false(use_binding_curve, cl_bld)
            binding_factor = cl_bld.factor

            sheet_count = get_binding_params(binding, False)

            #cl_node = binding_cl.evaluate(signature=binding_signature)
            #sheet_count = cl_node.count

        with Panel("Sheets"):
            width = Float.Distance(0.14, "Width", 0.05, 0.8)
            resolution = Integer(32, "Resolution", 2, 128)

        with Panel("Animation"):
            left_count0 = Integer(10, "From Left Sheets")
            left_count1 = Integer(10, "To Left Sheets")
            duration = Float.Factor(0.25, "Duration", 0.0001, 1.0)

        with Panel("From"):

            with Panel("Left"):
                left_cover0 = Bundle(name="Cover")
                left_bottom0 = Bundle(name="Sheet")
                left_back0 = Bundle(name="Back")

            with Panel("Right"):
                right_back0 = Bundle(name="Back")
                right_bottom0 = Bundle(name="Sheet")
                right_cover0 = Bundle(name="Cover")

        with Panel("To"):

            with Panel("Left"):
                left_cover1 = Bundle(name="Cover")
                left_bottom1 = Bundle(name="Sheet")
                left_back1 = Bundle(name="Back")

            with Panel("Right"):
                right_back1 = Bundle(name="Back")
                right_bottom1 = Bundle(name="Sheet")
                right_cover1 = Bundle(name="Cover")

        with Layout("Animation Parameters"):
            left_count0 = gnmath.imin(sheet_count - 1, left_count0)
            left_count1 = gnmath.imin(sheet_count, left_count1)
            left_count1 = gnmath.imax(left_count1, left_count0 + 1)
            count = left_count1 - left_count0
            single = count <= 1
            duration.switch(single, 1.0)
            spacing = Float.Switch(single, (1.0 - duration)/(count - 1),1.0)

        with Layout("Start and end sheets at current factor"):

            left_cover = G().profile_parameters_mix(factor, left_cover0, left_cover1)
            left_sheet = G().profile_parameters_mix(factor, left_bottom0, left_bottom1)
            left_back  = G().profile_parameters_mix(factor, left_back0, left_back1)
            
            right_back  = G().profile_parameters_mix(factor, right_back0, right_back1)
            right_sheet = G().profile_parameters_mix(factor, right_bottom0, right_bottom1)
            right_cover = G().profile_parameters_mix(factor, right_cover0, right_cover1)

            from_sheets = G().book_sheets(
                binding = binding,
                width = width,
                resolution = resolution,
                
                left_sheets = None, #left_count0,

                left_cover = left_cover,
                left_sheet = left_sheet,
                left_back  = left_back,
                
                right_back  = right_back,
                right_sheet = right_sheet,
                right_cover = right_cover,
            ).node

            to_sheets = from_sheets.duplicate_node(True)
            from_sheets.left_sheets = left_count0
            to_sheets.left_sheets = left_count1

        for rep in repeat(sheet_count, sheets=None):
            cur_index = rep.iteration
            cur_start = (rep.iteration - left_count0) * spacing
            cur_fac = factor.map_range(from_min=cur_start, from_max=cur_start + duration)

            sheet0 = Curve(from_sheets.sheets).splines[Integer("Index")==cur_index].separate().selection
            sheet1 = Curve(to_sheets.sheets).splines[Integer("Index")==cur_index].separate().selection

            sheet = G().sheet_interpolate(
                start = sheet0,
                end = sheet1,
                factor = cur_fac,
            )

            rep.sheets += sheet

        sheets = rep.sheets
        prev_sheets.switch(replace, sheets).out("Sheets")

        with Panel("Chaining"):
            binding_factor.out("Binding Factor")

            left_cover.out("Left Cover")
            left_sheet.out("Left Sheet")
            left_back.out("Left Back")
            
            right_back.out("Right Back")
            right_sheet.out("Right Sheet")
            right_cover.out("Right Cover")

    # =============================================================================================================================
    # Cover extrude
    #
    # Merge cozer, binding and back to make one single mesh
    # =============================================================================================================================

    with GeoNodes("Cover Extrude"):

        # ----------------------------------------------------------------------------------------------------
        # Prepare curve
        # ----------------------------------------------------------------------------------------------------
        
        def prep_curve(c):
            with Layout("Prepare"):
                count = c.points.count
                l = c.length()

                c = c.resample(count=count)
                fac = nd.index/(count - 1)

                c.points.U_Pos = fac

                pos = c.sample_factor(factor=fac).position
                c.points.Normal = pos.tangent.cross((0, -1, 0))

                return c, l

        # ----------------------------------------------------------------------------------------------------
        # Shifted curve to give thickness
        # ----------------------------------------------------------------------------------------------------
            
        def give_thickness(c, d):
            with Layout("Give thickness"):
                res = Curve(c)
                res.points.position += Vector("Normal").scale(d)
                res.reverse()
                return res
            
        # ----------------------------------------------------------------------------------------------------
        # Merge 3 curves in one mesh line
        # ----------------------------------------------------------------------------------------------------
            
        def merge_curves(curves):
            
            with Layout("Merge Curves in one mesh line"):

                with Layout("Prepare Curves"):
                    lengths = []
                    total_length = 0.0
                    npoints = []
                    total_points = 0
                    for i in range(3):
                        curves[i], l = prep_curve(curves[i])
                        lengths.append(l)
                        total_length += l
                        
                        npoints.append(curves[i].points.count)
                        total_points += npoints[-1]  
                        
                        
                with Layout("Adjust U pos"):            
                    ofs = 0.0
                    for i, (c, l) in enumerate(zip(curves, lengths)):
                        ul = l/total_length
                        c.points.U_Pos = ofs + Float("U Pos")*ul
                        if i < 2:
                            ofs += ul
                        
                with Layout("Transfer to a Mesh Curve"):
                    line_resol = total_points - 2
                    line = Mesh.Line(count=line_resol)
                    first = 0
                    for i, c in enumerate(curves):
                        with Layout(f"Curve {i}"):
                            line_range = nd.index >= first
                            if i == 1:
                                curve_idx = nd.index - first + 1
                                first += npoints[1] - 2
                            else:
                                curve_idx = nd.index - first
                                if i == 0:
                                    first += npoints[0]
                                    
                            line_range._lc("Line Range")
                            curve_idx._lc("Curve Idx")
                                
                            line.points[line_range].position = c.points.sample_index(nd.position, index=curve_idx)
                            line.points[line_range].Normal = c.points.sample_index(Vector("Normal"), index=curve_idx)
                            line.points[line_range].U_Pos = c.points.sample_index(Float("U Pos"), index=curve_idx)
                                
                return line, curves

        # ----------------------------------------------------------------------------------------------------
        # Main
        # ----------------------------------------------------------------------------------------------------
        
        B_RESOL = 12
        
        sheets = Curve(name="Sheets")
        binding = Curve(name="Binding")
        length = Float(0.25, "Length")
        thickness = Float(.001, "Thickness")
        mat = Material(None, "Cover")
        
        binding = binding.resample(count=B_RESOL)
        
        
        nsplines = sheets.splines.count
        
        cover = Curve(Curve(sheets).splines[Integer("Index")==0].separate().selection)
        cover.reverse()
        back = Curve(Curve(sheets).splines[Integer("Index")==nsplines - 1].separate().selection)
        
        line1, curves = merge_curves([cover, binding, back])
        cover = curves[0]
        back = curves[2]
        
        with Layout("Thickness Extruded line"):
            cover2 = give_thickness(cover, thickness).reverse()
            back2 = give_thickness(back, thickness).reverse()
            with Layout("Translate the binding"):
                
                n = cover.points.count
                P0 = cover2.points.sample_index(nd.position, index=n-1)
                P1 = back2.points.sample_index(nd.position, index=0)
                binding2 = Curve.Line(P0, P1).resample(count=B_RESOL)
                
            line2, _ = merge_curves([cover2, binding2, back2])

        with Layout("Thickness Face"):
            line_resol = line1.points.count
            line_resol2 = line_resol*2
            
            thick_line = Mesh.Circle(vertices=line_resol2, fill_type='N-Gon')
            
            with Layout("First Line"):
                idx = nd.index
                thick_line.points.position = line1.points.sample_index(nd.position, index=idx)
                thick_line.points.U_Pos = line1.points.sample_index(Float("U Pos"), index=idx)
                thick_line.points.VBack = False
                
            with Layout("Second Line"):
                
                sel = nd.index >= line_resol
                idx = line_resol2 - 1 - nd.index 
                
                pos = line2.points.sample_index(nd.position, index=idx)
                upos = line2.points.sample_index(Float("U Pos"), index=idx)
                
                thick_line.points[sel].position =  pos
                thick_line.points[sel].U_Pos =  1 - upos
                thick_line.points[sel].VBack = True
                
        with Layout("Extrude Page"):

            thick_line.faces.Side = 2.0
            thick_line.points.V_Pos = 0.0
            
            mesh = Mesh(thick_line).extrude((0, length, 0))
            top = mesh.top
            side = mesh.side
            mesh.points[top].V_Pos = 1.0
            
        with Layout("Side"):
            
            nfaces = mesh.faces.count
            mesh.faces[side].Side = 0.0
            mesh.faces[(nd.index==nfaces-1) | (nd.index==nfaces//2)].Side = 2.0
            
            mesh += thick_line.flip_faces()
            mesh = Mesh(mesh).merge_by_distance(distance=thickness/10)
            
            
            mesh.faces[Float("Side") == 0.0].shade_smooth=True
            mesh.faces.material = mat
            mesh.faces[Boolean("VBack")].Side = 1.0
            
        with Layout("UV Map"):
            mesh.corners.store_uv("UV Map", (Float("U Pos"), Float("V Pos"), 0))
            
        with Layout("Some Cleaning"):
            mesh.remove_named_attribute(name="U Pos")
            mesh.remove_named_attribute(name="V Pos")
            mesh.remove_named_attribute(name="VBack")
                    
        mesh.out()

    # =============================================================================================================================
    # Book Mesh
    #
    # Converts sheet and cover curves to renderable meshes.
    # =============================================================================================================================

    with GeoNodes("Book Extrude"):

        with Panel("Input"):
            sheets = Curve(name="Sheets")
            binding = Curve(name="Binding")

        with Panel("Dimensions"):
            length = Float.Distance(0.21, "Length", 0.01, 1)
            cover_thickness = Float.Distance(0.002, "Cover Thickness", 0.0001, 0.02)

        with Panel("Materials"):
            sheet_material_offset = Integer(1, "Page First Index", 0, 1000, tip="Materials for sheets are 'Page xxx'")
            sheet_material_count = Integer(8, "Sheet Materials", 1, 1000, tip="Materials 'Page xxx' count")
            seed = Integer(0, "Seed", tip="Pick random material in 'Page first_index' and 'Page last_index'")
            cover_mat = Material(None, "Cover")

        with Layout("Internal Sheets"):
            count = sheets.splines.count
            internal = (Integer("Index") > 0) & (Integer("Index") < count - 1)
            page_source = Curve(sheets)
            page_curves = Curve(page_source.splines[internal].separate())
            internal_count = count - 2
            point_count = page_curves.points.count/internal_count
            page_curves = page_curves.resample(count=point_count)
            page_curves.points.Page_U = page_curves.points.index_in_curve(nd.index)/(point_count - 1)
            sheet_mesh = page_curves.to_mesh()
            sheet_mesh.edges.extrude(offset=(0, length, 0))

        with Layout("Cover Surface"):
            cover_mesh = G().cover_extrude(
                sheets = sheets,
                binding = binding,
                length = length,
                thickness = cover_thickness,
                cover = cover_mat,
            )

        with Layout("UV Map"):
            u = Float("Page U")
            v = (nd.position.y/length).clamp(0, 1)
            sheet_mesh.corners.store_uv("UV Map", (u, v, 0))

        with Layout("Sheet Content"):
            sheet_mesh.faces.Sheet_Num = Integer("Index") + 1

        with Layout("Sheet Materials"):
            for i in range(100):
                mat = blender.get_resource('MATERIAL', f"Page {i}")
                if mat is None:
                    break
                sheet_mesh.set_material(Material(mat))

            material_index = sheet_material_offset + Integer.Random(
                min=0,
                max=sheet_material_count - 1,
                id=Integer("Sheet Num"),
                seed=seed,
            )
            sheet_mesh.faces.material_index = material_index

        (sheet_mesh + cover_mesh).out()


    # =============================================================================================================================
    # Set Sheet Material
    #
    # Forces consecutive material slots on a range of sheets.
    # =============================================================================================================================

    with GeoNodes("Set Sheet Material"):

        mesh = Mesh()

        ignore = Boolean(False, "Ignore")

        sheet_number = Integer(1, "Sheet Number", 1, 10000)
        sheet_count = Integer(1, "Sheet Count", 1, 10000)
        material_index = Integer(1, "Material Index", 0, 1000)

        with Layout("Sheet Selection"):
            local_index = Integer("Sheet Num") - sheet_number
            selection = (local_index >= 0) & (local_index < sheet_count)

        with Layout("Material"):
            new_mesh = Mesh(mesh)
            new_mesh.faces[selection].material_index = material_index + local_index
            new_mesh.switch(ignore, mesh)
            
        new_mesh.out()

    # =============================================================================================================================
    # A book
    # =============================================================================================================================

    with GeoNodes("Book"):

        show = Boolean(True, "Show")
        sheets_factor = Float.Factor(50, "Factor", 0, 100)
        duration = Float.Factor(0.2, "Duration", 0, 1)
        
        with Panel("Dimensions"):
            sheet_count = Integer(100, "Sheet Count", 4, 1000)
            thickness = Float(1, "Thickness",0.01, 10)
            width = Float.Distance(0.17, "Width", 0.05, .7)
            length = Float.Distance(0.24, "Length", 0.05, 0.7)
            resolution = Integer(32, "Resolution", )

        with Panel("Extrusion"):
            extrude = Boolean(True, "Extrude")
            cover_thickness = Float.Distance(0.001, "Cover Thickness", 0.000001, 0.005)
            
        with Layout("Parameters"):
            sheet_count = gnmath.max(4, sheet_count)
            factor = sheets_factor/100
            left_factor = 1 - factor
            duration = duration.map_range(to_min=1/(sheet_count+1), to_max=1)
            
            
        binding = G().binding(
            sheet_count = sheet_count,
            thickness = thickness,
            factor = factor,
            bending = .5,
            swiftness = 0.75,
            )
            
        cover_max_curv = 0.5
        sheet_max_curv = 0.9
        sheet_max_s    = 0.7
        
        cover_min_from_stick = 0.7
            
        with Layout("From Parameters"):
            with Layout("Left"):
                from_left_cover = G().profile_parameters_standard(
                    curvature = left_factor.map_range_smooth_step(to_max=cover_max_curv),
                    stick = left_factor.map_range(from_min=cover_min_from_stick),
                )._lc("Cover")
                from_left_sheet = G().profile_parameters_standard(
                    curvature = left_factor.map_range_smooth_step(to_max=sheet_max_curv),                
                    s_shape = left_factor.map_range_smooth_step(to_max=sheet_max_s),                
                    stick = left_factor.map_range(from_min=cover_min_from_stick/2),
                )._lc("Sheet")
                from_left_back = G().profile_parameters_standard(
                    curvature = 0.5,
                    flat_deformed=True,
                )._lc("Back")
                
            with Layout("Right"):
                from_right_back = G().profile_parameters_standard(
                    curvature = factor.map_range_smooth_step(to_max=cover_max_curv),
                    stick = factor.map_range(from_min=cover_min_from_stick),
                )._lc("Back")
                from_right_sheet = G().profile_parameters_standard(
                    curvature = factor.map_range_smooth_step(to_max=sheet_max_curv),                
                    s_shape = factor.map_range_smooth_step(to_max=sheet_max_s),                
                    stick = factor.map_range(from_min=cover_min_from_stick/2),
                )._lc("Sheet")
                from_right_cover = G().profile_parameters_standard(
                    curvature = 0.5,
                    flat_deformed=True,
                )._lc("Cover")
                
        with Layout("Left"):
            to_left_cover = G().profile_parameters_standard(
                curvature = left_factor.map_range_smooth_step(to_max=cover_max_curv),
                stick = left_factor.map_range(from_min=cover_min_from_stick),
            )._lc("Cover")
            to_left_sheet = G().profile_parameters_standard(
                curvature = left_factor.map_range_smooth_step(to_max=sheet_max_curv),                
                s_shape = left_factor.map_range_smooth_step(to_max=sheet_max_s),                
                stick = left_factor.map_range(from_min=cover_min_from_stick/2),
            )._lc("Sheet")
            to_left_back = G().profile_parameters_standard(
                curvature = 0.5,
                flat_deformed=True,
            )._lc("Back")
            
        with Layout("Right"):
            to_right_back = G().profile_parameters_standard(
                curvature = factor.map_range_smooth_step(to_max=cover_max_curv),
                stick = factor.map_range(from_min=cover_min_from_stick),
            )._lc("Back")
            to_right_sheet = G().profile_parameters_standard(
                curvature = factor.map_range_smooth_step(to_max=sheet_max_curv),                
                s_shape = factor.map_range_smooth_step(to_max=sheet_max_s),                
                stick = factor.map_range(from_min=cover_min_from_stick/2),
            )._lc("Sheet")
            to_right_cover = G().profile_parameters_standard(
                curvature = 0.5,
                flat_deformed=True,
            )._lc("Cover")
        
        sheets = G().book_sheets_animated(
            factor = factor,
            
            width = width,
            resolution = resolution,
            
            use_binding_curve = True,
            binding = binding,
            
            from_left_sheets = 0,
            to_left_sheets = sheet_count,
            duration = duration,
            
            from_left_cover = from_left_cover,
            from_left_sheet = from_left_sheet,
            from_left_back = from_left_back,
            
            from_right_cover = from_right_cover,
            from_right_sheet = from_right_sheet,
            from_right_back = from_right_back,
            
            to_left_cover = to_left_cover,
            to_left_sheet = to_left_sheet,
            to_left_back = to_left_back,
            
            to_right_cover = to_right_cover,
            to_right_sheet = to_right_sheet,
            to_right_back = to_right_back,
            )
            
        book = G().book_extrude(
            sheets = sheets,
            binding = binding,
            length = length,
            cover_thickness = cover_thickness,
            ).link_panel("Materials")
            
        book.switch_false(extrude, sheets)
            
        book.switch_false(show).out()

       


    # =============================================================================================================================
    # Book example
    # =============================================================================================================================

    with GeoNodes("Book Demo"):

        factor = Float.Factor(0.5, "Factor", 0, 1)
        left_count = Integer(30, "Sheets Left", 10, 60)
        count = Integer(5, "Count", 1, 20)
        duration = Float.Factor(0.2, "Duration", 0.001, 1.)
        use_extrude = Boolean(True, "Extrude")

        with Layout("Dynamic binding for animation"):
            binding = G().binding_closure(
                sheet_count = 100,
                thickness = 1.000,
                bending = 0.500,
                from_factor = 0.354,
                to_factor = 0.688,
            )

        with Layout("From Parameters"):
            left_cover0 = G().profile_parameters(
                opening = 3.138,
                root_angle = -0.216,
                tip_angle = 0.115,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )
            left_sheet0 = G().profile_parameters(
                opening = 3.128,
                root_angle = -0.792,
                tip_angle = 0.115,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )

            right_back0 = G().profile_parameters(
                opening = 0.003,
                root_angle = 0.192,
                tip_angle = 0.000,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )
            right_sheet0 = G().profile_parameters(
                opening = 0.003,
                root_angle = 0.227,
                tip_angle = 0.000,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )

        with Layout("To Parameters"):
            left_cover1 = G().profile_parameters(
                opening = 3.135,
                root_angle = -0.363,
                tip_angle = 0.115,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )

            left_sheet1 = G().profile_parameters(
                opening = 3.138,
                root_angle = -0.471,
                tip_angle = 0.115,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )

            right_back1 = G().profile_parameters(
                opening = 0.000,
                root_angle = 0.276,
                tip_angle = 0.000,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )

            right_sheet1 = G().profile_parameters(
                opening = 0.003,
                root_angle = 0.796,
                tip_angle = 0.000,
                root_intensity = 0.350,
                tip_intensity = 0.350,
            )

        with Layout("Animated Sheets"):
            sheets = G().book_sheets_animated(
                factor = factor,
                binding = binding,
                
                width = 0.14,
                resolution = 32,
                
                from_left_sheets = left_count,
                to_left_sheets = left_count + count,
                duration = duration,

                from_left_cover = left_cover0,
                from_left_sheet = left_sheet0,
                from_right_back = right_back0,
                from_right_sheet = right_sheet0,

                to_left_cover = left_cover1,
                to_left_sheet = left_sheet1,
                to_right_back = right_back1,
                to_right_sheet = right_sheet1,
            )

        with Layout("Extrude animated profiles"):
            book = G().book_extrude(
                sheets = sheets,
                #length = 0.21,
                #cover_thickness = 0.002,
                #binding_radius = 0.003,
                #first_sheet_material = 1,
                #sheet_materials = 8,
                #seed = 0,
                #cover = None,
                #binding = None,
            ).link_inputs(from_panel="Extrude")

        sheets.switch(use_extrude, book).out()        
