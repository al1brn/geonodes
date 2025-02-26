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

> Stick a tree structure on domains

The tree can be implemented on any domain
The tree is defined by two attributes (prefixed by the prefix)
- <prefix> ID : node identier
- <prefix> Owner : owner ID

In addition the attribute '<prefix> Selected' can be set

0 is the if ID of the tree root

> [!NOTE]
> Note that 0 is not an ID. Having 0 as owner means that it is a node
belonging to the root

> [!NOTE]
> Note that several elements can share the same id. The MUST have the same owner.

The following groups are provided (actual implementation makes use of a prefix)
- Set Id : set the id and the owner oof the selected items
- Set Owner : set the owner of the selected items
- Change Owner : change owner from old value to new value (allow to plug a tree into another one)
- Info : get the 3 existing attributes (to avoid entering directly the named attribute)
- Get Max Id : get the maximum id value of geometry, used to created a new id
- Select : set the '<prefix> Selected' attribute
- Join : join two trees:
  1. Shift the indices of the joined geometry
  2. Replace the 0 owner by the target owner id
  3. Actually join the geometries
- Separate : Separate a geometry into two different trees
- Id Owner : get the owner if from an item id
- Prepare Insert : get a new owner id and use it as owner of the passed item id.
  - NOTE : the tree is inconsistent until a geometry with (new id, old owner) is joined
- Get Index : Get the index of an element having the provided id.
  Since several elements can share the same id, it returns the first index
- Belongs to : test if an id belongs to the given owner. This is True when:
  - The item id is equal to the owner id (an items belongs to itself)
  - The item owner is directly the owner id
  - The items owner recursively belongs to the owner
- Select Tree : select the items belongs to an owner
- Dump : utility to visualize the ids and owners
- Demo : Build a simple tree

[Source Code](../demos/forest.py)

Animated formula

IN PROGRESS

