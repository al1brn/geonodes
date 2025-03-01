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

# Links

LK_AFTER  = 0
LK_EXP    = 1
LK_IND    = 2
LK_NUM    = 3
LK_DEN    = 4
LK_ABOVE  = 5
LK_BELOW  = 6
LG_BEFORE = 7

# Special groups

GR_SIGN        =  1
GR_SQRT        =  2
GR_SIGMA       =  3

GR_PARENTHESIS = 10
GR_BRACKETS    = 11

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

    formula_tree.build_tree(prefix='Tree')
    GTree = G("Tree")

    prefix = "Util"
    Util = G(prefix)

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
    # Utility nodes

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

    with GeoNodes("Dimensions", prefix=prefix, is_group=True):

        mesh = Mesh(Geometry())

        #mesh = Mesh(geo.switch(item_id.not_equal(0), Mesh(geo).faces[Integer("Item ID").not_equal(item_id)].delete()))

        node = mesh.points.attribute_statistic(nd.position)
        vmin = node.min
        vmax = node.max

        vdiff = vmax - vmin
        vmid  = (vmin + vmax)/2

        width, height, _ = vdiff.xyz
        left, below, _   = vmin.xyz
        right, over, _   = vmax.xyz
        x_mid, y_mid, _  = vmid.xyz

        left.out(  "Left")
        right.out( "Right")
        over.out(  "Over")
        below.out( "Below")
        width.out( "Width")
        height.out("Height")
        x_mid.out( "X Mid")
        y_mid.out( "Y Mid")
        vmin.out(  "V Min")
        vmax.out(  "V Max")

    # =============================================================================================================================
    # Base components

    # -----------------------------------------------------------------------------------------------------------------------------
    # Set fade and color

    with GeoNodes("Set Aspect", prefix=prefix, is_group=True):

        mesh = Mesh(Geometry())

        with Panel("Aspect"):
            color  = Color('black', 'Color')
            fade   = Float.Factor(0, "Fade", 0, 1)
            mat    = Material("Formula", "Material")

        mesh.faces._Color   = color
        mesh.faces._Fade    = fade
        mesh.faces.material = mat

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # LaTeX codes

    with GeoNodes("LaTeX Codes", prefix=prefix, is_group=True):

        s = String(None, "String")

        keys = sorted(formula_data.SYMBOLS.keys(), key= lambda x: 100 - len(x))

        for code in keys:
            c = formula_data.SYMBOLS[code]
            s = s.replace("\\" + code, c)

        s.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Characters

    with GeoNodes("Characters", prefix=prefix, is_group=True):

        s      = String(None,   "Chars")
        italic = Boolean(False, "Italic")
        bold   = Boolean(False, "Bold")

        s = G().latex_codes(s)

        reg = String(s).to_curves(size=FONT_SIZE, font=FONTS.regular)
        itl = String(s).to_curves(size=FONT_SIZE, font=FONTS.italic)
        bld = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold)
        bit = String(s).to_curves(size=FONT_SIZE, font=FONTS.bold_italic)

        curves = reg.switch(bold, bld).switch(italic, itl.switch(bold, bit))

        curves = Curve(curves.realize())

        chars = curves.fill_ngons()
        vmin = chars.points.attribute_statistic(nd.position).min

        with Layout("Left align"):
            chars.transform(translation=(-vmin.x, 0, 0))

        vmin = chars.points.attribute_statistic(nd.position).min
        vmax = vmin.max_
        width, height, _ = (vmax - vmin).xyz

        chars = Util.set_aspect(chars, link_from='TREE')

        chars.out()
        width.out("Width")
        height.out("Height")
        vmin.out("Min")
        vmax.out("Max")


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
        vmin = shape.points.attribute_statistic(nd.position).min
        vmax = vmin.max_

        shape = Util.set_aspect(shape, link_from='TREE')

        shape.out()
        width.out("Width")
        height.out("Height")
        vmin.out("Min")
        vmax.out("Max")

    # =============================================================================================================================
    # Term accentuation

    # -----------------------------------------------------------------------------------------------------------------------------
    # Accentuation
    # 0: Arrow, 1: Left Arrow, 2: Bar, 3: Dot, 4: Double dot 5: Triple Dot

    with GeoNodes("Accentuation", prefix=prefix, is_group=True):

        unit = DECO_THICK

        code    = Integer(0, "Code")
        bottom  = Boolean(False, "Bottom")

        vmin    = Vector(0, "Min", hide_value=True)
        vmax    = Vector(0, "Max", hide_value=True)

        width, height, _ = (vmax - vmin).xyz
        mid = (vmin + vmax)/2

        # ----------------------------------------------------------------------------------------------------
        # Accentuation : arrows, dots, bar
        # ----------------------------------------------------------------------------------------------------

        # ----- Usefull dims

        y = (vmax.y + Y_ABOVE).switch(bottom, vmin.y - Y_ABOVE)

        with Layout("Bar and Arrow dims"):
            left_margin = 2*unit
            right_margin = 4*unit
            bar_width = width + left_margin + right_margin

        with Layout("Dot Char"):
            dot_node = Util.characters(chars='.').node.link_from(include='Aspect')
            dot = dot_node._out
            dot.transform(translation=(mid.x - dot_node.width/2, y - dot_node.height/2, 0))
            dot_dx = (dot_node.width + X_SPACE)/2

        # ----- 0 : Arrow

        with If(Curve, code) as deco:

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

            r.transform(translation=(mid.x - width/2, y, 0))
            r = r.fill_ngons()

            deco.option = r

        # ----- 1 : Left Arrow

        with Elif(deco):

            cmin = r.points.attribute_statistic(nd.position).min
            cmax = cmin.max_
            cmid = (cmin + cmax)/2

            r.transform(translation=(-cmid.x, 0, 0))
            r.transform(scale=(-1, 1, 1))
            r.transform(translation=(cmid.x, 0, 0))
            r.flip_faces()

            deco.option = r

        # ----- 2 : Bar

        with Elif(deco):

            deco.option = Mesh.Grid(bar_width, DECO_THICK, 2, 2).transform(translation=(mid.x, y, 0))

        # ----- 3 : Dot

        with Elif(deco):

            deco.option = dot

        # ----- 4 : Double dots

        with Elif(deco):

            dot2 = Curve(dot).transform(translation=(-dot_dx, 0, 0)) + Curve(dot).transform(translation=(dot_dx, 0, 0))

            deco.option = dot2

        # ----- 5 : Triple dots

        with Elif(deco):

            deco.option = Curve(dot).transform(translation=(-2*dot_dx, 0, 0)) + Curve(dot2).transform(translation=(dot_dx, 0, 0))

        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Finalize

        # ----- Deco dims

        deco_min = deco.points.attribute_statistic(nd.position).min
        deco_max = deco_min.max_
        left_space  = gnmath.max(0, vmin.x - deco_min.x)
        right_space = gnmath.max(0, deco_max.x - vmax.x)

        # ----- Finalize

        deco = Util.set_aspect(deco, link_from='TREE')

        deco.out()
        left_space.out("Left")
        right_space.out("Right")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Brackets
    # 0: '( )', 1: '[ ]', 2: '| |', 3: '{ }', 4: '‖ ‖', 5: '⟨ ⟩ ', 6: '< >'

    with GeoNodes("Brackets", prefix=prefix, is_group=True):

        BRACKETS = ['()', '[]', '||', '{}', '‖‖', '⟨⟩', '<>']

        code      = Integer(0, "Code")
        use_left  = Boolean(True, "Left")
        use_right = Boolean(True, "Right")

        vmin      = Vector(0, "Min", hide_value=True)
        vmax      = Vector(0, "Max", hide_value=True)

        width, height, _ = (vmax - vmin).xyz
        mid = (vmin + vmax)/2

        # ---------------------------------------------------------------------------
        # Brackets instantiation

        brackets = [[], []]
        for chars in BRACKETS:
            for i in range(2):
                with Layout(f"Bracket {chars[i]}"):
                    br_node = Util.characters(chars=chars[i]).node.link_from(include='Aspect')
                    br_min, br_max = br_node.min, br_node.max
                    br_mid = (br_min + br_max)/2

                    br = br_node.geometry.transform(translation=(-br_min.x, -br_mid.y, 0))
                    scale = PAR_SCALE*gnmath.min(1, height)
                    tr = (0, mid.y, 0)
                    brackets[i].append(br.transform(translation=tr, scale=(1, scale, 1)))

        # ---------------------------------------------------------------------------
        # Brackets selection

        open  = Mesh.IndexSwitch(*brackets[0], index=code)
        close = Mesh.IndexSwitch(*brackets[1], index=code)

        b_min = open.points.attribute_statistic(nd.position).min
        b_max = b_min.max_
        b_width, b_height, _ = (b_max - b_min).xyz
        b_mid = (b_min + b_max)/2

        # ----- Brackets location

        open.transform(translation=(vmin.x - b_width - X_SPACE, mid.y - b_mid.y, 0))
        close.transform(translation=(vmax.x + X_SPACE, mid.y - b_mid.y, 0))

        # ----- Display or not

        open  = open.switch_false(use_left)
        close = close.switch_false(use_right)

        left_space  = (b_width + X_SPACE).switch_false(use_left)
        right_space = (b_width + X_SPACE).switch_false(use_right)

        (open + close).out()
        left_space.out("Left")
        right_space.out("Right")

    # =============================================================================================================================
    # Formula Compilation
    #
    # Node parameters:
    # - Type in [GEO, GROUP, CONT2, CONT3]
    # - SubType
    #
    # The compilation is made starting from the end.
    # Hence, each node can rely on its sub nodes to build it self
    #
    # Node Type: how to deal with sub nodes
    # - GEO   : a mesh or curve with no sub nodes
    # - GROUP : concat the sub nodes, with an optional parameterless decorator such a brackets, sqrt, arrow, ...
    # - CONT2 : node with 2 sub nodes, fraction for instance
    # - CONT3 : node with 3 sub nodes, for instance exp/indice, Sigma, Integral, ...
    #
    # Node Role: role within the owner
    # - CONTENT 0 : content
    # - PARAM1  1 : first parameter
    # - PARAM2  2 : second parameter
    #
    # Node Para
    #
    # =============================================================================================================================

    with GeoNodes("Compile", prefix=prefix, is_group=True):

        formula = Geometry(name="Formula")
        mesh = formula.mesh
        tree = formula.point_cloud

        with Layout("Delete computed faces"):
            mesh.faces[Boolean("Computed")].delete()
            mesh.faces._Computed = False

        with Layout("Compute Tree explore index"):
            tree = Cloud(GTree.compute_explore(tree))

        with Layout("Prepare exploration for sizing mesh nodes"):
            tree.points._Sized = False
            tree.points[index]._Width  = 0.
            tree.points[index]._Height = 0.
            tree.points[index]._Y0 = 0.
            tree.points[index]._Y1 = 0.

        with Repeat(tree=tree, mesh=mesh, iterations=tree.points.count - 1) as rep:

            tree = rep.tree
            mesh = rep.mesh

            index = rep.iteration + 1
            node_type = tree.points.sample_index(Integer("Node Type"), index=index)

            sized = node_type.equal(0)
            selected = Util.select(mesh + tree, id=index, block=False)
            vmin = selected.min_
            vmax = selected.max_

            mesh.points[Boolean("Selected")].offset(-vmin.x)
            width, height, _ = (vmax - vmin).xyz
            y0, y1 = vmin.y, vmax.y

            tree.points[index]._Sized  = True
            tree.points[index]._Width  = width
            tree.points[index]._Height = height
            tree.points[index]._Y0 = y0
            tree.points[index]._Y1 = y1

            rep.tree = tree
            rep.mesh = mesh



    # -----------------------------------------------------------------------------------------------------------------------------
    # Select mesh faces using the associated tree
    #
    # - Selected : selected faces
    # - Part : integer with -1: before, 0: mid, 1: after

    with GeoNodes("Select", prefix=prefix, is_group=True):

        formula = Geometry(name="Formula")
        with Panel("Block"):
            item_id   = Integer(0, "Id", single_value=True)
            use_block = Boolean(True, "Block")

        mesh = formula.mesh
        tree = formula.point_cloud

        # ----- Delete faces with no 'Item ID'
        mesh = mesh.faces[-Boolean("Item ID").exists_].delete()

        with Layout("Item Id only"):
            single = Mesh(mesh)
            single.faces._Selected = Integer("Item ID").equal(item_id)

        with Layout("Branch Selection"):
            tree = Mesh(GTree.select_branch(tree, index=item_id))

            with Repeat(mesh=mesh, iterations=mesh.faces.count) as rep:
                item_id = rep.mesh.faces.sample_index(Integer("Item ID"), index=rep.iteration)
                rep.mesh.faces[nd.index.equal(rep.iteration)]._Selected = tree.points.sample_index(Boolean("Selected"), index=item_id)

        mesh = single.switch(use_block, rep.mesh)

        with Layout("Part Before, Mid and After"):

            vmin = extract.points[Boolean("Selected")].attribute_statistic(nd.position).min
            vmax = min.max_

            mesh.faces._Part = 0

            sel_before = -Boolean("Selected")
            sel_after  = Boolean(sel_before)

            px = nd.position.x
            sel_before &= px <= vmin.x
            sel_after  &= px >= vmax.x

            mesh.faces[sel_before]._Part = -1
            mesh.faces[sel_after]._Part  = 1

        (mesh + tree).out()
        vmin.out("Min")
        vmax.out("Max")







            item_id = mesh.faces.


            tree = rep.tree
            mesh = rep.mesh

            with Layout("Current Item ID"):
                explore = count - 1 - rep.iteration
                index = tree.points[Integer("Explore").equal(explore)].attribute_statistic(nd.index).min.to_integer()

            with Layout("Select the group"):
                group_sel = Util.select(mesh + tree, id=index, block=True)
                vmin = group_sel.vmin
                vmax = group_sel.vmax
                width = (vmax - vmin).x

            with Layout("Get the term parameters"):
                owner     = rep.tree.points.sample_index(Integer("Owner"),    index=index)

                node_type = rep.tree.points.sample_index(Integer("Type"),     index=index)
                code      = rep.tree.points.sample_index(Integer("Code"),     index=index)
                sub_code  = rep.tree.points.sample_index(Integer("Sub Code"), index=index)

            # ----- 0 : Simply the mesh
            with If(Mesh, node_type) as term:
                l_shift_0  = 0.
                r_shift_0 = width + X_SPACE












        with Layout("Compute the meshes from last to first"):

            count = tree.points.count
            with Repeat(tree=tree, mesh=mesh, iterations=count - 1) as rep:

                tree = rep.tree
                mesh = rep.mesh

                with Layout("Current Item ID"):
                    explore = count - 1 - rep.iteration
                    index = tree.points[Integer("Explore").equal(explore)].attribute_statistic(nd.index).min.to_integer()

                with Layout("Select the group"):
                    group_sel = Util.select(mesh + tree, id=index, block=True)
                    vmin = group_sel.vmin
                    vmax = group_sel.vmax
                    width = (vmax - vmin).x

                with Layout("Get the term parameters"):
                    owner     = rep.tree.points.sample_index(Integer("Owner"),    index=index)

                    node_type = rep.tree.points.sample_index(Integer("Type"),     index=index)
                    code      = rep.tree.points.sample_index(Integer("Code"),     index=index)
                    sub_code  = rep.tree.points.sample_index(Integer("Sub Code"), index=index)

                # ----- 0 : Simply the mesh
                with If(Mesh, node_type) as term:
                    l_shift_0  = 0.
                    r_shift_0 = width + X_SPACE

                # ----- 1 : Accentuation

                with Elif(term):

                    u,0se_left  = sub_code.equal(0) | sub_code.equal(1)
                    use_right = sub_code.equal(0) | sub_code.equal(2)

                    acc = Util.accentuation(code=code, bottom=sub_code.not_equal(0), min=vmin, max=vmax)
                    term_shift_1  = acc.left_
                    right_shift_1 = acc.right_

                    acc = Mesh(acc)
                    acc.faces._Computed = True

                    term.option = acc

                # ----- 2 : Brackets

                with Elif(term):

                    group_sel = Util.select(mesh + tree, id=index, block=True)
                    vmin = group_sel.vmin
                    vmax = group_sel.vmax

                    use_left  = sub_code.equal(0) | sub_code.equal(1)
                    use_right = sub_code.equal(0) | sub_code.equal(2)

                    brs = Util.brackets(code=code, left=use_left, right=use_right, min=vmin, max=vmax)
                    term_shift_2  = brs.left_
                    right_shift_2 = brs.right_

                    brs = Mesh(brs)
                    brs.faces._Computed = True

                    term.option = brs

                # ----------------------------------------------------------------------------------------------------
                # Update mesh

                term.faces._Computed = True

                term_shift  = Float.IndexSwitch(term_shift_0, term_shift_1, term_shift_2, index=node_type)
                right_shift = Float.IndexSwitch(right_shift_0, right_shift_1, right_shift_2, index=node_type)

                mesh[Integer("Explore") >= explore].offset = (term_shift, 0, 0)
                mesh[Integer("Explore") >> explore].offset = (right_shift, 0, 0)



                mesh += term

                rep.tree = tree
                rep.mesh = mesh

        # Place de groups

        with Layout("Place the first level groy"):

            count = tree.points.count
            with Repeat(tree=tree, mesh=mesh, iterations=count - 1) as rep:



















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
