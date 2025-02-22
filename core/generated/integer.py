from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Integer(Socket):
    """"
    $DOC SET hidden
    """
    def less_than(self, b=None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_THAN'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b=None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b=None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_THAN'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b=None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b=None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b=None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'NOT_EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', sockets={'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def hash_value(self, seed=None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', sockets={'Value': self, 'Seed': seed}, data_type='INT')
        return node._out

    def add(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ADD'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='ADD')
        return node._out

    def subtract(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SUBTRACT'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='SUBTRACT')
        return node._out

    def multiply(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MULTIPLY'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='MULTIPLY')
        return node._out

    def divide(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='DIVIDE')
        return node._out

    def multiply_add(self, multiplier=None, addend=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MULTIPLY_ADD'

        Arguments
        ---------
        - multiplier (Integer) : socket 'Multiplier' (id: Value_001)
        - addend (Integer) : socket 'Addend' (id: Value_002)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD')
        return node._out

    def abs(self):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ABSOLUTE'

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self}, operation='ABSOLUTE')
        return node._out

    def negate(self):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'NEGATE'

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self}, operation='NEGATE')
        return node._out

    def power(self, exponent=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Base' : self
        - Parameter 'operation' : 'POWER'

        Arguments
        ---------
        - exponent (Integer) : socket 'Exponent' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': exponent}, operation='POWER')
        return node._out

    def min(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MINIMUM'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='MINIMUM')
        return node._out

    def max(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MAXIMUM'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='MAXIMUM')
        return node._out

    def sign(self):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SIGN'

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self}, operation='SIGN')
        return node._out

    def divide_round(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE_ROUND'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='DIVIDE_ROUND')
        return node._out

    def divide_floor(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE_FLOOR'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='DIVIDE_FLOOR')
        return node._out

    def divide_ceil(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE_CEIL'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='DIVIDE_CEIL')
        return node._out

    def floored_modulo(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'FLOORED_MODULO'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='FLOORED_MODULO')
        return node._out

    def modulo(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MODULO'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='MODULO')
        return node._out

    def gcd(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'GCD'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='GCD')
        return node._out

    def lcm(self, value=None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'LCM'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', sockets={'Value': self, 'Value_001': value}, operation='LCM')
        return node._out

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        """ > Node <&Node Random Value>

        Information
        -----------
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - min (Integer) : socket 'Min' (id: Min_002)
        - max (Integer) : socket 'Max' (id: Max_002)
        - id (Integer) : socket 'ID' (id: ID)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Random Value', sockets={'Min_002': min, 'Max_002': max, 'ID': id, 'Seed': seed}, data_type='INT')
        return cls(node._out)

    def to_string(self):
        """ > Node <&Node Value to String>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Returns
        -------
        - String
        """
        node = Node('Value to String', sockets={'Value': self}, data_type='INT')
        return node._out

    def blur(self, iterations=None, weight=None):
        """ > Node <&Node Blur Attribute>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Integer
        """
        node = Node('Blur Attribute', sockets={'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='INT')
        return node._out

    @classmethod
    def Named(cls, name=None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Integer
        """
        node = Node('Named Attribute', sockets={'Name': name}, data_type='INT')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name=None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Integer
        """
        node = Node('Named Attribute', sockets={'Name': name}, data_type='INT')
        return cls(node._out)

    def sample_grid(self, position=None, interpolation_mode='TRILINEAR'):
        """ > Node <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation_mode (str): parameter 'interpolation_mode' in ['NEAREST', 'TRILINEAR', 'TRIQUADRATIC']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Sample Grid', 'interpolation_mode', interpolation_mode, 'sample_grid', ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC'))
        node = Node('Sample Grid', sockets={'Grid': self, 'Position': position}, data_type='INT', interpolation_mode=interpolation_mode)
        return node._out

    def sample_grid_index(self, x=None, y=None, z=None):
        """ > Node <&Node Sample Grid Index>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - x (Integer) : socket 'X' (id: X)
        - y (Integer) : socket 'Y' (id: Y)
        - z (Integer) : socket 'Z' (id: Z)

        Returns
        -------
        - Integer
        """
        node = Node('Sample Grid Index', sockets={'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='INT')
        return node._out

