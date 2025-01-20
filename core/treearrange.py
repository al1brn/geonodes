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

X_SEPA = 60
Y_SEPA = 40
ZONE_INPUTS  = ['GeometryNodeRepeatInput', 'GeometryNodeSimulationInput', 'GeometryNodeForeachGeometryElementInput']
ZONE_OUTPUTS = ['GeometryNodeRepeatOutput', 'GeometryNodeSimulationOutput', 'GeometryNodeForeachGeometryElementOutput']

# =============================================================================================================================
# A link

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
        self.index0 = list(blink.from_node.outputs).index(blink.from_socket)
        self.index1 = list(blink.to_node.inputs).index(blink.to_socket)

    def __str__(self):
        return f"<Link [{self.node0.bnode.name}]({self.index0}) -> [{self.node1.bnode.name}]({self.index1})>"

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
        node_lab = self.node0.bnode.label
        if node_lab is None or node_lab == '':
            reroute.bnode.label = self.blink.from_socket.name
        else:
            reroute.bnode.label = node_lab

        # ----- From source node to reroute
        self.tree.new_link(self.node0, self.index0, reroute, 0)

        # ----- From reroute to target node
        self.replace_from(reroute, index0 = 0)

        return reroute


# =============================================================================================================================
# Node

class Node:

    def __init__(self, tree, bnode):
        """ > Node wrapper

        Properties
        ----------
        - tree (Tree) : tree wrapper
        - bnode (bpy.types.Node) : wrapped node
        - parent (Node) : parent node if any

        Arguments
        ---------
        - tree (Tree) : the tree to arrange
        - bnode (bpy.types.Node) : the wrapped node
        """
        self.tree  = tree
        self.bnode = bnode

    def __str__(self):
        sname = self.bnode.name if self.bnode.label == "" else self.bnode.label
        return f"<Node '{sname}'>"

    def __repr__(self):
        return str(self)

    def dump(self, depth=0):
        print("   "*depth, '-', str(self))

    @property
    def is_frame(self):
        return self.bnode.bl_idname == 'NodeFrame'

    @property
    def is_reroute(self):
        return self.bnode.bl_idname == 'NodeReroute'

    @property
    def is_layout(self):
        return self.bnode.bl_idname in ['NodeReroute', 'NodeFrame']

    @property
    def parent(self):
        bparent = self.bnode.parent
        if bparent is None:
            return self.tree
        else:
            return self.tree[bparent]

    # ====================================================================================================
    # Dimensions

    @property
    def has_node_editor(self):

        if not self.tree.get_true_dims:
            return False

        for area in bpy.context.screen.areas:
            if area.type == 'NODE_EDITOR':
                for space in area.spaces:
                    if space.type == 'NODE_EDITOR' and space.node_tree == self.tree.btree:
                        return True

        return False

    @classmethod
    def wait(cls):
        if False and cls.has_node_editor:
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

    @property
    def dimensions(self):
        """ Node dimensions

        Node dimensions are read from bnode if it is available in 'NODE_EDITOR' area.
        Otherwise, dimensions are approximated

        Returns
        -------
        - couple of floats : node dimensions
        """

        BASE_WIDTH           = 400
        BASE_HEIGHT          = 56*4
        SOCKET_HEIGHT        = 44
        PARAM_HEIGHT         = 53
        VECTOR_SOCKET_HEIGHT = 164

        if self.has_node_editor:
            return self.bnode.dimensions

        height = BASE_HEIGHT*2

        # ----- Input sockets

        count = 0
        for bsock in self.bnode.inputs:
            if not bsock.enabled:
                continue

            if bsock.type == 'VECTOR' and not bsock.is_linked:
                height += VECTOR_SOCKET_HEIGHT
            else:
                height += SOCKET_HEIGHT

            count += 1

        # ----- Output sockets

        for bsock in self.bnode.outputs:
            if not bsock.enabled:
                continue

            height += SOCKET_HEIGHT

            count += 1

        return (BASE_WIDTH, height/2)

    @property
    def width(self):
        """ Node width

        Returns
        -------
        - float : node width
        """
        return self.dimensions[0]

    @property
    def height(self):
        """ Node height

        Returns
        -------
        - float : node height
        """
        return self.dimensions[1]

    # ====================================================================================================
    # Input / output nodes

    @property
    def in_nodes(self):
        """ List of input nodes

        Returns
        -------
        - list of Nodes : nodes linked to one input socket of the node
        """
        in_nodes = []
        for link in self.tree.links:
            if link.node1 == self:
                in_nodes.append(link.node0)
        return in_nodes

    @property
    def out_nodes(self):
        """ List of output nodes

        Returns
        -------
        - list of Nodes : nodes linked to one output socket of the node
        """
        out_nodes = []
        for link in self.tree.links:
            if link.node0 == self:
                out_nodes.append(link.node1)

        return out_nodes

    # =============================================================================================================================
    # Hierarchy

    def is_child_of(self, frame):
        """ Belongs to the frame

        Returns
        -------
        - bool : True if the frame belongs to the parents hierarchy
        """
        if self.parent is None:
            return False
        elif self.parent == frame:
            return True
        else:
            return self.parent.is_child_of(frame)

    # =============================================================================================================================
    # Peer / outside

    def split_peers(self, nodes):
        """ Separate peer nodes from the other

        Nodes are peer when they share the same parent.

        This method splits the list of nodes in two list:
        - nodes inside the parent of self
        - nodes outside the parent of self

        The first list returns the ancestor of the node sharing the parent of self, not
        the node passed in the list.

        Arguments
        ---------
        - nodes (list of Nodes) : the list to split

        Returns
        -------
        - tuple of lists : peer nodes and not peer nodes
        """
        peers     = []
        not_peers = []
        for node in nodes:
            n = node
            while True:
                if n.parent is None:
                    not_peers.append(node)
                    break

                if n.parent == self.parent:
                    peers.append(n)
                    break

                n = n.parent

        return list(set(peers)), list(set(not_peers))

    # =============================================================================================================================
    # Forward / backward iterators

    def forwards(self):
        """ Iterate forwards

        Iterates on the right nodes

        Returns
        -------
        - Node
        """
        for link in self.tree.links:
            if link.node0 == self:
                yield link.node1
                for node in link.node1.forwards():
                    yield node

    def backwards(self):
        """ Iterate backwards

        Iterates on the left nodes

        Returns
        -------
        - Node
        """
        for link in self.tree.links:
            if link.node1 == self:
                yield link.node0
                for node in link.node0.backwards():
                    yield node

    # =============================================================================================================================
    # Is in zone

    def in_zone(self, input_node, output_node):
        """ The node belongs to a zone

        A node belongs to the zone if the zone input is linked to the node inputs
        and if the zone output is linked to the node outputs.

        Returns
        -------
        - bool : True if the node is in the zone
        """

        # ----- Frame algo
        # - Must feed output_zone and not another zone output
        # - Must not be fed by another zone input ???

        if self.is_frame:

            if self.bnode.parent is not None:
                return False

            ok = False
            for node in self.forwards():

                # NO : Feed an zone input

                if node.bnode.bl_idname in ZONE_INPUTS:
                    return False

                # A zone output : must be the zone we test

                if node.bnode.bl_idname in ZONE_OUTPUTS:
                    if node != output_node:
                        return False
                    else:
                        ok = True
                        break

            if not ok:
                return False

            # Not fed by the zone input

            for node in self.backwards():
                if node.bnode.bl_idname in ZONE_INPUTS:
                    if node != input_node:
                        return False
                    else:
                        return True

            return False

        # ----- Node algo

        ok = False
        for node in self.forwards():
            if node == output_node:
                ok = True
                break

        if not ok:
            return False

        for node in self.backwards():
            if node == input_node:
                return True

        return False

