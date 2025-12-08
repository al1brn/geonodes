# Generated 2025-12-08 09:52:50

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


class Rotation(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def AlignToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : ignored

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - axis (str): parameter 'axis' in ['X', 'Y', 'Z']
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'axis', axis, 'AlignToVector', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'AlignToVector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': None, 'Vector': vector, 'Factor': factor}, axis=axis, pivot_axis=pivot_axis)
        return cls(node._out)

    @classmethod
    def AlignXToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : ignored
        - Parameter 'axis' : 'X'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'AlignXToVector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': None, 'Vector': vector, 'Factor': factor}, axis='X', pivot_axis=pivot_axis)
        return cls(node._out)

    @classmethod
    def AlignYToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : ignored
        - Parameter 'axis' : 'Y'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'AlignYToVector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': None, 'Vector': vector, 'Factor': factor}, axis='Y', pivot_axis=pivot_axis)
        return cls(node._out)

    @classmethod
    def AlignZToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : ignored
        - Parameter 'axis' : 'Z'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'AlignZToVector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': None, 'Vector': vector, 'Factor': factor}, axis='Z', pivot_axis=pivot_axis)
        return cls(node._out)

    def align_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : self

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - axis (str): parameter 'axis' in ['X', 'Y', 'Z']
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'axis', axis, 'align_to_vector', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'align_to_vector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': self, 'Vector': vector, 'Factor': factor}, axis=axis, pivot_axis=pivot_axis)
        return node._out

    def align_x_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : self
        - Parameter 'axis' : 'X'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'align_x_to_vector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': self, 'Vector': vector, 'Factor': factor}, axis='X', pivot_axis=pivot_axis)
        return node._out

    def align_y_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : self
        - Parameter 'axis' : 'Y'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'align_y_to_vector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': self, 'Vector': vector, 'Factor': factor}, axis='Y', pivot_axis=pivot_axis)
        return node._out

    def align_z_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Information
        -----------
        - Socket 'Rotation' : self
        - Parameter 'axis' : 'Z'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'align_z_to_vector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': self, 'Vector': vector, 'Factor': factor}, axis='Z', pivot_axis=pivot_axis)
        return node._out

    @classmethod
    def FromAxes(cls,
                    primary_axis_1: Vector = None,
                    secondary_axis_1: Vector = None,
                    primary_axis: Literal['X', 'Y', 'Z'] = 'Z',
                    secondary_axis: Literal['X', 'Y', 'Z'] = 'X'):
        """ > Node <&Node Axes to Rotation>

        Arguments
        ---------
        - primary_axis_1 (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis_1 (Vector) : socket 'Secondary Axis' (id: Secondary Axis)
        - primary_axis (str): parameter 'primary_axis' in ['X', 'Y', 'Z']
        - secondary_axis (str): parameter 'secondary_axis' in ['X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Axes to Rotation', 'primary_axis', primary_axis, 'FromAxes', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Axes to Rotation', 'secondary_axis', secondary_axis, 'FromAxes', ('X', 'Y', 'Z'))
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis_1, 'Secondary Axis': secondary_axis_1}, primary_axis=primary_axis, secondary_axis=secondary_axis)
        return cls(node._out)

    @classmethod
    def FromXYAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None):
        """ > Node <&Node Axes to Rotation>

        Information
        -----------
        - Parameter 'primary_axis' : 'X'
        - Parameter 'secondary_axis' : 'Y'

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (id: Secondary Axis)

        Returns
        -------
        - Rotation
        """
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='X', secondary_axis='Y')
        return cls(node._out)

    @classmethod
    def FromYXAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None):
        """ > Node <&Node Axes to Rotation>

        Information
        -----------
        - Parameter 'primary_axis' : 'Y'
        - Parameter 'secondary_axis' : 'X'

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (id: Secondary Axis)

        Returns
        -------
        - Rotation
        """
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Y', secondary_axis='X')
        return cls(node._out)

    @classmethod
    def FromXZAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None):
        """ > Node <&Node Axes to Rotation>

        Information
        -----------
        - Parameter 'primary_axis' : 'X'
        - Parameter 'secondary_axis' : 'Z'

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (id: Secondary Axis)

        Returns
        -------
        - Rotation
        """
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='X', secondary_axis='Z')
        return cls(node._out)

    @classmethod
    def FromZXAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None):
        """ > Node <&Node Axes to Rotation>

        Information
        -----------
        - Parameter 'primary_axis' : 'Z'
        - Parameter 'secondary_axis' : 'X'

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (id: Secondary Axis)

        Returns
        -------
        - Rotation
        """
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Z', secondary_axis='X')
        return cls(node._out)

    @classmethod
    def FromYZAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None):
        """ > Node <&Node Axes to Rotation>

        Information
        -----------
        - Parameter 'primary_axis' : 'Y'
        - Parameter 'secondary_axis' : 'Z'

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (id: Secondary Axis)

        Returns
        -------
        - Rotation
        """
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Y', secondary_axis='Z')
        return cls(node._out)

    @classmethod
    def FromZYAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None):
        """ > Node <&Node Axes to Rotation>

        Information
        -----------
        - Parameter 'primary_axis' : 'Z'
        - Parameter 'secondary_axis' : 'Y'

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (id: Secondary Axis)

        Returns
        -------
        - Rotation
        """
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Z', secondary_axis='Y')
        return cls(node._out)

    @classmethod
    def FromAxisAngle(cls, axis: Vector = None, angle: Float = None):
        """ > Node <&Node Axis Angle to Rotation>

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)

        Returns
        -------
        - Rotation
        """
        node = Node('Axis Angle to Rotation', {'Axis': axis, 'Angle': angle})
        return cls(node._out)

    @classmethod
    def FromEuler(cls, euler: Vector = None):
        """ > Node <&Node Euler to Rotation>

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (id: Euler)

        Returns
        -------
        - Rotation
        """
        node = Node('Euler to Rotation', {'Euler': euler})
        return cls(node._out)

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'ROTATION'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='ROTATION')
        return node._out

    def invert(self):
        """ > Node <&Node Invert Rotation>

        Information
        -----------
        - Socket 'Rotation' : self

        Returns
        -------
        - Rotation
        """
        node = Node('Invert Rotation', {'Rotation': self})
        return node._out

    @classmethod
    def FromQuaternion(cls, w: Float = None, x: Float = None, y: Float = None, z: Float = None):
        """ > Node <&Node Quaternion to Rotation>

        Arguments
        ---------
        - w (Float) : socket 'W' (id: W)
        - x (Float) : socket 'X' (id: X)
        - y (Float) : socket 'Y' (id: Y)
        - z (Float) : socket 'Z' (id: Z)

        Returns
        -------
        - Rotation
        """
        node = Node('Quaternion to Rotation', {'W': w, 'X': x, 'Y': y, 'Z': z})
        return cls(node._out)

    def rotate(self,
                    rotate_by: Rotation = None,
                    rotation_space: Literal['GLOBAL', 'LOCAL'] = 'GLOBAL'):
        """ > Node <&Node Rotate Rotation>

        Information
        -----------
        - Socket 'Rotation' : self

        Arguments
        ---------
        - rotate_by (Rotation) : socket 'Rotate By' (id: Rotate By)
        - rotation_space (str): parameter 'rotation_space' in ['GLOBAL', 'LOCAL']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Rotate Rotation', 'rotation_space', rotation_space, 'rotate', ('GLOBAL', 'LOCAL'))
        node = Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space=rotation_space)
        return node._out

    def rotate_global(self, rotate_by: Rotation = None):
        """ > Node <&Node Rotate Rotation>

        Information
        -----------
        - Socket 'Rotation' : self
        - Parameter 'rotation_space' : 'GLOBAL'

        Arguments
        ---------
        - rotate_by (Rotation) : socket 'Rotate By' (id: Rotate By)

        Returns
        -------
        - Rotation
        """
        node = Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space='GLOBAL')
        return node._out

    def rotate_local(self, rotate_by: Rotation = None):
        """ > Node <&Node Rotate Rotation>

        Information
        -----------
        - Socket 'Rotation' : self
        - Parameter 'rotation_space' : 'LOCAL'

        Arguments
        ---------
        - rotate_by (Rotation) : socket 'Rotate By' (id: Rotate By)

        Returns
        -------
        - Rotation
        """
        node = Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space='LOCAL')
        return node._out

    def rotate_vector(self, vector: Vector = None):
        """ > Node <&Node Rotate Vector>

        Information
        -----------
        - Socket 'Rotation' : self

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)

        Returns
        -------
        - Vector
        """
        node = Node('Rotate Vector', {'Vector': vector, 'Rotation': self})
        return node._out

    def to_axis_angle(self):
        """ > Node <&Node Rotation to Axis Angle>

        Information
        -----------
        - Socket 'Rotation' : self

        Returns
        -------
        - Vector [angle_ (Float)]
        """
        node = Node('Rotation to Axis Angle', {'Rotation': self})
        return node._out

    @property
    def axis_angle(self):
        """ > Node <&Node Rotation to Axis Angle>

        Information
        -----------
        - Socket 'Rotation' : self

        Returns
        -------
        - tuple (Vector, Float)
        """
        node = Node('Rotation to Axis Angle', {'Rotation': self})
        return (node.axis, node.angle)

    def to_euler(self):
        """ > Node <&Node Rotation to Euler>

        Information
        -----------
        - Socket 'Rotation' : self

        Returns
        -------
        - Vector
        """
        node = Node('Rotation to Euler', {'Rotation': self})
        return node._out

    def to_quaternion(self):
        """ > Node <&Node Rotation to Quaternion>

        Information
        -----------
        - Socket 'Rotation' : self

        Returns
        -------
        - Float [x_ (Float), y_ (Float), z_ (Float)]
        """
        node = Node('Rotation to Quaternion', {'Rotation': self})
        return node._out

    @property
    def wxyz(self):
        """ > Node <&Node Rotation to Quaternion>

        Information
        -----------
        - Socket 'Rotation' : self

        Returns
        -------
        - tuple (Float, Float, Float, Float)
        """
        node = Node('Rotation to Quaternion', {'Rotation': self})
        return (node.w, node.x, node.y, node.z)

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'QUATERNION'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Rotation
        """
        node = Node('Named Attribute', {'Name': name}, data_type='QUATERNION')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'QUATERNION'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Rotation
        """
        node = Node('Named Attribute', {'Name': name}, data_type='QUATERNION')
        return cls(node._out)

    def mix(self, b: Rotation = None, factor: Float = None, clamp_factor = True):
        """ > Node <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'ROTATION'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Rotation) : socket 'B' (id: B_Rotation)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'

        Returns
        -------
        - Rotation
        """
        node = Node('Mix', {'A_Rotation': self, 'B_Rotation': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='ROTATION', factor_mode='UNIFORM')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'ROTATION'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Rotation
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='ROTATION')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = (0, 0, 0),
        name: str = 'Rotation',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        shape: Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE'] = 'AUTO',
         ):
        """ > Rotation Input

        New <#Rotation> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Rotation') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE')

        Returns
        -------
        - Rotation
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketRotation', default_value = defval,
            name=name, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default_attribute=default_attribute, shape=shape)

