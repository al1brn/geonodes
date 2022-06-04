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
    - Random : value (Float) 
    

    Methods
    =======
    - abs                 : value (Float) 
    - accumulate_field    : Sockets      [leading (Float), trailing (Float), total (Float)] 
    - add                 : value (Float) 
    - arccos              : value (Float) 
    - arcsin              : value (Float) 
    - arctan              : value (Float) 
    - arctan2             : value (Float) 
    - attribute_statistic : Sockets      [mean (Float), median (Float), sum (Float), min (Float), max (Float),
      range (Float), standard_deviation (Float), variance (Float)] 
    - capture_attribute   : Sockets      [geometry (Geometry), attribute (Float)] 
    - ceil                : value (Float) 
    - color_ramp          : Sockets      [color (Color), alpha (Float)] 
    - compare             : value (Float) 
    - cos                 : value (Float) 
    - cosh                : value (Float) 
    - degrees             : value (Float) 
    - divide              : value (Float) 
    - equal               : result (Boolean) 
    - exp                 : value (Float) 
    - field_at_index      : value (Float) 
    - floor               : value (Float) 
    - fract               : value (Float) 
    - greater_equal       : result (Boolean) 
    - greater_than        : result (Boolean) 
    - greater_than        : value (Float) 
    - inverse_sqrt        : value (Float) 
    - less_equal          : result (Boolean) 
    - less_than           : result (Boolean) 
    - less_than           : value (Float) 
    - log                 : value (Float) 
    - map_range           : result (Float) 
    - max                 : value (Float) 
    - min                 : value (Float) 
    - modulo              : value (Float) 
    - multiply            : value (Float) 
    - multiply_add        : value (Float) 
    - not_equal           : result (Boolean) 
    - pingpong            : value (Float) 
    - pow                 : value (Float) 
    - radians             : value (Float) 
    - raycast             : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float),
      attribute (Float)] 
    - round               : value (Float) 
    - sign                : value (Float) 
    - sin                 : value (Float) 
    - sinh                : value (Float) 
    - smooth_max          : value (Float) 
    - smooth_min          : value (Float) 
    - snap                : value (Float) 
    - sqrt                : value (Float) 
    - subtract            : value (Float) 
    - switch              : output (Float) 
    - tan                 : value (Float) 
    - tanh                : value (Float) 
    - to_integer          : integer (Integer) 
    - to_string           : string (String) 
    - transfer_attribute  : attribute (Float) 
    - trunc               : value (Float) 
    - wrap                : value (Float) 
    

    Stacked methods
    ===============
    - clamp : Float 
    - curve : Float 
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """Call node RandomValue (FunctionNodeRandomValue)

        Sockets arguments
        -----------------
            min            : Float
            max            : Float
            ID             : Integer
            seed           : Integer

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Float
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT'):
        """Call node AccumulateField (GeometryNodeAccumulateField)

        Sockets arguments
        -----------------
            value          : Float (self)
            group_index    : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Sockets [leading (Float), trailing (Float), total (Float)]
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT'):
        """Call node AttributeStatistic (GeometryNodeAttributeStatistic)

        Sockets arguments
        -----------------
            attribute      : Float (self)
            geometry       : Geometry
            selection      : Boolean

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            attribute      : Float (self)
            source         : Geometry
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """Call node CaptureAttribute (GeometryNodeCaptureAttribute)

        Sockets arguments
        -----------------
            value          : Float (self)
            geometry       : Geometry

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Float)]
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """Call node FieldAtIndex (GeometryNodeFieldAtIndex)

        Sockets arguments
        -----------------
            value          : Float (self)
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """Call node Raycast (GeometryNodeRaycast)

        Sockets arguments
        -----------------
            attribute      : Float (self)
            target_geometry: Geometry
            source_position: Vector
            ray_direction  : Vector
            ray_length     : Float

        Parameters arguments
        --------------------
            mapping        : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping)

    def switch(self, switch0=None, true=None):
        """Call node Switch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Float (self)
            switch0        : Boolean
            true           : Float

        Fixed parameters
        ----------------
            input_type     : 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.Switch(false=self, switch0=switch0, true=true, input_type='FLOAT').output

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR'):
        """Call node MapRange (ShaderNodeMapRange)

        Sockets arguments
        -----------------
            value          : Float (self)
            from_min       : Float
            from_max       : Float
            to_min         : Float
            to_max         : Float

        Parameters arguments
        --------------------
            clamp          : True
            interpolation_type: 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type).result

    def less_than(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Float (self)
            b              : Float

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'
            mode           : 'ELEMENT'
            operation      : 'LESS_THAN'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN').result

    def less_equal(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Float (self)
            b              : Float

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'
            mode           : 'ELEMENT'
            operation      : 'LESS_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL').result

    def greater_than(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Float (self)
            b              : Float

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'
            mode           : 'ELEMENT'
            operation      : 'GREATER_THAN'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN').result

    def greater_equal(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Float (self)
            b              : Float

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'
            mode           : 'ELEMENT'
            operation      : 'GREATER_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL').result

    def equal(self, b=None, epsilon=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Float (self)
            b              : Float
            epsilon        : Float

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'
            mode           : 'ELEMENT'
            operation      : 'EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL').result

    def not_equal(self, b=None, epsilon=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Float (self)
            b              : Float
            epsilon        : Float

        Fixed parameters
        ----------------
            data_type      : 'FLOAT'
            mode           : 'ELEMENT'
            operation      : 'NOT_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL').result

    def add(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'ADD'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='ADD').value

    def subtract(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'SUBTRACT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='SUBTRACT').value

    def multiply(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='MULTIPLY').value

    def divide(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'DIVIDE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='DIVIDE').value

    def multiply_add(self, value1=None, value2=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY_ADD'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

    def pow(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'POWER'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='POWER').value

    def log(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'LOGARITHM'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='LOGARITHM').value

    def sqrt(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'SQRT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='SQRT').value

    def inverse_sqrt(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'INVERSE_SQRT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='INVERSE_SQRT').value

    def abs(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'ABSOLUTE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='ABSOLUTE').value

    def exp(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'EXPONENT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='EXPONENT').value

    def min(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'MINIMUM'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='MINIMUM').value

    def max(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'MAXIMUM'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='MAXIMUM').value

    def less_than(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'LESS_THAN'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='LESS_THAN').value

    def greater_than(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'GREATER_THAN'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='GREATER_THAN').value

    def sign(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'SIGN'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='SIGN').value

    def compare(self, value1=None, value2=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'COMPARE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE').value

    def smooth_min(self, value1=None, value2=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SMOOTH_MIN'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN').value

    def smooth_max(self, value1=None, value2=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SMOOTH_MAX'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX').value

    def round(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'ROUND'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='ROUND').value

    def floor(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'FLOOR'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='FLOOR').value

    def ceil(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'CEIL'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='CEIL').value

    def trunc(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'TRUNC'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='TRUNC').value

    def fract(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'FRACT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='FRACT').value

    def modulo(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'MODULO'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='MODULO').value

    def wrap(self, value1=None, value2=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'WRAP'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP').value

    def snap(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'SNAP'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='SNAP').value

    def pingpong(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'PINGPONG'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='PINGPONG').value

    def sin(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'SINE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='SINE').value

    def cos(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'COSINE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='COSINE').value

    def tan(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'TANGENT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='TANGENT').value

    def arcsin(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'ARCSINE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='ARCSINE').value

    def arccos(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'ARCCOSINE'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='ARCCOSINE').value

    def arctan(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'ARCTANGENT'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='ARCTANGENT').value

    def arctan2(self, value1=None):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float

        Fixed parameters
        ----------------
            operation      : 'ARCTAN2'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, value1=value1, operation='ARCTAN2').value

    def sinh(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'SINH'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='SINH').value

    def cosh(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'COSH'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='COSH').value

    def tanh(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'TANH'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='TANH').value

    def radians(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'RADIANS'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='RADIANS').value

    def degrees(self):
        """Call node Math (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)

        Fixed parameters
        ----------------
            operation      : 'DEGREES'

        Returns
        -------
            Float
        """

        return nodes.Math(value0=self, operation='DEGREES').value

    def to_integer(self, rounding_mode='ROUND'):
        """Call node FloatToInteger (FunctionNodeFloatToInt)

        Sockets arguments
        -----------------
            float          : Float (self)

        Parameters arguments
        --------------------
            rounding_mode  : 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

        Returns
        -------
            Integer
        """

        return nodes.FloatToInteger(float=self, rounding_mode=rounding_mode).integer

    def to_string(self, decimals=None):
        """Call node ValueToString (FunctionNodeValueToString)

        Sockets arguments
        -----------------
            value          : Float (self)
            decimals       : Integer

        Returns
        -------
            String
        """

        return nodes.ValueToString(value=self, decimals=decimals).string

    def color_ramp(self):
        """Call node Colorramp (ShaderNodeValToRGB)

        Sockets arguments
        -----------------
            fac            : Float (self)

        Returns
        -------
            Sockets [color (Color), alpha (Float)]
        """

        return nodes.Colorramp(fac=self)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curve(self, value=None):
        """Call node FloatCurve (ShaderNodeFloatCurve)

        Sockets arguments
        -----------------
            factor         : Float (self)
            value          : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.FloatCurve(factor=self, value=value))

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        """Call node Clamp (ShaderNodeClamp)

        Sockets arguments
        -----------------
            value          : Float (self)
            min            : Float
            max            : Float

        Parameters arguments
        --------------------
            clamp_type     : 'MINMAX' in [MINMAX, RANGE]

        Returns
        -------
            self

        """

        return self.stack(nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type))


