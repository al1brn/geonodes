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
PAR_SCALE    = 1.05  # Parenthesis scale
SIGMA_SCALE  = 1.3   # Sigma scale
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
PLUS_WIDTH = .7

# FRACTION
FRAC_THICK  = DECO_THICK
FRAC_MARGIN = 2*X_SPACE

SQRT = '√'

# ===== Node Types

TYPE_GROUP    = 0 # Group of nodes with decorator
TYPE_GEO      = 1 # Simple geometry
TYPE_FRACTION = 2 # Fraction
TYPE_EXP_IND  = 3 # Exponent / Indice
TYPE_SIGMA    = 4 # Sigma

# ===== DECORATORS

# ----- Symbols
DECO_CAT_SYMBOL       = 0 # Fixed size symbols

DECO_NOTHING            = 0
DECO_SIGN               = 1 # Minus to plus varying with param
DECO_EQUAL              = 2 # Alternative to '=' character

# ----- Special
DECO_CAT_SPECIAL        = 10

DECO_SQRT               = 10

# ----- BLOCK
DECO_CAT_BLOCK          = 20

DECO_PARENTHESIS        = 20
DECO_BRACKETS           = 21
DECO_BRACES             = 22
DECO_ABSOLUTE           = 23
DECO_NORM               = 24
DECO_ANGLE              = 25
DECO_TOKEN              = 26

# ----- Accentuation

