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
SCALE_IND    = 0.4   # Indice and exponent scale

DECO_THICK   = 0.06   # Decoractors thickness

# SIGN
PLUS_THICK = DECO_THICK
PLUS_WIDTH = .7

# FRACTION
FRAC_THICK  = DECO_THICK
FRAC_MARGIN = 2*X_SPACE

# ===== Symbols

SYMB_NULL     = 0
SYMB_EQUAL    = 1 # Alternative to '=' character     = 2 # Minus to plus varying with param
SYMB_SIGN     = 2

SYMB_MAX_CODE = 4 # Max symbol code

# ===== Node Types

TYPE_GROUP    = 0 # Group of nodes with decorator
TYPE_REF      = 1 # Simple geometry
TYPE_SYMBOL   = 2 # Symbol dynamically computed
TYPE_DECO     = 3 # Decorator
TYPE_FRACTION = 4 # Fraction
TYPE_IND_EXP  = 5 # Indice / Exponent
TYPE_SIGMA    = 6 # Sigma
TYPE_INTEGRAL = 7 # Integral

VALID_ROLE_TYPES = {
    0: [TYPE_IND_EXP, TYPE_SIGMA, TYPE_INTEGRAL, TYPE_FRACTION, TYPE_DECO],
    1: [TYPE_IND_EXP, TYPE_SIGMA, TYPE_INTEGRAL, TYPE_FRACTION],
    2: [TYPE_IND_EXP, TYPE_SIGMA, TYPE_INTEGRAL],
    3: [],
}

# ===== DECORATORS

DECO_NOTHING            = 0

# ----- Prefixes : code is a symbol
DECO_CAT_PREFIX         = SYMB_MAX_CODE # Code belo

# ----- Special
DECO_CAT_SPECIAL        = 20

DECO_SQRT               = 20

# ----- BLOCK
DECO_CAT_BLOCK          = 30

DECO_PARENTHESIS        = 30
DECO_BRACKETS           = 31
DECO_BRACES             = 32
DECO_ABSOLUTE           = 33
DECO_NORM               = 34
DECO_ANGLE              = 35
DECO_TOKEN              = 36

# ----- Accentuation

DECO_CAT_ACCENTUATION   = 40
DECO_ARROW              = 40
DECO_LEFT_ARROW         = 41
DECO_BAR                = 42
DECO_DOT                = 43
DECO_DOT2               = 44
DECO_DOT3               = 45

# ===== ROLES

ROLE_CONTENT     = 0
ROLE_INDICE      = 1
ROLE_EXPONENT    = 2
ROLE_DENOMINATOR = 1

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
# demo
# =============================================================================================================================
# =============================================================================================================================

