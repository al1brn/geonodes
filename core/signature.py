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

module : signature
------------------
A signature is a way to transport the description of sockets.
It basically contains a dict keyed by socket names and containing a dict of socket properties.

A dedicated class is used to expose utilities

updates
-------
- creation : 2025/11/18
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

import bpy
from . import constants
from . import utils

class Signature:
    def __init__(self, inputs={}, outputs={}):
        """ Signature encapsulate two dicts for inputs and outputs.

        The lists contain one dict per socket with at least the following keys:
        - name : socket name
        - socket_type : in ('FLOAT', 'INT', 'BOOLEAN', 'ROTATION', 'MATRIX', 'STRING', 'MENU',
          'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'CLOSURE', 'BUNDLE')
        - bl_idname : in ('NodeSocketFloat', 'NodeSocketInt'...)
        """

        if isinstance(inputs, Signature):
            self.inputs  = inputs.inputs
            self.outputs = inputs.outputs

        else:
            self.inputs  = inputs
            self.outputs = outputs
            
    def __str__(self):
        if self.is_closure:
            return f"<Signature (closure) {len(self[0])} / {len(self[1])} sockets>"
        else:
            return f"<Signature (single) {len(self.sockets)} sockets>"
    
    def __repr__(self):    
        if self.is_closure:
            a = [f"{name:15s} : {d['socket_type']}" for name, d in self.inputs.items()]
            b = [f"{name:15s} : {d['socket_type']}" for name, d in self.outputs.items()]
            return str(self) + "\nINPUT\n- " + "\n- ".join(a) + "\nOUTPUT\n- " + "\n- ".join(b)
        else:
            a = [f"{name:15s} : {d['socket_type']}" for name, d in self.sockets.items()]
            return str(self) + "\n- " + "\n- ".join(a)
    
    # ====================================================================================================
    # Inputs and outputs
    # ====================================================================================================

    @property
    def inputs(self):
        if hasattr(self, '_inputs'):
            return self._inputs
        else:
            return {}

    @inputs.setter
    def inputs(self, value):
        self._inputs = self._load_dict(value)

    @property
    def outputs(self):
        if hasattr(self, '_outputs'):
            return self._outputs
        else:
            return {}

    @outputs.setter
    def outputs(self, value):
        self._outputs = self._load_dict(value)

    @property
    def input_signature(self):
        return Signature(self.inputs)
    
    @property
    def output_signature(self):
        return Signature(self.outputs)
    
    # ====================================================================================================
    # Behaves as a couple
    # ====================================================================================================

    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        if index in [0, 'INPUT']:
            return self.inputs
        elif index in [1, 'OUTPUT']:
            return self.outputs
        else:
            raise IndexError(f"Invalid index for Signature of length 2: {index}")
        
    def __setitem__(self, index, value):
        if index in [0, 'INPUT']:
            self.inputs = value
        elif index in [1, 'OUTPUT']:
            self.outputs = value
        else:
            raise IndexError(f"Invalid index for Signature of length 2: {index}")
        
    def __iter__(self):
        return (sockets for sockets in (self.inputs, self.outputs))
    
    # ====================================================================================================
    # Closure needs two non empty dicts
    # ====================================================================================================

    @property
    def is_closure(self):
        return len(self.inputs) and len(self.outputs)
    
    @property
    def sockets(self):
        """ Return a non empty dict of any

        Priority is given to inputs if both are non empty
        """
        if len(self.inputs):
            return self.inputs
        else:
            return self.outputs
        
    def switch(self):
        sockets = self.inputs
        self.inputs = self.outputs
        self.outputs = sockets

        return self
    
    # ====================================================================================================
    # Check a dict
    # ====================================================================================================

    def _load_dict(self, sockets):

        if sockets is None:
            return {}

        res = {}
        msg = None
        for name, info in sockets.items():

            try:
                d = {**info}
            except Exception as e:
                from pprint import pprint
                print("?"*100)
                print(f"sockets.keys: {list(sockets.keys())}\n")
                print(f"pprint of '{name}': d\n")
                pprint(info)
                print("?"*100)
                print("pprint of sockets\n")
                pprint(sockets)
                print("?"*100)
                raise e
            
            # ----------------------------------------------------------------------------------------------------
            # Must have a socket_type entry
            # ----------------------------------------------------------------------------------------------------

            socket_type = d.get('socket_type')
            bl_idname   = d.get('bl_idname')
            subtype     = None
            dims        = None

            if socket_type is None and bl_idname is None:
                if d.get('class') is None:
                    msg = f"name: '{name}': the dict doesn't contain nor 'socket_type' neither 'bl_idname' key key."
                else:
                    for k, v in constants.CLASS_NAMES.items():
                        if v == d['class']:
                            socket_type = k
                            break
                    if socket_type is None:
                        if d['class'] in constants.GEOMETRY_CLASSES:
                            socket_type = 'GEOMETRY'
                        else:
                            msg = f"name: '{name}': the class name '{d['class']}' is non valid. Should be in {list(constants.CLASS_NAMES.values()) + constants.GEOMETRY_CLASSES}."

                    if msg is None:
                        bl_idname = utils.socket_type_to_bl_idname(socket_type)

            else:
                if socket_type is None:
                    socket_type, subtype, dims = utils.get_socket_subtype(bl_idname)
                else:
                    socket_type, subtype, dims = utils.get_socket_subtype(socket_type)

            if msg is not None:
                from pprint import pprint
                print('?'*100)
                pprint(sockets)
                print('?'*100)
                raise RuntimeError(f"Invalid signature dict:  {msg}")
            
            # ----------------------------------------------------------------------------------------------------
            # Set socket_type, subtype and dimensions
            # ----------------------------------------------------------------------------------------------------

            assert socket_type is not None

            d['socket_type'] = socket_type
            if subtype is None:
                subtype = d.get('props', {}).get('subtype')
            if dims is None:
                dims = d.get('props', {}).get('dimensions')

            if subtype is not None or dims is not None:
                if 'props' not in d:
                    d['props'] = {}
                if subtype is not None:
                    d['props']['subtype'] = subtype
                if dims is not None:
                    d['props']['dimensions'] = dims

            # ----------------------------------------------------------------------------------------------------
            # We've got someting normalized
            # ----------------------------------------------------------------------------------------------------
            
            res[name] = d
        
        return res

    # ====================================================================================================
    # Initialize from a collection of sockets (node.inputs or node.outputs)
    # ====================================================================================================

    @classmethod
    def from_sockets(cls, 
            sockets_coll, 
            include: list = None, 
            exclude: list = [], 
            enabled_only: bool = False, 
            exclude_linked: bool =False, 
            with_sockets: bool = False):

        sockets = {}
        if sockets_coll is not None:

            names = {}
            for socket in sockets_coll:
                if socket.type == 'CUSTOM':
                    continue
                if enabled_only and not socket.enabled:
                    continue
                if include is not None and socket.name not in include:
                    continue
                if socket.name in exclude:
                    continue
                if exclude_linked and (socket.is_linked and not socket.is_multi_input):
                    continue

                name = socket.name
                key = name
                if socket.name in names:
                    names[name] += 1
                    key = f"{name}.{names[name]:03d}"
                else:
                    names[name] = 0

                sockets[key] = {
                    'name'        : name, 
                    'rank'        : names[name], 
                    'bl_idname'   : socket.bl_idname, 
                    'socket_type' : socket.type,
                    'identifier'  : socket.identifier,
                    }
                
                if with_sockets:
                    sockets[key]['socket'] = socket

        return Signature(sockets)
    
    # ====================================================================================================
    # Initialize from a node
    # ====================================================================================================

    @classmethod
    def from_node(cls, 
            node, 
            include: list = None,
            exclude: list = [], 
            enabled_only = False, 
            exclude_linked: bool = False,
            with_sockets: bool = False):

        from .treeinterface import TreeInterface

        node = utils.get_bnode(node)

        # The node has a TreeInterface
        if hasattr(node, 'node_tree'):
            tinf = TreeInterface(node.node_tree)
            return tinf.get_signature(include=include, exclude=exclude, exclude_linked=exclude_linked, with_sockets=with_sockets)
        
        # From sockets
        return cls(
            cls.from_sockets(node.inputs,  include=include, exclude=exclude, enabled_only=enabled_only, exclude_linked=exclude_linked, with_sockets=with_sockets).sockets,
            cls.from_sockets(node.outputs, enabled_only=enabled_only, exclude_linked=exclude_linked, with_sockets=with_sockets).sockets
        )

    # ====================================================================================================
    # Join signatures
    # ====================================================================================================

    def join(self, *signatures):
        
        inputs  = {}
        outputs = {}

        for s in [self] + list(signatures):
            for name, d in s.inputs.items():
                if name in inputs:
                    continue
                inputs[name] = {**d}

            for name, d in s.outputs.items():
                if name in outputs:
                    continue
                outputs[name] = {**d}

        return Signature(inputs, outputs)
    
    def __add__(self, other):
        return self.join(Signature(other))
    
    def __radd__(self, other):
        return Signature(other).join(self)
        
    # ====================================================================================================
    # Set the signature to items collection
    # ====================================================================================================

    def create_items(self, items, use_rank: bool = False, use_panel: bool = False, panel: str = ""):
        """ Create items in a node_items collection.

        Arguments
        ---------
        - items (bpy.types.prop_collection) : the collection of items
        - use_rank (bool = False) : add rank to homonyms
        - use_panel (bool = False) : prefix name with panel name

        Returns
        -------
        - list of created sockets
        """

        sockets = self.sockets
        names = {}
        created = {}

        for name, d in sockets.items():
            full_name = name
            if use_panel:
                panels = [] if panel == "" else [panel]
                panels = panels + [p['name'] for p in d.get('panels', [])]
                full_name = " ".join(panels + [name])

            if full_name in names:
                names[full_name] += 1
                if use_rank:
                    full_name += f" {names[full_name]}"

            else:
                names[full_name] = 0

            created[name] = items.new(utils.bl_idname_to_socket_type(d['socket_type']), full_name)

        return created
    




    
    
    


