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

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : nodezone
-------------------
- Paired nodes forming a zone

updates
-------
- creation : 2025/12/08
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

import bpy

from . import constants
from . import utils
from .sockettype import SocketType
from .treeclass import Tree
from .treeinterface import ItemPath, TreeInterface
from .nodeclass import Node
from typing import TYPE_CHECKING, Literal, Any



SIMULATION = "Simulation"
REPEAT     = "Repeat"
FOR_EACH   = "For Each Element"
CLOSURE    = "Closure"

ZONE_ID = Literal[SIMULATION, REPEAT, FOR_EACH, CLOSURE]

class Socket: ...

# ====================================================================================================
# Zone output node
# ====================================================================================================

class ZoneNode(Node):

    __slots__ = Node.__slots__ + ('_zone_id',)

    NODES = {
        SIMULATION : 'Simulation',
        REPEAT     : 'Repeat',
        FOR_EACH   : 'For Each Geometry Element',
        CLOSURE    : 'Closure', 
    }

    def __init__(self,
            zone_id         : Literal["Simulation", "Repeat", "For Each Element", "Closure"],
            socket          : Socket | SocketType,
            named_sockets   : dict = {}, 
            **sockets):
        """ Paired nodes forming a zone.

        This class overload the creation of a zone output node such as 'Simulation Output' or 'Repeat Output'.
        When the node is created, the input node is also created and paired.

        If the socket argument is a SocketType, an empty socket of this type is created.

        The two nodes can have dynamic sockets as described below
        
        Zone          Input Node          Output Node
        ----------    ------------        ------------
        Repeat          dyn_out                x
        Simulation      dyn_out                x
        For Each        dyn_out              dyn_in (two panels)
        Closure         dyn_out              dyn_in

        Arguments
        ---------
        - zone_id (str in ()"Simulation", "Repeat", "For Each Element", "Closure")) : zone id
        - socket (Socket | SocketType) : the socket for zone input
        - named_sockets (dict = {}) : initialization values for the node input sockets
        - domain (str: None) : domain for For Each zone
        - **parameters : node parameters and sockets
        """

        if zone_id not in ZoneNode.NODES:
            raise AttributeError(f"The zone id '{zone_id}' is not valid, valids are: {tuple(ZoneNode.NODES.keys())}.")
        
        self._zone_id = zone_id
        node_name = ZoneNode.NODES[zone_id]

        # ---------------------------------------------------------------------------
        # Create the output node
        # ---------------------------------------------------------------------------

        # Extract domain parameter for For Each zone
        if zone_id == FOR_EACH:
            if 'domain' in sockets:
                domain = sockets['domain']
                sockets = {k:v for k, v in sockets.items() if k != 'domain'}
            else:
                domain = 'POINT'
            
            super().__init__(node_name + ' Output', domain=domain)

        else:
            super().__init__(node_name + ' Output')

        # ---------------------------------------------------------------------------
        # Create the input node and pair them
        # ---------------------------------------------------------------------------

        inode = Node(node_name + ' Input')
        inode._bnode.pair_with_output(self._bnode)

        # ---------------------------------------------------------------------------
        # Setup the nodes
        # ---------------------------------------------------------------------------

        inode._is_paired_input = True
        inode._paired_output_node = self

        self._is_paired_output = True
        self._paired_input_node = inode

        class_name = type(socket).__name__

        # ---------------------------------------------------------------------------
        # Simulation
        # ---------------------------------------------------------------------------

        if zone_id == SIMULATION:
            inode._has_items  = True
            inode._has_dyn_in = True
            inode._items['INPUT']  = self._bnode.state_items
            inode._items['OUTPUT'] = self._bnode.state_items

            self._bnode.state_items.clear()
            inode.set_input_socket(class_name, socket)

        # ---------------------------------------------------------------------------
        # Repeat
        # ---------------------------------------------------------------------------

        elif zone_id == REPEAT:
            inode._has_items  = True
            inode._has_dyn_in = True
            inode._items['INPUT']  = self._bnode.repeat_items
            inode._items['OUTPUT'] = self._bnode.repeat_items

            self._bnode.repeat_items.clear()
            inode.set_input_socket(class_name, socket)

        # ---------------------------------------------------------------------------
        # For each element
        # ---------------------------------------------------------------------------

        elif zone_id == FOR_EACH:

            # generation_items, input_items, main_items

            # Input
            inode._has_items  = True
            inode._has_dyn_in = True
            inode._items['INPUT']  = self._bnode.input_items
            inode._items['OUTPUT'] = self._bnode.input_items

            inode.set_input_socket('Geometry', socket)

        # ---------------------------------------------------------------------------
        # Closure
        # ---------------------------------------------------------------------------
        
        elif zone_id == CLOSURE:

            # Input
            inode._has_items   = True
            inode._has_dyn_out = True
            inode._items['OUTPUT'] = self._bnode.input_items

            # Output
            self._has_items  = True
            self._has_dyn_in = True
            self._items['INPUT'] = self._bnode.output_items

        # ---------------------------------------------------------------------------
        # Set the arguments to input node
        # ---------------------------------------------------------------------------

        for name, value in {**named_sockets, **sockets}.items():
            inode.set_input_socket(name, value)

    # ====================================================================================================
    # Loop zone
    # ====================================================================================================

    def _loop_start(self):
        """ Start loop.

        Set up for code within the zone:
        - zone input node becomes the default input node
        - zone output node becomes the default output node
        """

        inode = self._paired_input_node

        # ---------------------------------------------------------------------------
        # Simulation
        # ---------------------------------------------------------------------------

        if self._zone_id == SIMULATION:
            inode._has_dyn_in  = False
            inode._has_dyn_out = True

            self._tree._input_stack.append(inode)
            self._tree._output_stack.append(self)

        # ---------------------------------------------------------------------------
        # Repeat
        # ---------------------------------------------------------------------------

        elif self._zone_id == REPEAT:
            inode._has_dyn_in  = False
            inode._has_dyn_out = True

            self._tree._input_stack.append(inode)
            self._tree._output_stack.append(self)

        # ---------------------------------------------------------------------------
        # For each element
        # ---------------------------------------------------------------------------

        elif self._zone_id == FOR_EACH:

            # generation_items, input_items, main_items

            # Input node
            inode._has_dyn_in  = False
            inode._has_dyn_out = True

            # Output node
            self._has_items   = True
            self._has_dyn_in = True
            
            # Two panels for items:
            # - main_items
            # -generation_items
            # Will be selected by code

            # Two panels
            #self._items['OUTPUT'] = {
            #    "Main":      self._bnode.main_items,
            #    "Generated": self._bnode.generation_items,
            #}

            self._tree._input_stack.append(inode)
            self._tree._output_stack.append(self)

        else:
            assert False, f"Shouldn't happen '{self._zone_id}'"


    def _loop_end(self):

        inode = self._paired_input_node

        # ---------------------------------------------------------------------------
        # Simulation
        # ---------------------------------------------------------------------------

        if self._zone_id == SIMULATION:

            self._tree._input_stack.pop()
            self._tree._output_stack.pop()

            inode._has_dyn_in = True
            inode._has_dyn_out = False

        # ---------------------------------------------------------------------------
        # Repeat
        # ---------------------------------------------------------------------------

        elif self._zone_id == REPEAT:

            self._tree._input_stack.pop()
            self._tree._output_stack.pop()

            inode._has_dyn_in = True
            inode._has_dyn_out = False

        # ---------------------------------------------------------------------------
        # For each element
        # ---------------------------------------------------------------------------

        elif self._zone_id == FOR_EACH:

            # generation_items, input_items, main_items

            self._tree._input_stack.pop()
            self._tree._output_stack.pop()

            # Input node
            inode._has_dyn_in  = True
            inode._has_dyn_out = False

            # Output node
            self._has_dyn_in = False

        else:
            assert False, f"Shouldn't happen '{self._zone_id}'"

