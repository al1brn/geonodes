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
            new_cloud = Cloud(tree)
            new_cloud.points._Index = nd.index
            new_cloud.points[Integer("ID").equal(node_id)].separate()
            new_cloud = Cloud(new_cloud)
            exists = new_cloud.points.count.equal(1)._lc("Exists")
            index = new_cloud.points.sample_index(Integer("Index"), index=0).switch_false(exists, -1)

            return index, exists


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
    # Empty tree

    def macro_is_empty(tree):
        return tree.points.count.equal(0)._lc("Empty")

    # ----------------------------------------------------------------------------------------------------
    # Max Id

    def macro_max_id(tree):

        with Layout("Tree Max ID"):
            empty = macro_is_empty(tree)
            max_id = tree.points.attribute_statistic(Integer("ID")).max.to_integer()
            max_id = max_id.switch(empty, -1)._lc("Max ID")

            return max_id

    # ----------------------------------------------------------------------------------------------------
    # Number of children

    def macro_children_count(tree, node_id):

        with Layout("Children Count", color=MACRO_COLOR):

            return Cloud(Cloud(tree).points[Integer("Owner").equal(node_id)].separate()).points.count._lc("Children")

    # ----------------------------------------------------------------------------------------------------
    # Update total : from node_id to root

    def macro_update_total(tree, node_id, delta):

        with Layout("Update total", color=MACRO_COLOR):

            node_index, node_exists = macro_id_index(tree, node_id)
            depth = macro_get_attr(tree, node_index, "Depth")

            with Repeat(tree=tree, node_id=node_id, node_index=node_index, iterations=depth + 1) as rep:

                tree = rep.tree

                tree.points[nd.index.equal(rep.node_index)]._Total = Integer("Total") + delta

                owner_id = macro_get_attr(tree, rep.node_index, "Owner")
                owner_index, _ = macro_id_index(tree, owner_id)

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
    # Dump
    # ====================================================================================================

    with ShaderNodes("Dump Mat"):
        fac = snd.attribute("Selected").fac
        col = Color((1, 1, 1)).mix((1, 0, 0), fac)
        ped = Shader.Principled(base_color=col)
        ped.out()

    with GeoNodes("Dump", prefix=prefix):

        geo = Geometry()
        use_labels = Boolean(True, "Labels")
        selection = Boolean(False, "Selection")

        tree = geo.point_cloud

        # ----------------------------------------------------------------------------------------------------
        # Compute positions


        tree.points._Index = nd.index
        with Repeat(tree=tree, y=0, iterations=tree.points.count) as rep:

            #info = GTree.explore_info(rep.tree, explore=rep.iteration).node
            sel_node = Cloud(rep.tree).points[Integer("Explore").equal(rep.iteration)].separate()
            sel_node = Cloud(sel_node)

            x          = sel_node.points.sample_index(Integer("Depth"), index=0)
            node_order = sel_node.points.sample_index(Integer("Order"), index=0)
            node_index = sel_node.points.sample_index(Integer("Index"), index=0)

            #x = info.depth
            y = rep.y.switch(node_order.not_equal(0), rep.y - 1)

            rep.tree[nd.index.equal(node_index)].position = (x, y, 0)
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

    # ====================================================================================================
    # Groups
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Node information from index, ID or Explore
    # ----------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------------
    # Node info : From Index

    with GeoNodes("Index Info", prefix=prefix, is_group=True):
        """ Get the node information from its index

        Arguments
        ---------
        - Tree (Cloud)
        - Index (Integer) : point index

        Returns
        -------
        - Index (Integer)
        - ID : (Integer)
        - Owner (Integer)
        - Depth (Integer)
        - Order (Integer)
        - Total (Integer)
        - Explore (Integer)
        - Exists (Boolean) : False if the index is not valid
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree  = Cloud(None, "Tree")
        index = Integer(1, "Index", single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        ko = (index < 0) | (index >= tree.points.count)

        index.out("Index")
        for name in NODE_ATTRS:
            tree.points.sample_index(Integer(name), index=index).switch(ko, -1).out(name)

        (-ko).out("Exists")

    # ----------------------------------------------------------------------------------------------------
    # Node info : From ID

    with GeoNodes("ID Info", prefix=prefix, is_group=True):
        """ Get the node information from its ID

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer) : point ID

        Returns
        -------
        - Index (Integer)
        - ID : (Integer)
        - Owner (Integer)
        - Depth (Integer)
        - Order (Integer)
        - Total (Integer)
        - Explore (Integer)
        - Exists (Boolean) : False if the ID is not valid
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree    = Cloud(None, "Tree")
        node_id = Integer(1, "ID", single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        index, _ = macro_id_index(tree, node_id)
        GTree.index_info(tree, index=index).node.out()

    # ----------------------------------------------------------------------------------------------------
    # Node info : From Explore

    with GeoNodes("Explore Info", prefix=prefix, is_group=True):
        """ Get the node information from its exploration index

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer) : point ID

        Returns
        -------
        - Index (Integer)
        - ID : (Integer)
        - Owner (Integer)
        - Depth (Integer)
        - Order (Integer)
        - Total (Integer)
        - Explore (Integer)
        - Exists (Boolean) : False if the exploration index is not valid
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree = Cloud(None, "Tree")
        expl = Integer(1, "Explore", single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        index = macro_explore_index(tree, expl)
        GTree.index_info(tree, index=index).node.out()

    # ----------------------------------------------------------------------------------------------------
    # Node info : From Selection

    with GeoNodes("Selection Info", prefix=prefix, is_group=True):
        """ Get the node information from selection in the tree

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer) : point ID

        Returns
        -------
        - Index (Integer)
        - ID : (Integer)
        - Owner (Integer)
        - Depth (Integer)
        - Order (Integer)
        - Total (Integer)
        - Explore (Integer)
        - Exists (Boolean) : False if the number of selected points is not equal to 1
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree = Cloud(None, "Tree")
        selection = Boolean(False, "Selection", hide_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        sel_tree = Cloud(tree).points[selection].separate()
        ok = sel_tree.points.count.equal(1)

        sel_id = sel_tree.points.sample_index(Integer("ID"), index=0)
        sel_id = sel_id.switch_false(ok, -1)

        GTree.id_info(tree, sel_id).node.out()

    # ====================================================================================================
    # Children
    # ====================================================================================================

    with GeoNodes("Children Count", prefix=prefix, is_group=True):
        """ Count the number of children

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer)

        Returns
        -------
        - Count (Integer) : number of children
        - Empty (Boolean) : if no child (i.e. `count.equal(0)`)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree    = Cloud(None,   "Tree")
        node_id = Integer(0,    "ID", single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        count = macro_children_count(tree, node_id)
        count.out("Count")
        count.equal(0).out("Empty")

    with GeoNodes("Get Child", prefix=prefix, is_group=True):
        """ Get information on a child by its order

        > [!NOTE]
        > As for a list, the order can be given from the last using a negative order

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer)
        - Order (Integer) : order of the child, from last one if negative

        Returns
        -------
        - Count (Integer) : number of children
        - Empty (Boolean) : if no child (i.e. `count.equal(0)`)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree    = Cloud(None,   "Tree")
        node_id = Integer(0,    "ID", single_value=True)
        order   = Integer(0,    "Order", single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        count = macro_children_count(tree, node_id)
        order = order.switch(order < 0, count + order)

        GTree.selection_info(tree, Integer("Owner").equal(node_id) & Integer("Order").equal(order)).node.out()

    # ====================================================================================================
    # Update the Total of the owner starting from a node
    # ====================================================================================================

    with GeoNodes("Update Total", prefix=prefix, is_group=True):

        tree    = Cloud(None, "Tree")
        node_id = Integer(0, "ID")
        incr    = Integer(0, "Increment")

        tree_init = Cloud(tree)

        id_info = GTree.id_info(tree, node_id).node
        depth = id_info.depth
        with Repeat(tree=tree, node_id=node_id, iterations=depth + 1) as rep:

            rep.tree.points[Integer("ID").equal(rep.node_id)]._Total = Integer("Total") + incr
            rep.node_id = GTree.id_info(rep.tree, rep.node_id).owner_

        tree = rep.tree
        tree_init.switch(id_info.exists, tree).out("Points")


    # ====================================================================================================
    # Selection
    # ====================================================================================================

    with GeoNodes("Select", prefix=prefix, is_group=True):
        """ Compute selection from an ID

        The 'Mode' menu socket defines what must be selected:
        - Branch : the node and all its sub nodes
        - Children : all the sub nodes but not the node itssel
        - Direct : the direct children
        - Single : The node only (equivalent to `Integer("ID").equal(node_id)`)

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer) : node ID
        - Mode (Menu) : what to select

        Returns
        -------
        - Selection (Boolean)
        """
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree    = Cloud(None, "Tree")
        node_id = Integer(1, "ID")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        sel_mode = Integer.MenuSwitch({'Branch': 0, 'Children': 1, 'Direct': 2, 'Single': 3}, menu='Branch', name="Mode")

        id_info = GTree.id_info(tree, id=node_id).node

        ex0 = id_info.explore
        ex1 = ex0 + id_info.total + 1

        expl = Integer("Explore")

        # ----- Branch
        with If(Boolean, sel_mode) as selection:
            selection.option = (expl >= ex0) & (expl < ex1)

        # ----- Children
        with Elif(selection):
            selection.option = (expl > ex0) & (expl < ex1)

        # ----- Direct
        with Elif(selection):
            selection.option = Integer("Owner").equal(node_id)

        # ----- Single
        with Elif(selection):
            selection.option = expl.equal(ex0)

        selection.out("Selection")

    # ----------------------------------------------------------------------------------------------------
    # Dissolve
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Dissolve", prefix=prefix, is_group=True):
        """ Rattach the children to the owner of the id, and delete the node

        Attributes
        - ID      : no change
        - Total   : -1 for the Owners
        - Explore : -1 for next Explore
        - Owner   : change the direct children
        - Order   : +1 for the following siblings
        - Depth   : -1 for all children

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer)

        Returns
        -------
        - Points (Cloud)
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree = Cloud(None, "Tree")
        node_id = Integer(1, "ID")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        id_info = GTree.id_info(tree, node_id).node
        owner_id = id_info.owner

        children_count = macro_children_count(tree, node_id)

        # ----------------------------------------------------------------------------------------------------
        # Can't dissolve root node if children_count != 1

        keep_tree = owner_id.equal(-1) & children_count.not_equal(1)
        tree_init = Cloud(tree)

        # ----------------------------------------------------------------------------------------------------
        # -1 for the owners

        tree = GTree.update_total(tree, id_info.owner, -1)

        # ----------------------------------------------------------------------------------------------------
        # Push next siblings

        tree.points[Integer("Owner").equal(id_info.owner) & (Integer("Order") > id_info.order)]._Order = Integer("Order") + children_count - 1

        # ----------------------------------------------------------------------------------------------------
        # Update children owner and order

        tree.points[Integer("Owner").equal(node_id)]._Order = Integer("Order") + id_info.order
        tree.points[Integer("Owner").equal(node_id)]._Owner = id_info.owner

        # ----------------------------------------------------------------------------------------------------
        # Update children depth

        sel = (Integer("Explore") > id_info.explore) & (Integer("Explore") <= id_info.explore + id_info.total)
        tree.points[sel]._Depth = Integer("Depth") - 1

        # ----------------------------------------------------------------------------------------------------
        # Update explore

        tree.points[Integer("Explore") > id_info.explore]._Explore = Integer("Explore") - 1

        # ----------------------------------------------------------------------------------------------------
        # We can delete the points

        tree.points[Integer("ID").equal(node_id)].delete()

        tree = tree.switch(keep_tree, tree_init)
        keep_tree.error("Trying to dissolve root")

        tree.out("Points")

    # ----------------------------------------------------------------------------------------------------
    # Insert an owner to a node
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Insert Owner", prefix=prefix, is_group=True):
        """ Insert an owner to a node

        Attributes
                    Created Group      Node         Other
        - ID      : new ID             .            .
        - Total   : node total + 1     .            +1 for owners
        - Explore : node explore       (+1)  <==    +1 for >= Explore
        - Owner   : node owner         new Group    .
        - Order   : node order         0            .
        - Depth   : node depth         (+1)  <==    +1 for branch

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer)

        Returns
        -------
        - Points (Cloud)
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree = Cloud(None, "Tree")
        node_id = Integer(1, "ID")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        id_info = GTree.id_info(tree, node_id).node
        owner_id = id_info.owner

        children_count = macro_children_count(tree, node_id)

        # ----------------------------------------------------------------------------------------------------
        # New group

        with Layout("New Group"):
            new_id = macro_max_id(tree) + 1
            new_group = Cloud.Points(1)
            new_group.points._ID      = new_id
            new_group.points._Total   = id_info.total + 1
            new_group.points._Explore = id_info.explore
            new_group.points._Owner   = id_info.owner
            new_group.points._Order   = id_info.order
            new_group.points._Depth   = id_info.depth

        # ----------------------------------------------------------------------------------------------------
        # Node

        with Layout("Update node"):
            node_sel = Integer("ID").equal(node_id)

            tree.points[node_sel]._Owner = new_id
            tree.points[node_sel]._Order = 0

        # ----------------------------------------------------------------------------------------------------
        # Othe nodes changes

        with Layout("Other nodes changes"):

            tree.points[GTree.select(tree, id=node_id, mode='Branch')]._Depth = Integer("Depth") + 1
            tree = GTree.update_total(tree, id_info.owner, 1)
            tree.points[Integer("Explore")>= id_info.explore]._Explore = Integer("Explore") + 1

        # ----------------------------------------------------------------------------------------------------
        # Done

        (tree + new_group).out("Points")
        new_id.out("Id")

    # ----------------------------------------------------------------------------------------------------
    # Group the children of a node
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Group Children", prefix=prefix, is_group=True):
        """ Group the children of a node

        Similar to "Insert Owner" but this last group doesn't apply to nodes of depth 1.

        Attributes
                    Created Group      Node         Other
        - ID      : new ID             .            .
        - Total   : node total         (+1)         +1 for owners starting from node
        - Explore : node explore + 1   .            +1 for > Explore
        - Owner   : node ID            .            direct children to new ID
        - Order   : 0                  .            .
        - Depth   : node depth + 1     .            +1 for branch

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer)
        - Force (Boolean) : group the children even if there is only one child

        Returns
        -------
        - Points (Cloud)
        - ID (Integer) : ID of the node grouping the children
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree    = Cloud(None, "Tree")
        node_id = Integer(1, "ID")
        force   = Boolean(False, "Force") # Do it event if more than 1 child

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("How many children"):
            id_info = GTree.id_info(tree, node_id).node
            count = macro_children_count(tree, node_id)

            do_it = force | (count > 1)
            tree_init = tree

            child_id = GTree.selection_info(tree, Integer("Owner").equal(node_id)).id_

        # ----------------------------------------------------------------------------------------------------
        # New group

        with Layout("New Group"):
            new_id = macro_max_id(tree) + 1
            new_group = Cloud.Points(1)
            new_group.points._ID      = new_id
            new_group.points._Total   = id_info.total
            new_group.points._Explore = id_info.explore + 1
            new_group.points._Owner   = node_id
            new_group.points._Order   = 0
            new_group.points._Depth   = id_info.depth + 1

        # ----------------------------------------------------------------------------------------------------
        # Node

        with Layout("Update owners from node itself"):
            tree = GTree.update_total(tree, node_id, 1)

        # ----------------------------------------------------------------------------------------------------
        # Other nodes changes

        with Layout("Other nodes changes"):

            tree.points[GTree.select(tree, id=node_id, mode='Children')]._Depth = Integer("Depth") + 1
            tree.points[Integer("Explore") > id_info.explore]._Explore = Integer("Explore") + 1
            tree.points[Integer("Owner").equal(node_id)]._Owner = new_id

        # ----------------------------------------------------------------------------------------------------
        # Done

        tree = tree_init.switch(do_it, tree + new_group)
        new_id = child_id.switch(do_it, new_id)

        tree.out("Points")
        new_id.out("ID")

    # ====================================================================================================
    # Attach a branch
    # ====================================================================================================

    with GeoNodes("Attach", prefix = prefix, is_group=True):
        """

        The location can be:
        - 0 : Last child
        - 1 : After
        - 2 : Before
        - 3 : First child (implemented as "before first child")

                                        Location
        Tree                Last child    After       Before
        - ID                    .           .           .
        - Owner                 .           .           .
        - Depth                 .           .           .
        - Order                 .        siblings    siblings
        - Total               owners      owners      owners
        - Explore               X           X           X

        Branch
        - ID                   root        root       root
        - Owner                root        root       root
        - Depth                all         all        all
        - Order                root        root       root
        - Total                 .           .           .
        - Explore              all         all        all

        Arguments
        ---------
        - Tree (Cloud)
        - Branch (Cloud)
        - ID (Integer) : ID of the node where to attache the branch
        - Location (Integer) : where to attach the new branch

        Returns
        -------
        - Points (Cloud)
        - ID (Integer) : ID of top node of the attached branch
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree      = Cloud(None,     "Tree")
        branch    = Cloud(None,     "Branch")

        node_id   = Integer(0,      "ID")
        location  = Integer(0,      "Location", 0, 3)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


        with Layout("Preparation"):
            tree_init    = Cloud(tree)
            branch_init  = Cloud(branch)
            empty_tree   = macro_is_empty(tree)
            empty_branch = macro_is_empty(branch)

            tree_max_id   = macro_max_id(tree)
            branch_max_id = macro_max_id(branch)

        # ----- Target Tree Info

        with Layout("'First child' is transformed in 'Last Child' if no child"):
            count = macro_children_count(tree, node_id)
            location = location.switch(location.equal(LOC_FIRST_CHILD) & count.equal(0), LOC_LAST_CHILD)

        with Layout("'First child' is transformed in 'Before' if children"):
            first_id = GTree.get_child(tree, node_id, 0).id_
            to_before = location.equal(LOC_FIRST_CHILD)

            node_id  = node_id.switch(to_before, first_id)
            location = location.switch(to_before, LOC_BEFORE)

        # ------ Node info

        id_info = GTree.id_info(tree, node_id).node

        # ----- Branch Info

        branch_info = GTree.selection_info(branch, Integer("Owner").equal(-1)).node

        shift_id = gnmath.imax(tree_max_id, branch_max_id) + 1
        with Layout("Shift IDs when necessary"):

            with Repeat(branch=branch, owner=Integer("Owner"), iterations=branch.points.count) as rep:

                cur_id    = rep.branch.points.sample_index(Integer("ID"), index=rep.iteration)
                cur_owner = rep.branch.points.sample_index(Integer("Owner"), index=rep.iteration)

                repl_id = cur_id + shift_id.switch_false(GTree.id_info(tree, cur_id).exists_)
                rep.branch.points[rep.iteration]._ID = repl_id

                repl_owner = cur_owner + shift_id.switch_false(GTree.id_info(tree, cur_owner).exists_)
                rep.branch.points[rep.iteration]._Owner = repl_owner

            branch = rep.branch

        # ----- New ID of branch root

        new_id = GTree.selection_info(branch, Integer("Owner").equal(-1)).id_

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
            tree = GTree.update_total(tree, total_id, branch_info.total + 1)

            # Shift Explore indices after explore index
            tree.points[Integer("Explore") >= explore]._Explore = Integer("Explore") + branch_info.total + 1

            # Shift Sibling
            tree.points[sibling]._Order = Integer("Order") + 1

        # --------------------------------------------------------------------------------
        # Branch Update
        # --------------------------------------------------------------------------------

        with Layout("Branch Update"):

            sel_root   = Integer("ID").equal(new_id)
            sel_depth1 = Integer("Depth").equal(1)

            root_owner  = Integer.IndexSwitch(root_owner0,  root_owner1,  root_owner2, index=location)
            root_order  = Integer.IndexSwitch(root_order0,  root_order1,  root_order2, index=location)
            root_depth  = Integer.IndexSwitch(root_depth0,  root_depth1,  root_depth2, index=location)

            branch.points[sel_root]._Owner   = root_owner
            branch.points[sel_depth1]._Owner = new_id
            branch.points[sel_root]._Order   = root_order
            branch.points._Depth             = Integer("Depth") + root_depth
            branch.points._Explore           = Integer("Explore") + explore

            # Last change
            branch[sel_root].points._ID = new_id

        # ----------------------------------------------------------------------------------------------------
        # Done

        tree += branch

        with Layout("No change if one is empty"):
            empty_branch.error("Trying to attach an empty branch")
            tree = tree.switch(empty_branch, tree_init).switch(empty_tree, branch_init)
            new_id = new_id.switch(empty_branch, GTree.get_child(tree_init, 0, 0))

        tree.out("Points")
        new_id.out("ID")

    # ====================================================================================================
    # Add a single node
    # ====================================================================================================

    with GeoNodes("New", prefix = prefix, is_group=True):
        """ Add a single node

        Symply "Attach" a Tree made of a single node

        Arguments
        ---------
        - Tree (Cloud)
        - Branch (Cloud)
        - ID (Integer) : ID of the node where to attach the branch
        - Location (Integer) : where to attach the new branch

        Returns
        -------
        - Points (Cloud)
        - ID (Integer) : ID of top node of the attached branch
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree = Cloud(None, "Tree")

        node_id  = Integer(0, "ID")
        location = Integer(0, "Location", 0, 3)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        branch = Cloud.Points(1)

        branch.points._ID       = 0
        branch.points._Owner    = -1
        branch.points._Depth    = 0
        branch.points._Total    = 0
        branch.points._Order    = 0
        branch.points._Explore  = 0

        GTree.attach(tree, branch, id=node_id, location=location).node.out()

    # ----------------------------------------------------------------------------------------------------
    # Detach
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Detach", prefix=prefix, is_group=True):
        """ Detach a node and its children

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer) : the ID to detach

        Returns
        -------
        - Points (Cloud) : main tree
        - Branch (Cloud) : detached tree
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree    = Cloud(None, "Tree")
        node_id = Integer(1, "ID")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        id_info = GTree.id_info(tree, node_id).node
        id_exists = id_info.exists_

        with Layout("Explore range to extract"):
            ex0   = id_info.explore
            count = id_info.total + 1
            ex1   = ex0 + count

        with Layout("Separate the branch"):
            tree   = Cloud(tree.points[(Integer("Explore") < ex0) | (Integer("Explore") >= ex1)].separate())
            branch = Cloud(tree.inverted_)

        with Layout("Update main tree"):
            tree.points[Integer("Explore") >= ex1]._Explore = Integer("Explore") - count
            tree = GTree.update_total(tree, id_info.owner, -count)
            tree.points[Integer("Owner").equal(id_info.owner) & (Integer("Order") > id_info.order)]._Order = Integer("Order") - 1

        with Layout("Make branch consistent"):
            branch.points._Depth   = Integer("Depth") - id_info.depth
            branch.points._Explore = Integer("Explore") - id_info.explore

            sel_root = Integer("ID").equal(node_id)
            branch.points[sel_root]._Owner = -1
            branch.points[sel_root]._Order = 0

        tree.out("Points")
        branch.out("Branch")

    # ----------------------------------------------------------------------------------------------------
    # Move
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Move", prefix=prefix, is_group=True):
        """ Move a branchj to another location

        Arguments
        ---------
        - Tree (Cloud)
        - ID (Integer) : ID of the node to move
        - To ID (Integer) : target ID where to move
        - Location (Integer) : where to attach the new branch relatively to "To ID"

        Returns
        -------
        - Points (Cloud)
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree     = Cloud(None,  "Tree")
        node_id  = Integer(2,   "ID")
        to_id    = Integer(1,   "To ID")
        location = Integer(0,   "Location", 0, 3)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree_init = Cloud(tree)

        tree = GTree.detach(tree, id=node_id)
        branch = tree.branch_

        error = GTree.id_info(branch, to_id).exists_

        tree = GTree.attach(tree, branch=branch, id=to_id, location=location)
        branch_id = tree.id_

        #tree = macro_change_id(tree, old_id=branch_id, new_id = node_id)

        tree = tree.switch(error, tree_init)
        error.error("Trying to move branch into one of its nodes")

        tree.out("Points")

    # ----------------------------------------------------------------------------------------------------
    # Group
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Group", prefix=prefix, is_group=True):
        """ Group selected nodes

        Arguments
        ---------
        - Tree (Cloud)
        - Selection (Boolean)

        Returns
        -------
        - Points (Cloud)
        - ID (Integer) : ID of the created node
        - Valid (Boolean) : selection is valid
        """

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        tree      = Cloud(None,    "Tree")
        selection = Boolean(False, "Selection", hide_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

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
            new_id   = new_tree.id_

        with Repeat(tree=new_tree, iterations=to_group.points.count) as rep:

            child_id = to_group.points.sample_index(Integer("ID"), index=rep.iteration)
            rep.tree = GTree.move(rep.tree, id=child_id, to_id=new_id, location=0)

        with Layout("No New id if nothing to group"):
            ok = to_group.points.count > 0
            tree = tree.switch(ok, rep.tree)
            new_id = new_id.switch(-ok, -1)

        tree.out("Points")
        new_id.out("Id")
        ok.out("Valid")
