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

module : inoutcontext
---------------------
- InOutContext: base class for node creation


updates
-------
- creation : 2025/11/18
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

from abc import ABC, abstractmethod
from typing import Literal

from .scripterror import NodeError
from . import utils
from .signature import Signature

# ====================================================================================================
# InOutContext
# ====================================================================================================

class InOutContext(ABC):

    # ====================================================================================================
    # Abstract methods :
    # - input creation
    # - output creation
    # - output creation
    # - getting the signature
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Create an input socket
    # ----------------------------------------------------------------------------------------------------

    #@abstractmethod
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
        return None
    
    # ----------------------------------------------------------------------------------------------------
    # Create a new input socket from an existing node input socket
    # ----------------------------------------------------------------------------------------------------

    #@abstractmethod
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
        return None
    
    # ----------------------------------------------------------------------------------------------------
    # Create a new output socket
    # ----------------------------------------------------------------------------------------------------

    #@abstractmethod
    def create_output_socket(self, socket, name=None, panel="", **props):
        """ Create a new output socket.

        This is an **output socket** of the Tree, hence an input socket of the <&Group Output> node.

        Arguments
        ---------
        - socket (socket) : socket
        - name (str) : Socket name
        - panel (str = "") : Panel name
        - props (dict) : socket properties

        Returns
        -------
            Socket
        """
        pass

    # ----------------------------------------------------------------------------------------------------
    # Get the signature
    # ----------------------------------------------------------------------------------------------------

    @abstractmethod
    def get_signature(self, include: list = None, exclude: list = [], enabled_only=True, with_sockets: bool = False):
        """ Build the signature of the node.

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
        pass

    # ====================================================================================================
    # Forward creation
    # ====================================================================================================

    def new_input(self, name=None, **props):
        """ Forward input socket creation.

        Used as socket value when creating a node (see example below):

        ``` python
        with GeoNodes("Forward Socket Creation") as tree:
            # The radius 
            sphere = Mesh.IcoSphere(radius=tree.new_input())
        ```
        """

        # Forward create function
        def create(in_socket, ioc, name, props):
            if name is None:
                name = in_socket.name

            ioc.create_input_from_socket(in_socket, name=name, **props)

        # Main: A dict to create dynamically the argument socket

        return {'create': create, 'args': [self, name, props]}

    # ====================================================================================================
    # Signature
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Set input signature
    # ----------------------------------------------------------------------------------------------------

    def set_input_signature(self, signature: Signature, reuse: bool = True, panel: str = ""):
        """ Create zone input sockets from a signature.

        If `reuse` argument is False, sockets are always created, if it is True, existing sockets are reused.

        Arguments
        ---------
        - signature (Signature) : the signature to use
        - reuse (bool = True) : reuse existing sockets when possible
        - panel (str = "") : panel iwhere to create sockets

        Returns
        -------
        - List of created input sockets
        """
        sockets = []

        for name, sig in signature.sockets.items():

            #name        = sig.get(name)
            value       = sig.get('value')
            props       = sig.get('props', {})
            sock_panel  = sig.get('panel', "")
            if panel != "":
                sock_panel = panel if sock_panel == "" else panel + " " + sock_panel

            if sig.get('socket', None) is None:
                sock = self.create_input_socket(
                    utils.socket_type_to_bl_idname(sig['socket_type']),
                    name    = name, 
                    value   = value,
                    panel   = sock_panel,
                    **props)
            else:
                sock = self.create_input_from_socket(
                    sig['socket'], 
                    name    = name,
                    panel   = sock_panel,
                    **props)

            sockets.append(sock)

        return sockets
    
    # ----------------------------------------------------------------------------------------------------
    # Set output signature
    # ----------------------------------------------------------------------------------------------------

    def set_output_signature(self, signature: Signature, reuse: bool = True, panel: str = ""):
        """ Create zone output sockets from a signature.

        If `reuse` argument is False, sockets are always created, if it is True, existing sockets are reused.

        Arguments
        ---------
        - signature (Signature) : the signature to use
        - reuse (bool = True) : reuse existing sockets when possible
        - panel (str = "") : panel iwhere to create sockets

        Returns
        -------
        - List of created output sockets
        """
        sockets = []

        # Loop on the two dicts in signature
        for name, sig in signature.sockets.items():
            
            sid         = sig.get('socket', sig['socket_type'])
            #name        = sig.get(name)
            props       = sig.get('props', {})
            sock_panel  = sig.get('panel')
            if panel != "":
                sock_panel = panel if sock_panel == "" else panel + " " + sock_panel

            sock = self.create_output_socket(sid, name=name, panel=sock_panel, **props)

            sockets.append(sock)

        return sockets        
    
    # ====================================================================================================
    # From Node
    # ====================================================================================================

    def create_from_node(self, 
            node, 
            in_out: Literal['INPUT', 'OUPUT', 'BOTH']='INPUT',
            include: list = None, 
            exclude: list = [], 
            exclude_linked: bool = False,
            reuse: bool = True, 
            panel: str = ""):
        """ Create sockets linked to a node.

        Sockets are created and are linked to the provided node input sockets.
        The sockets to create are controlled with `include` and `exclude` lists.
        The sockets are created below the panel provided in argument.
        Current panel is also taken into account.
        If `reuse` argument is False, sockets are always created, if it is True, existing sockets are reused.

        Arguments
        ---------
        - node (Node) : the node to feed
        - in_out (str in ('INPUT', 'OUTPUT', 'BOTH')) : signature extension
        - include (list = None) : limit the sockets to the list of panels / sockets if not None
        - exclude (list = []) : exclude sockets from the list of panels / sockets
        - reused (bool = True) : reuse existing sockets when possible
        - panel (str = "") : panel in Group Input where to create sockets

        Returns
        -------
        - List of created input sockets
        """

        signature = node.get_signature(include=include, exclude=exclude, exclude_linked=exclude_linked, enabled_only=True, with_sockets=True)

        if in_out in ['INPUT', 'BOTH']:
            ins = self.set_input_signature(signature.input_signature, reuse=reuse, panel=panel)
        if in_out in ['OUTPUT', 'BOTH']:
            outs = self.set_output_signature(signature.output_signature, reuse=reuse, panel=panel)

        if in_out == 'INPUT':
            return ins
        elif in_out == 'OUTPUT':
            return outs
        else:
            return ins, outs
        