# ====================================================================================================
# Zone Iterator
# ====================================================================================================

class ZoneIterator:

    __slots__ = ('_socket', '_input_node', '_output_node', '_name', '_done', '_in_zone')

    def __init__(self, socket: Socket, node: ZoneNode):
        """ Wrap the nodes creation within a zone.

        The ZoneIterator wraps a pair of nodes forming a zone : Simulation, Repeat, For Each, Closure.

        The iteration contains exactly one iteration in order to generate the nodes only once.

        The first call to __next__ method pushes the input and output nodes in order to capture inputs and outputs.
        The second call pops the i/o capture and raises StopIteration.

        The iterator returns itself as it exposes the nodes sockets:
        - During the iteration, the input sockets are the ones of the output node and the output sockets are
          the ones of the input node.
        - Outside the iteration, the input sockets are the ones of the input node and the output sockets are
          the ones of the output node.

        ``` python
        geo = Geometry()
        for sim in geo.simulation(A=1.0):
            
            # Output sockets come from input node
            a = sim.a

            # Sockets creation is captured
            # A new simulation socket named B is created
            b = Float(2.0, name="B")

            # Input sockets come from output node
            sim.a = a + b

            # Output is captured
            sim.b = a - b
            
            # No socket C was created
            try:
                sim.c = 0
            except AttributeError:
                print("An error is raised when accessing a non existing socket")

            # Within the loop, geo socket comes from input node
            # 
            geo.position += a

            # Default output geometry is in output node
            geo.out()

        # Outside the loop, geometry is now the output node output geometry
        # The zone output sockets can be accessed from simulation
        geo.position += sim.a

        geo.out()
        ```

        Arguments
        ---------
        - socket (Socket) : the socket to loop on
        - node (Node) : a valid zone output node
        """

        if not isinstance(node, ZoneNode) or node._zone_id == CLOSURE:
            raise RuntimeError(f"The iteration is possible only for nodes Simulation, Repeat or For Each, not {node}.")
        
        self._name = node._zone_id

        self._socket        = socket
        self._output_node   = node
        self._input_node    = node._paired_input_node
        self._done          = False
        self._in_zone       = False

        print("ZONE ITER", self._socket)

    def __str__(self):
        return f"<ZoneIterator {self._name}, in_zone: {self._in_zone}, done: {self._done}>"

    # ====================================================================================================
    # Iteration
    # ====================================================================================================

    def __iter__(self):

        self._done = False
        self._output_node._loop_start()

        if self._socket is not None:

            if self._name == SIMULATION:
                self._socket._jump(self._input_node._bnode.outputs[1])

            elif self._name == REPEAT:
                print("ZONE ITER jumping BEF", self._socket)
                self._socket._jump(self._input_node._bnode.outputs[1])
                print("ZONE ITER jumping AFT", self._socket)

            elif self._name == FOR_EACH:
                self._socket._jump(self._input_node._bnode.outputs[1])

            else:
                assert False

        return self

    def __next__(self):
        if self._done:
            self._output_node._loop_end()
            self._socket._jump(self._output_node._out)
            self._in_zone = False

            raise StopIteration
        
        else:
            self._done = True
            self._in_zone = True
            return self
        
    # ====================================================================================================
    # Attributes
    # ====================================================================================================

    @property
    def generated(self):
        if self._name == FOR_EACH:
            return self._output_node.socket_by_identifier('OUTPUT', "Generation_0")
        else:
            raise f"Attribute error: {self._name} zone doesn't have an output socket named 'Generated'."

    @property
    def Generated(self):
        return self.generated

    def __setattr__(self, name, value):
        if name in ZoneIterator.__slots__:
            super().__setattr__(name, value)
            return
        
        if self._in_zone:
            setattr(self._output_node, name, value)
        else:
            setattr(self._input_node, name, value)

    def __getattr__(self, name):
        if self._in_zone:
            return getattr(self._input_node, name)
        else:
            return getattr(self._output_node, name)

