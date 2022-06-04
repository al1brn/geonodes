import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Integer

class Integer(dsock.Integer):
    """ Class Integer
    

    | Inherits from: dsock.Integer 
    

    Constructors
    ============
    - Random : value (Integer) 
    

    Methods
    =======
    - abs                : value (Float) 
    - accumulate_field   : Sockets      [leading (Integer), trailing (Integer), total (Integer)] 
    - add                : value (Float) 
    - arccos             : value (Float) 
    - arcsin             : value (Float) 
    - arctan             : value (Float) 
    - arctan2            : value (Float) 
    - capture_attribute  : Sockets      [geometry (Geometry), attribute (Integer)] 
    - ceil               : value (Float) 
    - compare            : value (Float) 
    - cos                : value (Float) 
    - cosh               : value (Float) 
    - degrees            : value (Float) 
    - divide             : value (Float) 
    - equal              : result (Boolean) 
    - exp                : value (Float) 
    - field_at_index     : value (Integer) 
    - floor              : value (Float) 
    - fract              : value (Float) 
    - greater_equal      : result (Boolean) 
    - greater_than       : result (Boolean) 
    - greater_than       : value (Float) 
    - inverse_sqrt       : value (Float) 
    - less_equal         : result (Boolean) 
    - less_than          : result (Boolean) 
    - less_than          : value (Float) 
    - log                : value (Float) 
    - max                : value (Float) 
    - min                : value (Float) 
    - modulo             : value (Float) 
    - multiply           : value (Float) 
    - multiply_add       : value (Float) 
    - not_equal          : result (Boolean) 
    - pingpong           : value (Float) 
    - pow                : value (Float) 
    - radians            : value (Float) 
    - raycast            : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float),
      attribute (Integer)] 
    - round              : value (Float) 
    - sign               : value (Float) 
    - sin                : value (Float) 
    - sinh               : value (Float) 
    - smooth_max         : value (Float) 
    - smooth_min         : value (Float) 
    - snap               : value (Float) 
    - sqrt               : value (Float) 
    - subtract           : value (Float) 
    - switch             : output (Integer) 
    - tan                : value (Float) 
    - tanh               : value (Float) 
    - transfer_attribute : attribute (Integer) 
    - trunc              : value (Float) 
    - wrap               : value (Float) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Random
        

        | Node: RandomValue 
        

            v = Integer.Random(min, max, ID, seed) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - min  : Integer 
            - max  : Integer 
            - ID   : Integer 
            - seed : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

        Returns
        =======
                Integer 
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ accumulate_field
        

        | Node: AccumulateField 
        

            v = integer.accumulate_field(group_index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value       : Integer (self) 
            - group_index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Returns
        =======
                Sockets [leading (Integer), trailing (Integer), total (Integer)] 
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_attribute
        

        | Node: TransferAttribute 
        

            v = integer.transfer_attribute(source, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Integer (self) 
            - source          : Geometry 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Returns
        =======
                Integer 
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ capture_attribute
        

        | Node: CaptureAttribute 
        

            v = integer.capture_attribute(geometry, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Integer (self) 
            - geometry : Geometry 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Returns
        =======
                Sockets [geometry (Geometry), attribute (Integer)] 
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain)

    def field_at_index(self, value=None, domain='POINT'):
        """ field_at_index
        

        | Node: FieldAtIndex 
        

            v = integer.field_at_index(value, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - index : Integer (self) 
            - value : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Returns
        =======
                Integer 
        """

        return nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ raycast
        

        | Node: Raycast 
        

            v = integer.raycast(target_geometry, source_position, ray_direction, ray_length, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Integer (self) 
            - target_geometry : Geometry 
            - source_position : Vector 
            - ray_direction   : Vector 
            - ray_length      : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
        

            Parameters arguments
            --------------------
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST] 
        

        Returns
        =======
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute
                (Integer)] 
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping)

    def switch(self, switch0=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = integer.switch(switch0, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Integer (self) 
            - switch0 : Boolean 
            - true    : Integer 
        

            Fixed parameters
            ----------------
            - input_type : 'INT' 
        

        Returns
        =======
                Integer 
        """

        return nodes.Switch(false=self, switch0=switch0, true=true, input_type='INT').output

    def less_than(self, b=None):
        """ less_than
        

        | Node: Compare 
        

            v = integer.less_than(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Integer (self) 
            - b : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
            - mode      : 'ELEMENT' 
            - operation : 'LESS_THAN' 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN').result

    def less_equal(self, b=None):
        """ less_equal
        

        | Node: Compare 
        

            v = integer.less_equal(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Integer (self) 
            - b : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
            - mode      : 'ELEMENT' 
            - operation : 'LESS_EQUAL' 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL').result

    def greater_than(self, b=None):
        """ greater_than
        

        | Node: Compare 
        

            v = integer.greater_than(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Integer (self) 
            - b : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
            - mode      : 'ELEMENT' 
            - operation : 'GREATER_THAN' 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN').result

    def greater_equal(self, b=None):
        """ greater_equal
        

        | Node: Compare 
        

            v = integer.greater_equal(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Integer (self) 
            - b : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
            - mode      : 'ELEMENT' 
            - operation : 'GREATER_EQUAL' 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL').result

    def equal(self, b=None):
        """ equal
        

        | Node: Compare 
        

            v = integer.equal(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Integer (self) 
            - b : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
            - mode      : 'ELEMENT' 
            - operation : 'EQUAL' 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None):
        """ not_equal
        

        | Node: Compare 
        

            v = integer.not_equal(b) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - a : Integer (self) 
            - b : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'INT' 
            - mode      : 'ELEMENT' 
            - operation : 'NOT_EQUAL' 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL').result

    def add(self, value1=None):
        """ add
        

        | Node: Math 
        

            v = integer.add(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'ADD' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='ADD').value

    def subtract(self, value1=None):
        """ subtract
        

        | Node: Math 
        

            v = integer.subtract(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SUBTRACT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='SUBTRACT').value

    def multiply(self, value1=None):
        """ multiply
        

        | Node: Math 
        

            v = integer.multiply(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MULTIPLY' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MULTIPLY').value

    def divide(self, value1=None):
        """ divide
        

        | Node: Math 
        

            v = integer.divide(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'DIVIDE' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='DIVIDE').value

    def multiply_add(self, value1=None, value2=None):
        """ multiply_add
        

        | Node: Math 
        

            v = integer.multiply_add(value1, value2) 
        

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
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

    def pow(self, value1=None):
        """ pow
        

        | Node: Math 
        

            v = integer.pow(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'POWER' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='POWER').value

    def log(self, value1=None):
        """ log
        

        | Node: Math 
        

            v = integer.log(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'LOGARITHM' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='LOGARITHM').value

    def sqrt(self):
        """ sqrt
        

        | Node: Math 
        

            v = integer.sqrt() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SQRT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SQRT').value

    def inverse_sqrt(self):
        """ inverse_sqrt
        

        | Node: Math 
        

            v = integer.inverse_sqrt() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'INVERSE_SQRT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='INVERSE_SQRT').value

    def abs(self):
        """ abs
        

        | Node: Math 
        

            v = integer.abs() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ABSOLUTE' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ABSOLUTE').value

    def exp(self):
        """ exp
        

        | Node: Math 
        

            v = integer.exp() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'EXPONENT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='EXPONENT').value

    def min(self, value1=None):
        """ min
        

        | Node: Math 
        

            v = integer.min(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MINIMUM' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MINIMUM').value

    def max(self, value1=None):
        """ max
        

        | Node: Math 
        

            v = integer.max(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MAXIMUM' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MAXIMUM').value

    def less_than(self, value1=None):
        """ less_than
        

        | Node: Math 
        

            v = integer.less_than(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'LESS_THAN' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='LESS_THAN').value

    def greater_than(self, value1=None):
        """ greater_than
        

        | Node: Math 
        

            v = integer.greater_than(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'GREATER_THAN' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='GREATER_THAN').value

    def sign(self):
        """ sign
        

        | Node: Math 
        

            v = integer.sign() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SIGN' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SIGN').value

    def compare(self, value1=None, value2=None):
        """ compare
        

        | Node: Math 
        

            v = integer.compare(value1, value2) 
        

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
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE').value

    def smooth_min(self, value1=None, value2=None):
        """ smooth_min
        

        | Node: Math 
        

            v = integer.smooth_min(value1, value2) 
        

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
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN').value

    def smooth_max(self, value1=None, value2=None):
        """ smooth_max
        

        | Node: Math 
        

            v = integer.smooth_max(value1, value2) 
        

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
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX').value

    def round(self):
        """ round
        

        | Node: Math 
        

            v = integer.round() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ROUND' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ROUND').value

    def floor(self):
        """ floor
        

        | Node: Math 
        

            v = integer.floor() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'FLOOR' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='FLOOR').value

    def ceil(self):
        """ ceil
        

        | Node: Math 
        

            v = integer.ceil() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'CEIL' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='CEIL').value

    def trunc(self):
        """ trunc
        

        | Node: Math 
        

            v = integer.trunc() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TRUNC' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='TRUNC').value

    def fract(self):
        """ fract
        

        | Node: Math 
        

            v = integer.fract() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'FRACT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='FRACT').value

    def modulo(self, value1=None):
        """ modulo
        

        | Node: Math 
        

            v = integer.modulo(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'MODULO' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='MODULO').value

    def wrap(self, value1=None, value2=None):
        """ wrap
        

        | Node: Math 
        

            v = integer.wrap(value1, value2) 
        

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
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP').value

    def snap(self, value1=None):
        """ snap
        

        | Node: Math 
        

            v = integer.snap(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'SNAP' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='SNAP').value

    def pingpong(self, value1=None):
        """ pingpong
        

        | Node: Math 
        

            v = integer.pingpong(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'PINGPONG' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='PINGPONG').value

    def sin(self):
        """ sin
        

        | Node: Math 
        

            v = integer.sin() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SINE' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SINE').value

    def cos(self):
        """ cos
        

        | Node: Math 
        

            v = integer.cos() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'COSINE' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='COSINE').value

    def tan(self):
        """ tan
        

        | Node: Math 
        

            v = integer.tan() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TANGENT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='TANGENT').value

    def arcsin(self):
        """ arcsin
        

        | Node: Math 
        

            v = integer.arcsin() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ARCSINE' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ARCSINE').value

    def arccos(self):
        """ arccos
        

        | Node: Math 
        

            v = integer.arccos() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ARCCOSINE' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ARCCOSINE').value

    def arctan(self):
        """ arctan
        

        | Node: Math 
        

            v = integer.arctan() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'ARCTANGENT' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='ARCTANGENT').value

    def arctan2(self, value1=None):
        """ arctan2
        

        | Node: Math 
        

            v = integer.arctan2(value1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
            - value1 : Float 
        

            Fixed parameters
            ----------------
            - operation : 'ARCTAN2' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, value1=value1, operation='ARCTAN2').value

    def sinh(self):
        """ sinh
        

        | Node: Math 
        

            v = integer.sinh() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'SINH' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='SINH').value

    def cosh(self):
        """ cosh
        

        | Node: Math 
        

            v = integer.cosh() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'COSH' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='COSH').value

    def tanh(self):
        """ tanh
        

        | Node: Math 
        

            v = integer.tanh() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'TANH' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='TANH').value

    def radians(self):
        """ radians
        

        | Node: Math 
        

            v = integer.radians() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'RADIANS' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='RADIANS').value

    def degrees(self):
        """ degrees
        

        | Node: Math 
        

            v = integer.degrees() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value0 : Float (self) 
        

            Fixed parameters
            ----------------
            - operation : 'DEGREES' 
        

        Returns
        =======
                Float 
        """

        return nodes.Math(value0=self, operation='DEGREES').value


