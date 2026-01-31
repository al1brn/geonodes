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

$ DOC hidden

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : treearrange
---------------------
- arrange the tree nodes to make the whole readable

Note that this module is independant from node generation and can be used on any tree.

It registers a layout places in the tool tab or the nodes editor to offer some useful functions,
especially the help on selected nodes.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/01/18 : bug when deleting temp frames
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.1"
__blender_version__ = "4.3.0"


import bpy
from mathutils import Vector
from .constants import NODE_INFO

from bpy.props import BoolProperty

from typing import Literal, List

X_SEPA = 60
Y_SEPA = 40

ZONE_INPUTS  = ['GeometryNodeRepeatInput',  'GeometryNodeSimulationInput',  'GeometryNodeForeachGeometryElementInput',  'Closure Input']
ZONE_OUTPUTS = ['GeometryNodeRepeatOutput', 'GeometryNodeSimulationOutput', 'GeometryNodeForeachGeometryElementOutput', 'Closure Output']

INPUT_NODES  = ZONE_INPUTS  + ['NodeGroupInput']
OUTPUT_NODES = ZONE_OUTPUTS + ['NodeGroupOutput']

TEMP_FRAME = "$TEMP FRAME"

# Minimum input links for a frame to have its dedicated Group Input Node
MIN_INPUT_LINKS = 5

# ====================================================================================================
# A link between two nodes
# ====================================================================================================

class Link:
    def __init__(self, tree, blink):
        """ > Link wrapper

        Properties
        ----------
        - tree (Tree) : tree wrapper
        - blink (bpy.types.Link) : wrapped link
        - node0 (Node) : starting node
        - node1 (Node) : ending node
        - index0 (int) : starting socket index
        - index1 (int) : ending socket index
        """
        self.tree  = tree

        self.blink  = blink
        self.node0  = tree[blink.from_node]
        self.node1  = tree[blink.to_node]
        if True:
            _, self.index0, _, self.index1 = self.blink_key(blink)
        else:
            self.index0 = list(blink.from_node.outputs).index(blink.from_socket)
            self.index1 = list(blink.to_node.inputs).index(blink.to_socket)

    def __str__(self):
        return f"<Link [{self.node0.bnode.name}]({self.index0}) -> [{self.node1.bnode.name}]({self.index1})>"

    @classmethod
    def blink_key(cls, blink):
        index0 = list(blink.from_node.outputs).index(blink.from_socket)
        index1 = list(blink.to_node.inputs).index(blink.to_socket)
        return (blink.from_node.name, index0, blink.to_node.name, index1)

    @property
    def node0_key(self):
        return f"{self.node0.bnode.name}_{self.index0}"

    @property
    def node1_key(self):
        return f"{self.node1.bnode.name}_{self.index1}"

    @property
    def socket0(self):
        """ Starting socket

        > [!IMPORTANT]
        > The socket is not directly read from the link but from <#node0> using <#index0>.

        Returns
        -------
        - bpy.types.NodeSocket : from socket
        """
        return self.node0.bnode.outputs[self.index0]

    @property
    def socket1(self):
        """ Starting socket

        > [!IMPORTANT]
        > The socket is not directly read from the link but from <#node1> using <#index1>.

        Returns
        -------
        - bpy.types.NodeSocket : to socket
        """
        return self.node1.bnode.inputs[self.index1]

    def replace_to(self, node1, index1=None):
        """ Replace node 1

        The link is deleted and replaced by a link from <#node0> to the new <#node1>

        Arguments
        ---------
        - node1 (Node) : new 'node to'
        - index1 (int = None) : new index1, keep current if None
        """
        self.tree.btree.links.remove(self.blink)
        self.node1 = node1
        if index1 is not None:
            self.index1 = index1
        self.blink = self.tree.btree.links.new(self.socket0, self.socket1)

    def replace_from(self, node0, index0=None):
        """ Replace node 0

        The link is deleted and replaced by a link from new <#node0> to <#node1>

        Arguments
        ---------
        - node0 (Node) : new 'from node'
        - index0 (int = None) : new index0, keep current if None
        """
        self.tree.btree.links.remove(self.blink)
        self.node0 = node0
        if index0 is not None:
            self.index0 = index0
        self.blink = self.tree.btree.links.new(self.socket0, self.socket1)

    def insert_reroute(self, frame):
        """ Insert a reroute node

        Arguments
        ---------
        - parent (Frame) : parent frame

        Returns
        -------
        - Node : reroute node
        """

        # ----- Create the reroute node
        reroute = self.tree.new_reroute(frame)

        # ----- Label
        sock_descr = self.blink.from_socket.description
        if sock_descr.startswith("UL "):
            sock_descr = sock_descr[3:]
        else:
            sock_descr = ""

        if sock_descr == "":
            node_lab = self.node0.bnode.label
            if node_lab is None or node_lab == '':
                reroute.bnode.label = self.blink.from_socket.name
            else:
                reroute.bnode.label = node_lab
        else:
            reroute.bnode.label = sock_descr


        # ----- From source node to reroute
        self.tree.new_link(self.node0, self.index0, reroute, 0)

        # ----- From reroute to target node
        self.replace_from(reroute, index0 = 0)

        return reroute
    
# ====================================================================================================
# Hierarchy item
# Root class for Node and Tree
# ====================================================================================================