# =============================================================================================================================
# Frame

class Frame(Node):

    def __init__(self, tree, bnode):
        """ Frame node

        Properties
        ----------
        - input_node (Node)
        - output_node (Node)

        Arguments
        ---------
        - tree (Tree) : tree wrapper
        - bnode (bpy.types.Node) : the node of type 'NodeFrame'
        """

        assert(bnode is None or bnode.bl_idname == 'NodeFrame')

        super().__init__(tree, bnode)
        self.input_node  = None
        self.output_node = None

    def __str__(self):
        sname = "No name" if self.bnode.label == "" else self.bnode.label
        return f"<Frame '{sname}', {len(self.children)} nodes>"

    def dump(self, depth=0):
        super().dump(depth)
        print("   "*depth, "  In nodes: ", [node.bnode.name for node in self.in_nodes])
        print("   "*depth, "  Out nodes:", [node.bnode.name for node in self.out_nodes])
        for child in self.children:
            child.dump(depth + 1)

    # =============================================================================================================================
    # Children

    @property
    def children(self):
        """ Child nodes

        Returns
        -------
        - list of Nodes : the nodes directly parented to the frame
        """
        return [node for node in self.tree.nodes.values() if node.bnode.parent == self.bnode]

    @property
    def all_children(self):
        """ All child nodes

        Returns
        -------
        - list of Nodes : the nodes parented, directly or not, to the frame
        """
        return [node for node in self.tree.nodes.values() if node.is_child_of(self)]

    # =============================================================================================================================
    # Forward / backward iterators

    def forwards(self):
        """ Iterate forwards

        Iterates on the right nodes

        Returns
        -------
        - Node
        """
        for link in self.tree.links:
            if link.node0.is_child_of(self):
                if link.node1.is_child_of(self):
                    continue
                yield link.node1
                for node in link.node1.forwards():
                    if not node.is_child_of(self):
                        yield node

    def backwards(self):
        """ Iterate backwards

        Iterates on the left nodes

        Returns
        -------
        - Node
        """
        for link in self.tree.links:
            if link.node1.is_child_of(self):
                if link.node0.is_child_of(self):
                    continue
                yield link.node0
                for node in link.node0.backwards():
                    if not node.is_child_of(self):
                        yield node

    # =============================================================================================================================
    # Frame dimension

    @property
    def dimensions(self):

        if self.has_node_editor:
            dims = self.bnode.dimensions
            return (dims[0] + 120, dims[1] + 120)

        W0, W1, H0, H1 = 0, 400, 0, 400

        for inode, node in enumerate(self.children):

            ndim = node.dimensions

            w1 = 2*node.bnode.location[0]
            w0 = 2*node.bnode.location[0] - ndim[0]
            h0 = 2*node.bnode.location[1] - ndim[1]
            h1 = 2*node.bnode.location[1]

            if inode == 0:
                W0, W1, H0, H1 = w0, w1, h0, h1

            else:
                W0 = min(W0, w0)
                W1 = max(W1, w1)
                H0 = min(H0, h0)
                H1 = max(H1, h1)

        return ((W1 - W0) + 120, (H1 - H0) + 120)

    # ====================================================================================================
    # Input / output nodes

    @property
    def in_nodes(self):
        """ List of input nodes

        An input node of a frame is an input node of a node belonging to the frame
        but which is not in the frame.

        Returns
        -------
        - list of Nodes : the frame input nodes
        """
        in_nodes = []
        for child in self.children:
            for node in child.in_nodes:
                if node in in_nodes:
                    continue

                if not node.is_child_of(self):
                    in_nodes.append(node)
        return in_nodes

    @property
    def out_nodes(self):
        """ List of output nodes

        An output node of a frame is an output node of a node belonging to the frame
        but which is not in the frame.

        Returns
        -------
        - list of Nodes : the frame output nodes
        """
        out_nodes = []
        for child in self.children:
            for node in child.out_nodes:
                if node in out_nodes:
                    continue

                if not node.is_child_of(self):
                    out_nodes.append(node)
        return out_nodes

    # =============================================================================================================================
    # Frame "input / output"

    # ----------------------------------------------------------------------------------------------------
    # Build frame inputs as reroute nodes

    def frame_reroutes(self):

        # ----- All the links between a node inside the frame and a node outside the frame

        in_links = []
        out_links = []
        for link in self.tree.links:
            if link.node0.is_child_of(self):
                if not link.node1.is_child_of(self):
                    out_links.append(link)
            else:
                if link.node1.is_child_of(self):
                    in_links.append(link)

        # ----- Create input reroutes

        x_sepa  = 30
        y_sepa  = 50

        x = -self.width/2  - x_sepa
        y = -self.height/2 + y_sepa

        source_nodes = {}
        for link in in_links:
            source_key = link.node0_key
            reroute = source_nodes.get(source_key)
            if reroute is None:
                reroute = link.insert_reroute(self)
                reroute.bnode.location = (x + 200, y)
                # Order bottom down
                if True:
                    y -= y_sepa
                else:
                    y += y_sepa

                source_nodes[source_key] = reroute

            else:
                link.replace_from(reroute, index0=0)

        # ----- Create the output reroutes

        x = 2*x_sepa
        y = 0

        source_nodes = {}
        for link in out_links:
            source_key = link.node0_key
            reroute = source_nodes.get(source_key)
            if reroute is None:
                reroute = link.insert_reroute(self)
                reroute.bnode.location = (x + 100, y)
                y -= y_sepa
                source_nodes[source_key] = reroute

            else:
                link.replace_from(reroute, index0=0)

    # ====================================================================================================
    # Arrange

    def arrange(self, reroutes=True):
        """ Arrange the content of the frame

        The algorithm is the following:
        - get the peer output nodes of each node
        - the node column is the colum plus one of the left most peer output node
        - particular case: when a node without input has only one output node, it is placed
          in the same column

        Once the columns are build, the are sorted vertically

        Then, the nodes can be placed using the location property of <!Node#bnode>.
        """

        # ----------------------------------------------------------------------------------------------------
        # No child

        if len(self.children) == 0:
            return

        # ----------------------------------------------------------------------------------------------------
        # Group input in the frame

        for node in self.children:
            if self.input_node is None:
                if node.bnode.bl_idname in ['NodeGroupInput'] + ZONE_INPUTS:
                    self.input_node = node

            if self.output_node is None:
                if node.bnode.bl_idname in ZONE_OUTPUTS:
                    self.output_node = node

        # ----------------------------------------------------------------------------------------------------
        # Arrange sub frames
        # Prepare nodes for numbering

        for node in self.children:
            if node.is_frame:
                node.arrange(reroutes)

            node.col = None
            node.row = None

            node.in_peers, _  = node.split_peers(node.in_nodes)
            node.out_peers, _ = node.split_peers(node.out_nodes)

            if False and node.is_frame:
                print(">>>", self, "sub frame", node.bnode.label + "/" + node.bnode.name)
                print("- PEERS IN ", [n.bnode.label + "/" + n.bnode.name for n in node.in_peers])
                print("- PEERS OUT", [n.bnode.label + "/" + n.bnode.name for n in node.out_peers])

            if False:
                print(f"  -> OUT {node}: {node.out_peers}")
                print(f"     {node.out_nodes}")

        # ----------------------------------------------------------------------------------------------------
        # Column number computed recursively

        def place_in_col(node):

            node.col = -1 # To avoid infinite recursion
            node.follower = None
            node.below    = False

            # ----- No node after: right most node

            if len(node.out_peers) == 0 or node == self.output_node:
                node.col = 0
                return

            # ----- Get the left most following node

            left_most = None
            for follower in node.out_peers:
                if follower.col is None:
                    place_in_col(follower)

                if left_most is None or left_most.col < follower.col:
                    left_most = follower

            node.follower = left_most
            node.col      = left_most.col + 1

            # ----- Place the node below its follower

            # Not a frame or reroute
            below = not node.is_layout

            # No input sockets or specif
            if len(node.bnode.inputs) > 0:
                below = False
                #below = below and node.bnode.bl_idname.startswith('GeometryNodeInput')

            # Not the group input
            below = below and node != self.input_node

            # Feed only one output node which is not frame or reroute
            below = below and (len(node.out_nodes) == 1) and (not left_most.is_layout)

            # Not for output node
            below = below and (left_most != self.output_node)

            if below:
                node.col -= 1
                node.below = True

            # ----- Intricated frames are placed in the same column

            if node.is_frame and left_most.is_frame:
                if left_most in node.in_peers:
                    node.col -= 1
                    node.follower = left_most.follower

        # ----------------------------------------------------------------------------------------------------
        # Let's compute the column numbers

        # ----- Number of columns

        max_col = 0
        for node in self.children:
            if node.col is None:
                place_in_col(node)
            max_col = max(max_col, node.col)

        # ----- Columns : a list of list of nodes

        columns = [[] for _ in range(max_col + 1)]
        for node in self.children:
            columns[node.col].append(node)

        # ----- Input node : single left most node

        if self.input_node is not None:
            icol = self.input_node.col

            # if icol is null: input node has not output links
            if icol > 0:
                in_col = columns[icol]
                if len(in_col) == 1:
                    if self.input_node.col != max_col:
                        del columns[icol]
                        columns.append(in_col)
                else:
                    in_col.remove(self.input_node)
                    columns.append([self.input_node])

        if self.output_node is not None:
            assert(self.output_node in columns[0])

        # ----- Output node is single right most

        if self.output_node is not None:
            col = columns[0]
            if len(col) > 1:
                col.remove(self.output_node)
                columns.insert(0, [self.output_node])

        # Renum to be sure

        for icol, col in enumerate(columns):
            for node in col:
                node.col = icol

        # DEBUG
        if False:
            print(f">>> {str(self)} Columns:")
            for i, col in enumerate(columns):
                print("   ", i, [str(node) for node in col])

        # ----------------------------------------------------------------------------------------------------
        # Let's sort the columns

        for icol in range(len(columns)):
            col = columns[icol]
            if len(col) == 1:
                col[0].row = 0
                continue

            # Extract below nodes
            belows = [node for node in col if node.below]
            for node in belows:
                del col[col.index(node)]

            # Sort the nodes

            # sort by number of inputs
            if icol == 0:
                new_col = sorted(col, key=lambda nd : -len(nd.in_peers))

            # sort by row of follower
            else:
                def key_func(nd):
                    if nd.follower is None:
                        return 1000 - len(nd.in_peers)
                    else:
                        row = nd.follower.row
                        if row is None:
                            return 0
                        else:
                            return row

                new_col = sorted(col, key=key_func)

            # Replace the below nodes
            for node in belows:
                new_col.insert(new_col.index(node.follower) + 1, node)

            # Row numbers
            for i, node in enumerate(new_col):
                node.row = i

            columns[icol] = new_col

        # ----------------------------------------------------------------------------------------------------
        # We locate the children

        x = 0
        for icol, col in enumerate(columns):

            y, col_width = 0, 0

            for node in col:

                col_width = max(col_width, node.width)

                if node.below:
                    y += Y_SEPA/2
                if node.is_frame:
                    y -= Y_SEPA

                node.bnode.location = (x, y)
                y -= node.height/2 + Y_SEPA

            x -= col_width/2 + X_SEPA

        self.wait()

        # ----------------------------------------------------------------------------------------------------
        # reroutes

        if reroutes and self.bnode is not None and not self.bnode.label.startswith("$TEMP"):
            self.frame_reroutes()

