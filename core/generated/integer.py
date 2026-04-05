# Generated 2026-04-05 12:44:34

from __future__ import annotations
from .. sockettype import SocketType
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
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Integer(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def bw_and(self, b: Integer = None):
        """ > Node <&Node Bit Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | A           | `self`  |
        | Parameter | `operation` | `'AND'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B)
        

        Returns
        -------
        Integer
        """
        node = Node('Bit Math', {'A': self, 'B': b}, operation='AND')
        return node._out

    def bw_or(self, b: Integer = None):
        """ > Node <&Node Bit Math>

        **Fixed values**

        | Kind      | Name        | Value  |
        | --------- | ----------- | ------ |
        | Socket    | A           | `self` |
        | Parameter | `operation` | `'OR'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B)
        

        Returns
        -------
        Integer
        """
        node = Node('Bit Math', {'A': self, 'B': b}, operation='OR')
        return node._out

    def bw_xor(self, b: Integer = None):
        """ > Node <&Node Bit Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | A           | `self`  |
        | Parameter | `operation` | `'XOR'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B)
        

        Returns
        -------
        Integer
        """
        node = Node('Bit Math', {'A': self, 'B': b}, operation='XOR')
        return node._out

    def bw_not(self):
        """ > Node <&Node Bit Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | A           | `self`  |
        | Parameter | `operation` | `'NOT'` |

        Returns
        -------
        Integer
        """
        node = Node('Bit Math', {'A': self}, operation='NOT')
        return node._out

    def bw_shift(self, shift: Integer = None):
        """ > Node <&Node Bit Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | A           | `self`    |
        | Parameter | `operation` | `'SHIFT'` |

        Parameters
        ----------
        shift : Integer, optional
            socket 'Shift' (id: Shift)
        

        Returns
        -------
        Integer
        """
        node = Node('Bit Math', {'A': self, 'Shift': shift}, operation='SHIFT')
        return node._out

    def bw_rotate(self, shift: Integer = None):
        """ > Node <&Node Bit Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | A           | `self`     |
        | Parameter | `operation` | `'ROTATE'` |

        Parameters
        ----------
        shift : Integer, optional
            socket 'Shift' (id: Shift)
        

        Returns
        -------
        Integer
        """
        node = Node('Bit Math', {'A': self, 'Shift': shift}, operation='ROTATE')
        return node._out

    def less_than(self, b: Integer = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | A           | `self`        |
        | Parameter | `data_type` | `'INT'`       |
        | Parameter | `mode`      | `'ELEMENT'`   |
        | Parameter | `operation` | `'LESS_THAN'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B_INT)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | A           | `self`         |
        | Parameter | `data_type` | `'INT'`        |
        | Parameter | `mode`      | `'ELEMENT'`    |
        | Parameter | `operation` | `'LESS_EQUAL'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B_INT)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b: Integer = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | A           | `self`           |
        | Parameter | `data_type` | `'INT'`          |
        | Parameter | `mode`      | `'ELEMENT'`      |
        | Parameter | `operation` | `'GREATER_THAN'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B_INT)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | A           | `self`            |
        | Parameter | `data_type` | `'INT'`           |
        | Parameter | `mode`      | `'ELEMENT'`       |
        | Parameter | `operation` | `'GREATER_EQUAL'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B_INT)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | A           | `self`      |
        | Parameter | `data_type` | `'INT'`     |
        | Parameter | `mode`      | `'ELEMENT'` |
        | Parameter | `operation` | `'EQUAL'`   |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B_INT)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | A           | `self`        |
        | Parameter | `data_type` | `'INT'`       |
        | Parameter | `mode`      | `'ELEMENT'`   |
        | Parameter | `operation` | `'NOT_EQUAL'` |

        Parameters
        ----------
        b : Integer, optional
            socket 'B' (id: B_INT)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='INT')
        return node._out

    def add(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `operation` | `'ADD'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='ADD')
        return node._out

    def subtract(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Value       | `self`       |
        | Parameter | `operation` | `'SUBTRACT'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='SUBTRACT')
        return node._out

    def multiply(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Value       | `self`       |
        | Parameter | `operation` | `'MULTIPLY'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MULTIPLY')
        return node._out

    def divide(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `operation` | `'DIVIDE'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE')
        return node._out

    def multiply_add(self, multiplier: Integer = None, addend: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | Value       | `self`           |
        | Parameter | `operation` | `'MULTIPLY_ADD'` |

        Parameters
        ----------
        multiplier : Integer, optional
            socket 'Multiplier' (id: Value_001)
        
        addend : Integer, optional
            socket 'Addend' (id: Value_002)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD')
        return node._out

    def abs(self):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Value       | `self`       |
        | Parameter | `operation` | `'ABSOLUTE'` |

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self}, operation='ABSOLUTE')
        return node._out

    def negate(self):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `operation` | `'NEGATE'` |

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self}, operation='NEGATE')
        return node._out

    def power(self, exponent: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Base        | `self`    |
        | Parameter | `operation` | `'POWER'` |

        Parameters
        ----------
        exponent : Integer, optional
            socket 'Exponent' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': exponent}, operation='POWER')
        return node._out

    def min(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Value       | `self`      |
        | Parameter | `operation` | `'MINIMUM'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MINIMUM')
        return node._out

    def max(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Value       | `self`      |
        | Parameter | `operation` | `'MAXIMUM'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MAXIMUM')
        return node._out

    def sign(self):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Value       | `self`   |
        | Parameter | `operation` | `'SIGN'` |

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self}, operation='SIGN')
        return node._out

    def divide_round(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | Value       | `self`           |
        | Parameter | `operation` | `'DIVIDE_ROUND'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE_ROUND')
        return node._out

    def divide_floor(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | Value       | `self`           |
        | Parameter | `operation` | `'DIVIDE_FLOOR'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE_FLOOR')
        return node._out

    def divide_ceil(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value           |
        | --------- | ----------- | --------------- |
        | Socket    | Value       | `self`          |
        | Parameter | `operation` | `'DIVIDE_CEIL'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE_CEIL')
        return node._out

    def floored_modulo(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value              |
        | --------- | ----------- | ------------------ |
        | Socket    | Value       | `self`             |
        | Parameter | `operation` | `'FLOORED_MODULO'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='FLOORED_MODULO')
        return node._out

    def modulo(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `operation` | `'MODULO'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MODULO')
        return node._out

    def gcd(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `operation` | `'GCD'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='GCD')
        return node._out

    def lcm(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `operation` | `'LCM'` |

        Parameters
        ----------
        value : Integer, optional
            socket 'Value' (id: Value_001)
        

        Returns
        -------
        Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='LCM')
        return node._out

    @classmethod
    def Random(cls,
                    min: Integer = None,
                    max: Integer = None,
                    id: Integer = None,
                    seed: Integer = None):
        """ > Node <&Node Random Value>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        min : Integer, optional
            socket 'Min' (id: Min_002)
        
        max : Integer, optional
            socket 'Max' (id: Max_002)
        
        id : Integer, optional
            socket 'ID' (id: ID)
        
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Integer
        """
        node = Node('Random Value', {'Min_002': min, 'Max_002': max, 'ID': id, 'Seed': seed}, data_type='INT')
        return cls(node._out)

    def to_string(self):
        """ > Node <&Node Value to String>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Returns
        -------
        String
        """
        node = Node('Value to String', {'Value': self}, data_type='INT')
        return node._out

    def blur(self, iterations: Integer = None, weight: Float = None):
        """ > Node <&Node Blur Attribute>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Integer
        """
        node = Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='INT')
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Integer
        """
        node = Node('Named Attribute', {'Name': name}, data_type='INT')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Integer
        """
        node = Node('Named Attribute', {'Name': name}, data_type='INT')
        return cls(node._out)

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        interpolation : menu='Trilinear', optional
            ('Nearest Neighbor', 'Trilinear', 'Triquadratic')
        

        Returns
        -------
        Integer
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='INT')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        x : Integer, optional
            socket 'X' (id: X)
        
        y : Integer, optional
            socket 'Y' (id: Y)
        
        z : Integer, optional
            socket 'Z' (id: Z)
        

        Returns
        -------
        Integer
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='INT')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Topology    | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        None
        """
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='INT', **sockets)
        return node._out

    def advect_grid(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None):
        """ > Node <&Node Advect Grid>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        velocity : Vector, optional
            socket 'Velocity' (id: Velocity)
        
        time_step : Float, optional
            socket 'Time Step' (id: Time Step)
        
        integration_scheme : menu='Runge-Kutta 3', optional
            ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
        
        limiter : menu='Clamp', optional
            ('None', 'Clamp', 'Revert')
        

        Returns
        -------
        Integer
        """
        node = Node('Advect Grid', {'Grid': self, 'Velocity': velocity, 'Time Step': time_step, 'Integration Scheme': integration_scheme, 'Limiter': limiter}, data_type='INT')
        return node._out

    def prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Integer = None):
        """ > Node <&Node Prune Grid>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        mode : menu='Threshold', optional
            ('Inactive', 'Threshold', 'SDF')
        
        threshold : Integer, optional
            socket 'Threshold' (id: Threshold)
        

        Returns
        -------
        Integer
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode, 'Threshold': threshold}, data_type='INT')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Returns
        -------
        Integer
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='INT')
        return node._out

    @classmethod
    def voxel_index(cls):
        """ > Node <&Node Voxel Index>

        Returns
        -------
        Integer
            peer sockets: y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_x_ (Integer), extent_y_ (Integer), extent_z_ (Integer)

        """
        node = Node('Voxel Index', )
        return node._out

    def set_grid_background(self, background: Integer = None, update_inactive: Boolean = None):
        """ > Node <&Node Set Grid Background>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        background : Integer, optional
            socket 'Background' (id: Background)
        
        update_inactive : Boolean, optional
            socket 'Update Inactive' (id: Update Inactive)
        

        Returns
        -------
        Integer
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background, 'Update Inactive': update_inactive}, data_type='INT')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        transform : Matrix, optional
            socket 'Transform' (id: Transform)
        

        Returns
        -------
        Boolean
            peer sockets: grid_ (Integer)

        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='INT')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Returns
        -------
        Matrix
            peer sockets: background_value_ (Integer)

        """
        node = Node('Grid Info', {'Grid': self}, data_type='INT')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Value       | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Integer
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='INT')
        return node._out

    def clip_grid(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None):
        """ > Node <&Node Clip Grid>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        min_x : Integer, optional
            socket 'Min X' (id: Min X)
        
        min_y : Integer, optional
            socket 'Min Y' (id: Min Y)
        
        min_z : Integer, optional
            socket 'Min Z' (id: Min Z)
        
        max_x : Integer, optional
            socket 'Max X' (id: Max X)
        
        max_y : Integer, optional
            socket 'Max Y' (id: Max Y)
        
        max_z : Integer, optional
            socket 'Max Z' (id: Max Z)
        

        Returns
        -------
        Integer
        """
        node = Node('Clip Grid', {'Grid': self, 'Min X': min_x, 'Min Y': min_y, 'Min Z': min_z, 'Max X': max_x, 'Max Y': max_y, 'Max Z': max_z}, data_type='INT')
        return node._out

    def grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None):
        """ > Node <&Node Grid Dilate & Erode>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        connectivity : menu='Face', optional
            ('Face', 'Edge', 'Vertex')
        
        tiles : menu='Preserve', optional
            ('Ignore', 'Expand', 'Preserve')
        
        steps : Integer, optional
            socket 'Steps' (id: Steps)
        

        Returns
        -------
        Integer
        """
        node = Node('Grid Dilate & Erode', {'Grid': self, 'Connectivity': connectivity, 'Tiles': tiles, 'Steps': steps}, data_type='INT')
        return node._out

    def grid_mean(self, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node Grid Mean>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        width : Integer, optional
            socket 'Width' (id: Width)
        
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        

        Returns
        -------
        Integer
        """
        node = Node('Grid Mean', {'Grid': self, 'Width': width, 'Iterations': iterations}, data_type='INT')
        return node._out

    def grid_median(self, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node Grid Median>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Parameters
        ----------
        width : Integer, optional
            socket 'Width' (id: Width)
        
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        

        Returns
        -------
        Integer
        """
        node = Node('Grid Median', {'Grid': self, 'Width': width, 'Iterations': iterations}, data_type='INT')
        return node._out

    def grid_to_points(self):
        """ > Node <&Node Grid to Points>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Grid        | `self`  |
        | Parameter | `data_type` | `'INT'` |

        Returns
        -------
        Cloud
            peer sockets: value_ (Integer), x_ (Integer), y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_ (Integer)

        """
        node = Node('Grid to Points', {'Grid': self}, data_type='INT')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = 0,
        name: str = 'Integer',
        min: int = -2147483648,
        max: int = 2147483647,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INDEX', 'ID_OR_INDEX'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
        subtype: str = 'NONE',
         ):
        """ > Integer Input

        New <#Integer> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`0`
            Default value

        name : str, default=`Integer`
            Input socket name

        min : int, default=`-2147483648`
            Property min_value

        max : int, default=`2147483647`
            Property max_value

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')

        subtype : str, default=`NONE`
            Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR')


        Returns
        -------
        Integer
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketInt', default_value = defval, name=name,
            min=min, max=max, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype=subtype)

    @classmethod
    def Percentage(cls,
        value: object = 0,
        name: str = 'Percentage',
        min: int = -2147483648,
        max: int = 2147483647,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INDEX', 'ID_OR_INDEX'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Percentage Input

        New <#Integer> input with subtype 'PERCENTAGE'.

        Parameters
        ----------
        value : object, default=`0`
            Default value

        name : str, default=`Percentage`
            Input socket name

        min : int, default=`-2147483648`
            Property min_value

        max : int, default=`2147483647`
            Property max_value

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Integer
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default_attribute=default_attribute, default_input=default_input, shape=shape, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls,
        value: object = 0,
        name: str = 'Factor',
        min: int = -2147483648,
        max: int = 2147483647,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INDEX', 'ID_OR_INDEX'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Factor Input

        New <#Integer> input with subtype 'FACTOR'.

        Parameters
        ----------
        value : object, default=`0`
            Default value

        name : str, default=`Factor`
            Input socket name

        min : int, default=`-2147483648`
            Property min_value

        max : int, default=`2147483647`
            Property max_value

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Integer
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default_attribute=default_attribute, default_input=default_input, shape=shape, subtype='FACTOR')

