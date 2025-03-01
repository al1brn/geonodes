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
Y_SPACE      = 0.1   # Horizontal spacing
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

# ===== Math operators

OP_PLUS     = 1
OP_MINUS    = 2
OP_VAR_SIGN = 3

# ===== Node Types

TYPE_GROUP  = 0 # Group of nodes with decorator
TYPE_GEO    = 1 # Simple geometry
TYPE_CONT2  = 2 # Special with 2 nodes
TYPE_CONT3  = 3 # Special with 3 nodes

# ===== Codes

CONT2_FRACTION  = 0

CONT3_EXP_IND  = 0
CONT3_SIGMA    = 1
CONT3_INTEGRAL = 2

DECO_NOTHING            =  0
DECO_PLUS               =  1
DECO_MINUS              =  2
DECO_VAR_SIGN           =  3
DECO_SQRT               =  4

DECO_ARROW              = 10
DECO_LEFT_ARROW         = 11
DECO_BAR                = 12
DECO_DOT                = 12
DECO_DOT2               = 14
DECO_DOT3               = 15

DECO_BLOCK              = 20
DECO_PARENTHESIS        =  0
DECO_BRACKETS           =  1
DECO_BRACES             =  2
DECO_ABSOLUTE           =  3
DECO_NORM               =  4
DECO_ANGLE              =  5
DECO_TOKEN              =  6


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

    # ----------------------------------------------------------------------------------------------------
    # Formula reference (transparent, not displayed)

    with ShaderNodes("Formula Reference"):

        Shader.Transparent().out()


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

    FONTS = Fonts()

    formula_tree.build_tree(prefix='Tree')
    GTree = G("Tree")

    prefix = "Util"
    Util = G(prefix)

    # ----- Built in symbols

    create_curve("Util Sqrt Char", formula_data.SQRT_CHAR)
    create_curve("Util Sigma Char", formula_data.SIGMA_CHAR)

    def macro_is_ref():
        return Boolean("Reference")

    def macro_is_work():
        return -Boolean("Reference")

    def macro_get_ref(mesh):

        ref  = mesh.faces[macro_is_ref()].separate()
        work = ref.inverted_

        return Mesh(ref), Mesh(work)

    def macro_setup_ref(mesh, ref_type):
        mesh.faces._Reference = True
        mesh.faces._Type = ref_type

        mesh.faces.material = "Formula Reference"
        mesh.offset = (0, 0, -1)
        return mesh

    def macro_setup_work(mesh, item_id, explore):
        with Layout("Set up"):

            z = mesh.points.attribute_statistic(nd.position.z).min
            mesh.transform(translation=(0, 0, -z))

            mesh.faces._Reference = False

            mesh.faces.material = "Formula"
            mesh.faces._Item_ID = item_id
            mesh.faces._Explore = explore

            return mesh

    def macro_create_work(ref, item_id, explore):
        with Layout("Create Work faces from reference"):

            mesh = Mesh(ref).faces[Integer("Item ID").equal(item_id)].separate()

            mesh = Mesh(mesh)
            vmin = -mesh.points.attribute_statistic(nd.position).min
            x, y, z = vmin.xyz
            mesh.transform(translation=(x, 0, z))

            mesh.faces._Reference = False

            mesh.faces.material = "Formula"
            mesh.faces._Item_ID = item_id
            mesh.faces._Explore = explore

            return mesh

    # =============================================================================================================================
    # Dimensions

    with GeoNodes("Dimensions", prefix=prefix, is_group=True):

        mesh = Mesh()
        selection = Boolean(False, "Selection", hide_value=True)

        vmin = mesh.points[selection].attribute_statistic(nd.position).min
        vmax = vmin.max_
        vmid = (vmin + vmax)/2

        x0, y0, _     = vmin.xyz
        x1, y1, _     = vmax.xyz
        xmid, ymid, _ = vmid.xyz

        vmin.out(       "Min")
        vmax.out(       "Max")

        (x1 - x0).out(  "Width")
        (y1 - y0).out(  "Height")
        x0.out(         "X Min")
        y0.out(         "Y Min")
        x1.out(         "X Max")
        y1.out(         "Y Max")
        xmid.out(       "X Mid")
        ymid.out(       "Y Mid")

    # =============================================================================================================================
    # LaTeX codes

    with GeoNodes("LaTeX Codes", prefix=prefix, is_group=True):

        s = String(None, "String")

        keys = sorted(formula_data.SYMBOLS.keys(), key= lambda x: 100 - len(x))

        for code in keys:
            c = formula_data.SYMBOLS[code]
            s = s.replace("\\" + code, c)

        s.out()

    # =============================================================================================================================
    # Geometry

    # -----------------------------------------------------------------------------------------------------------------------------
    # Characters

    with GeoNodes("Characters", prefix=prefix, is_group=True):

        s      = String(None,   "Chars")
        italic = Boolean(False, "Italic")
        bold   = Boolean(False, "Bold")

        s = Util.latex_codes(s)

        reg = String(s).to_curves(size=FONT_SIZE, font=FONTS.regular)
        itl = String(s).to_curves(size=FONT_SIZE, font=FONTS.italic)
        bld = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold)
        bit = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold_italic)

        curves = reg.switch(bold, bld).switch(italic, itl.switch(bold, bit))

        curves = Curve(curves.realize())

        chars = curves.fill_ngons()
        dims = Util.dimensions(chars, selection=True).node

        chars = macro_setup_ref(chars, ref_type=TYPE_GEO)

        chars.out()
        dims.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Shape
    # 0: Rect, 1: Circle, 2: Triangle

    with GeoNodes("Shape", prefix=prefix, is_group=True):

        index    = Integer(0, "Code")
        width    = Float(1, "Width")
        height   = Float(1, "Height")
        tracking = Float(.1, "Tracking")

        with If(Mesh, index) as shape:
            shape.option = Mesh.Grid(width, height, 2, 2)

        with Elif(shape):
            shape.option = Mesh.Circle().transform(scale=(width, height, 1))

        with Elif(shape):
            shape.option = Mesh.Circle(vertices=3).transform(scale=(width, height, 1))

        vmin = shape.points.attribute_statistic(nd.position).min
        x, y, _ = vmin.xyz

        shape.transform(translation=(-x, -y - tracking, 0))
        dims = Util.dimensions(shape).node

        shape = macro_setup_ref(shape, ref_type=TYPE_GEO)

        shape.out()
        dims.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Math operators
    # see OP_xxx

    with GeoNodes("Operator", prefix=prefix, is_group=True):

        code  = Integer(1, "Code")
        param = Float.Factor(1, "Parameter", 0, 1)

        with Layout("Plus / Minus"):

            hrz = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_WIDTH, size_y=PLUS_THICK)
            vrt = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_THICK, size_y=PLUS_WIDTH)

            op = hrz.switch_false(code.equal(OP_MINUS))

            op = op.switch(code.equal(OP_PLUS), hrz + vrt)

            vrt.transform(scale=(1, param, 1))
            op = op.switch(code.equal(OP_VAR_SIGN), hrz + vrt)

        dims = Util.dimensions(op).node

        op = macro_setup_ref(op, ref_type=TYPE_GEO)

        op.out()
        dims.out()

    # =============================================================================================================================
    # DECORATORS

    with GeoNodes("Decorator", prefix=prefix, is_group=True):

        unit = DECO_THICK

        mesh = Mesh()

        content = Boolean(False, "Content", hide_value=True)

        item_id = Integer(1,      "Id", 1)
        explore = Integer(1,      "Explore", 1)
        factor  = Float.Factor(1, "Factor", 0, 1)

        code    = Integer(0,     "Code")
        option1 = Boolean(False, "Option 1")
        option2 = Boolean(False, "Option 2")
        param   = Float(0.,      "Param")

        # ----- Dimensions

        dims = Util.dimensions(mesh, content).node

        # ----------------------------------------------------------------------------------------------------
        # Accentuation : arrows, dots, bar
        # ----------------------------------------------------------------------------------------------------

        with Layout("Accentuation: arrow, bar, dot"):

            y = (dims.y_max + Y_ABOVE).switch(option1, dims.y_min - Y_ABOVE)

            with Layout("Bar and Arrow dims"):
                left_margin  = 2*unit
                right_margin = 4*unit
                bar_width = (dims.width + left_margin + right_margin)._lc("Bar Width")
                bar_width2 = (bar_width/2)._lc("Bar Width / 2")

            with Layout("Dot Char"):
                dot_node = Util.characters(chars='.').node
                dot = Mesh(dot_node._out)
                dot.transform(translation=(-dot_node.width/2, y - dot_node.height/2, 0))
                dot_dx = (dot_node.width + X_SPACE)/2

                dot = macro_setup_work(dot, item_id, explore)

            with Layout("Arrow"):

                r = Curve.Circle(resolution=7)

                w2 = unit/2
                ar_x_int  = unit*4
                ar_x_wing = unit*2
                ar_y_wing = unit*1.5

                r[0].position = (0, -w2, 0)
                r[1].position = (bar_width - ar_x_int, -w2, 0)
                r[2].position = (bar_width - (ar_x_int + ar_x_wing), -w2 - ar_y_wing, 0)
                r[3].position = (bar_width, 0, 0)
                r[nd.index > 3].position = r.points.sample_index(nd.position*(1, -1, 1), index=6-nd.index)

                r.transform(translation=(bar_width2, y, 0))
                r = r.fill_ngons()
                r = macro_setup_work(r, item_id, explore)

                deco = Mesh(mesh) + r
                deco.points[content].offset = (left_margin, 0, 0)

                mesh = mesh.switch(code.equal(DECO_ARROW), deco)

            with Layout("Left Arrow"):

                r.transform(translation=(-bar_width2, 0, 0))
                r.transform(scale=(-1, 1, 1))
                r.transform(translation=(bar_width2, 0, 0))
                r.flip_faces()

                deco = Mesh(mesh) + r
                deco.points[content].offset = (left_margin, 0, 0)

                mesh = mesh.switch(code.equal(DECO_LEFT_ARROW), deco)

            with Layout("Bar"):

                r = Mesh.Grid(bar_width, DECO_THICK, 2, 2).transform(translation=(bar_width2, y, 0))

                r = macro_setup_work(r, item_id, explore)

                deco = Mesh(mesh) + r
                deco.points[content].offset = (left_margin, 0, 0)

                mesh = mesh.switch(code.equal(DECO_BAR), deco)

            with Layout("Dots"):

                is_dot  = code.equal(DECO_DOT)
                is_dot2 = code.equal(DECO_DOT2)
                is_dot3 = code.equal(DECO_DOT3)

                dot2 = Mesh(dot).transform(translation=( -dot_dx, 0, 0))  + Mesh(dot ).transform(translation=(dot_dx, 0, 0))
                dot3 = Mesh(dot).transform(translation=(-2*dot_dx, 0, 0)) + Mesh(dot2).transform(translation=(dot_dx, 0, 0))

                r = dot.switch(is_dot2, dot2).switch(is_dot3, dot3)
                deco = Mesh(mesh) + r

                mesh = mesh.switch(is_dot | is_dot2 | is_dot3, deco)

        # ----------------------------------------------------------------------------------------------------
        # Block
        #
        # DECO_BLOCK              = 20
        # DECO_PARENTHESIS        =  0
        # DECO_BRACKETS           =  1
        # DECO_BRACES             =  2
        # DECO_ABSOLUTE           =  3
        # DECO_NORM               =  4
        # DECO_ANGLE              =  5
        # DECO_TOKEN              =  6
        # ----------------------------------------------------------------------------------------------------

        with Layout("Block : parenthesis, brackets, ..."):

            with Layout("A valid code"):
                block_code = (code - DECO_BLOCK)
                is_block = (block_code >= 0) & (block_code < DECO_TOKEN)
                block_code = block_code.switch_false(is_block, 0)._lc("Block Code")

                use_left  = option1
                use_right = option2

            # ---------------------------------------------------------------------------
            # Brackets instantiation

            BRACKETS = ['()', '[]', '||', '{}', '‖‖', '⟨⟩', '<>']
            brackets = [[], []]
            for chars in BRACKETS:
                for i in range(2):
                    with Layout(f"Bracket {chars[i]}"):

                        br_node = Util.characters(chars=chars[i]).node
                        br = br_node.geometry
                        br.transform(scale=(1, PAR_SCALE*gnmath.min(1, dims.height), 1))

                        brackets[i].append(br)

            # ---------------------------------------------------------------------------
            # Brackets selection

            with Layout("Select the brackets"):
                open  = Mesh.IndexSwitch(*brackets[0], index=block_code)
                close = Mesh.IndexSwitch(*brackets[1], index=block_code)

                open  = macro_setup_work(open,  item_id, explore)
                close = macro_setup_work(close, item_id, explore)

            with Layout("Opening bracket"):

                b_dims = Util.dimensions(open, selection=True).node

                deco = Mesh(mesh) + open
                deco.points[content].offset = (b_dims.width + X_SPACE/3, 0, 0)

                mesh = mesh.switch(use_left & is_block, deco)

            with Layout("Closing bracket"):

                new_dims = Util.dimensions(mesh, content).node
                close.transform(translation=(new_dims.x_max + X_SPACE/3, 0, 0))

                deco = Mesh(mesh) + close

                mesh = mesh.switch(use_right & is_block, deco)

        mesh.out()

    # =============================================================================================================================
    # TWO CONTENTS

    # -----------------------------------------------------------------------------------------------------------------------------
    # Fraction

    with GeoNodes("Fraction", prefix=prefix, is_group=True):

        mesh = Mesh()

        num_sel = Boolean(False, "Numerator",   hide_value=True)
        den_sel = Boolean(False, "Denominator", hide_value=True)

        item_id = Integer(1, "Id", 1)
        explore = Integer(1, "Explore", 1)
        factor  = Float.Factor(1, "Factor", 0, 1)

        ndims = Util.dimensions(mesh, num_sel).node
        ddims = Util.dimensions(mesh, den_sel).node

        with Layout("Build the bar"):

            width = gnmath.max(ndims.width, ddims.width) + 2*FRAC_MARGIN
            x_center = width/2
            bar = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=width, size_y=FRAC_THICK).transform(translation=(x_center, Y_ALIGN, 0))

            bar = macro_setup_work(bar, item_id, explore)

        with Layout("Locate numerator and denominator"):

            mesh.points[num_sel].offset = (x_center - ndims.x_mid,  FRAC_THICK + Y_SPACE - ndims.y_min, 0)
            mesh.points[den_sel].offset = (x_center - ddims.x_mid, -FRAC_THICK - Y_SPACE - ndims.y_max, 0)

        mesh.out()

    # =============================================================================================================================
    # TWO CONTENTS

    # -----------------------------------------------------------------------------------------------------------------------------
    # Exponent & Indice

    with GeoNodes("Exponent Indice", prefix=prefix, is_group=True):

        mesh = Mesh()

        content  = Boolean(False, "Content",   hide_value=True)
        exponent = Boolean(False, "Exponent",  hide_value=True)
        indice   = Boolean(False, "Indice",    hide_value=True)

        factor  = Float.Factor(1, "Factor", 0, 1)

        # ----- Dimensions

        cdims = Util.dimensions(mesh, content).node
        edims = Util.dimensions(mesh, exponent).node
        idims = Util.dimensions(mesh, indice).node

        with Layout("Scale Exponent and Indice"):
            mesh.points[exponent].position *= SCALE_IND
            mesh.points[indice].position *= SCALE_IND

        with Layout("Offset Exponent and Indice"):
            left = cdims.x_max + X_SPACE/3

            mesh.points[exponent].offset = (left, cdims.y_min + .8*cdims.height, 0)
            mesh.points[indice].offset   = (left, cdims.y_min + .1*cdims.height, 0)

        mesh.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sigma

    with GeoNodes("Sigma", prefix=prefix, is_group=True):

        mesh = Mesh()

        content  = Boolean(False, "Content", hide_value=True)
        below    = Boolean(False, "Below",   hide_value=True)
        above    = Boolean(False, "Above",   hide_value=True)

        item_id = Integer(1, "Id", 1)
        explore = Integer(1, "Explore", 1)
        factor  = Float.Factor(1, "Factor", 0, 1)

        with Layout("Scale Below and Above"):
            mesh.points[below].position *= SCALE_IND
            mesh.points[above].position *= SCALE_IND

        # ----- Dimensions

        cdims = Util.dimensions(mesh, content).node
        bdims = Util.dimensions(mesh, below).node
        adims = Util.dimensions(mesh, above).node

        # ----- Sigma Symbol

        with Layout("Sigma Symbol"):

            # ----- Base
            sigma = Mesh(Util.sigma_char(fill=True))

            # ----- Height
            sigma_height = PAR_SCALE*gnmath.max(1, cdims.height)
            sigma.transform(scale=(1, sigma_height, 1))

            # ----- Vertical center with content
            sigma.transform(translation=(0, cdims.y_mid - sigma_height/2, 0))

            # ----- Add to the mesh
            sigma = macro_setup_work(sigma, item_id, explore)
            mesh += sigma

            # ----- Get the final dims
            sdims = Util.dimensions(mesh, Integer("ID").equal(item_id)).node

        with Layout("Locate content"):
            mesh.points[content].offset = (sdims.x_max + X_SPACE/3, 0, 0)

        with Layout("Locate Below and Above"):
            mesh.points[below].offset = (sdims.x_mid - bdims.x_mid, sdims.y_min - Y_SPACE - bdims.y_max , 0)
            mesh.points[above].offset = (sdims.x_mid - adims.x_mid, sdims.y_max + Y_SPACE - bdims.y_min , 0)

        mesh.out()

    # =============================================================================================================================
    # Formula Compilation
    #
    # Node Type: how to deal with sub nodes
    # TYPE_GROUP  = 0 # Group of nodes with decorator
    # TYPE_GEO    = 1 # Simple geometry
    # TYPE_CONT2  = 2 # Special with 2 nodes
    # TYPE_CONT3  = 3 # Special with 2 nodes
    #
    # Node Role: role within the owner
    # - CONTENT 0 : content
    # - PARAM1  1 : first parameter
    # - PARAM2  2 : second parameter
    #
    #
    # Node parameters:
    # - Type : in [GEO, GROUP, CONT2, CONT3]
    # - Code :
    #   - GEO   : always 0
    #   - GROUP : decorator code
    #   - CONT2 : FRACTION, NSQRT
    #   - CONT3 : EXP, SIGMA, INTEGRAL
    # - Argument : Argument order for multicontent owner
    # - Factor : Factor effect
    # - Color : Color
    # - Fade : Fade factor
    # - Option 1 : decorator option 1
    # - Option 2 : decorator option 2
    # - Param : decoratoir param
    #
    # The whole formula is built bottom up, starting from the last node
    #
    # =============================================================================================================================

    with GeoNodes("Index Info", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")
        index = Integer(0, "Index")

        info = GTree.index_info(tree, index=index).node
        info.out()

        tree.points.sample_index(Integer(  "Type"),     index=index).out("Type")
        tree.points.sample_index(Integer(  "Code"),     index=index).out("Code")
        tree.points.sample_index(Integer(  "Argument"), index=index).out("Argument")
        tree.points.sample_index(Float(    "Factor"),   index=index).out("Factor")
        tree.points.sample_index(Color(    "Color"),    index=index).out("Color")
        tree.points.sample_index(Integer(  "Fade"),     index=index).out("Fade")

        tree.points.sample_index(Integer(  "Role"),     index=index).out("Role")

        tree.points.sample_index(Boolean(  "Option 1"), index=index).out("Option 1")
        tree.points.sample_index(Boolean(  "Option 2"), index=index).out("Option 2")
        tree.points.sample_index(Float(    "Param"),    index=index).out("Param")

    with GeoNodes("Id Info", prefix=prefix, is_group=True):

        tree    = Cloud(None, "Tree")
        node_id = Integer(1,  "Id")

        Util.index_info(tree, index=GTree.id_info(tree, id=node_id)).node.out()

    with GeoNodes("Explore Info", prefix=prefix, is_group=True):

        tree    = Cloud(None, "Tree")
        explore = Integer(1,  "Explore")

        Util.index_info(tree, index=GTree.explore_info(tree, explore=explore)).node.out()


    with GeoNodes("Compile", prefix=prefix, is_group=True):

        formula = Geometry(name="Formula")
        ref_mesh, _ = macro_get_ref(formula.mesh)

        tree = formula.point_cloud

        # ----- Let's explore the tree from last to start

        count = tree.points.count
        with Repeat(mesh=None, iterations=count) as rep:

            mesh = rep.mesh

            with Layout("Last to first Explore index info"):
                expl_index = count - 1 - rep.iteration
                node_info  = Util.explore_info(tree, explore=expl_index).node
                node_id    = node_info.id._lc("Node ID")

            # ----------------------------------------------------------------------------------------------------
            # Instantiate from reference
            # ----------------------------------------------------------------------------------------------------

            with Layout("GEO: Instantiate from reference"):

                geo = macro_create_work(ref_mesh, node_id, expl_index)
                mesh = mesh.switch(node_info.type.equal(TYPE_GEO), mesh + geo)

            # ----------------------------------------------------------------------------------------------------
            # Children concatenation
            # ----------------------------------------------------------------------------------------------------

            with Layout("GROUP: sub nodes are concatanated"):

                children_count = GTree.children_count(tree, id=node_id)

                with Repeat(mesh=rep.mesh, x=0., iterations=children_count) as rep2:

                    mesh2 = rep2.mesh

                    child_id  = GTree.get_child(tree, id=node_id, order=rep2.iteration).id_
                    child_sel = GTree.select(tree, id=child_id, mode='Branch')

                    mesh2.points[child_sel].offset = (rep2.x, 0, 0)
                    vmax = mesh2.points[child_sel].attribute_statistic(nd.position).max

                    rep2.x = vmax.x + X_SPACE
                    rep2.mesh = mesh2

                mesh = mesh.switch(node_info.type.equal(TYPE_GROUP), rep2.mesh)

            with Layout("DECORATOR to apply to the group"):

                deco = Util.decorator(mesh=mesh,
                    content  = GTree.select(tree, id=node_id, mode='Children'),
                    id       = node_id,
                    explore  = expl_index,
                    factor   = factor,

                    code     = node_info.code,
                    option_1 = node_info.option_1,
                    option_2 = node_info.option_2,
                    param    = node_info.param,
                )

                mesh = mesh.switch(node_info.type.equal(TYPE_GROUP), deco)

            # ----------------------------------------------------------------------------------------------------
            # TWO CONTENTS
            # ----------------------------------------------------------------------------------------------------

            with Layout("TWO CONTENTS"):

                type2 = node_info.type.equal(TYPE_CONT2)

                role0 = GTree.selection_info(Integer("Owner").equal(node_id) & Integer("Role").equal(0)).node
                role1 = GTree.selection_info(Integer("Owner").equal(node_id) & Integer("Role").equal(1)).node

                # ----- Fraction

                with Layout("Fraction"):
                    fraction = Util.fraction(mesh,
                        numerator   = GTree.select(tree, id=role0.id, mode='Branch'),
                        denominator = GTree.select(tree, id=role1.id, mode='Branch'),
                        id      = node_id,
                        explore = expl_index,
                        factor  = factor,
                    )
                    mesh = mesh.switch(type2 & node_info.code.equal(CONT2_FRACTION), fraction)

            # ----------------------------------------------------------------------------------------------------
            # THREE CONTENTS
            # ----------------------------------------------------------------------------------------------------

            with Layout("THREE CONTENTS"):

                type3 = node_info.type.equal(TYPE_CONT3)

                role0 = GTree.selection_info(Integer("Owner").equal(node_id) & Integer("Role").equal(0)).node
                role1 = GTree.selection_info(Integer("Owner").equal(node_id) & Integer("Role").equal(1)).node
                role2 = GTree.selection_info(Integer("Owner").equal(node_id) & Integer("Role").equal(2)).node

                # ----- Exponent / indice

                with Layout("Exponent / Indice"):

                    exp_ind = Util.exponent_indice(mesh,
                        content  = GTree.select(tree, id=role0.id, mode='Branch'),
                        exponent = GTree.select(tree, id=role1.id, mode='Branch'),
                        indice   = GTree.select(tree, id=role2.id, mode='Branch'),
                        factor = factor,
                    )
                    mesh = mesh.switch(type3 & node_info.code.equal(CONT3_EXP_IND), fraction)

                # ----- Sigma

                with Layout("Sigma"):

                    exp_ind = Util.sigma(mesh,
                        content = GTree.select(tree, id=role0.id, mode='Branch'),
                        below   = GTree.select(tree, id=role1.id, mode='Branch'),
                        above   = GTree.select(tree, id=role2.id, mode='Branch'),
                        id      = node_id,
                        explore = expl_index,
                        factor  = factor,
                    )
                    mesh = mesh.switch(type3 & node_info.code.equal(CONT3_SIGMA), fraction)

            rep.mesh = mesh

        mesh = rep.mesh

        (ref_mesh + mesh + tree).out()

    # =============================================================================================================================
    # Formula operations

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add

    with GeoNodes("Add", prefix=prefix, is_group=True):

        formula   = Geometry()
        term      = Mesh(None, "Term")

        with Panel("Node"):
            node_type = Integer(0, "Type", hide_value=True)
            code      = Integer(0, "Code", hide_value=True)

        with Panel("Position"):
            node_id = Integer(0, "Node Id")

        mesh = formula.mesh
        tree = formula.point_cloud

        tree = Cloud(GTree.new(tree, id=0, location=0))
        index = tree.index_

        term.faces._Item_ID = tree.id_

        sel_index = nd.index.equal(index)
        tree.points[sel_index]._Type = node_type
        tree.points[sel_index]._Code = code

        mesh += term

        (mesh + tree).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Group n child nodes from last

    with GeoNodes("Group", prefix=prefix, is_group=True):

        formula = Geometry()
        item_id = Integer(0, "Id")
        count   = Integer(1, "Count", 1)

        deco    = Integer(0, "Decoration")
        option1 = Boolean(False, "Option 1")
        option2 = Boolean(False, "Option 2")
        param   = Float(0., "Parameter")

        mesh = formula.mesh
        tree = formula.point_cloud

        children_count = GTree.children_count(tree, id=item_id)
        group_sel = Integer("Owner").equal(item_id) & (Integer("Order") >= children_count - count)

        new_tree = Cloud(GTree.group(tree, selection=group_sel))
        new_id = new_tree.id_
        valid = new_tree.valid_

        info = Util.id_info(new_tree, new_id).node
        index_sel = nd.index.equal(info.index)

        new_tree.points[index_sel]._Type      = TYPE_GROUP
        new_tree.points[index_sel]._Code      = deco
        new_tree.points[index_sel]._Option_1  = option1
        new_tree.points[index_sel]._Option_2  = option2
        new_tree.points[index_sel]._Param     = param

        tree = tree.switch(valid, new_tree)

        (mesh + tree).out()




    # =============================================================================================================================
    # Modifiers


    with GeoNodes("Characters"):

        formula = Geometry()

        chars = Util.characters(link_from='TREE').node

        formula = Util.add(formula, term=chars, type=TYPE_GEO, code=0, link_from='TREE')

        Util.compile(formula).out()



    return














    # =============================================================================================================================
    # Formula builder

    with GeoNodes("Add", prefix=prefix, is_group=True):

        formula = Geometry(name="Formula")
        term    = Mesh(name="Mesh")
        owner   = Integer(0, "Owner")

        mesh = formula.mesh
        tree = formula.point_cloud

        with Layout("Suppress Faces without Item ID"):
            mesh.faces[-Integer("Item ID").exists_].delete()

        with Layout("Create a new node in the tree"):
            tree = GTree.new(tree)
            new_id = tree.index_

            term.faces._Item_ID = new_id

        (mesh + term + tree).out("Formula")
        new_id.out("Id")








    return






    # =============================================================================================================================
    # Formula is made of:
    # - faces with a node id
    # - tree managing the formula structure

    with GeoNodes("Add Item", prefix=prefix, is_group=True):

        formula   = Geometry( None,     "Formula")
        term      = Geometry( None,     "Term")
        target    = Integer( 0,         "Target", single_value=True)
        use_block = Boolean( True,      "Block",  single_value=True)
        link      = Integer( 0,         "Link",   single_value=True)
        use_group = Boolean(False,      "Group",  single_value=True)

        # ----- Make sure the item is a formula

        with Layout("Make sure the new term is a formula"):
            term_mesh = term.mesh
            term_tree = term.point_cloud

            count = term_tree.points.count
            term_tree = term_tree.switch(count.equal(0), GTree.new())

        mesh = formula.mesh
        tree = formula.point_cloud

        # ----- Owner insertion

        with Layout("Owner depends upon the link"):
            target_owner = GTree.index_owner(tree, index=target)

            # 0: After, 1: Exp 2: Indice, 3: Numerator, 4: Denominator 5: Above, 6: Below 7: Before
            owner = Integer.IndexSwitch(target_owner, target, target, target_owner, target_owner, target, target, target_owner, index=link)
            owner = owner.switch(owner < 0, 0)

        # ----- Use Group option

        with Layout("Group option"):
            use_group = Boolean.IndexSwitch(use_group, False, False, use_group, use_group, use_group, use_group, use_group, index=link)
            owner = owner.switch(use_group, target_owner)

        # ----- Add the branch

        with Layout("Insert in the tree formula"):
            tree = Cloud(GTree.new(tree, owner=owner))
            item_id = tree.index_

            tree = Cloud(GTree.join(tree, index=item_id, branch=term_tree))

        with Layout("Change Capture the group"):
            tree = tree.switch(use_group, GTree.change_owner(tree, from_owner=target_owner, to_owner=item_id, selection=nd.index.equal(target)))
            tree = Cloud(tree)

        # ----- Item properties

        with Layout("Inserted items properties"):

            tree.points[item_id]._Target       = target
            tree.points[item_id]._Target_Block = use_block
            tree.points[item_id]._Target_Link  = link

        # ----- Join the mesh

        mesh += term_mesh

        # ----- Done

        (mesh + tree).out()

    # =============================================================================================================================
    # Formula (mesh + tree) management

    # Compilation
    #
    # Type
    # -1: Empty (simple group)
    #  0: Mesh
    #  1: Brackets (bracket like: arrow, braces, sign,...)

    with GeoNodes("Compile", prefix=prefix, is_group=True):

        formula = Geometry()

        mesh = formula.mesh
        tree = formula.point_cloud

        expl = Cloud(GTree.compute_explore())

        count = tree.points.count
        with Repeat(cloud=expl, iterations=count-1) as rep:

            cur_expl = count - 1 - rep.iterations
            index = rep.cloud.points[Integer("Explore").equal(cur_expl)].attribute_statistic(nd.index).min.to_integer()
            sel_index = nd.index.equal(index)

            item_type = tree.points.sample_index(Integer("Type"), index=index)

            with Layout("A Mesh"):
                t = Util.select(tree, id=index, block=False)
                dims = t.node

                t0_min  = dims.vmin
                t0_max  = dims.vmax
                t0_mesh = t







            vmin = dims.vmin
            vmax = dims.vmax

            tree.points[sel_index]._Width  = dims.width
            tree.points[sel_index]._Height = dims.height





    # =============================================================================================================================
    # Independant meshes transformation

    # -----------------------------------------------------------------------------------------------------------------------------
    # Scale Mesh
    #
    # Scale based on bottom left component

    with GeoNodes("Scale", prefix=prefix, is_group=True):

        mesh = Mesh(Geometry())

        sx = Float(1., "x")
        sy = Float(1., "y")

        vmin = mesh.points.attribute_statistic(nd.position).min
        vmax = vmin.max_

        mesh.points.offset = -vmin
        mesh.transform(scale=(sx, sy, 1))
        mesh.points.offset = vmin

        mesh.out()


    # =============================================================================================================================
    # Formula / Tree management


    # -----------------------------------------------------------------------------------------------------------------------------
    # Move a Group

    with GeoNodes("Move"):

        geo       = Geometry()

        dx        = Float(0., "X")
        dy        = Float(0., "Y")
        scale     = Float(1., "Scale")
        space0    = Float(0., "Space Before")
        space1    = Float(0., "Space After")
        use_scale = Boolean(True, "Shrink Space")

        geo = Util.select(geo, link_from='TREE')
        dims = geo.node

        mesh = geo.mesh
        tree = geo.point_cloud

        selection = Boolean("Selected")

        # ----- Scale and offset

        with Layout("Scale and Offset"):
            mesh.points[selection].offset = -dims.v_min
            mesh.points[selection].position = nd.position*scale
            mesh.points[selection].offset = dims.v_min + (dx, dy, 0)

        # ----- Scale and offset

        dw = dims.width*(scale - 1)
        space1 = space1.switch(use_scale, space1 + dw)

        mesh.points[selection | (Integer("Part") >= 0)].offset = (space0, 0, 0)
        mesh.points[(Integer("Part") > 0)].offset = (space1, 0, 0)

        (mesh + tree).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Locate relatively to component

    with GeoNodes("Relative Location", prefix=prefix, is_group=True):

        formula  = Geometry(None, "Formula")
        new_item = Mesh(None, "New Item")

        with Panel("Target"):
            item_id   = Integer(0, "Id")
            use_block = Boolean(True, "Block")
            index     = Integer.MenuSwitch({'After': 0, 'Exponent': 1, 'Indice': 2, 'Numerator': 3, 'Denominator': 4, 'Above': 5, 'Below': 6, 'Before': 7}, name="Location", menu="After")

        formula = Util.select(formula, id=item_id, block=use_block)
        ref_dims = formula.node

        dims = Util.dimensions(new_item).node

        right   = ref_dims.right + X_SPACE
        x_size2 = dims.width * (SCALE_IND/2)
        y_size  = dims.height * SCALE_IND

        x = Float.IndexSwitch(right + X_SPACE, right, right,
            right, right,
            ref_dims.x_mid - x_size2, ref_dims.x_mid - x_size2,
            ref_dims.left,
            index=index)

        y = Float.IndexSwitch(0., ref_dims.over - Y_IND, ref_dims.below,
            Y_ALIGN - dims.below + Y_ABOVE, Y_ALIGN - dims.over - Y_ABOVE,
            ref_dims.over + Y_ABOVE, ref_dims.below - Y_ABOVE - y_size,
            0.,
            index=index)

        s = Float.IndexSwitch(1., SCALE_IND, SCALE_IND,
            1., 1.,
            SCALE_IND, SCALE_IND,
            1.,
            index=index)

        x.out("X")
        y.out("Y")
        Vector((x, y, 0)).out("Translation")
        s.out("Scale")
        index.out("Index")


    return

    # =============================================================================================================================
    # Formula components

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add a new component

    with GeoNodes("Add", prefix=prefix, is_group=True):

        formula  = Geometry(None, "Formula")
        new_item = Mesh(None, "New Item")

        with Panel("Target"):
            item_id   = Integer(0, "Id")
            use_block = Block(True, "Block")

        with Panel("Relation"):
            ref   = Geometry(None, "Relative to")

        loc_node = Util.relative_location(formula, new_item=new_item, id=item_id, block=use_block, link_from='TREE').node

        # ----- Select the target

        formula = Util.select(formula, id=item_id, block=use_block)
        target_dims = formula.node

        # Index comes from the menu
        index = dims.index

        # ----- Item transformation

        item0 = Geometry(new_item).transform(translation=loc_node.translation, scale=loc_node.scale)
        item_dims = Util.dimensions(item0).node

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





        return




















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