class Item:

    def get_node(self, name):
        return self.tree.nodes[name]

    # ----------------------------------------------------------------------------------------------------
    # Reset (create the hierarchy attributes)
    # ----------------------------------------------------------------------------------------------------

    def reset(self):
        self.owner    = None
        self.children = []

        # Will be set by tree.build_hierarchy
        self.items_in    = {}
        self.items_out   = {}
        self.through_in  = {}
        self.through_out = {}

        # Cache
        self._left_items  = None
        self._right_items = None
    
    # ----------------------------------------------------------------------------------------------------
    # Hierarchy Interface
    # ----------------------------------------------------------------------------------------------------

    def append(self, item):
        item.owner = self
        self.children.append(item)

    @property
    def is_top(self):
        return self.owner is None
    
    @property
    def top(self):
        cur = self
        while cur.owner is not None:
            cur = cur.owner
        return cur
    
    @property
    def depth(self):
        depth = 0
        cur = self
        while cur.owner is not None:
            cur = cur.owner
            depth += 1
        return depth

    @property
    def is_child_of(self, item):
        cur = self
        while cur.owner is not None:
            if cur.owner == item:
                return True
            cur = cur.owner
        return False
    
    @property
    def owners_stack(self):
        cur = self.owner
        owners = []
        while cur is not None:
            owners.append(cur)
            cur = cur.owner

        return owners
    
    def common_ancestor(self, other):

        if self.owner == other.owner:
            return self.owner, self, other
        
        owners0 = self.owners_stack
        owners1 = other.owners_stack

        assert owners0[-1] == owners1[-1], "Oups"

        n0, n1 = len(owners0), len(owners1)
        n = min(n0, n1)

        for i in range(1, n):
            idx = -i - 1
            if owners0[idx] != owners1[idx]:
                return owners0[idx + 1], owners0[idx], owners1[idx]
            
        if n == n0:
            return owners0[-n], self, owners1[-n - 1]
        else:
            return owners0[-n], owners0[-n - 1], other

    # ====================================================================================================
    # Exploration
    # ====================================================================================================

    def all_children(self):
        for child in self.children:
            yield child, 1
            for ch, depth in child.all_children():
                yield ch, depth + 1

    # ====================================================================================================
    # Backward / forward exploration
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Build the dicts
    # ----------------------------------------------------------------------------------------------------

    def left_right_items(self, left):
        """ All the intems linked to in / out items

        Arguments
        ---------
        - left (bool) : left or right items

        Returns
        -------
        - dict : name -> (min dist, max dist)
        """

        items = {}

        # ---------------------------------------------------------------------------
        # The list of directly linked items (dist min = 1)
        # ---------------------------------------------------------------------------

        base = self.items_in if left else self.items_out
        for item_name in base:
            items[item_name] = (1, 1)

        # ---------------------------------------------------------------------------
        # Add the linked items of these items
        # ---------------------------------------------------------------------------

        for item in [self.tree.nodes[item_name] for item_name in base]:

            loop_list = item.left_items if left else item.right_items
            for next_name, (d_min, d_max) in loop_list.items():
                if next_name in items:
                    cur_min, cur_max = items[next_name]
                    items[next_name] = min(cur_min, d_min + 1), max(cur_max, d_max + 1)
                else:
                    items[next_name] = d_min + 1, d_max + 1

        return items
    
    # ----------------------------------------------------------------------------------------------------
    # Left items
    # ----------------------------------------------------------------------------------------------------

    @property
    def left_items(self):
        if self._left_items is None:
            self._left_items = self.left_right_items(True)
        return self._left_items
    
    # ----------------------------------------------------------------------------------------------------
    # Right items
    # ----------------------------------------------------------------------------------------------------

    @property
    def right_items(self):
        if self._right_items is None:
            self._right_items = self.left_right_items(False)
        return self._right_items
    
    # ====================================================================================================
    # Arrange
    # ====================================================================================================

    def arrange(self, right_column=[]):
        """ Arrange the content of the frame

        The algorithm is the following:
        - get the peer output nodes of each node
        - the node column is the colum plus one of the left most peer output node
        - particular case: when a node without input has only one output node, it is placed
          in the same column

        Once the columns are build, the are sorted vertically

        Then, the nodes can be placed using the location property of <!Node#bnode>.
        """

        if len(self.children) == 0:
            return
        
        # ---------------------------------------------------------------------------
        # The children must be arranged
        # ---------------------------------------------------------------------------

        for node in self.children:      
            node.arrange()

        # ===========================================================================
        # STEP 1 - Compute the columns
        # ===========================================================================

        # Nodes without items_out are column 0 (rightmost)
        # Input nodes are put in columns left depending on the distance

        col_max = 10_000
        cols = set()
        for node in self.children:

            # Only nodes without items out
            if len(node.items_out):
                continue

            if node.is_reroute:
                node.col = 0
            else:
                node.col = 1

            cols.add(node.col)

            # Other nodes are put left
            for it_name, (d_min, d_max) in node.left_items.items():
                it = self.get_node(it_name)

                # In reroute are left most
                if it.is_reroute:
                    it.col = col_max

                else:
                    new_d_max = node.col + d_max
                    if it.col is None:
                        it.col = new_d_max
                    else:
                        it.col = max(it.col, new_d_max)

                cols.add(it.col)

        # Transform col attribute into a valid list index
        cols = sorted(list(cols))
        transco = {}
        for i, col in enumerate(cols):
            transco[col] = i

        for node in self.children:
            node.col = transco[node.col]

        ncols = len(cols)

        # ===========================================================================
        # STEP 2 - Compute the rows
        # ===========================================================================

        columns    = []
        col_widths = []

        for i_col in range(ncols):

            # ---------------------------------------------------------------------------
            # Current column with its width
            # ---------------------------------------------------------------------------
            
            col_width = 0
            column = []
            for node in self.children:
                if node.col != i_col:
                    continue

                column.append(node)
                col_width = max(col_width, node.width)

            # ---------------------------------------------------------------------------
            # Rows of rightmost column
            # ---------------------------------------------------------------------------

            if i_col == 0:
                # Rightmost colum order
                # First : Output
                # If reroute
                # - Geometry first
                # Else:
                # - Right column
                def order(node):
                    if node.is_group_output:
                        return 0
                    
                    if node.is_reroute:
                        if node.bnode.outputs[0].type == 'GEOMETRY':
                            return 0
                    
                    for i_right, right_item in enumerate(right_column):
                        if right_item in right_column:
                            return 1 + i_right*1000
                        
                    return (len(right_column) + 1)*1000 - len(node.items_in)

                column = sorted(column, key=order)

            # ---------------------------------------------------------------------------
            # Rows of other columns
            # ---------------------------------------------------------------------------

            else:
                def order(node):
                    for i_right, right_node in enumerate(columns[i_col - 1]):
                        rank = right_node.input_rank(node)
                        if rank is not None:
                            return i_right*1000 + rank

                    return len(columns[i_col - 1])*1000
                
                column = sorted(column, key=order)

            # ---------------------------------------------------------------------------
            # Append the column sorted by its row
            # ---------------------------------------------------------------------------

            for i_node, node in enumerate(column):
                node.row = i_node

                if i_col == 0:
                    node.arrange(right_column = right_column)

                if i_col > 0:
                    node.arrange(right_column = columns[i_col-1])

                    for right_node in columns[i_col - 1]:
                        if right_node.name in node.items_out:
                            node.first_right = right_node
                            break

            columns.append(column)
            col_widths.append(col_width)

        # ===========================================================================
        # STEP 3 - Locate the items
        # ===========================================================================

        x = 0
        for icol, (col, col_width) in enumerate(zip(columns, col_widths)):

            assert len(col), f"{icol} : {col}"

            #x -= col_width/2 + X_SEPA

            y = 0
            for node in col:

                #if node.below:
                #    y += Y_SEPA/2

                if node.is_frame:
                    y -= Y_SEPA*5

                # Align vertically to the first right node
                if node.first_right is not None:
                    y = min(y, node.first_right.y)

                node.location = (x - node.width/2, y)
                #node.location = (x, y)

                y -= node.height/2 + Y_SEPA

            x -= col_width/2

            # Sepa proportional to cols width
            if icol < len(columns) - 1:
                max_width = max(col_width, col_widths[icol+1])
            else:
                max_width = col_width
            sepa = round(max(X_SEPA, 0.1*max_width))
            x -= sepa

        # ---------------------------------------------------------------------------
        # Align vertically to the first left node
        # ---------------------------------------------------------------------------

        for col, prev_col in zip(columns[:-1], columns[1:]):
            for i_node, node in enumerate(col):
                for prev in prev_col:
                    if prev.name in node.items_in:
                        offset = prev.y - node.y
                        if offset < 0:
                            for nd in col[i_node:]:
                                nd.y += offset
                                pass
                        break


