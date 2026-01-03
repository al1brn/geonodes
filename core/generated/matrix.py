# Generated 2026-01-03 16:39:50

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


class Matrix(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def Combine(cls,
                    column_1_row_1: Float = None,
                    column_1_row_2: Float = None,
                    column_1_row_3: Float = None,
                    column_1_row_4: Float = None,
                    column_2_row_1: Float = None,
                    column_2_row_2: Float = None,
                    column_2_row_3: Float = None,
                    column_2_row_4: Float = None,
                    column_3_row_1: Float = None,
                    column_3_row_2: Float = None,
                    column_3_row_3: Float = None,
                    column_3_row_4: Float = None,
                    column_4_row_1: Float = None,
                    column_4_row_2: Float = None,
                    column_4_row_3: Float = None,
                    column_4_row_4: Float = None):
        """ > Node <&Node Combine Matrix>

        Arguments
        ---------
        - column_1_row_1 (Float) : socket 'Column 1 Row 1' (id: Column 1 Row 1)
        - column_1_row_2 (Float) : socket 'Column 1 Row 2' (id: Column 1 Row 2)
        - column_1_row_3 (Float) : socket 'Column 1 Row 3' (id: Column 1 Row 3)
        - column_1_row_4 (Float) : socket 'Column 1 Row 4' (id: Column 1 Row 4)
        - column_2_row_1 (Float) : socket 'Column 2 Row 1' (id: Column 2 Row 1)
        - column_2_row_2 (Float) : socket 'Column 2 Row 2' (id: Column 2 Row 2)
        - column_2_row_3 (Float) : socket 'Column 2 Row 3' (id: Column 2 Row 3)
        - column_2_row_4 (Float) : socket 'Column 2 Row 4' (id: Column 2 Row 4)
        - column_3_row_1 (Float) : socket 'Column 3 Row 1' (id: Column 3 Row 1)
        - column_3_row_2 (Float) : socket 'Column 3 Row 2' (id: Column 3 Row 2)
        - column_3_row_3 (Float) : socket 'Column 3 Row 3' (id: Column 3 Row 3)
        - column_3_row_4 (Float) : socket 'Column 3 Row 4' (id: Column 3 Row 4)
        - column_4_row_1 (Float) : socket 'Column 4 Row 1' (id: Column 4 Row 1)
        - column_4_row_2 (Float) : socket 'Column 4 Row 2' (id: Column 4 Row 2)
        - column_4_row_3 (Float) : socket 'Column 4 Row 3' (id: Column 4 Row 3)
        - column_4_row_4 (Float) : socket 'Column 4 Row 4' (id: Column 4 Row 4)

        Returns
        -------
        - Matrix
        """
        node = Node('Combine Matrix', {'Column 1 Row 1': column_1_row_1, 'Column 1 Row 2': column_1_row_2, 'Column 1 Row 3': column_1_row_3, 'Column 1 Row 4': column_1_row_4, 'Column 2 Row 1': column_2_row_1, 'Column 2 Row 2': column_2_row_2, 'Column 2 Row 3': column_2_row_3, 'Column 2 Row 4': column_2_row_4, 'Column 3 Row 1': column_3_row_1, 'Column 3 Row 2': column_3_row_2, 'Column 3 Row 3': column_3_row_3, 'Column 3 Row 4': column_3_row_4, 'Column 4 Row 1': column_4_row_1, 'Column 4 Row 2': column_4_row_2, 'Column 4 Row 3': column_4_row_3, 'Column 4 Row 4': column_4_row_4})
        return cls(node._out)

    @classmethod
    def CombineTransform(cls,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Combine Transform>

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Matrix
        """
        node = Node('Combine Transform', {'Translation': translation, 'Rotation': rotation, 'Scale': scale})
        return cls(node._out)

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'MATRIX'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='MATRIX')
        return node._out

    def invert(self):
        """ > Node <&Node Invert Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - Matrix [invertible_ (Boolean)]
        """
        node = Node('Invert Matrix', {'Matrix': self})
        return node._out

    def determinant(self):
        """ > Node <&Node Matrix Determinant>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - Float
        """
        node = Node('Matrix Determinant', {'Matrix': self})
        return node._out

    def multiply(self, matrix: Matrix = None):
        """ > Node <&Node Multiply Matrices>

        Information
        -----------
        - Socket 'Matrix' : self

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix_001)

        Returns
        -------
        - Matrix
        """
        node = Node('Multiply Matrices', {'Matrix': self, 'Matrix_001': matrix})
        return node._out

    def project_point(self, vector: Vector = None):
        """ > Node <&Node Project Point>

        Information
        -----------
        - Socket 'Transform' : self

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)

        Returns
        -------
        - Vector
        """
        node = Node('Project Point', {'Vector': vector, 'Transform': self})
        return node._out

    @property
    def as_tuple(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - tuple (Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float)
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return (node.column_1_row_1, node.column_1_row_2, node.column_1_row_3, node.column_1_row_4, node.column_2_row_1, node.column_2_row_2, node.column_2_row_3, node.column_2_row_4, node.column_3_row_1, node.column_3_row_2, node.column_3_row_3, node.column_3_row_4, node.column_4_row_1, node.column_4_row_2, node.column_4_row_3, node.column_4_row_4)

    def separate(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - node [column_1_row_1 (Float), column_1_row_2 (Float), column_1_row_3 (Float), column_1_row_4 (Float), column_2_row_1 (Float), column_2_row_2 (Float), column_2_row_3 (Float), column_2_row_4 (Float), column_3_row_1 (Float), column_3_row_2 (Float), column_3_row_3 (Float), column_3_row_4 (Float), column_4_row_1 (Float), column_4_row_2 (Float), column_4_row_3 (Float), column_4_row_4 (Float)]
        """
        node = Node('Separate Matrix', {'Matrix': self})
        return node

    def separate_matrix(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - node [column_1_row_1 (Float), column_1_row_2 (Float), column_1_row_3 (Float), column_1_row_4 (Float), column_2_row_1 (Float), column_2_row_2 (Float), column_2_row_3 (Float), column_2_row_4 (Float), column_3_row_1 (Float), column_3_row_2 (Float), column_3_row_3 (Float), column_3_row_4 (Float), column_4_row_1 (Float), column_4_row_2 (Float), column_4_row_3 (Float), column_4_row_4 (Float)]
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node

    @property
    def column_1_row_1(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_1
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_1_row_1

    @property
    def column_1_row_2(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_2
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_1_row_2

    @property
    def column_1_row_3(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_3
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_1_row_3

    @property
    def column_1_row_4(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_4
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_1_row_4

    @property
    def column_2_row_1(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_1
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_2_row_1

    @property
    def column_2_row_2(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_2
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_2_row_2

    @property
    def column_2_row_3(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_3
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_2_row_3

    @property
    def column_2_row_4(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_4
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_2_row_4

    @property
    def column_3_row_1(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_1
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_3_row_1

    @property
    def column_3_row_2(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_2
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_3_row_2

    @property
    def column_3_row_3(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_3
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_3_row_3

    @property
    def column_3_row_4(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_4
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_3_row_4

    @property
    def column_4_row_1(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_1
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_4_row_1

    @property
    def column_4_row_2(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_2
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_4_row_2

    @property
    def column_4_row_3(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_3
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_4_row_3

    @property
    def column_4_row_4(self):
        """ > Node <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_4
        """
        node = self._cache('Separate Matrix', {'Matrix': self})
        return node.column_4_row_4

    @property
    def trs(self):
        """ > Node <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - tuple (Vector, Rotation, Vector)
        """
        node = Node('Separate Transform', {'Transform': self})
        return (node.translation, node.rotation, node.scale)

    def separate_transform(self):
        """ > Node <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - node [translation (Vector), rotation (Rotation), scale (Vector)]
        """
        node = self._cache('Separate Transform', {'Transform': self})
        return node

    @property
    def translation(self):
        """ > Node <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - translation
        """
        node = self._cache('Separate Transform', {'Transform': self})
        return node.translation

    @property
    def rotation(self):
        """ > Node <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - rotation
        """
        node = self._cache('Separate Transform', {'Transform': self})
        return node.rotation

    @property
    def scale(self):
        """ > Node <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - scale
        """
        node = self._cache('Separate Transform', {'Transform': self})
        return node.scale

    def transform_direction(self, direction: Vector = None):
        """ > Node <&Node Transform Direction>

        Information
        -----------
        - Socket 'Transform' : self

        Arguments
        ---------
        - direction (Vector) : socket 'Direction' (id: Direction)

        Returns
        -------
        - Vector
        """
        node = Node('Transform Direction', {'Direction': direction, 'Transform': self})
        return node._out

    def transform_point(self, vector: Vector = None):
        """ > Node <&Node Transform Point>

        Information
        -----------
        - Socket 'Transform' : self

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)

        Returns
        -------
        - Vector
        """
        node = Node('Transform Point', {'Vector': vector, 'Transform': self})
        return node._out

    def transpose(self):
        """ > Node <&Node Transpose Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - Matrix
        """
        node = Node('Transpose Matrix', {'Matrix': self})
        return node._out

    def transform_gizmo(self,
                    *value: Matrix,
                    position: Vector = None,
                    rotation: Rotation = None,
                    use_rotation_x = True,
                    use_rotation_y = True,
                    use_rotation_z = True,
                    use_scale_x = True,
                    use_scale_y = True,
                    use_scale_z = True,
                    use_translation_x = True,
                    use_translation_y = True,
                    use_translation_z = True):
        """ > Node <&Node Transform Gizmo>

        Arguments
        ---------
        - value (Matrix) : socket 'Value' (id: Value)
        - position (Vector) : socket 'Position' (id: Position)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - use_rotation_x (bool): parameter 'use_rotation_x'
        - use_rotation_y (bool): parameter 'use_rotation_y'
        - use_rotation_z (bool): parameter 'use_rotation_z'
        - use_scale_x (bool): parameter 'use_scale_x'
        - use_scale_y (bool): parameter 'use_scale_y'
        - use_scale_z (bool): parameter 'use_scale_z'
        - use_translation_x (bool): parameter 'use_translation_x'
        - use_translation_y (bool): parameter 'use_translation_y'
        - use_translation_z (bool): parameter 'use_translation_z'

        Returns
        -------
        - Geometry
        """
        node = Node('Transform Gizmo', {'Value': [self] + list(value), 'Position': position, 'Rotation': rotation}, use_rotation_x=use_rotation_x, use_rotation_y=use_rotation_y, use_rotation_z=use_rotation_z, use_scale_x=use_scale_x, use_scale_y=use_scale_y, use_scale_z=use_scale_z, use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT4X4'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Matrix
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT4X4')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT4X4'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Matrix
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT4X4')
        return cls(node._out)

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'MATRIX'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Matrix
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='MATRIX')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        name: str = 'Matrix',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INSTANCE_TRANSFORM'] = 'VALUE',
        shape: Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE'] = 'AUTO',
         ):
        """ > Matrix Input

        New <#Matrix> input with subtype 'NONE'.

        Aguments
        --------
        - name  (str = 'Matrix') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INSTANCE_TRANSFORM')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE')

        Returns
        -------
        - Matrix
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketMatrix', name=name, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default_attribute=default_attribute, default_input=default_input, shape=shape)

