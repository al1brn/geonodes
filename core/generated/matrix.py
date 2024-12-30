from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Matrix(Socket):

    @classmethod
    def Combine(cls, column_1_row_1=None, column_1_row_2=None, column_1_row_3=None, column_1_row_4=None, column_2_row_1=None, column_2_row_2=None, column_2_row_3=None, column_2_row_4=None, column_3_row_1=None, column_3_row_2=None, column_3_row_3=None, column_3_row_4=None, column_4_row_1=None, column_4_row_2=None, column_4_row_3=None, column_4_row_4=None):
        """ > Constructor <&Node Combine Matrix>

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
        node = Node('Combine Matrix', sockets={'Column 1 Row 1': column_1_row_1, 'Column 1 Row 2': column_1_row_2, 'Column 1 Row 3': column_1_row_3, 'Column 1 Row 4': column_1_row_4, 'Column 2 Row 1': column_2_row_1, 'Column 2 Row 2': column_2_row_2, 'Column 2 Row 3': column_2_row_3, 'Column 2 Row 4': column_2_row_4, 'Column 3 Row 1': column_3_row_1, 'Column 3 Row 2': column_3_row_2, 'Column 3 Row 3': column_3_row_3, 'Column 3 Row 4': column_3_row_4, 'Column 4 Row 1': column_4_row_1, 'Column 4 Row 2': column_4_row_2, 'Column 4 Row 3': column_4_row_3, 'Column 4 Row 4': column_4_row_4})
        return cls(node._out)

    @classmethod
    def CombineTransform(cls, translation=None, rotation=None, scale=None):
        """ > Constructor <&Node Combine Transform>

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Matrix
        """
        node = Node('Combine Transform', sockets={'Translation': translation, 'Rotation': rotation, 'Scale': scale})
        return cls(node._out)

    def hash_value(self, seed=None):
        """ > Method <&Node Hash Value>

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
        node = Node('Hash Value', sockets={'Value': self, 'Seed': seed}, data_type='MATRIX')
        return node._out

    def invert(self):
        """ > Method <&Node Invert Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - Matrix [invertible_ (Boolean)]
        """
        node = Node('Invert Matrix', sockets={'Matrix': self})
        return node._out

    @property
    def determinant(self):
        """ > Property Get <&Node Matrix Determinant>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - Float
        """
        node = Node('Matrix Determinant', sockets={'Matrix': self})
        return node._out

    def multiply(self, matrix=None):
        """ > Method <&Node Multiply Matrices>

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
        node = Node('Multiply Matrices', sockets={'Matrix': self, 'Matrix_001': matrix})
        return node._out

    def project_point(self, vector=None):
        """ > Method <&Node Project Point>

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
        node = Node('Project Point', sockets={'Vector': vector, 'Transform': self})
        return node._out

    @property
    def separate(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - tuple (Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float)
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return (node.column_1_row_1, node.column_1_row_2, node.column_1_row_3, node.column_1_row_4, node.column_2_row_1, node.column_2_row_2, node.column_2_row_3, node.column_2_row_4, node.column_3_row_1, node.column_3_row_2, node.column_3_row_3, node.column_3_row_4, node.column_4_row_1, node.column_4_row_2, node.column_4_row_3, node.column_4_row_4)

    @property
    def separate_matrix(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - node [column_1_row_1 (Float), column_1_row_2 (Float), column_1_row_3 (Float), column_1_row_4 (Float), column_2_row_1 (Float), column_2_row_2 (Float), column_2_row_3 (Float), column_2_row_4 (Float), column_3_row_1 (Float), column_3_row_2 (Float), column_3_row_3 (Float), column_3_row_4 (Float), column_4_row_1 (Float), column_4_row_2 (Float), column_4_row_3 (Float), column_4_row_4 (Float)]
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node

    @property
    def column_1_row_1(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_1
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_1_row_1

    @property
    def column_1_row_2(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_2
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_1_row_2

    @property
    def column_1_row_3(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_3
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_1_row_3

    @property
    def column_1_row_4(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_1_row_4
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_1_row_4

    @property
    def column_2_row_1(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_1
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_2_row_1

    @property
    def column_2_row_2(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_2
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_2_row_2

    @property
    def column_2_row_3(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_3
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_2_row_3

    @property
    def column_2_row_4(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_2_row_4
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_2_row_4

    @property
    def column_3_row_1(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_1
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_3_row_1

    @property
    def column_3_row_2(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_2
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_3_row_2

    @property
    def column_3_row_3(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_3
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_3_row_3

    @property
    def column_3_row_4(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_3_row_4
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_3_row_4

    @property
    def column_4_row_1(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_1
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_4_row_1

    @property
    def column_4_row_2(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_2
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_4_row_2

    @property
    def column_4_row_3(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_3
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_4_row_3

    @property
    def column_4_row_4(self):
        """ > Property Get <&Node Separate Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - column_4_row_4
        """
        node = self._cache('Separate Matrix', sockets={'Matrix': self})
        return node.column_4_row_4

    @property
    def trs(self):
        """ > Property Get <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - tuple (Vector, Rotation, Vector)
        """
        node = Node('Separate Transform', sockets={'Transform': self})
        return (node.translation, node.rotation, node.scale)

    @property
    def separate_transform(self):
        """ > Property Get <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - node [translation (Vector), rotation (Rotation), scale (Vector)]
        """
        node = self._cache('Separate Transform', sockets={'Transform': self})
        return node

    @property
    def translation(self):
        """ > Property Get <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - translation
        """
        node = self._cache('Separate Transform', sockets={'Transform': self})
        return node.translation

    @property
    def rotation(self):
        """ > Property Get <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - rotation
        """
        node = self._cache('Separate Transform', sockets={'Transform': self})
        return node.rotation

    @property
    def scale(self):
        """ > Property Get <&Node Separate Transform>

        Information
        -----------
        - Socket 'Transform' : self

        Returns
        -------
        - scale
        """
        node = self._cache('Separate Transform', sockets={'Transform': self})
        return node.scale

    def transform_direction(self, direction=None):
        """ > Method <&Node Transform Direction>

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
        node = Node('Transform Direction', sockets={'Direction': direction, 'Transform': self})
        return node._out

    def transform_point(self, vector=None):
        """ > Method <&Node Transform Point>

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
        node = Node('Transform Point', sockets={'Vector': vector, 'Transform': self})
        return node._out

    @property
    def transpose(self):
        """ > Property Get <&Node Transpose Matrix>

        Information
        -----------
        - Socket 'Matrix' : self

        Returns
        -------
        - Matrix
        """
        node = Node('Transpose Matrix', sockets={'Matrix': self})
        return node._out

    def transform_gizmo(self, *value, position=None, rotation=None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True):
        """ > Method <&Node Transform Gizmo>

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
        node = Node('Transform Gizmo', sockets={'Value': [self] + list(value), 'Position': position, 'Rotation': rotation}, use_rotation_x=use_rotation_x, use_rotation_y=use_rotation_y, use_rotation_z=use_rotation_z, use_scale_x=use_scale_x, use_scale_y=use_scale_y, use_scale_z=use_scale_z, use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)
        return node._out

    @classmethod
    def Named(cls, name=None):
        """ > Constructor <&Node Named Attribute>

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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='FLOAT4X4')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name=None):
        """ > Constructor <&Node Named Attribute>

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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='FLOAT4X4')
        return cls(node._out)

