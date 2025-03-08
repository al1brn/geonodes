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
SYMB_EQUAL    = 1 # Alternative to '=' character
SYMB_SIGN     = 2 # Minus to plus varying with param
SYMB_MINUS    = 3
SYMB_PLUS     = 4

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
ROLE_DENOMINATOR = 3

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

    comp_prefix = "Compile"

    GChar  = G(char_prefix)
    GUtil  = G(util_prefix)
    GBuild = G(build_prefix)
    GTerm  = G(term_prefix)
    GComp  = G(comp_prefix)


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

    def macro_get_ref(mesh):

        ref  = mesh.faces[macro_is_ref()].separate()
        work = ref.inverted_

        return Mesh(ref), Mesh(work)

    def macro_setup_ref(mesh): #, ref_type):
        mesh.faces._Reference = True

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

        chars = macro_setup_ref(chars) #, ref_type=TYPE_REF)

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

        shape = macro_setup_ref(shape) #, ref_type=TYPE_REF)

        shape.out("Mesh")
        dims.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Math operators

    with GeoNodes("Symbol", prefix=char_prefix, is_group=True):
        """ Create a reference mesh from an operator code

        Valid operator codes are:
        - SYMB_EQUAL    = 1 # Alternative to '=' character
        - SYMB_SIGN     = 2 # Minus to plus varying with param
        - SYMB_MINUS    = 3
        - SYMB_PLUS     = 4

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
        param  = Float.Factor(1, "Parameter", 0, 1)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Plus / Minus"):

            hrz = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_WIDTH, size_y=PLUS_THICK)
            symb = hrz.switch_false(symbol.equal(SYMB_MINUS))

            vrt = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_THICK, size_y=PLUS_WIDTH)
            symb = symb.switch(symbol.equal(SYMB_PLUS), hrz + vrt)

            var_vrt = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=PLUS_THICK, size_y=PLUS_WIDTH*param)
            symb = symb.switch(symbol.equal(SYMB_SIGN), hrz + vrt)

        with Layout("Equal"):

            symb = symb.switch(symbol.equal(SYMB_EQUAL),
                    Mesh(hrz).transform(translation=(0,  Y_SPACE, 0)) +
                    Mesh(hrz).transform(translation=(0, -Y_SPACE, 0)))

        symb.transform(translation=(0, Y_ALIGN, 0))

        dims = GUtil.dimensions(symb).node
        symb = macro_setup_ref(symb) #, ref_type=TYPE_REF)

        symb.out("Mesh")
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

        if False:
            tree.points.sample_index(Color(    "Color"),    index=index).out("Color")
            tree.points.sample_index(Integer(  "Fade"),     index=index).out("Fade")
            tree.points.sample_index(Boolean(  "Option 1"), index=index).out("Option 1")
            tree.points.sample_index(Boolean(  "Option 2"), index=index).out("Option 2")

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

        """
        with Panel("Aspect"):
            tree.points[selection]._Color     = Color(None,     "Color")
            tree.points[selection]._Fade      = Float(0,        "Fade")
            tree.points[selection]._Mat_Index = Integer(0,      "Material Index")

        with Panel("Animation):
            tree.points[selection]._Left      = Float(0,  "Left")
            tree.points[selection]._Right     = Float(0,  "Right")
            tree.points[selection]._Offset    = Vector(0, "Offset")
            tree.points[selection]._Scale     = Vector(1, "Scale")
            tree.points[selection]._Rotation  = Vector(1, "Rotation")
        """

        tree.out("Points")

    # =============================================================================================================================
    # =============================================================================================================================
    # Compilation
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # GROUP : Children concatenation

    with GeoNodes("Group", prefix=comp_prefix, is_group=True):

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
            vmax = new_mesh.points[child_sel].attribute_statistic(nd.position).max

            rep.x = rep.x.switch(is_content, vmax.x + X_SPACE)
            rep.mesh = mesh.switch(is_content, new_mesh)

        mesh = rep.mesh

        mesh.out("Mesh")

    # =============================================================================================================================
    # GEO : Instantiate from reference

    with GeoNodes("Reference", prefix=comp_prefix, is_group=True):

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        ref_mesh  = Mesh(None,    "Reference Mesh")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh += macro_create_work(ref_mesh, node_id, explore)

        mesh.out("Mesh")

    # =============================================================================================================================
    # SYMBOL : Instantiate from symbol code

    with GeoNodes("Symbol", prefix=comp_prefix, is_group=True):

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        with Panel("Symbol"):
            code  = Integer(0, "Symbol Code", single_value=True)
            param = Integer(0, "Parameter",   single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        symb_ref = Mesh(GChar.symbol(symbol=code, parameter=param/100))
        symb_ref.faces._ID = node_id
        mesh += macro_create_work(symb_ref, node_id, explore)

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
        shifted_mesh = Mesh(mesh)
        shifted_mesh.points[content].offset = (factor*left_shift, factor*vert_shift, 0)

        mesh.switch(apply, shifted_mesh + deco).out("Mesh")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Compile the decorator

    with GeoNodes("Decorator", prefix=comp_prefix, is_group=True):
        """ Build a decorator onto a formula mesh.

        The decorator is sized and located on the provided Selection on the mesh.

        The decorator codes are organized in categories.

        Symbol category (<= SYMB_MAX_CODE):
        - DECO_NOTHING : no decoration
        - Symbol code in SYMB_???

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

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        with Panel("Decorator"):
            code  = Integer(0, "Decoration Code", single_value=True)
            param = Integer(0, "Parameter",       single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

        mesh.out("Mesh")

    # =============================================================================================================================
    # Exponent & Indice

    with GeoNodes("Indice Exponent", prefix=comp_prefix, is_group=True):
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

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Content"):
            cont_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_CONTENT)).node
            content   = GTree.select(tree, id=cont_node.id, mode='Branch')
            cdims     = GUtil.dimensions(mesh, content).node

        with Layout("Indice"):
            ind_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_INDICE)).node
            indice   = GTree.select(tree, id=ind_node.id, mode='Branch')

        with Layout("Exponent"):
            exp_node = GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Role").equal(ROLE_EXPONENT)).node
            exponent = GTree.select(tree, id=exp_node.id, mode='Branch')

        with Layout("Scale Exponent and Indice"):
            mesh.points[exponent].position *= (SCALE_IND*factor, SCALE_IND, SCALE_IND)
            mesh.points[indice].position   *= (SCALE_IND*factor, SCALE_IND, SCALE_IND)

        with Layout("Offset Exponent and Indice"):
            left = cdims.x_max + X_SPACE/3

            mesh.points[exponent].offset = (left, cdims.y_min + .8*cdims.height, 0)
            mesh.points[indice].offset   = (left, cdims.y_min - .1*cdims.height, 0)

        mesh.out("Mesh")

    # =============================================================================================================================
    # Sigma

    with GeoNodes("Sigma", prefix=comp_prefix, is_group=True):
        """ Discreet sum.

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

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

        # ----- Sigma Symbol

        with Layout("Sigma Symbol"):

            # ----- Base
            sigma = Mesh(GUtil.sigma_char(fill=True)).transform(scale=SIGMA_SCALE)

            # ----- Height
            sigma_height = gnmath.min(1, cdims.height)
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

        with Layout("Locate Below and Above"):
            mesh.points[below].offset = (sdims.x_mid - bdims.x_mid, sdims.y_min - Y_SPACE - bdims.y_max , 0)
            mesh.points[above].offset = (sdims.x_mid - adims.x_mid, sdims.y_max + Y_SPACE - bdims.y_min , 0)
            mesh.points[below].position *= (factor, 1, 1)
            mesh.points[above].position *= (factor, 1, 1)


        mesh.out("Mesh")

    # =============================================================================================================================
    # Integral

    with GeoNodes("Integral", prefix=comp_prefix, is_group=True):
        """ Integral.

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

        mesh      = Mesh(None,    "Mesh")
        tree      = Cloud(None,   "Tree")
        factor    = Float(1.,     "Factor")

        with Panel("Mesh Tree Info"):
            node_id = Integer(1,    "Id",       hide_value=True, single_value=True)
            explore = Integer(1,    "Explore",  hide_value=True, single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
            integral = Mesh(GUtil.integral_char(fill=True, height=sigma_height))
            int_dims = GUtil.dimensions(integral, True).node

            # ----- Vertical center with content
            integral.transform(translation=(0, cdims.y_mid - int_dims.y_mid, 0))

            # ----- Add to the mesh
            integral = macro_setup_work(integral, node_id, explore)
            integral.transform(scale = (factor, 1, 1))
            mesh += integral

            # ----- Get the final dims
            sdims = GUtil.dimensions(mesh, Integer("ID").equal(node_id)).node

        with Layout("Locate content"):
            mesh.points[content].offset = ((sdims.x_max + X_SPACE/3)*factor, 0, 0)

        with Layout("Locate Below and Above"):
            mesh.points[below].offset = (sdims.x_min + sdims.width*.5, sdims.y_min - bdims.y_mid, 0)
            mesh.points[above].offset = (sdims.x_max + X_SPACE/2,      sdims.y_max - adims.y_mid , 0)
            mesh.points[below].position *= (factor, 1, 1)
            mesh.points[above].position *= (factor, 1, 1)


        mesh.out("Mesh")

    # =============================================================================================================================
    # Compilation test

    with GeoNodes("Test", prefix=comp_prefix, is_group=True):

        factor = Float.Factor(1, "Factor", 0, 1)
        code   = Integer(0, "Code")
        param  = Integer(0, "Parameter")

        with If(Geometry, 'Characters') as geo:
            ref_mesh = GChar.characters(chars="Ref")
            ref_mesh.faces._ID = 1

            tree = GTree.new()
            tree = GUtil.initialize_node(tree, True)
            tree.points[nd.index.equal(1)]._Type = TYPE_REF

            geo.option = GComp.reference(tree=tree, id=1, reference_mesh=ref_mesh, factor=factor)

        with Elif(geo, 'Group'):
            a = macro_setup_work(GChar.characters(chars="pi"),   2, 2)
            b = macro_setup_work(GChar.characters(chars="\\approx"),    3, 3)
            c = macro_setup_work(GChar.characters(chars="3.14"), 4, 4)
            mesh = a + (b, c)

            # Group
            tree = GTree.new()
            gid = tree.id_

            # 3 chars
            tree = GTree.new(tree, gid)
            tree = GTree.new(tree, gid)
            tree = GTree.new(tree, gid)

            #tree.points[Integer("ID").equal(0) & Integer("ID").equal(gid)]._Type = TYPE_REF

            geo.option = GComp.group(mesh=mesh, tree=tree, id=gid, factor=factor)

        with Elif(geo, 'Symbol'):

            tree = GTree.new()
            tree.points[nd.index.equal(1)]._Type = TYPE_SYMBOL
            geo.option = GComp.symbol(tree=tree, id=1, symbol_code=code, factor=factor)


        with Elif(geo, 'Decorator'):

            mesh = macro_setup_work(GChar.characters(chars="x", italic=True), 2, 2)

            tree = GTree.new(tree)
            tree = GTree.new(tree, 1)
            tree.points[nd.index.equal(1)]._Type = TYPE_DECO

            geo.option = GComp.decorator(mesh=mesh, tree=tree, factor=factor, id=1,
                decoration_code=code, parameter=param)

        with Elif(geo, "Fraction"):

            mesh  = macro_setup_work(GChar.characters(chars="dF", italic=True),  2, 2)
            mesh += macro_setup_work(GChar.characters(chars="dx", italic=True), 3, 3)

            tree = GTree.new()
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree.points[Integer("ID").equal(2)]._Role = ROLE_CONTENT
            tree.points[Integer("ID").equal(3)]._Role = ROLE_DENOMINATOR

            geo.option = GComp.fraction(mesh=mesh, tree=tree, factor=factor, id=1)

        with Elif(geo, "Indice"):

            mesh  = macro_setup_work(GChar.characters(chars="x", italic=True), 2, 2)
            mesh += macro_setup_work(GChar.characters(chars="i", italic=True), 3, 3)
            mesh += macro_setup_work(GChar.characters(chars="2", italic=True), 4, 4)

            tree = GTree.new()
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree.points[Integer("ID").equal(2)]._Role = ROLE_CONTENT
            tree.points[Integer("ID").equal(3)]._Role = ROLE_INDICE
            tree.points[Integer("ID").equal(4)]._Role = ROLE_EXPONENT

            geo.option = GComp.indice_exponent(mesh=mesh, tree=tree, factor=factor, id=1)

        with Elif(geo, "Sigma"):

            mesh  = macro_setup_work(GChar.characters(chars="1/i", italic=True), 2, 2)
            mesh += macro_setup_work(GChar.characters(chars="i=1", italic=True), 3, 3)
            mesh += macro_setup_work(GChar.characters(chars="i=\\infty", italic=True), 4, 4)

            tree = GTree.new()
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree.points[Integer("ID").equal(2)]._Role = ROLE_CONTENT
            tree.points[Integer("ID").equal(3)]._Role = ROLE_INDICE
            tree.points[Integer("ID").equal(4)]._Role = ROLE_EXPONENT

            geo.option = GComp.sigma(mesh=mesh, tree=tree, factor=factor, id=1)

        with Elif(geo, "Integral"):

            mesh  = macro_setup_work(GChar.characters(chars="f(t)dt", italic=True), 2, 2)
            mesh += macro_setup_work(GChar.characters(chars="t=0", italic=True), 3, 3)
            mesh += macro_setup_work(GChar.characters(chars="t=\\infty", italic=True), 4, 4)

            tree = GTree.new()
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree = GTree.new(tree, 1)
            tree.points[Integer("ID").equal(2)]._Role = ROLE_CONTENT
            tree.points[Integer("ID").equal(3)]._Role = ROLE_INDICE
            tree.points[Integer("ID").equal(4)]._Role = ROLE_EXPONENT

            geo.option = GComp.integral(mesh=mesh, tree=tree, factor=factor, id=1)

        geo.out()

    # =============================================================================================================================
    # Formula compilation
    #
    # All types are implemented in dedicated group for the sake of clarity

    with GeoNodes("Main", prefix=comp_prefix, is_group=True):
        """ Compile the formula

        Formula compilation is made with following steps:
        - Separate Tree Structure (cloud of point) form the mesh
        - Delete work faces from the messh to keep the "Reference faces"
        - The a loop is performed from en empyty meh to build the final formula.
          The building loop is made from last node to tree root.
          for each node, a mesh is built depending on the node 'Type':
          - TYPE_GROUP    : chain the child meshes in their order and then add ad decorator
          - TYPE_REF      : copy the reference mesh into the mesh
          - TYPE_FRACTION : Fraction between the two child nodes
          - TYPE_IND_EXP  : use the three child nodes as content, exponent and indice
          - TYPE_SIGMA    : use the three child nodes as content, below and above sigma sum
          - TYPE_DECO     : decorator

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

            with Layout("Last to first Explore index info"):
                explore    = (count - 1 - rep.iteration)._lc("Explore")
                node_info  = GUtil.explore_info(tree, explore=explore).node
                node_id    = node_info.id
                node_type  = node_info.type
                factor     = node_info.factor

            # TYPE_GROUP    = 0
            # TYPE_REF      = 1
            # TYPE_SYMBOL   = 2
            # TYPE_DECO     = 3
            # TYPE_FRACTION = 4
            # TYPE_IND_EXP  = 5
            # TYPE_SIGMA    = 6
            # TYPE_INTEGRAL = 7

            with If(Mesh, node_type) as mesh:
                mesh.option = GComp.group(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            with Elif(mesh):
                mesh.option = GComp.reference(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore,
                reference_mesh = ref_mesh)

            with Elif(mesh):
                mesh.option = GComp.symbol(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore,
                    symbol_code=node_info.code, parameter=node_info.parameter)

            with Elif(mesh):
                mesh.option = GComp.decorator(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore,
                    decoration_code=node_info.code, parameter=node_info.parameter)

            with Elif(mesh):
                mesh.option = GComp.fraction(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            with Elif(mesh):
                mesh.option = GComp.indice_exponent(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            with Elif(mesh):
                mesh.option = GComp.sigma(mesh=rep.mesh, tree=tree,  factor=factor, id=node_id, explore=explore)

            with Elif(mesh):
                mesh.option = GComp.sigma(mesh=rep.mesh, tree=tree, factor=factor, id=node_id, explore=explore)

            # ----- Done

            rep.mesh = mesh

        formula.switch(use_compile, ref_mesh + rep.mesh + tree).out("Formula")

    # =============================================================================================================================
    # =============================================================================================================================
    # Building formula
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # Ensure a geometry contains tree

    with GeoNodes("Ensure Formula", prefix=util_prefix, is_group=True):
        """ Initialize a formula if not already done

        Arguments
        ---------
        - Geometry

        Returns
        -------
        - Formula
        - Mesh
        - Points
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula = Geometry()

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        use_init = tree.points.count.equal(0)
        is_empty = mesh.points.count.equal(0) & use_init

        with Layout("Create a new tree"):
            new_tree = GTree.new()
            new_id = new_tree.id_
            new_tree = GUtil.initialize_node(new_tree, True)
            new_tree.points[Integer("ID").equal(new_id)]._Type = TYPE_REF

        with Layout("ID and Explore to mesh faces"):
            new_mesh = Mesh(mesh)
            new_mesh.faces._ID = new_id

        mesh = mesh.switch(use_init, new_mesh).switch(is_empty)
        tree = tree.switch(use_init, new_tree).switch(is_empty)

        (mesh + tree).out("Formula")
        mesh.out("Mesh")
        tree.out("Points")
        is_empty.out("Empty")

    # =============================================================================================================================
    # Group children
    # =============================================================================================================================

    with GeoNodes("Group Children", prefix=util_prefix, is_group=True):

        formula   = Geometry(None,  "Formula")
        node_type = Integer(0,      "Type")
        role      = Integer(0,      "Role")
        code      = Integer(0,      "Code")
        force     = Boolean(False,  "Force")

        formula = GUtil.ensure_formula(formula)
        f_empty = formula.empty_

        mesh = formula.mesh
        tree = formula.point_cloud

        tree = GTree.group_children(tree, id=0, force=force)
        group_id = tree.id_

        tree = GUtil.initialize_node(tree, selection=Integer("ID").equal(group_id), type=node_type, role=role, code=code)

        formula = (mesh + tree).switch(f_empty)
        group_id = group_id.switch(f_empty, -1)

        formula.out("Formula")
        group_id.out("ID")

    # =============================================================================================================================
    # Group children
    # =============================================================================================================================

    with GeoNodes("Insert Owner", prefix=util_prefix, is_group=True):

        formula   = Geometry(None,  "Formula")
        node_id   = Integer(1,      "ID")
        node_type = Integer(0,      "Type")
        role      = Integer(0,      "Role")
        code      = Integer(0,      "Code")

        formula = GUtil.ensure_formula(formula)
        f_empty = formula.empty_

        mesh = formula.mesh
        tree = formula.point_cloud

        tree = GTree.insert_owner(tree, id=node_id)
        group_id = tree.id_

        tree = GUtil.initialize_node(tree, selection=Integer("ID").equal(group_id), type=node_type, role=role, code=code)

        formula = (mesh + tree).switch(f_empty)
        group_id = group_id.switch(f_empty, -1)

        formula.out("Formula")
        group_id.out("ID")

    # =============================================================================================================================
    # Read the group types info

    with GeoNodes("Single Group Info", prefix=util_prefix, is_group=True):

        formula = Geometry(None, "Formula")

        tree = formula.point_cloud

        count = GTree.children_count(tree)
        is_single = count.equal(1)

        with Layout("Single child group info"):
            group_info = GUtil.selection_info(tree, Integer("Owner").equal(0)).node
            is_single &= group_info.exists

        group_info.type.out("Type")
        group_info.id.out("ID")
        is_single.out("Exists")

        for i in range(4):
            with Layout(f"Role {i}"):
                child_info = GUtil.selection_info(tree, Integer("Owner").equal(group_info.id) & Integer("Role").equal(i)).node
                child_info.id.out(f"Role ID {i}")
                (child_info.exists & is_single).out(f"Exists {i}")

    # =============================================================================================================================
    # Join another term to a formula

    with GeoNodes("Join", prefix=util_prefix, is_group=True):
        """ Join another formula

        > [!IMPORTANT]
        > The root of the joined formula is dissolved if is has only one child
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula   = Geometry(None, "Formula")
        term      = Geometry(None, "Term")

        owner_id  = Integer(0, "Owner Id")
        location  = Integer.MenuSwitch({'Last Child': 0, 'After': 1, 'Before': 2, 'First Child': 3}, name='Location', menu='Last Child')
        dissolve  = Integer.MenuSwitch({'Auto': 0, 'Dissolve': 1, 'Keep': 2}, name="Dissolve", menu='Auto')

        node_type = Integer(0,      "Type")
        role      = Integer(0,      "Role")
        code      = Integer(0,      "Code")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula_init = Geometry(formula)
        term_init = Geometry(term)

        with Layout("Separate Mesh and Tree"):

            formula   = GUtil.ensure_formula(formula)
            mesh      = formula.mesh_
            tree      = formula.points_
            f_is_none = formula.empty_

            #formula_init = Geometry(formula)


            term      = GUtil.ensure_formula(term)
            t_mesh    = term.mesh_
            t_tree    = term.points_
            t_is_none = term.empty_

            #term_init = Geometry(term)


        with Layout("Dissolve condition"):
            t_children   = Cloud(t_tree).points[Integer("Owner").equal(0)].separate()
            use_dissolve = Cloud(t_children).points.count.equal(1)
            use_dissolve = Boolean.IndexSwitch(use_dissolve, True, False, index=dissolve)

        with Layout("Save old IDs and attach the branch"):
            t_tree.points._Temp_Old = Integer("ID")

            tree = GTree.attach(tree, branch=t_tree, id=owner_id, location=location)
            group_id = tree.id_
            tree = Cloud(tree)

        # ----- Group code

        with Layout("Set the group Type, Role and Decoration"):
            sel_id = Integer("ID").equal(group_id)

            tree = GUtil.initialize_node(tree, sel_id, type=node_type, role=role, code=code)

        with Repeat(mesh=t_mesh, iterations=tree.points.count) as rep:
            old_id = tree.points.sample_index(Integer('Temp Old'), index=rep.iteration)
            new_id = tree.points.sample_index(Integer('ID'),       index=rep.iteration)

            rep.mesh.faces[Integer("ID").equal(old_id)]._Temp_New = new_id

        with Layout("Set the new ID"):
            t_mesh = rep.mesh
            t_mesh.faces._ID = Integer("Temp New")

        with Layout("Dissolve old root"):
            child_id = GTree.selection_info(tree, Integer("Owner").equal(group_id)).id_

            tree = tree.switch(use_dissolve, GTree.dissolve(tree, group_id))
            group_id = group_id.switch(use_dissolve, child_id)

        with Layout("Done"):
            tree.remove_names("Temp*")
            mesh += t_mesh

        formula = mesh + tree
        formula = formula.switch(f_is_none, term_init).switch(t_is_none, formula_init)
        group_id = group_id.switch(f_is_none, 0).switch(t_is_none, -1)

        formula.out("Formula")
        group_id.out("Id")

    # =============================================================================================================================
    # Append
    # =============================================================================================================================

    with GeoNodes("Append", prefix=term_prefix, is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = Geometry(None, "Formula")
        term    = Geometry(None, "Term")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        formula = GUtil.ensure_formula(formula)
        f_empty = formula.empty_

        term = GUtil.ensure_formula(term)
        t_empty = term.empty_

        with Layout("Term must has a single child"):
            term = GUtil.group_children(term)

        with Layout("Place as content if there is space"):
            single = GUtil.single_group_info(formula).node
            as_content = single.exists_ & (-single.exists_0)
            as_content &= macro_type_has_role(single.id, 0)

        as_content = False

        with If(Geometry, as_content) as new_formula:
            frm = GUtil.join(formula, term, owner_id=single.id)
            new_id_cont = frm.id_
            new_formula.option = frm

        with Else(new_formula):
            frm = GUtil.join(formula, term=term, owner_id=0)
            new_id_app = frm.id_
            new_formula.option = frm

        formula = new_formula
        new_id = new_id_app.switch(as_content, new_id_cont)

        with Layout("Compile"):
            formula.switch(compile, GComp.main(formula)).out("Formula")
            new_id.out("Id")


    # =============================================================================================================================
    # Characters
    # =============================================================================================================================

    with GeoNodes("Characters", prefix=term_prefix, is_group=True):

        formula = Geometry(None, "Formula")
        chars   = String(None,   "Characters")

        italic = Boolean(False, "Italic")
        bold   = Boolean(False, "Bold")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        GTerm.append(formula, GChar.characters(chars, italic=italic, bold=bold), compile=compile).node.out()

    # =============================================================================================================================
    # Decoration
    # =============================================================================================================================

    with GeoNodes("Decorate", prefix=term_prefix, is_group=True):

        formula = Geometry(None, "Formula")
        code    = Integer(0, "Code")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        formula = GUtil.group_children(formula, force=False)
        node_id = formula.id_

        formula = GUtil.insert_owner(formula, id=node_id, type=TYPE_DECO, code=code)
        node_id = formula.id_

        with Layout("Compile"):
            formula.switch(compile, GComp.main(formula)).out("Formula")
            node_id.out("Id")

    # =============================================================================================================================
    # Exponent
    # =============================================================================================================================

    with GeoNodes("Indice Exponent", prefix=term_prefix, is_group=True):

        formula  = Geometry(None, "Formula")
        indice   = Geometry(None, "Indice")
        exponent = Geometry(None, "Exponent")

        with Panel("Compile"):
            compile = Boolean(True, "Compile")

        formula = GUtil.group_children(formula, force=False)
        node_id = formula.id_

        formula = GUtil.insert_owner(formula, id=node_id, type=TYPE_IND_EXP, code=code)
        group_id = formula.id_

        formula = GUtil.join(formula, indice,   owner_id=group_id, role=ROLE_INDICE)
        formula = GUtil.join(formula, exponent, owner_id=group_id, role=ROLE_EXPONENT)

        with Layout("Compile"):
            formula.switch(compile, GComp.main(formula)).out("Formula")
            group_id.out("Id")



    return

    # =============================================================================================================================
    # Group n child nodes from last
    # =============================================================================================================================

    with GeoNodes("Group", prefix=util_prefix, is_group=True):
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
        - Decoration > Code (Integer) : decoration code
        - Decoration > Factor (Float in [0, 1]) : animation factor
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

        formula   = Geometry(None,  "Formula")
        item_id   = Integer(0,      "Owner Id")
        count     = Integer(1,      "Count", 1)

        node_type = Integer(0,      "Type")
        role      = Integer(0,      "Role")
        deco      = Integer(0,      "Code")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        children_count = GTree.children_count(tree, id=item_id)
        group_sel = (Integer("Owner").equal(item_id)) & ((Integer("Order") >= children_count - count))

        new_tree = Cloud(GTree.group(tree, selection=group_sel))
        new_id = new_tree.id_
        valid = new_tree.valid_

        new_tree = GUtil.initialize_node(tree, valid & Integer("ID").equal(new_id),
           type=node_type, role=role, deco=deco)

        tree = tree.switch(valid, new_tree)

        (mesh + tree).out("Formula")
        new_id.out("Id")
        valid.out("Valid")




    return


    # -----------------------------------------------------------------------------------------------------------------------------
    # Add
    # -----------------------------------------------------------------------------------------------------------------------------

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
        - Term (Geometry) : The mesh or formule to add
        - Owner Id : owner ID where to crate the new node
        - Type (Integer) : node type
        - Code (Integer) : node code
        - Role (Integer) : node role
        - Decorator > Parameters : see "Build Set Decorator"

        Returns
        -------
        - Formula
        """
        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula   = Geometry(None, "Formula")
        term      = Geometry(None, "Term")

        owner_id  = Integer(0, "Owner Id",      single_value=True)
        location  = Integer(0, "Location",      single_value=True)
        node_type = Integer(0, "Type",          single_value=True)
        code      = Integer(0, "Code",          single_value=True)
        role      = Integer(0, "Role",          single_value=True)
        factor    = Float(  1, "Factor", 0, 1,  single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        tree = Cloud(GTree.new(tree, id=owner_id, location=0))
        new_id = tree.id_
        index = tree.index_

        term.faces._ID = tree.id_

        sel_index = nd.index.equal(index)
        tree.points[sel_index]._Type   = node_type
        tree.points[sel_index]._Code   = code
        tree.points[sel_index]._Role   = role
        tree.points[sel_index]._Factor = factor

        mesh += term

        (mesh + tree).out("Formula")
        new_id.out("Id")


    # -----------------------------------------------------------------------------------------------------------------------------
    # Transform a node to a group with the requested type

    with GeoNodes("Make Group", prefix=build_prefix, is_group=True):
        """ Transform a node to a group with the requested type.

        Arguments
        ---------
        - Formula
        - Node Id (Integer) : target node id
        - Group Type (Integer) : type of the created group
        - Role (Integer) : new role for the node in the group
        - Force (Boolean) : create a group even if condition is already met
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula    = Geometry(None,  "Formula")
        node_id    = Integer(1,      "Node Id", 1,        single_value=True)
        group_type = Integer(0,      "Group Type",        single_value=True)
        role       = Integer(0,      "Node Role",         single_value=True)
        force      = Boolean(False,  "Force",             single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        with Layout("The node already matches the required condtion"):
            id_info = GUtil.id_info(tree, node_id).node
            go = id_info.type.not_equal(group_type) | force

        with Layout("Insert a node as owner of the target"):
            new_tree = Cloud(GTree.insert_owner(tree, id=node_id))
            new_id = new_tree.id_

            sel_group = Integer("ID").equal(new_id)
            new_tree.points[sel_group]._Type = group_type

            sel_node = Integer("ID").equal(node_id)
            new_tree.points[sel_node]._Role = role

        tree = tree.switch(go, new_tree)
        new_id = new_id.switch_false(go, node_id)

        (mesh + tree).out("Formula")
        new_id.out("Id")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Add Exponent or Indice

    with GeoNodes("Add Indice Exponent", prefix=build_prefix, is_group=True):
        """ Add exponent
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula   = Geometry(None, "Formula")
        term      = Geometry(None, "Term")
        node_id   = Integer(0, "Id")
        role      = Integer(1, "Role", 1, 4)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        with Layout("Last Child if Id is not valid"):
            tree = formula.point_cloud

            last_id = GTree.get_child(tree, 0, -1).id_
            node_id = node_id.switch(node_id <= 0, last_id)

        with Layout("Insert in a 'Ind Exp' group is necessary"):

            formula = GBuild.make_group(formula, node_id=node_id, group_type=TYPE_IND_EXP, node_role=ROLE_CONTENT)
            node_id = formula.id_

            formula = GBuild.join(formula, other=term, owner_id=node_id, role=role)

        formula.out("Formula")





    # =============================================================================================================================
    # =============================================================================================================================
    # DECORATORS
    #
    # Decorators are dynamically built meshes.
    # The decorators are located relatively formula terms: sqrt, sign, arrows
    # =============================================================================================================================
    # =============================================================================================================================


    # =============================================================================================================================
    # TWO CONTENTS


    # =============================================================================================================================
    # =============================================================================================================================
    # Formula Compilation
    # =============================================================================================================================
    # =============================================================================================================================



    # =============================================================================================================================
    # =============================================================================================================================
    # Formula building
    # =============================================================================================================================
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Apply a decorator

    with GeoNodes("Set Decorator", prefix=build_prefix, is_group=True):
        """ Set decorator parameters

        Arguments
        ---------
        - Formula (Mesh + Cloud)
        - Id (Integer) : id to set
        - Code (Integer) : node code
        - Option 1 (Boolean) : option 1
        - Option 2 (Boolean) : option 2
        - Parameter (Float) : parameter

        Returns
        -------
        - Formula
        """

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        formula   = Geometry(None, "Formula")
        node_id   = Float(1, "Id", single_value=True)

        with Panel("Decorator"):
            code      = Integer(0,      "Code",         single_value=True)
            factor    = Float.Factor(1, "Factor", 0, 1, single_value=True)
            option_1  = Boolean(False,  "Option 1",     single_value=True)
            option_2  = Boolean(False,  "Option 2",     single_value=True)
            param     = Float(0,        "Parameter",    single_value=True)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        mesh = formula.mesh
        tree = formula.point_cloud

        id_sel = Integer("ID").equal(node_id)
        tree.points[id_sel]._Code     = code
        tree.points[id_sel]._Factor   = factor
        tree.points[id_sel]._Option_1 = option_1
        tree.points[id_sel]._Option_2 = option_2
        tree.points[id_sel]._Param    = param

        (mesh + tree).out("Formula")



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
            rep.y -= gnmath.max(1, dims.height) + 1

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

        formula = GBuild.add(formula, term=chars, owner_id=0, type=TYPE_REF)

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
        symbol   = Integer.MenuSwitch({'Minus to Plus': SYMB_SIGN, 'Minus': SYMB_MINUS, 'Plus': SYMB_PLUS, 'Equal': SYMB_EQUAL}, name='Symbol')
        param    = Float.Factor(1, "Parameter", 0, 1, tip="Minus to plus factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        #code  = Integer.IndexSwitch(DECO_SIGN, DECO_SIGN, DECO_EQUAL, DECO_SIGN, index=what)
        #param = Float.IndexSwitch(0., 1., 1., sign_fac, index=what)

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        symbol = GChar.symbol(symbol=symbol, parameter=param)

        formula = GBuild.add(formula, term=symbol, owner_id=0, type=TYPE_REF)

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

        formula = GBuild.group(formula, owner_id=0, count=count, code=DECO_CAT_BLOCK + code,  option_1=option_1, option_2=option_2, factor=factor)

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
        tree.points[Integer("ID").equal(den_info.id)]._Role = ROLE_DENOMINATOR

        # ----- Done

        formula = mesh + tree

        GBuild.compile(formula, link_from='TREE').out("Formula")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Exponent and indice

    with GeoNodes("Indice Exponent", prefix=term_prefix):
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
        sbelow   = String(None, "Indice")
        sabove   = String(None, "Exponent")
        factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # Group the content

        formula = GBuild.group(formula, owner_id=0, count=count, type=TYPE_GROUP, factor=factor)
        group_id = formula.id_

        formula = GBuild.group(formula, owner_id=0, count=1, type=TYPE_IND_EXP, factor=factor)
        new_id = formula.id_

        for i, (s, role) in enumerate([(sbelow, ROLE_INDICE), (sabove, ROLE_EXPONENT)]):

            with Layout("Exponent" if i == ROLE_ABOVE else "Indice"):

                ok = s.length().not_equal(0)

                chars = GChar.characters(chars=s, italic=True)
                comp_id = chars.id_

                new_formula = GBuild.add(formula, term=chars, owner_id=new_id, type=TYPE_REF, role=role)
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
        sbelow   = String(None, "From")
        sabove   = String(None, "To")
        factor   = Float.Factor(1, "Factor", 0, 1, tip="Animation factor")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        # Group the content

        formula = GBuild.group(formula, owner_id=0, count=count, type=TYPE_GROUP, factor=factor)
        content_id = formula.id_

        # Sigma char

        formula = GBuild.group(formula, owner_id=0, count=1, type=TYPE_SIGMA, factor=factor)
        new_id = formula.id_

        for i, (s, role) in enumerate([(sbelow, ROLE_INDICE), (sabove, ROLE_EXPONENT)]):

            with Layout("From (Below)" if i == ROLE_INDICE else "To (Above)"):

                ok = s.length().not_equal(0)

                chars = GChar.characters(chars=s, italic=True)
                comp_id = chars.id_

                new_formula = GBuild.add(formula, term=chars, owner_id=new_id, type=TYPE_REF, role=role)
                formula = formula.switch(ok, new_formula)

        # ----- Done

        GBuild.compile(formula, link_from='TREE').out("Formula")
