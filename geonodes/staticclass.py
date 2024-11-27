#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : staticclass
--------------------
- Functional nodes

Functional nodes are nodes which can't be considered as methods or properties of a data class.
Functional nodes also include input nodes such as 'Position' or 'Index'. Theses nodes should be considered
as properties of geometry but to ease the scripting, there are also implemented as functions.

Functional nodes are implemented as static functions and properties or a class named nd which is short.

```  python
# Some functional nodes
pos = nd.position
i = nd.index
attr = named_attribute(name, 'FLOAT')
```

classes
-------
- nd

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import numpy as np

import bpy
from .treeclass import Node

# =============================================================================================================================
# Static class

class nd:
    """ > All nodes

    $ DOC no_init

    This class exposes all possible Geometry Nodes under their **snake_case** name.

    ``` python
    # Node 'Set Position'
    nd.set_position()
    ```

    ### Returned values

    - When the node has only one output socket, this socket is returned.
    - When the node has several output sockets, the node is returned.
    - Output sockets can be read using their **snake_case** name:

    ``` python
    # 'Set Position' node has  only one output socket
    geometry = nd.set_position()

    # 'Rotation to Axis Angle' node has two output sockets
    node = nd.rotation_to_axis_angle()
    axis = node.axis
    angle = node.angle
    ```

    ### Methods arguments

    Methods arguments are:
    - the snake case name of the node sockets
    - the node parameters

    ``` python
    node = nd.set_position(geometry=None, selection=None, position=None, offset=None)

    # 'Math' node has two parameters : operation and use_clamp
    sum = nd.math(value=1, value_1=1, operation='ADD', use_clamp=False)
    ```

    ### Properties

    Nodes with no output socket are implemented as properties:

    ``` python
    # Node 'Index'
    index = nd.index

    # Node 'Special Characters'
    node = nd.special_characters
    line_break = node.line_break
    tab = node.tab
    ```
    """

    @classmethod
    def align_euler_to_vector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ > Node <&Node Align Euler to Vector>

        Arguments
        ---------
        - rotation (Vector) : socket 'Rotation' (Rotation)
        - factor (Float) : socket 'Factor' (Factor)
        - vector (Vector) : socket 'Vector' (Vector)
        - axis (str): Node.axis in ('X', 'Y', 'Z')
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Vector
        """

        node = Node('Align Euler to Vector', {'Rotation': rotation, 'Factor': factor, 'Vector': vector}, axis=axis, pivot_axis=pivot_axis)
        return node._out


    @classmethod
    def align_rotation_to_vector(cls, rotation=None, factor=None, vector=None, axis='Z', pivot_axis='AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - factor (Float) : socket 'Factor' (Factor)
        - vector (Vector) : socket 'Vector' (Vector)
        - axis (str): Node.axis in ('X', 'Y', 'Z')
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """

        node = Node('Align Rotation to Vector', {'Rotation': rotation, 'Factor': factor, 'Vector': vector}, axis=axis, pivot_axis=pivot_axis)
        return node._out


    @classmethod
    def axes_to_rotation(cls, primary_axis_1=None, secondary_axis_1=None, primary_axis='Z', secondary_axis='X'):
        """ > Node <&Node Axes to Rotation>

        Arguments
        ---------
        - primary_axis_1 (Vector) : socket 'Primary Axis' (Primary Axis)
        - secondary_axis_1 (Vector) : socket 'Secondary Axis' (Secondary Axis)
        - primary_axis (str): Node.primary_axis in ('X', 'Y', 'Z')
        - secondary_axis (str): Node.secondary_axis in ('X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """

        node = Node('Axes to Rotation', {'Primary Axis': primary_axis_1, 'Secondary Axis': secondary_axis_1}, primary_axis=primary_axis, secondary_axis=secondary_axis)
        return node._out


    @classmethod
    def axis_angle_to_rotation(cls, axis=None, angle=None):
        """ > Node <&Node Axis Angle to Rotation>

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (Axis)
        - angle (Float) : socket 'Angle' (Angle)

        Returns
        -------
        - Rotation
        """

        node = Node('Axis Angle to Rotation', {'Axis': axis, 'Angle': angle})
        return node._out


    @classmethod
    def boolean_math(cls, boolean=None, boolean_1=None, operation='AND'):
        """ > Node <&Node Boolean Math>

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (Boolean)
        - boolean_1 (Boolean) : socket 'Boolean' (Boolean_001)
        - operation (str): Node.operation in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

        Returns
        -------
        - Boolean
        """

        node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation=operation)
        return node._out


    @classmethod
    def combine_color(cls, red=None, green=None, blue=None, alpha=None, mode='RGB'):
        """ > Node <&Node Combine Color>

        Arguments
        ---------
        - red (Float) : socket 'Red' (Red)
        - green (Float) : socket 'Green' (Green)
        - blue (Float) : socket 'Blue' (Blue)
        - alpha (Float) : socket 'Alpha' (Alpha)
        - mode (str): Node.mode in ('RGB', 'HSV', 'HSL')

        Returns
        -------
        - Color
        """

        node = Node('Combine Color', {'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode=mode)
        return node._out


    @classmethod
    def combine_matrix(cls, column_1_row_1=None, column_1_row_2=None, column_1_row_3=None, column_1_row_4=None, column_2_row_1=None, column_2_row_2=None, column_2_row_3=None, column_2_row_4=None, column_3_row_1=None, column_3_row_2=None, column_3_row_3=None, column_3_row_4=None, column_4_row_1=None, column_4_row_2=None, column_4_row_3=None, column_4_row_4=None):
        """ > Node <&Node Combine Matrix>

        Arguments
        ---------
        - column_1_row_1 (Float) : socket 'Column 1 Row 1' (Column 1 Row 1)
        - column_1_row_2 (Float) : socket 'Column 1 Row 2' (Column 1 Row 2)
        - column_1_row_3 (Float) : socket 'Column 1 Row 3' (Column 1 Row 3)
        - column_1_row_4 (Float) : socket 'Column 1 Row 4' (Column 1 Row 4)
        - column_2_row_1 (Float) : socket 'Column 2 Row 1' (Column 2 Row 1)
        - column_2_row_2 (Float) : socket 'Column 2 Row 2' (Column 2 Row 2)
        - column_2_row_3 (Float) : socket 'Column 2 Row 3' (Column 2 Row 3)
        - column_2_row_4 (Float) : socket 'Column 2 Row 4' (Column 2 Row 4)
        - column_3_row_1 (Float) : socket 'Column 3 Row 1' (Column 3 Row 1)
        - column_3_row_2 (Float) : socket 'Column 3 Row 2' (Column 3 Row 2)
        - column_3_row_3 (Float) : socket 'Column 3 Row 3' (Column 3 Row 3)
        - column_3_row_4 (Float) : socket 'Column 3 Row 4' (Column 3 Row 4)
        - column_4_row_1 (Float) : socket 'Column 4 Row 1' (Column 4 Row 1)
        - column_4_row_2 (Float) : socket 'Column 4 Row 2' (Column 4 Row 2)
        - column_4_row_3 (Float) : socket 'Column 4 Row 3' (Column 4 Row 3)
        - column_4_row_4 (Float) : socket 'Column 4 Row 4' (Column 4 Row 4)

        Returns
        -------
        - Matrix
        """

        node = Node('Combine Matrix', {'Column 1 Row 1': column_1_row_1, 'Column 1 Row 2': column_1_row_2, 'Column 1 Row 3': column_1_row_3, 'Column 1 Row 4': column_1_row_4, 'Column 2 Row 1': column_2_row_1, 'Column 2 Row 2': column_2_row_2, 'Column 2 Row 3': column_2_row_3, 'Column 2 Row 4': column_2_row_4, 'Column 3 Row 1': column_3_row_1, 'Column 3 Row 2': column_3_row_2, 'Column 3 Row 3': column_3_row_3, 'Column 3 Row 4': column_3_row_4, 'Column 4 Row 1': column_4_row_1, 'Column 4 Row 2': column_4_row_2, 'Column 4 Row 3': column_4_row_3, 'Column 4 Row 4': column_4_row_4})
        return node._out


    @classmethod
    def combine_transform(cls, translation=None, rotation=None, scale=None):
        """ > Node <&Node Combine Transform>

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)

        Returns
        -------
        - Matrix
        """

        node = Node('Combine Transform', {'Translation': translation, 'Rotation': rotation, 'Scale': scale})
        return node._out


    @classmethod
    def compare(cls, a=None, b=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):
        """ > Node <&Node Compare>

        Arguments
        ---------
        - a (Float) : socket 'A' (A)
        - b (Float) : socket 'B' (B)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
        - mode (str): Node.mode in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
        - operation (str): Node.operation in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')

        Returns
        -------
        - Boolean
        """

        node = Node('Compare', {'A': a, 'B': b}, data_type=data_type, mode=mode, operation=operation)
        return node._out


    @classmethod
    def euler_to_rotation(cls, euler=None):
        """ > Node <&Node Euler to Rotation>

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (Euler)

        Returns
        -------
        - Rotation
        """

        node = Node('Euler to Rotation', {'Euler': euler})
        return node._out


    @classmethod
    def float_to_integer(cls, float=None, rounding_mode='ROUND'):
        """ > Node <&Node Float to Integer>

        Arguments
        ---------
        - float (Float) : socket 'Float' (Float)
        - rounding_mode (str): Node.rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

        Returns
        -------
        - Integer
        """

        node = Node('Float to Integer', {'Float': float}, rounding_mode=rounding_mode)
        return node._out


    @classmethod
    def boolean(cls, boolean=False):
        """ > Node <&Node Boolean>

        Arguments
        ---------
        - boolean (bool): Node.boolean

        Returns
        -------
        - Boolean
        """

        node = Node('Boolean', boolean=boolean)
        return node._out


    @classmethod
    def color(cls, value=None):
        """ > Node <&Node Color>

        Arguments
        ---------
        - value (bpy_prop_array): Node.value

        Returns
        -------
        - Color
        """

        node = Node('Color', value=value)
        return node._out


    @classmethod
    def integer(cls, integer=0):
        """ > Node <&Node Integer>

        Arguments
        ---------
        - integer (int): Node.integer

        Returns
        -------
        - Integer
        """

        node = Node('Integer', integer=integer)
        return node._out


    @classmethod
    def rotation(cls, rotation_euler=None):
        """ > Node <&Node Rotation>

        Arguments
        ---------
        - rotation_euler (Euler): Node.rotation_euler

        Returns
        -------
        - Rotation
        """

        node = Node('Rotation', rotation_euler=rotation_euler)
        return node._out


    @classmethod
    @property
    def special_characters(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        - Node
        """

        node = Node('Special Characters')
        return node


    @classmethod
    def string(cls, string=''):
        """ > Node <&Node String>

        Arguments
        ---------
        - string (str): Node.string

        Returns
        -------
        - String
        """

        node = Node('String', string=string)
        return node._out


    @classmethod
    def vector(cls, vector=None):
        """ > Node <&Node Vector>

        Arguments
        ---------
        - vector (Vector): Node.vector

        Returns
        -------
        - Vector
        """

        node = Node('Vector', vector=vector)
        return node._out


    @classmethod
    def invert_matrix(cls, matrix=None):
        """ > Node <&Node Invert Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (Matrix)

        Returns
        -------
        - Node
        """

        node = Node('Invert Matrix', {'Matrix': matrix})
        return node


    @classmethod
    def invert_rotation(cls, rotation=None):
        """ > Node <&Node Invert Rotation>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Rotation
        """

        node = Node('Invert Rotation', {'Rotation': rotation})
        return node._out


    @classmethod
    def multiply_matrices(cls, matrix=None, matrix_1=None):
        """ > Node <&Node Multiply Matrices>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (Matrix)
        - matrix_1 (Matrix) : socket 'Matrix' (Matrix_001)

        Returns
        -------
        - Matrix
        """

        node = Node('Multiply Matrices', {'Matrix': matrix, 'Matrix_001': matrix_1})
        return node._out


    @classmethod
    def project_point(cls, vector=None, transform=None):
        """ > Node <&Node Project Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - transform (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - Vector
        """

        node = Node('Project Point', {'Vector': vector, 'Transform': transform})
        return node._out


    @classmethod
    def quaternion_to_rotation(cls, w=None, x=None, y=None, z=None):
        """ > Node <&Node Quaternion to Rotation>

        Arguments
        ---------
        - w (Float) : socket 'W' (W)
        - x (Float) : socket 'X' (X)
        - y (Float) : socket 'Y' (Y)
        - z (Float) : socket 'Z' (Z)

        Returns
        -------
        - Rotation
        """

        node = Node('Quaternion to Rotation', {'W': w, 'X': x, 'Y': y, 'Z': z})
        return node._out


    @classmethod
    def random_value(cls, min=None, max=None, id=None, seed=None, data_type='FLOAT'):
        """ > Node <&Node Random Value>

        Arguments
        ---------
        - min (Float) : socket 'Min' (Min_001)
        - max (Float) : socket 'Max' (Max_001)
        - id (Integer) : socket 'ID' (ID)
        - seed (Integer) : socket 'Seed' (Seed)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

        Returns
        -------
        - Node
        """

        node = Node('Random Value', {'Min_001': min, 'Max_001': max, 'ID': id, 'Seed': seed}, data_type=data_type)
        return node


    @classmethod
    def replace_string(cls, string=None, find=None, replace=None):
        """ > Node <&Node Replace String>

        Arguments
        ---------
        - string (String) : socket 'String' (String)
        - find (String) : socket 'Find' (Find)
        - replace (String) : socket 'Replace' (Replace)

        Returns
        -------
        - String
        """

        node = Node('Replace String', {'String': string, 'Find': find, 'Replace': replace})
        return node._out


    @classmethod
    def rotate_euler(cls, rotation=None, rotate_by=None, rotation_type='EULER', space='OBJECT'):
        """ > Node <&Node Rotate Euler>

        Arguments
        ---------
        - rotation (Vector) : socket 'Rotation' (Rotation)
        - rotate_by (Vector) : socket 'Rotate By' (Rotate By)
        - rotation_type (str): Node.rotation_type in ('AXIS_ANGLE', 'EULER')
        - space (str): Node.space in ('OBJECT', 'LOCAL')

        Returns
        -------
        - Vector
        """

        node = Node('Rotate Euler', {'Rotation': rotation, 'Rotate By': rotate_by}, rotation_type=rotation_type, space=space)
        return node._out


    @classmethod
    def rotate_rotation(cls, rotation=None, rotate_by=None, rotation_space='GLOBAL'):
        """ > Node <&Node Rotate Rotation>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - rotate_by (Rotation) : socket 'Rotate By' (Rotate By)
        - rotation_space (str): Node.rotation_space in ('GLOBAL', 'LOCAL')

        Returns
        -------
        - Rotation
        """

        node = Node('Rotate Rotation', {'Rotation': rotation, 'Rotate By': rotate_by}, rotation_space=rotation_space)
        return node._out


    @classmethod
    def rotate_vector(cls, vector=None, rotation=None):
        """ > Node <&Node Rotate Vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Vector
        """

        node = Node('Rotate Vector', {'Vector': vector, 'Rotation': rotation})
        return node._out


    @classmethod
    def rotation_to_axis_angle(cls, rotation=None):
        """ > Node <&Node Rotation to Axis Angle>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Node
        """

        node = Node('Rotation to Axis Angle', {'Rotation': rotation})
        return node


    @classmethod
    def rotation_to_euler(cls, rotation=None):
        """ > Node <&Node Rotation to Euler>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Vector
        """

        node = Node('Rotation to Euler', {'Rotation': rotation})
        return node._out


    @classmethod
    def rotation_to_quaternion(cls, rotation=None):
        """ > Node <&Node Rotation to Quaternion>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Node
        """

        node = Node('Rotation to Quaternion', {'Rotation': rotation})
        return node


    @classmethod
    def separate_color(cls, color=None, mode='RGB'):
        """ > Node <&Node Separate Color>

        Arguments
        ---------
        - color (Color) : socket 'Color' (Color)
        - mode (str): Node.mode in ('RGB', 'HSV', 'HSL')

        Returns
        -------
        - Node
        """

        node = Node('Separate Color', {'Color': color}, mode=mode)
        return node


    @classmethod
    def separate_matrix(cls, matrix=None):
        """ > Node <&Node Separate Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (Matrix)

        Returns
        -------
        - Node
        """

        node = Node('Separate Matrix', {'Matrix': matrix})
        return node


    @classmethod
    def separate_transform(cls, transform=None):
        """ > Node <&Node Separate Transform>

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - Node
        """

        node = Node('Separate Transform', {'Transform': transform})
        return node


    @classmethod
    def slice_string(cls, string=None, position=None, length=None):
        """ > Node <&Node Slice String>

        Arguments
        ---------
        - string (String) : socket 'String' (String)
        - position (Integer) : socket 'Position' (Position)
        - length (Integer) : socket 'Length' (Length)

        Returns
        -------
        - String
        """

        node = Node('Slice String', {'String': string, 'Position': position, 'Length': length})
        return node._out


    @classmethod
    def string_length(cls, string=None):
        """ > Node <&Node String Length>

        Arguments
        ---------
        - string (String) : socket 'String' (String)

        Returns
        -------
        - Integer
        """

        node = Node('String Length', {'String': string})
        return node._out


    @classmethod
    def transform_direction(cls, direction=None, transform=None):
        """ > Node <&Node Transform Direction>

        Arguments
        ---------
        - direction (Vector) : socket 'Direction' (Direction)
        - transform (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - Vector
        """

        node = Node('Transform Direction', {'Direction': direction, 'Transform': transform})
        return node._out


    @classmethod
    def transform_point(cls, vector=None, transform=None):
        """ > Node <&Node Transform Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - transform (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - Vector
        """

        node = Node('Transform Point', {'Vector': vector, 'Transform': transform})
        return node._out


    @classmethod
    def transpose_matrix(cls, matrix=None):
        """ > Node <&Node Transpose Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (Matrix)

        Returns
        -------
        - Matrix
        """

        node = Node('Transpose Matrix', {'Matrix': matrix})
        return node._out


    @classmethod
    def value_to_string(cls, value=None, decimals=None):
        """ > Node <&Node Value to String>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - decimals (Integer) : socket 'Decimals' (Decimals)

        Returns
        -------
        - String
        """

        node = Node('Value to String', {'Value': value, 'Decimals': decimals})
        return node._out


    @classmethod
    def accumulate_field(cls, value=None, group_id=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Accumulate Field>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - group_id (Integer) : socket 'Group ID' (Group Index)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Node
        """

        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node


    @classmethod
    def domain_size(cls, geometry=None, component='MESH'):
        """ > Node <&Node Domain Size>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - component (str): Node.component in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')

        Returns
        -------
        - Node
        """

        node = Node('Domain Size', {'Geometry': geometry}, component=component)
        return node


    @classmethod
    def attribute_statistic(cls, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Attribute Statistic>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - attribute (Float) : socket 'Attribute' (Attribute)
        - data_type (str): Node.data_type in ('FLOAT', 'FLOAT_VECTOR')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Node
        """

        node = Node('Attribute Statistic', {'Geometry': geometry, 'Selection': selection, 'Attribute': attribute}, data_type=data_type, domain=domain)
        return node


    @classmethod
    def bake(cls, geometry=None, active_index=0, active_item=None, bake_items=None):
        """ > Node <&Node Bake>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Item_0)
        - active_index (int): Node.active_index
        - active_item (NodeGeometryBakeItem): Node.active_item
        - bake_items (bpy_prop_collection): Node.bake_items

        Returns
        -------
        - Node
        """

        node = Node('Bake', {'Item_0': geometry}, active_index=active_index, active_item=active_item, bake_items=bake_items)
        return node


    @classmethod
    def blur_attribute(cls, value=None, iterations=None, weight=None, data_type='FLOAT'):
        """ > Node <&Node Blur Attribute>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - iterations (Integer) : socket 'Iterations' (Iterations)
        - weight (Float) : socket 'Weight' (Weight)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR')

        Returns
        -------
        - Float
        """

        node = Node('Blur Attribute', {'Value': value, 'Iterations': iterations, 'Weight': weight}, data_type=data_type)
        return node._out


    @classmethod
    def bounding_box(cls, geometry=None):
        """ > Node <&Node Bounding Box>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Node
        """

        node = Node('Bounding Box', {'Geometry': geometry})
        return node


    @classmethod
    def capture_attribute(cls, geometry=None, active_index=0, active_item=None, capture_items=None, domain='POINT'):
        """ > Node <&Node Capture Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - active_index (int): Node.active_index
        - active_item (NoneType): Node.active_item
        - capture_items (bpy_prop_collection): Node.capture_items
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Node
        """

        node = Node('Capture Attribute', {'Geometry': geometry}, active_index=active_index, active_item=active_item, capture_items=capture_items, domain=domain)
        return node


    @classmethod
    def collection_info(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ > Node <&Node Collection Info>

        Arguments
        ---------
        - collection (Collection) : socket 'Collection' (Collection)
        - separate_children (Boolean) : socket 'Separate Children' (Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (Reset Children)
        - transform_space (str): Node.transform_space in ('ORIGINAL', 'RELATIVE')

        Returns
        -------
        - Geometry
        """

        node = Node('Collection Info', {'Collection': collection, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out


    @classmethod
    def convex_hull(cls, geometry=None):
        """ > Node <&Node Convex Hull>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Geometry
        """

        node = Node('Convex Hull', {'Geometry': geometry})
        return node._out


    @classmethod
    def corners_of_edge(cls, edge_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (Edge Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Node
        """

        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node


    @classmethod
    def corners_of_face(cls, face_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Face>

        Arguments
        ---------
        - face_index (Integer) : socket 'Face Index' (Face Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Node
        """

        node = Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node


    @classmethod
    def corners_of_vertex(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (Vertex Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Node
        """

        node = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node


    @classmethod
    def arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, mode='RADIUS'):
        """ > Node <&Node Arc>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - radius (Float) : socket 'Radius' (Radius)
        - start_angle (Float) : socket 'Start Angle' (Start Angle)
        - sweep_angle (Float) : socket 'Sweep Angle' (Sweep Angle)
        - connect_center (Boolean) : socket 'Connect Center' (Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (Invert Arc)
        - mode (str): Node.mode in ('POINTS', 'RADIUS')

        Returns
        -------
        - Node
        """

        node = Node('Arc', {'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode=mode)
        return node


    @classmethod
    def endpoint_selection(cls, start_size=None, end_size=None):
        """ > Node <&Node Endpoint Selection>

        Arguments
        ---------
        - start_size (Integer) : socket 'Start Size' (Start Size)
        - end_size (Integer) : socket 'End Size' (End Size)

        Returns
        -------
        - Boolean
        """

        node = Node('Endpoint Selection', {'Start Size': start_size, 'End Size': end_size})
        return node._out


    @classmethod
    def handle_type_selection(cls, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ > Node <&Node Handle Type Selection>

        Arguments
        ---------
        - handle_type (str): Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        - mode (set): Node.mode

        Returns
        -------
        - Boolean
        """

        node = Node('Handle Type Selection', handle_type=handle_type, mode=mode)
        return node._out


    @classmethod
    def curve_length(cls, curve=None):
        """ > Node <&Node Curve Length>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)

        Returns
        -------
        - Float
        """

        node = Node('Curve Length', {'Curve': curve})
        return node._out


    @classmethod
    def curve_of_point(cls, point_index=None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (Point Index)

        Returns
        -------
        - Node
        """

        node = Node('Curve of Point', {'Point Index': point_index})
        return node


    @classmethod
    def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ > Node <&Node Bézier Segment>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - start (Vector) : socket 'Start' (Start)
        - start_handle (Vector) : socket 'Start Handle' (Start Handle)
        - end_handle (Vector) : socket 'End Handle' (End Handle)
        - end (Vector) : socket 'End' (End)
        - mode (str): Node.mode in ('POSITION', 'OFFSET')

        Returns
        -------
        - Geometry
        """

        node = Node('Bézier Segment', {'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode=mode)
        return node._out


    @classmethod
    def curve_circle(cls, resolution=None, radius=None, mode='RADIUS'):
        """ > Node <&Node Curve Circle>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - radius (Float) : socket 'Radius' (Radius)
        - mode (str): Node.mode in ('POINTS', 'RADIUS')

        Returns
        -------
        - Node
        """

        node = Node('Curve Circle', {'Resolution': resolution, 'Radius': radius}, mode=mode)
        return node


    @classmethod
    def curve_line(cls, start=None, end=None, mode='POINTS'):
        """ > Node <&Node Curve Line>

        Arguments
        ---------
        - start (Vector) : socket 'Start' (Start)
        - end (Vector) : socket 'End' (End)
        - mode (str): Node.mode in ('POINTS', 'DIRECTION')

        Returns
        -------
        - Geometry
        """

        node = Node('Curve Line', {'Start': start, 'End': end}, mode=mode)
        return node._out


    @classmethod
    def quadrilateral(cls, width=None, height=None, mode='RECTANGLE'):
        """ > Node <&Node Quadrilateral>

        Arguments
        ---------
        - width (Float) : socket 'Width' (Width)
        - height (Float) : socket 'Height' (Height)
        - mode (str): Node.mode in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

        Returns
        -------
        - Geometry
        """

        node = Node('Quadrilateral', {'Width': width, 'Height': height}, mode=mode)
        return node._out


    @classmethod
    def quadratic_bezier(cls, resolution=None, start=None, middle=None, end=None):
        """ > Node <&Node Quadratic Bézier>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - start (Vector) : socket 'Start' (Start)
        - middle (Vector) : socket 'Middle' (Middle)
        - end (Vector) : socket 'End' (End)

        Returns
        -------
        - Geometry
        """

        node = Node('Quadratic Bézier', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end})
        return node._out


    @classmethod
    def set_handle_type(cls, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ > Node <&Node Set Handle Type>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - handle_type (str): Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        - mode (set): Node.mode

        Returns
        -------
        - Geometry
        """

        node = Node('Set Handle Type', {'Curve': curve, 'Selection': selection}, handle_type=handle_type, mode=mode)
        return node._out


    @classmethod
    def spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ > Node <&Node Spiral>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - rotations (Float) : socket 'Rotations' (Rotations)
        - start_radius (Float) : socket 'Start Radius' (Start Radius)
        - end_radius (Float) : socket 'End Radius' (End Radius)
        - height (Float) : socket 'Height' (Height)
        - reverse (Boolean) : socket 'Reverse' (Reverse)

        Returns
        -------
        - Geometry
        """

        node = Node('Spiral', {'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius, 'End Radius': end_radius, 'Height': height, 'Reverse': reverse})
        return node._out


    @classmethod
    def set_spline_type(cls, curve=None, selection=None, spline_type='POLY'):
        """ > Node <&Node Set Spline Type>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - spline_type (str): Node.spline_type in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

        Returns
        -------
        - Geometry
        """

        node = Node('Set Spline Type', {'Curve': curve, 'Selection': selection}, spline_type=spline_type)
        return node._out


    @classmethod
    def star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ > Node <&Node Star>

        Arguments
        ---------
        - points (Integer) : socket 'Points' (Points)
        - inner_radius (Float) : socket 'Inner Radius' (Inner Radius)
        - outer_radius (Float) : socket 'Outer Radius' (Outer Radius)
        - twist (Float) : socket 'Twist' (Twist)

        Returns
        -------
        - Node
        """

        node = Node('Star', {'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})
        return node


    @classmethod
    def curve_to_mesh(cls, curve=None, profile_curve=None, fill_caps=None):
        """ > Node <&Node Curve to Mesh>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - profile_curve (Geometry) : socket 'Profile Curve' (Profile Curve)
        - fill_caps (Boolean) : socket 'Fill Caps' (Fill Caps)

        Returns
        -------
        - Geometry
        """

        node = Node('Curve to Mesh', {'Curve': curve, 'Profile Curve': profile_curve, 'Fill Caps': fill_caps})
        return node._out


    @classmethod
    def curve_to_points(cls, curve=None, count=None, mode='COUNT'):
        """ > Node <&Node Curve to Points>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - count (Integer) : socket 'Count' (Count)
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Node
        """

        node = Node('Curve to Points', {'Curve': curve, 'Count': count}, mode=mode)
        return node


    @classmethod
    def deform_curves_on_surface(cls, curves=None):
        """ > Node <&Node Deform Curves on Surface>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (Curves)

        Returns
        -------
        - Geometry
        """

        node = Node('Deform Curves on Surface', {'Curves': curves})
        return node._out


    @classmethod
    def delete_geometry(cls, geometry=None, selection=None, domain='POINT', mode='ALL'):
        """ > Node <&Node Delete Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
        - mode (str): Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry
        """

        node = Node('Delete Geometry', {'Geometry': geometry, 'Selection': selection}, domain=domain, mode=mode)
        return node._out


    @classmethod
    def distribute_points_in_grid(cls, grid=None, density=None, seed=None, mode='DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (Grid)
        - density (Float) : socket 'Density' (Density)
        - seed (Integer) : socket 'Seed' (Seed)
        - mode (str): Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')

        Returns
        -------
        - Geometry
        """

        node = Node('Distribute Points in Grid', {'Grid': grid, 'Density': density, 'Seed': seed}, mode=mode)
        return node._out


    @classmethod
    def distribute_points_in_volume(cls, volume=None, density=None, seed=None, mode='DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Volume>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (Volume)
        - density (Float) : socket 'Density' (Density)
        - seed (Integer) : socket 'Seed' (Seed)
        - mode (str): Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')

        Returns
        -------
        - Geometry
        """

        node = Node('Distribute Points in Volume', {'Volume': volume, 'Density': density, 'Seed': seed}, mode=mode)
        return node._out


    @classmethod
    def distribute_points_on_faces(cls, mesh=None, selection=None, density=None, seed=None, distribute_method='RANDOM', use_legacy_normal=False):
        """ > Node <&Node Distribute Points on Faces>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)
        - density (Float) : socket 'Density' (Density)
        - seed (Integer) : socket 'Seed' (Seed)
        - distribute_method (str): Node.distribute_method in ('RANDOM', 'POISSON')
        - use_legacy_normal (bool): Node.use_legacy_normal

        Returns
        -------
        - Node
        """

        node = Node('Distribute Points on Faces', {'Mesh': mesh, 'Selection': selection, 'Density': density, 'Seed': seed}, distribute_method=distribute_method, use_legacy_normal=use_legacy_normal)
        return node


    @classmethod
    def dual_mesh(cls, mesh=None, keep_boundaries=None):
        """ > Node <&Node Dual Mesh>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - keep_boundaries (Boolean) : socket 'Keep Boundaries' (Keep Boundaries)

        Returns
        -------
        - Geometry
        """

        node = Node('Dual Mesh', {'Mesh': mesh, 'Keep Boundaries': keep_boundaries})
        return node._out


    @classmethod
    def duplicate_elements(cls, geometry=None, selection=None, amount=None, domain='POINT'):
        """ > Node <&Node Duplicate Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - amount (Integer) : socket 'Amount' (Amount)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

        Returns
        -------
        - Node
        """

        node = Node('Duplicate Elements', {'Geometry': geometry, 'Selection': selection, 'Amount': amount}, domain=domain)
        return node


    @classmethod
    def edge_paths_to_curves(cls, mesh=None, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Curves>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - start_vertices (Boolean) : socket 'Start Vertices' (Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (Next Vertex Index)

        Returns
        -------
        - Geometry
        """

        node = Node('Edge Paths to Curves', {'Mesh': mesh, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out


    @classmethod
    def edge_paths_to_selection(cls, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Selection>

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (Next Vertex Index)

        Returns
        -------
        - Boolean
        """

        node = Node('Edge Paths to Selection', {'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out


    @classmethod
    def edges_of_corner(cls, corner_index=None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Node
        """

        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node


    @classmethod
    def edges_of_vertex(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Node <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (Vertex Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Node
        """

        node = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node


    @classmethod
    def edges_to_face_groups(cls, boundary_edges=None):
        """ > Node <&Node Edges to Face Groups>

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (Boundary Edges)

        Returns
        -------
        - Integer
        """

        node = Node('Edges to Face Groups', {'Boundary Edges': boundary_edges})
        return node._out


    @classmethod
    def extrude_mesh(cls, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """ > Node <&Node Extrude Mesh>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)
        - offset (Vector) : socket 'Offset' (Offset)
        - offset_scale (Float) : socket 'Offset Scale' (Offset Scale)
        - individual (Boolean) : socket 'Individual' (Individual)
        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES')

        Returns
        -------
        - Node
        """

        node = Node('Extrude Mesh', {'Mesh': mesh, 'Selection': selection, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode=mode)
        return node


    @classmethod
    def face_of_corner(cls, corner_index=None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Node
        """

        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node


    @classmethod
    def evaluate_at_index(cls, index=None, value=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Evaluate at Index>

        Arguments
        ---------
        - index (Integer) : socket 'Index' (Index)
        - value (Float) : socket 'Value' (Value)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Float
        """

        node = Node('Evaluate at Index', {'Index': index, 'Value': value}, data_type=data_type, domain=domain)
        return node._out


    @classmethod
    def evaluate_on_domain(cls, value=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Evaluate on Domain>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Float
        """

        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain=domain)
        return node._out


    @classmethod
    def fill_curve(cls, curve=None, group_id=None, mode='TRIANGLES'):
        """ > Node <&Node Fill Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - mode (str): Node.mode in ('TRIANGLES', 'NGONS')

        Returns
        -------
        - Geometry
        """

        node = Node('Fill Curve', {'Curve': curve, 'Group ID': group_id}, mode=mode)
        return node._out


    @classmethod
    def fillet_curve(cls, curve=None, radius=None, limit_radius=None, mode='BEZIER'):
        """ > Node <&Node Fillet Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - radius (Float) : socket 'Radius' (Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (Limit Radius)
        - mode (str): Node.mode in ('BEZIER', 'POLY')

        Returns
        -------
        - Geometry
        """

        node = Node('Fillet Curve', {'Curve': curve, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)
        return node._out


    @classmethod
    def flip_faces(cls, mesh=None, selection=None):
        """ > Node <&Node Flip Faces>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)

        Returns
        -------
        - Geometry
        """

        node = Node('Flip Faces', {'Mesh': mesh, 'Selection': selection})
        return node._out


    @classmethod
    def geometry_to_instance(cls, geometry=None):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Geometry
        """

        node = Node('Geometry to Instance', {'Geometry': geometry})
        return node._out


    @classmethod
    def get_named_grid(cls, volume=None, name=None, remove=None, data_type='FLOAT'):
        """ > Node <&Node Get Named Grid>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (Volume)
        - name (String) : socket 'Name' (Name)
        - remove (Boolean) : socket 'Remove' (Remove)
        - data_type (str): Node.data_type in ('FLOAT', 'VECTOR')

        Returns
        -------
        - Node
        """

        node = Node('Get Named Grid', {'Volume': volume, 'Name': name, 'Remove': remove}, data_type=data_type)
        return node


    @classmethod
    def grid_to_mesh(cls, grid=None, threshold=None, adaptivity=None):
        """ > Node <&Node Grid to Mesh>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (Grid)
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)

        Returns
        -------
        - Geometry
        """

        node = Node('Grid to Mesh', {'Grid': grid, 'Threshold': threshold, 'Adaptivity': adaptivity})
        return node._out


    @classmethod
    def group(cls, node_tree=None):
        """ > Node <&Node Group>

        Arguments
        ---------
        - node_tree (NoneType): Node.node_tree
        """

        node = Node('Group', node_tree=node_tree)
        return node._out


    @classmethod
    def image_info(cls, image=None, frame=None):
        """ > Node <&Node Image Info>

        Arguments
        ---------
        - image (Image) : socket 'Image' (Image)
        - frame (Integer) : socket 'Frame' (Frame)

        Returns
        -------
        - Node
        """

        node = Node('Image Info', {'Image': image, 'Frame': frame})
        return node


    @classmethod
    def image_texture(cls, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """ > Node <&Node Image Texture>

        Arguments
        ---------
        - image (Image) : socket 'Image' (Image)
        - vector (Vector) : socket 'Vector' (Vector)
        - frame (Integer) : socket 'Frame' (Frame)
        - extension (str): Node.extension in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
        - interpolation (str): Node.interpolation in ('Linear', 'Closest', 'Cubic')

        Returns
        -------
        - Node
        """

        node = Node('Image Texture', {'Image': image, 'Vector': vector, 'Frame': frame}, extension=extension, interpolation=interpolation)
        return node


    @classmethod
    def index_of_nearest(cls, position=None, group_id=None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - group_id (Integer) : socket 'Group ID' (Group ID)

        Returns
        -------
        - Node
        """

        node = Node('Index of Nearest', {'Position': position, 'Group ID': group_id})
        return node


    @classmethod
    def index_switch(cls, index=None, _0=None, _1=None, data_type='GEOMETRY', index_switch_items=None):
        """ > Node <&Node Index Switch>

        Arguments
        ---------
        - index (Integer) : socket 'Index' (Index)
        - _0 (Geometry) : socket '0' (Item_0)
        - _1 (Geometry) : socket '1' (Item_1)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL')
        - index_switch_items (bpy_prop_collection): Node.index_switch_items

        Returns
        -------
        - Geometry
        """

        node = Node('Index Switch', {'Index': index, 'Item_0': _0, 'Item_1': _1}, data_type=data_type, index_switch_items=index_switch_items)
        return node._out


    @classmethod
    @property
    def active_camera(cls):
        """ > Node <&Node Active Camera>

        Returns
        -------
        - Object
        """

        node = Node('Active Camera')
        return node._out


    @classmethod
    def curve_handle_positions(cls, relative=None):
        """ > Node <&Node Curve Handle Positions>

        Arguments
        ---------
        - relative (Boolean) : socket 'Relative' (Relative)

        Returns
        -------
        - Node
        """

        node = Node('Curve Handle Positions', {'Relative': relative})
        return node


    @classmethod
    @property
    def curve_tilt(cls):
        """ > Node <&Node Curve Tilt>

        Returns
        -------
        - Float
        """

        node = Node('Curve Tilt')
        return node._out


    @classmethod
    @property
    def is_edge_smooth(cls):
        """ > Node <&Node Is Edge Smooth>

        Returns
        -------
        - Boolean
        """

        node = Node('Is Edge Smooth')
        return node._out


    @classmethod
    @property
    def id(cls):
        """ > Node <&Node ID>

        Returns
        -------
        - Integer
        """

        node = Node('ID')
        return node._out


    @classmethod
    def image(cls, image=None):
        """ > Node <&Node Image>

        Arguments
        ---------
        - image (NoneType): Node.image

        Returns
        -------
        - Image
        """

        node = Node('Image', image=image)
        return node._out


    @classmethod
    @property
    def index(cls):
        """ > Node <&Node Index>

        Returns
        -------
        - Integer
        """

        node = Node('Index')
        return node._out


    @classmethod
    @property
    def instance_rotation(cls):
        """ > Node <&Node Instance Rotation>

        Returns
        -------
        - Rotation
        """

        node = Node('Instance Rotation')
        return node._out


    @classmethod
    @property
    def instance_scale(cls):
        """ > Node <&Node Instance Scale>

        Returns
        -------
        - Vector
        """

        node = Node('Instance Scale')
        return node._out


    @classmethod
    def material(cls, material=None):
        """ > Node <&Node Material>

        Arguments
        ---------
        - material (NoneType): Node.material

        Returns
        -------
        - Material
        """

        node = Node('Material', material=material)
        return node._out


    @classmethod
    @property
    def material_index(cls):
        """ > Node <&Node Material Index>

        Returns
        -------
        - Integer
        """

        node = Node('Material Index')
        return node._out


    @classmethod
    @property
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - Node
        """

        node = Node('Edge Angle')
        return node


    @classmethod
    @property
    def edge_neighbors(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        - Integer
        """

        node = Node('Edge Neighbors')
        return node._out


    @classmethod
    @property
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - Node
        """

        node = Node('Edge Vertices')
        return node


    @classmethod
    @property
    def face_area(cls):
        """ > Node <&Node Face Area>

        Returns
        -------
        - Float
        """

        node = Node('Face Area')
        return node._out


    @classmethod
    def is_face_planar(cls, threshold=None):
        """ > Node <&Node Is Face Planar>

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (Threshold)

        Returns
        -------
        - Boolean
        """

        node = Node('Is Face Planar', {'Threshold': threshold})
        return node._out


    @classmethod
    @property
    def face_neighbors(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        - Node
        """

        node = Node('Face Neighbors')
        return node


    @classmethod
    @property
    def mesh_island(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        - Node
        """

        node = Node('Mesh Island')
        return node


    @classmethod
    @property
    def vertex_neighbors(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        - Node
        """

        node = Node('Vertex Neighbors')
        return node


    @classmethod
    def named_attribute(cls, name=None, data_type='FLOAT'):
        """ > Node <&Node Named Attribute>

        Arguments
        ---------
        - name (String) : socket 'Name' (Name)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Returns
        -------
        - Node
        """

        node = Node('Named Attribute', {'Name': name}, data_type=data_type)
        return node


    @classmethod
    def named_layer_selection(cls, name=None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (Name)

        Returns
        -------
        - Boolean
        """

        node = Node('Named Layer Selection', {'Name': name})
        return node._out


    @classmethod
    @property
    def normal(cls):
        """ > Node <&Node Normal>

        Returns
        -------
        - Vector
        """

        node = Node('Normal')
        return node._out


    @classmethod
    @property
    def position(cls):
        """ > Node <&Node Position>

        Returns
        -------
        - Vector
        """

        node = Node('Position')
        return node._out


    @classmethod
    @property
    def radius(cls):
        """ > Node <&Node Radius>

        Returns
        -------
        - Float
        """

        node = Node('Radius')
        return node._out


    @classmethod
    @property
    def scene_time(cls):
        """ > Node <&Node Scene Time>

        Returns
        -------
        - Node
        """

        node = Node('Scene Time')
        return node


    @classmethod
    @property
    def is_face_smooth(cls):
        """ > Node <&Node Is Face Smooth>

        Returns
        -------
        - Boolean
        """

        node = Node('Is Face Smooth')
        return node._out


    @classmethod
    def shortest_edge_paths(cls, end_vertex=None, edge_cost=None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (Edge Cost)

        Returns
        -------
        - Node
        """

        node = Node('Shortest Edge Paths', {'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node


    @classmethod
    @property
    def is_spline_cyclic(cls):
        """ > Node <&Node Is Spline Cyclic>

        Returns
        -------
        - Boolean
        """

        node = Node('Is Spline Cyclic')
        return node._out


    @classmethod
    @property
    def spline_resolution(cls):
        """ > Node <&Node Spline Resolution>

        Returns
        -------
        - Integer
        """

        node = Node('Spline Resolution')
        return node._out


    @classmethod
    @property
    def curve_tangent(cls):
        """ > Node <&Node Curve Tangent>

        Returns
        -------
        - Vector
        """

        node = Node('Curve Tangent')
        return node._out


    @classmethod
    def instance_on_points(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Node <&Node Instance on Points>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - selection (Boolean) : socket 'Selection' (Selection)
        - instance (Geometry) : socket 'Instance' (Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (Instance Index)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)

        Returns
        -------
        - Geometry
        """

        node = Node('Instance on Points', {'Points': points, 'Selection': selection, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out


    @classmethod
    @property
    def instance_transform(cls):
        """ > Node <&Node Instance Transform>

        Returns
        -------
        - Matrix
        """

        node = Node('Instance Transform')
        return node._out


    @classmethod
    def instances_to_points(cls, instances=None, selection=None, position=None, radius=None):
        """ > Node <&Node Instances to Points>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (Instances)
        - selection (Boolean) : socket 'Selection' (Selection)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Geometry
        """

        node = Node('Instances to Points', {'Instances': instances, 'Selection': selection, 'Position': position, 'Radius': radius})
        return node._out


    @classmethod
    def interpolate_curves(cls, guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Node <&Node Interpolate Curves>

        Arguments
        ---------
        - guide_curves (Geometry) : socket 'Guide Curves' (Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (Guide Group ID)
        - points (Geometry) : socket 'Points' (Points)
        - point_up (Vector) : socket 'Point Up' (Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (Max Neighbors)

        Returns
        -------
        - Node
        """

        node = Node('Interpolate Curves', {'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node


    @classmethod
    @property
    def is_viewport(cls):
        """ > Node <&Node Is Viewport>

        Returns
        -------
        - Boolean
        """

        node = Node('Is Viewport')
        return node._out


    @classmethod
    def join_geometry(cls, *geometry):
        """ > Node <&Node Join Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Geometry
        """

        node = Node('Join Geometry', {'Geometry': list(geometry)})
        return node._out


    @classmethod
    def material_selection(cls, material=None):
        """ > Node <&Node Material Selection>

        Arguments
        ---------
        - material (Material) : socket 'Material' (Material)

        Returns
        -------
        - Boolean
        """

        node = Node('Material Selection', {'Material': material})
        return node._out


    @classmethod
    def menu_switch(cls, menu=None, a=None, b=None, active_index=1, data_type='GEOMETRY'):
        """ > Node <&Node Menu Switch>

        Arguments
        ---------
        - menu (Menu) : socket 'Menu' (Menu)
        - a (Geometry) : socket 'A' (Item_0)
        - b (Geometry) : socket 'B' (Item_1)
        - active_index (int): Node.active_index
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL')

        Returns
        -------
        - Geometry
        """

        #node = Node('Menu Switch', {'Menu': menu, 'Item_0': a, 'Item_1': b}, active_index=active_index, active_item=active_item, data_type=data_type, enum_definition=enum_definition, enum_items=enum_items)
        node = Node('Menu Switch', {'Menu': menu, 'Item_0': a, 'Item_1': b}, active_index=active_index, data_type=data_type)
        return node._out


    @classmethod
    def merge_by_distance(cls, geometry=None, selection=None, distance=None, mode='ALL'):
        """ > Node <&Node Merge by Distance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - distance (Float) : socket 'Distance' (Distance)
        - mode (str): Node.mode in ('ALL', 'CONNECTED')

        Returns
        -------
        - Geometry
        """

        node = Node('Merge by Distance', {'Geometry': geometry, 'Selection': selection, 'Distance': distance}, mode=mode)
        return node._out


    @classmethod
    def mesh_boolean(cls, mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Arguments
        ---------
        - mesh_1 (Geometry) : socket 'Mesh 1' (Mesh 1)
        - mesh_2 (Geometry) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - operation (str): Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Node
        """

        node = Node('Mesh Boolean', {'Mesh 1': mesh_1, 'Mesh 2': mesh_2, 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation=operation, solver=solver)
        return node


    @classmethod
    def mesh_circle(cls, vertices=None, radius=None, fill_type='NONE'):
        """ > Node <&Node Mesh Circle>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - radius (Float) : socket 'Radius' (Radius)
        - fill_type (str): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Geometry
        """

        node = Node('Mesh Circle', {'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        return node._out


    @classmethod
    def cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """ > Node <&Node Cone>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - side_segments (Integer) : socket 'Side Segments' (Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (Fill Segments)
        - radius_top (Float) : socket 'Radius Top' (Radius Top)
        - radius_bottom (Float) : socket 'Radius Bottom' (Radius Bottom)
        - depth (Float) : socket 'Depth' (Depth)
        - fill_type (str): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Node
        """

        node = Node('Cone', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        return node


    @classmethod
    def cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """ > Node <&Node Cube>

        Arguments
        ---------
        - size (Vector) : socket 'Size' (Size)
        - vertices_x (Integer) : socket 'Vertices X' (Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (Vertices Y)
        - vertices_z (Integer) : socket 'Vertices Z' (Vertices Z)

        Returns
        -------
        - Node
        """

        node = Node('Cube', {'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        return node


    @classmethod
    def cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """ > Node <&Node Cylinder>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - side_segments (Integer) : socket 'Side Segments' (Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (Fill Segments)
        - radius (Float) : socket 'Radius' (Radius)
        - depth (Float) : socket 'Depth' (Depth)
        - fill_type (str): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Node
        """

        node = Node('Cylinder', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius': radius, 'Depth': depth}, fill_type=fill_type)
        return node


    @classmethod
    def face_group_boundaries(cls, face_group_id=None):
        """ > Node <&Node Face Group Boundaries>

        Arguments
        ---------
        - face_group_id (Integer) : socket 'Face Group ID' (Face Set)

        Returns
        -------
        - Boolean
        """

        node = Node('Face Group Boundaries', {'Face Set': face_group_id})
        return node._out


    @classmethod
    def grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """ > Node <&Node Grid>

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (Size X)
        - size_y (Float) : socket 'Size Y' (Size Y)
        - vertices_x (Integer) : socket 'Vertices X' (Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (Vertices Y)

        Returns
        -------
        - Node
        """

        node = Node('Grid', {'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        return node


    @classmethod
    def ico_sphere(cls, radius=None, subdivisions=None):
        """ > Node <&Node Ico Sphere>

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (Radius)
        - subdivisions (Integer) : socket 'Subdivisions' (Subdivisions)

        Returns
        -------
        - Node
        """

        node = Node('Ico Sphere', {'Radius': radius, 'Subdivisions': subdivisions})
        return node


    @classmethod
    def mesh_line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """ > Node <&Node Mesh Line>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (Count)
        - start_location (Vector) : socket 'Start Location' (Start Location)
        - offset (Vector) : socket 'Offset' (Offset)
        - count_mode (str): Node.count_mode in ('TOTAL', 'RESOLUTION')
        - mode (str): Node.mode in ('OFFSET', 'END_POINTS')

        Returns
        -------
        - Geometry
        """

        node = Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode=mode)
        return node._out


    @classmethod
    def mesh_to_curve(cls, mesh=None, selection=None):
        """ > Node <&Node Mesh to Curve>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)

        Returns
        -------
        - Geometry
        """

        node = Node('Mesh to Curve', {'Mesh': mesh, 'Selection': selection})
        return node._out


    @classmethod
    def mesh_to_density_grid(cls, mesh=None, density=None, voxel_size=None, gradient_width=None):
        """ > Node <&Node Mesh to Density Grid>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - density (Float) : socket 'Density' (Density)
        - voxel_size (Float) : socket 'Voxel Size' (Voxel Size)
        - gradient_width (Float) : socket 'Gradient Width' (Gradient Width)

        Returns
        -------
        - Float
        """

        node = Node('Mesh to Density Grid', {'Mesh': mesh, 'Density': density, 'Voxel Size': voxel_size, 'Gradient Width': gradient_width})
        return node._out


    @classmethod
    def mesh_to_points(cls, mesh=None, selection=None, position=None, radius=None, mode='VERTICES'):
        """ > Node <&Node Mesh to Points>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)
        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

        Returns
        -------
        - Geometry
        """

        node = Node('Mesh to Points', {'Mesh': mesh, 'Selection': selection, 'Position': position, 'Radius': radius}, mode=mode)
        return node._out


    @classmethod
    def mesh_to_sdf_grid(cls, mesh=None, voxel_size=None, band_width=None):
        """ > Node <&Node Mesh to SDF Grid>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - voxel_size (Float) : socket 'Voxel Size' (Voxel Size)
        - band_width (Integer) : socket 'Band Width' (Band Width)

        Returns
        -------
        - Float
        """

        node = Node('Mesh to SDF Grid', {'Mesh': mesh, 'Voxel Size': voxel_size, 'Band Width': band_width})
        return node._out


    @classmethod
    def mesh_to_volume(cls, mesh=None, density=None, voxel_amount=None, interior_band_width=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Mesh to Volume>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - density (Float) : socket 'Density' (Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (Voxel Amount)
        - interior_band_width (Float) : socket 'Interior Band Width' (Interior Band Width)
        - resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Geometry
        """

        node = Node('Mesh to Volume', {'Mesh': mesh, 'Density': density, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width}, resolution_mode=resolution_mode)
        return node._out


    @classmethod
    def uv_sphere(cls, segments=None, rings=None, radius=None):
        """ > Node <&Node UV Sphere>

        Arguments
        ---------
        - segments (Integer) : socket 'Segments' (Segments)
        - rings (Integer) : socket 'Rings' (Rings)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Node
        """

        node = Node('UV Sphere', {'Segments': segments, 'Rings': rings, 'Radius': radius})
        return node


    @classmethod
    def object_info(cls, object=None, as_instance=None, transform_space='ORIGINAL'):
        """ > Node <&Node Object Info>

        Arguments
        ---------
        - object (Object) : socket 'Object' (Object)
        - as_instance (Boolean) : socket 'As Instance' (As Instance)
        - transform_space (str): Node.transform_space in ('ORIGINAL', 'RELATIVE')

        Returns
        -------
        - Node
        """

        node = Node('Object Info', {'Object': object, 'As Instance': as_instance}, transform_space=transform_space)
        return node


    @classmethod
    def offset_corner_in_face(cls, corner_index=None, offset=None):
        """ > Node <&Node Offset Corner in Face>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)
        - offset (Integer) : socket 'Offset' (Offset)

        Returns
        -------
        - Integer
        """

        node = Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})
        return node._out


    @classmethod
    def offset_point_in_curve(cls, point_index=None, offset=None):
        """ > Node <&Node Offset Point in Curve>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (Point Index)
        - offset (Integer) : socket 'Offset' (Offset)

        Returns
        -------
        - Node
        """

        node = Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset})
        return node


    @classmethod
    def points(cls, count=None, position=None, radius=None):
        """ > Node <&Node Points>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (Count)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Geometry
        """

        node = Node('Points', {'Count': count, 'Position': position, 'Radius': radius})
        return node._out


    @classmethod
    def points_of_curve(cls, curve_index=None, weights=None, sort_index=None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (Curve Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Node
        """

        node = Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node


    @classmethod
    def points_to_curves(cls, points=None, curve_group_id=None, weight=None):
        """ > Node <&Node Points to Curves>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - curve_group_id (Integer) : socket 'Curve Group ID' (Curve Group ID)
        - weight (Float) : socket 'Weight' (Weight)

        Returns
        -------
        - Geometry
        """

        node = Node('Points to Curves', {'Points': points, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out


    @classmethod
    def points_to_sdf_grid(cls, points=None, radius=None, voxel_size=None):
        """ > Node <&Node Points to SDF Grid>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - radius (Float) : socket 'Radius' (Radius)
        - voxel_size (Float) : socket 'Voxel Size' (Voxel Size)

        Returns
        -------
        - Float
        """

        node = Node('Points to SDF Grid', {'Points': points, 'Radius': radius, 'Voxel Size': voxel_size})
        return node._out


    @classmethod
    def points_to_vertices(cls, points=None, selection=None):
        """ > Node <&Node Points to Vertices>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - selection (Boolean) : socket 'Selection' (Selection)

        Returns
        -------
        - Geometry
        """

        node = Node('Points to Vertices', {'Points': points, 'Selection': selection})
        return node._out


    @classmethod
    def points_to_volume(cls, points=None, density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Points to Volume>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - density (Float) : socket 'Density' (Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (Voxel Amount)
        - radius (Float) : socket 'Radius' (Radius)
        - resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Geometry
        """

        node = Node('Points to Volume', {'Points': points, 'Density': density, 'Voxel Amount': voxel_amount, 'Radius': radius}, resolution_mode=resolution_mode)
        return node._out


    @classmethod
    def geometry_proximity(cls, geometry=None, group_id=None, sample_position=None, sample_group_id=None, target_element='FACES'):
        """ > Node <&Node Geometry Proximity>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Target)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sample_position (Vector) : socket 'Sample Position' (Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (Sample Group ID)
        - target_element (str): Node.target_element in ('POINTS', 'EDGES', 'FACES')

        Returns
        -------
        - Node
        """

        node = Node('Geometry Proximity', {'Target': geometry, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=target_element)
        return node


    @classmethod
    def raycast(cls, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):
        """ > Node <&Node Raycast>

        Arguments
        ---------
        - target_geometry (Geometry) : socket 'Target Geometry' (Target Geometry)
        - attribute (Float) : socket 'Attribute' (Attribute)
        - source_position (Vector) : socket 'Source Position' (Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (Ray Length)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - mapping (str): Node.mapping in ('INTERPOLATED', 'NEAREST')

        Returns
        -------
        - Node
        """

        node = Node('Raycast', {'Target Geometry': target_geometry, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type, mapping=mapping)
        return node


    @classmethod
    def realize_instances(cls, geometry=None, selection=None, realize_all=None, depth=None):
        """ > Node <&Node Realize Instances>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - realize_all (Boolean) : socket 'Realize All' (Realize All)
        - depth (Integer) : socket 'Depth' (Depth)

        Returns
        -------
        - Geometry
        """

        node = Node('Realize Instances', {'Geometry': geometry, 'Selection': selection, 'Realize All': realize_all, 'Depth': depth})
        return node._out


    @classmethod
    def remove_named_attribute(cls, geometry=None, name=None, pattern_mode='EXACT'):
        """ > Node <&Node Remove Named Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - name (String) : socket 'Name' (Name)
        - pattern_mode (str): Node.pattern_mode in ('EXACT', 'WILDCARD')

        Returns
        -------
        - Geometry
        """

        node = Node('Remove Named Attribute', {'Geometry': geometry, 'Name': name}, pattern_mode=pattern_mode)
        return node._out


    @classmethod
    def repeat_input(cls, iterations=None, pair_with_output=None, paired_output=None):
        """ > Node <&Node Repeat Input>

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (Iterations)
        - pair_with_output (bpy_func): Node.pair_with_output
        - paired_output (NoneType): Node.paired_output

        Returns
        -------
        """

        node = Node('Repeat Input', {'Iterations': iterations}, pair_with_output=pair_with_output, paired_output=paired_output)
        return node._out


    @classmethod
    def repeat_output(cls, geometry=None, active_index=0, active_item=None, inspection_index=0, repeat_items=None):
        """ > Node <&Node Repeat Output>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Item_0)
        - active_index (int): Node.active_index
        - active_item (RepeatItem): Node.active_item
        - inspection_index (int): Node.inspection_index
        - repeat_items (bpy_prop_collection): Node.repeat_items

        Returns
        -------
        - Node
        """

        node = Node('Repeat Output', {'Item_0': geometry}, active_index=active_index, active_item=active_item, inspection_index=inspection_index, repeat_items=repeat_items)
        return node


    @classmethod
    def replace_material(cls, geometry=None, old=None, new=None):
        """ > Node <&Node Replace Material>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - old (Material) : socket 'Old' (Old)
        - new (Material) : socket 'New' (New)

        Returns
        -------
        - Geometry
        """

        node = Node('Replace Material', {'Geometry': geometry, 'Old': old, 'New': new})
        return node._out


    @classmethod
    def resample_curve(cls, curve=None, selection=None, count=None, mode='COUNT'):
        """ > Node <&Node Resample Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - count (Integer) : socket 'Count' (Count)
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Geometry
        """

        node = Node('Resample Curve', {'Curve': curve, 'Selection': selection, 'Count': count}, mode=mode)
        return node._out


    @classmethod
    def reverse_curve(cls, curve=None, selection=None):
        """ > Node <&Node Reverse Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)

        Returns
        -------
        - Geometry
        """

        node = Node('Reverse Curve', {'Curve': curve, 'Selection': selection})
        return node._out


    @classmethod
    def rotate_instances(cls, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ > Node <&Node Rotate Instances>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (Instances)
        - selection (Boolean) : socket 'Selection' (Selection)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - pivot_point (Vector) : socket 'Pivot Point' (Pivot Point)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Geometry
        """

        node = Node('Rotate Instances', {'Instances': instances, 'Selection': selection, 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})
        return node._out


    @classmethod
    def sdf_grid_boolean(cls, grid_1=None, grid_2=None, operation='DIFFERENCE'):
        """ > Node <&Node SDF Grid Boolean>

        Arguments
        ---------
        - grid_1 (Float) : socket 'Grid 1' (Grid 1)
        - grid_2 (Float) : socket 'Grid 2' (Grid 2)
        - operation (str): Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')

        Returns
        -------
        - Float
        """

        node = Node('SDF Grid Boolean', {'Grid 1': grid_1, 'Grid 2': grid_2}, operation=operation)
        return node._out


    @classmethod
    def sample_curve(cls, curves=None, value=None, factor=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):
        """ > Node <&Node Sample Curve>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (Curves)
        - value (Float) : socket 'Value' (Value)
        - factor (Float) : socket 'Factor' (Factor)
        - curve_index (Integer) : socket 'Curve Index' (Curve Index)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - mode (str): Node.mode in ('FACTOR', 'LENGTH')
        - use_all_curves (bool): Node.use_all_curves

        Returns
        -------
        - Node
        """

        node = Node('Sample Curve', {'Curves': curves, 'Value': value, 'Factor': factor, 'Curve Index': curve_index}, data_type=data_type, mode=mode, use_all_curves=use_all_curves)
        return node


    @classmethod
    def sample_grid(cls, grid=None, position=None, data_type='FLOAT', interpolation_mode='TRILINEAR'):
        """ > Node <&Node Sample Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (Grid)
        - position (Vector) : socket 'Position' (Position)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR')
        - interpolation_mode (str): Node.interpolation_mode in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')

        Returns
        -------
        - Float
        """

        node = Node('Sample Grid', {'Grid': grid, 'Position': position}, data_type=data_type, interpolation_mode=interpolation_mode)
        return node._out


    @classmethod
    def sample_grid_index(cls, grid=None, x=None, y=None, z=None, data_type='FLOAT'):
        """ > Node <&Node Sample Grid Index>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (Grid)
        - x (Integer) : socket 'X' (X)
        - y (Integer) : socket 'Y' (Y)
        - z (Integer) : socket 'Z' (Z)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR')

        Returns
        -------
        - Float
        """

        node = Node('Sample Grid Index', {'Grid': grid, 'X': x, 'Y': y, 'Z': z}, data_type=data_type)
        return node._out


    @classmethod
    def sample_index(cls, geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Sample Index>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - value (Float) : socket 'Value' (Value)
        - index (Integer) : socket 'Index' (Index)
        - clamp (bool): Node.clamp
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Float
        """

        node = Node('Sample Index', {'Geometry': geometry, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain=domain)
        return node._out


    @classmethod
    def sample_nearest(cls, geometry=None, sample_position=None, domain='POINT'):
        """ > Node <&Node Sample Nearest>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - sample_position (Vector) : socket 'Sample Position' (Sample Position)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER')

        Returns
        -------
        - Integer
        """

        node = Node('Sample Nearest', {'Geometry': geometry, 'Sample Position': sample_position}, domain=domain)
        return node._out


    @classmethod
    def sample_nearest_surface(cls, mesh=None, value=None, group_id=None, sample_position=None, sample_group_id=None, data_type='FLOAT'):
        """ > Node <&Node Sample Nearest Surface>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - value (Float) : socket 'Value' (Value)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sample_position (Vector) : socket 'Sample Position' (Sample Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (Sample Group ID)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Returns
        -------
        - Node
        """

        node = Node('Sample Nearest Surface', {'Mesh': mesh, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)
        return node


    @classmethod
    def sample_uv_surface(cls, mesh=None, value=None, uv_map=None, sample_uv=None, data_type='FLOAT'):
        """ > Node <&Node Sample UV Surface>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - value (Float) : socket 'Value' (Value)
        - uv_map (Vector) : socket 'UV Map' (Source UV Map)
        - sample_uv (Vector) : socket 'Sample UV' (Sample UV)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Returns
        -------
        - Node
        """

        node = Node('Sample UV Surface', {'Mesh': mesh, 'Value': value, 'Source UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)
        return node


    @classmethod
    def scale_elements(cls, geometry=None, selection=None, scale=None, center=None, domain='FACE', scale_mode='UNIFORM'):
        """ > Node <&Node Scale Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - scale (Float) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - domain (str): Node.domain in ('FACE', 'EDGE')
        - scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

        Returns
        -------
        - Geometry
        """

        node = Node('Scale Elements', {'Geometry': geometry, 'Selection': selection, 'Scale': scale, 'Center': center}, domain=domain, scale_mode=scale_mode)
        return node._out


    @classmethod
    def scale_instances(cls, instances=None, selection=None, scale=None, center=None, local_space=None):
        """ > Node <&Node Scale Instances>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (Instances)
        - selection (Boolean) : socket 'Selection' (Selection)
        - scale (Vector) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Geometry
        """

        node = Node('Scale Instances', {'Instances': instances, 'Selection': selection, 'Scale': scale, 'Center': center, 'Local Space': local_space})
        return node._out


    @classmethod
    @property
    def self_object(cls):
        """ > Node <&Node Self Object>

        Returns
        -------
        - Object
        """

        node = Node('Self Object')
        return node._out


    @classmethod
    def separate_components(cls, geometry=None):
        """ > Node <&Node Separate Components>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Node
        """

        node = Node('Separate Components', {'Geometry': geometry})
        return node


    @classmethod
    def separate_geometry(cls, geometry=None, selection=None, domain='POINT'):
        """ > Node <&Node Separate Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Node
        """

        node = Node('Separate Geometry', {'Geometry': geometry, 'Selection': selection}, domain=domain)
        return node


    @classmethod
    def set_handle_positions(cls, curve=None, selection=None, position=None, offset=None, mode='LEFT'):
        """ > Node <&Node Set Handle Positions>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - position (Vector) : socket 'Position' (Position)
        - offset (Vector) : socket 'Offset' (Offset)
        - mode (str): Node.mode in ('LEFT', 'RIGHT')

        Returns
        -------
        - Geometry
        """

        node = Node('Set Handle Positions', {'Curve': curve, 'Selection': selection, 'Position': position, 'Offset': offset}, mode=mode)
        return node._out


    @classmethod
    def set_curve_normal(cls, curve=None, selection=None, mode='MINIMUM_TWIST'):
        """ > Node <&Node Set Curve Normal>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - mode (str): Node.mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')

        Returns
        -------
        - Geometry
        """

        node = Node('Set Curve Normal', {'Curve': curve, 'Selection': selection}, mode=mode)
        return node._out


    @classmethod
    def set_curve_radius(cls, curve=None, selection=None, radius=None):
        """ > Node <&Node Set Curve Radius>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Curve Radius', {'Curve': curve, 'Selection': selection, 'Radius': radius})
        return node._out


    @classmethod
    def set_curve_tilt(cls, curve=None, selection=None, tilt=None):
        """ > Node <&Node Set Curve Tilt>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - tilt (Float) : socket 'Tilt' (Tilt)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Curve Tilt', {'Curve': curve, 'Selection': selection, 'Tilt': tilt})
        return node._out


    @classmethod
    def set_id(cls, geometry=None, selection=None, id=None):
        """ > Node <&Node Set ID>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - id (Integer) : socket 'ID' (ID)

        Returns
        -------
        - Geometry
        """

        node = Node('Set ID', {'Geometry': geometry, 'Selection': selection, 'ID': id})
        return node._out


    @classmethod
    def set_instance_transform(cls, instances=None, selection=None, transform=None):
        """ > Node <&Node Set Instance Transform>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (Instances)
        - selection (Boolean) : socket 'Selection' (Selection)
        - transform (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Instance Transform', {'Instances': instances, 'Selection': selection, 'Transform': transform})
        return node._out


    @classmethod
    def set_material(cls, geometry=None, selection=None, material=None):
        """ > Node <&Node Set Material>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - material (Material) : socket 'Material' (Material)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Material', {'Geometry': geometry, 'Selection': selection, 'Material': material})
        return node._out


    @classmethod
    def set_material_index(cls, geometry=None, selection=None, material_index=None):
        """ > Node <&Node Set Material Index>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - material_index (Integer) : socket 'Material Index' (Material Index)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Material Index', {'Geometry': geometry, 'Selection': selection, 'Material Index': material_index})
        return node._out


    @classmethod
    def set_point_radius(cls, points=None, selection=None, radius=None):
        """ > Node <&Node Set Point Radius>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - selection (Boolean) : socket 'Selection' (Selection)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Point Radius', {'Points': points, 'Selection': selection, 'Radius': radius})
        return node._out


    @classmethod
    def set_position(cls, geometry=None, selection=None, position=None, offset=None):
        """ > Node <&Node Set Position>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - position (Vector) : socket 'Position' (Position)
        - offset (Vector) : socket 'Offset' (Offset)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Position', {'Geometry': geometry, 'Selection': selection, 'Position': position, 'Offset': offset})
        return node._out


    @classmethod
    def set_shade_smooth(cls, geometry=None, selection=None, shade_smooth=None, domain='FACE'):
        """ > Node <&Node Set Shade Smooth>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - shade_smooth (Boolean) : socket 'Shade Smooth' (Shade Smooth)
        - domain (str): Node.domain in ('EDGE', 'FACE')

        Returns
        -------
        - Geometry
        """

        node = Node('Set Shade Smooth', {'Geometry': geometry, 'Selection': selection, 'Shade Smooth': shade_smooth}, domain=domain)
        return node._out


    @classmethod
    def set_spline_cyclic(cls, geometry=None, selection=None, cyclic=None):
        """ > Node <&Node Set Spline Cyclic>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - cyclic (Boolean) : socket 'Cyclic' (Cyclic)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Spline Cyclic', {'Geometry': geometry, 'Selection': selection, 'Cyclic': cyclic})
        return node._out


    @classmethod
    def set_spline_resolution(cls, geometry=None, selection=None, resolution=None):
        """ > Node <&Node Set Spline Resolution>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - resolution (Integer) : socket 'Resolution' (Resolution)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Spline Resolution', {'Geometry': geometry, 'Selection': selection, 'Resolution': resolution})
        return node._out


    @classmethod
    def simulation_input(cls, pair_with_output=None, paired_output=None):
        """ > Node <&Node Simulation Input>

        Arguments
        ---------
        - pair_with_output (bpy_func): Node.pair_with_output
        - paired_output (NoneType): Node.paired_output

        Returns
        -------
        - Float
        """

        node = Node('Simulation Input', pair_with_output=pair_with_output, paired_output=paired_output)
        return node._out


    @classmethod
    def simulation_output(cls, skip=None, geometry=None, active_index=0, active_item=None, state_items=None):
        """ > Node <&Node Simulation Output>

        Arguments
        ---------
        - skip (Boolean) : socket 'Skip' (Skip)
        - geometry (Geometry) : socket 'Geometry' (Item_0)
        - active_index (int): Node.active_index
        - active_item (SimulationStateItem): Node.active_item
        - state_items (bpy_prop_collection): Node.state_items

        Returns
        -------
        - Node
        """

        node = Node('Simulation Output', {'Skip': skip, 'Item_0': geometry}, active_index=active_index, active_item=active_item, state_items=state_items)
        return node


    @classmethod
    def sort_elements(cls, geometry=None, selection=None, group_id=None, sort_weight=None, domain='POINT'):
        """ > Node <&Node Sort Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (Sort Weight)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Geometry
        """

        node = Node('Sort Elements', {'Geometry': geometry, 'Selection': selection, 'Group ID': group_id, 'Sort Weight': sort_weight}, domain=domain)
        return node._out


    @classmethod
    @property
    def spline_length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - Node
        """

        node = Node('Spline Length')
        return node


    @classmethod
    @property
    def spline_parameter(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - Node
        """

        node = Node('Spline Parameter')
        return node


    @classmethod
    def split_edges(cls, mesh=None, selection=None):
        """ > Node <&Node Split Edges>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)

        Returns
        -------
        - Geometry
        """

        node = Node('Split Edges', {'Mesh': mesh, 'Selection': selection})
        return node._out


    @classmethod
    def split_to_instances(cls, geometry=None, selection=None, group_id=None, domain='POINT'):
        """ > Node <&Node Split to Instances>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Node
        """

        node = Node('Split to Instances', {'Geometry': geometry, 'Selection': selection, 'Group ID': group_id}, domain=domain)
        return node


    @classmethod
    def store_named_attribute(cls, geometry=None, selection=None, name=None, value=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Store Named Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - name (String) : socket 'Name' (Name)
        - value (Float) : socket 'Value' (Value)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Geometry
        """

        node = Node('Store Named Attribute', {'Geometry': geometry, 'Selection': selection, 'Name': name, 'Value': value}, data_type=data_type, domain=domain)
        return node._out


    @classmethod
    def store_named_grid(cls, volume=None, name=None, grid=None, data_type='FLOAT'):
        """ > Node <&Node Store Named Grid>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (Volume)
        - name (String) : socket 'Name' (Name)
        - grid (Float) : socket 'Grid' (Grid)
        - data_type (str): Node.data_type in ('FLOAT', 'FLOAT_VECTOR', 'FLOAT2')

        Returns
        -------
        - Geometry
        """

        node = Node('Store Named Grid', {'Volume': volume, 'Name': name, 'Grid': grid}, data_type=data_type)
        return node._out


    @classmethod
    def join_strings(cls, delimiter=None, strings=None):
        """ > Node <&Node Join Strings>

        Arguments
        ---------
        - delimiter (String) : socket 'Delimiter' (Delimiter)
        - strings (String) : socket 'Strings' (Strings)

        Returns
        -------
        - String
        """

        node = Node('Join Strings', {'Delimiter': delimiter, 'Strings': strings})
        return node._out


    @classmethod
    def string_to_curves(cls, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """ > Node <&Node String to Curves>

        Arguments
        ---------
        - string (String) : socket 'String' (String)
        - size (Float) : socket 'Size' (Size)
        - character_spacing (Float) : socket 'Character Spacing' (Character Spacing)
        - word_spacing (Float) : socket 'Word Spacing' (Word Spacing)
        - line_spacing (Float) : socket 'Line Spacing' (Line Spacing)
        - text_box_width (Float) : socket 'Text Box Width' (Text Box Width)
        - align_x (str): Node.align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
        - align_y (str): Node.align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
        - font (VectorFont): Node.font
        - overflow (str): Node.overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
        - pivot_mode (str): Node.pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')

        Returns
        -------
        - Node
        """

        node = Node('String to Curves', {'String': string, 'Size': size, 'Character Spacing': character_spacing, 'Word Spacing': word_spacing, 'Line Spacing': line_spacing, 'Text Box Width': text_box_width}, align_x=align_x, align_y=align_y, font=font, overflow=overflow, pivot_mode=pivot_mode)
        return node


    @classmethod
    def subdivide_curve(cls, curve=None, cuts=None):
        """ > Node <&Node Subdivide Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - cuts (Integer) : socket 'Cuts' (Cuts)

        Returns
        -------
        - Geometry
        """

        node = Node('Subdivide Curve', {'Curve': curve, 'Cuts': cuts})
        return node._out


    @classmethod
    def subdivide_mesh(cls, mesh=None, level=None):
        """ > Node <&Node Subdivide Mesh>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - level (Integer) : socket 'Level' (Level)

        Returns
        -------
        - Geometry
        """

        node = Node('Subdivide Mesh', {'Mesh': mesh, 'Level': level})
        return node._out


    @classmethod
    def subdivision_surface(cls, mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """ > Node <&Node Subdivision Surface>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - level (Integer) : socket 'Level' (Level)
        - edge_crease (Float) : socket 'Edge Crease' (Edge Crease)
        - vertex_crease (Float) : socket 'Vertex Crease' (Vertex Crease)
        - boundary_smooth (str): Node.boundary_smooth in ('PRESERVE_CORNERS', 'ALL')
        - uv_smooth (str): Node.uv_smooth in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')

        Returns
        -------
        - Geometry
        """

        node = Node('Subdivision Surface', {'Mesh': mesh, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease}, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth)
        return node._out


    @classmethod
    def switch(cls, switch=None, false=None, true=None, input_type='GEOMETRY'):
        """ > Node <&Node Switch>

        Arguments
        ---------
        - switch (Boolean) : socket 'Switch' (Switch)
        - false (Geometry) : socket 'False' (False)
        - true (Geometry) : socket 'True' (True)
        - input_type (str): Node.input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL')

        Returns
        -------
        - Geometry
        """

        node = Node('Switch', {'Switch': switch, 'False': false, 'True': true}, input_type=input_type)
        return node._out


    @classmethod
    @property
    def _3d_cursor(cls):
        """ > Node <&Node 3D Cursor>

        Returns
        -------
        - Node
        """

        node = Node('3D Cursor')
        return node


    @classmethod
    def active_element(cls, domain='POINT'):
        """ > Node <&Node Active Element>

        Arguments
        ---------
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE')

        Returns
        -------
        - Node
        """

        node = Node('Active Element', domain=domain)
        return node


    @classmethod
    @property
    def face_set(cls):
        """ > Node <&Node Face Set>

        Returns
        -------
        - Node
        """

        node = Node('Face Set')
        return node


    @classmethod
    @property
    def mouse_position(cls):
        """ > Node <&Node Mouse Position>

        Returns
        -------
        - Node
        """

        node = Node('Mouse Position')
        return node


    @classmethod
    @property
    def selection(cls):
        """ > Node <&Node Selection>

        Returns
        -------
        - Boolean
        """

        node = Node('Selection')
        return node._out


    @classmethod
    def set_face_set(cls, mesh=None, selection=None, face_set=None):
        """ > Node <&Node Set Face Set>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)
        - face_set (Integer) : socket 'Face Set' (Face Set)

        Returns
        -------
        - Geometry
        """

        node = Node('Set Face Set', {'Mesh': mesh, 'Selection': selection, 'Face Set': face_set})
        return node._out


    @classmethod
    def set_selection(cls, geometry=None, selection=None, domain='POINT'):
        """ > Node <&Node Set Selection>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE')

        Returns
        -------
        - Geometry
        """

        node = Node('Set Selection', {'Geometry': geometry, 'Selection': selection}, domain=domain)
        return node._out


    @classmethod
    def transform_geometry(cls, geometry=None, translation=None, rotation=None, scale=None, mode='COMPONENTS'):
        """ > Node <&Node Transform Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - translation (Vector) : socket 'Translation' (Translation)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)
        - mode (str): Node.mode in ('COMPONENTS', 'MATRIX')

        Returns
        -------
        - Geometry
        """

        node = Node('Transform Geometry', {'Geometry': geometry, 'Translation': translation, 'Rotation': rotation, 'Scale': scale}, mode=mode)
        return node._out


    @classmethod
    def translate_instances(cls, instances=None, selection=None, translation=None, local_space=None):
        """ > Node <&Node Translate Instances>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (Instances)
        - selection (Boolean) : socket 'Selection' (Selection)
        - translation (Vector) : socket 'Translation' (Translation)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Geometry
        """

        node = Node('Translate Instances', {'Instances': instances, 'Selection': selection, 'Translation': translation, 'Local Space': local_space})
        return node._out


    @classmethod
    def triangulate(cls, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ > Node <&Node Triangulate>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - selection (Boolean) : socket 'Selection' (Selection)
        - minimum_vertices (Integer) : socket 'Minimum Vertices' (Minimum Vertices)
        - ngon_method (str): Node.ngon_method in ('BEAUTY', 'CLIP')
        - quad_method (str): Node.quad_method in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

        Returns
        -------
        - Geometry
        """

        node = Node('Triangulate', {'Mesh': mesh, 'Selection': selection, 'Minimum Vertices': minimum_vertices}, ngon_method=ngon_method, quad_method=quad_method)
        return node._out


    @classmethod
    def trim_curve(cls, curve=None, selection=None, start=None, end=None, mode='FACTOR'):
        """ > Node <&Node Trim Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - selection (Boolean) : socket 'Selection' (Selection)
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)
        - mode (str): Node.mode in ('FACTOR', 'LENGTH')

        Returns
        -------
        - Geometry
        """

        node = Node('Trim Curve', {'Curve': curve, 'Selection': selection, 'Start': start, 'End': end}, mode=mode)
        return node._out


    @classmethod
    def pack_uv_islands(cls, uv=None, selection=None, margin=None, rotate=None):
        """ > Node <&Node Pack UV Islands>

        Arguments
        ---------
        - uv (Vector) : socket 'UV' (UV)
        - selection (Boolean) : socket 'Selection' (Selection)
        - margin (Float) : socket 'Margin' (Margin)
        - rotate (Boolean) : socket 'Rotate' (Rotate)

        Returns
        -------
        - Vector
        """

        node = Node('Pack UV Islands', {'UV': uv, 'Selection': selection, 'Margin': margin, 'Rotate': rotate})
        return node._out


    @classmethod
    def uv_unwrap(cls, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """ > Node <&Node UV Unwrap>

        Arguments
        ---------
        - selection (Boolean) : socket 'Selection' (Selection)
        - seam (Boolean) : socket 'Seam' (Seam)
        - margin (Float) : socket 'Margin' (Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (Fill Holes)
        - method (str): Node.method in ('ANGLE_BASED', 'CONFORMAL')

        Returns
        -------
        - Vector
        """

        node = Node('UV Unwrap', {'Selection': selection, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)
        return node._out


    @classmethod
    def vertex_of_corner(cls, corner_index=None):
        """ > Node <&Node Vertex of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Integer
        """

        node = Node('Vertex of Corner', {'Corner Index': corner_index})
        return node._out


    @classmethod
    def viewer(cls, geometry=None, value=None, data_type='FLOAT', domain='AUTO'):
        """ > Node <&Node Viewer>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - value (Float) : socket 'Value' (Value)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        """

        node = Node('Viewer', {'Geometry': geometry, 'Value': value}, data_type=data_type, domain=domain)
        return node._out


    @classmethod
    @property
    def viewport_transform(cls):
        """ > Node <&Node Viewport Transform>

        Returns
        -------
        - Node
        """

        node = Node('Viewport Transform')
        return node


    @classmethod
    def volume_cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
        """ > Node <&Node Volume Cube>

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)
        - background (Float) : socket 'Background' (Background)
        - min (Vector) : socket 'Min' (Min)
        - max (Vector) : socket 'Max' (Max)
        - resolution_x (Integer) : socket 'Resolution X' (Resolution X)
        - resolution_y (Integer) : socket 'Resolution Y' (Resolution Y)
        - resolution_z (Integer) : socket 'Resolution Z' (Resolution Z)

        Returns
        -------
        - Geometry
        """

        node = Node('Volume Cube', {'Density': density, 'Background': background, 'Min': min, 'Max': max, 'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})
        return node._out


    @classmethod
    def volume_to_mesh(cls, volume=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ > Node <&Node Volume to Mesh>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (Volume)
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)
        - resolution_mode (str): Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Geometry
        """

        node = Node('Volume to Mesh', {'Volume': volume, 'Threshold': threshold, 'Adaptivity': adaptivity}, resolution_mode=resolution_mode)
        return node._out


    @classmethod
    def frame(cls, label_size=20, shrink=True, text=None):
        """ > Node <&Node Frame>

        Arguments
        ---------
        - label_size (int): Node.label_size
        - shrink (bool): Node.shrink
        - text (NoneType): Node.text
        """

        node = Node('Frame', label_size=label_size, shrink=shrink, text=text)
        return node._out


    @classmethod
    @property
    def group_input(cls):
        """ > Node <&Node Group Input>

        Returns
        -------
        """

        node = Node('Group Input')
        return node._out


    @classmethod
    def group_output(cls, is_active_output=True):
        """ > Node <&Node Group Output>

        Arguments
        ---------
        - is_active_output (bool): Node.is_active_output
        """

        node = Node('Group Output', is_active_output=is_active_output)
        return node._out


    @classmethod
    def reroute(cls, input=None):
        """ > Node <&Node Reroute>

        Arguments
        ---------
        - input (Color) : socket 'Input' (Input)

        Returns
        -------
        - Color
        """

        node = Node('Reroute', {'Input': input})
        return node._out


    @classmethod
    def blackbody(cls, temperature=None):
        """ > Node <&Node Blackbody>

        Arguments
        ---------
        - temperature (Float) : socket 'Temperature' (Temperature)

        Returns
        -------
        - Color
        """

        node = Node('Blackbody', {'Temperature': temperature})
        return node._out


    @classmethod
    def clamp(cls, value=None, min=None, max=None, clamp_type='MINMAX'):
        """ > Node <&Node Clamp>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - min (Float) : socket 'Min' (Min)
        - max (Float) : socket 'Max' (Max)
        - clamp_type (str): Node.clamp_type in ('MINMAX', 'RANGE')

        Returns
        -------
        - Float
        """

        node = Node('Clamp', {'Value': value, 'Min': min, 'Max': max}, clamp_type=clamp_type)
        return node._out


    @classmethod
    def combine_xyz(cls, x=None, y=None, z=None):
        """ > Node <&Node Combine XYZ>

        Arguments
        ---------
        - x (Float) : socket 'X' (X)
        - y (Float) : socket 'Y' (Y)
        - z (Float) : socket 'Z' (Z)

        Returns
        -------
        - Vector
        """

        node = Node('Combine XYZ', {'X': x, 'Y': y, 'Z': z})
        return node._out


    @classmethod
    def float_curve(cls, factor=None, value=None, mapping=None):
        """ > Node <&Node Float Curve>

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor)
        - value (Float) : socket 'Value' (Value)
        - mapping (CurveMapping): Node.mapping

        Returns
        -------
        - Float
        """

        node = Node('Float Curve', {'Factor': factor, 'Value': value}, mapping=mapping)
        return node._out


    @classmethod
    def map_range(cls, value=None, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR'):
        """ > Node <&Node Map Range>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - from_min (Float) : socket 'From Min' (From Min)
        - from_max (Float) : socket 'From Max' (From Max)
        - to_min (Float) : socket 'To Min' (To Min)
        - to_max (Float) : socket 'To Max' (To Max)
        - clamp (bool): Node.clamp
        - data_type (str): Node.data_type in ('FLOAT', 'FLOAT_VECTOR')
        - interpolation_type (str): Node.interpolation_type in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')

        Returns
        -------
        - Node
        """

        node = Node('Map Range', {'Value': value, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)
        return node


    @classmethod
    def math(cls, value=None, value_1=None, operation='ADD', use_clamp=False):
        """ > Node <&Node Math>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - value_1 (Float) : socket 'Value' (Value_001)
        - operation (str): Node.operation in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
        - use_clamp (bool): Node.use_clamp

        Returns
        -------
        - Float
        """

        node = Node('Math', {'Value': value, 'Value_001': value_1}, operation=operation, use_clamp=use_clamp)
        return node._out


    @classmethod
    def mix(cls, factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM'):
        """ > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor_Float)
        - a (Float) : socket 'A' (A_Float)
        - b (Float) : socket 'B' (B_Float)
        - blend_type (str): Node.blend_type in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
        - clamp_factor (bool): Node.clamp_factor
        - clamp_result (bool): Node.clamp_result
        - data_type (str): Node.data_type in ('FLOAT', 'VECTOR', 'RGBA', 'ROTATION')
        - factor_mode (str): Node.factor_mode in ('UNIFORM', 'NON_UNIFORM')

        Returns
        -------
        - Node
        """

        node = Node('Mix', {'Factor_Float': factor, 'A_Float': a, 'B_Float': b}, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type=data_type, factor_mode=factor_mode)
        return node


    @classmethod
    def rgb_curves(cls, fac=None, color=None, mapping=None):
        """ > Node <&Node RGB Curves>

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (Fac)
        - color (Color) : socket 'Color' (Color)
        - mapping (CurveMapping): Node.mapping

        Returns
        -------
        - Color
        """

        node = Node('RGB Curves', {'Fac': fac, 'Color': color}, mapping=mapping)
        return node._out


    @classmethod
    def separate_xyz(cls, vector=None):
        """ > Node <&Node Separate XYZ>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)

        Returns
        -------
        - Node
        """

        node = Node('Separate XYZ', {'Vector': vector})
        return node


    @classmethod
    def brick_texture(cls, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None):
        """ > Node <&Node Brick Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - color1 (Color) : socket 'Color1' (Color1)
        - color2 (Color) : socket 'Color2' (Color2)
        - mortar (Color) : socket 'Mortar' (Mortar)
        - scale (Float) : socket 'Scale' (Scale)
        - mortar_size (Float) : socket 'Mortar Size' (Mortar Size)
        - mortar_smooth (Float) : socket 'Mortar Smooth' (Mortar Smooth)
        - bias (Float) : socket 'Bias' (Bias)
        - brick_width (Float) : socket 'Brick Width' (Brick Width)
        - row_height (Float) : socket 'Row Height' (Row Height)
        - color_mapping (ColorMapping): Node.color_mapping
        - offset (float): Node.offset
        - offset_frequency (int): Node.offset_frequency
        - squash (float): Node.squash
        - squash_frequency (int): Node.squash_frequency
        - texture_mapping (TexMapping): Node.texture_mapping

        Returns
        -------
        - Node
        """

        node = Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, color_mapping=color_mapping, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency, texture_mapping=texture_mapping)
        return node


    @classmethod
    def checker_texture(cls, vector=None, color1=None, color2=None, scale=None, color_mapping=None, texture_mapping=None):
        """ > Node <&Node Checker Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - color1 (Color) : socket 'Color1' (Color1)
        - color2 (Color) : socket 'Color2' (Color2)
        - scale (Float) : socket 'Scale' (Scale)
        - color_mapping (ColorMapping): Node.color_mapping
        - texture_mapping (TexMapping): Node.texture_mapping

        Returns
        -------
        - Node
        """

        node = Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale}, color_mapping=color_mapping, texture_mapping=texture_mapping)
        return node


    @classmethod
    def gradient_texture(cls, vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None):
        """ > Node <&Node Gradient Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - color_mapping (ColorMapping): Node.color_mapping
        - gradient_type (str): Node.gradient_type in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
        - texture_mapping (TexMapping): Node.texture_mapping

        Returns
        -------
        - Node
        """

        node = Node('Gradient Texture', {'Vector': vector}, color_mapping=color_mapping, gradient_type=gradient_type, texture_mapping=texture_mapping)
        return node


    @classmethod
    def magic_texture(cls, vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2):
        """ > Node <&Node Magic Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - distortion (Float) : socket 'Distortion' (Distortion)
        - color_mapping (ColorMapping): Node.color_mapping
        - texture_mapping (TexMapping): Node.texture_mapping
        - turbulence_depth (int): Node.turbulence_depth

        Returns
        -------
        - Node
        """

        node = Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion}, color_mapping=color_mapping, texture_mapping=texture_mapping, turbulence_depth=turbulence_depth)
        return node


    @classmethod
    def noise_texture(cls, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, color_mapping=None, noise_dimensions='3D', noise_type='FBM', normalize=True, texture_mapping=None):
        """ > Node <&Node Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - detail (Float) : socket 'Detail' (Detail)
        - roughness (Float) : socket 'Roughness' (Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (Lacunarity)
        - distortion (Float) : socket 'Distortion' (Distortion)
        - color_mapping (ColorMapping): Node.color_mapping
        - noise_dimensions (str): Node.noise_dimensions in ('1D', '2D', '3D', '4D')
        - noise_type (str): Node.noise_type in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
        - normalize (bool): Node.normalize
        - texture_mapping (TexMapping): Node.texture_mapping

        Returns
        -------
        - Node
        """

        node = Node('Noise Texture', {'Vector': vector, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Distortion': distortion}, color_mapping=color_mapping, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize, texture_mapping=texture_mapping)
        return node


    @classmethod
    def voronoi_texture(cls, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, color_mapping=None, distance='EUCLIDEAN', feature='F1', normalize=False, texture_mapping=None, voronoi_dimensions='3D'):
        """ > Node <&Node Voronoi Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - detail (Float) : socket 'Detail' (Detail)
        - roughness (Float) : socket 'Roughness' (Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (Lacunarity)
        - randomness (Float) : socket 'Randomness' (Randomness)
        - color_mapping (ColorMapping): Node.color_mapping
        - distance (str): Node.distance in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
        - feature (str): Node.feature in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
        - normalize (bool): Node.normalize
        - texture_mapping (TexMapping): Node.texture_mapping
        - voronoi_dimensions (str): Node.voronoi_dimensions in ('1D', '2D', '3D', '4D')

        Returns
        -------
        - Node
        """

        node = Node('Voronoi Texture', {'Vector': vector, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Randomness': randomness}, color_mapping=color_mapping, distance=distance, feature=feature, normalize=normalize, texture_mapping=texture_mapping, voronoi_dimensions=voronoi_dimensions)
        return node


    @classmethod
    def wave_texture(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', color_mapping=None, rings_direction='X', texture_mapping=None, wave_profile='SIN', wave_type='BANDS'):
        """ > Node <&Node Wave Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - distortion (Float) : socket 'Distortion' (Distortion)
        - detail (Float) : socket 'Detail' (Detail)
        - detail_scale (Float) : socket 'Detail Scale' (Detail Scale)
        - detail_roughness (Float) : socket 'Detail Roughness' (Detail Roughness)
        - phase_offset (Float) : socket 'Phase Offset' (Phase Offset)
        - bands_direction (str): Node.bands_direction in ('X', 'Y', 'Z', 'DIAGONAL')
        - color_mapping (ColorMapping): Node.color_mapping
        - rings_direction (str): Node.rings_direction in ('X', 'Y', 'Z', 'SPHERICAL')
        - texture_mapping (TexMapping): Node.texture_mapping
        - wave_profile (str): Node.wave_profile in ('SIN', 'SAW', 'TRI')
        - wave_type (str): Node.wave_type in ('BANDS', 'RINGS')

        Returns
        -------
        - Node
        """

        node = Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, color_mapping=color_mapping, rings_direction=rings_direction, texture_mapping=texture_mapping, wave_profile=wave_profile, wave_type=wave_type)
        return node


    @classmethod
    def white_noise_texture(cls, vector=None, noise_dimensions='3D'):
        """ > Node <&Node White Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - noise_dimensions (str): Node.noise_dimensions in ('1D', '2D', '3D', '4D')

        Returns
        -------
        - Node
        """

        node = Node('White Noise Texture', {'Vector': vector}, noise_dimensions=noise_dimensions)
        return node


    @classmethod
    def color_ramp(cls, fac=None, color_ramp=None):
        """ > Node <&Node Color Ramp>

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (Fac)
        - color_ramp (ColorRamp): Node.color_ramp

        Returns
        -------
        - Node
        """

        node = Node('Color Ramp', {'Fac': fac}, color_ramp=color_ramp)
        return node


    @classmethod
    @property
    def value(cls):
        """ > Node <&Node Value>

        Returns
        -------
        - Float
        """

        node = Node('Value')
        return node._out


    @classmethod
    def vector_curves(cls, fac=None, vector=None, mapping=None):
        """ > Node <&Node Vector Curves>

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (Fac)
        - vector (Vector) : socket 'Vector' (Vector)
        - mapping (CurveMapping): Node.mapping

        Returns
        -------
        - Vector
        """

        node = Node('Vector Curves', {'Fac': fac, 'Vector': vector}, mapping=mapping)
        return node._out


    @classmethod
    def vector_math(cls, vector=None, vector_1=None, operation='ADD'):
        """ > Node <&Node Vector Math>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - vector_1 (Vector) : socket 'Vector' (Vector_001)
        - operation (str): Node.operation in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

        Returns
        -------
        - Node
        """

        node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation=operation)
        return node


    @classmethod
    def vector_rotate(cls, vector=None, center=None, axis=None, angle=None, invert=False, rotation_type='AXIS_ANGLE'):
        """ > Node <&Node Vector Rotate>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - center (Vector) : socket 'Center' (Center)
        - axis (Vector) : socket 'Axis' (Axis)
        - angle (Float) : socket 'Angle' (Angle)
        - invert (bool): Node.invert
        - rotation_type (str): Node.rotation_type in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')

        Returns
        -------
        - Vector
        """

        node = Node('Vector Rotate', {'Vector': vector, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type=rotation_type)
        return node._out

    # =============================================================================================================================
    # Blender 4.3
    # - Initial generation with : node_explore.gen_node_code
    # - Manual changes

    @classmethod
    def hash_value(cls, value=None, seed=None, data_type='INT'):
        """ > Node <&Node Hash Value>

        Arguments
        ---------
        - value (Integer) : socket 'Value' (Value)
        - seed (Integer) : socket 'Seed' (Seed)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA')

        Returns
        -------
        - Integer
        """

        node = Node('Hash Value', {'Value': value, 'Seed': seed}, data_type=data_type)
        return node._out

    @classmethod
    def integer_math(cls, value=None, value_1=None, operation='ADD'):
        """ > Node <&Node Integer Math>

        Arguments
        ---------
        - value (Integer) : socket 'Value' (Value)
        - value_1 (Integer) : socket 'Value' (Value_001)
        - operation (str): Node.operation in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM')

        Returns
        -------
        - Integer
        """

        node = Node('Integer Math', [value, value_1], operation=operation)
        return node._out

    @classmethod
    def matrix_determinant(cls, matrix=None):
        """ > Node <&Node Matrix Determinant>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (Matrix)

        Returns
        -------
        - Float
        """

        node = Node('Matrix Determinant', {'Matrix': matrix})
        return node._out

    @classmethod
    def curves_to_grease_pencil(cls, curves=None, instances_as_layers=None):
        """ > Node <&Node Curves to Grease Pencil>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (Curves)
        - selection (Boolean) : socket 'Selection' (Selection)
        - instances_as_layers (Boolean) : socket 'Instances as Layers' (Instances as Layers)

        Returns
        -------
        - Geometry
        """

        node = Node('Curves to Grease Pencil', {'Curves': curves, 'Selection': self._sel, 'Instances as Layers': instances_as_layers})
        return node._out

    @classmethod
    def dial_gizmo(cls, *value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY'):
        """ > Node <&Node Dial Gizmo>

        [&RETURN_NODE]

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - up (Vector) : socket 'Up' (Up)
        - screen_space (Boolean) : socket 'Screen Space' (Screen Space)
        - radius (Float) : socket 'Radius' (Radius)
        - color_id (str): Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None
        node = Node('Dial Gizmo', {'Value': values, 'Position': position, 'Up': up, 'Screen Space': screen_space, 'Radius': radius}, color_id=color_id)
        return node

    @classmethod
    def linear_gizmo(cls, *value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW'):
        """ > Node <&Node Linear Gizmo>

        [&RETURN_NODE]

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - direction (Vector) : socket 'Direction' (Direction)
        - color_id (str): Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')
        - draw_style (str): Node.draw_style in ('ARROW', 'CROSS', 'BOX')

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None
        node = Node('Linear Gizmo', {'Value': values, 'Position': position, 'Direction': direction}, color_id=color_id, draw_style=draw_style)
        return node

    @classmethod
    def transform_gizmo(cls, *value, position=None, rotation=None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True):
        """ > Node <&Node Transform Gizmo>

        [&RETURN_NODE]

        Arguments
        ---------
        - value (Matrix) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - use_rotation_x (bool): Node.use_rotation_x
        - use_rotation_y (bool): Node.use_rotation_y
        - use_rotation_z (bool): Node.use_rotation_z
        - use_scale_x (bool): Node.use_scale_x
        - use_scale_y (bool): Node.use_scale_y
        - use_scale_z (bool): Node.use_scale_z
        - use_translation_x (bool): Node.use_translation_x
        - use_translation_y (bool): Node.use_translation_y
        - use_translation_z (bool): Node.use_translation_z

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None
        node = Node('Transform Gizmo', {'Value': values, 'Position': position, 'Rotation': rotation}, use_rotation_x=use_rotation_x, use_rotation_y=use_rotation_y, use_rotation_z=use_rotation_z, use_scale_x=use_scale_x, use_scale_y=use_scale_y, use_scale_z=use_scale_z, use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)
        return node

    @classmethod
    def grease_pencil_to_curves(cls, grease_pencil=None, layers_as_instances=None):
        """ > Node <&Node Grease Pencil to Curves>

        Arguments
        ---------
        - grease_pencil (Geometry) : socket 'Grease Pencil' (Grease Pencil)
        - selection (Boolean) : socket 'Selection' (Selection)
        - layers_as_instances (Boolean) : socket 'Layers as Instances' (Layers as Instances)

        Returns
        -------
        - Geometry
        """
        node = Node('Grease Pencil to Curves', {'Grease Pencil': grease_pencil, 'Selection': self._sel, 'Layers as Instances': layers_as_instances})
        return node._out

    @classmethod
    def import_obj(cls, path=None):
        """ > Node <&Node Import OBJ>

        Arguments
        ---------
        - path (String) : socket 'Path' (Path)

        Returns
        -------
        - Geometry
        """
        node = Node('Import OBJ', {'Path': path})
        return node._out

    @classmethod
    def import_ply(cls, path=None):
        """ > Node <&Node Import PLY>

        Arguments
        ---------
        - path (String) : socket 'Path' (Path)

        Returns
        -------
        - Geometry
        """
        node = Node('Import PLY', {'Path': path})
        return node._out

    @classmethod
    def import_stl(cls, path=None):
        """ > Node <&Node Import STL>

        Arguments
        ---------
        - path (String) : socket 'Path' (Path)

        Returns
        -------
        - Geometry
        """
        node = Node('Import STL', {'Path': path})
        return node._out

    @classmethod
    def merge_layers(cls, grease_pencil=None, mode='MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        Arguments
        ---------
        - grease_pencil (Geometry) : socket 'Grease Pencil' (Grease Pencil)
        - selection (Boolean) : socket 'Selection' (Selection)
        - mode (str): Node.mode in ('MERGE_BY_NAME', 'MERGE_BY_ID')

        Returns
        -------
        - Geometry
        """
        node = Node('Merge Layers', {'Grease Pencil': grease_pencil, 'Selection': self._sel}, mode=mode)
        return node._out

    @classmethod
    def set_geometry_name(cls, geometry=None, name=None):
        """ > Node <&Node Set Geometry Name>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - name (String) : socket 'Name' (Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Geometry Name', {'Geometry': geometry, 'Name': name})
        return node._out

    @classmethod
    def warning(cls, show=None, message=None, warning_type='ERROR'):
        """ > Node <&Node Warning>

        Arguments
        ---------
        - show (Boolean) : socket 'Show' (Show)
        - message (String) : socket 'Message' (Message)
        - warning_type (str): Node.warning_type

        Returns
        -------
        - Boolean
        """
        node = Node('Warning', {'Show': show, 'Message': message}, warning_type=warning_type)
        return node._out

    @classmethod
    def gabor_texture(cls, vector=None, scale=None, frequency=None, anisotropy=None, orientation=None, gabor_type='2D'):
        """ > Node <&Node Gabor Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - frequency (Float) : socket 'Frequency' (Frequency)
        - anisotropy (Float) : socket 'Anisotropy' (Anisotropy)
        - orientation (Float) : socket 'Orientation' (Orientation 2D)
        - gabor_type (str): Node.gabor_type in ('2D', '3D')

        Returns
        -------
        - Float
        """
        node = Node('Gabor Texture', {'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation': orientation}, gabor_type=gabor_type)
        return node._out
