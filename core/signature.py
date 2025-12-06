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

    __slots__ = ['_inputs', '_outputs']

    def __init__(self, inputs=None, outputs=None):
        """ Signature encapsulate two lists for inputs and outputs.

        The lists contain one dict per socket with at least the following keys:
        - name : socket name or path
        - socket_type : socket bl id name
        """

        if isinstance(inputs, Signature):
            self._inputs  = list(inputs.inputs)
            self._outputs = list(inputs.outputs)

        else:
            self.inputs  = inputs
            self.outputs = outputs
            
    def __str__(self):
        return f"<Signature ({len(self.inputs)}, {len(self.outputs)}): {self.input_names} -> {self.output_names}"
    
    def __repr__(self):
        a = [f"{d['name']:15s} : {d['socket_type']}" for d in self.inputs]
        b = [f"{d['name']:15s} : {d['socket_type']}" for d in self.outputs]
        s = f"<Signature  ({len(self.inputs)}, {len(self.outputs)})\n"
        s +=  "INPUT\n-   " + "\n-   ".join(a)
        s += "OUTPUT\n-   " + "\n-   ".join(b)
        return s + "\n"
    
    # ====================================================================================================
    # Inputs and outputs
    # ====================================================================================================

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        self._inputs = self._load_value(value)

    @property
    def outputs(self):
        return self._outputs

    @outputs.setter
    def outputs(self, value):
        self._outputs = self._load_value(value)

    @property
    def input_signature(self):
        return Signature(self.inputs)
    
    @property
    def output_signature(self):
        return Signature(self.outputs)
    
    # ====================================================================================================
    # Input and output names
    # ====================================================================================================

    @property
    def input_names(self):
        return [d['name'] for d in self._inputs]

    @property
    def output_names(self):
        return [d['name'] for d in self._outputs]
    
    @property
    def input_keys(self):
        return [(d.get('path', d['name']), d['socket_id']) for d in self._inputs]

    @property
    def output_keys(self):
        return [(d.get('path', d['name']), d['socket_id']) for d in self._outputs]
    
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
    def sockets(self):
        """ Return a non empty dict of any

        Priority is given to inputs if both are non empty
        """
        if len(self.inputs):
            return self.inputs
        else:
            return self.outputs
        
    def switch(self):
        sockets = self._inputs
        self._inputs = self._outputs
        self._outputs = sockets

        return self
    
    # ====================================================================================================
    # Check a dict
    # ====================================================================================================

    def _load_value(self, value):

        keys = ['socket_type', 'socket', 'type', 'bl_idname', 'class', 'class_name', 'socket_id', 'full_socket_id']

        if value is None:
            return []
        
        # ---------------------------------------------------------------------------
        # Dict to list
        # ---------------------------------------------------------------------------
        
        if isinstance(value, dict):
            a = []
            for k, v in value.items():

                # Value can be socket type
                if isinstance(v, dict):
                    d = {**v}
                else:
                    d = {'socket_type': SocketType(v).serialize()}

                # Key can be (name, socket_type)
                if isinstance(k, tuple) and len(k) == 2:
                    d['name'] = k[0]
                    d['socket_type'] = k[1]
                else:
                    d['name'] = k
                
                a.append(d)
        else:
            a = value

        # ---------------------------------------------------------------------------
        # Dict
        # ---------------------------------------------------------------------------

        res = []
        for v in a:
            if not isinstance(v, dict):
                raise RuntimeError(f"The signature values must be dicts, not {v} in {value}.")
            
            d = {**v}
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
                        f"There is no key in {list(d.keys())} which is a valid socket type key: {keys}")
            else:
                d['socket_type'] = SocketType(sid).serialize()

            if d.get('path') is None:
                d['path'] = d['name']

            d['key'] = (d['path'], SocketType(d['socket_type']).socket_id)

            res.append(d)
        
        return res
    
    # ====================================================================================================
    # From named sockets (used to initialize a Node for instance)
    # ====================================================================================================

    @classmethod
    def from_named_sockets(cls, named_sockets: dict = {}, with_sockets: bool = True, **sockets):

        from . import utils

        a = []
        for name, value in {**named_sockets, **sockets}.items():
            stype = SocketType(value)
            d = {
                'name'        : name,
                'socket_type' : stype.serialize(),
                'socket_id'   : stype.socket_id,
                'key'         : (name, stype.socket_id),
                }
            if with_sockets:
                bsocket = utils.get_bsocket(value)
                if bsocket is not None:
                    d[name]['socket'] = bsocket
            
            a.append(d)

        return cls(a)

    # ====================================================================================================
    # Join signatures
    # ====================================================================================================

    def join(self, *signatures):
        
        inputs, outputs = [], []
        in_keys, out_keys = set(), set()

        for value in [self] + list(signatures):

            sig = Signature(value)

            for d in sig.inputs:
                if d['key'] in in_keys:
                    continue
                inputs.append({**d})
                in_keys.add(d['key'])

            for d in sig.outputs:
                if d['key'] in out_keys:
                    continue
                inputs.append({**d})
                out_keys.add(d['key'])

        return Signature(inputs, outputs)
    
    def __add__(self, other):
        return self.join(Signature(other))
    
    def __radd__(self, other):
        return Signature(other).join(self)
        



    
    
    