# ====================================================================================================
# A Node
# ====================================================================================================

class Node(Item):

    def __init__(self, tree, bnode):
        """ > Node wrapper

        Properties
        ----------
        - tree (Tree) : tree wrapper
        - bnode (bpy.types.Node) : wrapped node

        Arguments
        ---------
        - tree (Tree) : the tree to arrange
        - bnode (bpy.types.Node) : the wrapped node
        """
        self.tree  = tree
        self.bnode = bnode

        # Location
        x, y = self.bnode.location
        self.x = int(x)
        self.y = int(y)

        # Topology
        self.reset()

    def reset(self):
        super().reset()

        self._child_bounds = None

        self.col = None
        self.row = None
        self.first_left = None
        self.first_right = None

        # Right and left nodes
        self._out_nodes = None
        self._in_nodes  = None
        self._rights    = None
        self._lefts     = None

    def __str__(self):
        sname = self.bnode.name if self.bnode.label == "" else self.bnode.label
        x, y = self.bnode.location
        w, h = self.dimensions

        return f"<{'Frame' if self.is_frame else 'Node '} {sname:15s} ({x:.0f}, {y:.0f}) [{w:.0f}, {h:.0f}]>"

    def __repr__(self):
        return str(self)

    # ====================================================================================================
    # Node wrapper
    # ====================================================================================================

    @property
    def name(self):
        return self.bnode.name

    @property
    def is_frame(self):
        return self.bnode.bl_idname == 'NodeFrame'

    @property
    def is_temp_frame(self):
        if self.bnode is None:
            return False
        else:
            return self.bnode.label.startswith(TEMP_FRAME)
        
    @is_temp_frame.setter
    def is_temp_frame(self, value):
        if value == True:
            self.bnode.label = TEMP_FRAME
        else:
            self.bnode.label = value

    @property
    def is_reroute(self):
        return self.bnode.bl_idname == 'NodeReroute'

    @property
    def is_layout(self):
        return self.bnode.bl_idname in ['NodeReroute', 'NodeFrame']
    
    @property
    def is_node(self):
        return not self.is_frame
    
    @property
    def counter(self):
        count = len(self.children)
        for child in self.children:
            count += child.counter

    @property
    def is_group_input(self):
        return self.bnode.bl_idname in ['NodeGroupInput']
    
    @property
    def is_group_output(self):
        return self.bnode.bl_idname in ['NodeGroupOutput']
    
    # ====================================================================================================
    # Parent Frame
    # ====================================================================================================

    @property
    def parent(self):
        bparent = self.bnode.parent
        if bparent is None:
            return None
        else:
            return self.tree[bparent.name]
        
    @parent.setter
    def parent(self, value):
        if value is None:
            self.bnode.parent = None
        else:
            self.bnode.parent = value.bnode
        
    def is_in_frame(self, frame):
        """ Is in a frame

        Arguments
        ---------
        - frame (Node) : the frame to test

        Returns
        -------
        - bool : True if the frame belongs to the parents hierarchy
        """
        if self.parent is None:
            return False
        
        elif self.parent == frame:
            return True
        
        else:
            return self.parent.is_in_frame(frame)
        
    # ====================================================================================================
    # Directly linked nodes
    # ====================================================================================================

    @property
    def in_nodes(self):
        """ Direct input nodes

        Returns
        -------
        - set of Nodes : nodes linked to one input socket of the node
        """
        if self._in_nodes is None:
            self._in_nodes = set()
            for socket in self.bnode.inputs:
                for blink in socket.links:
                    self._in_nodes.add(self.tree.nodes[blink.from_node.name])
        
        return self._in_nodes

    @property
    def out_nodes(self):
        """ Direct output nodes

        Returns
        -------
        - set of Nodes : nodes linked to one output socket of the node
        """
        if self._out_nodes is None:
            self._out_nodes = set()
            for socket in self.bnode.outputs:
                for blink in socket.links:
                    self._out_nodes.add(self.tree.nodes[blink.to_node.name])

        return self._out_nodes

    # ====================================================================================================
    # Right and left nodes
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Build the dicts
    # ----------------------------------------------------------------------------------------------------

    def left_right_nodes(self, left: bool):
        """ All the nodes linked to node input sockets

        Arguments
        ---------
        - left (bool) : left or right nodes

        Returns
        -------
        - dict : name -> (min dist, max dist)
        """

        nodes = {}

        # ---------------------------------------------------------------------------
        # The list of directly linked nodes (dist min = 1)
        # ---------------------------------------------------------------------------

        base = self.in_nodes if left else self.out_nodes
        for node in base:
            nodes[node.name] = (1, 1)

        # ---------------------------------------------------------------------------
        # Add the linked nodes of these nodes
        # ---------------------------------------------------------------------------

        ends = ZONE_INPUTS if left else ZONE_OUTPUTS

        for node in [self.tree.nodes[node_name] for node_name in nodes]:

            if node.bnode.bl_idname in ends:
                continue

            loop_list = node.lefts if left else node.rights
            for next_name, (d_min, d_max) in loop_list.items():
                if next_name in nodes:
                    cur_min, cur_max = nodes[next_name]
                    nodes[next_name] = min(cur_min, d_min + 1), max(cur_max, d_max + 1)
                else:
                    nodes[next_name] = d_min + 1, d_max + 1

        return nodes
    
    # ----------------------------------------------------------------------------------------------------
    # Left nodes
    # ----------------------------------------------------------------------------------------------------

    @property
    def lefts(self):
        if self._lefts is None:
            self._lefts = self.left_right_nodes(True)
        return self._lefts
    
    # ----------------------------------------------------------------------------------------------------
    # Right nodes
    # ----------------------------------------------------------------------------------------------------

    @property
    def rights(self):
        if self._rights is None:
            self._rights = self.left_right_nodes(False)
        return self._rights
    
    # ====================================================================================================
    # Link order
    # ====================================================================================================

    def input_rank(self, node):
        """ Return the link input rank of a left node

        Returns
        -------
        - int : the linked order, None if not linked
        """
        rank = 0
        for socket in self.bnode.inputs:
            for blink in socket.links:
                if blink.from_node.name == node.name:
                    return rank
            rank += 1

        return None
    
    # ====================================================================================================
    # Child bounds
    # ====================================================================================================

    @property
    def child_bounds(self):
        """ Child nodes bounds

        CAUTION : height is top down when y is from down to top. Moreover, dimensions are
        doubled in the coordinates space

        Node top :      y
                        |
        Node bottom :  y-h/2

        HENCE : x0, y0 is the left bottom corner (smallest y)

        top left corner is : (x0, y1)
        dims is : (x1 - x0), (y1 - y0)
        """
        if not len(self.children):
            return None
        
        if self._child_bounds is None:
            X0 = None
            for child in self.children:

                w, h = child.dimensions
                x0, y0, x1, y1 = child.x, child.y - round(h/2), child.x + round(w/2), child.y

                if X0 is None:
                    X0, Y0, X1, Y1 = x0, y0, x1, y1
                else:
                    X0, Y0, X1, Y1 = min(X0, x0), min(Y0, y0), max(X1, x1), max(Y1, y1)

            self._child_bounds = X0, Y0, X1, Y1

        return self._child_bounds
    
    # ====================================================================================================
    # Location
    # ====================================================================================================

    @property
    def location(self):
        return self.x, self.y

    @location.setter
    def location(self, value):
        x, y = value
        self.x, self.y = round(x), round(y)

    def location_to_node(self):

        if self.is_node or (len(self.children) == 0):
            self.bnode.location = (self.x, self.y)
            return
        
        x0, _, _, y0 = self.child_bounds

        for child in self.children:
            child.x -= x0 # + 30
            child.y -= y0 # - 36
            child.location_to_node()

        self.bnode.location = (self.x, self.y)

    # ====================================================================================================
    # Dimensions
    # ====================================================================================================

    @property
    def dimensions(self):

        # ---------------------------------------------------------------------------
        # Frame
        # ---------------------------------------------------------------------------

        if self.is_frame:
            if len(self.children):
                x0, y0, x1, y1 = self.child_bounds
                return (x1 - x0)*2 + 120, (y1 - y0)*2 + 132
            else:
                return 0, 0

        # ---------------------------------------------------------------------------
        # Node
        # ---------------------------------------------------------------------------

        # Dimensions are directly available
        if self.tree.use_true_dims:
            w, h = self.bnode.dimensions
            return round(w), round(h)
        
        # ----- Input Socket height

        def socket_height(socket):
            
            if not socket.enabled:
                return 0
            
            if socket.hide_value:
                h = SOCKET
                
            else:
                if socket.type == 'VECTOR':
                    if socket.is_linked:
                        h = 24
                    else:
                        h = 148
                        
                elif socket.type == 'BOOLEAN':
                    h = 42
                    
                else:
                    h = SOCKET

            return h
        
        # ----- Node height

        HEADER    = 56
        SOCKET    = 44
        SOCK_SEPA =  6
    
        # out height
        out_height = 0
        for socket in self.bnode.outputs:
            out_height += SOCKET
            
        # in height
        in_height = 0
        for socket in self.bnode.inputs:
            in_height += socket_height(socket)
            
        height = HEADER  + out_height + in_height
        if in_height and out_height:
            height += SOCK_SEPA
            
        # Delta from constant array
        dims = NODE_INFO[self.bnode.bl_idname]['dims']
        return dims[0], dims[2] + height
    
    @property
    def width(self):
        """ Node width

        Returns
        -------
        - float : node width
        """
        return round(self.dimensions[0])

    @property
    def height(self):
        """ Node height

        Returns
        -------
        - float : node height
        """
        return round(self.dimensions[1])     
    