DECO_CAT_ACCENTUATION   = 30
DECO_ARROW              = 30
DECO_LEFT_ARROW         = 31
DECO_BAR                = 32
DECO_DOT                = 33
DECO_DOT2               = 34
DECO_DOT3               = 35


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

    # ----- We need tree for organize the formula terms

    formula_tree.build_tree(prefix='Tree')
    GTree = G("Tree")

    # ----- Formula group prefixes:
    # - Char  : Characters (mesh create)
    # - Util  : Utilities (take mesh or tree struct as input)
    # - Build : Low level terms combining (take formula as input)
    # - Formula : Modifiers

    char_prefix  = "Char"
    util_prefix  = "Util"
    build_prefix = "Build"
    term_prefix  = "Term"

    GChar  = G(char_prefix)
    GUtil  = G(util_prefix)
    GBuild = G(build_prefix)
    GTerm  = G(term_prefix)


    # ----- Built in symbols

    create_curve("Util Sqrt Char", formula_data.SQRT_CHAR)
    create_curve("Util Sigma Char", formula_data.SIGMA_CHAR)

    # ----------------------------------------------------------------------------------------------------
    # Macros
    # ----------------------------------------------------------------------------------------------------

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

    def macro_setup_work(mesh, item_id, explore, x_align='LEFT'):
        with Layout("Set up"):

            vmin = mesh.points.attribute_statistic(nd.position).min
            xmax = vmin.max_.x

            x, y, z = vmin.xyz
            if x_align == 'CENTER':
                mesh.transform(translation=(-(x + xmax)/2, 0, -z))
            elif x_align == 'RIGHT':
                mesh.transform(translation=(-x - xmax, 0, -z))
            else:
                mesh.transform(translation=(-x, 0, -z))

            mesh.faces._Reference = False

            mesh.faces.material = "Formula"
            mesh.faces._ID = item_id
            mesh.faces._Explore = explore

            return mesh

    def macro_create_work(ref, item_id, explore):
        with Layout("Create Work faces from reference"):

            mesh = Mesh(ref).faces[Integer("ID").equal(item_id)].separate()

            mesh = Mesh(mesh)
            vmin = -mesh.points.attribute_statistic(nd.position).min
            x, y, z = vmin.xyz
            mesh.transform(translation=(x, 0, z))

            mesh.faces._Reference = False

            mesh.faces.material = "Formula"
            mesh.faces._ID      = item_id
            mesh.faces._Explore = explore

            return mesh

    def macro_init_node(tree, selection, node_type, code, argument=0, factor=1., color=(0, 0, 0), fade=0, role=0, option_1=False, option_2=False, param=0.):

        with Layout("Setup tree node"):
            tree.points[selection]._Type      = Integer(node_type)
            tree.points[selection]._Code      = Integer(code)
            tree.points[selection]._Argument  = Integer(argument)
            tree.points[selection]._Factor    = Float(factor)
            tree.points[selection]._Color     = Color(color)
            tree.points[selection]._Fade      = Integer(fade)
            tree.points[selection]._Role      = Integer(role)
            tree.points[selection]._Option_1  = Boolean(option_1)
            tree.points[selection]._Option_2  = Boolean(option_2)
            tree.points[selection]._Param     = Float(param)

            return tree

    # =============================================================================================================================
    # Dimensions

    with GeoNodes("Dimensions", prefix=util_prefix, is_group=True):
        """ Compute dimensions of a selection in the mesh

        Arguments
        ---------
        - Mesh (Mesh): input geometry
        - Selection (Boolean) : Selection on mesh

        Returns (meaning is obvious !)
        ------------------------------
        - Min : Vector
        - Max : Vector
        - Width : Float
        - Height : Float
        - X Min : Float
        - X Max : Float
        - X Mid : Float
        - X Max : Float
        """

        mesh = Mesh(None, "Mesh")
        selection = Boolean(True, "Selection", hide_value=True)

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

    with GeoNodes("LaTeX Codes", prefix=char_prefix, is_group=True):
        """ Replace LaTeX code '\key_word' by its unicode value

        For instance : \exists -> '∃'

        Arguments
        ---------
        - String (String) : input string

        Returns
        -------
        - String : string where LaTeX codes are replaced
        """

        s = String(None, "String")

        keys = sorted(formula_data.SYMBOLS.keys(), key= lambda x: 100 - len(x))

        for code in keys:
            c = formula_data.SYMBOLS[code]
            s = s.replace("\\" + code, c)

        s.out()

    # =============================================================================================================================
    # =============================================================================================================================
    # Characters builder
    # =============================================================================================================================
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Characters

    with GeoNodes("Characters", prefix=char_prefix, is_group=True):
        """ Create a reference mesh from a string.

        > [!NOTE]
        > - LaTeX codes are accepted and replaced by there unicode value.
        > - The created meshes id left aligned
        > - The node also returns the dimensions of the created mesh using the
        >   output sockets of "Util Dimensions"

        Arguments
        ---------
        - Chars (String) : the input string
        - Italic (Boolean) : use italic font
        - Bold (Boolean) : use bold font

        Returns
        -------
        - Mesh : the reference mesh
        - Output sockets of "Util Dimensions"
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        s      = String(None,   "Chars")
        italic = Boolean(False, "Italic", single_value=True)
        bold   = Boolean(False, "Bold", single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        s = GChar.latex_codes(s)

        reg = String(s).to_curves(size=FONT_SIZE, font=FONTS.regular)
        itl = String(s).to_curves(size=FONT_SIZE, font=FONTS.italic)
        bld = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold)
        bit = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold_italic)

        curves = reg.switch(bold, bld).switch(italic, itl.switch(bold, bit))

        curves = Curve(curves.realize())

        chars = curves.fill_ngons()
        dims = GUtil.dimensions(chars).node

        chars = macro_setup_ref(chars, ref_type=TYPE_GEO)

        chars.out("Mesh")
        dims.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Shape
    # 0: Rect, 1: Circle, 2: Triangle

    with GeoNodes("Shape", prefix=char_prefix, is_group=True):
        """ Create a reference mesh from a shape code

        Valid shape codes are:
        - 0 : Rectangle
        - 1 : Circle / Ellipse
        - 2 : Triangle

        > [!NOTE]
        > - The created mesh is left aligned
        > - The node also returns the dimensions of the created mesh using the
        >   output sockets of "Util Dimensions"

        Arguments
        ---------
        - Code (Integer) : shape code
        - Width (Float) : shape width
        - Height (Float) : shape height
        - Tracking (Float) : tracking value (length below 0)

        Returns
        -------
        - Mesh : the reference mesh
        - Output sockets of "Util Dimensions"
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        index    = Integer(0, "Code", single_value=True)
        width    = Float(1, "Width")
        height   = Float(1, "Height")
        tracking = Float(.1, "Tracking")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with If(Mesh, index) as shape:
            shape.option = Mesh.Grid(width, height, 2, 2)

        with Elif(shape):
            shape.option = Mesh.Circle().transform(scale=(width, height, 1))

        with Elif(shape):
            shape.option = Mesh.Circle(vertices=3).transform(scale=(width, height, 1))

        vmin = shape.points.attribute_statistic(nd.position).min
        x, y, _ = vmin.xyz

        shape.transform(translation=(-x, -y - tracking, 0))
        dims = GUtil.dimensions(shape).node

        shape = macro_setup_ref(shape, ref_type=TYPE_GEO)

        shape.out("Mesh")
        dims.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Math operators

    with GeoNodes("Symbol", prefix=char_prefix, is_group=True):
        """ Create a reference mesh from an operator code

        Valid operator codes are:
        - DECO_NOTHING)  : Nothing
        - DECO_SIGN      : Minus to Plus varying char, base on Parameter
        - DECO_EQUAL     : Equal sign (alterntive to '=' sign)

        > [!NOTE]
        > - The created mesh is left aligned
        > - The node also returns the dimensions of the created mesh using the
        >   output sockets of "Util Dimensions"

        Arguments
        ---------
        - Code (Integer) : operator code
        - Parameter (Float) : Factor for varying meshes

        Returns
        -------
        - Mesh : the reference mesh
        - Output sockets of "Util Dimensions"
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        code  = Integer(1, "Code")
        param = Float.Factor(1, "Parameter", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Plus / Minus"):

            hrz = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_WIDTH, size_y=PLUS_THICK)
            vrt = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_THICK, size_y=PLUS_WIDTH*param)

            op = Mesh.Switch(code.equal(DECO_SIGN), None, hrz + vrt)

        with Layout("Equal"):

            op = op.switch(code.equal(DECO_EQUAL),
                    Mesh(hrz).transform(translation=(0,  Y_SPACE, 0)) +
                    Mesh(hrz).transform(translation=(0, -Y_SPACE, 0)))

        op.transform(translation=(0, Y_ALIGN, 0))

        dims = GUtil.dimensions(op).node
        op = macro_setup_ref(op, ref_type=TYPE_GEO)

        op.out("Mesh")
        dims.out()

    # =============================================================================================================================
    # =============================================================================================================================
    # DECORATORS
    #
    # Decorators are dynamically built meshes.
    # The decorators are located relatively formula terms: sqrt, sign, arrows
    # =============================================================================================================================
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Insert a decorator

    with GeoNodes("Add Decorator", prefix=util_prefix, is_group=True):
        """ Add a decorator to a mesh

        The decoratoir must have been computed to take place into the formula.
        adding the mesh generally requires to move the termes it refers to.

        The adding process is the following:
        - shifting the target terms
        - adding the decorator

        This process is controlled by a factor to animated the decoration process.

        > [!NOTE]
        > If 'Apply' argument is False, the mesh is returned unchanged. This allows
        > to use this group to add optional decorator, typically with the following
        > piece of code:

        ``` python
        mesh = Mesh(None, "Mesh") # Getting the current mesh
        deco = my_decorator(mesh, ...) # Build a decorator on the mesh
        mesh = GUtil.add_decorator(mesh, decorator=deco, apply=my_code.equal(DECO_CODE))
        ```

        Arguments
        ---------
        - Mesh : mesh being built
        - Content (Boolean) : selection on the mesh where to locate the decorator
        - Apply (Boolean) : apply the decoration if True, keep unchange otherwise
        - Decorator (Mesh) : the decorator to add
        - Left Shift (Float) : horizontal translation of the mesh content
        - Vertical Shift (Float) : vertical translation of the mesh content
        - Factor (Float in [0, 1]) : apply effect

        Returns
        -------
        - Mesh : the decorated mesh
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh    = Mesh(None, "Mesh")
        content = Boolean(False, "Content", hide_value=True)
        apply   = Boolean(True, "Apply")

        deco       = Mesh(None, "Decorator")
        left_shift = Float(0., "Left Shift")
        vert_shift = Float(0., "Vertical Shift")
        factor     = Float.Factor(1, "Factor", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        xmin = deco.points.attribute_statistic(nd.position.x).min
        xmax = xmin.max_

        deco = deco.transform(translation=(-xmin, 0, 0)).transform(scale=(factor, 1, 1)).transform(translation=(xmin, 0, 0))
        deco = deco.switch(factor.equal(0))
        shifted_mesh = Mesh(mesh)
        shifted_mesh.points[content].offset = (factor*left_shift, factor*vert_shift, 0)

        mesh.switch(apply, shifted_mesh + deco).out("Mesh")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create a decorator

    with GeoNodes("Decorator", prefix=util_prefix, is_group=True):
        """ Build a decorator onto a formula mesh.

        The decorator is sized and located on the provided Selection on the mesh.

        The decorator codes are organized in categories.

        Symbol category (DECO_CAT_SYMBOL):
        - DECO_NOTHING : no decoration
        - DECO_SIGN : minus to plus sign
        - DECO_EQUAL : alternative to '=' character

        Special category (DECO_CAT_SPECIAL):
        - DECO_SQRT : square root

        Block category (DECO_CAT_BLOCK):
        - DECO_PARENTHESIS : ( ... )
        - DECO_BRACKETS : [ ... ]
        - DECO_BRACES : { ... }
        - DECO_ABSOLUTE : | ... |
        - DECO_NORM : ‖ ... ‖
        - DECO_ANGLE : ⟨ ... ⟩
        - DECO_TOKEN : < ... >

        Accentuation category (DECO_CAT_ACCENTUATION):
        - DECO_ARROW : right arrow
        - DECO_LEFT_ARROW : left arrow
        - DECO_BAR : bar
        - DECO_DOT : dot
        - DECO_DOT2 : double dot
        - DECO_DOT3 : triple dot

        > [!NOTE]
        > Two options ('Option 1' and 'Option 2') can be set to control the decorator appearance.
        > For accentuation codes, 'Option 1' draws the symbol below the target rather than above.
        > For brackets codes, the two options control whether to hide the opening and closing symbols.
        > If both are True, no bracket is drawn.

        Arguments
        ---------
        - Mesh
        - Content (Boolean) : where to locate the decorator within the mesh
        - Id (Integer) : Node ID of the decorator mesh
        - Explore (Integer) : Explore index of the decorator mesh
        - Factor (Float in [0, 1]) : decorator animation factor
        - Code (Integer) : decorator code
        - Option 1 (Boolean) : option 1
        - Option 2 (Boolean) : option 2
        - Param (Float) : decorator param

        Returns
        -------
        - Mesh : decorated mesh
        """

        unit = DECO_THICK

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh    = Mesh(None, "Mesh")
        content = Boolean(False, "Content", hide_value=True)

        item_id = Integer(1,      "Id", 1)
        explore = Integer(1,      "Explore", 1)
        factor  = Float.Factor(1, "Factor", 0, 1)

        code    = Integer(0,     "Code")
        option1 = Boolean(False, "Option 1")
        option2 = Boolean(False, "Option 2")
        param   = Float(0.,      "Param")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # ----- Dimensions

        dims = GUtil.dimensions(mesh, content).node

        # ====================================================================================================
        # SYMBOL
        # ====================================================================================================

        with Layout("Symbol"):

            is_operator = (code >= DECO_CAT_SYMBOL) & (code < (DECO_CAT_SYMBOL + 10))

            op_node = GChar.symbol(code=code, parameter=param).node
            op = macro_setup_work(op_node.mesh, item_id, explore)

            mesh = GUtil.add_decorator(mesh, content, is_operator, decorator=op, left_shift=op_node.width + X_SPACE, factor=factor)

        # ====================================================================================================
        # Special
        # ====================================================================================================

        # -----------------------------------------------------------------------------------------------------------------------------
        # Square Root

        with Layout("Special"):

            #is_special = (code >= DECO_CAT_SPECIAL) & (code < (DECO_CAT_SPECIAL + 10))

            sqrt = GUtil.sqrt_char(fill=False)
            sqrt_dims = GUtil.dimensions(sqrt).node

            with Layout("Scale to fit with content"):

                scale = PAR_SCALE*gnmath.max(1, dims.height)

                x_content = sqrt_dims.width*scale

                sqrt = sqrt.transform(translation=(0, dims.y_mid - scale*sqrt_dims.y_mid, 0), scale=scale)

                sqrt = Curve(sqrt)
                count = sqrt.points.count
                sqrt.points[count-3, count-2].offset = (dims.width*1.1, 0, 0)

            sqrt = sqrt.fill_ngons()
            sqrt = macro_setup_work(sqrt, item_id, explore)

            mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_SQRT), decorator=sqrt, left_shift=x_content, factor=factor)

        # ====================================================================================================
        # Accentuation : arrows, dots, bar
        # ====================================================================================================

        with Layout("Accentuation: arrow, bar, dot"):

            #is_accentuation = (code >= DECO_CAT_ACCENTUATION) & (code < (DECO_CAT_ACCENTUATION + 10))

            y = (dims.y_max + Y_ABOVE).switch(option1, dims.y_min - Y_ABOVE)

            with Layout("Bar and Arrow dims"):
                left_margin  = 2*unit
                right_margin = 4*unit
                bar_width = (dims.width + left_margin + right_margin)._lc("Bar Width")
                bar_width2 = (bar_width/2)._lc("Bar Width / 2")

            with Layout("Dot Char"):
                dot_node = GChar.characters(chars='.').node
                dot = Mesh(dot_node._out)
                dot = macro_setup_work(dot, item_id, explore, x_align='CENTER')

                dot.transform(translation=(dims.x_mid + dot_node.width, y - dot_node.height/2, 0))
                dot_dx = (dot_node.width + X_SPACE/2)/2

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

                mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_ARROW), decorator=r, left_shift=left_margin, factor=factor)

            with Layout("Left Arrow"):

                r.transform(translation=(-bar_width2, 0, 0))
                r.transform(scale=(-1, 1, 1))
                r.transform(translation=(bar_width2, 0, 0))
                r.flip_faces()

                mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_LEFT_ARROW), decorator=r, left_shift=left_margin, factor=factor)

            with Layout("Bar"):

                r = Mesh.Grid(bar_width, DECO_THICK, 2, 2).transform(translation=(bar_width2, y, 0))
                r = macro_setup_work(r, item_id, explore)

                mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_BAR), decorator=r, left_shift=left_margin, factor=factor)

            with Layout("Dots"):

                is_dot  = code.equal(DECO_DOT)
                is_dot2 = code.equal(DECO_DOT2)
                is_dot3 = code.equal(DECO_DOT3)

                dot2 = Mesh(dot).transform(translation=( -dot_dx, 0, 0))  + Mesh(dot ).transform(translation=(dot_dx, 0, 0))
                dot3 = Mesh(dot).transform(translation=(-2*dot_dx, 0, 0)) + Mesh(dot2).transform(translation=(dot_dx, 0, 0))

                r = dot.switch(is_dot2, dot2).switch(is_dot3, dot3)

                mesh = GUtil.add_decorator(mesh, content, is_dot | is_dot2 | is_dot3, decorator=r, left_shift=left_margin, factor=factor)

        # ====================================================================================================
        # Block
        # ====================================================================================================

        with Layout("Block : parenthesis, brackets, ..."):

            with Layout("A valid code"):
                block_code = code - DECO_CAT_BLOCK
                is_block = (block_code >= 0) & (block_code < DECO_TOKEN)
                block_code = block_code.switch_false(is_block, 0)._lc("Block Code")

                use_left  = -option1
                use_right = -option2

            # ---------------------------------------------------------------------------
            # Brackets instantiation
            # BRACKETS = ['()', '[]', '||', '{}', '‖‖', '⟨⟩', '<>']

            for i in range(2):

                with Layout("Open Char" if i == 0 else "Close Char"):

                    if i == 0:
                        s = String.IndexSwitch('(', '[', '|', '{', '‖', '⟨', '<', index=block_code)
                    else:
                        s = String.IndexSwitch(')', ']', '|', '}', '‖', '⟩', '>', index=block_code)

                    br_node = GChar.characters(chars=s).node
                    br = br_node.mesh
                    br = macro_setup_work(br,  item_id, explore)

                    br_scale = PAR_SCALE*gnmath.max(1, dims.height)

                    br.transform(translation=(0, -br_node.y_mid, 0))
                    br.transform(scale=(1, br_scale, 1))
                    br.transform(translation=(0, dims.y_mid, 0))

                    if i== 0:
                        br_open = br
                    else:
                        br_close = br

            with Layout("Opening bracket"):

                b_dims = GUtil.dimensions(br_open).node
                mesh = GUtil.add_decorator(mesh, content, use_left & is_block, decorator=br_open, left_shift=b_dims.width + X_SPACE/3, factor=factor)

            with Layout("Closing bracket"):

                new_dims = GUtil.dimensions(mesh, content).node
                br_close.transform(translation=(new_dims.x_max + X_SPACE/3, 0, 0))

                mesh = GUtil.add_decorator(mesh, content, use_right & is_block, decorator=br_close, left_shift=0., factor=factor)

        mesh.out("Mesh")

    # =============================================================================================================================
    # TWO CONTENTS

    # -----------------------------------------------------------------------------------------------------------------------------
    # Fraction

    with GeoNodes("Fraction", prefix=util_prefix, is_group=True):
        """ Organize two terms as a fraction.

        Arguments
        ---------
        - Mesh
        - Numerator (Boolean) : selection of numerator terms
        - Denominator (Boolean) : selection of denominator terms
        - Id (Integer) : Node ID of the fraction bar mesh
        - Explore (Integer) : Explore index of the decorator mesh
        - Factor (Float in [0, 1]) : animation factor

        Returns
        -------
        - Mesh : mesh where the two termes are organized as a fraction
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = Mesh(None, "Mesh")

        num_sel = Boolean(False, "Numerator",   hide_value=True)
        den_sel = Boolean(False, "Denominator", hide_value=True)

        item_id = Integer(1, "Id", 1)
        explore = Integer(1, "Explore", 1)
        factor  = Float.Factor(1, "Factor", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        ndims = GUtil.dimensions(mesh, num_sel).node
        ddims = GUtil.dimensions(mesh, den_sel).node

        with Layout("Build the bar"):

            width = gnmath.max(ndims.width, ddims.width) + 2*FRAC_MARGIN
            x_center = width/2
            bar = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=width, size_y=FRAC_THICK).transform(translation=(x_center, Y_ALIGN, 0))

            bar = macro_setup_work(bar, item_id, explore)

        with Layout("Locate numerator and denominator"):

            n_left_shift = x_center - ndims.x_mid
            d_left_shift = x_center - ddims.x_mid

            n_vert_shift = Y_ALIGN + FRAC_THICK + Y_SPACE - ndims.y_min
            d_vert_shift = Y_ALIGN - FRAC_THICK - Y_SPACE - ddims.y_max

            mesh = GUtil.add_decorator(mesh, num_sel, decorator=bar, left_shift=n_left_shift, vertical_shift=n_vert_shift, factor=factor)

            # Denominator disappears with animation

            mesh.points[den_sel].offset = (-ddims.x_mid, -ddims.y_mid, 0)
            mesh.points[den_sel].position *= factor
            mesh.points[den_sel].offset = (d_left_shift*factor + ddims.x_mid, d_vert_shift + ddims.y_mid, 0)

            #mesh = GUtil.add_decorator(mesh, den_sel,                left_shift=d_left_shift, vertical_shift=d_vert_shift, factor=factor)

        mesh.out("Mesh")

    # =============================================================================================================================
    # THREE CONTENTS

    # -----------------------------------------------------------------------------------------------------------------------------
    # Exponent & Indice

    with GeoNodes("Exponent Indice", prefix=util_prefix, is_group=True):
        """ Organize three terms as a term with an indice and an exponent.

        Arguments
        ---------
        - Mesh
        - Content (Boolean) : selection of content terms
        - Exponent (Boolean) : selection of exponent terms
        - Indice (Boolean) : selection of indice terms
        - Factor (Float in [0, 1]) : decorator animation factor

        Returns
        -------
        - Mesh : mesh where the three termes are organized as expected
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = Mesh()

        content  = Boolean(False, "Content",   hide_value=True)
        exponent = Boolean(False, "Exponent",  hide_value=True)
        indice   = Boolean(False, "Indice",    hide_value=True)

        factor  = Float.Factor(1, "Factor", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # ----- Dimensions

        cdims = GUtil.dimensions(mesh, content).node
        edims = GUtil.dimensions(mesh, exponent).node
        idims = GUtil.dimensions(mesh, indice).node

        with Layout("Scale Exponent and Indice"):
            mesh.points[exponent].position *= (SCALE_IND*factor, SCALE_IND, SCALE_IND)
            mesh.points[indice].position *= (SCALE_IND*factor, SCALE_IND, SCALE_IND)

        with Layout("Offset Exponent and Indice"):
            left = cdims.x_max + X_SPACE/3

            mesh.points[exponent].offset = (left, cdims.y_min + .8*cdims.height, 0)
            mesh.points[indice].offset   = (left, cdims.y_min - .1*cdims.height, 0)

        mesh.out("Mesh")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sigma

    with GeoNodes("Sigma", prefix=util_prefix, is_group=True):
        """ Organize three terms as a term with an indice and an exponent.

        Arguments
        ---------
        - Mesh
        - Content (Boolean) : selection of content terms
        - Below (Boolean) : selection of terms above sigma sign
        - Above (Boolean) : selection of terms above sigma sign
        - Id (Integer) : Node ID of the sigma mesh
        - Explore (Integer) : Explore index of the sigma mesh
        - Factor (Float in [0, 1]) : decorator animation factor

        Returns
        -------
        - Mesh : mesh where the three termes are organized as expected
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = Mesh()

        content  = Boolean(False, "Content", hide_value=True)
        below    = Boolean(False, "Below",   hide_value=True)
        above    = Boolean(False, "Above",   hide_value=True)

        item_id = Integer(1, "Id", 1)
        explore = Integer(1, "Explore", 1)
        factor  = Float.Factor(1, "Factor", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Scale Below and Above"):
            mesh.points[below].position *= SCALE_IND
            mesh.points[above].position *= SCALE_IND

        # ----- Dimensions

        cdims = GUtil.dimensions(mesh, content).node
        bdims = GUtil.dimensions(mesh, below).node
        adims = GUtil.dimensions(mesh, above).node

        # ----- Sigma Symbol

        with Layout("Sigma Symbol"):

            # ----- Base
            sigma = Mesh(GUtil.sigma_char(fill=True))

            # ----- Height
            sigma_height = SIGMA_SCALE*gnmath.min(1, cdims.height)
            sigma.transform(scale=(1, sigma_height, 1))

            # ----- Vertical center with content
            sigma.transform(translation=(0, cdims.y_mid - sigma_height/2, 0))

            # ----- Add to the mesh
            sigma = macro_setup_work(sigma, item_id, explore)
            mesh += sigma

            # ----- Get the final dims
            sdims = GUtil.dimensions(mesh, Integer("ID").equal(item_id)).node

        with Layout("Locate content"):
            mesh.points[content].offset = (sdims.x_max + X_SPACE/3, 0, 0)

        with Layout("Locate Below and Above"):
            mesh.points[below].offset = (sdims.x_mid - bdims.x_mid, sdims.y_min - Y_SPACE - bdims.y_max , 0)
            mesh.points[above].offset = (sdims.x_mid - adims.x_mid, sdims.y_max + Y_SPACE - bdims.y_min , 0)

        mesh.out()

    # =============================================================================================================================
    # =============================================================================================================================
    # Formula Compilation
    # =============================================================================================================================
    # =============================================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Reading tree structure

    with GeoNodes("Index Info", prefix=util_prefix, is_group=True):
        """ Read the node info by index.

        Arguments
        ---------
        - Tree (Cloud) : the tree structure
        - Index (Integer) : an index on the tree structure

        Returns
        -------
        - Default node info (index, ID, Owner, Depth, Order, Total, Explore)
        - Type (Integer)
        - Code (Integer)
        - Argument (Integer)
        - Factor (Float)
        - Color (Color)
        - Fade (Float)
        - Role (Integer)
        - Option 1 (Boolean)
        - Option 2 (Boolean)
        - Param (Float)
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        tree = Cloud(None, "Tree")
        index = Integer(0, "Index")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

    with GeoNodes("Id Info", prefix=util_prefix, is_group=True):
        """ Read the node info by ID.

        Arguments
        ---------
        - Tree (Cloud) : the tree structure
        - Id (Integer) : an ID on the tree structure

        Returns
        -------
        - see "Util Index Info"
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        tree    = Cloud(None, "Tree")
        node_id = Integer(1,  "Id")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        GUtil.index_info(tree, index=GTree.id_info(tree, id=node_id)).node.out()

    with GeoNodes("Explore Info", prefix=util_prefix, is_group=True):
        """ Read the node info by Explore index.

        Arguments
        ---------
        - Tree (Cloud) : the tree structure
        - Explore (Integer) : an Explore index on the tree structure

        Returns
        -------
        - see "Util Index Info"
        """
        tree    = Cloud(None, "Tree")
        explore = Integer(1,  "Explore")

        GUtil.index_info(tree, index=GTree.explore_info(tree, explore=explore)).node.out()

    # ----------------------------------------------------------------------------------------------------
    # Formula compilation

    with GeoNodes("Compile", prefix=build_prefix, is_group=True):
        """ Compile the formula

        Formula compilation is made with following steps:
        - Separate Tree Structure (cloud of point) form the mesh
        - Delete work faces from the messh to keep the "Reference faces"
        - The a loop is performed from en empyty meh to build the final formula.
          The building loop is made from last node to tree root.
          for each node, a mesh is built depending on the node 'Type':
          - TYPE_GROUP    : chain the child meshes in their order and then add ad decorator
          - TYPE_GEO      : copy the reference mesh into the mesh
          - TYPE_FRACTION : Fraction between the two child nodes
          - TYPE_EXP_IND  : Use the three child nodes as content, exponent and indice
          - TYPE_SIGMA    : Use the three child nodes as content, below and above sigma sum

        Arguments
        ---------
        - Formula (Mesh + Cloud) : the formula to compile

        Returns
        -------
        - Formula (Mesh + Cloud)
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry(name="Formula")

        with Panel("Compile"):
            use_compile = Boolean(True, "Compile", tip="Disable but last term if performance issues are encountered")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        ref_mesh, _ = macro_get_ref(formula.mesh)

        tree = formula.point_cloud

        # ----- Let's explore the tree from last to start

        count = tree.points.count
        with Repeat(mesh=None, iterations=count) as rep:

            mesh = rep.mesh

            with Layout("Last to first Explore index info"):
                expl_index = count - 1 - rep.iteration
                node_info  = GUtil.explore_info(tree, explore=expl_index).node
                node_id    = node_info.id._lc("Node ID")

            # ====================================================================================================
            # GEO : Instantiate from reference
            # ====================================================================================================

            with Layout("GEO: Instantiate from reference"):

                geo = macro_create_work(ref_mesh, node_id, expl_index)

                # DEBUG
                if False:
                    dbg_dims = GUtil.dimensions(geo).node
                    geo = Mesh.Grid(dbg_dims.width, dbg_dims.height, 2, 2).transform(translation=(dbg_dims.width/2, 0, 0))
                    geo = macro_setup_work(geo, node_id, expl_index)

                mesh = mesh.switch(node_info.type.equal(TYPE_GEO), mesh + geo)

            # ====================================================================================================
            # GROUP : Children concatenation
            # ====================================================================================================

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

                deco = GUtil.decorator(mesh=mesh,
                    content  = GTree.select(tree, id=node_id, mode='Children'),
                    id       = node_id,
                    explore  = expl_index,
                    factor   = node_info.factor,

                    code     = node_info.code,
                    option_1 = node_info.option_1,
                    option_2 = node_info.option_2,
                    param    = node_info.param,
                )

                mesh = mesh.switch(node_info.type.equal(TYPE_GROUP), deco)

            # ====================================================================================================
            # FRACTION
            # ====================================================================================================

            with Layout("Two contents"):
                role0 = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(0)).node
                role1 = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(1)).node

            with Layout("Fraction"):
                fraction = GUtil.fraction(mesh,
                    numerator   = GTree.select(tree, id=role0.id, mode='Branch'),
                    denominator = GTree.select(tree, id=role1.id, mode='Branch'),
                    id      = node_id,
                    explore = expl_index,
                    factor  = node_info.factor,
                )
                mesh = mesh.switch(node_info.type.equal(TYPE_FRACTION), fraction)

            # ----------------------------------------------------------------------------------------------------
            # THREE CONTENTS
            # ----------------------------------------------------------------------------------------------------

            with Layout("Thre Contents"):

                role0 = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(0)).node
                role1 = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(1)).node
                role2 = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(2)).node

            # ----- Exponent / indice

            with Layout("Exponent / Indice"):

                exp_ind = GUtil.exponent_indice(mesh,
                    content  = GTree.select(tree, id=role0.id, mode='Branch'),
                    exponent = GTree.select(tree, id=role1.id, mode='Branch'),
                    indice   = GTree.select(tree, id=role2.id, mode='Branch'),
                    factor = node_info.factor,
                )
                mesh = mesh.switch(node_info.type.equal(TYPE_EXP_IND), exp_ind)

            # ----- Sigma

            with Layout("Sigma"):

                sigma = GUtil.sigma(mesh,
                    content = GTree.select(tree, id=role0.id, mode='Branch'),
                    below   = GTree.select(tree, id=role1.id, mode='Branch'),
                    above   = GTree.select(tree, id=role2.id, mode='Branch'),
                    id      = node_id,
                    explore = expl_index,
                    factor  = node_info.factor,
                )
                mesh = mesh.switch(node_info.type.equal(TYPE_SIGMA), sigma)

            rep.mesh = mesh

        mesh = rep.mesh

        formula.switch(use_compile, ref_mesh + mesh + tree).out("Formula")

    # =============================================================================================================================
    # =============================================================================================================================
    # Formula building
    # =============================================================================================================================
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add

    with GeoNodes("Add", prefix=build_prefix, is_group=True):
        """ Add a term into a formula.

        > [!NOTE]
        > The term is added as last child of the passed 'Id'.

        > [!CAUTION]
        > The mesh term must be a 'Reference' Mesh, i.e. with Faces Boolean
        > named attribute 'Reference' set to True.

        The adding process creates a new entry in the tree structure.
        The initialization just takes the node Type and Code parameters.
        The created id is set to the term Mesh.

        The algorithm is the following:
        1. Create a new node in the structure:
           - location : last child i-of the passed 'Id' argument
           - type : initialized with Type argument
           - code : initialized with code argument
        2. Set the created ID as term Faces 'ID' attribute
        3. Join the mesh and the term

        Arguments
        ---------
        - Formula (Mesh + Cloud)
        - Term (Mesh) : The mesh to add
        - Owner Id : owner ID where to crate the new node
        - Type (Integer) : node type
        - Code (Integer) : node code
        - Role (Integer) : node role

        Returns
        -------
        - Formula
        """
        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula   = Geometry(None, "Formula")
        term      = Mesh(None, "Term")

        owner_id  = Integer(0, "Owner Id")
        node_type = Integer(0, "Type", hide_value=True)
        code      = Integer(0, "Code", hide_value=True)
        role      = Integer(0, "Role", hide_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        tree = Cloud(GTree.new(tree, id=owner_id, location=0))
        index = tree.index_

        term.faces._ID = tree.id_

        sel_index = nd.index.equal(index)
        tree.points[sel_index]._Type = node_type
        tree.points[sel_index]._Code = code
        tree.points[sel_index]._Role = role

        mesh += term

        (mesh + tree).out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Group n child nodes from last

    with GeoNodes("Group", prefix=build_prefix, is_group=True):
        """ Group terms in a new node.

        The last child nodes are grouped under their common owner.

        The adding process creates a new entry in the tree structure.

        The algorithm is the following:
        1. Create a new node in the structure:
           - location : last child i-of the passed 'Id' argument
           - type : initialized with Type argument
           - code : initialized with code argument
        2. Set the created ID as term Faces 'ID' attribute
        3. Join the mesh and the term

        Arguments
        ---------
        - Formula (Mesh + Cloud)
        - Owner Id (Integer) : owner of the nodes to group
        - Count (Integer) : number of nodes to group, i.e. the last count child nodes of the owner
        - Type (Integer) : Type
        - Factor (Float in [0, 1]) : animation factor
        - Decoration > Code (Integer) : decoration code
        - Decoration > Option 1 (Boolean) : option 1
        - Decoration > Option 2 (Boolean) : option 2
        - Decoration > Parameter (Float) : decoration parameter

        Returns
        -------
        - Formula
        - Id (Integer) : created group id
        - Valid (Boolean) : creation is successful
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula   = Geometry(None, "Formula")
        item_id   = Integer(0, "Owner Id")
        count     = Integer(1, "Count", 1)
        node_type = Integer(TYPE_GROUP, "Type")
        factor    = Float.Factor(1, "Factor", 0, 1)


        with Panel("Decoration"):
            deco    = Integer(0, "Code")
            option1 = Boolean(False, "Option 1")
            option2 = Boolean(False, "Option 2")
            param   = Float(0., "Parameter")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        children_count = GTree.children_count(tree, id=item_id)
        group_sel = (Integer("Owner").equal(item_id)) & ((Integer("Order") >= children_count - count))

        new_tree = Cloud(GTree.group(tree, selection=group_sel))
        new_id = new_tree.id_
        valid = new_tree.valid_

        new_tree = macro_init_node(new_tree, valid & Integer("ID").equal(new_id),
            node_type = node_type,
            code      = deco,
            factor    = factor,
            option_1  = option1,
            option_2  = option2,
            param     = param,
        )

        tree = tree.switch(valid, new_tree)

        (mesh + tree).out("Formula")
        new_id.out("Id")
        valid.out("Valid")

    # =============================================================================================================================
    # =============================================================================================================================
    # Modifiers
    # =============================================================================================================================
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Debug

    with GeoNodes("Show Terms", prefix=term_prefix):
        """ Debugging group

        This group splits the formula into its terms

        Arguments
        ---------
        - Formula
        - Tree Structure (Boolean) : Show tree structure
        - Show (Boolean) : split is active

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry(None, "Formula")
        use_tree = Boolean(False, "Tree Structure")
        show = Boolean(True, "Show")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        count = tree.points.count
        with Repeat(terms=None, y=0., iterations=count) as rep:

            explore = rep.iteration
            info = GTree.explore_info(tree, explore=explore).node

            item_id = info.id
            s = item_id.to_string() + " (" + info.owner.to_string() + ")"
            label = Curve(s.to_curves(size=1).realize()).fill_ngons()
            lab_dims = GUtil.dimensions(label).node

            term = Mesh(mesh).faces[GTree.select(tree, id=info.id)].separate()
            dims = GUtil.dimensions(term).node

            label.transform(translation=(0, rep.y - dims.y_mid - lab_dims.y_mid, 0))
            term.transform(translation=(4,  rep.y - dims.y_max, 0))

            rep.terms += label + term
            rep.y -= dims.height + 1

        debug = rep.terms

        tree = formula.point_cloud
        debug = debug.switch(use_tree, GTree.dump(tree))

        formula.switch(show, debug).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Characters

    with GeoNodes("Characters", prefix=term_prefix):
        """ Characters

        Arguments
        ---------
        - Formula
        - Chars (String) : the input string
        - Italic (Boolean) : use italic font
        - Bold (Boolean) : use bold font

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry(None, "Formula")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        chars = GChar.characters(link_from='TREE')

        formula = GBuild.add(formula, term=chars, owner_id=0, type=TYPE_GEO)

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Symbol

    with GeoNodes("Symbol", prefix=term_prefix):
        """ Add a symbol

        Arguments
        ---------
        - Formula
        - Symbol (Menu) : symbol selection
        - Plus Factor (Boolean) : Minus to plus transformation

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula  = Geometry(None, "Formula")
        what     = Integer.MenuSwitch({'Minus': 0, 'Plus': 1, 'Equal': 2, 'Minus to Plus': 3}, name='Symbol')
        sign_fac = Float.Factor(1, "Plus Factor", 0, 1, tip="Minus to plus factor")
        #factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        code  = Integer.IndexSwitch(DECO_SIGN, DECO_SIGN, DECO_EQUAL, DECO_SIGN, index=what)
        param = Float.IndexSwitch(0., 1., 1., sign_fac, index=what)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        symbol = GChar.symbol(code=code, parameter=param)

        formula = GBuild.add(formula, term=symbol, owner_id=0, type=TYPE_GEO)

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Group

    with GeoNodes("Group", prefix=term_prefix):
        """ Group the previous terms

        Arguments
        ---------
        - Formula
        - Count (Integer) : number of nodes to group, i.e. the last count child nodes of the owner

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry(None, "Formula")
        count = Integer(1, "Count", 1, tip="Number of terms to group starting from last one")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = GBuild.group(formula, owner_id=0, count=count)

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Accentuation

    with GeoNodes("Accentuation", prefix=term_prefix):
        """ Add an accentuation symbol on the previous terms

        Arguments
        ---------
        - Formula
        - Count (Integer) : number of nodes to group, i.e. the last count child nodes of the owner
        - Symbol (Menu) : select accentuation shape
        - Below (Boolean) : put the accentuation below
        - Factor (Float in [0, 1]) : animation factor

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry(None, "Formula")
        count   = Integer(1, "Count", 1, tip="Number of terms to group starting from last one")
        code    = Integer.MenuSwitch({'Arrow': 0, 'Left Arrow': 1, 'Bar': 2, 'Dot': 3, 'Double Dot': 4, 'Triple Dot': 5}, name='Symbol')
        below   = Boolean(False, "Below")
        factor  = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = GBuild.group(formula, owner_id=0, count=count, code=DECO_ARROW + code,  option_1=below, factor=factor)

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Block

    with GeoNodes("Block", prefix=term_prefix):
        """ Group terms into brackets

        Arguments
        ---------
        - Formula
        - Count (Integer) : number of nodes to group, i.e. the last count child nodes of the owner
        - Symbol (Menu) : select brackets shape
        - Hide Left (Boolean) : hide left bracket
        - Hide Right (Boolean) : hide right bracket
        - Factor (Float in [0, 1]) : animation factor

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula  = Geometry(None, "Formula")
        count    = Integer(1, "Count", 1, tip="Number of terms to group starting from last one")
        code     = Integer.MenuSwitch({'( ... )': 0, '[ ... ]': 1, '| ... |': 2, '{ ... }': 3, '‖ ... ‖': 4, '⟨ ... ⟩': 5, '< ... >': 6}, name='Symbol')
        option_1 = Boolean(False, "Hide Left")
        option_2 = Boolean(False, "Hide Right")
        factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = GBuild.group(formula, owner_id=0, count=count, code=DECO_BLOCK + code,  option_1=option_1, option_2=option_2, factor=factor)

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Fraction

    with GeoNodes("Fraction", prefix=term_prefix):
        """ Create a fraction with the two last terms

        Arguments
        ---------
        - Formula
        - Factor (Float in [0, 1]) : animation factor

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula  = Geometry(None, "Formula")
        factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # ----- Group the two last children

        formula = GBuild.group(formula, owner_id=0, count=2, type=TYPE_FRACTION, factor=factor)

        new_id = formula.id_

        # ----- Set denominator role to the second child

        mesh = formula.mesh
        tree = formula.point_cloud

        den_info = GTree.get_child(tree, new_id, 1).node
        tree.points[Integer("ID").equal(den_info.id)]._Role = 1

        # ----- Done

        formula = mesh + tree

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Exponent and indice

    with GeoNodes("Exponent Indice", prefix=term_prefix):
        """ Add exponent and indice to a content

        Arguments
        ---------
        - Formula
        - Count (Integer) : number of nodes to group, i.e. the last count child nodes of the owner
        - Exponent (String) : exponent string
        - Indice (String) : indice string
        - Factor (Float in [0, 1]) : animation factor

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula  = Geometry(None, "Formula")
        count    = Integer(1, "Count", 1, tip="Number of terms to group starting from last one")
        sexp     = String(None, "Exponent")
        sind     = String(None, "Indice")
        factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # Group the content

        formula = GBuild.group(formula, owner_id=0, count=count, type=TYPE_EXP_IND, factor=factor)
        new_id = formula.id_

        for i, (s, role) in enumerate([(sexp, 1), (sind, 2)]):

            with Layout("Exponent" if i == 0 else "Indice"):

                ok = s.length().not_equal(0)

                chars = GChar.characters(chars=s, italic=True)
                comp_id = chars.id_

                new_formula = GBuild.add(formula, term=chars, owner_id=new_id, type=TYPE_GEO, role=role)
                formula = formula.switch(ok, new_formula)

        # ----- Done

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Sigma

    with GeoNodes("Sigma", prefix=term_prefix):
        """ Create sigma to a content

        Arguments
        ---------
        - Formula
        - Count (Integer) : number of nodes to group, i.e. the last count child nodes of the owner
        - Below (String) : exponent string
        - Above (String) : indice string
        - Factor (Float in [0, 1]) : animation factor

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula  = Geometry(None, "Formula")
        count    = Integer(1, "Count", 1, tip="Number of terms to group starting from last one")
        sfrom    = String(None, "From")
        sto      = String(None, "To")
        factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # Group the content

        formula = GBuild.group(formula, owner_id=0, count=count, type=TYPE_SIGMA, factor=factor)
        new_id = formula.id_

        for i, (s, role) in enumerate([(sfrom, 1), (sto, 2)]):

            with Layout("From (Below)" if i == 0 else "To (Above)"):

                ok = s.length().not_equal(0)

                chars = GChar.characters(chars=s, italic=True)
                comp_id = chars.id_

                new_formula = GBuild.add(formula, term=chars, owner_id=new_id, type=TYPE_GEO, role=role)
                formula = formula.switch(ok, new_formula)

        # ----- Done

        GBuild.compile(formula, link_from='TREE').out("Formula")
