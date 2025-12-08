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

module : sock_string
---------------------
- String socket

This class inherits from Socket and from generated.String
which is automatically generated.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


import numpy as np

import bpy
from . import utils
from .treeclass import Tree
from .nodeclass import Node
from .socket_class import Socket
from .  import generated

class String(generated.String):

    SOCKET_TYPE = 'STRING'

    def __init__(self, 
        value: Socket = None,
        name: str = None,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        subtype: str = 'NONE',
        ):
        """ Socket of type String

        Node <&Node String>

        A group input socket of type String is created if the name is not None.

        Arguments
        ---------
        - value (str or Socket = None) : initial value
        - name (str = None) : group input socket name if not None
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - subtype (str = 'NONE') : Socket sub type in ('NONE', 'FILE_PATH')
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('String', string=str(value))._out
            else:
                bsock = self._create_input_socket(value=value, name=name, tip=tip,
                    panel=panel, optional_label=optional_label, hide_value=hide_value,
                    hide_in_modifier=hide_in_modifier, subtype=subtype)
                
        super().__init__(bsock)

    # ====================================================================================================
    # Operators

    def __add__(self, other):
        if isinstance(other, tuple):
            return Node('Join Strings', {'Strings': [self] + list(other)})._out
        else:
            return Node('Join Strings', {'Strings': [self, other]})._out

    def __radd__(self, other):
        return Node('Join Strings', {'Strings': [other, self]})._out

    def __iadd__(self, other):
        return self._jump(self + other)

    def __mul__(self, other):
        if isinstance(other, tuple):
            return self.join(*other)
        else:
            return self.join(other)

    def __imul__(self, other):
        if isinstance(other, tuple):
            return self.join(*other)
        else:
            return self.join(other)
        
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, String, Boolean, Integer, nd, Input

        with GeoNodes("String Test") as tree:
            
            g = Mesh()
            name = String("Attribute", name="Attr name")
            g.points.store(name, 0.)
            
            a = String("String A ")
            b = a + "String B "
            c = a + (b, Integer(123).to_string())
            d = c.replace("String", "TK")
            s = String.Join(a, b, c, d, delimiter = "/")
            Boolean(True).info(s)
            
            with Layout("Match String"):
                ref_string = String("Matching test string")
                search_string = String("test", name="Search String")
                
                ok = ref_string.match_string(Input("Match"), search_string)
                ok.info(String("'{}' found in '{}'.").format(token=search_string, ref=ref_string))
                ok.bnot().warning(String("'{}' not found in '{}'.").format(token=search_string, ref=ref_string))
                
            with Layout("Conversion"):
                f = String("3.1415926").to_float()
                i = String("123").to_integer()
                
                sf = f.to_string(decimals=4)
                si = i.to_string()
                
                s = String("Float: {:.2f}, Int: {:05d} ({} and {})").format(float=f, integer=i, sfloat=sf, sint=si)
                Boolean(True).info(s)
                
            with Layout("Special"):
                _n = nd.special_characters().line_break
                _t = nd.special_characters().tab
                s = "Text with \t and \n"
                s = String(s).replace(_t, "TAB").replace(_n, "LINE_BREAK")
                Boolean(True).info(s)
                
            g.out()
        