# ====================================================================================================
# Tree Wrapper
# ====================================================================================================

class Tree(Item):
    def __init__(self, btree, no_empty_frame=True):
        """ > Tree wrapper

        Properties
        -----------
        - btree (bpy.types.Tree)

        Arguments
        ---------
        - btree (bpy.types.Tree) : the tree to wrap
        """        
        if isinstance(btree, str):
            btree = bpy.data.node_groups[btree]

        self.btree       = btree
        self.input_node  = None
        self.output_node = None

        # ---------------------------------------------------------------------------
        # Delete empty frames
        # ---------------------------------------------------------------------------

        if no_empty_frame:
            frames = []
            not_empty = set()
            for node in self.btree.nodes:
                if node.bl_idname == 'NodeFrame':
                    frames.append(node)
                else:
                    par = node.parent
                    while par is not None:
                        not_empty.add(par.name)
                        par = par.parent

            for frame in frames:
                if frame.name not in not_empty:
                    self.btree.nodes.remove(frame)

        # ---------------------------------------------------------------------------
        # Nodes
        # ---------------------------------------------------------------------------

        self.nodes  = {}
        for bnode in self.btree.nodes:
            new_node = Node(self, bnode)
            self.nodes[new_node.name] = new_node

            if bnode.bl_idname == 'NodeGroupOutput':
                bnode.parent = None
                if self.output_node is None:
                    self.output_node = new_node

            elif bnode.bl_idname == 'NodeGroupInput':
                if bnode.parent is None or self.input_node is None:
                    self.input_node = new_node

        # ---------------------------------------------------------------------------
        # Links
        # ---------------------------------------------------------------------------

        self.links = [Link(self, blink) for blink in self.btree.links]

        # ---------------------------------------------------------------------------
        # Zones
        # ---------------------------------------------------------------------------

        """
        self.zones = []
        for node in self.nodes.values():
            if node.bnode.bl_idname not in ZONE_INPUTS:
                continue

            # Shouldn't occur, but just in case
            if node.bnode.paired_output is None:
                continue

            self.zones.append(Zone(self, node, self.nodes[node.bnode.paired_output.name]))
        """

    def __str__(self):
        return f"<Tree {self.btree.name} {len(self.nodes)} nodes>"
    
    def get_node(self, name):
        return self.nodes[name]

    # ====================================================================================================
    # As a list of nodes
    # ====================================================================================================

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.nodes[index]

        elif isinstance(index, bpy.types.NodeInternal):
            return self.nodes[index.name]

        raise AttributeError(f"Node index not valid: {index}")
    
    # ====================================================================================================
    # Nodes management
    # ====================================================================================================

    def new_node(self, bl_idname, frame=None):
        bnode = self.btree.nodes.new(bl_idname)
        bnode.select = False
        node = Node(self, bnode)
        self.nodes[bnode.name] = node

        if frame is not None:
            bnode.parent = frame.bnode

        return node

    def new_frame(self, frame=None, temp=False):
        frame = self.new_node('NodeFrame', frame=frame)
        if temp:
            frame.is_temp_frame = True
        return frame

    def new_reroute(self, frame=None):
        return self.new_node('NodeReroute', frame=frame)

    def del_node(self, node):
        for link in self.links:
            if link.node0 == node or link.node1 == node:
                raise Exception(f"Impossible to delete  node {node}, links still exist")

        if self.input_node == node:
            self.input_node = None
        if self.output_node == node:
            self.output_node = None

        del self.nodes[node.bnode.name]
        self.btree.nodes.remove(node.bnode)

    def del_frame(self, node):
        del self.nodes[node.name]
        self.btree.nodes.remove(node.bnode)


    def del_link(self, link):
        self.btree.links.remove(link.blink)
        self.links.remove(link)

    def new_link(self, node0, index0, node1, index1):
        blink = self.btree.links.new(node0.bnode.outputs[index0], node1.bnode.inputs[index1])
        link = Link(self, blink)
        self.links.append(link)
        return link
    
    # ====================================================================================================
    # Reroutes
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Delete the reroute nodes
    # ----------------------------------------------------------------------------------------------------

    def del_reroutes(self):
        """ > Delete reroute nodes
        """
        reroutes = [node for node in self.nodes.values() if node.is_reroute]
        for reroute in reroutes:
            in_links  = []
            out_links = []
            for link in self.links:
                if link.node0 == reroute:
                    out_links.append(link)
                if link.node1 == reroute:
                    in_links.append(link)

            if len(in_links) == 0:
                for link in out_links:
                    self.del_link(link)

            else:
                assert(len(in_links) == 1)

                for link in out_links:
                    link.replace_from(in_links[0].node0, in_links[0].index0)

                self.del_link(in_links[0])

            self.del_node(reroute)

    # ----------------------------------------------------------------------------------------------------
    # Build frame inputs as reroute nodes
    # ----------------------------------------------------------------------------------------------------

    def insert_reroutes(self):

        frames = [node for node in self.nodes.values() if node.is_frame]

        for frame in frames:

            if frame.is_temp_frame:
                continue

            # ----- All the links between a node inside the frame and a node outside the frame

            in_links = []
            out_links = []
            for link in self.links:
                if link.node0.is_in_frame(frame):
                    if not link.node1.is_in_frame(frame):
                        out_links.append(link)
                else:
                    if link.node1.is_in_frame(frame):
                        in_links.append(link)

            # ----- Create input reroutes

            source_nodes = {}
            for link in in_links:
                source_key = link.node0_key
                reroute = source_nodes.get(source_key)
                if reroute is None:
                    reroute = link.insert_reroute(frame)
                    source_nodes[source_key] = reroute

                else:
                    link.replace_from(reroute, index0=0)

            # ----- Create the output reroutes

            source_nodes = {}
            for link in out_links:
                source_key = link.node0_key
                reroute = source_nodes.get(source_key)
                if reroute is None:
                    reroute = link.insert_reroute(frame)
                    source_nodes[source_key] = reroute

                else:
                    link.replace_from(reroute, index0=0)

    # ====================================================================================================
    # Group input management
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # The current list of group input nodes
    # ----------------------------------------------------------------------------------------------------

    @property
    def group_inputs(self):
        """ > List of Group Input nodes

        Returns
        -------
        - list of nodes : nodes with bl_idname equal to 'NodeGroupInput'
        """
        return [node for node in self.nodes.values() if node.bnode.bl_idname == 'NodeGroupInput']

    # ----------------------------------------------------------------------------------------------------
    # Keep one single gorup output
    # ----------------------------------------------------------------------------------------------------

    def single_group_input(self):
        """ > Keep only one Group Input node

        Remove all the ***Goup Input*** node but one.
        The remaining one is placed out of any frame
        """

        inputs = self.group_inputs
        if len(inputs) <= 1:
            return

        group_input = inputs[0]
        for link in self.links:
            if link.node0 not in inputs[1:]:
                continue

            link.replace_from(group_input)

        for node in inputs[1:]:
            self.del_node(node)
            self.input_node = None

        group_input.bnode.parent = None

    # ----------------------------------------------------------------------------------------------------
    # Create one group input per frame
    # ----------------------------------------------------------------------------------------------------

    def group_input_per_frame(self, all_frames: bool = False):
        """ Create one group input node per frame linked to the group input
        """

        # ---------------------------------------------------------------------------
        # One single group input
        # ---------------------------------------------------------------------------

        self.single_group_input()
        inputs = self.group_inputs
        if len(inputs) == 0:
            return

        assert(len(inputs) == 1)
        group_input = inputs[0]

        # ---------------------------------------------------------------------------
        # frames dict : frame -> list of links from group input to one of its nodes
        # ---------------------------------------------------------------------------

        frame_links = {}
        frame_depths = {}
        total = 0
        for link in self.links:

            # Only links from Group Input to a node within a Frame

            if link.node0 != group_input:
                continue

            total += 1

            frame = link.node1.parent
            if frame is None:
                continue

            # We register the link in the dict

            links = frame_links.get(frame.name)
            if links is None:
                frame_links[frame.name] = [link]
            else:
                links.append(link)

            # The depths
            depth = 0
            cur = frame
            while cur.parent is not None:
                depth -= 1
                cur = cur.parent
            frame_depths[frame.name] = depth

        # ---------------------------------------------------------------------------
        # For frames with less than MIN_INPUT_LINKS, transfer the links to its parent
        # ---------------------------------------------------------------------------
        
        if not all_frames:
            # Loop on frame links starting from max depth
            for frame_name in sorted(frame_depths, key=frame_depths.get):
                links = frame_links[frame_name]

                if len(links) >= MIN_INPUT_LINKS:
                    continue

                parent = self.nodes[frame_name].parent
                while (parent is not None) and (parent.name not in frame_links):
                    parent = parent.parent

                if parent is not None:
                    frame_links[parent.name].extend(links)
                    del frame_links[frame_name]

        # ---------------------------------------------------------------------------
        # Create one group input per frame
        # ---------------------------------------------------------------------------

        for frame_name, links in frame_links.items():

            frame = self.nodes[frame_name]

            frame_input = self.new_node('NodeGroupInput', frame)

            frame_input.bnode.use_custom_color = True
            frame_input.bnode.color = (.11, .11, .11)

            #Plug the links to the frame group input
            for link in links:
                link.replace_from(frame_input)

            total -= len(links)

        if False:
            frames = {}
            for link in self.links:
                if link.node0 != group_input:
                    continue

                frame = link.node1.parent
                if frame is None:
                    continue

                # Only top frames or frame with more than 5 links
                if not all:
                    while frame.parent is not None:
                        frame = frame.parent

                # Create the frame group input if it doesn't already exist
                frame_input = frames.get(frame.name)
                if frame_input is None:
                    frame_input = self.new_node('NodeGroupInput', frame)
                    frame_input.bnode.use_custom_color = True
                    frame_input.bnode.color = (.11, .11, .11)
                    frames[frame.name] = frame_input

                # Replace the link to the frame group input
                link.replace_from(frame_input)

        # ---------------------------------------------------------------------------
        # Keep if outputs remain
        # ---------------------------------------------------------------------------

        if True:
            assert total >= 0, "Oups"
            if total == 0:
                self.del_node(group_input)

        else:
            keep = False
            for link in self.btree.links:
                if link.from_node == group_input.bnode:
                    keep = True
                    break
            if not keep:
                self.del_node(group_input)

    # ====================================================================================================
    # Zones in frames
    # ====================================================================================================

    def zones_in_frame(self):
        """ Create a temporary frame around zones
        """

        # ---------------------------------------------------------------------------
        # Get the existing zones
        # ---------------------------------------------------------------------------

        zones = []
        for node in self.nodes.values():
            if node.bnode.bl_idname not in ZONE_INPUTS:
                continue

            if node.bnode.paired_output is None:
                continue

            zone_input  = node
            zone_output = self[node.bnode.paired_output]
            zone_nodes = [zone_input] + [self.nodes[name] for name in zone_input.rights]

            # The frame can be created only if all the zone nodes belong
            # to the input node frame

            zone_frame = zone_input.parent
            change = zone_frame is None
            
            if not change:
                change = True
                for node in zone_nodes:
                    if not node.is_in_frame(zone_frame):
                        change = False
                        break

            # In addition, no zone node must belongs to a frame owning anoter input node

            if change:
                frames = set()
                for node in zone_nodes:
                    if node.parent is None or node.parent in frames:
                        continue
                    cur = node.parent
                    for cur_node in self.nodes.values():
                        if (cur_node.parent != cur) or (cur_node in zone_nodes):
                            continue

                        for prev_name in list(cur_node.lefts.keys()) + [cur_node.name]:
                            prev = self.nodes[prev_name]
                            if prev.bnode.bl_idname in INPUT_NODES and prev != zone_input:
                                change = False
                                break

                        if not change:
                            break
                    if not change:
                        break

                    frames.add(cur)

            if change:
                zones.append((zone_frame, zone_nodes))

        # ---------------------------------------------------------------------------
        # Change the owning frames
        # ---------------------------------------------------------------------------

        for zone_frame, zone_nodes in zones:

            new_frame = self.new_frame(temp=True)
            new_frame.parent = zone_frame
            for node in zone_nodes:
                cur = node
                while cur.parent != new_frame and cur.parent != zone_frame:
                    cur = cur.parent
                if cur.parent == zone_frame:
                    cur.parent = new_frame

    # ====================================================================================================
    # Delete temporary frames
    # ====================================================================================================

    def del_temp_frames(self):
        """ Delete temporary frames
        """
        to_del = set()
        for node in self.nodes.values():
            if node.parent is None:
                continue
            if node.parent.is_temp_frame:
                to_del.add(node.parent)
                node.parent = node.parent.parent

        for frame in to_del:
            self.del_frame(frame)

    # ====================================================================================================
    # Hierarchy
    # ====================================================================================================

    def build_hierarchy(self):

        # ---------------------------------------------------------------------------
        # Reset
        # ---------------------------------------------------------------------------

        self.reset()
        for node in self.nodes.values():
            node.reset()

        # ---------------------------------------------------------------------------
        # Hierarchy
        # ---------------------------------------------------------------------------

        for node in self.nodes.values():
            if node.parent is None:
                self.append(node)
            else:
                self.nodes[node.parent.name].append(node)

        # ---------------------------------------------------------------------------
        # Link simplification
        # ---------------------------------------------------------------------------
        """
        A link between two nodes is transformed in a link between two items:
        - if the nodes have the same owner, the link is between their item
        - if the nodes don'ts share the same owner, the link is created between the two
          owner nodes sharing the same parent. For instance if is link exists beteween the
          nodes [Top > Frame > Frame B > Node 1] and [Top > Frame > Node 2], the item link
          is between [Frame B] and [Node 2].

        The item link is stored in:
        - The outputs dict of the first item
        - The inputs dict of the second item

        The key of the dicts is the item name, the value is the list of Node Links.

        Similarily, the items where the links go through maintain the dicts of passing through links:
        - through_in
        - through_out

        For exemple, if a link exists between the two nodes:
        - Top > Frame > Frame A > Frame B > Node 1
        - Top > Frame > Node 2
        """

        for link in self.links:

            # Owner nodes sharing the same owner

            _, node0, node1 = link.node0.common_ancestor(link.node1)

            # Update direct
            #   avoiding strange case of a node being both in and out,
            #   this could happen with frames.
            if node0.name not in node1.items_out:
                if node0.name in node1.items_in:
                    node1.items_in[node0.name].append(link)
                else:
                    node1.items_in[node0.name] = [link]

            if node1.name not in node0.items_in:
                if node1.name in node0.items_out:
                    node0.items_out[node1.name].append(link)
                else:
                    node0.items_out[node1.name] = [link]

            # Update through

            cur = link.node0
            while cur != node0:
                if node1.name in cur.through_out:
                    cur.through_out[node1.name].append(link)
                else:
                    cur.through_out[node1.name] = [link]
                cur = cur.owner

            cur = link.node1
            while cur != node1:
                if node0.name in cur.through_in:
                    cur.through_in[node0.name].append(link)
                else:
                    cur.through_in[node0.name] = [link]
                cur = cur.owner
    
    # ====================================================================================================
    # There is a Node editor
    # ====================================================================================================

    def wait(self):
        if self.use_true_dims:
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

    @property
    def use_true_dims(self):

        for area in bpy.context.screen.areas:
            if area.type == 'NODE_EDITOR':
                for space in area.spaces:
                    if space.type == 'NODE_EDITOR' and space.node_tree == self.btree:
                        return True

        return False
    
    # ====================================================================================================
    # Arrange
    # ====================================================================================================

    def arrange(self, reroutes: bool = True, single_input: bool = False):
        """ Nodes arrangement

        Arguments
        ---------
        - reroutes (bool = True) : insert reroutes in frames as in / out sockets
        - single_input (bool = False) : one single Group Input node or one per top frame
        """

        # ---------------------------------------------------------------------------
        # Prepare
        # ---------------------------------------------------------------------------

        # No reroute (we are in auto arrangement !)
        self.del_reroutes()

        # One input per frame
        if single_input:
            self.single_group_input()
        else:
            self.group_input_per_frame(all_frames=False)

        # Zones to temmp frames
        self.zones_in_frame()

        # Insert reroutes
        if reroutes:
            self.insert_reroutes()

        # ---------------------------------------------------------------------------
        # Arrange
        # ---------------------------------------------------------------------------

        self.build_hierarchy()
        self.wait()
        super().arrange()

        # ---------------------------------------------------------------------------
        # Finalize
        # ---------------------------------------------------------------------------

        # From virtual to actual location
        for child in self.children:
            child.location_to_node()

        # Delete temp frames
        self.del_temp_frames()


