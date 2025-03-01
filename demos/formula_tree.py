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
- creation :   2025/02/25

$ DOC START

> A Tree structure implemented on cloud points

Points index is the node id.
Attribute "Owner" stores the link to node owner
The tree root is index 0 width Owner = -1

The following groups are provided (actual implementation makes use of a prefix)
- New : Add a node to the structure under a given owner
- Index Owner : Get the owner of an index
- Group : group the selection under a new node
- Join : join a branch
- Change Owner : move nodes from one owner to another one
- Insert : insert a new node above or below an existing node
- Select Branch : select a node and sub nodes
- Compute Explore : compute tree parameters (order, depth, explore)

[Source Code](../demos/forest.py)

Animated formula

IN PROGRESS

``` python
from geonodes.demos import formula

formula.demo()
```
"""

from geonodes import *

# Insertion locations

LOC_LAST_CHILD  = 0 # As last child of the targer
LOC_AFTER       = 1 # After the target
LOC_BEFORE      = 2 # Before the target
LOC_FIRST_CHILD = 3 # As first child

def build_tree(prefix='Tree'):

    GTree = G(prefix)

    NODE_ATTRS = ["ID", "Owner", "Depth", "Order", "Total", "Explore"]
    MACRO_COLOR = (.1, .1, .1)


    # ====================================================================================================
    # Macros

    # ----------------------------------------------------------------------------------------------------
    # Index of id

    def macro_id_index(tree, node_id):

        with Layout("Index of ID"):
            return tree.points[Integer("ID").equal(node_id)].attribute_statistic(nd.index).min.to_integer()._lc("Index")

    # ----------------------------------------------------------------------------------------------------
    # Index of Explore

    def macro_explore_index(tree, explore):

        with Layout("Index of ID"):
            return tree.points[Integer("Explore").equal(explore)].attribute_statistic(nd.index).min.to_integer()._lc("Index")

    # ----------------------------------------------------------------------------------------------------
    # Get attribute

    def macro_get_attr(tree, index, name):

        return tree.points.sample_index(Integer(name), index=index)._lc(name)

    # ----------------------------------------------------------------------------------------------------
    # Empty Tree

    def macro_create(tree):

        with Layout("Create an empty tree structure", color=MACRO_COLOR):
            empty = Cloud.Points(1)
            empty.points._ID      = 0
            empty.points._Owner   = -1
            empty.points._Depth   = 0
            empty.points._Order   = 0
            empty.points._Total   = 0
            empty.points._Explore = 0

            count = tree.points.count

            return tree.switch(count.equal(0), empty)

    # ----------------------------------------------------------------------------------------------------
    # Max Id

    def macro_max_id(tree):

        return tree.points.attribute_statistic(Integer("ID")).max.to_integer()._lc("Max ID")

    # ----------------------------------------------------------------------------------------------------
    # Number of children

    def macro_children_count(tree, node_id):

        with Layout("Children Count", color=MACRO_COLOR):

            return Cloud(Cloud(tree).points[Integer("Owner").equal(node_id)].separate()).points.count._lc("Children")

    # ----------------------------------------------------------------------------------------------------
    # Update total : from node_id to root

    def macro_update_total(tree, node_id, delta):

        with Layout("Update total", color=MACRO_COLOR):

            node_index = macro_id_index(tree, node_id)
            depth = macro_get_attr(tree, node_index, "Depth")

            with Repeat(tree=tree, node_id=node_id, node_index=node_index, iterations=depth + 1) as rep:

                tree = rep.tree

                tree.points[nd.index.equal(rep.node_index)]._Total = Integer("Total") + delta

                owner_id = macro_get_attr(tree, rep.node_index, "Owner")
                owner_index = macro_id_index(tree, owner_id)

                rep.tree       = tree
                rep.node_id    = owner_id
                rep.node_index = owner_index

            return rep.tree

    def macro_change_id(tree, old_id, new_id):

        with Layout("Change ID", color=MACRO_COLOR):

            tree = Cloud(tree)

            tree.points[Integer("ID").equal(old_id)]._ID = new_id
            tree.points[Integer("Owner").equal(old_id)]._Owner = new_id

            return tree

    # ====================================================================================================
    # Groups

    # ----------------------------------------------------------------------------------------------------
    # Node information from index, ID or Explore
    # ----------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------------
    # Node info : From Index

    with GeoNodes("Index Info", prefix=prefix, is_group=True):

        tree  = Cloud(None, "Tree")
        index = Integer(1, "Index", single_value=True)

        index.out("Index")
        for name in NODE_ATTRS:
            tree.points.sample_index(Integer(name), index=index).out(name)

    # ----------------------------------------------------------------------------------------------------
    # Node info : From ID

    with GeoNodes("ID Info", prefix=prefix, is_group=True):

        tree    = Cloud(None, "Tree")
        node_id = Integer(1, "ID", single_value=True)

        index = macro_id_index(tree, node_id)
        GTree.index_info(tree, index=index).node.out()

    # ----------------------------------------------------------------------------------------------------
    # Node info : From Explore

    with GeoNodes("Explore Info", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")
        expl = Integer(1, "Explore", single_value=True)

        index = macro_explore_index(tree, expl)
        GTree.index_info(tree, index=index).node.out()

    # ----------------------------------------------------------------------------------------------------
    # Attach a branch
    # ----------------------------------------------------------------------------------------------------
    #                                 Location
    # Tree                Last child    After       Before
    # - ID                    .           .           .
    # - Owner                 .           .           .
    # - Depth                 .           .           .
    # - Order                 .        siblings    siblings
    # - Total               owners      owners      owners
    # - Explore               X           X           X
    #
    # Branch
    # - ID                   root        root       root
    # - Owner                root        root       root
    # - Depth                all         all        all
    # - Order                root        root       root
    # - Total                 .           .           .
    # - Explore              all         all        all

    with GeoNodes("Attach", prefix = prefix, is_group=True):

        tree      = Cloud(None, "Tree")
        branch    = Cloud(None, "Branch")

        node_id   = Integer(0, "ID")
        location  = Integer(0, "Location", 0, 3)
        shift_ids = Boolean(True, "Shift IDs")

        tree   = macro_create(tree)
        branch = macro_create(branch)

        tree_max_id   = macro_max_id(tree)
        branch_max_id = macro_max_id(branch)

        # ----- Target Tree Info

        with Layout("'First child' is transformed in 'Last Child' if no child"):
            count = macro_children_count(tree, node_id)
            location = location.switch(location.equal(LOC_FIRST_CHILD) & count.equal(0), LOC_LAST_CHILD)

        with Layout("'First child' is transformed in 'Before Id' if children"):

            to_before = location.equal(LOC_FIRST_CHILD)
            first_point = Cloud(tree).points[Integer("Owner").equal(node_id) & Integer("Order").equal(0)].separate()
            first_id = Cloud(first_point).points.sample_index(Integer("ID"), index=0)

            node_id  = node_id.switch(to_before, first_id)
            location = location.switch(to_before, LOC_BEFORE)

        # ------ Node info

        id_info    = GTree.id_info(tree, node_id).node
        #owner_info = GTree.id_info(tree, id_info.owner).node

        # ----- Branch Info

        branch_info = GTree.id_info(branch, 0).node

        # ----- Shift IDS

        new_id = (tree_max_id + 1).switch(shift_ids, tree_max_id + branch_max_id + 1)

        with Layout("Shift IDS"):
            shifted = Cloud(branch)
            shifted.points[Integer("Depth") > 0]._ID    = Integer("ID")    + tree_max_id
            shifted.points[Integer("Depth") > 1]._Owner = Integer("Owner") + tree_max_id

            branch = branch.switch(shift_ids, shifted)

        # --------------------------------------------------------------------------------
        # Below the target
        # --------------------------------------------------------------------------------

        with Layout("Below the target"):

            explore0  = id_info.explore + id_info.total + 1
            total_id0 = node_id
            sibling0  = Boolean(False)

            root_owner0 = node_id
            root_order0 = macro_children_count(tree, node_id)
            root_depth0 = id_info.depth + 1

        # --------------------------------------------------------------------------------
        # After the target
        # --------------------------------------------------------------------------------

        with Layout("After the target"):

            explore1  = id_info.explore + id_info.total + 1
            total_id1 = id_info.owner
            sibling1  = Integer("Owner").equal(id_info.owner) & (Integer("Order") > id_info.order)

            root_owner1 = id_info.owner
            root_order1 = id_info.order + 1
            root_depth1 = id_info.depth

        # --------------------------------------------------------------------------------
        # Before the target
        # --------------------------------------------------------------------------------

        with Layout("Before the target"):

            explore2  = id_info.explore
            total_id2 = id_info.owner
            sibling2  = Integer("Owner").equal(id_info.owner) & (Integer("Order") >= id_info.order)

            root_owner2 = id_info.owner
            root_order2 = id_info.order
            root_depth2 = id_info.depth

        # --------------------------------------------------------------------------------
        # Tree Update
        # --------------------------------------------------------------------------------

        with Layout("Tree Update"):

            explore  = Integer.IndexSwitch(explore0,  explore1,  explore2,  index=location)
            total_id = Integer.IndexSwitch(total_id0, total_id1, total_id2, index=location)
            sibling  = Boolean.IndexSwitch(sibling0,  sibling1,  sibling2,  index=location)

            # Increase the total in the hierarchy of owners
            tree = macro_update_total(tree, total_id, branch_info.total + 1)

            # Shift Explore indices after explore index
            tree.points[Integer("Explore") >= explore]._Explore += branch_info.total + 1

            # Shift Sibling
            tree.points[sibling]._Order = Integer("Order") + 1

        # --------------------------------------------------------------------------------
        # Branch Update
        # --------------------------------------------------------------------------------

        with Layout("Branch Update"):

            sel_root   = Integer("ID").equal(0)
            sel_depth1 = Integer("Depth").equal(1)

            root_owner  = Integer.IndexSwitch(root_owner0,  root_owner1,  root_owner2, index=location)
            root_order  = Integer.IndexSwitch(root_order0,  root_order1,  root_order2, index=location)
            root_depth  = Integer.IndexSwitch(root_depth0,  root_depth1,  root_depth2, index=location)

            branch.points[sel_root]._Owner   = root_owner
            branch.points[sel_depth1]._Owner = new_id
            branch.points[sel_root]._Order   = root_order
            branch.points._Depth             = Integer("Depth") + root_depth
            branch.points._Explore           = Integer("Explore") + explore

            # Last because sel_root is ID == 0
            branch[sel_root].points._ID = new_id

        # ----------------------------------------------------------------------------------------------------
        # Done

        index = tree.points.count
        tree += branch

        tree.out("Tree")
        new_id.out("ID")
        index.out("Index")

    # ----------------------------------------------------------------------------------------------------
    # Add a node

    with GeoNodes("New", prefix = prefix, is_group=True):

        tree = Cloud(None, "Tree")

        node_id  = Integer(0, "ID")
        location = Integer(0, "Location", 0, 3)

        node = GTree.attach(tree, id=node_id, location=location, shift_ids=True).node
        node.out()

    # ----------------------------------------------------------------------------------------------------
    # Detach
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Detach", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")

        node_id = Integer(1, "ID")

        id_info = GTree.id_info(tree, node_id).node

        with Layout("Explore range to extract"):
            ex0   = id_info.explore
            count = id_info.total + 1
            ex1   = ex0 + count

        with Layout("Separate the branch"):
            tree = Cloud(tree.points[(Integer("Explore") < ex0) | (Integer("Explore") >= ex1)].separate())
            branch = Cloud(tree.inverted_)

        with Layout("Update main tree"):
            tree.points[Integer("Explore") >= ex1]._Explore = Integer("Explore") - count
            tree = macro_update_total(tree, id_info.owner, -count)
            tree.points[Integer("Owner").equal(id_info.owner) & (Integer("Order") > id_info.order)]._Order = Integer("Order") - 1

        with Layout("Make branch consistent"):
            branch.points._Depth                 = Integer("Depth") - id_info.depth
            branch.points._Explore               = Integer("Explore") - id_info.explore
            branch.points[Integer("ID").equal(node_id)]._ID  = 0
            branch.points[Integer("ID").equal(0)]._Order = 0
            branch.points[Integer("Owner").equal(node_id)]._Owner = 0

        tree.out("Tree")
        branch.out("Branch")

    # ----------------------------------------------------------------------------------------------------
    # Move
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Move", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")

        node_id = Integer(1, "ID")
        to_id   = Integer(1, "To ID")
        location = Integer(0, "Location", 0, 3)

        tree = GTree.detach(tree, id=node_id)
        branch = tree.branch_

        tree = GTree.attach(tree, branch=branch, id=to_id, location=location, shift_ids=False)
        branch_id = tree.id_

        tree = macro_change_id(tree, old_id=branch_id, new_id = node_id)

        tree.out("Tree")

    # ----------------------------------------------------------------------------------------------------
    # Group
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Group", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")

        selection = Boolean(False, "Selection", hide_value=True)

        with Layout("Get minimum Depth"):
            depth = tree.points[selection].attribute_statistic(Integer("Depth")).min.to_integer()
            selection &= Integer("Depth").equal(depth)

        with Layout("Same owner"):
            sel_tree = Cloud(tree).points[selection].separate()
            owner = sel_tree.points.sample_index(Integer("Owner"), index=0)
            selection &= Integer("Owner").equal(owner)

            to_group = Cloud(tree).points[selection].separate()

        with Layout("Create a new id within the owner"):
            new_tree = GTree.new(tree, owner)
            new_id = new_tree.id_

        with Repeat(tree=new_tree, iterations=to_group.points.count) as rep:

            child_id = to_group.points.sample_index(Integer("ID"))
            rep.tree = GTree.move(rep.tree, id=child_id, to_id=new_id, location=0)

        with Layout("No New id if nothing to group"):
            ok = to_group.points.count > 0
            tree = tree.switch(ok, rep.tree)

        tree.out("Tree")
        new_id.out("Id")
        ok.out("Valid")


    # ====================================================================================================
    # Selection
    # ====================================================================================================

    with GeoNodes("Select", prefix=prefix, is_group=True):

        tree    = Cloud(None, "Tree")
        node_id = Integer(1, "ID")

        sel_mode = Integer.MenuSwitch({'Branch': 0, 'Children': 1, 'Single': 2}, menu='Branch', name="Mode")

        id_info = GTree.id_info(tree, id=node_id).node

        ex0 = id_info.explore
        ex1 = ex0 + id_info.total + 1

        expl = Integer("Explore")

        with If(Boolean, sel_mode) as selection:

            selection.option = (expl >= ex0) & (expl < ex1)

        with Elif(selection):

            selection.option = (expl > ex0) & (expl < ex1)

        with Elif(selection):

            selection.option = expl.equal(ex0)

        selection.out("Selection")

    # ====================================================================================================
    # Set Explore attribute on a domain
    # - Domain are supposed to have an 'Item ID' attribute pointing to a Tree Node
    # - This Group update the 'Explore' attribute to ease selection in the domain
    # ====================================================================================================

    with GeoNodes("Allow Selection", prefix=prefix, is_group=True):

        geo  = Geometry()

        tree = Cloud(None, "Tree")

        with Repeat(geo=geo, tree=tree, iterations=tree.points.count) as rep:
            node_id = rep.tree.points.sample_index(Integer("ID"), index=rep.iteration)
            explore = rep.tree.points.sample_index(Integer("Explore"), index=rep.iteration)

            with If(Geometry, 'Point', name='Domain') as mapped:
                mesh  = Mesh(rep.geo)
                mesh.points[Integer("Item ID").equal(node_id)]._Explore = explore
                mapped.option = mesh

            with Elif(mapped, 'Face'):
                mesh  = Mesh(rep.geo)
                mesh.faces[Integer("Item ID").equal(node_id)]._Explore = explore
                mapped.option = mesh

            with Elif(mapped, 'Edge'):
                mesh  = Mesh(rep.geo)
                mesh.edges[Integer("Item ID").equal(node_id)]._Explore = explore
                mapped.option = mesh

            with Elif(mapped, 'Spline'):
                curve  = Curve(rep.geo)
                curve.splines[Integer("Item ID").equal(node_id)]._Explore = explore
                mapped.option = curve

            with Elif(mapped, 'Instance'):
                inst  = Instances(rep.geo)
                inst.insts[Integer("Item ID").equal(node_id)]._Explore = explore
                mapped.option = inst

            rep.geo = mapped

        rep.geo.out()

    # ====================================================================================================
    # Navigation
    # ====================================================================================================

    with GeoNodes("Selection Info", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")
        selection = Boolean(False, "Selection", hide_value=True)

        sel_tree = tree.points[selection].separate()
        ok = sel_tree.points.count.equal(1)

        sel_id = sel_tree.points.sample_index(Integer("ID"), index=0)
        sel_id = sel_id.switch_false(ok, -1)

        GTree.id_info(tree, sel_id).node.out()
        ok.out("Exists")

    with GeoNodes("Children Count", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")
        node_id = Integer(0, "Id", single_value=True)

        count = macro_children_count(tree, node_id)
        count.out("Count")
        count.equal(0).out("Empty")

    with GeoNodes("Get Child", prefix=prefix, is_group=True):

        tree = Cloud(None, "Tree")
        node_id = Integer(0, "Id", single_value=True)
        order   = Integer(0, "Order", single_value=True)

        GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Order").equal(order)).node.out()



    # ====================================================================================================
    # Dump
    # ====================================================================================================

    with ShaderNodes("Dump Mat"):
        fac = snd.attribute("Selected").fac
        col = Color((1, 1, 1)).mix((1, 0, 0), fac)
        ped = Shader.Principled(base_color=col)
        ped.out()

    with GeoNodes("Dump", prefix=prefix):

        tree = Cloud(None, "Tree")
        use_labels = Boolean(True, "Labels")
        selection = Boolean(False, "Selection")

        # ----------------------------------------------------------------------------------------------------
        # Compute positions

        with Repeat(tree=tree, y=0, iterations=tree.points.count) as rep:

            info = GTree.explore_info(rep.tree, explore=rep.iteration).node

            x = info.depth
            y = rep.y.switch(info.order.not_equal(0), rep.y - 1)

            rep.tree[nd.index.equal(info.index)].position = (x, y, 0)
            rep.y = y

        tree = rep.tree

        # ----- Labels

        with tree.points.for_each(item_id=Integer("ID"), owner=Integer("Owner"), pos=nd.position, sel=selection) as feel:

            s = feel.item_id.to_string() + " [" + feel.owner.to_string() + "]"
            curves = s.to_curves(size=.3).realize()
            labels = Curve(curves).fill()

            labels.transform(translation=feel.pos)
            labels.faces._Color = Color((1, 1, 1)).switch(feel.sel, (1, 0, 0))

            feel.generated.geometry = labels

        labels = feel.generated.geometry
        labels.set_material("Dump Mat")

        tree = tree.switch(use_labels, labels)

        tree.out()
