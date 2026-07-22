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

module : geometry_class
-----------------------
- Geometry class

Geometry class inherits from Socket.
Subclasses of Geometry represent the different types of Geometries: Mesh, Curve...

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


from .nodeclass import Node
from . import utils
from .socket_class import Socket
from .geom import Geom
from . import generated
from .treeinterface import ItemPath

# ====================================================================================================
# Geometry class
# ====================================================================================================

class Geometry(generated.Geometry, Geom):

    __slots__ = Socket.__slots__ + ('_geo', '_selection')

    SOCKET_TYPE = 'GEOMETRY'

    def __init__(self,
        value               : Socket = None, 
        name                : str = None,
        tip                 : str = '',
        panel               : str = "",
        **props,
    ):
        """ Socket of type 'GEOMETRY'.

        If value is None, a Group Input socket of type Geometry is created.
        When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

        ``` python
        geometry = Geometry() # Default group input geometry
        geometry = Geometry(name="Mesh") # Input group geometry
        ```

        Parameters
        ----------
        value : Socket, optional
            initial value default=None.

        name : str, optional
            Create an Group Input socket with the provided str default=None.

        tip : str, default=''
            Property description

        panel : str, optional
            Panel name default="".

        props : dict
            input properties

        """
        # ---------------------------------------------------------------------------
        # Geom interface
        # ---------------------------------------------------------------------------

        self._geo       = self
        self._selection = None

        super().__init__(value, name=name, tip=tip, panel=panel, **props)

    # ====================================================================================================
    # get item is ambiguous since V5.2
    # ====================================================================================================

    def __getitem__(self, index):
        if self._is_list:
            return Socket.__getitem__(self, index)
        else:
            return Geom.__getitem__(self, index)
        
    # ====================================================================================================
    # Attributes
    # ====================================================================================================

    def get(self, name, data_type=None, domain=None, prefix=None):
        """Return a helper for a named attribute on this geometry.

        > Node <&Node Named Attribute>

        The returned <!Attribute> stores the geometry, attribute name, data
        type and domain. No node is created until the attribute is read or
        written. Reading the attribute creates the node.

        ``` python
        mesh = Mesh()
        weight = mesh.get("Weight", Float, domain="Point")
        field = weight.value
        ```

        Parameters
        ----------
        name : str
            Name of the attribute.
        data_type : type | str | value, optional
            Attribute socket type, for example ``Float``, ``Integer`` or
            ``Vector``. The default is ``Float``.
        domain : str | Domain, optional
            Domain on which the attribute is stored. The default is ``Point``.
        prefix : str, optional
            Prefix prepended to the attribute name.

        Returns
        -------
        Attribute
            Named-attribute helper attached to this geometry.
        """
        from .attributes import Attribute

        attr = Attribute(name, data_type=data_type, domain=domain, prefix=prefix)
        attr.geometry = self
        return attr
    
    def set(self, name, value, domain=None):
        """Store a named attribute on this geometry.

        > Node <&Node Store Named Attribute>

        This is the direct counterpart of ``get()`` when a helper does not
        need to be kept. The value determines the attribute data type.

        ``` python
        mesh = Mesh()
        attr = mesh.set("Weight", 1.0, domain="Point")
        mesh.set("Direction", (0, 0, 1), domain="Face")
        ```

        Parameters
        ----------
        name : str
            Name of the attribute to create or update.
        value : value | Socket
            Constant or field stored in the attribute.
        domain : str | Domain, optional
            Domain on which to store the attribute. The default is ``Point``.

        Returns
        -------
        Attribute
            Helper representing the stored attribute.
        """
        from .attributes import Attribute

        if isinstance(name, Attribute):
            attr = Attribute(name.name, value, domain=domain, prefix=name.prefix)
        else:
            attr = self.get(name, value, domain=domain)
            
        attr.set(value)
        return attr

    
    def get_attribute_names(self, data_type=None, domain=None):
        """Return the names of attributes available on this geometry.

        > Node <&Node Get Attribute Names>

        Supplying ``data_type`` or ``domain`` enables the corresponding filter
        on the node. Leaving an argument unset disables that filter.

        ``` python
        mesh = Mesh()

        names = mesh.get_attribute_names()
        vector_names = mesh.get_attribute_names(Vector)
        face_vectors = mesh.get_attribute_names(Vector, domain="Face")
        ```

        Parameters
        ----------
        data_type : type | str | value, optional
            Restrict the result to this attribute data type.
        domain : str | Domain, optional
            Restrict the result to this geometry domain.

        Returns
        -------
        String
            String socket containing the matching attribute names.
        """
        from .attributes import Attribute

        _, dn = Attribute._get_geo_domain(domain)
        dt = Attribute._get_data_type(data_type)

        ok_dt = dt is not None
        ok_dn = dn is not None

        return Node("Get Attribute Names", {
            "Geometry": self,
            "Filter Data Type" : ok_dt,
            "Data Type" : dt,
            "Filter Domain" : ok_dn,
            "Domain" : dn
            })._out

    # ====================================================================================================
    # Geometry Operations
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Bake
    # ----------------------------------------------------------------------------------------------------

    def bake(self, **kwargs):
        """ Node <&Node Bake>

        [&JUMP]

        Returns
        -------
        Geometry
            self

        """

        node = Node('Bake', {'Geometry': self})

        items = node._bnode.bake_items
        for name, value in kwargs.items():
            items.new(utils.get_value_socket_type(value), name)

        return self._jump(node._out)

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def __add__(self, other):
        if isinstance(other, tuple):
            return type(self).Join(self, *other)

        elif isinstance(other, type(self)):
            return type(self).Join(self, other)

        else:
            return Geometry.Join(self, other)
        
    def __iadd__(self, other):
        return self._jump(self + other)
        
