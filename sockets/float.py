import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Float

class Float(dsock.Float):
    """ Class Float
    

    | Inherits from: dsock.Float 
    

    Constructors
    ============
    - Random : RandomValue value (Float) 
    

    Methods
    =======
    - abs                 : Math value (Float) 
    - accumulate_field    : AccumulateField Sockets      [leading (Float), trailing (Float), total (Float)] 
    - add                 : Math value (Float) 
    - arccos              : Math value (Float) 
    - arcsin              : Math value (Float) 
    - arctan              : Math value (Float) 
    - arctan2             : Math value (Float) 
    - attribute_statistic : AttributeStatistic Sockets      [mean (Float), median (Float), sum (Float), min
      (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)] 
    - capture_attribute   : CaptureAttribute Sockets      [geometry (Geometry), attribute (Float)] 
    - ceil                : Math value (Float) 
    - color_ramp          : Colorramp Sockets      [color (Color), alpha (Float)] 
    - compare             : Math value (Float) 
    - cos                 : Math value (Float) 
    - cosh                : Math value (Float) 
    - degrees             : Math value (Float) 
    - divide              : Math value (Float) 
    - equal               : Compare result (Boolean) 
    - exp                 : Math value (Float) 
    - field_at_index      : FieldAtIndex value (Float) 
    - floor               : Math value (Float) 
    - fract               : Math value (Float) 
    - greater_equal       : Compare result (Boolean) 
    - greater_than        : Compare result (Boolean) 
    - greater_than        : Math value (Float) 
    - inverse_sqrt        : Math value (Float) 
    - less_equal          : Compare result (Boolean) 
    - less_than           : Compare result (Boolean) 
    - less_than           : Math value (Float) 
    - log                 : Math value (Float) 
    - map_range           : MapRange result (Float) 
    - max                 : Math value (Float) 
    - min                 : Math value (Float) 
    - modulo              : Math value (Float) 
    - multiply            : Math value (Float) 
    - multiply_add        : Math value (Float) 
    - not_equal           : Compare result (Boolean) 
    - pingpong            : Math value (Float) 
    - pow                 : Math value (Float) 
    - radians             : Math value (Float) 
    - raycast             : Raycast Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance
      (Float), attribute (Float)] 
    - round               : Math value (Float) 
    - sign                : Math value (Float) 
    - sin                 : Math value (Float) 
    - sinh                : Math value (Float) 
    - smooth_max          : Math value (Float) 
    - smooth_min          : Math value (Float) 
    - snap                : Math value (Float) 
    - sqrt                : Math value (Float) 
    - subtract            : Math value (Float) 
    - switch              : Switch output (Float) 
    - tan                 : Math value (Float) 
    - tanh                : Math value (Float) 
    - to_integer          : FloatToInteger integer (Integer) 
    - to_string           : ValueToString string (String) 
    - transfer_attribute  : TransferAttribute attribute (Float) 
    - trunc               : Math value (Float) 
    - wrap                : Math value (Float) 
    

    Stacked methods
    ===============
    - clamp : Clamp Float 
    - curve : FloatCurve Float 
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Random
        

        | Node: RandomValue 
        

            v = Float.Random(min, max, ID, seed) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - min  : Float 
            - max  : Float 
            - ID   : Integer 
            - seed : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

        Node creation
        =============
        

            node = nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT') 
        

        Returns
        =======
                Float 
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ accumulate_field
        

        | Node: AccumulateField 
        

            v = float.accumulate_field(group_index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value       : Float (self) 
            - group_index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain) 
        

        Returns
        =======
                Sockets [leading (Float), trailing (Float), total (Float)] 
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT'):
        """ attribute_statistic
        

        | Node: AttributeStatistic 
        

            v = float.attribute_statistic(geometry, selection, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute : Float (self) 
            - geometry  : Geometry 
            - selection : Boolean 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT',
            domain=domain) 
        

        Returns
        =======
                Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation
                (Float), variance (Float)] 
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_attribute
        

        | Node: TransferAttribute 
        

            v = float.transfer_attribute(source, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Float (self) 
            - source          : Geometry 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index,
            data_type='FLOAT', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Float 
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ capture_attribute
        

        | Node: CaptureAttribute 
        

            v = float.capture_attribute(geometry, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Float (self) 
            - geometry : Geometry 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain) 
        

        Returns
        =======
                Sockets [geometry (Geometry), attribute (Float)] 
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """ field_at_index
        

        | Node: FieldAtIndex 
        

            v = float.field_at_index(index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value : Float (self) 
            - index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain) 
        

        Returns
        =======
                Float 
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ raycast
        

        | Node: Raycast 
        

            v = float.raycast(target_geometry, source_position, ray_direction, ray_length, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Float (self) 
            - target_geometry : Geometry 
            - source_position : Vector 
            - ray_direction   : Vector 
            - ray_length      : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

            Parameters arguments
            --------------------
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST] 
        

        Node creation
        =============
        

            node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position,
            ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping) 
        

        Returns
        =======
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute
                (Float)] 
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping)

    def switch(self, switch0=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = float.switch(switch0, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Float (self) 
            - switch0 : Boolean 
            - true    : Float 
        

            Fixed parameters
            ----------------
            - input_type : 'FLOAT' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch0=switch0, true=true, input_type='FLOAT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Switch(false=self, switch0=switch0, true=true, input_type='FLOAT').output

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR'):
        """ map_range
        

        | Node: MapRange 
        

            v = float.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Float (self) 
            - from_min : Float 
            - from_max : Float 
            - to_min   : Float 
            - to_max   : Float 
        

            Parameters arguments
            --------------------
            - clamp              : True 
            - interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP] 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
        

        Node creation
        =============
        

            node = nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max,
            clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type) 
        

        Returns
        =======
                Float 
        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type).result

    def less_than(self, b=None):
        """ less_than
        

        | Node: Compare 
        

            v = float.less_than(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Float (self) 
            - b : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
            - mode      : 'ELEMENT' 
            - operation : 'LESS_THAN' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN').result

    def less_equal(self, b=None):
        """ less_equal
        

        | Node: Compare 
        

            v = float.less_equal(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Float (self) 
            - b : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
            - mode      : 'ELEMENT' 
            - operation : 'LESS_EQUAL' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL').result

    def greater_than(self, b=None):
        """ greater_than
        

        | Node: Compare 
        

            v = float.greater_than(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Float (self) 
            - b : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
            - mode      : 'ELEMENT' 
            - operation : 'GREATER_THAN' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN').result

    def greater_equal(self, b=None):
        """ greater_equal
        

        | Node: Compare 
        

            v = float.greater_equal(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Float (self) 
            - b : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
            - mode      : 'ELEMENT' 
            - operation : 'GREATER_EQUAL' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL').result

    def equal(self, b=None, epsilon=None):
        """ equal
        

        | Node: Compare 
        

            v = float.equal(b, epsilon) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a       : Float (self) 
            - b       : Float 
            - epsilon : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
            - mode      : 'ELEMENT' 
            - operation : 'EQUAL' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None, epsilon=None):
        """ not_equal
        

        | Node: Compare 
        

            v = float.not_equal(b, epsilon) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a       : Float (self) 
            - b       : Float 
            - epsilon : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'FLOAT' 
            - mode      : 'ELEMENT' 
            - operation : 'NOT_EQUAL' 
        

        Node creation
        =============
        

            node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL')
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL').result

    def add(self, value1=None):
        """ add
        

        | Node: Math 
        

            v = float.add(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'ADD' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='ADD') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='ADD').value

    def subtract(self, value1=None):
        """ subtract
        

        | Node: Math 
        

            v = float.subtract(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SUBTRACT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='SUBTRACT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='SUBTRACT').value

    def multiply(self, value1=None):
        """ multiply
        

        | Node: Math 
        

            v = float.multiply(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MULTIPLY' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='MULTIPLY') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MULTIPLY').value

    def divide(self, value1=None):
        """ divide
        

        | Node: Math 
        

            v = float.divide(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'DIVIDE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='DIVIDE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='DIVIDE').value

    def multiply_add(self, value1=None, value2=None):
        """ multiply_add
        

        | Node: Math 
        

            v = float.multiply_add(value1, value2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
            - value2 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MULTIPLY_ADD' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

    def pow(self, value1=None):
        """ pow
        

        | Node: Math 
        

            v = float.pow(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'POWER' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='POWER') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='POWER').value

    def log(self, value1=None):
        """ log
        

        | Node: Math 
        

            v = float.log(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'LOGARITHM' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='LOGARITHM') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='LOGARITHM').value

    def sqrt(self):
        """ sqrt
        

        | Node: Math 
        

            v = float.sqrt() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SQRT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='SQRT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SQRT').value

    def inverse_sqrt(self):
        """ inverse_sqrt
        

        | Node: Math 
        

            v = float.inverse_sqrt() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'INVERSE_SQRT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='INVERSE_SQRT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='INVERSE_SQRT').value

    def abs(self):
        """ abs
        

        | Node: Math 
        

            v = float.abs() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ABSOLUTE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='ABSOLUTE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ABSOLUTE').value

    def exp(self):
        """ exp
        

        | Node: Math 
        

            v = float.exp() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'EXPONENT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='EXPONENT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='EXPONENT').value

    def min(self, value1=None):
        """ min
        

        | Node: Math 
        

            v = float.min(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MINIMUM' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='MINIMUM') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MINIMUM').value

    def max(self, value1=None):
        """ max
        

        | Node: Math 
        

            v = float.max(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MAXIMUM' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='MAXIMUM') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MAXIMUM').value

    def less_than(self, value1=None):
        """ less_than
        

        | Node: Math 
        

            v = float.less_than(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'LESS_THAN' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='LESS_THAN') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='LESS_THAN').value

    def greater_than(self, value1=None):
        """ greater_than
        

        | Node: Math 
        

            v = float.greater_than(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'GREATER_THAN' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='GREATER_THAN') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='GREATER_THAN').value

    def sign(self):
        """ sign
        

        | Node: Math 
        

            v = float.sign() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SIGN' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='SIGN') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SIGN').value

    def compare(self, value1=None, value2=None):
        """ compare
        

        | Node: Math 
        

            v = float.compare(value1, value2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
            - value2 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'COMPARE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE').value

    def smooth_min(self, value1=None, value2=None):
        """ smooth_min
        

        | Node: Math 
        

            v = float.smooth_min(value1, value2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
            - value2 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SMOOTH_MIN' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN').value

    def smooth_max(self, value1=None, value2=None):
        """ smooth_max
        

        | Node: Math 
        

            v = float.smooth_max(value1, value2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
            - value2 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SMOOTH_MAX' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX').value

    def round(self):
        """ round
        

        | Node: Math 
        

            v = float.round() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ROUND' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='ROUND') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ROUND').value

    def floor(self):
        """ floor
        

        | Node: Math 
        

            v = float.floor() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'FLOOR' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='FLOOR') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='FLOOR').value

    def ceil(self):
        """ ceil
        

        | Node: Math 
        

            v = float.ceil() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'CEIL' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='CEIL') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='CEIL').value

    def trunc(self):
        """ trunc
        

        | Node: Math 
        

            v = float.trunc() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TRUNC' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='TRUNC') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='TRUNC').value

    def fract(self):
        """ fract
        

        | Node: Math 
        

            v = float.fract() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'FRACT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='FRACT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='FRACT').value

    def modulo(self, value1=None):
        """ modulo
        

        | Node: Math 
        

            v = float.modulo(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MODULO' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='MODULO') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MODULO').value

    def wrap(self, value1=None, value2=None):
        """ wrap
        

        | Node: Math 
        

            v = float.wrap(value1, value2) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
            - value2 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'WRAP' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP').value

    def snap(self, value1=None):
        """ snap
        

        | Node: Math 
        

            v = float.snap(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SNAP' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='SNAP') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='SNAP').value

    def pingpong(self, value1=None):
        """ pingpong
        

        | Node: Math 
        

            v = float.pingpong(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'PINGPONG' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='PINGPONG') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='PINGPONG').value

    def sin(self):
        """ sin
        

        | Node: Math 
        

            v = float.sin() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SINE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='SINE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SINE').value

    def cos(self):
        """ cos
        

        | Node: Math 
        

            v = float.cos() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'COSINE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='COSINE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='COSINE').value

    def tan(self):
        """ tan
        

        | Node: Math 
        

            v = float.tan() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TANGENT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='TANGENT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='TANGENT').value

    def arcsin(self):
        """ arcsin
        

        | Node: Math 
        

            v = float.arcsin() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ARCSINE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='ARCSINE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ARCSINE').value

    def arccos(self):
        """ arccos
        

        | Node: Math 
        

            v = float.arccos() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ARCCOSINE' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='ARCCOSINE') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ARCCOSINE').value

    def arctan(self):
        """ arctan
        

        | Node: Math 
        

            v = float.arctan() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ARCTANGENT' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='ARCTANGENT') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ARCTANGENT').value

    def arctan2(self, value1=None):
        """ arctan2
        

        | Node: Math 
        

            v = float.arctan2(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'ARCTAN2' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, value1=value1, operation='ARCTAN2') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='ARCTAN2').value

    def sinh(self):
        """ sinh
        

        | Node: Math 
        

            v = float.sinh() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SINH' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='SINH') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SINH').value

    def cosh(self):
        """ cosh
        

        | Node: Math 
        

            v = float.cosh() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'COSH' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='COSH') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='COSH').value

    def tanh(self):
        """ tanh
        

        | Node: Math 
        

            v = float.tanh() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TANH' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='TANH') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='TANH').value

    def radians(self):
        """ radians
        

        | Node: Math 
        

            v = float.radians() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'RADIANS' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='RADIANS') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='RADIANS').value

    def degrees(self):
        """ degrees
        

        | Node: Math 
        

            v = float.degrees() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'DEGREES' 
        

        Node creation
        =============
        

            node = nodes.Math(value0=self, operation='DEGREES') 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='DEGREES').value

    def to_integer(self, rounding_mode='ROUND'):
        """ to_integer
        

        | Node: FloatToInteger 
        

            v = float.to_integer(rounding_mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - float : Float (self) 
        

            Parameters arguments
            --------------------
            - rounding_mode : 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE] 
        

        Node creation
        =============
        

            node = nodes.FloatToInteger(float=self, rounding_mode=rounding_mode) 
        

        Returns
        =======
                Integer 
        """

        return nodes.FloatToInteger(float=self, rounding_mode=rounding_mode).integer

    def to_string(self, decimals=None):
        """ to_string
        

        | Node: ValueToString 
        

            v = float.to_string(decimals) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Float (self) 
            - decimals : Integer 
        

        Node creation
        =============
        

            node = nodes.ValueToString(value=self, decimals=decimals) 
        

        Returns
        =======
                String 
        """

        return nodes.ValueToString(value=self, decimals=decimals).string

    def color_ramp(self):
        """ color_ramp
        

        | Node: Colorramp 
        

            v = float.color_ramp() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - fac : Float (self) 
        

        Node creation
        =============
        

            node = nodes.Colorramp(fac=self) 
        

        Returns
        =======
                Sockets [color (Color), alpha (Float)] 
        """

        return nodes.Colorramp(fac=self)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curve(self, value=None):
        """ curve
        

        | Node: FloatCurve 
        

            float.curve(value) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - factor : Float (self) 
            - value  : Float 
        

        Node creation
        =============
        

            node = nodes.FloatCurve(factor=self, value=value) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.FloatCurve(factor=self, value=value))

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        """ clamp
        

        | Node: Clamp 
        

            float.clamp(min, max, clamp_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value : Float (self) 
            - min   : Float 
            - max   : Float 
        

            Parameters arguments
            --------------------
            - clamp_type : 'MINMAX' in [MINMAX, RANGE] 
        

        Node creation
        =============
        

            node = nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type))