``` python
from geonodes.demos import formula

formula.demo()
```
"""

from geonodes import *

def build_tree(prefix='Tree', max_depth=10):

    GTree = G(prefix)

    # ----------------------------------------------------------------------------------------------------
    # New node

    with GeoNodes("New", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        owner = Integer(0, "Owner")

        count = cloud.points.count
        first = count.equal(0)

        with Layout("Tree Root"):
            root = Cloud.Points()
            root.points._Owner = -1

        cloud = cloud.switch(first, root)
        count = count.switch(first, 1)

        with Layout("New"):
            new = Cloud.Points(1, position=(count, 0, 0))
            new.points._Owner = owner

        (cloud + new).out("Tree")
        count.out("Index")

    # ----------------------------------------------------------------------------------------------------
    # Owner of an id

    with GeoNodes("Index Owner", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        index = Integer.Index("Index")

        owner = cloud.points.sample_index(Integer("Owner"), index=index)
        owner.out("Owner")

    # ----------------------------------------------------------------------------------------------------
    # Group

    with GeoNodes("Group", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        owner = Integer(0, "Owner", single_value=True, tip="Create a new node under this owner an put selection under it")
        sel   = Boolean(True, "Selection")

        new_index = cloud.points.count + 1

        sel &= Integer("Owner").equal(owner)
        cloud.points[sel]._Owner = new_index

        new = GTree.New(cloud, owner=owner)

        cloud.out("Tree")
        new_index.out("Index")

    # ----------------------------------------------------------------------------------------------------
    # Join

    with GeoNodes("Join", prefix=prefix, is_group=True):

        cloud  = Cloud(None, "Tree")
        index  = Integer(0, "Index", single_value=True, tip="Attach the new branch to this owner")
        branch = Cloud(None, "Branch")

        shift_index = cloud.points.count - 1
        #new_index = cloud.points.count + 1

        # ----- Remove the root in the branch

        branch = branch.points[nd.index.equal(0)].delete()

        # ----- Shift branch owners

        branch.points._Owner = Integer("Owner") + shift_index

        # ----- Old (index, 0) are now (index, shift_index)
        # We plug them to index as new owner

        branch.points[Integer("Owner").equal(shift_index)]._Owner = index

        # ----- Add the branch

        (cloud + branch).out("Tree")

    # ----------------------------------------------------------------------------------------------------
    # Change Owner

    with GeoNodes("Change Owner", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        from_owner = Integer(1, "From Owner")
        to_owner = Integer(1, "To Owner")

        cloud.points[Integer("Owner").equal(from_owner)]._Owner = to_owner

        cloud.out("Tree")

    # ----------------------------------------------------------------------------------------------------
    # Insert

    with GeoNodes("Insert", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        index = Integer(1, "Index")
        below = Boolean(False, "Below")

        new_index = cloud.points.count + 1

        with Layout("Below"):
            below_cloud = Cloud(cloud).points[Integer("Owner").equal(index)]._Owner = new_index
            below_owner = index

        with Layout("Above"):
            above_owner = GTree.index_owner(cloud, index=index)
            above_cloud = Cloud(cloud).points[index]._Owner = new_index

        above_cloud.switch(below, below_cloud).out("Tree")

        cloud = GTree.new(cloud, owner=above_owner.switch(below, below_owner))

        cloud.out("Tree")
        new_index.out("Id")

    # ----------------------------------------------------------------------------------------------------
    # Select a group

    with GeoNodes("Select Group", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        index = Integer(0, "Index", single_value=True)

        cloud.points._Selected = nd.index.equal(index)
        cloud.points._Depth = 0

        with Repeat(cloud=cloud, iterations=max_depth) as rep:
            sel = -Boolean("Selected")
            rep.cloud[sel].points._Depth = rep.iteration + 1
            rep.cloud.points[sel]._Selected = rep.cloud.points.sample_index(Boolean("Selected"), index=Integer("Owner"))

        rep.cloud.out("Tree")

    # ----------------------------------------------------------------------------------------------------
    # Build tree
    #
    # Set the tree attributes from owner
    # - Order : order within its direct owner
    # - Total : total number of children
    # - First : first children
    # - Depth : depth

    with GeoNodes("Build Tree", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")
        count = cloud.points.count

        # X : depth
        # Y : cumulative order

        cloud.points.position = 0

        # Loop on depths

        cloud.points._Children = 0
        cloud.points._Done     = False
        cloud.points._Explore  = 0

        cloud.points._Next_Sel = nd.index.equal(0)

        with Repeat(cloud=cloud, iterations=max_depth) as rep:

            rep.cloud.points._Depth_Sel = Boolean("Next Sel")
            rep.cloud.points._Next_Sel = False

            # Loop on items belonging to curent depth
            with Repeat(cloud=rep.cloud, iterations=count) as rep2:

                owner = rep2.cloud.points.sample_index(Integer("Owner"), index=rep2.iteration)._lc("Owner")

                ok         = rep2.cloud.points.sample_index(Boolean("Depth Sel"), index=owner)._lc("Ok")
                children   = rep2.cloud.points.sample_index(Integer("Children"),  index=owner)._lc("Children")
                owner_expl = rep2.cloud.points.sample_index(Integer("Explore"),   index=owner)._lc("Owner Expl")
                index_expl = (owner_expl + children + 1)._lc("Index Explore")

                # ----- Selection for attributes update

                with Layout("Index Selection"):
                    index_sel = (ok & nd.index.equal(rep2.iteration))._lc("Index Sel")

                with Layout("Owner Selection"):
                    owner_sel = (ok & nd.index.equal(owner))._lc("Owner Sel")

                with Layout("After Selection"):
                    after_sel = (ok & Boolean("Done") & (Integer("Explore") >= index_expl))._lc("After Sel")

                # ----- Explore & order

                rep2.cloud.points[index_sel]._Order   = children
                rep2.cloud.points[after_sel]._Explore  += 1
                rep2.cloud.points[index_sel]._Explore = index_expl

                rep2.cloud.points[owner_sel]._Children += 1

                rep2.cloud.points[index_sel]._Depth = rep.iteration

                # ----- Done

                rep2.cloud.points[index_sel]._Done = True
                rep2.cloud.points[index_sel]._Next_Sel = True

            rep.cloud = rep2.cloud

        cloud = rep.cloud

        cloud.remove_names("* Sel")
        cloud.remove_names("Done")

        cloud.out()


    # ----------------------------------------------------------------------------------------------------
    # Set explore index

    with GeoNodes("Set Explore", prefix=prefix, is_group=True):

        cloud = Cloud(None, "Tree")

        # --------------------------------------------------------------------------------
        # Order items within their direct owner

        count = cloud.points.count
        cloud.points._Order = 0

        with Repeat(cloud=cloud, iterations=count) as rep:

            with Repeat(cloud=rep.cloud, order=0, iterations=count) as rep2:

                ok = rep2.cloud.points.sample_index(Integer("Owner"), index=rep2.iteration).equal(rep.iteration)
                rep2.cloud.points[ok & nd.index.equal(rep2.iteration)]._Order = rep2.order

                rep2.order = rep2.order.switch(ok, rep2.order + 1)

            rep.cloud = rep2.cloud

        cloud = rep.cloud

        # --------------------------------------------------------------------------------
        # Items depth initialized relatively to root

        cloud = Cloud(GTree.select_group(cloud, index=0))

        # --------------------------------------------------------------------------------
        # Total number of children

        cloud.points._Total = 1

        # Loop from max_depth to 0

        with Repeat(cloud=cloud, iterations=max_depth) as rep:

            # Work only on items of the current depth
            depth = max_depth - rep.iteration

            # Loop on the items with this depth
            with Repeat(cloud=rep.cloud, iterations=count) as rep2:

                # Ok to add the total the the owner ?
                ok = rep2.cloud.points.sample_index(Integer("Depth").equal(depth), index=rep2.iteration)

                # Owner
                owner = rep2.cloud.points.sample_index(Integer("Owner"), index=rep2.iteration)

                # The total to add
                total = rep2.cloud.points.sample_index(Integer("Total"), index=rep2.iteration)

                # We add the total to the owner
                rep2.cloud.points[ok & nd.index.equal(owner)]._Total = Integer("Total") + total

            rep.cloud = rep2.cloud

        cloud = rep.cloud

        # Totals include the nodes themselves

        cloud.points._Total = Integer("Total") - 1

        # --------------------------------------------------------------------------------
        # Explore order

        cloud.points._Explore = 0

        # Loop on the depths from 1

        with Repeat(cloud=cloud, iterations=max_depth - 1) as rep:

            depth = rep.iteration + 1

            # Loop on the items of this depth
            with Repeat(cloud=rep.cloud, total=0, iterations=count) as rep2:

                # We get the owner explore value
                owner = rep2.cloud.points.sample_index(Integer("Owner"), index=rep2.iteration)
                explore = rep2.cloud.points.sample_index(Integer("Explore"), index=owner)

                # Depth is ok ?
                ok = rep2.cloud.points.sample_index(Integer("Depth"), index=rep2.iteration).equal(depth)

                # Order
                order = rep2.cloud.points.sample_index(Integer("Order"), index=rep2.iteration)

                # Total children
                children = rep2.cloud.points.sample_index(Integer("Total"), index=rep2.iteration)

                # If order is 0, we reset total
                total = rep2.total.switch(order.equal(0), 0)

                # We add self
                total += 1

                # We can now set the explore index

                rep2.cloud.points[ok & nd.index.equal(rep2.iteration)]._Explore = explore + total

                # Update total

                rep2.total = total + children

            rep.cloud = rep2.cloud

        cloud = rep.cloud


        cloud.out()


    # ----------------------------------------------------------------------------------------------------
    # Dump

    with GeoNodes("Dump", prefix=prefix):

        cloud = Cloud(None, "Tree")
        use_labels = Boolean(True, "Labels")

        # ----------------------------------------------------------------------------------------------------
        # Build Tree

        cloud = Cloud(GTree.build_tree(cloud))
        count = cloud.points.count

        # ----------------------------------------------------------------------------------------------------
        # Order items with Explore

        expl = Cloud.Points(count)
        with Repeat(expl=expl, cloud=cloud, iterations=count) as rep:

            index = rep.cloud.points[Integer("Explore").equal(rep.iteration)].attribute_statistic(nd.index).min.to_integer()
            sel = nd.index.equal(rep.iteration)

            rep.expl.points[sel]._Index = index
            rep.expl.points[sel]._Owner = rep.cloud.points.sample_index(Integer("Owner"), index=index)
            rep.expl.points[sel]._Order = rep.cloud.points.sample_index(Integer("Order"), index=index)
            rep.expl.points[sel]._Depth = rep.cloud.points.sample_index(Integer("Depth"), index=index)

        expl = rep.expl

        # ----------------------------------------------------------------------------------------------------
        # Compute positions

        with Repeat(cloud=expl, y=0, iterations=cloud.points.count) as rep:

            order = rep.cloud.points.sample_index(Integer("Order"), index=rep.iteration)
            depth = rep.cloud.points.sample_index(Integer("Depth"), index=rep.iteration)

            x = depth
            y = rep.y.switch(order.not_equal(0), rep.y - 1)

            rep.cloud[nd.index.equal(rep.iteration)].position = (x, y, 0)
            rep.y = y

        cloud = rep.cloud

        cloud[0].position = (-1, 0, 0)

        # ----- Labels

        with cloud.points.for_each(item_index=Integer("Index"), owner=Integer("Owner"), pos=nd.position) as feel:

            s = feel.item_index.to_string() + " [" + feel.owner.to_string() + "]"
            curves = s.to_curves(size=.3).realize()
            labels = Curve(curves).fill()

            labels.transform(translation=feel.pos)

            feel.generated.geometry = labels

        cloud = cloud.switch(use_labels, feel.generated.geometry)

        cloud.out()


    # ----------------------------------------------------------------------------------------------------
    # A Demo

    with GeoNodes("Demo", prefix = prefix):

        # ----- Build a Tree

        tree = GTree.New() # 1
        tree = GTree.New(tree) # 2
        tree = GTree.New(tree, owner=2) # 3
        tree = GTree.New(tree, owner=2) # 4
        tree = GTree.New(tree, owner=3) # 5
        tree = GTree.New(tree, owner=5) # 5
        tree = GTree.New(tree, owner=5) # 5
        tree = GTree.New(tree, owner=0)
        tree = GTree.New(tree, owner=0)

        # ---- Plug to 4

        with Layout("Join"):
            tree = GTree.join(tree, branch=tree, index=4)
            index = tree.index_
            #tree = GTree.new(tree, owner=index)

        tree = GTree.set_explore(tree)

        tree.out()


        return













    # ----------------------------------------------------------------------------------------------------
    # Set owner

    with GeoNodes("Set Owner", prefix=prefix):

        geo   = Geometry()
        owner = Integer(0, "Owner")
        sel   = Boolean(True, "Selection")

        geo = get_domain(geo)[sel].store(owner_name, owner)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Change owner

    with GeoNodes("Change Owner", prefix=prefix):

        geo = Geometry()
        old_owner = Integer(0, "Old Owner")
        new_owner = Integer(0, "New Owner")
        sel = Boolean(True, "Selection")

        geo = get_domain(geo)[sel & Integer(owner_name).equal(old_owner)].store(owner_name, new_owner)

        geo.out()




    # ----------------------------------------------------------------------------------------------------
    # Get id and owner

    with GeoNodes("Info", prefix=prefix, is_group=True):

        Integer(id_name).out("Id")
        Integer(owner_name).out("Owner")
        Boolean(sel_name).out("Selected")

    # ----------------------------------------------------------------------------------------------------
    # Select items

    with GeoNodes("Select", prefix=prefix):

        geo = Geometry()
        sel = Boolean(True, "Selection")

        geo = get_domain(geo).store(sel_name, sel)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Join two trees

    with GeoNodes("Join", prefix=prefix, is_group=True):

        geo   = Geometry()
        item  = Geometry(name="Item")
        owner = Integer(0, "Owner", single_value=True)
        shift_ids = Boolean(True, "Shift Ids")

        # ----- Increment id and owner

        with If(Geometry, shift_ids) as to_join:

            id_ofs = G(prefix).get_max_id(geo)
            g = G(prefix).set_id(item, id=Integer(id_name) + id_ofs, owner=Integer(owner_name) + id_ofs)

            # ----- Previous id 0 is renumed id_ofs
            # It's owner is now owner

            to_join.option = G(prefix).set_owner(g, owner=owner, selection=Integer(owner_name).equal(id_ofs))

        # ----- Just change the owner

        with Else(to_join):

            to_join.option = G(prefix).set_owner(item, owner=owner, selection=Integer(owner_name).equal(0))

        # ----- Join the geometries

        (geo + to_join).out()

    # ----------------------------------------------------------------------------------------------------
    # The the owner id of an id

    with GeoNodes("Id Owner", prefix=prefix, is_group=True):
        geo = Geometry()
        item_id = Integer(1, "Id", single_value=True)

        sel = Integer(id_name).equal(item_id)
        owner = get_domain(geo)[sel].attribute_statistic(Integer(owner_name)).min.to_integer()

        owner = owner.switch(item_id.equal(0), 0)

        owner.out("Owner")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Set id
    #
    # Set the item id

    with GeoNodes("Prepare Insert", prefix=prefix, is_group=True):

        formula = Geometry()
        item_id = Integer(0, "Id", single_value=True)

        # ----- New id for inserted item
        new_id = G(prefix).get_max_id(formula) + 1

        # ----- What is the owner of group which will be encapsulated
        owner = G(prefix).id_owner(item_id)

        # ----- Change the owner of items with item_id
        # NOTE : the tree is inconsistent until a geometry will be inserted with
        # - item id  : new_id
        # - owner id : owner

        G(prefix).set_owner(formula, owner=owner, selection=G(prefix).info().node.id.equal(item_id))

        formula.out()
        new_id.out("New Id")
        owner.out("Owner")

    # ----------------------------------------------------------------------------------------------------
    # Get the index of an element with a given id
    #
    # Note that several element can share the same id

    with GeoNodes("Get Index", prefix=prefix, is_group=True):

        geo = Geometry()
        item_id = Integer(1, "Id", single_value=True)

        sel = Integer(id_name).equal(item_id)
        index = get_domain(geo)[sel].attribute_statistic(nd.index).min.to_integer()

        index.out("Index")
        index.not_equal(0).out("Exists")

    # ----------------------------------------------------------------------------------------------------
    # Does an item belong to an owner
    #
    # Returns a boolean plus depth

    with GeoNodes("Belongs to", prefix=prefix, is_group=True):

        geo = Geometry()
        item_id = Integer(1, name="Id", single_value=True)
        owner   = Integer(0, name="Owner", single_value=True)

        with Repeat(geo=geo, item_id=item_id, ok=item_id.equal(owner), depth=0, iterations=max_depth) as rep:

            rep.depth = (rep.depth + 1).switch(rep.ok, rep.depth)

            item_owner = get_domain(rep.geo)[Integer(id_name).equal(rep.item_id)].attribute_statistic(Integer(owner_name)).min

            rep.ok |= item_owner.equal(owner)

            rep.item_id = item_owner

        rep.ok.out("Belongs")
        rep.depth.out("Depth")

    # ----------------------------------------------------------------------------------------------------
    # Select the items belonging to an owner

    with GeoNodes("Select Tree", prefix=prefix, is_group=True):

        geo   = Geometry()
        owner = Integer(0, "Id", single_value=True)

        with Repeat(geo=geo, iterations=domain_count(geo)) as rep:

            item_id = get_domain(rep.geo).sample_index(Integer(id_name), index=rep.iteration)
            rep.geo = get_domain(rep.geo)[rep.iteration].store(sel_name, G(prefix).belongs_to(rep.geo, id=item_id, owner=owner))

        rep.geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Separate a group

    with GeoNodes("Separate", prefix=prefix,is_group=True):

        geo   = Geometry()
        owner = Integer(0, "Id", single_value=True)

        G(prefix).select_tree(geo, id=id)

        sel_part = get_domain(geo)[Boolean(sel_name)].separate()
        inv_part = sel_part.inverted_

        # ------ Owner now belongs to 0

        sel_part = G(prefix).set_owner(sel_part, owner=0, selection=Integer(item_id).equal(owner))

        sel_part.out("Selection")
        inv_part.out("Inverted")

    # ----------------------------------------------------------------------------------------------------
    # Dump

    with GeoNodes("Dump", prefix=prefix):

        geo = Geometry()
        size = Float(.5, "Height")
        dist = Float(1, "Distance")

        with get_domain(geo).for_each(item_id=Integer(id_name), owner=Integer(owner_name), pos=nd.position, normal=nd.normal) as feel:

            s = feel.item_id.to_string() + ' [' + feel.owner.to_string() + ']'
            curves = s.to_curves(size=size).realize()
            label = Curve(curves).fill()

            loc = feel.pos + feel.normal.scale(dist)

            label.transform(translation=loc)

            label += Curve.Line(feel.pos, loc)

            feel.generated.geometry = label

        (geo + feel.generated.geometry).out()


    # ----------------------------------------------------------------------------------------------------
    # Select the items belonging to an owner

    with GeoNodes("Demo", prefix = prefix):

        def new_item():
            if domain == 'POINT':
                item = Cloud.Points(1)
                item = G(prefix)._set_id(item, id=1)
                return item

            elif domain in ['CURVE', 'SPLINE']:
                item = Curve.Line()
                item = G(prefix)._set_id(item, id=1)
                return item

            else:
                item = Mesh.Cube(.3)
                item = G(prefix)._set_id(item, id=1)
                return item

        with Layout(f"Base tree"):

            sub_tree = new_item()

            sub_tree = G(prefix).join(sub_tree, new_item())
            sub_tree = G(prefix).join(sub_tree, new_item())


            sub_tree = G(prefix).join(sub_tree, new_item(), owner=2)

        geo = G(prefix).join(sub_tree, sub_tree)
        geo = G(prefix).join(geo, sub_tree, owner=7)

        ok = G(prefix).belongs_to(geo, id=1, owner=0)

        nd.viewer(geo, ok)

        geo = G(prefix).select_tree(geo, id=0)

        with get_domain(geo).for_each(pos=Vector.Random(-10, 10, seed=0)) as feel:

            element = feel.element.transform(translation=feel.pos)

            feel.generated.geometry = element

        geo = feel.generated.geometry

        geo.out()


def build_tree_OLD(domain='POINT', prefix='Tree', max_depth=10):

    id_name    = f"{prefix} ID"
    owner_name = f"{prefix} Owner"
    sel_name   = f"{prefix} Selected"

    def get_domain(geo):
        if domain == 'POINT':
            return Cloud(geo).points

        elif domain == 'FACE':
            return Mesh(geo).faces

        elif domain == 'EDGE':
            return Mesh(geo).edges

        elif domain == 'CORNER':
            return Mesh(geo).corners

        elif domain in ['SPLINE', 'CURVE']:
            return Curve(geo).splines

        assert(False)

    def domain_count(geo):
        if domain == 'POINT':
            return geo.mesh.points.count + geo.curve.points.count + geo.point_cloud.points.count

        else:
            return get_domain(geo).count

    # ----------------------------------------------------------------------------------------------------
    # Set id and owner

    with GeoNodes("Set Id", prefix=prefix):

        geo   = Geometry()
        id    = Integer(1, "Id")
        owner = Integer(0, "Owner")
        sel   = Boolean(True, "Selection")

        geo = get_domain(geo)[sel].store(id_name, id)
        geo = get_domain(geo)[sel].store(owner_name, owner)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Set owner

    with GeoNodes("Set Owner", prefix=prefix):

        geo   = Geometry()
        owner = Integer(0, "Owner")
        sel   = Boolean(True, "Selection")

        geo = get_domain(geo)[sel].store(owner_name, owner)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Change owner

    with GeoNodes("Change Owner", prefix=prefix):

        geo = Geometry()
        old_owner = Integer(0, "Old Owner")
        new_owner = Integer(0, "New Owner")
        sel = Boolean(True, "Selection")

        geo = get_domain(geo)[sel & Integer(owner_name).equal(old_owner)].store(owner_name, new_owner)

        geo.out()




    # ----------------------------------------------------------------------------------------------------
    # Get id and owner

    with GeoNodes("Info", prefix=prefix, is_group=True):

        Integer(id_name).out("Id")
        Integer(owner_name).out("Owner")
        Boolean(sel_name).out("Selected")

    # ----------------------------------------------------------------------------------------------------
    # Get max existing id

    with GeoNodes("Get Max Id", prefix=prefix, is_group=True):

        geo = Geometry()
        sel = Boolean(True, "Selection")

        max_id = get_domain(geo)[sel].attribute_statistic(Integer(id_name)).max
        min_id = max_id.min_

        max_id.to_integer().out("Max Id")
        min_id.to_integer().out("Min Id")

    # ----------------------------------------------------------------------------------------------------
    # Select items

    with GeoNodes("Select", prefix=prefix):

        geo = Geometry()
        sel = Boolean(True, "Selection")

        geo = get_domain(geo).store(sel_name, sel)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Join two trees

    with GeoNodes("Join", prefix=prefix, is_group=True):

        geo   = Geometry()
        item  = Geometry(name="Item")
        owner = Integer(0, "Owner", single_value=True)
        shift_ids = Boolean(True, "Shift Ids")

        # ----- Increment id and owner

        with If(Geometry, shift_ids) as to_join:

            id_ofs = G(prefix).get_max_id(geo)
            g = G(prefix).set_id(item, id=Integer(id_name) + id_ofs, owner=Integer(owner_name) + id_ofs)

            # ----- Previous id 0 is renumed id_ofs
            # It's owner is now owner

            to_join.option = G(prefix).set_owner(g, owner=owner, selection=Integer(owner_name).equal(id_ofs))

        # ----- Just change the owner

        with Else(to_join):

            to_join.option = G(prefix).set_owner(item, owner=owner, selection=Integer(owner_name).equal(0))

        # ----- Join the geometries

        (geo + to_join).out()

    # ----------------------------------------------------------------------------------------------------
    # The the owner id of an id

    with GeoNodes("Id Owner", prefix=prefix, is_group=True):
        geo = Geometry()
        item_id = Integer(1, "Id", single_value=True)

        sel = Integer(id_name).equal(item_id)
        owner = get_domain(geo)[sel].attribute_statistic(Integer(owner_name)).min.to_integer()

        owner = owner.switch(item_id.equal(0), 0)

        owner.out("Owner")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Set id
    #
    # Set the item id

    with GeoNodes("Prepare Insert", prefix=prefix, is_group=True):

        formula = Geometry()
        item_id = Integer(0, "Id", single_value=True)

        # ----- New id for inserted item
        new_id = G(prefix).get_max_id(formula) + 1

        # ----- What is the owner of group which will be encapsulated
        owner = G(prefix).id_owner(item_id)

        # ----- Change the owner of items with item_id
        # NOTE : the tree is inconsistent until a geometry will be inserted with
        # - item id  : new_id
        # - owner id : owner

        G(prefix).set_owner(formula, owner=owner, selection=G(prefix).info().node.id.equal(item_id))

        formula.out()
        new_id.out("New Id")
        owner.out("Owner")

    # ----------------------------------------------------------------------------------------------------
    # Get the index of an element with a given id
    #
    # Note that several element can share the same id

    with GeoNodes("Get Index", prefix=prefix, is_group=True):

        geo = Geometry()
        item_id = Integer(1, "Id", single_value=True)

        sel = Integer(id_name).equal(item_id)
        index = get_domain(geo)[sel].attribute_statistic(nd.index).min.to_integer()

        index.out("Index")
        index.not_equal(0).out("Exists")

    # ----------------------------------------------------------------------------------------------------
    # Does an item belong to an owner
    #
    # Returns a boolean plus depth

    with GeoNodes("Belongs to", prefix=prefix, is_group=True):

        geo = Geometry()
        item_id = Integer(1, name="Id", single_value=True)
        owner   = Integer(0, name="Owner", single_value=True)

        with Repeat(geo=geo, item_id=item_id, ok=item_id.equal(owner), depth=0, iterations=max_depth) as rep:

            rep.depth = (rep.depth + 1).switch(rep.ok, rep.depth)

            item_owner = get_domain(rep.geo)[Integer(id_name).equal(rep.item_id)].attribute_statistic(Integer(owner_name)).min

            rep.ok |= item_owner.equal(owner)

            rep.item_id = item_owner

        rep.ok.out("Belongs")
        rep.depth.out("Depth")

    # ----------------------------------------------------------------------------------------------------
    # Select the items belonging to an owner

    with GeoNodes("Select Tree", prefix=prefix, is_group=True):

        geo   = Geometry()
        owner = Integer(0, "Id", single_value=True)

        with Repeat(geo=geo, iterations=domain_count(geo)) as rep:

            item_id = get_domain(rep.geo).sample_index(Integer(id_name), index=rep.iteration)
            rep.geo = get_domain(rep.geo)[rep.iteration].store(sel_name, G(prefix).belongs_to(rep.geo, id=item_id, owner=owner))

        rep.geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Separate a group

    with GeoNodes("Separate", prefix=prefix,is_group=True):

        geo   = Geometry()
        owner = Integer(0, "Id", single_value=True)

        G(prefix).select_tree(geo, id=id)

        sel_part = get_domain(geo)[Boolean(sel_name)].separate()
        inv_part = sel_part.inverted_

        # ------ Owner now belongs to 0

        sel_part = G(prefix).set_owner(sel_part, owner=0, selection=Integer(item_id).equal(owner))

        sel_part.out("Selection")
        inv_part.out("Inverted")

    # ----------------------------------------------------------------------------------------------------
    # Dump

    with GeoNodes("Dump", prefix=prefix):

        geo = Geometry()
        size = Float(.5, "Height")
        dist = Float(1, "Distance")

        with get_domain(geo).for_each(item_id=Integer(id_name), owner=Integer(owner_name), pos=nd.position, normal=nd.normal) as feel:

            s = feel.item_id.to_string() + ' [' + feel.owner.to_string() + ']'
            curves = s.to_curves(size=size).realize()
            label = Curve(curves).fill()

            loc = feel.pos + feel.normal.scale(dist)

            label.transform(translation=loc)

            label += Curve.Line(feel.pos, loc)

            feel.generated.geometry = label

        (geo + feel.generated.geometry).out()


    # ----------------------------------------------------------------------------------------------------
    # Select the items belonging to an owner


    with GeoNodes("Demo", prefix = prefix):

        def new_item():
            if domain == 'POINT':
                item = Cloud.Points(1)
                item = G(prefix)._set_id(item, id=1)
                return item

            elif domain in ['CURVE', 'SPLINE']:
                item = Curve.Line()
                item = G(prefix)._set_id(item, id=1)
                return item

            else:
                item = Mesh.Cube(.3)
                item = G(prefix)._set_id(item, id=1)
                return item

        with Layout(f"Base tree"):

            sub_tree = new_item()

            sub_tree = G(prefix).join(sub_tree, new_item())
            sub_tree = G(prefix).join(sub_tree, new_item())


            sub_tree = G(prefix).join(sub_tree, new_item(), owner=2)

        geo = G(prefix).join(sub_tree, sub_tree)
        geo = G(prefix).join(geo, sub_tree, owner=7)

        ok = G(prefix).belongs_to(geo, id=1, owner=0)

        nd.viewer(geo, ok)

        geo = G(prefix).select_tree(geo, id=0)

        with get_domain(geo).for_each(pos=Vector.Random(-10, 10, seed=0)) as feel:

            element = feel.element.transform(translation=feel.pos)

            feel.generated.geometry = element

        geo = feel.generated.geometry

        geo.out()
