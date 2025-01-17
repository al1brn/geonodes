from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Rotation(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def AlignToVector(cls, vector=None, factor=None, axis='Z', pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': None, 'Vector': vector, 'Factor': factor}, axis=axis, pivot_axis=pivot_axis)
        return cls(node._out)

    @classmethod
    def AlignXToVector(cls, vector=None, factor=None, pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': None, 'Vector': vector, 'Factor': factor}, axis='X', pivot_axis=pivot_axis)
        return cls(node._out)

    @classmethod
    def AlignYToVector(cls, vector=None, factor=None, pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': None, 'Vector': vector, 'Factor': factor}, axis='Y', pivot_axis=pivot_axis)
        return cls(node._out)

    @classmethod
    def AlignZToVector(cls, vector=None, factor=None, pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': None, 'Vector': vector, 'Factor': factor}, axis='Z', pivot_axis=pivot_axis)
        return cls(node._out)

    def align_toVector(self, vector=None, factor=None, axis='Z', pivot_axis='AUTO'):
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
        utils.check_enum_arg('Align Rotation to Vector', 'axis', axis, 'align_toVector', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'align_toVector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', sockets={'Rotation': self, 'Vector': vector, 'Factor': factor}, axis=axis, pivot_axis=pivot_axis)
        return node._out

    def align_x_to_vector(self, vector=None, factor=None, pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': self, 'Vector': vector, 'Factor': factor}, axis='X', pivot_axis=pivot_axis)
        return node._out

    def align_y_to_vector(self, vector=None, factor=None, pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': self, 'Vector': vector, 'Factor': factor}, axis='Y', pivot_axis=pivot_axis)
        return node._out

    def align_z_to_vector(self, vector=None, factor=None, pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': self, 'Vector': vector, 'Factor': factor}, axis='Z', pivot_axis=pivot_axis)
        return node._out

    @classmethod
    def FromAxes(cls, primary_axis_1=None, secondary_axis_1=None, primary_axis='Z', secondary_axis='X'):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis_1, 'Secondary Axis': secondary_axis_1}, primary_axis=primary_axis, secondary_axis=secondary_axis)
        return cls(node._out)

    @classmethod
    def FromXYAxes(cls, primary_axis=None, secondary_axis=None):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='X', secondary_axis='Y')
        return cls(node._out)

    @classmethod
    def FromYXAxes(cls, primary_axis=None, secondary_axis=None):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Y', secondary_axis='X')
        return cls(node._out)

    @classmethod
    def FromXZAxes(cls, primary_axis=None, secondary_axis=None):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='X', secondary_axis='Z')
        return cls(node._out)

    @classmethod
    def FromZXAxes(cls, primary_axis=None, secondary_axis=None):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Z', secondary_axis='X')
        return cls(node._out)

    @classmethod
    def FromYZAxes(cls, primary_axis=None, secondary_axis=None):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Y', secondary_axis='Z')
        return cls(node._out)

    @classmethod
    def FromZYAxes(cls, primary_axis=None, secondary_axis=None):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis='Z', secondary_axis='Y')
        return cls(node._out)

    @classmethod
    def FromAxisAngle(cls, axis=None, angle=None):
        """ > Node <&Node Axis Angle to Rotation>

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)

        Returns
        -------
        - Rotation
        """
        node = Node('Axis Angle to Rotation', sockets={'Axis': axis, 'Angle': angle})
        return cls(node._out)

    @classmethod
    def FromEuler(cls, euler=None):
        """ > Node <&Node Euler to Rotation>

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (id: Euler)

        Returns
        -------
        - Rotation
        """
        node = Node('Euler to Rotation', sockets={'Euler': euler})
        return cls(node._out)

    def hash_value(self, seed=None):
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
        node = Node('Hash Value', sockets={'Value': self, 'Seed': seed}, data_type='ROTATION')
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
        node = Node('Invert Rotation', sockets={'Rotation': self})
        return node._out

    @classmethod
    def FromQuaternion(cls, w=None, x=None, y=None, z=None):
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
        node = Node('Quaternion to Rotation', sockets={'W': w, 'X': x, 'Y': y, 'Z': z})
        return cls(node._out)

    def rotate(self, rotate_by=None, rotation_space='GLOBAL'):
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
        node = Node('Rotate Rotation', sockets={'Rotation': self, 'Rotate By': rotate_by}, rotation_space=rotation_space)
        return node._out

    def rotate_global(self, rotate_by=None):
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
        node = Node('Rotate Rotation', sockets={'Rotation': self, 'Rotate By': rotate_by}, rotation_space='GLOBAL')
        return node._out

    def rotate_local(self, rotate_by=None):
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
        node = Node('Rotate Rotation', sockets={'Rotation': self, 'Rotate By': rotate_by}, rotation_space='LOCAL')
        return node._out

    def rotate_vector(self, vector=None):
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
        node = Node('Rotate Vector', sockets={'Vector': vector, 'Rotation': self})
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
        node = Node('Rotation to Axis Angle', sockets={'Rotation': self})
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
        node = Node('Rotation to Axis Angle', sockets={'Rotation': self})
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
        node = Node('Rotation to Euler', sockets={'Rotation': self})
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
        node = Node('Rotation to Quaternion', sockets={'Rotation': self})
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
        node = Node('Rotation to Quaternion', sockets={'Rotation': self})
        return (node.w, node.x, node.y, node.z)

    @classmethod
    def Named(cls, name=None):
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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='QUATERNION')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name=None):
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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='QUATERNION')
        return cls(node._out)

    def mix(self, b=None, factor=None, clamp_factor=True):
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
        node = Node('Mix', sockets={'A_Rotation': self, 'B_Rotation': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='ROTATION', factor_mode='UNIFORM')
        return node._out

