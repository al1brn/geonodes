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

module : demo formula
---------------------

Anim formula expressed in simplified LaTeX

IN PROGRESS

updates
-------
- creation :   2025/02/22

$ DOC START

[Source Code](../demos/forest.py)

Animated formula

IN PROGRESS

``` python
from geonodes.demos import formula

formula.demo()
```
"""

import bpy
from . import formula_data
from . import formula_tree

from geonodes import *
from geonodes.core import utils

# =============================================================================================================================
# =============================================================================================================================
# Font dependant constants
# Default constants are set for 'Times New Roman'' font
# =============================================================================================================================
# =============================================================================================================================

FONT_SIZE    = 2.0   # Font size to have A with an height of 1.
Y_ALIGN      = 0.2323*FONT_SIZE # Location of base line (center of = sign)
PAR_SCALE    = 1.2   # Parenthesis scale
X_SPACE      = 0.2   # Horizontal spacing
X_IND        = 0.2   # Horizontal spacing for indice and exponent
Y_EXP        = 0.5
Y_IND        = 0.2
Y_ABOVE      = 0.3
SCALE_IND    = 0.3   # Indice and exponent scale

DECO_THICK   = 0.06   # Decoractors thickness

# SIGN
PLUS_THICK = DECO_THICK
PLUS_WIDTH = .5

# FRACTION
FRAC_THICK  = DECO_THICK
FRAC_MARGIN = 4*X_SPACE

SQRT = '√'

# -----------------------------------------------------------------------------------------------------------------------------
# Load fonts

class Fonts:
    def __init__(self):
        self.regular     = utils.get_font("Times New Roman")
        self.italic      = utils.get_font("Times New Roman Italic")
        self.bold        = utils.get_font("Times New Roman Bold")
        self.bold_italic = utils.get_font("Times New Roman Bold Italic")

# =============================================================================================================================
# =============================================================================================================================
# Shaders
# =============================================================================================================================
# =============================================================================================================================

def build_shaders():
    # ----------------------------------------------------------------------------------------------------
    # Fade using Fade attribute

    with ShaderNodes("Fade Shader", is_group=True):

        shader = Shader(name="Shader")

        fade = snd.attribute("Fade").fac
        transp = Shader.Transparent()

        shader = shader.mix(transp, fac=fade)
        shader.out("Shader")

    # ----------------------------------------------------------------------------------------------------
    # Formula shader

    with ShaderNodes("Formula"):

        ped = Shader.Principled(
            base_color = snd.attribute("Color").color,
            roughness  = 1 - snd.attribute("Shiny").fac,
            alpha      = 1 - snd.attribute("Fade").fac,
            )

        ped.out()

# =============================================================================================================================
# =============================================================================================================================
# utilities
# =============================================================================================================================
# =============================================================================================================================

# =============================================================================================================================
# Python utilities

# -----------------------------------------------------------------------------------------------------------------------------
# This utility capture a curve

def capture_curve(name):
    curve = bpy.data.objects[name]
    splines = curve.data.splines
    print("splines = [")
    for spline in splines:
        print("   [")
        for bp in spline.bezier_points:
            x, y, _ = bp.co
            lx, ly, _ = bp.handle_left
            rx, ry, _ = bp.handle_right
            print(f"    ( ({x}, {y}), ({lx}, {ly}), ({rx}, {ry}) ),")
        print("   ],")
    print("]")

# -----------------------------------------------------------------------------------------------------------------------------
# This utility build a captured char

def create_curve(name, splines):

    with GeoNodes(name):

        curves = None
        as_mesh = Boolean(True, "Fill")

        for spline in splines:
            c = Curve.Circle(resolution=len(spline))
            c.splines.type = 'BEZIER'
            for i, (pos, left, right) in enumerate(spline):
                sel = nd.index.equal(i)
                c[sel].position = (pos[0], pos[1], 0)
                c[sel].left_handle_position = (left[0], left[1], 0)
                c[sel].right_handle_position = (right[0], right[1], 0)

            if curves is None:
                curves = c
            else:
                curves += c

        mesh = curves.fill_ngons()

        curves.switch(as_mesh, mesh).out()

# =============================================================================================================================
# =============================================================================================================================
# Formula components
# =============================================================================================================================
# =============================================================================================================================

def build_groups():

    formula_tree.build_tree(domain='FACE', prefix='Face', max_depth=10)
    GTree = G("Face")

    create_curve("Node Sqrt Char", formula_data.SQRT_CHAR)
    create_curve("Node Sigma Char", formula_data.SIGMA_CHAR)

    FONTS = Fonts()

    # =============================================================================================================================
    # Debug
    #
    # Display the item ids

    with GeoNodes("Debug Formula"):

        geo   = Mesh(Geometry())
        use_boxes = Boolean(False, "Boxes")
        use_debug = Boolean(True, "Debug")
        seed  = Integer(0, "Seed")

        with Layout("One color per id"):
            count = geo.faces.count
            cols = Cloud.Points(count=count)
            cols.points._Color = Color.CombineHSV(Float.Random(0, 1, seed=seed.hash_value(nd.index)), 1, 1)

        with geo.faces.for_each(color=Color.Named("Color"), item_id=Integer("Item ID")) as feel:

            vmin = Mesh(feel.element).points.attribute_statistic(nd.position).min
            vmax = vmin.max_

            vdiff = vmax - vmin
            width, height, _ = vdiff.xyz
            center = (vmin + vmax)/2

            face = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=width, size_y=height).transform(translation=center)
            face.faces.material = "Formula"
            face.faces._Color = feel.color #(1, 1, 1)
            face.faces._Item_ID = feel.item_id

            num = feel.item_id.to_string().to_curves(size=gnmath.max(.2, height*.8), align_x='CENTER', align_y='MIDDLE')
            num = Curve(num.realize())
            num = num.fill()
            num.faces.material = "Formula"
            num.faces._Color = cols.points.sample_index(Color.Named("Color"), index=feel.item_id)
            num.offset = center + (0, 0, .1)

            feel.generated.geometry = face + num

        boxes = feel.generated.geometry

        colored = Mesh(geo)
        colored.faces._Color = cols.points.sample_index(Color.Named("Color"), index=Integer("Item ID"))

        debug_geo = colored.switch(use_boxes, boxes)

        geo.switch(use_debug, debug_geo).out()

    # =============================================================================================================================
    # LaTeX codes

    with GeoNodes("LaTeX Codes", is_group=True):

        s = String(None, "String")

        keys = sorted(formula_data.SYMBOLS.keys(), key= lambda x: 100 - len(x))

        for code in keys:
            c = formula_data.SYMBOLS[code]
            s = s.replace("\\" + code, c)

        s.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Geometry dimensions
    #
    # Return measures of the geometry
    # - Either the whole geometry
    # - Or the item identified by id
    #
    # - Right: right position of the geometry
    # - Over : height over the base line
    # - Width : width
    # - Height : total height
    # - X Mid : horizontal center
    # - Y Mid : vertical center

    with GeoNodes("Dimensions", is_group=True):

        geo     = Geometry()
        item_id = Integer(0, "Id")

        mesh = Mesh(geo.switch(item_id.not_equal(0), Mesh(geo).faces[Integer("Item ID").not_equal(item_id)].delete()))

        node = mesh.points.attribute_statistic(nd.position)
        vmin = node.min
        vmax = node.max

        vdiff = vmax - vmin
        vmid  = (vmin + vmax)/2

        width, height, _ = vdiff.xyz
        left, below, _   = vmin.xyz
        right, over, _   = vmax.xyz
        x_mid, y_mid, _  = vmid.xyz

        left.out("Left")
        right.out("Right")
        over.out("Over")
        below.out("Below")
        width.out("Width")
        height.out("Height")
        x_mid.out("X Mid")
        y_mid.out("Y Mid")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Scale geometry
    #
    # Scale based on bottom left component

    with GeoNodes("Scale"):

       geo = Mesh(Geometry())
       sx  = Float(1., "x")
       sy  = Float(1., "y")

       vmin = geo.points.attribute_statistic(nd.position).min
       vmax = vmin.max_

       geo.points.offset = -vmin
       geo.transform(scale=(sx, sy, 1))
       geo.points.offset = vmin

       geo.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Fade a component
    #
    # Set the fade value
    # The geometry is horizontally scaled to 0 when fade grows up to 1

    with GeoNodes("Fade"):

        # The geometry is kept even when not visible in order to keep tree ids

        geo  = Mesh(Geometry())
        fade = Float.Factor(0, "Fade", 0, 1)

        geo.faces._Fade = fade
        scale = fade.map_range(.7, 1, 1, 0)

        geo = G().scale(geo, x=scale)

        geo.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Set fade and color
    #
    # Set the color, fade and material

    with GeoNodes("Set Aspect"):

        geo = Mesh(Geometry())
        with Panel("Aspect"):
            color  = Color('black', 'Color')
            fade   = Float.Factor(0, "Fade", 0, 1)
            mat    = Material("Formula", "Material")

        comps = geo.separate_components()
        geo = Mesh(comps.mesh + comps.curve.fill_ngons())

        geo.faces._Color = color
        geo.faces.material = mat

        faded = G().fade(geo, fade=fade)

        faded.out("Geometry")
        geo.out("Not Faded")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Split the geometry with the id
    #
    # - item : the selected item
    # - remain : all but the item
    # - left : left faces
    # - right : right faces
    #
    # Note that remain = left + right

    with GeoNodes("Node Id Split"):

        geo = Mesh(Geometry())
        item_id = Integer(0, "Id", single_value=True)

        # ----- Select the group

        geo = GTree.select_tree(geo, id=item_id)

        # ----- Separate on selection

        item   = Mesh(geo).faces[GTree.info().node.selected].separate()
        remain = Mesh(item.inverted_)
        dims   = G().dimensions(item).node

        left_part = Mesh(remain).faces[nd.position.x <= dims.x_mid].separate()
        right_part = left_part.inverted_

        null_id = item_id.equal(0)

        item.switch(null_id, geo).out("Item")
        remain.switch(null_id).out("Remain")
        left_part.switch(null_id).out("Left")
        right_part.switch(null_id).out("Right")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Offset an item

    with GeoNodes("Item Offset"):

        geo       = Geometry()
        item_id   = Integer(0, "Id", single_value=True)
        dx        = Float(0, "x")
        dy        = Float(0, "y")
        scale     = Float(0, "Scale")
        space_fac = Float(1, "Space")

        # ----- Item to move

        splitten = G().node_id_split(geo, id=item_id).node
        item  = splitten.item
        left  = splitten.left
        right = splitten.right

        dims = G().dimensions(item).node

        item = G().scale(item.transform(translation=(dx, dy, 0)), x=scale, y=scale)
        right.offset = (dims.width*(space_fac - 1.), 0, 0)

        (item + (left, right)).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Locate relatively to component

    with GeoNodes("Relative Location", is_group=True):

        item = Geometry()

        with Panel("Relation"):
            ref   = Geometry(None, "Relative to")
            index = Integer.MenuSwitch({'None': 0, 'After': 1, 'Exponent': 2, 'Indice': 3, 'Numerator': 4, 'Denominator': 5, 'Above': 6, 'Below': 7, 'Before': 8}, name="Location", menu="After")

        dims = G().dimensions(item).node
        ref_dims = G().dimensions(ref).node

        right   = ref_dims.right + X_SPACE
        x_size2 = dims.width * (SCALE_IND/2)
        y_size  = dims.height * SCALE_IND

        x = Float.IndexSwitch(0., right + X_SPACE, right, right,
            right, right,
            ref_dims.x_mid - x_size2, ref_dims.x_mid - x_size2,
            ref_dims.left,
            index=index)

        y = Float.IndexSwitch(0., 0., ref_dims.over - Y_IND, ref_dims.below,
            Y_ALIGN - dims.below + Y_ABOVE, Y_ALIGN - dims.over - Y_ABOVE,
            ref_dims.over + Y_ABOVE, ref_dims.below - Y_ABOVE - y_size,
            0.,
            index=index)

        s = Float.IndexSwitch(1., 1., SCALE_IND, SCALE_IND,
            1., 1.,
            SCALE_IND, SCALE_IND,
            1.,
            index=index)

        x.out("X")
        y.out("Y")
        Vector((x, y, 0)).out("Translation")
        s.out("Scale")
        index.out("Index")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Fraction

    with GeoNodes("Node Fraction"):

        formula = Geometry()
        item_id = Integer(0, "Id", single_value=True)

        item1 = Geometry(name="Item")
        as_numerator = Boolean(False, "Numerator")

        # ----- Fraction bar will own the two items

        formula = GTree.prepare_insert(formula, item_id)
        prepare = formula.node
        # Item1 is supposed to be a separate group
        item1 = GTree.change_owner(item1, old_owner=0, new_owner=prepare.owner)

        fade = Mesh(item1).faces.sample_index(Float("Fade"), index=0)
        fade = fade.switch(Mesh(item1).points.count.equal(0), 1)
        fade_scale = fade.map_range(.7, 1, 1, 0)

        with Layout("Extract item"):
            item0 = G().node_id_split(formula, id=item_id)
            left_part  = item0.left_
            right_part = item0.right_
            dims = G().dimensions(item0).node

        num = item0.switch(as_numerator, item1)
        den = item1.switch(as_numerator, item0)

        num_dims = G().dimensions(num).node
        den_dims = G().dimensions(den).node

        # ----- Align both of them to left (we one is placed and one is somewhere)

        num.transform(translation=(-num_dims.left, 0, 0))
        den.transform(translation=(-den_dims.left, 0, 0))

        num_rel = G().relative_location(num, relative_to=den, location='Numerator').node
        den_rel = G().relative_location(den, relative_to=num, location='Denominator').node

        width = gnmath.max(num_dims.width, den_dims.width) + 2*FRAC_MARGIN

        with Layout("Fraction Bar"):
            bar = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=width, size_y=FRAC_THICK).transform(translation=(width/2, Y_ALIGN, 0))
            bar = G().set_aspect(bar, fade=fade, link_from='TREE')

            bar = GTree.set_id(bar, id=prepare.new_id, owner=prepare.owner)

            fraction = bar

        fraction += num.transform(translation=((width - num_dims.width)*(fade_scale/2), fade_scale*num_rel.y, 0))
        fraction += den.transform(translation=((width - den_dims.width)*(fade_scale/2), fade_scale*den_rel.y, 0))

        fraction = fraction.transform(translation=(dims.left, 0, 0))

        f_dims = G().dimensions(fraction).node
        (left_part + (fraction, right_part.transform(translation=(f_dims.width - dims.width, 0, 0)))).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add
    # Node version

    with GeoNodes("Node Add"):

        formula   = Geometry(None, "Formula")
        item      = Geometry(None, "Item")
        shift_ids = Boolean(True, "Shift Ids")

        with Panel("Link"):
            link_id = Integer(0, "Link Id")
            x_ofs   = Float(0, "Offset")
            scale   = Float(1, "Scale")

        # ----- Ignore faces without item id

        with Layout("Ignore faces with no Item ID"):
            ignore = -Boolean("Face ID").exists_
            formula = Mesh(formula).faces[ignore].delete()

        # ----- Split the formula

        with Layout("Get the item by id"):
            block  = G().node_id_split(formula, id=link_id)
            left   = block.left_
            right  = block.right_

        dims   = G().dimensions(block).node

        # ----- Relative location

        location = G().relative_location(item, relative_to=block).node.link_from(include='Location', panel="Link")
        index = location.index_

        # ----- Item transformation

        item0  = Geometry(item).transform(translation=location.translation + (x_ofs, 0, 0), scale=location.scale*scale)
        block0 = Geometry(block)
        delta0 = 0.

        with Layout("Numerator"):
            item_num = G().node_fraction(block, id=0, item=item, numerator=True)

        with Layout("Denominator"):
            item_den = G().node_fraction(block, id=0, item=item, numerator=False)

        with Layout("Before"):
            x_min = Mesh(item).points.attribute_statistic(nd.position.x).min
            x_max = x_min.max_
            item_bef= Mesh(item).transform(translation=(dims.left - x_min, 0, 0))
            block_bef = Geometry(block).transform(translation=(x_max - x_min, 0, 0))

        # ----- As numerator
        # 'None': 0,
        # 'After': 1,
        # 'Exponent': 2,
        # 'Indice': 3,
        # 'Numerator': 4,
        # 'Denominator': 5,
        # 'Above': 6,
        # 'Below': 7,
        # 'Before': 8

        item  = Mesh.IndexSwitch(item0, item0, item0, item0, item_num, item_den, item0, item0, item0, index=index)
        block = Mesh.IndexSwitch(None, block0, block0, block0, None, None, block0, block0, block_bef, index=index)

        new_block = item + block
        new_dims = G().dimensions(new_block).node
        delta = dims.left - new_dims.left
        new_block.transform(translation=(delta, 0, 0))
        new_dims = G().dimensions(new_block).node

        right = right.transform(translation=(new_dims.right - dims.right, 0, 0))

        (left + (new_block, right)).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add
    # Modifier Version

    with GeoNodes("Add"):

        formula  = Geometry()
        item_obj = Object("Item")

        item = item_obj.info().geometry

        G().node_add(formula, item=item, link_from='TREE').out()


    # -----------------------------------------------------------------------------------------------------------------------------
    # Set location

    with GeoNodes("Move"):

        geo = Geometry()
        factor = Float.Factor(0, "Factor", 0, 1)

        with Panel("From"):
            ref0 = Geometry(None, "Relative to")

        with Panel("To"):
            ref1 = Geometry(None, "Relative to")

        node0 = G().relative_location(geo, relative_to=ref0, location=('Location', 'From')).node
        node1 = G().relative_location(geo, relative_to=ref1, location=('Location', 'To')).node

        translation = node0.translation.mix(node1.translation, factor)
        scale = factor.map_range(to_min=node0.scale, to_max=node1.scale)

        geo = geo.transform(translation=translation, scale=scale)

        geo.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Base formula string
    #
    # Create the curves from the string passed as argument
    # Options are : font face (italic, bold), color and fade (1 for transparent)
    #
    # Returns the curves and the dimensions

    with GeoNodes("Characters"):

        base = Geometry()

        s      = String(None, "Chars")

        italic = Boolean(False, "Italic")
        bold   = Boolean(False, "Bold")

        ret_id = Boolean(True, "Ret Id", hide_in_modifier=True)

        s = G().latex_codes(s)

        reg = String(s).to_curves(size=FONT_SIZE, font=FONTS.regular)
        itl = String(s).to_curves(size=FONT_SIZE, font=FONTS.italic)
        bld = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold)
        bit = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold_italic)

        curves = reg.switch(bold, bld).switch(italic, itl.switch(bold, bit))

        curves = Curve(curves.realize())

        # Align to left
        if False:
            dims   = G().dimensions(curves).node
            curves = curves.transform(translation=(-dims.left, 0, 0))

        mesh = G().set_aspect(curves, link_from='TREE')
        new_id = GTree.get_max_id(base) + 1
        mesh = GTree.set_id(mesh, id=new_id, owner=0)
        mesh = G().node_add(base, item=mesh, link_from='TREE')

        Boolean(ret_id).info("Id: " + new_id.to_string())

        mesh.switch(s.length().equal(0)).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Brackets

    with GeoNodes("Brackets"):

        formula = Geometry()
        index   = Integer.MenuSwitch({'Parenthesis': 0, 'Brackets': 1, 'Absolute': 2, 'Braces': 3, 'Norm': 4, 'Angles': 5, 'Token': 6}, name="Brackets")
        left    = Boolean(True, "Left")
        right   = Boolean(True, "Right")

        item_id = Integer(0, "Id", single_value=True)

        # ----- Prepapre the insertion of the brackets
        # prepare node contains new_id and owner for the brackets

        formula = GTree.prepare_insert(formula, id=item_id)
        prepare = formula.node

        # ----- Around item id

        item = G().node_id_split(formula, id=item_id)
        left_part  = item.left_
        right_part = item.right_
        dims = G().dimensions(item).node

        # ----- Brackets selection

        brackets = [[], []]
        for chars in ['()', '[]', '||', '{}', '‖‖', '⟨⟩', '<>']:
            for i in range(2):
                with Layout(f"Bracket {chars[i]}"):
                    br_node = G().characters(chars=chars[i]).node.link_from(include='Aspect')
                    br_dims = G().dimensions(br_node).node
                    br = br_node.geometry.transform(translation=(0, -br_dims.y_mid, 0))

                    scale = PAR_SCALE*gnmath.min(1, dims.height)
                    tr = (0, dims.y_mid, 0)
                    brackets[i].append(br.transform(translation=tr, scale=(1, scale, 1)))

        # ----- Brackets instantiation

        open  = Curve.IndexSwitch(*brackets[0], index=index)
        close = Curve.IndexSwitch(*brackets[1], index=index)

        # ----- Id and owner

        open  = GTree.set_id(open,  id=prepare.new_id, owner=prepare.owner)
        close = GTree.set_id(close, id=prepare.new_id, owner=prepare.owner)

        # ----- Brackets dims

        open_dims = G().dimensions(open).node
        tr1 = (open_dims.right + X_SPACE).switch_false(left)
        tr2 = tr1 + (dims.width + X_SPACE)

        new_item = open.switch_false(left).transform(translation=(dims.left, 0, 0))
        new_item += item.transform(translation=(tr1, 0, 0))
        new_item += close.transform(translation=(dims.left + tr2, 0, 0)).switch_false(right)

        new_dims = G().dimensions(new_item).node
        tr = new_dims.width - dims.width

        (left_part + (new_item, right_part.transform(translation=(tr, 0, 0)))).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Above decoration

    with GeoNodes("Accentuation"):

        unit = DECO_THICK

        formula = Geometry()
        index   = Integer.MenuSwitch({'Arrow': 0, 'Bar': 1, 'Dot': 2, 'Double dot': 3, 'Triple Dot': 4}, name="Decorator")
        item_id = Integer(0, "Id", single_value=True)
        bottom  = Boolean(False, "Bottom")

        # ----- Prepare decoration insertion

        formula = GTree.prepare_insert(formula, item_id)
        prepara = formula.node

        # ----- Around item id

        item  = G().node_id_split(formula, id=item_id)
        left  = item.left_
        right = item.right_

        dims = G().dimensions(item).node

        # ----- Usefull dims

        y = (dims.over + Y_ABOVE).switch(bottom, dims.below - Y_ABOVE)

        with Layout("Bar and Arrow dims"):
            left_margin = 2*unit
            right_margin = 4*unit
            bar_width = dims.width + left_margin + right_margin

        with Layout("Dot Char"):
            dot_node = G().characters(chars='.').node.link_from(include='Aspect')
            dot_dims = G().dimensions(dot_node).node
            dot_width = dot_dims.width
            dot = dot_node.geometry.transform(translation=(-dot_dims.x_mid, -dot_dims.y_mid, 0), scale=1)

        # ----- 0 : Arrow

        with If(Curve, index) as deco:

            r = Curve.Circle(resolution=7)

            w2 = unit/2
            ar_x_int  = unit*4
            ar_x_wing = unit*2
            ar_y_wing = unit*1.5

            r[0].position = (-left_margin, -w2, 0)
            r[1].position = (-left_margin + bar_width - ar_x_int, -w2, 0)
            r[2].position = (-left_margin + bar_width - (ar_x_int + ar_x_wing), -w2 - ar_y_wing, 0)
            r[3].position = (-left_margin + bar_width, 0, 0)
            r[nd.index > 3].position = r.points.sample_index(nd.position*(1, -1, 1), index=6-nd.index)

            r = r.transform(translation=(dims.left, y, 0))

            deco.option = r

        # ----- 1 : Bar

        with Elif(deco):
            r = Curve.Quadrilateral(width=bar_width, height=DECO_THICK)
            r = r.transform(translation=(dims.x_mid, y, 0))

            deco.option = r

        # ----- 2 : Dot

        with Elif(deco):

            deco.option = Curve(dot).transform(translation=(dims.x_mid, y, 0))

        # ----- 3 : Double dots

        with Elif(deco):

            dx = (dot_width + X_SPACE)/2

            deco.option = Curve(dot).transform(translation=(dims.x_mid - dx, y, 0)) + Curve(dot).transform(translation=(dims.x_mid + dx, y, 0))

        # ----- 4 : Triple dots

        with Elif(deco):

            dx = dot_width + X_SPACE

            deco.option = Curve(dot).transform(translation=(dims.x_mid - dx, y, 0)) + Curve(dot).transform(translation=(dims.x_mid, y, 0)) + Curve(dot).transform(translation=(dims.x_mid + dx, y, 0))

        # ----- Complete deco

        deco = G().set_aspect(deco, link_from='TREE')
        deco = GTree.set_id(deco, id=prepare.new_id, owner=prepare.owner)

        # ---- Put deco on item

        tr = Float.IndexSwitch(left_margin, left_margin, 0, 0, 0, index=index)
        accentuated = (deco + item).transform(translation=(tr, 0, 0))

        r_tr = left_margin+right_margin
        r_tr = Float.IndexSwitch(r_tr, left_margin+right_margin, 0, 0, 0, index=index)


        (left + (accentuated, right.transform(translation=(r_tr, 0, 0)))).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sigma

    with GeoNodes("Sigma"):

        formula = Geometry()
        sbelow  = String(name="From")
        sabove  = String(name="To")
        item_id = Integer(0, "Id")

        # Sigma will group:
        # - The content : (item_id, owner) -> (item_id, sigma_id)
        # - below : (new_id, sigma_id)
        # - above : (new_id + 1, sigma_id)
        # - sigma itself: (sigma_id, owner)

        formula = GTree.prepare_insert(formula)
        new_id = formula.new_id_
        owner  = formula.owner_

        sigma_id = new_id + 2

        # ----- Extract the item for size

        item  = G().node_id_split(formula, id=item_id)

        with Layout("Sigma Symbol"):
            sigma = G().node_sigma_char(fill=True)
            sigma = G().set_aspect(sigma, link_from='TREE')

            fade = Tree.current_tree.input_node.fade
            fade_scale = fade.map_range(.7, 1, 1, 0)

        with Layout("Scale to fit with content"):
            sigma_dims = G().dimensions(sigma).node
            dims = G().dimensions(item).node

            scale = PAR_SCALE*gnmath.max(1, dims.height/sigma_dims.height)
            sigma = sigma.transform(translation=(0, dims.y_mid - scale*sigma_dims.y_mid, 0), scale=scale*(fade_scale, 1, 1))
            sigma_dims = G().dimensions(sigma).node

        below = G().characters(chars=sbelow, italic=True)
        above = G().characters(chars=sabove, italic=True)

        null = fade_scale.equal(0)
        geo = Mesh(sigma).switch(null)

        # ----- Sigma id with content owner
        geo = GTree.set_id(geo, sigma_id, owner=owner)

        for g, loc, add_id in [(below, 'Below', new_id), (above, 'Above', new_id + 1)]:
            node = G().relative_location(g, relative_to=sigma, location=loc).node
            add = g.transform(translation=node.translation, scale=node.scale)
            if loc != 'After':
                add = G().fade(add, fade=fade)

            add = GTree.set_id(add, id=add_id, owner=sigma_id)

            geo += add

        geo = G().node_add(formula=formula, item=geo, location='Before', link_id=item_id)

        geo.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sign

    with GeoNodes("Sign"):

        formula = Geometry()
        plus    = Float.Factor(0, "Plus", 0, 1)
        item_id = Integer(0, "Id")

        # Id

        formula = GTree.prepare_insert(formula)
        prepare = formula.node

        with Layout("Build the sign"):
            hrz = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_WIDTH, size_y=PLUS_THICK)
            vrt = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_THICK, size_y=plus*PLUS_WIDTH)

            sign = hrz.switch(plus > 0, hrz + vrt)

            sign = sign.transform(translation=(PLUS_WIDTH/2, Y_ALIGN, 0))
            sign = G().set_aspect(sign, link_from='TREE')
            sign = GTree.set_id(sign, id=prepare.new_id, owner=prepare.owner)

        geo = G().node_add(formula=formula, item=sign, location='Before', link_id=item_id)

        geo.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Square Root

    with GeoNodes("Sqrt"):

        formula = Geometry()
        n       = Integer(2, "n", 2)
        item_id = Integer(0, "Id", single_value=True)

        with Panel("Aspect"):
            fade = Float.Factor(0, "Fade", 0, 1)
        fade_scale = fade.map_range(.7, 1, 1, 0)

        # ----- New id

        formula = GTree.prepare_insert(formula, id=item_id)
        prepare = formula.node

        with Layout("Get the item by id"):
            item   = G().node_id_split(formula, id=item_id)
            left   = item.left_
            right  = item.right_

        dims = G().dimensions(item).node

        sqrt = G().node_sqrt_char(fill=False)
        sqrt_dims = G().dimensions(sqrt).node

        with Layout("Scale to fit with content"):

            x_content = sqrt_dims.width

            scale = PAR_SCALE*gnmath.max(1, dims.height)

            sqrt = sqrt.transform(translation=(dims.left, dims.y_mid - scale*sqrt_dims.y_mid, 0), scale=(scale*fade_scale, scale, scale))

            sqrt = Curve(sqrt)
            count = sqrt.points.count
            sqrt.points[count-3, count-2].offset = (dims.width*fade_scale, 0, 0)

        sqrt = G().set_aspect(sqrt, link_from='TREE')
        sqrt = GTree.set_id(sqrt, id=prepare.new_id, owner=owner)
        sqrt += item.transform(translation=(x_content*scale*fade_scale, 0, 0))

        sqrt_dims = G().dimensions(sqrt).node

        geo = left + (sqrt, right.transform(translation=(sqrt_dims.width - dims.width, 0, 0)))

        geo.out()

# =============================================================================================================================
# =============================================================================================================================
# Animation
# =============================================================================================================================
# =============================================================================================================================

# =============================================================================================================================
# Animation curves

class Key:
    def __init__(self, time: float, value: float, interpolation='SMOOTH'):
        self.time          = time
        self.value         = value
        self.interpolation = interpolation

# -----------------------------------------------------------------------------------------------------------------------------
# Animation curve builder

class AnimationCurve(list):

    def __init__(self, name: str, value: float):
        super().__init__()
        self.name = name
        self.append(Key(0., value))

    def build_curve(self):

        with Layout(f"Curve - {self.name}"):

            line = Curve.Line().resample(len(self))
            line.splines.type = 'BEZIER'

            for i, kf in enumerate(self):
                line.points[i].position=(kf.time, kf.value, 0)

            return line

            #line.out(self.name)

    @property
    def time(self):
        return self[-1].time

    @property
    def value(self):
        return self[-1].value

    def add(self, time, value, interpolation='SMOOTH'):
        self[-1].interpolation = interpolation
        self.append(Key(time, value))

    def mark(self, time: float):
        self.add(time, self.value)

    def change(self, time: float, duration: float, value: float, interpolation='SMOOTH'):
        self.mark(time)
        self.add(time + duration, value, interpolation)

    def pingpong(self, time: float, duration: float, value: float, interpolation='SMOOTH'):
        old = self.value
        self.mark(time)
        self.add(time + duration/2, value, interpolation)
        self.add(time + duration, old, interpolation)

# -----------------------------------------------------------------------------------------------------------------------------
# Animation group builder

class AnimationCurves(list):

    def new(self, name: str, value: float):
        ac = AnimationCurve(name, value)
        self.append(ac)
        return ac

    def build_node(self, name, to_node):

        with GeoNodes(name, is_group=True):

            for ac in self:
                line = ac.build_curve()
                value = G().time_line_curve(line)
                value.out(ac.name)

        anim_node = Group(name)
        for ac in self:
            setattr(to_node, ac.name.lower(), getattr(anim_node, ac.name.lower()))

# -----------------------------------------------------------------------------------------------------------------------------
# Build a block animator

def build_item_animator(name):

    with GeoNodes(f"{name} Animator"):

        with Panel(name):

            x            = Float(0, "X")
            y            = Float(0, "Y")
            scale        = Float(1, "Scale")
            width_offset = Float(0, "Width Offset")

        node = Group(name, sockets=parameters, link_from='TREE')

        geo = node._out
        geo = geo.transform(translation=(x + width_offset/2, y, 0), scale=scale)

        geo.out()

# =============================================================================================================================
# groups

def build_anim():

    with GeoNodes("Time Line Curve", is_group=True):
        curve = Curve()
        t = nd.scene_time().seconds

        x_max = curve.points.attribute_statistic(nd.position.x).max
        x = gnmath.max(0, gnmath.min(t, x_max))

        factor = x/x_max

        v = curve.sample_factor(nd.position.y, factor=factor)
        v.out("Value")

    with GeoNodes("Write"):

        content = Mesh(Geometry())
        factor  = Float.Factor(1, "Factor", 0, 1)

        cur_fade = content.faces.sample_index(Float("Fade"), index=0)

        dims = G().dimensions(content).node
        x = factor.map_range_linear(to_min=dims.left, to_max=dims.right)
        content.faces._Fade = nd.position.x.map_range_linear(x-.2, x, 0, cur_fade)

        content.out()

    with GeoNodes("Animator"):

        content = Geometry()

        # Location
        x            = Float(0, "X")
        y            = Float(0, "Y")
        scale        = Float(1, "Scale")
        width_offset = Float(0, "Width Offset")

        # Aspect
        color        = Color('black', "Color")
        fade         = Float.Factor(0, "Fade", 0, 1)

        # Sign
        plus         = Float.Factor(0, "Sign Plus")
        sign_fade    = Float.Factor(1, "Sign Fade")

        # Write
        write        = Float.Factor(1, "Write", 0, 1)

        # Show
        show         = Boolean(True, "Show")

        geo = G().sign(content, plus=plus, fade=sign_fade, color=color)
        geo = G().set_aspect(G().sign(geo, plus=plus, fade=sign_fade), fade=fade, color=color)
        geo = geo.transform(translation=(x + width_offset/2, y, 0), scale=scale)

        geo = G().write(geo, factor=write)

        geo.switch_false(show).out()