# ====================================================================================================
# Main - Arrange a tree
# ====================================================================================================

def arrange(btree, reroutes: bool = None, single_input: bool = None):

    tree = Tree(btree)

    if reroutes is None:
        reroutes = getattr(bpy.context.scene, 'arrange_reroutes', True)
    if single_input is None:
        single_input = getattr(bpy.context.scene, 'arrange_single_input', False)

    tree.arrange(reroutes=reroutes, single_input=single_input)


# ====================================================================================================
# UI

# bl_region_type in
# ('WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF',
# 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR')

class ArrangeNodesOperator(bpy.types.Operator):
    """Auto arrange nodes"""
    bl_idname = "node.arrange_nodes"
    bl_label  = "Arrange nodes"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR' and space.edit_tree is not None

    def execute(self, context):
        space = context.space_data

        reroutes = context.scene.arrange_reroutes
        single_input = context.scene.arrange_single_input

        arrange(space.edit_tree, reroutes=reroutes, single_input=single_input)
        
        return {'FINISHED'}

class NodeDumpOperator(bpy.types.Operator):
    """Node dump"""
    bl_idname = "node.dump_node"
    bl_label  = "Node Help"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        if space.type != 'NODE_EDITOR' or space.edit_tree is None:
            return False
        nodes = [node for node in space.edit_tree.nodes if node.select]
        return len(nodes) > 0

    def execute(self, context):

        from geonodes.generation.node_explore import NodeInfo

        space = context.space_data
        tree = space.edit_tree
        nodes = [node for node in tree.nodes if node.select]

        txt_name = 'Node Help'

        if len(nodes) == 0:
            print("Node Help: you must select at least one node.")

        else:
            NodeInfo.dump_nodes(tree, nodes, target=txt_name)
            if len(nodes) == 1:
                print(f"Node Help: help on '{nodes[0].name}' available in '{txt_name}'")
            else:
                print(f"Node Help: help on {len(nodes)} nodes available in '{txt_name}'")

        return {'FINISHED'}

