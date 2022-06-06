import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Vector

class Vector(dsock.Vector):
    """ Class Vector
    

    | Inherits from: dsock.Vector 
    

    Index 
    

    Constructors
    ============
    - **AlignToVector** : AlignEulerToVector rotation (Vector) 
    - **Combine**       : CombineXyz vector (Vector) 
    - **Random**        : RandomValue value (Vector) 
    

    Properties
    ==========
    - **separate** : SeparateXyz Sockets      [x (Float), y (Float), z (Float)] 
    

    Methods
    =======
    - **absolute**            : VectorMath vector (Vector) 
    - **accumulate_field**    : AccumulateField Sockets      [leading (Vector), trailing (Vector), total (Vector)]
    - **add**                 : VectorMath vector (Vector) 
    - **attribute_statistic** : AttributeStatistic Sockets      [mean (Vector), median (Vector), sum (Vector),
      min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)] 
    - **capture_attribute**   : CaptureAttribute Sockets      [geometry (Geometry), attribute (Vector)] 
    - **ceil**                : VectorMath vector (Vector) 
    - **cos**                 : VectorMath vector (Vector) 
    - **cross**               : VectorMath vector (Vector) 
    - **distance**            : VectorMath value (Float) 
    - **divide**              : VectorMath vector (Vector) 
    - **dot**                 : VectorMath value (Float) 
    - **equal**               : Compare result (Boolean) 
    - **faceforward**         : VectorMath vector (Vector) 
    - **field_at_index**      : FieldAtIndex value (Vector) 
    - **floor**               : VectorMath vector (Vector) 
    - **fraction**            : VectorMath vector (Vector) 
    - **greater_equal**       : Compare result (Boolean) 
    - **greater_than**        : Compare result (Boolean) 
    - **length**              : VectorMath value (Float) 
    - **less_equal**          : Compare result (Boolean) 
    - **less_than**           : Compare result (Boolean) 
    - **map_range**           : MapRange vector (Vector) 
    - **max**                 : VectorMath vector (Vector) 
    - **min**                 : VectorMath vector (Vector) 
    - **modulo**              : VectorMath vector (Vector) 
    - **multiply**            : VectorMath vector (Vector) 
    - **multiply_add**        : VectorMath vector (Vector) 
    - **normalize**           : VectorMath vector (Vector) 
    - **not_equal**           : Compare result (Boolean) 
    - **project**             : VectorMath vector (Vector) 
    - **raycast**             : Raycast Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance
      (Float), attribute (Vector)] 
    - **reflect**             : VectorMath vector (Vector) 
    - **refract**             : VectorMath vector (Vector) 
    - **rotate**              : VectorRotate vector (Vector) 
    - **scale**               : VectorMath vector (Vector) 
    - **sin**                 : VectorMath vector (Vector) 
    - **snap**                : VectorMath vector (Vector) 
    - **subtract**            : VectorMath vector (Vector) 
    - **tan**                 : VectorMath vector (Vector) 
    - **transfer_attribute**  : TransferAttribute attribute (Vector) 
    - **wrap**                : VectorMath vector (Vector) 
    

    Stacked methods
    ===============
    - **align_to_vector** : AlignEulerToVector Vector 
    - **curves**          : VectorCurves Vector 
    - **rotate_euler**    : RotateEuler Vector 
    """


    def reset_properties(self):
        self.separate_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Random
        

        | Node: RandomValue 
        

        Top Index 
        

            v = Vector.Random(min, max, ID, seed) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - min  : Vector 
            - max  : Vector 
            - ID   : Integer 
            - seed : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

        Node creation
        =============
        

            node = nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR') 
        

        Returns
        =======
                Vector 
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """ Combine
        

        | Node: CombineXyz 
        

        Top Index 
        

            v = Vector.Combine(x, y, z) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - x : Float 
            - y : Float 
            - z : Float 
        

        Node creation
        =============
        

            node = nodes.CombineXyz(x=x, y=y, z=z) 
        

        Returns
        =======
                Vector 
        """

        return cls(nodes.CombineXyz(x=x, y=y, z=z).vector)

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ AlignToVector
        

        | Node: AlignEulerToVector 
        

        Top Index 
        

            v = Vector.AlignToVector(rotation, factor, vector, axis, pivot_axis) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - rotation : Vector 
            - factor   : Float 
            - vector   : Vector 
        

            Parameters arguments
            --------------------
            - axis       : 'X' in [X, Y, Z] 
            - pivot_axis : 'AUTO' in [AUTO, X, Y, Z] 
        

        Node creation
        =============
        

            node = nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis)
        

        Returns
        =======
                Vector 
        """

        return cls(nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ separate
        

        | Node: SeparateXyz 
        

        Top Index 
        

            v = vector.separate 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector : Vector (self) 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.separate" 
        

        Node creation
        =============
        

            node = nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate") 
        

        Returns
        =======
                Sockets [x (Float), y (Float), z (Float)] 
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
        return self.separate_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ accumulate_field
        

        | Node: AccumulateField 
        

        Top Index 
        

            v = vector.accumulate_field(group_index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value       : Vector (self) 
            - group_index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)
        

        Returns
        =======
                Sockets [leading (Vector), trailing (Vector), total (Vector)] 
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT'):
        """ attribute_statistic
        

        | Node: AttributeStatistic 
        

        Top Index 
        

            v = vector.attribute_statistic(geometry, selection, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute : Vector (self) 
            - geometry  : Geometry 
            - selection : Boolean 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR',
            domain=domain) 
        

        Returns
        =======
                Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation
                (Vector), variance (Vector)] 
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_attribute
        

        | Node: TransferAttribute 
        

        Top Index 
        

            v = vector.transfer_attribute(source, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Vector (self) 
            - source          : Geometry 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index,
            data_type='FLOAT_VECTOR', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Vector 
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ capture_attribute
        

        | Node: CaptureAttribute 
        

        Top Index 
        

            v = vector.capture_attribute(geometry, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Vector (self) 
            - geometry : Geometry 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain)
        

        Returns
        =======
                Sockets [geometry (Geometry), attribute (Vector)] 
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """ field_at_index
        

        | Node: FieldAtIndex 
        

        Top Index 
        

            v = vector.field_at_index(index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value : Vector (self) 
            - index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain) 
        

        Returns
        =======
                Vector 
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ raycast
        

        | Node: Raycast 
        

        Top Index 
        

            v = vector.raycast(target_geometry, source_position, ray_direction, ray_length, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Vector (self) 
            - target_geometry : Geometry 
            - source_position : Vector 
            - ray_direction   : Vector 
            - ray_length      : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

            Parameters arguments
            --------------------
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST] 
        

        Node creation
        =============
        

            node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position,
            ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping) 
        

        Returns
        =======
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute
                (Vector)] 
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping)

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR'):
        """ map_range
        

        | Node: MapRange 
        

        Top Index 
        

            v = vector.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector   : Vector (self) 
            - from_min : Vector 
            - from_max : Vector 
            - to_min   : Vector 
            - to_max   : Vector 
        

            Parameters arguments
            --------------------
            - clamp              : True 
            - interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP] 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT_VECTOR' 
        

        Node creation
        =============
        

            node = nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max,
            clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type) 
        

        Returns
        =======
                Vector 
        """

        return nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type).vector

    def less_than(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """ less_than
        

        | Node: Compare 
        

        Top Index 
        

            v = vector.less_than(b, c, angle, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a     : Vector (self) 
            - b     : Vector 
            - c     : Float 
            - angle : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'VECTOR' 
            - operation : 'LESS_THAN' 
        

            Parameters arguments
            --------------------
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN').result

    def less_equal(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """ less_equal
        

        | Node: Compare 
        

        Top Index 
        

            v = vector.less_equal(b, c, angle, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a     : Vector (self) 
            - b     : Vector 
            - c     : Float 
            - angle : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'VECTOR' 
            - operation : 'LESS_EQUAL' 
        

            Parameters arguments
            --------------------
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL').result

    def greater_than(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """ greater_than
        

        | Node: Compare 
        

        Top Index 
        

            v = vector.greater_than(b, c, angle, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a     : Vector (self) 
            - b     : Vector 
            - c     : Float 
            - angle : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'VECTOR' 
            - operation : 'GREATER_THAN' 
        

            Parameters arguments
            --------------------
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN').result

    def greater_equal(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """ greater_equal
        

        | Node: Compare 
        

        Top Index 
        

            v = vector.greater_equal(b, c, angle, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a     : Vector (self) 
            - b     : Vector 
            - c     : Float 
            - angle : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'VECTOR' 
            - operation : 'GREATER_EQUAL' 
        

            Parameters arguments
            --------------------
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL').result

    def equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT'):
        """ equal
        

        | Node: Compare 
        

        Top Index 
        

            v = vector.equal(b, c, angle, epsilon, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a       : Vector (self) 
            - b       : Vector 
            - c       : Float 
            - angle   : Float 
            - epsilon : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'VECTOR' 
            - operation : 'EQUAL' 
        

            Parameters arguments
            --------------------
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL').result

    def not_equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT'):
        """ not_equal
        

        | Node: Compare 
        

        Top Index 
        

            v = vector.not_equal(b, c, angle, epsilon, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a       : Vector (self) 
            - b       : Vector 
            - c       : Float 
            - angle   : Float 
            - epsilon : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'VECTOR' 
            - operation : 'NOT_EQUAL' 
        

            Parameters arguments
            --------------------
            - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL').result

    def add(self, vector1=None):
        """ add
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.add(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'ADD' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD').vector

    def subtract(self, vector1=None):
        """ subtract
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.subtract(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'SUBTRACT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT').vector

    def multiply(self, vector1=None):
        """ multiply
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.multiply(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'MULTIPLY' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY').vector

    def divide(self, vector1=None):
        """ divide
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.divide(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'DIVIDE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE').vector

    def multiply_add(self, vector1=None, vector2=None):
        """ multiply_add
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.multiply_add(vector1, vector2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
            - vector2 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'MULTIPLY_ADD' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector

    def cross(self, vector1=None):
        """ cross
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.cross(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'CROSS_PRODUCT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT').vector

    def project(self, vector1=None):
        """ project
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.project(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'PROJECT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT').vector

    def reflect(self, vector1=None):
        """ reflect
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.reflect(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'REFLECT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT').vector

    def refract(self, vector1=None, scale=None):
        """ refract
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.refract(vector1, scale) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
            - scale   : Float 
        

            Fixed parameters
            ----------------
            - operation : 'REFRACT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT').vector

    def faceforward(self, vector1=None, vector2=None):
        """ faceforward
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.faceforward(vector1, vector2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
            - vector2 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'FACEFORWARD' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector

    def dot(self, vector1=None):
        """ dot
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.dot(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'DOT_PRODUCT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT') 
        

        Returns
        =======
                Float 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT').value

    def distance(self, vector1=None):
        """ distance
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.distance(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'DISTANCE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE') 
        

        Returns
        =======
                Float 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE').value

    def length(self):
        """ length
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.length() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'LENGTH' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='LENGTH') 
        

        Returns
        =======
                Float 
        """

        return nodes.VectorMath(vector0=self, operation='LENGTH').value

    def scale(self, scale=None):
        """ scale
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.scale(scale) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - scale   : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SCALE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, scale=scale, operation='SCALE') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, scale=scale, operation='SCALE').vector

    def normalize(self):
        """ normalize
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.normalize() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'NORMALIZE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='NORMALIZE') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='NORMALIZE').vector

    def absolute(self):
        """ absolute
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.absolute() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ABSOLUTE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='ABSOLUTE') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='ABSOLUTE').vector

    def min(self, vector1=None):
        """ min
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.min(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'MINIMUM' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM').vector

    def max(self, vector1=None):
        """ max
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.max(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'MAXIMUM' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM').vector

    def floor(self):
        """ floor
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.floor() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'FLOOR' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='FLOOR') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='FLOOR').vector

    def ceil(self):
        """ ceil
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.ceil() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'CEIL' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='CEIL') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='CEIL').vector

    def fraction(self):
        """ fraction
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.fraction() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'FRACTION' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='FRACTION') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='FRACTION').vector

    def modulo(self, vector1=None):
        """ modulo
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.modulo(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'MODULO' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO').vector

    def wrap(self, vector1=None, vector2=None):
        """ wrap
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.wrap(vector1, vector2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
            - vector2 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'WRAP' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP').vector

    def snap(self, vector1=None):
        """ snap
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.snap(vector1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
            - vector1 : Vector 
        

            Fixed parameters
            ----------------
            - operation : 'SNAP' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP').vector

    def sin(self):
        """ sin
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.sin() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SINE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='SINE') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='SINE').vector

    def cos(self):
        """ cos
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.cos() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'COSINE' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='COSINE') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='COSINE').vector

    def tan(self):
        """ tan
        

        | Node: VectorMath 
        

        Top Index 
        

            v = vector.tan() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector0 : Vector (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TANGENT' 
        

        Node creation
        =============
        

            node = nodes.VectorMath(vector0=self, operation='TANGENT') 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorMath(vector0=self, operation='TANGENT').vector

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
        """ rotate
        

        | Node: VectorRotate 
        

        Top Index 
        

            v = vector.rotate(center, axis, angle, rotation, invert, rotation_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector   : Vector (self) 
            - center   : Vector 
            - axis     : Vector 
            - angle    : Float 
            - rotation : Vector 
        

            Parameters arguments
            --------------------
            - invert        : False 
            - rotation_type : 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ] 
        

        Node creation
        =============
        

            node = nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert,
            rotation_type=rotation_type) 
        

        Returns
        =======
                Vector 
        """

        return nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type).vector


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """ curves
        

        | Node: VectorCurves 
        

        Top Index 
        

            vector.curves(fac) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector : Vector (self) 
            - fac    : Float 
        

        Node creation
        =============
        

            node = nodes.VectorCurves(vector=self, fac=fac) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.VectorCurves(vector=self, fac=fac))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ align_to_vector
        

        | Node: AlignEulerToVector 
        

        Top Index 
        

            vector.align_to_vector(factor, vector, axis, pivot_axis) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - rotation : Vector (self) 
            - factor   : Float 
            - vector   : Vector 
        

            Parameters arguments
            --------------------
            - axis       : 'X' in [X, Y, Z] 
            - pivot_axis : 'AUTO' in [AUTO, X, Y, Z] 
        

        Node creation
        =============
        

            node = nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis)
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))

    def rotate_euler(self, rotate_by=None, space='OBJECT'):
        """ rotate_euler
        

        | Node: RotateEuler 
        

        Top Index 
        

            vector.rotate_euler(rotate_by, space) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - rotation  : Vector (self) 
            - rotate_by : Vector 
        

            Parameters arguments
            --------------------
            - space : 'OBJECT' in [OBJECT, LOCAL] 
        

        Node creation
        =============
        

            node = nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space))


