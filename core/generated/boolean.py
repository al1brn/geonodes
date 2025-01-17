from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Boolean(Socket):
    """"
    $DOC SET hidden
    """
    def band(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='AND')
        return node._out

    def bor(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='OR')
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
        node = Node('Boolean Math', sockets={'Boolean': self}, operation='NOT')
        return node._out

    def not_and(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='NAND')
        return node._out

    def nor(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='NOR')
        return node._out

    def xnor(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='XNOR')
        return node._out

    def xor(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='XOR')
        return node._out

    def imply(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='IMPLY')
        return node._out

    def nimply(self, boolean=None):
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
        node = Node('Boolean Math', sockets={'Boolean': self, 'Boolean_001': boolean}, operation='NIMPLY')
        return node._out

    @classmethod
    def Random(cls, probability=None, id=None, seed=None):
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
        node = Node('Random Value', sockets={'Probability': probability, 'ID': id, 'Seed': seed}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    def Named(cls, name=None):
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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name=None):
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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    @property
    def is_viewport(cls):
        """ > Node <&Node Is Viewport>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Viewport', sockets={})
        return node._out

    def sample_grid(self, position=None, interpolation_mode='TRILINEAR'):
        """ > Node <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation_mode (str): parameter 'interpolation_mode' in ['NEAREST', 'TRILINEAR', 'TRIQUADRATIC']

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Sample Grid', 'interpolation_mode', interpolation_mode, 'sample_grid', ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC'))
        node = Node('Sample Grid', sockets={'Grid': self, 'Position': position}, data_type='BOOLEAN', interpolation_mode=interpolation_mode)
        return node._out

    def sample_grid_index(self, x=None, y=None, z=None):
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
        node = Node('Sample Grid Index', sockets={'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='BOOLEAN')
        return node._out

    def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """ > Node <&Node UV Unwrap>

        Information
        -----------
        - Socket 'Selection' : self

        Arguments
        ---------
        - seam (Boolean) : socket 'Seam' (id: Seam)
        - margin (Float) : socket 'Margin' (id: Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (id: Fill Holes)
        - method (str): parameter 'method' in ['ANGLE_BASED', 'CONFORMAL']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('UV Unwrap', 'method', method, 'uv_unwrap', ('ANGLE_BASED', 'CONFORMAL'))
        node = Node('UV Unwrap', sockets={'Selection': self, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)
        return node._out

    def error(self, message=None):
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
        node = Node('Warning', sockets={'Show': self, 'Message': message}, warning_type='ERROR')
        return node._out

    def warning(self, message=None):
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
        node = Node('Warning', sockets={'Show': self, 'Message': message}, warning_type='WARNING')
        return node._out

    def info(self, message=None):
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
        node = Node('Warning', sockets={'Show': self, 'Message': message}, warning_type='INFO')
        return node._out