def demo():
    build_shaders()
    build_groups()

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
# Utilities
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

    REF_OFFSET_Z = False

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
    anim_prefix  = "Anim"

    comp_prefix = "Compile"

    GChar  = G(char_prefix)
    GUtil  = G(util_prefix)
    GBuild = G(build_prefix)
    GTerm  = G(term_prefix)
    GComp  = G(comp_prefix)
    CAnim  = G(anim_prefix)


    # ----- Built in symbols

    create_curve("Util Sqrt Char", formula_data.SQRT_CHAR)
    create_curve("Util Sigma Char", formula_data.SIGMA_CHAR)
    create_curve("Util Half Integral", formula_data.INTEGRAL_CHAR)

    # ----------------------------------------------------------------------------------------------------
    # Macros
    # ----------------------------------------------------------------------------------------------------

    def macro_is_ref():
        return Boolean("Reference")

    def macro_is_work():
        return -Boolean("Reference")

    def macro_get_ref_mesh(mesh):

        ref  = mesh.faces[macro_is_ref()].separate()
        work = ref.inverted_

        return Mesh(ref), Mesh(work)

    def macro_new_ref_id(formula):
        with Layout("New Reference ID"):
            return mesh.mesh.faces.attribute_statistic(Integer("Ref ID")).max.to_integer() + 1

    def macro_get_ref_id(mesh, ref_id):
        with Layout("Get Reference ID"):
            return Mesh(mesh.faces[Boolean("Reference") & Integer("Ref ID").equal(ref_id)].separate())

    def macro_setup_work(mesh, item_id, explore, x_align='LEFT'):
        with Layout("Set up"):

            vmin = mesh.points.attribute_statistic(nd.position).min
            xmax = vmin.max_.x

            x, y, z = vmin.xyz

            if REF_OFFSET_Z:
                dz = -z
            else:
                dz = 0

            if x_align == 'CENTER':
                mesh.transform(translation=(-(x + xmax)/2, 0, dz))
            elif x_align == 'RIGHT':
                mesh.transform(translation=(-x - xmax, 0, dz))
            else:
                mesh.transform(translation=(-x, 0, dz))

            mesh.faces._Reference = False

            mesh.faces.material = "Formula"
            mesh.faces._ID      = item_id
            mesh.faces._Explore = explore

            return mesh

    def macro_create_work(ref, ref_id, item_id, explore):
        with Layout("Create Work faces from reference"):

            mesh = Mesh(ref).faces[Integer("Ref ID").equal(ref_id)].separate()

            mesh = Mesh(mesh)
            vmin = -mesh.points.attribute_statistic(nd.position).min
            x, y, z = vmin.xyz

            if REF_OFFSET_Z:
                dz = z
            else:
                dz = 0

            mesh.transform(translation=(x, 0, dz))

            mesh.faces._Reference = False

            mesh.faces.material = "Formula"
            mesh.faces._ID      = item_id
            mesh.faces._Explore = explore

            return mesh

    def macro_formula_is_empty(geo):
        with Layout("Formula is empty"):
            mesh = geo.mesh
            tree = geo.point_cloud
            return mesh.points.equal(0) & tree.points.equal(0)

    def macro_type_has_role(node_type, role):

        with Layout(f"Type has role {role}"):
            has_role = None
            for t in VALID_ROLE_TYPES[role]:
                test = node_type.equal(t)
                if has_role is None:
                    has_role = test
                else:
                    has_role |= test
            return has_role

    # =============================================================================================================================
    # Integral char

    with GeoNodes("Integral Char", prefix=util_prefix, is_group=True):

        fill   = Boolean(True, "Fill")
        height = Float(1., "Height", 1)

        half = Curve(GUtil.half_integral(fill=False))

        count = half.points.count
        total = 2*count - 2

        int_char = Curve.Circle(resolution = total)
        int_char.splines.type = 'BEZIER'
        int_char.handle_type  = 'FREE'
        int_char.resolution   = 36

        with Layout("Scale"):
            half.points[(nd.index > 0) & (nd.index < count-1)].position += (0, height - 1, 0)
            half[nd.index.equal(0)].right_handle_position *= (1, height, 1)
            # 1.5 is linked to model is not perfect
            half[nd.index.equal(count-1)].right_handle_position *= (1, height*1.5, 1)

        with Layout("First half"):
            int_char.points[nd.index < count].position = half.points.sample_index(nd.position, index=nd.index)

            int_char[nd.index < count].left_handle_position = half.points.sample_index(half.left_handle_position, index=nd.index)
            int_char[nd.index < count].right_handle_position = half.points.sample_index(half.right_handle_position, index=nd.index)

        with Layout("Second half"):

            full_sel = nd.index >= count
            half_index = nd.index - count + 1

            half.transform(rotation=(0, 0, pi))

            int_char.points[full_sel].position = half.points.sample_index(nd.position, index=half_index)

            int_char[full_sel].left_handle_position  = half.points.sample_index(half.left_handle_position,  index=half_index)
            int_char[full_sel].right_handle_position = half.points.sample_index(half.right_handle_position, index=half_index)


        int_char.switch(fill, int_char.fill_ngons()).out()


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
    # Set up reference mesh
    # =============================================================================================================================

    with GeoNodes("Setup Reference Mesh", prefix=util_prefix, is_group=True):

        mesh = Mesh(None, "Mesh")
        seed = Integer(0, "Seed")

        with Layout("Random Reference ID"):
            v = mesh.points.attribute_statistic(nd.position).sum
            ref_id = v.hash_value(seed=seed)

        with Layout("Set up the mesh as reference"):
            mesh.faces._Reference = True
            mesh.faces._Ref_ID    = ref_id
            mesh.faces.material   = "Formula Reference"

            if REF_OFFSET_Z:
                mesh.offset = (0, 0, -1)

        mesh.out("Mesh")
        ref_id.out("Reference ID")

    with GeoNodes("Append Reference Mesh", prefix=util_prefix, is_group=True):

        mesh = Mesh(None, "Mesh")
        term = Mesh(None, "Term")

        with Repeat(term=term, iterations=term.faces.count) as rep:
            ref_id = rep.term.faces.sample_index(Integer("Ref ID"), index=rep.iteration)
            ok_del = Mesh(Mesh(mesh).faces[Integer("Ref ID").equal(ref_id)].separate()).points.count.not_equal(0)
            rep.term.faces[nd.index.equal(rep.iteration)]._Delete = ok_del

        term = rep.term

        term = term.faces[Boolean("Delete")].delete()
        term = term.switch(term.faces.count > 0, Mesh(term).remove_named_attribute("Delete"))

        (mesh + term).out("Mesh")


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

        chars = GUtil.setup_reference_mesh(chars)
        ref_id = chars.reference_id_

        chars.out("Mesh")
        ref_id.out("Reference ID")
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

        shape = GUtil.setup_reference_mesh(shape)
        ref_id = shape.reference_id_

        shape.out("Mesh")
        ref_id.out("Reference ID")
        dims.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Math operators

    with GeoNodes("Symbol", prefix=char_prefix, is_group=True):
        """ Create a reference mesh from an operator code

        Valid operator codes are:
        - SYMB_EQUAL    = 1 # Alternative to '=' character
        - SYMB_SIGN     = 2

        > [!NOTE]
        > - The created mesh is left aligned
        > - The node also returns the dimensions of the created mesh using the
        >   output sockets of "Util Dimensions"

        Arguments
        ---------
        - Symbol (Integer) : symbol code
        - Parameter (Float) : Factor for varying meshes

        Returns
        -------
        - Mesh : the reference mesh
        - Output sockets of "Util Dimensions"
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        symbol = Integer(1, "Symbol")
        param  = Integer(0, "Parameter")

        factor = gnmath.min(100, gnmath.max(0, param))/100

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Plus / Minus"):

            hrz = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_WIDTH, size_y=PLUS_THICK)
            vrt = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_THICK, size_y=PLUS_WIDTH*factor)
            symb = (hrz + vrt).switch_false(symbol.equal(SYMB_SIGN))

        with Layout("Equal"):

            symb = symb.switch(symbol.equal(SYMB_EQUAL),
                    Mesh(hrz).transform(translation=(0,  Y_SPACE, 0)) +
                    Mesh(hrz).transform(translation=(0, -Y_SPACE, 0)))

        symb.transform(translation=(0, Y_ALIGN, 0))

        dims = GUtil.dimensions(symb).node
        symb = GUtil.setup_reference_mesh(symb)
        ref_id = symb.reference_id_

        symb.out("Mesh")
        ref_id.out("Reference ID")
        dims.out()

    # =============================================================================================================================
    # =============================================================================================================================
    # Reading tree structure
    # =============================================================================================================================
    # =============================================================================================================================

    with GeoNodes("Index Info", prefix=util_prefix, is_group=True):
        """ Read the node info by index.

        Arguments
        ---------
        - Formula (Geometry) : Geometry with tree structure
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

        formula = Geometry(None, "Formula")
        index = Integer(0, "Index")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        tree = formula.point_cloud

        info = GTree.index_info(tree, index=index).node
        info.out()

        tree.points.sample_index(Integer(  "Type"),     index=index).out("Type")
        tree.points.sample_index(Integer(  "Role"),     index=index).out("Role")
        tree.points.sample_index(Integer(  "Code"),     index=index).out("Code")
        tree.points.sample_index(Float(    "Factor"),   index=index).out("Factor")
        tree.points.sample_index(Integer(  "Param"),    index=index).out("Parameter")

        tree.points.sample_index(Boolean(  "Set Color"),index=index).out("Set Color")
        tree.points.sample_index(Color(    "Color"),    index=index).out("Color")
        tree.points.sample_index(Float(    "Fade"),     index=index).out("Fade")
        tree.points.sample_index(Integer(  "Mat Index"),index=index).out("Mat Index")

        tree.points.sample_index(Float(    "Left"),     index=index).out("Left")
        tree.points.sample_index(Float(    "Right"),    index=index).out("Right")
        tree.points.sample_index(Float(    "Scale X"),  index=index).out("Scale X")
        tree.points.sample_index(Float(    "Scale Y"),  index=index).out("Scale Y")
        tree.points.sample_index(Float(    "Rotation"), index=index).out("Rotation")


    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Id Info", prefix=util_prefix, is_group=True):
        """ Read the node info by ID.

        Arguments
        ---------
        - Formula (Geometry) : Geometry with tree structure
        - Id (Integer) : an ID on the tree structure

        Returns
        -------
        - see "Util Index Info"
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry(None, "Formula")
        node_id = Integer(1,  "Id")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        GUtil.index_info(formula, index=GTree.id_info(formula.point_cloud, id=node_id)).node.out()

    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Explore Info", prefix=util_prefix, is_group=True):
        """ Read the node info by Explore index.

        Arguments
        ---------
        - Formula (Geometry) : Geometry with tree structure
        - Explore (Integer) : an Explore index on the tree structure

        Returns
        -------
        - see "Util Index Info"
        """

        formula = Geometry(None, "Formula")
        explore = Integer(1,  "Explore")

        GUtil.index_info(formula, index=GTree.explore_info(formula.point_cloud, explore=explore)).node.out()

    with GeoNodes("Selection Info", prefix=util_prefix, is_group=True):
        """ Read the node info by selection in the tree.

        Arguments
        ---------
        - Formula (Geometry) : Geometry with tree structure
        - Selection (Boolean) : an Explore index on the tree structure

        Returns
        -------
        - see "Util Index Info"
        """

        formula   = Geometry(None, "Formula")
        selection = Boolean(False,  "Selection")

        tree = formula.point_cloud
        info = GTree.selection_info(tree, selection).node
        exists = info.exists_

        GUtil.index_info(formula, index=info.index).node.out()
        exists.out("Exists")

    # =============================================================================================================================
    # Initialize a node

    with GeoNodes("Initialize Node", prefix=util_prefix, is_group=True):
        """ Initialize a node with its default values

        Arguments
        ---------
        - Tree (Cloud)
        - Selection (Boolean)
        - Initial values

        Returns
        -------
        - Tree
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        tree = Cloud(None, "Tree")
        selection = Boolean(False, "Selection")

        tree.points[selection]._Type   = Integer(0,       "Type")
        tree.points[selection]._Role   = Integer(0,       "Role")
        tree.points[selection]._Code   = Integer(0,       "Code")

        tree.points[selection]._Factor = Float.Factor(1,  "Factor", 0, 1)
        tree.points[selection]._Param  = Integer(0,       "Parameter")

        with Panel("Aspect"):
            tree.points[selection]._Set_color = Boolean(None,   "Set Color")
            tree.points[selection]._Color     = Color(None,     "Color")
            tree.points[selection]._Fade      = Float(0,        "Fade")
            tree.points[selection]._Mat_Index = Integer(0,      "Material Index")

        with Panel("Animation"):
            tree.points[selection]._Left      = Float(0,  "Left")
            tree.points[selection]._Right     = Float(0,  "Right")
            tree.points[selection]._Scale_X   = Float(1,  "Scale X")
            tree.points[selection]._Scale_Y   = Float(1,  "Scale Y")
            tree.points[selection]._Rotation  = Float(0,  "Rotation")

        tree.out("Points")

    # =============================================================================================================================
    # =============================================================================================================================
    # Compilation
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # Rotation parameter

    with GeoNodes("Transform", prefix=util_prefix, is_group=True):
        """ Rotate a term

        Arguments
        ---------
        - Mesh
        - Scale X (Float)
        - Scale Y (Float)
        - Rotation (Angle)
        - Set Color (Boolean)
        - Color (Color)
        - Fade (Float)
        - Selection (Boolean = True) : selection

        Returns
        -------
        - Mesh : Transformed Mesh
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None, "Mesh")
        scale_x = Float(1, "Scale X")
        scale_y = Float(1, "Scale Y")
        rot     = Float.Angle(0, "Rotation")
        set_col = Boolean(False, "Set Color")
        color   = Color(0, "Color")
        fade    = Float(0, "Fade")
        sel     = Boolean(True, "Selection")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh.faces[sel].separate()
        inv_mesh = mesh.inverted_

        center = mesh.points.attribute_statistic(nd.position).mean
        mesh.transform(translation=-center)
        mesh.transform(translation=center, rotation=(0, 0, rot), scale=(scale_x, scale_y, 1))
        col_mesh = Mesh(mesh)
        col_mesh.faces._Color = color
        col_mesh.faces._Fade  = fade
        mesh = mesh.switch(set_col, col_mesh)

        mesh += inv_mesh
        mesh.out()

    # =============================================================================================================================
    # GROUP : Children concatenation

    with GeoNodes("Group", prefix=comp_prefix, is_group=True):
        """ Compile a group

        Child meshes have be previously compiled, i.e. having ID and Explore attributes.
        These child mesh are aligned to form the group mesh.

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        children_count = GTree.children_count(tree, id=node_id)

        with Repeat(mesh=mesh, x=0., iterations=children_count) as rep:

            mesh = rep.mesh

            child_id   = GTree.get_child(tree, id=node_id, order=rep.iteration).id_
            child_info = GUtil.id_info(tree, child_id).node
            child_role = child_info.role
            is_content = child_role.equal(ROLE_CONTENT)

            child_sel = GTree.select(tree, id=child_id, mode='Branch')

            new_mesh = Mesh(mesh)
            new_mesh.points[child_sel].offset = (rep.x, 0, 0)
            new_mesh.faces[child_sel]._Work = True
            vmax = new_mesh.points[child_sel].attribute_statistic(nd.position).max
            vmin = vmax.min_
            width = vmax.x - vmin.x
            dx = (width + X_SPACE).switch(width.equal(0))
            dx = dx.switch_false(is_content)

            rep.x += dx
            rep.mesh = mesh.switch(is_content, new_mesh)

        mesh = rep.mesh

        mesh.out("Mesh")

    # =============================================================================================================================
    # GEO : Instantiate from reference

    with GeoNodes("Reference", prefix=comp_prefix, is_group=True):
        """ Compile a refrence mesh

        The reference mesh is duplicated and aligned left with proper material.

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index
        - Reference > Reference Mesh (Mesh) : reference mesh to copy faces from
        - Reference > Reference ID (Integer) : reference ID in the reference mesh

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        with Panel("Reference"):
            ref_mesh  = Mesh(None, "Reference Mesh")
            ref_id    = Integer(0, "Reference ID", single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        id_info = GUtil.id_info(tree, id=node_id).node

        work = macro_create_work(ref_mesh, ref_id, node_id, explore)
        work.faces._Color = id_info.color
        work.faces._Fade  = id_info.fade
        work.points.position *= (id_info.scale_x, id_info.scale_y, 1)

        work.faces._Work = True

        mesh += work

        mesh.out("Mesh")

    # =============================================================================================================================
    # SYMBOL : Instantiate from symbol code

    with GeoNodes("Symbol", prefix=comp_prefix, is_group=True):
        """ Compile a symbol

        Faces are built form symbol code

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index
        - Symbol > Symbol Code (Integer) : symbol code
        - Symbol > Parameter (Integer) : symbol parameter

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        with Panel("Symbol"):
            code  = Integer(0, "Symbol Code", single_value=True)
            param = Integer(0, "Parameter",   single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        symb_ref = Mesh(GChar.symbol(symbol=code, parameter=param))
        symb_ref.faces._Ref_ID = 1

        symb = Mesh(macro_create_work(symb_ref, 1, node_id, explore))
        symb.faces._Work = True

        mesh += symb

        mesh.out("Mesh")

    # =============================================================================================================================
    # Create a decorator

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add the created decorator

    with GeoNodes("Add Decorator", prefix=util_prefix, is_group=True):
        """ Add a decorator to a mesh

        The decorator must have been computed to take place into the formula.
        adding the mesh generally requires to move the terms it refers to.

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

        mesh       = Mesh(None,         "Mesh")
        content    = Boolean(False,     "Content", hide_value=True)
        apply      = Boolean(True,      "Apply")

        deco       = Mesh(None,         "Decorator")
        left_shift = Float(0.,          "Left Shift")
        vert_shift = Float(0.,          "Vertical Shift")
        factor     = Float.Factor(1,    "Factor", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        xmin = deco.points.attribute_statistic(nd.position.x).min
        xmax = xmin.max_

        deco = deco.transform(translation=(-xmin, 0, 0)).transform(scale=(factor, 1, 1)).transform(translation=(xmin, 0, 0))
        deco = deco.switch(factor.equal(0))
        deco.faces._Work = True

        shifted_mesh = Mesh(mesh)
        shifted_mesh.points[content].offset = (factor*left_shift, factor*vert_shift, 0)
        shifted_mesh.points[content]._Work = True

        mesh.switch(apply, shifted_mesh + deco).out("Mesh")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Compile the decorator

    with GeoNodes("Decorator", prefix=comp_prefix, is_group=True):
        """ Compile a decorator

        The decorator is built on the first child

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index
        - Decorator > Decoration Code (Integer) : decoration code
        - Decorator > Parameter (Integer) : decoration parameter

        Returns
        -------
        - Mesh (Mesh)
        """

        unit = DECO_THICK

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        with Panel("Decorator"):
            code  = Integer(0, "Decoration Code", single_value=True)
            param = Integer(0, "Parameter",       single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Content selection"):
            content = GTree.select(tree, id=node_id, mode='Children')
            dims    = GUtil.dimensions(mesh, content).node

        # ====================================================================================================
        # SYMBOL
        # ====================================================================================================

        with Layout("Symbol"):

            is_symbol = code <= SYMB_MAX_CODE

            op_node = GChar.symbol(symbol=code, parameter=param).node
            op = macro_setup_work(op_node.mesh, node_id, explore)

            mesh = GUtil.add_decorator(mesh, content, is_symbol, decorator=op, left_shift=op_node.width + X_SPACE, factor=factor)

        # ====================================================================================================
        # Special
        # ====================================================================================================

        # -----------------------------------------------------------------------------------------------------------------------------
        # Square Root

        with Layout("Special"):

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
            sqrt = macro_setup_work(sqrt, node_id, explore)

            mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_SQRT), decorator=sqrt, left_shift=x_content, factor=factor)

        # ====================================================================================================
        # Accentuation : arrows, dots, bar
        # ====================================================================================================

        with Layout("Accentuation: arrow, bar, dot"):

            use_above = (param % 2).equal(1)

            y = (dims.y_max + Y_ABOVE).switch(use_above, dims.y_min - Y_ABOVE)

            with Layout("Bar and Arrow dims"):
                left_margin  = 2*unit
                right_margin = 4*unit
                bar_width = (dims.width + left_margin + right_margin)._lc("Bar Width")
                bar_width2 = (bar_width/2)._lc("Bar Width / 2")

            with Layout("Dot Char"):
                dot_node = GChar.characters(chars='.').node
                dot = Mesh(dot_node._out)
                dot = macro_setup_work(dot, node_id, explore, x_align='CENTER')

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
                r = macro_setup_work(r, node_id, explore)

                mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_ARROW), decorator=r, left_shift=left_margin, factor=factor)

            with Layout("Left Arrow"):

                r.transform(translation=(-bar_width2, 0, 0))
                r.transform(scale=(-1, 1, 1))
                r.transform(translation=(bar_width2, 0, 0))
                r.flip_faces()

                mesh = GUtil.add_decorator(mesh, content, code.equal(DECO_LEFT_ARROW), decorator=r, left_shift=left_margin, factor=factor)

            with Layout("Bar"):

                r = Mesh.Grid(bar_width, DECO_THICK, 2, 2).transform(translation=(bar_width2, y, 0))
                r = macro_setup_work(r, node_id, explore)

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

                use_left  = (param % 2).equal(0) # 0 or 2
                use_right = param < 2            # 0 or 1

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
                    br = macro_setup_work(br,  node_id, explore)

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
    # Fraction

    with GeoNodes("Fraction", prefix=comp_prefix, is_group=True):
        """ Compile a fraction

        The fraction node has two children with roles ROLE_CONTENT ROLE_NUMERATOR

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Numerator"):
            num_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_CONTENT)).node
            num_sel  = GTree.select(tree, id=num_node.id, mode='Branch')
            ndims    = GUtil.dimensions(mesh, num_sel).node

        with Layout("Denominator"):
            den_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_DENOMINATOR)).node
            den_sel  = GTree.select(tree, id=den_node.id, mode='Branch')
            ddims    = GUtil.dimensions(mesh, den_sel).node

        with Layout("Build the bar"):

            width = gnmath.max(ndims.width, ddims.width) + 2*FRAC_MARGIN
            x_center = width/2
            bar = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=width, size_y=FRAC_THICK).transform(translation=(x_center, Y_ALIGN, 0))

            bar = macro_setup_work(bar, node_id, explore)

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

            mesh.faces[den_sel]._Work = True

        mesh.out("Mesh")

    # =============================================================================================================================
    # Exponent & Indice

    with GeoNodes("Indice Exponent", prefix=comp_prefix, is_group=True):
        """ Compile an indice and/or exponent node

        This node has 3 children:
        - Content
        - Indice
        - Exponent

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Content"):
            cont_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_CONTENT)).node
            content   = GTree.select(tree, id=cont_node.id, mode='Branch')
            cdims     = GUtil.dimensions(mesh, content).node
            mesh.faces[content]._Work = True

        with Layout("Indice"):
            ind_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_INDICE)).node
            indice   = GTree.select(tree, id=ind_node.id, mode='Branch')

        with Layout("Exponent"):
            exp_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_EXPONENT)).node
            exponent = GTree.select(tree, id=exp_node.id, mode='Branch')

        with Layout("Scale Exponent and Indice"):
            mesh.points[exponent].position *= (SCALE_IND*factor, SCALE_IND, SCALE_IND)
            mesh.points[indice].position   *= (SCALE_IND*factor, SCALE_IND, SCALE_IND)

            mesh.faces[exponent]._Work = True
            mesh.faces[indice]._Work   = True

        with Layout("Offset Exponent and Indice"):
            left = cdims.x_max + X_SPACE/3

            mesh.points[exponent].offset = (left, cdims.y_min + .8*cdims.height, 0)
            mesh.points[indice].offset   = (left, cdims.y_min - .1*cdims.height, 0)

        mesh.out("Mesh")

    # =============================================================================================================================
    # Sigma

    with GeoNodes("Sigma", prefix=comp_prefix, is_group=True):
        """ Compile discreet sum

        This node has 3 children:
        - Content
        - Below
        - Above

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Content"):
            cont_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_CONTENT)).node
            content   = GTree.select(tree, id=cont_node.id, mode='Branch')._lc("Content")
            cdims     = GUtil.dimensions(mesh, content).node

        with Layout("Below"):
            bel_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_INDICE)).node
            below    = GTree.select(tree, id=bel_node.id, mode='Branch')._lc("Below")

        with Layout("Above"):
            abv_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_EXPONENT)).node
            above    = GTree.select(tree, id=abv_node.id, mode='Branch')._lc("Above")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Scale Below and Above"):
            mesh.points[below].position *= SCALE_IND
            mesh.points[above].position *= SCALE_IND

            bdims    = GUtil.dimensions(mesh, below).node
            adims    = GUtil.dimensions(mesh, above).node

        # ----- Sigma Symbol

        with Layout("Sigma Symbol"):

            # ----- Base
            sigma = Mesh(GUtil.sigma_char(fill=True)).transform(scale=SIGMA_SCALE)
            sigma.faces._Work = True

            # ----- Height
            sigma_height = gnmath.max(1, cdims.height)
            sigma.transform(scale=(1, sigma_height, 1))

            # ----- Vertical center with content
            sigma.transform(translation=(0, cdims.y_mid - sigma_height*(SIGMA_SCALE/2), 0))

            # ----- Add to the mesh
            sigma = macro_setup_work(sigma, node_id, explore)
            sigma.transform(scale = (factor, 1, 1))
            mesh += sigma

            # ----- Get the final dims
            sdims = GUtil.dimensions(mesh, Integer("ID").equal(node_id)).node

        with Layout("Locate content"):
            mesh.points[content].offset = ((sdims.x_max + X_SPACE/3)*factor, 0, 0)
            mesh.faces[content]._Work = True

        with Layout("Locate Below and Above"):
            mesh.points[below].offset = (sdims.x_mid - bdims.x_mid, sdims.y_min - Y_SPACE - bdims.y_max , 0)
            mesh.points[above].offset = (sdims.x_mid - adims.x_mid, sdims.y_max + Y_SPACE - bdims.y_min , 0)
            mesh.points[below].position *= (factor, 1, 1)
            mesh.points[above].position *= (factor, 1, 1)


        mesh.out("Mesh")

    # =============================================================================================================================
    # Integral

    with GeoNodes("Integral", prefix=comp_prefix, is_group=True):
        """ Compile an integral

        This node has 3 children:
        - Content
        - From
        - To

        Arguments
        ---------
        - Mesh (Mesh) : current compiled mesh
        - Tree (Cloud) : tree
        - Factor (Float) : animation factor
        - Node > ID (Integer): compilation node ID
        - Node > Explore (Integer) : compilation node explore index

        Returns
        -------
        - Mesh (Mesh)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh    = Mesh(None,    "Mesh")
        tree    = Cloud(None,   "Tree")
        factor  = Float(1.,     "Factor")

        with Panel("Node"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh_init = Mesh(mesh)

        with Layout("Content"):
            cont_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_CONTENT)).node
            content   = GTree.select(tree, id=cont_node.id, mode='Branch')
            cdims     = GUtil.dimensions(mesh, content).node

        with Layout("Below"):
            bel_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_INDICE)).node
            below    = GTree.select(tree, id=bel_node.id, mode='Branch')

        with Layout("Above"):
            abv_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_EXPONENT)).node
            above    = GTree.select(tree, id=abv_node.id, mode='Branch')

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Scale Below and Above"):
            mesh.points[below].position *= SCALE_IND
            mesh.points[above].position *= SCALE_IND

            bdims    = GUtil.dimensions(mesh, below).node
            adims    = GUtil.dimensions(mesh, above).node

        # ----- Integral Symbol

        with Layout("Integral"):

            # ----- Base
            integral_height = gnmath.min(1, cdims.height)
            integral = Mesh(GUtil.integral_char(fill=True, height=integral_height))
            integral.faces._Work = True
            int_dims = GUtil.dimensions(integral, True).node

            # ----- Vertical center with content
            integral.transform(translation=(0, cdims.y_mid - int_dims.y_mid, 0))

            # ----- Add to the mesh
            integral = macro_setup_work(integral, node_id, explore)
            integral.transform(scale=(factor, 1, 1))
            mesh += integral

            # ----- Get the final dims
            sdims = GUtil.dimensions(mesh, Integer("ID").equal(node_id)).node

        with Layout("Locate content"):
            mesh.points[content].offset = ((sdims.x_max + X_SPACE/3)*factor, 0, 0)
            mesh.faces[content]._Work = True

        with Layout("Locate Below and Above"):
            mesh.points[below].offset = (sdims.x_min + sdims.width*.5, sdims.y_min - bdims.y_mid, 0)
            mesh.points[above].offset = (sdims.x_max + X_SPACE/2,      sdims.y_max - adims.y_mid , 0)
            mesh.points[below].position *= (factor, 1, 1)
            mesh.points[above].position *= (factor, 1, 1)

            mesh.faces[below]._Work = True
            mesh.faces[above]._Work = True


        mesh.out("Mesh")

    # =============================================================================================================================
    # Compilation test

    with GeoNodes("Test", prefix=comp_prefix, is_group=True):
        """ Compilation nodes test
        """

        factor = Float.Factor(1, "Factor", 0, 1)
        code   = Integer(0, "Code")
        param  = Integer(0, "Parameter")

        def setup_tree(node_type, roles_count):

            with Layout(f"Setup a Tree {node_type} with {roles_count} roles"):
                tree = GTree.new()
                root_id = tree.id_
                tree.points[Integer("ID").equal(root_id)]._Type = node_type

                ids = [root_id]
                for i in range(roles_count):
                    tree = GTree.new(tree, root_id)
                    ids.append(tree.id_)
                    tree.points[Integer("ID").equal(ids[-1])]._Role = i

                return tree, ids

        with If(Geometry, 'Characters') as geo:

            ref_id = 123

            # Tree
            tree = GTree.new()
            node_id = tree.id_
            tree = GUtil.initialize_node(tree, selection=True, type=TYPE_REF, code=ref_id)

            # Mesh
            ref_mesh = GChar.characters(chars="Ref")
            ref_mesh.faces._Ref_ID = ref_id

            geo.option = GComp.reference(tree=tree, id=node_id, reference_mesh=ref_mesh, reference_id=ref_id, factor=factor)

        with Elif(geo, 'Group'):

            # Tree
            tree = GTree.new()
            root_id = tree.id_

            tree = GTree.new(tree, root_id)
            a_id = tree.id_
            tree = GTree.new(tree, root_id)
            b_id = tree.id_
            tree = GTree.new(tree, root_id)
            c_id = tree.id_

            # Mesh
            a = macro_setup_work(GChar.characters(chars="pi"),       a_id, 1)
            b = macro_setup_work(GChar.characters(chars="\\approx"), b_id, 2)
            c = macro_setup_work(GChar.characters(chars="3.14"),     c_id, 3)
            mesh = a + (b, c)

            geo.option = GComp.group(mesh=mesh, tree=tree, id=root_id, factor=factor)

        with Elif(geo, 'Symbol'):

            tree = GTree.new()
            root_id = tree.id_

            tree.points[nd.index.equal(root_id)]._Type = TYPE_SYMBOL
            geo.option = GComp.symbol(tree=tree, id=root_id, symbol_code=code, parameter=param, factor=factor)


        with Elif(geo, 'Decorator'):

            # Tree
            tree, ids = setup_tree(TYPE_DECO, 1)

            # Mesh
            mesh = macro_setup_work(GChar.characters(chars="x", italic=True), ids[1], 1)

            geo.option = GComp.decorator(mesh=mesh, tree=tree, factor=factor, id=ids[0],
                decoration_code=code, parameter=param)

        with Elif(geo, "Fraction"):

            # Tree
            tree, ids = setup_tree(TYPE_FRACTION, 2)

            # Mesh
            mesh  = macro_setup_work(GChar.characters(chars="dF", italic=True), ids[1], 1)
            mesh += macro_setup_work(GChar.characters(chars="dx", italic=True), ids[2], 2)

            geo.option = GComp.fraction(mesh=mesh, tree=tree, factor=factor, id=ids[0], explore=0)

        with Elif(geo, "Indice"):

            # Tree
            tree, ids = setup_tree(TYPE_IND_EXP, 3)

            # Mesh
            mesh  = macro_setup_work(GChar.characters(chars="x", italic=True), ids[1], 1)
            mesh += macro_setup_work(GChar.characters(chars="i", italic=True), ids[2], 2)
            mesh += macro_setup_work(GChar.characters(chars="2", italic=True), ids[3], 3)

            geo.option = GComp.indice_exponent(mesh=mesh, tree=tree, factor=factor, id=ids[0])

        with Elif(geo, "Sigma"):

            # Tree
            tree, ids = setup_tree(TYPE_SIGMA, 3)

            mesh  = macro_setup_work(GChar.characters(chars="1/i", italic=True), ids[1], 1)
            mesh += macro_setup_work(GChar.characters(chars="i=1", italic=True), ids[2], 2)
            mesh += macro_setup_work(GChar.characters(chars="i=\\infty", italic=True), ids[3], 3)

            geo.option = GComp.sigma(mesh=mesh, tree=tree, factor=factor, id=ids[0], explore=0)

        with Elif(geo, "Integral"):

            # Tree
            tree, ids = setup_tree(TYPE_INTEGRAL, 3)

            mesh  = macro_setup_work(GChar.characters(chars="f(t)dt", italic=True), ids[1], 1)
            mesh += macro_setup_work(GChar.characters(chars="t=0", italic=True), ids[2], 2)
            mesh += macro_setup_work(GChar.characters(chars="t=\\infty", italic=True), ids[3], 3)

            geo.option = GComp.integral(mesh=mesh, tree=tree, factor=factor, id=ids[0], explore=0)

        geo.out()

    # =============================================================================================================================
    # Formula compilation
    #
    # All types are implemented in dedicated group for the sake of clarity

    with GeoNodes("Main", prefix=comp_prefix, is_group=True):
        """ Compile the formula

        The formula compilation performs on the nodes from last explore index to the
        first one (i.e. finishing by he root node).

        This guarantees that each group has if children ready for scaling and translation.


        Arguments
        ---------
        - Formula (Mesh + Cloud) : the formula to compile
        - Compile (Boolean) : compile or node

        Returns
        -------
        - Formula (Mesh + Cloud)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(name="Formula")

        with Panel("Compile"):
            use_compile = Boolean(True, "Compile", tip="Disable but last term if performance issues are encountered")
            final       = Boolean(False,"Final",   tip="Final mesh")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        ref_mesh, _ = macro_get_ref_mesh(formula.mesh)

        tree = formula.point_cloud

        # ----- Let's explore the tree from last to start

        count = tree.points.count
        with Repeat(mesh=None, iterations=count) as rep:

            with Layout("Last to first Explore index info"):
                explore    = (count - 1 - rep.iteration)._lc("Explore")
                node_info  = GUtil.explore_info(tree, explore=explore).node
                node_id    = node_info.id
                node_type  = node_info.type
                factor     = node_info.factor

            # ----- 0: Group
            with If(Mesh, node_type) as mesh:
                mesh.option = GComp.group(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            # ----- 1: Reference
            with Elif(mesh):
                mesh.option = GComp.reference(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore,
                reference_mesh = ref_mesh, reference_id=node_info.code)

            # ----- 2 : Symbol
            with Elif(mesh):
                mesh.option = GComp.symbol(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore,
                    symbol_code=node_info.code, parameter=node_info.parameter)

            # ----- 3 : Decorator
            with Elif(mesh):
                mesh.option = GComp.decorator(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore,
                    decoration_code=node_info.code, parameter=node_info.parameter)

            # ----- 4 : Fraction
            with Elif(mesh):
                mesh.option = GComp.fraction(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            # ----- 5 : Indice / Exponent
            with Elif(mesh):
                mesh.option = GComp.indice_exponent(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            # ------ 6 : Sigma
            with Elif(mesh):
                mesh.option = GComp.sigma(mesh=rep.mesh, tree=tree,  factor=factor, id=node_id, explore=explore)

            # ----- 7 : Integral
            with Elif(mesh):
                mesh.option = GComp.integral(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            # ----- Transformation

            mesh = Mesh(GUtil.transform(mesh,
                scale_x   = node_info.scale_x,
                scale_y   = node_info.scale_y,
                rotation  = node_info.rotation,
                set_color = node_info.set_color,
                color     = node_info.color,
                fade      = node_info.fade,
                selection = Boolean("Work")))
            mesh.faces._Work = False

            # ----- Done

            rep.mesh = mesh

        formula = formula.switch(use_compile | final, ref_mesh + (rep.mesh + tree))
        formula = formula.switch(final, Geometry(formula).mesh.faces[-Boolean("Reference")].separate())
        formula.out("Formula")

    # =============================================================================================================================
    # =============================================================================================================================
    # Building formula
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # Insert Owner
    # =============================================================================================================================

    with GeoNodes("Insert Owner", prefix=util_prefix, is_group=True):
        """ Insert an owner on top of the given node

        Arguments
        ---------
        - Formula (Geometry)
        - ID (Integer) : Target node
        - Create > Type (Integer) : created node type
        - Create > Role (Integer) : created node role
        - Create > Code (Integer) : created node core

        Returns
        -------
        - Formula (Geometry)
        - ID (Integer) : created node ID
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula   = Geometry(None,  "Formula")
        node_id   = Integer(0,      "ID")
        with Panel("Create"):
            node_type = Integer(0,  "Type")
            role      = Integer(0,  "Role")
            code      = Integer(0,  "Code")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh = formula.mesh
        tree = formula.point_cloud
        f_empty = mesh.points.count.equal(0) & tree.points.count.equal(0)

        tree = GTree.insert_owner(tree, id=node_id)
        group_id = tree.id_

        tree = GUtil.initialize_node(tree, selection=Integer("ID").equal(group_id), type=node_type, role=role, code=code)

        formula = (mesh + tree).switch(f_empty)
        group_id = group_id.switch(f_empty, -1)

        formula.out("Formula")
        group_id.out("ID")

    # =============================================================================================================================
    # Attach another term to a formula
    # =============================================================================================================================

    with GeoNodes("Attach", prefix=util_prefix, is_group=True):
        """ Attach a term to a formula

        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula   = Geometry(None, "Formula")
        term      = Geometry(None, "Term")
        node_id   = Integer(0, "ID")
        location  = Integer.MenuSwitch({'Last Child': 0, 'After': 1, 'Before': 2, 'First Child': 3}, name='Location', menu='Last Child')

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula_init = Geometry(formula)
        term_init = Geometry(term)

        with Layout("Separate Mesh and Tree"):
            mesh      = formula.mesh
            tree      = formula.point_cloud
            f_is_none = mesh.points.count.equal(0) & tree.points.count.equal(0)

            t_mesh    = term.mesh
            t_tree    = term.point_cloud
            t_is_none = t_mesh.points.count.equal(0) & t_tree.points.count.equal(0)

        with Layout("Save old IDs and attach the branch"):
            t_tree.points._Temp_Old = Integer("ID")

            tree = GTree.attach(tree, branch=t_tree, id=node_id, location=location)
            new_id = tree.id_

        with Repeat(mesh=t_mesh, iterations=tree.points.count) as rep:
            rep_old_id = tree.points.sample_index(Integer('Temp Old'), index=rep.iteration)
            rep_new_id = tree.points.sample_index(Integer('ID'),       index=rep.iteration)

            rep.mesh.faces[Integer("ID").equal(rep_old_id)]._Temp_New = rep_new_id

        t_mesh = rep.mesh

        with Layout("Set the new ID"):
            t_mesh.faces._ID = Integer("Temp New")

        with Layout("Merge the formula"):
            tree.remove_names("Temp*")
            mesh = GUtil.append_reference_mesh(mesh, t_mesh)
            #mesh += t_mesh
            formula = mesh + tree

        with Layout("When formula or branch is None"):
            formula_root = GUtil.selection_info(formula_init, Integer("Owner").equal(-1)).id_
            term_root    = GUtil.selection_info(term_init,  Integer("Owner").equal(-1)).id_

            formula = formula.switch(f_is_none, term_init).switch(t_is_none, formula_init)
            new_id = new_id.switch(f_is_none, term_root).switch(t_is_none, formula_root)

        formula.out("Formula")
        new_id.out("Id")

    # =============================================================================================================================
    # Ensure a formula is a group
    # =============================================================================================================================

    with GeoNodes("Ensure Group", prefix=util_prefix, is_group=True):
        """ Make sure the tree root is a group

        Arguments
        ---------
        - Formula (Geometry)

        Returns
        -------
        - Formula (Geometry) : formula with root node to type TYPE_GROUP
        - Empty (Boolean) : True if no points
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(None, "Formula")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula_init = Geometry(formula)
        is_empty = Cloud(formula).points.count.equal(0)

        root_info = GUtil.selection_info(formula, Integer("Owner").equal(-1)).node
        is_group = root_info.type.equal(TYPE_GROUP)
        root_id = root_info.id

        new_formula = GUtil.insert_owner(formula, id=root_id, type=TYPE_GROUP)
        new_id = new_formula.id_

        formula = formula.switch_false(is_group, new_formula)
        root_id = root_id.switch_false(is_group, new_id)

        formula = formula.switch(is_empty)
        root_id = root_id.switch(is_empty, -1)

        formula.out("Formula")
        root_id.out("ID")

    # =============================================================================================================================
    # Append
    # =============================================================================================================================

    with GeoNodes("Append", prefix=term_prefix, is_group=True):
        """ Append a term as last child of the formula root

        If the formula root node is not a group (Type == TYPE_GROUP), a group is inserted
        on top of it.

        The term is joined as last join of the formula root.

        > [!NOTE]
        > If formula is empty, the term is returned without change

        Arguments
        ---------
        - Formula (Geometry) : the current formula
        - Term (Geometry) : he term to append
        - Compile > Compile : compile the result

        Returns
        -------
        - Formula (Geometry)
        - ID (Integer) : ID of the inserted term
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(None, "Formula")
        term    = Geometry(None, "Term")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Root Selection"):
            sel_root = Integer("Owner").equal(-1)

        term_init = Geometry(term)
        formula_is_empty = Cloud(formula).points.count.equal(0)
        term_root = GUtil.selection_info(term, selection=sel_root).id_

        """
        with Layout("Ensure formula is a group"):
            root_info = GUtil.selection_info(formula, sel_root).node
            is_group = root_info.type.equal(TYPE_GROUP)
            root_id = root_info.id

            new_formula = GUtil.insert_owner(formula, id=root_id, type=TYPE_GROUP)
            new_id = new_formula.id_

            formula = formula.switch_false(is_group, new_formula)
            root_id = root_id.switch_false(is_group, new_id)
        """
        formula = GUtil.ensure_group(formula)
        root_id = formula.id_

        with Layout("Join as last child of root"):
            formula = GUtil.attach(formula, term=term, id=root_id, location='Last Child')
            new_id = formula.id_

        with Layout("Formula could be empty"):
            formula = formula.switch(formula_is_empty, term_init)
            new_id = new_id.switch(formula_is_empty, term_root)

        with Layout("Compile"):
            formula.switch(compile, GComp.main(formula)).out("Formula")
            new_id.out("ID")

    # =============================================================================================================================
    # Characters
    # =============================================================================================================================

    with GeoNodes("Characters", prefix=term_prefix, is_group=True):
        """ A term made of characters

        Arguments
        ---------
        - Formula (Geometry) : the current formula
        - Characters (String) : characters forming the term
        - Compile > Compile : compile the result

        Returns
        -------
        - Formula (Geometry)
        - ID (Integer) : ID of the created term
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(None, "Formula")
        chars   = String(None,   "Characters")

        italic = Boolean(False, "Italic")
        bold   = Boolean(False, "Bold")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Build the reference mesh"):
            mesh = GChar.characters(chars, italic=italic, bold=bold)
            ref_id = mesh.reference_id_

        with Layout("Build a single node tree"):
            tree = GTree.new()
            node_id = tree.id_
            tree = GUtil.initialize_node(tree, selection=True, type=TYPE_REF, code=ref_id)

        term = mesh + tree

        GTerm.append(formula, term=term, compile=compile).node.out()

    # =============================================================================================================================
    # Symbol
    # =============================================================================================================================

    with GeoNodes("Symbol", prefix=term_prefix, is_group=True):
        """ A symbol

        Arguments
        ---------
        - Formula (Geometry) : the current formula
        - Symbol (Menu) : symbol
        - Parameter (Integer) : parameters
        - Compile > Compile : compile the result

        Returns
        -------
        - Formula (Geometry)
        - ID (Integer) : ID of the created term
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(None, "Formula")
        symbol  = Integer.MenuSwitch({'=': SYMB_EQUAL, 'Sign': SYMB_SIGN}, menu='=', name="Symbol")
        param   = Integer(0, "Parameter")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Build the reference mesh"):
            mesh = GChar.symbol(symbol=symbol, parameter=param)
            ref_id = mesh.reference_id_

        with Layout("Build a single node tree"):
            tree = GTree.new()
            node_id = tree.id_
            tree = GUtil.initialize_node(tree, selection=True, type=TYPE_REF, code=ref_id)

        term = mesh + tree

        GTerm.append(formula, term=term, compile=compile).node.out()

    # =============================================================================================================================
    # Join a content and roles
    # =============================================================================================================================

    with GeoNodes("Join", prefix=term_prefix, is_group=True):
        """ Append a types group

        A type group is a group with children having diffent roles:
        - Role 0 : Content
        - Role 1 : Indice / Below / Denominator
        - Role 2 : Exponent / above
        - Role 3 : RFU

        Arguments
        ---------
        - Formula (Geometry) : the current formula
        - Type (Integer) : the group type
        - Code (Integer) : code
        - Parameter (Integer) : parameter
        - Content (Geometry) : content term
        - Role 1 (Geometry) : role 1 term
        - Role 2 (Geometry) : role 2 term
        - Role 3 (Geometry) : role 3 term
        - Compile > Compile : compile the result

        Returns
        -------
        - Formula (Geometry) : formula
        - ID (Integer) : ID of the created node
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula   = Geometry(None,  "Formula")
        node_type = Integer(0,      "Type")
        code      = Integer(0,      "Code")
        param     = Integer(0,      "Parameter")
        content   = Geometry(None,  "Content")
        role_1    = Geometry(None,  "Role 1")
        role_2    = Geometry(None,  "Role 2")
        role_3    = Geometry(None,  "Role 3")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Create a new tree with requested type"):
            tree = GTree.new()
            new_id = tree.id_
            term = GUtil.initialize_node(tree, selection=Integer("ID").equal(new_id), type=node_type, code=code, parameter=param)

        subs = [content, role_1, role_2, role_3]

        for i in range(4):

            with Layout(f"Add role {i}"):
                sub = subs[i]
                is_empty = Cloud(sub).points.count.equal(0)

                sub_mesh = sub.mesh
                sub_tree = sub.point_cloud
                sub_tree.points[Integer("Owner").equal(-1)]._Role = i
                sub = sub_mesh + sub_tree

                new_term = GUtil.attach(term, term=sub, id=new_id)
                term = new_term.switch(is_empty, term)

        with Layout("Append"):
            formula = GTerm.append(formula, term)
            new_id = formula.id_

        formula.out("Formula")
        new_id.out("ID")

    # =============================================================================================================================
    # =============================================================================================================================
    # Animate terms
    #
    # Reference can be animated with some parameters but it is not very efficient
    # =============================================================================================================================
    # =============================================================================================================================

    with GeoNodes("Parameter", fake_user=True, prefix="Formula Set"):
        """ Set parameter on selection

        Arguments
        ---------
        - Formula (Geometry) : the formula to set
        - ID (Integer) : the formula term to change
        - Scope (Menu) : group scope
        - Change Color (Boolean) : change color
        - Color (Color) : color to set if change is requested
        - Factor (Float = 1.) : factor
        - Scale (Float = 1.) : scale
        - X Scale (Float = 1.) : x scale
        - Y Scale (Float = 1.) : y scale
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(None, "Formula")
        node_id = Integer(0, "ID")
        scope   = Integer.MenuSwitch({'All': 0, 'Children': 1, 'Top': 2}, menu='All', name="Scope")

        use_color = Boolean(True,   "Change Color")
        color     = Color((1, 0, 0),"Color")
        fade      = Float.Factor(0, "Fade", 0, 1)
        factor    = Float(1.,       "Factor")
        scale     = Float(1.,       "Scale")
        rot       = Float.Angle(0., "Rotation")
        scale_x   = Float(1.,       "Scale X")
        scale_y   = Float(1.,       "Scale Y")

        with Panel("Compile"):
            compile = Boolean(True,  "Compile")
            final   = Boolean(False, "Final")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        mesh = formula.mesh
        tree = formula.point_cloud

        with If(Boolean, scope) as sel:
            sel.option = GTree.select(tree, id=node_id, mode='Branch')

        with Elif(sel):
            sel.option = GTree.select(tree, id=node_id, mode='Children')

        with Elif(sel):
            sel.option = GTree.select(tree, id=node_id, mode='Single')

        tree = tree.switch(use_color,   Cloud(tree).points[sel].store("Color",   color))
        tree = tree.switch(use_color,   Cloud(tree).points[sel].store("Set Color", True))
        tree.points[sel].store("Scale X",  scale_x*scale)
        tree.points[sel].store("Scale Y",  scale_y*scale)
        tree.points[sel].store("Factor",   factor)
        tree.points[sel].store("Fade",     fade)
        tree.points[sel].store("Rotation", rot)

        # ----------------------------------------------------------------------------------------------------
        # Compilation

        with Layout("Compile"):
            formula = GComp.main(mesh + tree, compile=compile)

            mesh = formula.mesh
            mesh.faces[-Boolean("Reference")].separate()
            formula.switch(final, mesh).out("Geometry")

    # =============================================================================================================================
    # =============================================================================================================================
    # Animate compiled geometry
    #
    # The items can be animated once compiled
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # Select faces
    # =============================================================================================================================

    with GeoNodes("Select", fake_user=True, prefix=anim_prefix, is_group=True):
        """ Select faces by their id
        """

        select = Boolean(False, "Selection")
        ids = [Integer(-1, f"ID {i}") for i in range(10)]

        face_id = Integer("ID")
        for id in ids:
            select |= id.equal(face_id)

        select.out("Selection")

    # =============================================================================================================================
    # Transform selection
    # =============================================================================================================================

    with GeoNodes("Transform", fake_user=True, prefix=anim_prefix, is_group=True):
        """ Transform a selection
        """

        mesh   = Mesh()
        select = Boolean(True, "Selection")
        pivot  = Vector(0, "Pivot Offset")
        with Panel("Transform"):
            transl = Vector(0, "Translation")
            rot    = Vector.Euler(0, "Rotation")
            scale  = Vector(1, "Scale")

        mesh = mesh.faces[select].separate()
        rem_mesh = mesh.inverted_

        with Layout("Pivot"):

            node = mesh.points.attribute_statistic(nd.position).node
            center = (node.min + node.max)/2 + pivot

            mesh.transform(translation=-center)

        mesh.transform(translation=transl, rotation=rot, scale=scale)

        mesh.transform(translation=center)

        (mesh + rem_mesh).out("Mesh")

    # =============================================================================================================================
    # Write formula
    # =============================================================================================================================

    with GeoNodes("Write", fake_user=True, prefix=anim_prefix, is_group=True):
        """ Write selection
        """

        mesh   = Mesh()
        select = Boolean(True,     "Selection")
        factor = Float.Factor(1,   "Factor", 0, 1)
        width  = Float.Factor(.05, "Width", 0, 1)

        mesh = mesh.faces[select].separate()
        rem_mesh = mesh.inverted_

        x = nd.position.x

        with Layout("Size"):
            node = mesh.faces.attribute_statistic(x).node
            xmin = node.min
            xmax = node.max
            amp   = xmax - xmin
            margin = amp/100
            xmax += margin
            amp  += margin

            width = gnmath.max(.01, width)

            delta = amp*width
            x0 = factor.map_range(to_min=xmin - delta, to_max=xmax)
            fade = x.map_range(from_min=x0, from_max=x0+delta) #, to_min=1, to_max=0)

            #fade = x.map_range(from) >= factor.map_range(to_min=xmin, to_max=xmax+(xmax-xmin)/100)

        mesh.faces._Fade = fade

        (mesh + rem_mesh).out("Mesh")

    # =============================================================================================================================
    # Change color
    # =============================================================================================================================

    with GeoNodes("Color", fake_user=True, prefix=anim_prefix, is_group=True):
        """ Change color
        """

        mesh   = Mesh()
        select = Boolean(True, "Selection")
        color  = Color((1, 0, 0), "Color")

        mesh = mesh.faces[select].separate()
        rem_mesh = mesh.inverted_

        mesh.faces._Color = color

        (mesh + rem_mesh).out("Mesh")

    # =============================================================================================================================
    # Change fade
    # =============================================================================================================================

    with GeoNodes("Fade", fake_user=True, prefix=anim_prefix, is_group=True):
        """ Write selection
        """

        mesh   = Mesh()
        select = Boolean(True, "Selection")
        fade   = Float.Factor(0, "fade", 0, 1)

        mesh = mesh.faces[select].separate()
        rem_mesh = mesh.inverted_

        mesh.faces._Fade = fade

        (mesh + rem_mesh).out("Mesh")
