# Generated 2026-04-04 17:31:31

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


class Vector(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def less_than(self, b: Vector = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | A           | `self`        |
        | Parameter | `data_type` | `'VECTOR'`    |
        | Parameter | `mode`      | `'ELEMENT'`   |
        | Parameter | `operation` | `'LESS_THAN'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_VEC3)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b: Vector = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | A           | `self`         |
        | Parameter | `data_type` | `'VECTOR'`     |
        | Parameter | `mode`      | `'ELEMENT'`    |
        | Parameter | `operation` | `'LESS_EQUAL'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_VEC3)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b: Vector = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | A           | `self`           |
        | Parameter | `data_type` | `'VECTOR'`       |
        | Parameter | `mode`      | `'ELEMENT'`      |
        | Parameter | `operation` | `'GREATER_THAN'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_VEC3)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b: Vector = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | A           | `self`            |
        | Parameter | `data_type` | `'VECTOR'`        |
        | Parameter | `mode`      | `'ELEMENT'`       |
        | Parameter | `operation` | `'GREATER_EQUAL'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_VEC3)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b: Vector = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | A           | `self`      |
        | Parameter | `data_type` | `'VECTOR'`  |
        | Parameter | `mode`      | `'ELEMENT'` |
        | Parameter | `operation` | `'EQUAL'`   |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_VEC3)
        
        epsilon : Float, optional
            socket 'Epsilon' (id: Epsilon)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b, 'Epsilon': epsilon}, data_type='VECTOR', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: Vector = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | A           | `self`        |
        | Parameter | `data_type` | `'VECTOR'`    |
        | Parameter | `mode`      | `'ELEMENT'`   |
        | Parameter | `operation` | `'NOT_EQUAL'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_VEC3)
        
        epsilon : Float, optional
            socket 'Epsilon' (id: Epsilon)
        

        Returns
        -------
        Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b, 'Epsilon': epsilon}, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def to_rotation(self):
        """ > Node <&Node Euler to Rotation>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Euler | `self` |

        Returns
        -------
        Rotation
        """
        node = Node('Euler to Rotation', {'Euler': self})
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='VECTOR')
        return node._out

    @classmethod
    def Random(cls,
                    min: Vector = None,
                    max: Vector = None,
                    id: Integer = None,
                    seed: Integer = None):
        """ > Node <&Node Random Value>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Parameter | `data_type` | `'FLOAT_VECTOR'` |

        Parameters
        ----------
        min : Vector, optional
            socket 'Min' (id: Min)
        
        max : Vector, optional
            socket 'Max' (id: Max)
        
        id : Integer, optional
            socket 'ID' (id: ID)
        
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Vector
        """
        node = Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    def blur(self, iterations: Integer = None, weight: Float = None):
        """ > Node <&Node Blur Attribute>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | Value       | `self`           |
        | Parameter | `data_type` | `'FLOAT_VECTOR'` |

        Parameters
        ----------
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Vector
        """
        node = Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='FLOAT_VECTOR')
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Parameter | `data_type` | `'FLOAT_VECTOR'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Vector
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Parameter | `data_type` | `'FLOAT_VECTOR'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Vector
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    def pack_uv_islands(self,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None):
        """ > Node <&Node Pack UV Islands>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | UV        | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        margin : Float, optional
            socket 'Margin' (id: Margin)
        
        rotate : Boolean, optional
            socket 'Rotate' (id: Rotate)
        
        method : menu='Bounding Box', optional
            ('Bounding Box', 'Convex Hull', 'Exact Shape')
        
        bottom_left : Vector, optional
            socket 'Bottom Left' (id: Bottom Left)
        
        top_right : Vector, optional
            socket 'Top Right' (id: Top Right)
        

        Returns
        -------
        Vector
        """
        node = Node('Pack UV Islands', {'UV': self, 'Selection': self.get_selection(), 'Margin': margin, 'Rotate': rotate, 'Method': method, 'Bottom Left': bottom_left, 'Top Right': top_right})
        return node._out

    @classmethod
    def CombineXYZ(cls, x: Float = None, y: Float = None, z: Float = None):
        """ > Node <&Node Combine XYZ>

        Parameters
        ----------
        x : Float, optional
            socket 'X' (id: X)
        
        y : Float, optional
            socket 'Y' (id: Y)
        
        z : Float, optional
            socket 'Z' (id: Z)
        

        Returns
        -------
        Vector
        """
        node = Node('Combine XYZ', {'X': x, 'Y': y, 'Z': z})
        return cls(node._out)

    def map_range(self,
                    from_min: Vector = None,
                    from_max: Vector = None,
                    to_min: Vector = None,
                    to_max: Vector = None,
                    clamp = True,
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR'):
        """ > Node <&Node Map Range>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | Vector      | `self`           |
        | Parameter | `data_type` | `'FLOAT_VECTOR'` |

        Parameters
        ----------
        from_min : Vector, optional
            socket 'From Min' (id: From_Min_FLOAT3)
        
        from_max : Vector, optional
            socket 'From Max' (id: From_Max_FLOAT3)
        
        to_min : Vector, optional
            socket 'To Min' (id: To_Min_FLOAT3)
        
        to_max : Vector, optional
            socket 'To Max' (id: To_Max_FLOAT3)
        
        clamp : bool
            parameter `clamp`
        
        interpolation_type : Literal['Linear', 'Stepped Linear', 'Smooth Step', 'Smoother Step']
            parameter `interpolation_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Map Range', 'interpolation_type', interpolation_type, 'map_range', ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'))
        node = Node('Map Range', {'Vector': self, 'From_Min_FLOAT3': from_min, 'From_Max_FLOAT3': from_max, 'To_Min_FLOAT3': to_min, 'To_Max_FLOAT3': to_max}, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type)
        return node._out

    def mix_uniform(self, b: Vector = None, factor: Float = None, clamp_factor = True):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name           | Value       |
        | --------- | -------------- | ----------- |
        | Socket    | A              | `self`      |
        | Parameter | `blend_type`   | `'MIX'`     |
        | Parameter | `clamp_result` | `False`     |
        | Parameter | `data_type`    | `'VECTOR'`  |
        | Parameter | `factor_mode`  | `'UNIFORM'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_Vector)
        
        factor : Float, optional
            socket 'Factor' (id: Factor_Float)
        
        clamp_factor : bool
            parameter `clamp_factor`
        

        Returns
        -------
        Vector
        """
        node = Node('Mix', {'A_Vector': self, 'B_Vector': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='UNIFORM')
        return node._out

    def mix_non_uniform(self, b: Vector = None, factor: Vector = None, clamp_factor = True):
        """ > Node <&Node Mix>

        **Fixed values**

        | Kind      | Name           | Value           |
        | --------- | -------------- | --------------- |
        | Socket    | A              | `self`          |
        | Parameter | `blend_type`   | `'MIX'`         |
        | Parameter | `clamp_result` | `False`         |
        | Parameter | `data_type`    | `'VECTOR'`      |
        | Parameter | `factor_mode`  | `'NON_UNIFORM'` |

        Parameters
        ----------
        b : Vector, optional
            socket 'B' (id: B_Vector)
        
        factor : Vector, optional
            socket 'Factor' (id: Factor_Vector)
        
        clamp_factor : bool
            parameter `clamp_factor`
        

        Returns
        -------
        Vector
        """
        node = Node('Mix', {'A_Vector': self, 'B_Vector': b, 'Factor_Vector': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='NON_UNIFORM')
        return node._out

    @property
    def xyz(self):
        """ > Node <&Node Separate XYZ>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Returns
        -------
        tuple (Float, Float, Float)
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return (node.x, node.y, node.z)

    def separate_xyz(self):
        """ > Node <&Node Separate XYZ>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Returns
        -------
        node [x (Float), y (Float), z (Float)]
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node

    @property
    def x(self):
        """ > Node <&Node Separate XYZ>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Returns
        -------
        x
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node.x

    @property
    def y(self):
        """ > Node <&Node Separate XYZ>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Returns
        -------
        y
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node.y

    @property
    def z(self):
        """ > Node <&Node Separate XYZ>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Returns
        -------
        z
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node.z

    def add(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Vector      | `self`  |
        | Parameter | `operation` | `'ADD'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='ADD')
        return node._out

    def subtract(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Vector      | `self`       |
        | Parameter | `operation` | `'SUBTRACT'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='SUBTRACT')
        return node._out

    def multiply(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Vector      | `self`       |
        | Parameter | `operation` | `'MULTIPLY'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MULTIPLY')
        return node._out

    def divide(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Vector      | `self`     |
        | Parameter | `operation` | `'DIVIDE'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='DIVIDE')
        return node._out

    def multiply_add(self, multiplier: Vector = None, addend: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value            |
        | --------- | ----------- | ---------------- |
        | Socket    | Vector      | `self`           |
        | Parameter | `operation` | `'MULTIPLY_ADD'` |

        Parameters
        ----------
        multiplier : Vector, optional
            socket 'Multiplier' (id: Vector_001)
        
        addend : Vector, optional
            socket 'Addend' (id: Vector_002)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': multiplier, 'Vector_002': addend}, operation='MULTIPLY_ADD')
        return node._out

    def cross(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Vector      | `self`            |
        | Parameter | `operation` | `'CROSS_PRODUCT'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='CROSS_PRODUCT')
        return node._out

    def project(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Vector      | `self`      |
        | Parameter | `operation` | `'PROJECT'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='PROJECT')
        return node._out

    def reflect(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Vector      | `self`      |
        | Parameter | `operation` | `'REFLECT'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='REFLECT')
        return node._out

    def refract(self, vector: Vector = None, ior: Float = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Vector      | `self`      |
        | Parameter | `operation` | `'REFRACT'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        
        ior : Float, optional
            socket 'IOR' (id: Scale)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector, 'Scale': ior}, operation='REFRACT')
        return node._out

    def faceforward(self, incident: Vector = None, reference: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value           |
        | --------- | ----------- | --------------- |
        | Socket    | Vector      | `self`          |
        | Parameter | `operation` | `'FACEFORWARD'` |

        Parameters
        ----------
        incident : Vector, optional
            socket 'Incident' (id: Vector_001)
        
        reference : Vector, optional
            socket 'Reference' (id: Vector_002)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': incident, 'Vector_002': reference}, operation='FACEFORWARD')
        return node._out

    def dot(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value           |
        | --------- | ----------- | --------------- |
        | Socket    | Vector      | `self`          |
        | Parameter | `operation` | `'DOT_PRODUCT'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Float
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='DOT_PRODUCT')
        return node._out

    def distance(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Vector      | `self`       |
        | Parameter | `operation` | `'DISTANCE'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Float
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='DISTANCE')
        return node._out

    def length(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Vector      | `self`     |
        | Parameter | `operation` | `'LENGTH'` |

        Returns
        -------
        Float
        """
        node = Node('Vector Math', {'Vector': self}, operation='LENGTH')
        return node._out

    def scale(self, scale: Float = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Vector      | `self`    |
        | Parameter | `operation` | `'SCALE'` |

        Parameters
        ----------
        scale : Float, optional
            socket 'Scale' (id: Scale)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Scale': scale}, operation='SCALE')
        return node._out

    def normalize(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value         |
        | --------- | ----------- | ------------- |
        | Socket    | Vector      | `self`        |
        | Parameter | `operation` | `'NORMALIZE'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='NORMALIZE')
        return node._out

    def abs(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Vector      | `self`       |
        | Parameter | `operation` | `'ABSOLUTE'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='ABSOLUTE')
        return node._out

    def power(self, exponent: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Base        | `self`    |
        | Parameter | `operation` | `'POWER'` |

        Parameters
        ----------
        exponent : Vector, optional
            socket 'Exponent' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': exponent}, operation='POWER')
        return node._out

    def sign(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Vector      | `self`   |
        | Parameter | `operation` | `'SIGN'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='SIGN')
        return node._out

    def min(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Vector      | `self`      |
        | Parameter | `operation` | `'MINIMUM'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MINIMUM')
        return node._out

    def max(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Vector      | `self`      |
        | Parameter | `operation` | `'MAXIMUM'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MAXIMUM')
        return node._out

    def round(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Vector      | `self`    |
        | Parameter | `operation` | `'ROUND'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='ROUND')
        return node._out

    def floor(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Vector      | `self`    |
        | Parameter | `operation` | `'FLOOR'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='FLOOR')
        return node._out

    def ceil(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Vector      | `self`   |
        | Parameter | `operation` | `'CEIL'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='CEIL')
        return node._out

    def fraction(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value        |
        | --------- | ----------- | ------------ |
        | Socket    | Vector      | `self`       |
        | Parameter | `operation` | `'FRACTION'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='FRACTION')
        return node._out

    def modulo(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Vector      | `self`     |
        | Parameter | `operation` | `'MODULO'` |

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MODULO')
        return node._out

    def wrap(self, max: Vector = None, min: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Vector      | `self`   |
        | Parameter | `operation` | `'WRAP'` |

        Parameters
        ----------
        max : Vector, optional
            socket 'Max' (id: Vector_001)
        
        min : Vector, optional
            socket 'Min' (id: Vector_002)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': max, 'Vector_002': min}, operation='WRAP')
        return node._out

    def snap(self, increment: Vector = None):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Vector      | `self`   |
        | Parameter | `operation` | `'SNAP'` |

        Parameters
        ----------
        increment : Vector, optional
            socket 'Increment' (id: Vector_001)
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': increment}, operation='SNAP')
        return node._out

    def sin(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Vector      | `self`   |
        | Parameter | `operation` | `'SINE'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='SINE')
        return node._out

    def cos(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Vector      | `self`     |
        | Parameter | `operation` | `'COSINE'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='COSINE')
        return node._out

    def tan(self):
        """ > Node <&Node Vector Math>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Vector      | `self`      |
        | Parameter | `operation` | `'TANGENT'` |

        Returns
        -------
        Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='TANGENT')
        return node._out

    def rotate(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE'):
        """ > Node <&Node Vector Rotate>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        center : Vector, optional
            socket 'Center' (id: Center)
        
        axis : Vector, optional
            socket 'Axis' (id: Axis)
        
        angle : Float, optional
            socket 'Angle' (id: Angle)
        
        invert : bool
            parameter `invert`
        
        rotation_type : Literal['Axis Angle', 'X Axis', 'Y Axis', 'Z Axis', 'Euler']
            parameter `rotation_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Rotate', 'rotation_type', rotation_type, 'rotate', ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'))
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type=rotation_type)
        return node._out

    def rotate_axis_angle(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False):
        """ > Node <&Node Vector Rotate>

        **Fixed values**

        | Kind      | Name            | Value          |
        | --------- | --------------- | -------------- |
        | Socket    | Vector          | `self`         |
        | Parameter | `rotation_type` | `'AXIS_ANGLE'` |

        Parameters
        ----------
        center : Vector, optional
            socket 'Center' (id: Center)
        
        axis : Vector, optional
            socket 'Axis' (id: Axis)
        
        angle : Float, optional
            socket 'Angle' (id: Angle)
        
        invert : bool
            parameter `invert`
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type='AXIS_ANGLE')
        return node._out

    def rotate_x_axis(self, center: Vector = None, angle: Float = None, invert = False):
        """ > Node <&Node Vector Rotate>

        **Fixed values**

        | Kind      | Name            | Value      |
        | --------- | --------------- | ---------- |
        | Socket    | Vector          | `self`     |
        | Parameter | `rotation_type` | `'X_AXIS'` |

        Parameters
        ----------
        center : Vector, optional
            socket 'Center' (id: Center)
        
        angle : Float, optional
            socket 'Angle' (id: Angle)
        
        invert : bool
            parameter `invert`
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='X_AXIS')
        return node._out

    def rotate_y_axis(self, center: Vector = None, angle: Float = None, invert = False):
        """ > Node <&Node Vector Rotate>

        **Fixed values**

        | Kind      | Name            | Value      |
        | --------- | --------------- | ---------- |
        | Socket    | Vector          | `self`     |
        | Parameter | `rotation_type` | `'Y_AXIS'` |

        Parameters
        ----------
        center : Vector, optional
            socket 'Center' (id: Center)
        
        angle : Float, optional
            socket 'Angle' (id: Angle)
        
        invert : bool
            parameter `invert`
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='Y_AXIS')
        return node._out

    def rotate_z_axis(self, center: Vector = None, angle: Float = None, invert = False):
        """ > Node <&Node Vector Rotate>

        **Fixed values**

        | Kind      | Name            | Value      |
        | --------- | --------------- | ---------- |
        | Socket    | Vector          | `self`     |
        | Parameter | `rotation_type` | `'Z_AXIS'` |

        Parameters
        ----------
        center : Vector, optional
            socket 'Center' (id: Center)
        
        angle : Float, optional
            socket 'Angle' (id: Angle)
        
        invert : bool
            parameter `invert`
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='Z_AXIS')
        return node._out

    def rotate_euler_xyz(self, center: Vector = None, rotation: Vector = None, invert = False):
        """ > Node <&Node Vector Rotate>

        **Fixed values**

        | Kind      | Name            | Value         |
        | --------- | --------------- | ------------- |
        | Socket    | Vector          | `self`        |
        | Parameter | `rotation_type` | `'EULER_XYZ'` |

        Parameters
        ----------
        center : Vector, optional
            socket 'Center' (id: Center)
        
        rotation : Vector, optional
            socket 'Rotation' (id: Rotation)
        
        invert : bool
            parameter `invert`
        

        Returns
        -------
        Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Rotation': rotation}, invert=invert, rotation_type='EULER_XYZ')
        return node._out

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        interpolation : menu='Trilinear', optional
            ('Nearest Neighbor', 'Trilinear', 'Triquadratic')
        

        Returns
        -------
        Vector
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='VECTOR')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

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
        Vector
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='VECTOR')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Topology    | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

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
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='VECTOR', **sockets)
        return node._out

    def advect_grid(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None):
        """ > Node <&Node Advect Grid>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

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
        Vector
        """
        node = Node('Advect Grid', {'Grid': self, 'Velocity': velocity, 'Time Step': time_step, 'Integration Scheme': integration_scheme, 'Limiter': limiter}, data_type='VECTOR')
        return node._out

    def grid_curl(self):
        """ > Node <&Node Grid Curl>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Grid | `self` |

        Returns
        -------
        Vector
        """
        node = Node('Grid Curl', {'Grid': self})
        return node._out

    def grid_divergence(self):
        """ > Node <&Node Grid Divergence>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Grid | `self` |

        Returns
        -------
        Float
        """
        node = Node('Grid Divergence', {'Grid': self})
        return node._out

    def prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Vector = None):
        """ > Node <&Node Prune Grid>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        mode : menu='Threshold', optional
            ('Inactive', 'Threshold', 'SDF')
        
        threshold : Vector, optional
            socket 'Threshold' (id: Threshold)
        

        Returns
        -------
        Vector
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode, 'Threshold': threshold}, data_type='VECTOR')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Returns
        -------
        Vector
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='VECTOR')
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

    def set_grid_background(self, background: Vector = None, update_inactive: Boolean = None):
        """ > Node <&Node Set Grid Background>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        background : Vector, optional
            socket 'Background' (id: Background)
        
        update_inactive : Boolean, optional
            socket 'Update Inactive' (id: Update Inactive)
        

        Returns
        -------
        Vector
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background, 'Update Inactive': update_inactive}, data_type='VECTOR')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        transform : Matrix, optional
            socket 'Transform' (id: Transform)
        

        Returns
        -------
        Boolean
            peer sockets: grid_ (Vector)

        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='VECTOR')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Returns
        -------
        Matrix
            peer sockets: background_value_ (Vector)

        """
        node = Node('Grid Info', {'Grid': self}, data_type='VECTOR')
        return node._out

    def uv_tangent(self, method: Literal['Exact', 'Fast'] = None):
        """ > Node <&Node UV Tangent>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | UV   | `self` |

        Parameters
        ----------
        method : menu='Exact', optional
            ('Exact', 'Fast')
        

        Returns
        -------
        Vector
        """
        node = Node('UV Tangent', {'Method': method, 'UV': self})
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Vector
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='VECTOR')
        return node._out

    def radial_tiling(self, sides: Float = None, roundness: Float = None, normalize = False):
        """ > Node <&Node Radial Tiling>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        sides : Float, optional
            socket 'Sides' (id: Sides)
        
        roundness : Float, optional
            socket 'Roundness' (id: Roundness)
        
        normalize : bool
            parameter `normalize`
        

        Returns
        -------
        Vector
            peer sockets: segment_id_ (Float), segment_width_ (Float), segment_rotation_ (Float)

        """
        node = Node('Radial Tiling', {'Vector': self, 'Sides': sides, 'Roundness': roundness}, normalize=normalize)
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

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

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
        Vector
        """
        node = Node('Clip Grid', {'Grid': self, 'Min X': min_x, 'Min Y': min_y, 'Min Z': min_z, 'Max X': max_x, 'Max Y': max_y, 'Max Z': max_z}, data_type='VECTOR')
        return node._out

    def grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None):
        """ > Node <&Node Grid Dilate & Erode>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

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
        Vector
        """
        node = Node('Grid Dilate & Erode', {'Grid': self, 'Connectivity': connectivity, 'Tiles': tiles, 'Steps': steps}, data_type='VECTOR')
        return node._out

    def grid_mean(self, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node Grid Mean>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        width : Integer, optional
            socket 'Width' (id: Width)
        
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        

        Returns
        -------
        Vector
        """
        node = Node('Grid Mean', {'Grid': self, 'Width': width, 'Iterations': iterations}, data_type='VECTOR')
        return node._out

    def grid_median(self, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node Grid Median>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Parameters
        ----------
        width : Integer, optional
            socket 'Width' (id: Width)
        
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        

        Returns
        -------
        Vector
        """
        node = Node('Grid Median', {'Grid': self, 'Width': width, 'Iterations': iterations}, data_type='VECTOR')
        return node._out

    def grid_to_points(self):
        """ > Node <&Node Grid to Points>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Grid        | `self`     |
        | Parameter | `data_type` | `'VECTOR'` |

        Returns
        -------
        Cloud
            peer sockets: value_ (Vector), x_ (Integer), y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_ (Integer)

        """
        node = Node('Grid to Points', {'Grid': self}, data_type='VECTOR')
        return node._out

    def mapping(self,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT'):
        """ > Node <&ShaderNode Mapping>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        location : Vector, optional
            socket 'Location' (id: Location)
        
        rotation : Vector, optional
            socket 'Rotation' (id: Rotation)
        
        scale : Vector, optional
            socket 'Scale' (id: Scale)
        
        vector_type : Literal['Point', 'Texture', 'Vector', 'Normal']
            parameter `vector_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Mapping', 'vector_type', vector_type, 'mapping', ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL'))
        node = Node('Mapping', {'Vector': self, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    def normal(self):
        """ > Node <&ShaderNode Normal>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Normal | `self` |

        Returns
        -------
        Vector
            peer sockets: dot_ (Float)

        """
        node = Node('Normal', {'Normal': self})
        return node._out

    @classmethod
    def Tangent(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = ''):
        """ > Node <&ShaderNode Tangent>

        Parameters
        ----------
        axis : Literal['X', 'Y', 'Z']
            parameter `axis`
        
        direction_type : Literal['Radial', 'UV Map']
            parameter `direction_type`
        
        uv_map : str
            parameter `uv_map`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Tangent', 'axis', axis, 'Tangent', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Tangent', 'direction_type', direction_type, 'Tangent', ('RADIAL', 'UV_MAP'))
        node = Node('Tangent', axis=axis, direction_type=direction_type, uv_map=uv_map)
        return cls(node._out)

    def environment_texture(self,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR'):
        """ > Node <&ShaderNode Environment Texture>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        image : NoneType
            parameter `image`
        
        interpolation : Literal['Linear', 'Closest', 'Cubic', 'Smart']
            parameter `interpolation`
        
        projection : Literal['Equirectangular', 'Mirror Ball']
            parameter `projection`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Environment Texture', 'interpolation', interpolation, 'environment_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Environment Texture', 'projection', projection, 'environment_texture', ('EQUIRECTANGULAR', 'MIRROR_BALL'))
        node = Node('Environment Texture', {'Vector': self}, image=image, interpolation=interpolation, projection=projection)
        return node._out

    def ies_texture_internal(self, strength: Float = None, filepath = '', ies = None):
        """ > Node <&ShaderNode IES Texture>

        **Fixed values**

        | Kind      | Name   | Value        |
        | --------- | ------ | ------------ |
        | Socket    | Vector | `self`       |
        | Parameter | `mode` | `'INTERNAL'` |

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        filepath : str
            parameter `filepath`
        
        ies : NoneType
            parameter `ies`
        

        Returns
        -------
        Float
        """
        node = Node('IES Texture', {'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode='INTERNAL')
        return node._out

    def ies_texture_external(self, strength: Float = None, filepath = '', ies = None):
        """ > Node <&ShaderNode IES Texture>

        **Fixed values**

        | Kind      | Name   | Value        |
        | --------- | ------ | ------------ |
        | Socket    | Vector | `self`       |
        | Parameter | `mode` | `'EXTERNAL'` |

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        filepath : str
            parameter `filepath`
        
        ies : NoneType
            parameter `ies`
        

        Returns
        -------
        Float
        """
        node = Node('IES Texture', {'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode='EXTERNAL')
        return node._out

    def ies_texture(self,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL'):
        """ > Node <&ShaderNode IES Texture>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        filepath : str
            parameter `filepath`
        
        ies : NoneType
            parameter `ies`
        
        mode : Literal['Internal', 'External']
            parameter `mode`
        

        Returns
        -------
        Float
        """
        utils.check_enum_arg('IES Texture', 'mode', mode, 'ies_texture', ('INTERNAL', 'EXTERNAL'))
        node = Node('IES Texture', {'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode=mode)
        return node._out

    def image_texture(self,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0):
        """ > Node <&ShaderNode Image Texture>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        extension : Literal['Repeat', 'Extend', 'Clip', 'Mirror']
            parameter `extension`
        
        image : NoneType
            parameter `image`
        
        interpolation : Literal['Linear', 'Closest', 'Cubic', 'Smart']
            parameter `interpolation`
        
        projection : Literal['Flat', 'Box', 'Sphere', 'Tube']
            parameter `projection`
        
        projection_blend : float
            parameter `projection_blend`
        

        Returns
        -------
        Color
            peer sockets: alpha_ (Float)

        """
        utils.check_enum_arg('Image Texture', 'extension', extension, 'image_texture', ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'))
        utils.check_enum_arg('Image Texture', 'interpolation', interpolation, 'image_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Image Texture', 'projection', projection, 'image_texture', ('FLAT', 'BOX', 'SPHERE', 'TUBE'))
        node = Node('Image Texture', {'Vector': self}, extension=extension, image=image, interpolation=interpolation, projection=projection, projection_blend=projection_blend)
        return node._out

    @classmethod
    def UvMap(cls, from_instancer = False, uv_map = ''):
        """ > Node <&ShaderNode UV Map>

        Parameters
        ----------
        from_instancer : bool
            parameter `from_instancer`
        
        uv_map : str
            parameter `uv_map`
        

        Returns
        -------
        Vector
        """
        node = Node('UV Map', from_instancer=from_instancer, uv_map=uv_map)
        return cls(node._out)

    def vector_transform(self,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR'):
        """ > Node <&ShaderNode Vector Transform>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Vector | `self` |

        Parameters
        ----------
        convert_from : Literal['World', 'Object', 'Camera']
            parameter `convert_from`
        
        convert_to : Literal['World', 'Object', 'Camera']
            parameter `convert_to`
        
        vector_type : Literal['Point', 'Vector', 'Normal']
            parameter `vector_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Transform', 'convert_from', convert_from, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'convert_to', convert_to, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'vector_type', vector_type, 'vector_transform', ('POINT', 'VECTOR', 'NORMAL'))
        node = Node('Vector Transform', {'Vector': self}, convert_from=convert_from, convert_to=convert_to, vector_type=vector_type)
        return node._out

    def raycast(self, direction: Vector = None, length: Float = None, only_local = False):
        """ > Node <&ShaderNode Raycast>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Position | `self` |

        Parameters
        ----------
        direction : Vector, optional
            socket 'Direction' (id: Direction)
        
        length : Float, optional
            socket 'Length' (id: Length)
        
        only_local : bool
            parameter `only_local`
        

        Returns
        -------
        Float
            peer sockets: self_hit_ (Float), hit_distance_ (Float), hit_position_ (Vector), hit_normal_ (Vector)

        """
        node = Node('Raycast', {'Position': self, 'Direction': direction, 'Length': length}, only_local=only_local)
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = (0, 0, 0),
        name: str = 'Vector',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
        subtype: str = 'NONE',
         ):
        """ > Vector Input

        New <#Vector> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Vector`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')

        subtype : str, default=`NONE`
            Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')


        Returns
        -------
        Vector
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketVector', default_value = defval,
            name=name, min=min, max=max, tip=tip, panel=panel, optional_label=optional_label,
            hide_value=hide_value, hide_in_modifier=hide_in_modifier, dimensions=dimensions,
            default_attribute=default_attribute, default_input=default_input, shape=shape, subtype=subtype)

    @classmethod
    def Percentage(cls,
        value: object = (0, 0, 0),
        name: str = 'Percentage',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Percentage Input

        New <#Vector> input with subtype 'PERCENTAGE'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Percentage`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls,
        value: object = (0, 0, 0),
        name: str = 'Factor',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Factor Input

        New <#Vector> input with subtype 'FACTOR'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Factor`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='FACTOR')

    @classmethod
    def Translation(cls,
        value: object = (0, 0, 0),
        name: str = 'Translation',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Translation Input

        New <#Vector> input with subtype 'TRANSLATION'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Translation`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='TRANSLATION')

    @classmethod
    def Direction(cls,
        value: object = (0, 0, 0),
        name: str = 'Direction',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Direction Input

        New <#Vector> input with subtype 'DIRECTION'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Direction`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='DIRECTION')

    @classmethod
    def Velocity(cls,
        value: object = (0, 0, 0),
        name: str = 'Velocity',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Velocity Input

        New <#Vector> input with subtype 'VELOCITY'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Velocity`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='VELOCITY')

    @classmethod
    def Acceleration(cls,
        value: object = (0, 0, 0),
        name: str = 'Acceleration',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Acceleration Input

        New <#Vector> input with subtype 'ACCELERATION'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Acceleration`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='ACCELERATION')

    @classmethod
    def Euler(cls,
        value: object = (0, 0, 0),
        name: str = 'Euler',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Euler Input

        New <#Vector> input with subtype 'EULER'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Euler`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='EULER')

    @classmethod
    def Xyz(cls,
        value: object = (0, 0, 0),
        name: str = 'Xyz',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Xyz Input

        New <#Vector> input with subtype 'XYZ'.

        Parameters
        ----------
        value : object, default=`(0, 0, 0)`
            Default value

        name : str, default=`Xyz`
            Input socket name

        min : float, default=`-3.40282e+38`
            Property min_value

        max : float, default=`3.40282e+38`
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

        dimensions : int, default=`3`
            Property dimensions

        default_attribute : str, default=`''`
            Property default_attribute_name

        default_input : str, default=`'VALUE'`
            Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='XYZ')