class LayoutArrangePanel(bpy.types.Panel):
    """Creates a Panel in the node editor context of the properties editor"""
    bl_label       = "Module geonodes"
    bl_idname      = "NODE_EDITOR_PT_arrange"
    bl_space_type  = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context     = "scene"
    bl_category    = "Tool"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Node dump
        row = layout.row()
        #row.scale_y = 2.0
        row.operator("node.dump_node")

        # Reroutes
        layout.prop(scene, "arrange_reroutes")
        layout.prop(scene, "arrange_single_input")

        # Arrange
        row = layout.row()
        row.scale_y = 2.0
        row.operator("node.arrange_nodes")

        # Remove reroutes
        #row = layout.row()
        #row.operator("node.remove_reroutes")

def register():
    try:
        bpy.types.Scene.arrange_reroutes = bpy.props.BoolProperty(
            name="Reroutes",
            description="Add reroute nodes in layouts",
            default=True,
        )
        bpy.types.Scene.arrange_single_input = bpy.props.BoolProperty(
            name="Single Group Input",
            description="One single Group Input or create duplicates in layouts",
            default=False,
        )

        #bpy.utils.register_class(RemoveReroutesOperator)
        bpy.utils.register_class(ArrangeNodesOperator)
        bpy.utils.register_class(NodeDumpOperator)

        bpy.utils.register_class(LayoutArrangePanel)
    except:
        pass

def unregister():
    try:
        #bpy.utils.unregister_class(RemoveReroutesOperator)
        bpy.utils.unregister_class(ArrangeNodesOperator)
        bpy.utils.unregister_class(NodeDumpOperator)

        bpy.utils.unregister_class(LayoutArrangePanel)

        del bpy.types.Scene.arrange_reroutes
        del bpy.types.Scene.arrange_single_input
    except:
        pass

