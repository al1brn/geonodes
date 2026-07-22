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

from . import generated
from .nodeclass import Node

class String(generated.String):
    """ String Socket.

    A String socket easily operated with python str.

    ``` python
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
    ```
    """

    SOCKET_TYPE = 'STRING'

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
        return self._jump(self.__mul__(other))
        
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

            with Layout("Operators"):
                s = String("String")
                Boolean(True).info("Prefix " + s)
                s += " suffix"
                Boolean(True).info(s)
                s *= ("A", "B", "C")
                Boolean(True).info(s)

            with Layout("Compare and Search"):
                s = String("Geometry Nodes")
                s.equal("Geometry Nodes").bnot().warning("Equal strings expected")
                s.not_equal("Geometry Nodes").warning("Equal strings expected")
                s.find("Nodes").not_equal(9).warning("'Nodes' expected at position 9")
                s.find_in_string("o", mode="From End").not_equal(10).warning("Last 'o' expected at position 10")
                s.hash_value(seed=0).out()

            with Layout("Slice and Length"):
                s = String("Geometry Nodes")
                part = s.slice(position=9, length=5)
                part.not_equal("Nodes").warning("'Nodes' expected")
                s.length().not_equal(14).warning("String length 14 expected")

            with Layout("String Operations"):
                s = String("  Geometry Nodes  ")
                Boolean(True).info(s.trim(whitespace=True, start=True, end=True))
                Boolean(True).info(s.reverse())
                Boolean(True).info(s.lower())
                Boolean(True).info(s.upper())
                Boolean(True).info(s.set_case("Uppercase"))

                parts = String("one/two/three").split("/")
                parts.list_length().not_equal(3).warning("Three strings expected")

                String("Geometry Nodes").tag_filter("Geometry").info("Tag filter matched")

            with Layout("Class Format"):
                s = String.Format(format="Float: {:.2f}, Integer: {}", float=3.14159, integer=123)
                Boolean(True).info(s)

            with Layout("String to Curves"):
                _curves = String("Geometry Nodes").to_curves(size=1.)
                g += _curves
                
            g.out()
        