# =============================================================================================================================
# A Tree

class Tree(Frame):
    def __init__(self, btree, get_true_dims=False):
        """ > Tree wrapper

        Properties
        -----------
        - btree (bpy.types.Tree)
        - get_true_dims (bool) : read the dimensions from nodes are use an estimate

        Arguments
        ---------
        - btree (bpy.types.Tree) : the tree to wrap
        - get_true_dims (bool) : read the dimensions from nodes are use an estimate
        """
        super().__init__(self, None)
        if isinstance(btree, str):
            btree = bpy.data.node_groups[btree]
        self.btree = btree
        self.get_true_dims = get_true_dims

        # ----- Nodes

        self.nodes = {}
        for bnode in self.btree.nodes:
            if bnode.bl_idname == 'NodeFrame':
                new_node = Frame(self, bnode)
            else:
                new_node = Node(self, bnode)
                if bnode.bl_idname == 'NodeGroupOutput' and bnode.parent is None:
                    self.output_node = new_node

                if bnode.bl_idname == 'NodeGroupInput' and bnode.parent is None:
                    self.input_node = new_node

            self.nodes[bnode.name] = new_node

        # ----- Links

        self.links = [Link(self, blink) for blink in self.btree.links]

    def __str__(self):
        return f"<Tree '{self.btree.name}', {len(self.nodes)} nodes, {len(self.links)} links, {len(self.children)} children>"

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.nodes[index]

        elif isinstance(index, bpy.types.NodeInternal):
            return self.nodes[index.name]

        raise AttributeError(f"Node index not valid: {index}")

    @property
    def parent(self):
        return None

    # ====================================================================================================
    # Nodes management

    def new_node(self, bl_idname, frame=None):
        bnode = self.btree.nodes.new(bl_idname)
        if bl_idname == 'NodeFrame':
            node = Frame(self, bnode)
        else:
            node = Node(self, bnode)
        self.nodes[bnode.name] = node

        if frame is not None:
            bnode.parent = frame.bnode

        return node

    def new_frame(self, frame=None):
        return self.new_node('NodeFrame', frame=frame)

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

    def del_link(self, link):
        self.btree.links.remove(link.blink)
        self.links.remove(link)

    def new_link(self, node0, index0, node1, index1):
        blink = self.btree.links.new(node0.bnode.outputs[index0], node1.bnode.inputs[index1])
        link = Link(self, blink)
        self.links.append(link)
        return link

    # ====================================================================================================
    # Delete the reroute nodes

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

    # =============================================================================================================================
    # Group input management

    # -----------------------------------------------------------------------------------------------------------------------------
    # Group input nodes

    @property
    def group_inputs(self):
        """ > List of Group Input nodes

        Returns
        -------
        - list of nodes : nodes with bl_idname equal to 'NodeGroupInput'
        """
        return [node for node in self.nodes.values() if node.bnode.bl_idname == 'NodeGroupInput']

    # -----------------------------------------------------------------------------------------------------------------------------
    # Keep one single gorup output

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

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create one group input per frame

    def group_input_per_frame(self):
        """ Create one group input node per frame linked to the group input
        """

        # ----- One single group input

        self.single_group_input()
        inputs = self.group_inputs
        if len(inputs) == 0:
            return

        assert(len(inputs) == 1)
        group_input = inputs[0]

        # ----------------------------------------------------------------------------------------------------
        # Loop on the output links

        frames = {}
        for link in self.links:
            if link.node0 != group_input:
                continue

            bframe = link.node1.bnode.parent
            if bframe is None:
                continue

            frame = self[bframe]
            frame_input = frames.get(bframe.name)
            if frame_input is None:
                frame_input = self.new_node('NodeGroupInput', frame)
                frames[bframe.name] = frame_input

            link.replace_from(frame_input)

        # ----- Remain if not output

        keep = False
        for link in self.btree.links:
            if link.from_node == group_input.bnode:
                keep = True
                break
        if not keep:
            self.del_node(group_input)

    # =============================================================================================================================
    # Zones in frames

    def zones_in_frame(self):
        """ Create a temporary frame around zones
        """

        # ----------------------------------------------------------------------------------------------------
        # Get the existing zones

        zones = []

        for node in self.nodes.values():
            if node.bnode.bl_idname not in ZONE_INPUTS:
                continue

            if node.bnode.paired_output is None:
                continue

            zone_input  = node
            zone_output = self[node.bnode.paired_output]

            if False:
                zone = [zone_input, zone_output] + [node for node in self.nodes.values() if node.in_zone(zone_input, zone_output)]
            else:
                zone = [zone_input, zone_output]
                for node in self.nodes.values():
                    ok = node.in_zone(zone_input, zone_output)
                    if ok:
                        zone.append(node)


            zones.append(zone)

        if len(zones) == 0:
            return

        # ----------------------------------------------------------------------------------------------------
        # Zones imbrication

        imbrication = [None] * len(zones)
        if len(zones) > 1:
            for izone, zone in enumerate(zones):
                for iz, z in enumerate(zones):
                    if iz == izone:
                        continue

                    # Zone imbricated in z
                    if zone[0].in_zone(z[0], z[1]):
                        icur = imbrication[izone]
                        if icur is None:
                            imbrication[izone] = iz
                        else:
                            cur = zones[icur]
                            if z[0].in_zone(cur[0], cur[1]):
                                imbrication[izone] = iz

        # ----------------------------------------------------------------------------------------------------
        # Create the temporary frames
        #
        # Start by the most imbricated zone

        n = len(zones)
        frames = [None]*n
        for _ in range(n):
            for izone, zone in enumerate(zones):

                if zone is None:
                    continue

                # ----- Has the zone imbricated zones

                KO = False
                for z in zones:
                    if z is None or z == zone:
                        continue
                    if z[0].in_zone(zone[0], zone[1]):
                        # z is imbricated in zone, it must be treated before
                        KO = True
                        break

                if KO:
                    continue

                # ----- Creates a frame only if not already in a frame

                if zone[0].parent == self and zone[1].parent == self:
                    frame = self.new_frame()
                    frame.bnode.label = "$TEMP_ZONE"
                    frames[izone] = frame
                    for node in zone:
                        if node.bnode.parent is None:
                            node.bnode.parent = frame.bnode

                zones[izone] = None
                break

        # ---- Parent of created frames

        for i, frame in enumerate(frames):
            if frame is None:
                continue
            iparent = imbrication[i]
            if iparent is not None:
                frame.bnode.parent = frames[iparent].bnode

        self.wait()

    # =============================================================================================================================
    # Delete temporary frames

    def del_temp_frames(self):
        """ Delete temporary frames

        Temporary frames have a label starting by '$TEMP'
        """
        to_delete = [frame for frame in self.nodes.values() if frame.bnode.label.startswith("$TEMP")]
        for frame in to_delete:

            bframe = frame.bnode
            for bnode in self.btree.nodes:
                if bnode.parent == bframe:
                    bnode.parent = bframe.parent

            self.tree.del_node(frame)

