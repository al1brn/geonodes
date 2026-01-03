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
from .nodezone import ZoneNode
from .socket_class import Socket
from .signature import Signature
from . import generated

# ====================================================================================================
# Closure class
# ====================================================================================================

class Closure(generated.Closure):
    """ Closure Socket.

    A Closure is defined as a Tree within a `with` context:

    ``` python
    with Closure() as c:
        # Create a closure input socket
        pi = Float(3.14, "Pi")
        # Create a closure output socket
        pi.out("Pi")
    ````

    The Closure can be then evaluated using `evaluate` method. This method requires a Signature. The
    Signature can be read from an existing Closure or created manually as a couple of dicts.


    ``` python
    with GeoNodes("Closure Test") as tree:
        
        Geometry().out()
        
        with Layout("First closure"):
        
            with Closure() as cl:
                g = Mesh()
                g.points.store(String("Pi Attr", name="Attr Name"), Float(3.14, "Float Attribute"))
                
                (Integer(2, "Two") + Integer(2, "Two")).out("Four")
                
                cloud = g.faces.distribute_points()
                cloud.node.link_inputs(None, "Cloud")
                cloud.node.link_outputs(None, "Cloud")

                g.out()
                cloud.out("Points")
                
        with Layout("Direct evaluation"):
            cl.evaluate().out(panel="First closure")
            
        cl.out("First Closure")
            
        # Get the first signature
        sig1 = cl.get_signature()
            
        with Layout("Second Closure"):
            cl = Closure()
            
            with cl:
                spiral = Curve.Spiral(resolution=Integer(name="Resolution"))
                spiral.out("Spiral")
                
            with cl:
                spiral.to_mesh(profile_curve=Curve(name="Profile")).out("Mesh")
                
        cl.out("Second Closure")
        
        # Get the second signature
        sig2 = cl.get_signature()
        
        with Layout("Evaluate with signatures"):
            
            cl1 = Closure(name="Closure 1")
            cl2 = Closure(name="Closure 2")
            
            # Using evaluate method
            cl1.evaluate(signature=sig1).node.out(panel="Closure 1 out")

            # Using calling methjod
            cl2(signature=sig2).node.out(panel="Closure 2 out")

        # Manual signature
        with Closure() as cl3:
            pi = Float(3.14, "Pi")
            fac = Integer(2, "Multiplicator")
            (fac*pi).out("Tau")

        cl3.evaluate(signature=({'Pi': Float, 'Multiplicator': Integer}, {'Tau': Float})).out("Manual Signature")
    ```
    """

    SOCKET_TYPE = 'CLOSURE'

    # ====================================================================================================
    # Zone
    # ====================================================================================================

    @property
    def _has_zone(self):
        return self.node._bnode.bl_idname == 'NodeClosureOutput'
    
    # ====================================================================================================
    # Context management
    # ====================================================================================================

    def _push(self):

        from .treeclass import Layout

        if self._has_zone:
            # I/O
            self._tree._output_stack.append(self.node)
            self._tree._input_stack.append(self.node._paired_input_node)

            # Layout
            layout = Layout("Closure", node=self.node)
            layout.include_node(self.node._paired_input_node)
            layout.push()

        else:
            super()._push()

    def _pop(self, error: bool = False):

        if self._has_zone:
            # Layout
            self._tree._layouts.pop()

            # I/O
            self._tree._output_stack.pop()
            self._tree._input_stack.pop()

        else:
            super()._pop(error=error)


    # ====================================================================================================
    # Signature
    # ====================================================================================================

    def get_signature(self, with_sockets: bool = False):
        """ Build the closure signature of the zone.

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
        if self._has_zone:
            return Signature(
                self.node._paired_input_node.get_signature(with_sockets=with_sockets).outputs,
                self.node.get_signature(with_sockets=with_sockets).inputs)
        else:
            raise RuntimeError(f"The Closure socket {self} doesn't come from a Closure pair of nodes. Impossible to get its signature.")

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

        already_linked = False
        # Closure has a zone: let's get it
        if self._has_zone:
            signature = self.get_signature()

        # Signature is not provided: we use the sockets (hoping they cover the needs)
        elif signature is None:
            already_linked = True
            signature = Signature.from_named_sockets(named_sockets, **sockets)

        else:
            signature = Signature(signature)

        # ----------------------------------------------------------------------------------------------------
        # Create the node
        # ----------------------------------------------------------------------------------------------------

        # Closure evaluation node
        node = Node('NodeEvaluateClosure', {"Closure": self})

        # Set the signature
        node.set_signature('INPUT', Signature(signature.inputs))
        node.set_signature('OUTPUT', Signature(signature.outputs))

        # Link the input
        if not already_linked:
            for name, value in {**named_sockets, **sockets}.items():
                node.set_input_socket(name, value)

        # We are done :-)
        return node._out
    
    # ----------------------------------------------------------------------------------------------------
    # Function call syntax
    # ----------------------------------------------------------------------------------------------------
    
    def __call__(self, named_sockets: dict = {}, signature: Signature = None, **sockets):
        return self.evaluate(named_sockets=named_sockets, signature=signature, **sockets)

    
    # ===============================================s=====================================================
    # Test
    # =====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Geometry, Mesh, Float, Integer, Layout, Closure, Curve, String

        with GeoNodes("Closure Test") as tree:
            
            Geometry().out()
            
            with Layout("First closure"):
            
                with Closure() as cl:
                    g = Mesh()
                    g.points.store(String("Pi Attr", name="Attr Name"), Float(3.14, "Float Attribute"))
                    
                    (Integer(2, "Two") + Integer(2, "Two")).out("Four")
                    
                    cloud = g.faces.distribute_points()
                    cloud.node.link_inputs(None, "Cloud")
                    cloud.node.link_outputs(None, "Cloud")

                    g.out()
                    cloud.out("Points")
                    
            with Layout("Direct evaluation"):
                cl.evaluate().out(panel="First closure")
                
            cl.out("First Closure")
                
            # Get the first signature
            sig1 = cl.get_signature()
                
            with Layout("Second Closure"):
                cl = Closure()
                
                with cl:
                    spiral = Curve.Spiral(resolution=Integer(name="Resolution"))
                    spiral.out("Spiral")
                    
                with cl:
                    spiral.to_mesh(profile_curve=Curve(name="Profile")).out("Mesh")
                    
            cl.out("Second Closure")
            
            # Get the second signature
            sig2 = cl.get_signature()
            
            with Layout("Evaluate with signatures"):
                
                cl1 = Closure(name="Closure 1")
                cl2 = Closure(name="Closure 2")
                
                # Using evaluate method
                cl1.evaluate(signature=sig1).node.out(panel="Closure 1 out")

                # Using calling methjod
                cl2(signature=sig2).node.out(panel="Closure 2 out")

            # Manual signature
            with Closure() as cl3:
                pi = Float(3.14, "Pi")
                fac = Integer(2, "Multiplicator")
                (fac*pi).out("Tau")

            cl3.evaluate(signature=({'Pi': Float, 'Multiplicator': Integer}, {'Tau': Float})).out("Manual Signature")
                
              
            
    