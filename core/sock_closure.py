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

module : sock_closure
---------------------
- Closure socket


updates
-------
- creation : 2025/11/15
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"


import numpy as np

from .scripterror import NodeError

from . import utils
from .nodeclass import Node
from .socket_class import Socket
from .signature import Signature
from . import generated

# ====================================================================================================
# Closure class
# ====================================================================================================

class Closure(generated.Closure):

    SOCKET_TYPE = 'CLOSURE'

    def __init__(self, 
        value: Socket = None,
        name: str = None,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        ):
        """ Socket of type Closure

        Arguments
        ---------
        - value  (Socket = None) : Default value
        - name  (str = None) : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:

            # ---------------------------------------------------------------------------
            # No name : let's create a Closure Zone
            # ---------------------------------------------------------------------------

            if name is None:

                input_node  = Node('NodeClosureInput')
                output_node = Node('NodeClosureOutput')
                input_node._bnode.pair_with_output(output_node._bnode)
                output_node._bnode.output_items.clear()

                bsock = output_node._bnode.outputs["Closure"]

            # ---------------------------------------------------------------------------
            # We have a name: let's create it from the group input
            # ---------------------------------------------------------------------------

            else:
                bsock = self._create_input_socket(value=value, name=name, tip=tip,
                    panel=panel, optional_label=optional_label, hide_value=hide_value,
                    hide_in_modifier=hide_in_modifier)
                
        super().__init__(bsock)

        # No layout when capturing in out
        self._use_layout = False


    # ====================================================================================================
    # Zone
    # ====================================================================================================

    @property
    def _has_zone(self):
        return self.node._bnode.bl_idname == 'NodeClosureOutput'
    
    @property
    def _output_node(self):
        if self._has_zone:
            return self.node
        else:
            return None
    
    @property
    def _input_node(self):
        if not self._has_zone:
            return None
        
        out_bnode = self.node._bnode
        
        for node in self._tree._nodes:
            if node._bnode.bl_idname != 'NodeClosureInput':
                continue

            if node._bnode.paired_output == out_bnode:
                return node
            
        assert False, "Shouldn't happen {self}"

    # ====================================================================================================
    # InOutContext implementation
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Create an input socket
    # ----------------------------------------------------------------------------------------------------

    def create_input_socket(self, bl_idname, name, value=None, panel="", **props):
        """ Create a new input socket.

        Arguments
        ---------
            - bl_idname (str) : socket bl_idname
            - name (str): Socket name
            - value (Any = None) : Default value
            - panel (str = "") : Panel to place the socket in
            - props : properties specific to interface socket

        Returns
        -------
            Socket
        """
        # No zone: behaves as a standard Socket
        if not self._has_zone:
            return super().create_input_socket(bl_idname, name, value=value, panel=panel, **props)

        # Panel
        name = " ".join([s.strip() for s in panel.split(">")] + [name])

        # Create new item
        items = self._output_node._bnode.input_items
        items.new(utils.bl_idname_to_socket_type(bl_idname), name)

        socket = self._input_node[len(items) - 1]
        if hasattr(socket._bsocket, 'default_value') and value is not None:
            socket._bsocket.default_value = value

        return socket

    # ----------------------------------------------------------------------------------------------------
    # Create a new input socket from an existing node input socket
    # ----------------------------------------------------------------------------------------------------

    def create_input_from_socket(self, input_socket, name=None, panel="", **props):
        """ Create a new group input socket from an existing input socket.

        Arguments
        ---------
        - input_socket (socket) : a node input _insocket
        - name (str = None) : name of the group input socket to create
        - panel (str = "") : name of the panel
        - props (dict) : socket properties

        Returns
        -------
        - Socket
        """

        # No zone: behaves as a standard Socket
        if not self._has_zone:
            return super().create_input_from_socket(input_socket, name=name, panel=panel, **props)

        # Ensure name
        if name is None:
            name = utils.get_socket_name(input_socket)

        # Panel
        if panel is None:
            panel = ""
        name = " ".join([s.strip() for s in panel.split(">")] + [name])

        # Create new item and link it
        items = self._output_node._bnode.input_items
        item_type = utils.get_bsocket(input_socket).type
        if item_type == 'VALUE':
            item_type = 'FLOAT'
        items.new(item_type, name)
        socket = self._input_node._bnode.outputs[len(items)-1]
        self._tree.link(socket, input_socket)

        # Return the created socket
        return self._input_node[name]
    
    # ----------------------------------------------------------------------------------------------------
    # Get the signature
    # ----------------------------------------------------------------------------------------------------

    def get_signature(self, include: list = None, exclude: list = [], enabled_only=True, with_sockets: bool = False):
        """ Build the closure signature of the node.

        Closure signature is the tuple (input_signature, output_signature)

        Arguments
        ---------
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - enabled_only (bool = True) : ignore disabled sockets
        - with_sockets (bool = False) : include sockets

        Returns
        -------
        - Signature
        """
        if not self._has_zone:
            return super().get_signature(include=include, exclude=exclude, enabled_only=enabled_only, with_sockets = with_sockets)
        
        in_sig = self._input_node.get_signature(
            include      = include, 
            exclude      = exclude, 
            enabled_only = enabled_only, 
            with_sockets = with_sockets).outputs
        
        out_sig = self._output_node.get_signature(
            enabled_only = enabled_only, 
            with_sockets = with_sockets).inputs
        
        return Signature(in_sig, out_sig)

    # ===============================================s=====================================================
    # Evaluate
    # ====================================================================================================

    def evaluate(self, named_sockets: dict = {}, signature: Signature = None, **sockets):
        """ > Node <&Node Closure Evaluate>

        Evaluate the closure.

        The closure signature can be read directly when the closure sockets comes from a Closure
        zone. Otherwise, the signature argument must be defined.

        ``` python
        with GeoNodes("Closure Evaluation"):
            
            # ----- Evaluation from a Closure zone
            
            with Closure() as cl:
                cube = Mesh.Cube(size=cl.new_input(), vertices_x=cl.new_input("Resolution"))
                cube.node.vertices_y = cl.input_node.resolution
                cube.node.vertices_z = cl.input_node.resolution
                cube.out("Cube")
                
            # Direct evalution: no signature required
            cl.evaluate(size=(1, 2, 3), resolution=5).out("First Closure")
            
            # ----- Evaluation with a closure signature
            
            # A closure is passed as Tree input argument
            closure = Closure(None, name="Other Closure")
            
            # The closure can be switched for instance
            closure = cl.switch(Boolean(False, "Use other"), closure)
            
            # Evaluation is made using the reference signature
            closure.evaluate(signature=cl.get_signature(), size=(10, 20, 30), resolution=10).out("Second Closure")
            
            # ----- Evaluation with any signature
            
            # A closure is passed as Tree input argument
            closure = Closure(None, name="IcoSphere Closure")
            
            # The signature is supposed to be the one of an ico sphere creation
            ico = Mesh.IcoSphere()
            
            # Evaluation with this node signature
            closure.evaluate(closure_signature=ico.node.get_signature(), radius=3.14).out("Third Closure")
        ```

        Arguments
        ---------
        - named_sockets (dict = {}) : named sockets values
        - signature (Signature = None) : the evaluation signature
        - sockets : socket values

        Returns
        -------
        - First output socket of evaluation node
        """

        _btree = self._tree._btree

        # ----------------------------------------------------------------------------------------------------
        # Let's ensure a proper signature
        # ----------------------------------------------------------------------------------------------------

        # Closure has a zone: let's get it
        if self._has_zone:
            signature = self.get_signature()

        # Signature is not provided: we can infer the output sockets :-(
        elif signature is None:
            raise NodeError(f"Closure evaluation error: 'Closure.evaluate' must be called from a Closure zone or using 'signature' argument.")

        # ----------------------------------------------------------------------------------------------------
        # Create the node and plug self
        # ----------------------------------------------------------------------------------------------------

        # Closure evaluation node
        node = Node('NodeEvaluateClosure')

        # Link closure input
        link = _btree.links.new(self._bsocket, node._bnode.inputs["Closure"], handle_dynamic_sockets=True)
        utils.check_link(link)

        # ----------------------------------------------------------------------------------------------------
        # Create sockets from signature
        # ----------------------------------------------------------------------------------------------------

        bnode = node._bnode
        Signature(signature.inputs).create_items( bnode.input_items,  use_rank=True, use_panel=True)
        Signature(signature.outputs).create_items(bnode.output_items, use_rank=True, use_panel=True)

        # ----------------------------------------------------------------------------------------------------
        # Plug the arguments to the newly created sockets
        # ----------------------------------------------------------------------------------------------------

        for name, value in named_sockets.items():
            node.plug_value_into_socket(value, node.socket_by_name('INPUT', name, as_argument=False))

        for name, value in sockets.items():
            node.plug_value_into_socket(value, node.socket_by_name('INPUT', name, as_argument=True))

        # We are done :-)
        return node._out
    
    # ===============================================s=====================================================
    # Test
    # =====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Geometry, Mesh, Float, Integer, Layout, Closure, Curve

        with GeoNodes("Closure Test") as tree:
            
            with Layout("First clossure"):
            
                with Closure() as cl:
                    g = Mesh()
                    g.points.store("Float", Float(3.14, "Float Attribute"))
                    
                    (Integer(2, "Two") + Integer(2, "Two")).out("Four")
                    
                    cloud = g.faces.distribute_points()
                    cl.create_from_node(cloud.node, 'BOTH')

                    g.out()
                    cloud.out("Points")
                    
            cl.evaluate().out(panel="First closure")
                
            with Layout("Second Closure"):
                cl = Closure()
                spiral = Curve.Spiral()
                cl.create_from_node(spiral.to_mesh().node, 'BOTH', exclude_linked=True)
                cl.create_from_node(spiral.node, 'INPUT', exclude_linked=True, panel="Spiral")
                
                cl.evaluate().out(panel="Second Closure")
                
                sig = cl.get_signature()
                
            # ------ Get another closure from sockets
            
            with Layout("Evaluate the Closure with the second signature"):
                sock_cl = Closure(name="Other Closure")
                sock_cl.evaluate(signature=sig).out(panel="Other Closure")
                
            
    