# ====================================================================================================
# Arrange a tree

def arrange(btree, reroutes=True, input_in_frames=True, get_true_dims=False):

    # Try to update node dimensions !
    Node.wait()

    tree = Tree(btree, get_true_dims=get_true_dims)

    if reroutes:
        tree.del_reroutes()

    if input_in_frames:
        tree.group_input_per_frame()

    if False: # COULD BE VERY SLOW
        tree.zones_in_frame()
    tree.arrange(reroutes=reroutes)
    tree.del_temp_frames()

# ====================================================================================================
# UI

# bl_region_type in
# ('WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF',
# 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR')

class RemoveReroutesOperator(bpy.types.Operator):
    """Remove the 'reroute' nodes"""
    bl_idname = "node.remove_reroutes"
    bl_label  = "Remove Reroutes"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR' and space.edit_tree is not None
        #return space.type == 'NODE_EDITOR' and space.node_tree is not None

    def execute(self, context):
        space = context.space_data
        tree = Tree(space.edit_tree)
        tree.del_reroutes()
        arrange(space.edit_tree, reroutes=False)
        return {'FINISHED'}

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
        arrange(space.edit_tree, get_true_dims=True)
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
    bl_label       = "Nodes tree arrange"
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

        # Arrange
        row = layout.row()
        row.scale_y = 2.0
        row.operator("node.arrange_nodes")

        # Remove reroutes
        row = layout.row()
        row.operator("node.remove_reroutes")

def register():
    try:
        bpy.utils.register_class(RemoveReroutesOperator)
        bpy.utils.register_class(ArrangeNodesOperator)
        bpy.utils.register_class(NodeDumpOperator)

        bpy.utils.register_class(LayoutArrangePanel)
    except:
        pass

def unregister():
    try:
        bpy.utils.unregister_class(RemoveReroutesOperator)
        bpy.utils.unregister_class(ArrangeNodesOperator)
        bpy.utils.unregister_class(NodeDumpOperator)

        bpy.utils.unregister_class(LayoutArrangePanel)
    except:
        pass
