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

from . import constants
from . import utils
from .sockettype import SocketType

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

        keys = ['socket_type', 'socket', 'type', 'bl_idname', 'class', 'class_name', 'socket_id', 'full_socket_id']

        if sockets is None:
            return {}

        res = {}
        for name, info in sockets.items():

            if isinstance(info, dict):
                d = {**info}
                sid = d.get('socket_type')
                if sid is None:
                    ok = False
                    for n, v in d.items():
                        if n in keys:
                            d['socket_type'] = SocketType(v).serialize()
                            ok = True
                            break

                    if not ok:
                        raise RuntimeError(f"Invalid Signature dict for name '{name}': "
                            f"there is no key in {list(d.keys())} which is a valid socket type key: {keys}")
                else:
                    d['socket_type'] = SocketType(sid).serialize()

            else:
                d = {'socket_type': SocketType(info).serialize()}

            res[name] = d
        
        return res
    
    # ====================================================================================================
    # From named sockets (used to initialize a Node for instance)
    # ====================================================================================================

    @classmethod
    def from_named_sockets(cls, named_sockets: dict = {}, with_sockets: bool = True, **sockets):

        from . import utils

        sig = {}
        for name, value in {**named_sockets, **sockets}.items():
            sig[name] = {'socket_type': SocketType(value).serialize()}
            if with_sockets:
                bsocket = utils.get_bsocket(value)
                if bsocket is not None:
                    sig[name]['socket'] = bsocket

        return cls(sig)

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
        



    
    
    


