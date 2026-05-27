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
        ped = Shader.Principled(
            base_color = img,
            roughness = 0.7,
            )
            
        inside = Shader.Principled(
            base_color = (0.8, 0.8, 0.8),
            roughness = 0.0,
        )
            
        side = snd.attribute("Side").factor
        
        shader = ped.mix(inside, factor=side.compare(2, epsilon=0.1))
            
        shader.out()
        


def demo():
    """Build all shader-independent node groups and geometry modifiers."""


    # ====================================================================================================
    # Binding curve
    #
    # Animated spine curve used to attach sheet profiles.
    # ====================================================================================================

    with GeoNodes("Binding", is_group=True):

        count = Integer(100, "Sheet Count")
        thickness = Float(1, "Thickness", 0.01, 10)/10000
        factor = Float.Factor(0.5, "Opening Factor", 0, 1)
        bend = Float.Factor(0.5, "Bending", 0, 1)

        with Layout("Dims"):
            length = thickness*count
            x = length/2
            hl = x*bend.map_range(to_min=0, to_max=0.5)

        with Layout("3 phases"):
            f0 = 0.5
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
            
            binding = G().binding(
                sheet_count=count,
                thickness=thickness,
                opening_factor=factor.map_range(to_min=factor0, to_max=factor1),
                bending=bending,
            )

            binding.out("Bending")
            count.out("Count")
            thickness.out("Thickness")

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

        sheets_count = get_binding_params(binding)
        start_position = get_binding_position(binding, sheets_count, index, False)

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

        curve.out("Sheet")
        binding.out("Binding")

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

        with Layout("Book parameters"):

            curve = Curve(Curve(sheets).splines[Integer("Index")==index].separate())

            sheets_count, thickness = get_binding_params(binding, True)
            index_fac = Integer.Switch(left_side, -1, 1)

            length = curve.length()
            resol = curve.points.count

        for rep in repeat(count, sheets=sheets, curve=curve):

            shifted = Curve(rep.curve).resample(count=resol + 1)
            source_factor = (nd.index - 1)/(resol - 1)

            tangent = rep.curve.sample_factor(factor=source_factor).tangent
            pos = tangent.position_
            tangent = tangent.normalize()
            normal = tangent.cross((0, 1, 0)).normalize()
            normal = normal.scale(Float.Switch(left_side, 1, -1))

            new_index = index + index_fac*(rep.iteration + 1)
            start_position = binding.sample_factor(factor=new_index/(sheets_count-1)).position
            shifted.points.position = (pos + normal.scale(thickness)).switch(nd.index == 0, start_position)

            shifted = shifted.trim_length(start=0, end=length).resample(count=resol)
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

            sheets_count = get_binding_params(binding)

            left_count = Integer(30, "Left Sheets", 0, 1000)
            left_count = gnmath.imin(left_count, sheets_count)

        with Panel("Left Parameters"):
            left_cover = Bundle(name="Cover")
            left_bottom = Bundle(name="Bottom Sheet")
            left_back = Bundle(name="Back")

        with Panel("Right Parameters"):
            right_back = Bundle(name="Back")
            right_bottom = Bundle(name="Bottom Sheet")
            right_cover = Bundle(name="Cover")

        with Layout("Cover and back positions"):
            cover_is_left = (left_count > 0)._lc("Cover is Left")
            has_left_bottom = (left_count > 1)._lc("Has left bottom")
            back_is_left = (left_count == sheets_count)._lc("Back is left")

            n_lefts = gnmath.imax(0, left_count - 2)
            n_lefts.switch(back_is_left, n_lefts - 1)._lc("Left stack")

            right_count = sheets_count - left_count
            back_is_right = back_is_left.bnot()._lc("Back is right")
            cover_is_right = cover_is_left.bnot()._lc("Cover is right")
            has_right_bottom = (right_count > 1)._lc("Has right bottom")

            n_rights = gnmath.imax(0, right_count - 2)
            n_rights.switch(cover_is_right, n_rights - 1)._lc("Right stack")

            back_index = sheets_count - 1


        with Layout("Left Pages"):

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
            curve.switch_false(has_left_bottom)
            book += curve

            # Stack sheets on to
            book = G().sheets_on_to(
                sheets = book,
                binding = binding,
                index = 1,
                left_side = True,
                count = n_lefts,
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
            curve.switch_false(has_right_bottom)
            book += curve

            # Stack sheets on right
            book = G().sheets_on_to(
                sheets = book,
                binding = binding,
                index = back_index - 1,
                left_side = False,
                count = n_rights,
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

        factor = Float.Factor(0.5, "Factor", 0, 1)

        with Layout("Binding"):
            binding_cl = Closure(None, "Binding")
            cl_node = binding_cl.evaluate(signature=binding_signature)
            sheets_count = cl_node.count

        with Panel("Sheets"):
            width = Float.Distance(0.14, "Width", 0.05, 0.8)
            resolution = Integer(32, "Resolution", 2, 128)

        with Panel("Animation"):
            left_count0 = Integer(10, "From Left Sheets")
            left_count1 = Integer(10, "To Left Sheets")
            duration = Float.Factor(0.25, "Duration", 0.0001, 1.0)

        with Panel("From Configuration"):

            with Panel("Left Parameters"):
                left_cover0 = Bundle(name="Cover")
                left_bottom0 = Bundle(name="Bottom Sheet")
                left_back0 = Bundle(name="Back")

            with Panel("Right Parameters"):
                right_back0 = Bundle(name="Back")
                right_bottom0 = Bundle(name="Bottom Sheet")
                right_cover0 = Bundle(name="Cover")

        with Panel("To Configuration"):

            with Panel("Left Parameters"):
                left_cover1 = Bundle(name="Cover")
                left_bottom1 = Bundle(name="Bottom Sheet")
                left_back1 = Bundle(name="Back")

            with Panel("Right Parameters"):
                right_back1 = Bundle(name="Back")
                right_bottom1 = Bundle(name="Bottom Sheet")
                right_cover1 = Bundle(name="Cover")

        with Layout("Animation Parameters"):
            left_count0 = gnmath.imin(sheets_count - 1, left_count0)
            left_count1 = gnmath.imin(sheets_count, left_count1)
            left_count1 = gnmath.imax(left_count1, left_count0 + 1)
            count = left_count1 - left_count0
            single = count <= 1
            duration.switch(single, 1.0)
            spacing = Float.Switch(single, (1.0 - duration)/(count - 1),1.0)

        with Layout("Start and end sheets at current factor"):

            from_sheets = G().book_sheets(
                binding = binding_cl.evaluate(factor=factor, signature=binding_signature),
                width = width,
                resolution = resolution,
                
                left_sheets = None, #left_count0,

                left_parameters_cover        = G().profile_parameters_mix(factor, left_cover0, left_cover1),
                left_parameters_bottom_sheet = G().profile_parameters_mix(factor, left_bottom0, left_bottom1),
                left_parameters_back         = G().profile_parameters_mix(factor, left_back0, left_back1),
                
                right_parameters_cover        = G().profile_parameters_mix(factor, right_cover0, right_cover1),
                right_parameters_bottom_sheet = G().profile_parameters_mix(factor, right_bottom0, right_bottom1),
                right_parameters_back         = G().profile_parameters_mix(factor, right_back0, right_back1),      
            ).node

            to_sheets = from_sheets.duplicate_node(True)
            from_sheets.left_sheets = left_count0
            to_sheets.left_sheets = left_count1

        for rep in repeat(sheets_count, sheets=None):
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

            #sheet.switch(cur_index < left_count0, sheet0)
            #sheet.switch(cur_index >= left_count1, sheets_count - left_count1, sheet1)

            rep.sheets += sheet


        sheets = rep.sheets
        sheets.out("Sheets")

    # =============================================================================================================================
    # Book Mesh
    #
    # Converts sheet and cover curves to renderable meshes.
    # =============================================================================================================================

    with GeoNodes("Book Extrude"):

        with Panel("Input"):
            sheets = Curve(name="Sheets")

        with Panel("Dimensions"):
            length = Float.Distance(0.21, "Length", 0.01, 1)
            cover_thickness = Float.Distance(0.002, "Cover Thickness", 0.0001, 0.02)

        with Panel("Materials"):
            sheet_material_offset = Integer(1, "First Sheet Material", 0, 1000)
            sheet_material_count = Integer(8, "Sheet Materials", 1, 1000)
            seed = Integer(0, "Seed")
            cover_mat = Material(None, "Cover")

        with Layout("Split Sheets"):
            count = sheets.splines.count
            sheets.splines.Sheet_Index = nd.index
            sheets.points._T_u = Spline.parameter_factor
            is_cover_sheet = Integer("Sheet Index") == 0
            is_back_sheet = Integer("Sheet Index") == count - 1

        with Layout("Binding Curve"):
            binding_source = Curve(sheets)
            binding_points = Curve(binding_source.points[Float("T u").equal(0)].separate()).to_points()
            binding = binding_points.to_curves(weight=Integer("Sheet Index"))

        with Layout("Sheets Surface"):
            page_source = Curve(sheets)
            page_curves = Curve(page_source.splines[(is_cover_sheet | is_back_sheet).bnot()].separate())
            sheet_mesh = page_curves.to_mesh()
            sheet_mesh.edges.extrude(offset=(0, length, 0))

        with Layout("Cover Surface"):
            with Layout("Merge cover, binding and back"):
                cover_source = Curve(sheets)
                cover_curve = Curve(cover_source.splines[is_cover_sheet].separate())
                cover_curve.reverse()
                back_source = Curve(sheets)
                back_curve = Curve(back_source.splines[is_back_sheet].separate())

                cover_len = cover_curve.length()
                binding_len = binding.length()
                back_len = back_curve.length()
                total_len = gnmath.max(cover_len + binding_len + back_len, 0.000001)

                cover_curve.points._Cover_U = 1 - Spline.parameter_factor*cover_len/total_len
                binding.points._Cover_U = 1 - (cover_len + Spline.parameter_factor*binding_len)/total_len
                back_curve.points._Cover_U = 1 - (cover_len + binding_len + Spline.parameter_factor*back_len)/total_len

                cover_line = Curve(cover_curve + binding + back_curve)
                cover_mesh = cover_line.to_mesh().merge_by_distance()

            with Layout("Solidify"):
                cover_mesh.edges.extrude(offset=(0, length, 0))
                cover_mesh.faces.Side = 0.0 # Top faces

                cover_base = Mesh(cover_mesh).flip_faces()
                cover_base.faces.Side = 2.0 # Inner faces

                cover_mesh.faces.extrude(offset=nd.normal.scale(cover_thickness), individual=False)
                cover_mesh.faces[cover_mesh.side].Side = 1.0 # Side faces

                cover_v = (nd.position.y/length).clamp(0, 1)
                cover_mesh.corners.store_uv("UV Map", (Float("Cover U"), cover_v, 0))
                cover_base.corners.store_uv("UV Map", (1 - Float("Cover U"), cover_v, 0))
                cover_mesh += cover_base
                cover_mesh.merge_by_distance()
                cover_mesh.faces.material = cover_mat

        with Layout("UV Map"):
            u = Float("T u")
            v = (nd.position.y/length).clamp(0, 1)
            sheet_mesh.corners.store_uv("UV Map", (u, v, 0))

        with Layout("Sheet Content"):
            sheet_mesh.faces.Sheet_Num = Integer("Sheet Index") + 1

        with Layout("Sheet Materials"):
            for i in range(100):
                mat = blender.get_resource('MATERIAL', f"Page {i}")
                if mat is None:
                    break
                sheet_mesh.set_material(Material(mat))

            material_index = sheet_material_offset + Integer.Random(
                min=0,
                max=sheet_material_count - 1,
                id=Integer("Sheet Index"),
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
            left_bottom0 = G().profile_parameters(
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
            right_bottom0 = G().profile_parameters(
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

            left_bottom1 = G().profile_parameters(
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

            right_bottom1 = G().profile_parameters(
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

                from_configuration_left_parameters_cover = left_cover0,
                from_configuration_left_parameters_bottom_sheet = left_bottom0,
                from_configuration_right_parameters_back = right_back0,
                from_configuration_right_parameters_bottom_sheet = right_bottom0,

                to_configuration_left_parameters_cover = left_cover1,
                to_configuration_left_parameters_bottom_sheet = left_bottom1,
                to_configuration_right_parameters_back = right_back1,
                to_configuration_right_parameters_bottom_sheet = right_bottom1,
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




