# Generated 2025-12-07 10:17:11

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Boolean(Socket):
    """"
    $DOC SET hidden
    """
    def band(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'AND'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='AND')
        return node._out

    def bor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'OR'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='OR')
        return node._out

    def bnot(self):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'NOT'

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self}, operation='NOT')
        return node._out

    def not_and(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'NAND'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='NAND')
        return node._out

    def nor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'NOR'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='NOR')
        return node._out

    def xnor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'XNOR'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='XNOR')
        return node._out

    def xor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'XOR'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='XOR')
        return node._out

    def imply(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'IMPLY'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='IMPLY')
        return node._out

    def nimply(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        Information
        -----------
        - Socket 'Boolean' : self
        - Parameter 'operation' : 'NIMPLY'

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean_001)

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='NIMPLY')
        return node._out

    @classmethod
    def Random(cls, probability: Float = None, id: Integer = None, seed: Integer = None):
        """ > Node <&Node Random Value>

        Information
        -----------
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - probability (Float) : socket 'Probability' (id: Probability)
        - id (Integer) : socket 'ID' (id: ID)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Boolean
        """
        node = Node('Random Value', {'Probability': probability, 'ID': id, 'Seed': seed}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Attribute', {'Name': name}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Attribute', {'Name': name}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    @property
    def is_viewport(cls):
        """ > Node <&Node Is Viewport>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Viewport', )
        return node._out

    def uv_unwrap(self,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal'] = None):
        """ > Node <&Node UV Unwrap>

        Information
        -----------
        - Socket 'Selection' : self

        Arguments
        ---------
        - seam (Boolean) : socket 'Seam' (id: Seam)
        - margin (Float) : socket 'Margin' (id: Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (id: Fill Holes)
        - method (menu='Angle Based') : ('Angle Based', 'Conformal')

        Returns
        -------
        - Vector
        """
        node = Node('UV Unwrap', {'Selection': self, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes, 'Method': method})
        return node._out

    def error(self, message: String = None):
        """ > Node <&Node Warning>

        Information
        -----------
        - Socket 'Show' : self
        - Parameter 'warning_type' : 'ERROR'

        Arguments
        ---------
        - message (String) : socket 'Message' (id: Message)

        Returns
        -------
        - Boolean
        """
        node = Node('Warning', {'Show': self, 'Message': message}, warning_type='ERROR')
        return node._out

    def warning(self, message: String = None):
        """ > Node <&Node Warning>

        Information
        -----------
        - Socket 'Show' : self
        - Parameter 'warning_type' : 'WARNING'

        Arguments
        ---------
        - message (String) : socket 'Message' (id: Message)

        Returns
        -------
        - Boolean
        """
        node = Node('Warning', {'Show': self, 'Message': message}, warning_type='WARNING')
        return node._out

    def info(self, message: String = None):
        """ > Node <&Node Warning>

        Information
        -----------
        - Socket 'Show' : self
        - Parameter 'warning_type' : 'INFO'

        Arguments
        ---------
        - message (String) : socket 'Message' (id: Message)

        Returns
        -------
        - Boolean
        """
        node = Node('Warning', {'Show': self, 'Message': message}, warning_type='INFO')
        return node._out

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation (menu='Trilinear') : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')

        Returns
        -------
        - Boolean
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='BOOLEAN')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - x (Integer) : socket 'X' (id: X)
        - y (Integer) : socket 'Y' (id: Y)
        - z (Integer) : socket 'Z' (id: Z)

        Returns
        -------
        - Boolean
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='BOOLEAN')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        Information
        -----------
        - Socket 'Topology' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Returns
        -------
        - None
        """
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='BOOLEAN', **sockets)
        return node._out

    def prune_grid(self, mode: Literal['Inactive', 'Threshold', 'SDF'] = None):
        """ > Node <&Node Prune Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - mode (menu='Threshold') : ('Inactive', 'Threshold', 'SDF')

        Returns
        -------
        - Boolean
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode}, data_type='BOOLEAN')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Returns
        -------
        - Boolean
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='BOOLEAN')
        return node._out

    @classmethod
    def voxel_index(cls):
        """ > Node <&Node Voxel Index>

        Returns
        -------
        - Integer [y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_x_ (Integer), extent_y_ (Integer), extent_z_ (Integer)]
        """
        node = Node('Voxel Index', )
        return node._out

    def set_grid_background(self, background: Boolean = None):
        """ > Node <&Node Set Grid Background>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - background (Boolean) : socket 'Background' (id: Background)

        Returns
        -------
        - Boolean
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background}, data_type='BOOLEAN')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Boolean [grid_ (Boolean)]
        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='BOOLEAN')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Returns
        -------
        - Matrix [background_value_ (Boolean)]
        """
        node = Node('Grid Info', {'Grid': self}, data_type='BOOLEAN')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Boolean
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='BOOLEAN')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = False,
        name: str = 'Boolean',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        layer_selection: bool = False,
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Boolean Input

        New <#Boolean> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = False) : Default value
        - name  (str = 'Boolean') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default_attribute  (str = '') : Property default_attribute_name
        - layer_selection  (bool = False) : Property layer_selection_field
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Boolean
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketBool', default_value = defval, name=name,
            tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default_attribute=default_attribute,
            layer_selection=layer_selection, shape=shape)

