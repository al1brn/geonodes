from geonodes import baseclasses as bcls
from geonodes import nodes

# ----------------------------------------------------------------------------------------------------
# Argument is a vector

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ----------------------------------------------------------------------------------------------------
# Sockets outputs

class Sockets:
    def __init__(self, **kwargs):
        for k, w in kwargs.items():
            setattr(self, k, w)


# ==============================================================================================================
# Data class Boolean

class Boolean(bcls.Boolean):
    """ Socket data class Boolean

    Constructors
    ------------
        Random               : FunctionNodeRandomValue  (data_type = BOOLEAN)

    Methods
    -------
        b_and                : FunctionNodeBooleanMath  (operation = AND)
        b_not                : FunctionNodeBooleanMath  (operation = NOT)
        b_or                 : FunctionNodeBooleanMath  (operation = OR)
        imply                : FunctionNodeBooleanMath  (operation = IMPLY)
        nand                 : FunctionNodeBooleanMath  (operation = NAND)
        nimply               : FunctionNodeBooleanMath  (operation = NIMPLY)
        nor                  : FunctionNodeBooleanMath  (operation = NOR)
        switch               : GeometryNodeSwitch       (input_type = BOOLEAN)
        to_viewer            : node GeometryNodeViewer(data_type = BOOLEAN)
        xnor                 : FunctionNodeBooleanMath  (operation = XNOR)
        xor                  : FunctionNodeBooleanMath  (operation = XOR)

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        return Boolean(NodeRandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def b_and(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean)

    def b_or(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean)

    def b_not(self):
        return Boolean(NodeBooleanMath(boolean0=self, operation='NOT').boolean)

    def nand(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean)

    def nor(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean)

    def xnor(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean)

    def xor(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean)

    def imply(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean)

    def nimply(self, boolean1=None):
        return Boolean(NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean)

    def switch(self, false=None, true=None):
        return Boolean(NodeSwitch(switch=self, false=false, true=true, input_type='BOOLEAN').output)

    def to_viewer(self, geometry=None):
        return NodeViewer(value=self, geometry=geometry, data_type='BOOLEAN')


# ==============================================================================================================
# Data class Integer

class Integer(bcls.IntFloat):
    """ Socket data class Integer

    Constructors
    ------------
        Random               : FunctionNodeRandomValue  (data_type = INT)

    Methods
    -------
        abs                  : (Integer) ShaderNodeMath           (operation = ABSOLUTE)
        add                  : (Integer) ShaderNodeMath           (operation = ADD)
        arccos               : (Float) ShaderNodeMath           (operation = ARCCOSINE)
        arcsin               : (Float) ShaderNodeMath           (operation = ARCSINE)
        arctan               : (Float) ShaderNodeMath           (operation = ARCTANGENT)
        arctan2              : (Float) ShaderNodeMath           (operation = ARCTAN2)
        ceil                 : (Integer) ShaderNodeMath           (operation = CEIL)
        compare              : ShaderNodeMath           (operation = COMPARE)
        cos                  : (Float) ShaderNodeMath           (operation = COSINE)
        cosh                 : (Float) ShaderNodeMath           (operation = COSH)
        degrees              : (Float) ShaderNodeMath           (operation = DEGREES)
        divide               : (Float) ShaderNodeMath           (operation = DIVIDE)
        exp                  : (Float) ShaderNodeMath           (operation = EXPONENT)
        floor                : (Integer) ShaderNodeMath           (operation = FLOOR)
        fract                : (Float) ShaderNodeMath           (operation = FRACT)
        greater_than         : (Boolean) ShaderNodeMath           (operation = GREATER_THAN)
        inverse_sqrt         : (Float) ShaderNodeMath           (operation = INVERSE_SQRT)
        less_than            : (Boolean) ShaderNodeMath           (operation = LESS_THAN)
        log                  : (Float) ShaderNodeMath           (operation = LOGARITHM)
        max                  : (Integer) ShaderNodeMath           (operation = MAXIMUM)
        min                  : (Integer) ShaderNodeMath           (operation = MINIMUM)
        modulo               : (Integer) ShaderNodeMath           (operation = MODULO)
        multiply             : (Integer) ShaderNodeMath           (operation = MULTIPLY)
        multiply_add         : (Integer) ShaderNodeMath           (operation = MULTIPLY_ADD)
        pingpong             : (Integer) ShaderNodeMath           (operation = PINGPONG)
        pow                  : (Integer) ShaderNodeMath           (operation = POWER)
        radians              : (Float) ShaderNodeMath           (operation = RADIANS)
        round                : (Integer) ShaderNodeMath           (operation = ROUND)
        sign                 : (Integer) ShaderNodeMath           (operation = SIGN)
        sin                  : (Float) ShaderNodeMath           (operation = SINE)
        sinh                 : (Float) ShaderNodeMath           (operation = SINH)
        smooth_max           : (Integer) ShaderNodeMath           (operation = SMOOTH_MAX)
        smooth_min           : (Integer) ShaderNodeMath           (operation = SMOOTH_MIN)
        snap                 : ShaderNodeMath           (operation = SNAP)
        sqrt                 : (Float) ShaderNodeMath           (operation = SQRT)
        substract            : (Integer) ShaderNodeMath           (operation = SUBTRACT)
        switch               : GeometryNodeSwitch       (input_type = INT)
        tan                  : (Float) ShaderNodeMath           (operation = TANGENT)
        tanh                 : (Float) ShaderNodeMath           (operation = TANH)
        to_viewer            : node GeometryNodeViewer(data_type = INT)
        trunc                : (Integer) ShaderNodeMath           (operation = TRUNC)
        wrap                 : ShaderNodeMath           (operation = WRAP)

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        return Integer(NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='ADD', use_clamp=use_clamp).value)

    def substract(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='SUBTRACT', use_clamp=use_clamp).value)

    def multiply(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MULTIPLY', use_clamp=use_clamp).value)

    def divide(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='DIVIDE', use_clamp=use_clamp).value)

    def multiply_add(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='MULTIPLY_ADD', use_clamp=use_clamp).value)

    def pow(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='POWER', use_clamp=use_clamp).value)

    def log(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='LOGARITHM', use_clamp=use_clamp).value)

    def sqrt(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SQRT', use_clamp=use_clamp).value)

    def inverse_sqrt(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='INVERSE_SQRT', use_clamp=use_clamp).value)

    def abs(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ABSOLUTE', use_clamp=use_clamp).value)

    def exp(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='EXPONENT', use_clamp=use_clamp).value)

    def min(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MINIMUM', use_clamp=use_clamp).value)

    def max(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MAXIMUM', use_clamp=use_clamp).value)

    def less_than(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='LESS_THAN', use_clamp=use_clamp).value)

    def greater_than(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='GREATER_THAN', use_clamp=use_clamp).value)

    def sign(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SIGN', use_clamp=use_clamp).value)

    def compare(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='COMPARE', use_clamp=use_clamp).value)

    def smooth_min(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='SMOOTH_MIN', use_clamp=use_clamp).value)

    def smooth_max(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='SMOOTH_MAX', use_clamp=use_clamp).value)

    def round(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ROUND', use_clamp=use_clamp).value)

    def floor(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='FLOOR', use_clamp=use_clamp).value)

    def ceil(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='CEIL', use_clamp=use_clamp).value)

    def trunc(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='TRUNC', use_clamp=use_clamp).value)

    def fract(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='FRACT', use_clamp=use_clamp).value)

    def modulo(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MODULO', use_clamp=use_clamp).value)

    def wrap(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='WRAP', use_clamp=use_clamp).value)

    def snap(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='SNAP', use_clamp=use_clamp).value)

    def pingpong(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='PINGPONG', use_clamp=use_clamp).value)

    def sin(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SINE', use_clamp=use_clamp).value)

    def cos(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='COSINE', use_clamp=use_clamp).value)

    def tan(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='TANGENT', use_clamp=use_clamp).value)

    def arcsin(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ARCSINE', use_clamp=use_clamp).value)

    def arccos(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ARCCOSINE', use_clamp=use_clamp).value)

    def arctan(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ARCTANGENT', use_clamp=use_clamp).value)

    def arctan2(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='ARCTAN2', use_clamp=use_clamp).value)

    def sinh(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SINH', use_clamp=use_clamp).value)

    def cosh(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='COSH', use_clamp=use_clamp).value)

    def tanh(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='TANH', use_clamp=use_clamp).value)

    def radians(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='RADIANS', use_clamp=use_clamp).value)

    def degrees(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='DEGREES', use_clamp=use_clamp).value)

    def switch(self, switch=None, true=None):
        return Integer(NodeSwitch(false=self, switch=switch, true=true, input_type='INT').output)

    def to_viewer(self, geometry=None):
        return NodeViewer(value=self, geometry=geometry, data_type='INT')


# ==============================================================================================================
# Data class Float

class Float(bcls.IntFloat):
    """ Socket data class Float

    Constructors
    ------------
        Random               : FunctionNodeRandomValue  (data_type = FLOAT)

    Methods
    -------
        abs                  : (Float) ShaderNodeMath           (operation = ABSOLUTE)
        add                  : (Float) ShaderNodeMath           (operation = ADD)
        arccos               : (Float) ShaderNodeMath           (operation = ARCCOSINE)
        arcsin               : (Float) ShaderNodeMath           (operation = ARCSINE)
        arctan               : (Float) ShaderNodeMath           (operation = ARCTANGENT)
        arctan2              : (Float) ShaderNodeMath           (operation = ARCTAN2)
        ceil                 : (Integer) ShaderNodeMath           (operation = CEIL)
        compare              : ShaderNodeMath           (operation = COMPARE)
        cos                  : (Float) ShaderNodeMath           (operation = COSINE)
        cosh                 : (Float) ShaderNodeMath           (operation = COSH)
        degrees              : (Float) ShaderNodeMath           (operation = DEGREES)
        divide               : (Float) ShaderNodeMath           (operation = DIVIDE)
        exp                  : (Float) ShaderNodeMath           (operation = EXPONENT)
        floor                : (Integer) ShaderNodeMath           (operation = FLOOR)
        fract                : (Float) ShaderNodeMath           (operation = FRACT)
        greater_than         : (Boolean) ShaderNodeMath           (operation = GREATER_THAN)
        inverse_sqrt         : (Float) ShaderNodeMath           (operation = INVERSE_SQRT)
        less_than            : (Boolean) ShaderNodeMath           (operation = LESS_THAN)
        log                  : (Float) ShaderNodeMath           (operation = LOGARITHM)
        max                  : (Float) ShaderNodeMath           (operation = MAXIMUM)
        min                  : (Float) ShaderNodeMath           (operation = MINIMUM)
        modulo               : (Float) ShaderNodeMath           (operation = MODULO)
        multiply             : (Float) ShaderNodeMath           (operation = MULTIPLY)
        multiply_add         : (Float) ShaderNodeMath           (operation = MULTIPLY_ADD)
        pingpong             : (Float) ShaderNodeMath           (operation = PINGPONG)
        pow                  : (Float) ShaderNodeMath           (operation = POWER)
        radians              : (Float) ShaderNodeMath           (operation = RADIANS)
        round                : (Integer) ShaderNodeMath           (operation = ROUND)
        sign                 : (Integer) ShaderNodeMath           (operation = SIGN)
        sin                  : (Float) ShaderNodeMath           (operation = SINE)
        sinh                 : (Float) ShaderNodeMath           (operation = SINH)
        smooth_max           : (Float) ShaderNodeMath           (operation = SMOOTH_MAX)
        smooth_min           : (Float) ShaderNodeMath           (operation = SMOOTH_MIN)
        snap                 : ShaderNodeMath           (operation = SNAP)
        sqrt                 : (Float) ShaderNodeMath           (operation = SQRT)
        substract            : (Float) ShaderNodeMath           (operation = SUBTRACT)
        switch               : GeometryNodeSwitch       (input_type = FLOAT)
        tan                  : (Float) ShaderNodeMath           (operation = TANGENT)
        tanh                 : (Float) ShaderNodeMath           (operation = TANH)
        to_integer           : (Integer) FunctionNodeFloatToInt   
        to_string            : (String) FunctionNodeValueToString
        to_viewer            : node GeometryNodeViewer(data_type = FLOAT)
        trunc                : (Integer) ShaderNodeMath           (operation = TRUNC)
        wrap                 : ShaderNodeMath           (operation = WRAP)

    Stacked methods
    ---------------
        curve                : node ShaderNodeFloatCurve

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        return Float(NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='ADD', use_clamp=use_clamp).value)

    def substract(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='SUBTRACT', use_clamp=use_clamp).value)

    def multiply(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MULTIPLY', use_clamp=use_clamp).value)

    def divide(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='DIVIDE', use_clamp=use_clamp).value)

    def multiply_add(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='MULTIPLY_ADD', use_clamp=use_clamp).value)

    def pow(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='POWER', use_clamp=use_clamp).value)

    def log(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='LOGARITHM', use_clamp=use_clamp).value)

    def sqrt(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SQRT', use_clamp=use_clamp).value)

    def inverse_sqrt(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='INVERSE_SQRT', use_clamp=use_clamp).value)

    def abs(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ABSOLUTE', use_clamp=use_clamp).value)

    def exp(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='EXPONENT', use_clamp=use_clamp).value)

    def min(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MINIMUM', use_clamp=use_clamp).value)

    def max(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MAXIMUM', use_clamp=use_clamp).value)

    def less_than(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='LESS_THAN', use_clamp=use_clamp).value)

    def greater_than(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='GREATER_THAN', use_clamp=use_clamp).value)

    def sign(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SIGN', use_clamp=use_clamp).value)

    def compare(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='COMPARE', use_clamp=use_clamp).value)

    def smooth_min(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='SMOOTH_MIN', use_clamp=use_clamp).value)

    def smooth_max(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='SMOOTH_MAX', use_clamp=use_clamp).value)

    def round(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ROUND', use_clamp=use_clamp).value)

    def floor(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='FLOOR', use_clamp=use_clamp).value)

    def ceil(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='CEIL', use_clamp=use_clamp).value)

    def trunc(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='TRUNC', use_clamp=use_clamp).value)

    def fract(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='FRACT', use_clamp=use_clamp).value)

    def modulo(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='MODULO', use_clamp=use_clamp).value)

    def wrap(self, value1=None, value=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, value=value, operation='WRAP', use_clamp=use_clamp).value)

    def snap(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='SNAP', use_clamp=use_clamp).value)

    def pingpong(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='PINGPONG', use_clamp=use_clamp).value)

    def sin(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SINE', use_clamp=use_clamp).value)

    def cos(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='COSINE', use_clamp=use_clamp).value)

    def tan(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='TANGENT', use_clamp=use_clamp).value)

    def arcsin(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ARCSINE', use_clamp=use_clamp).value)

    def arccos(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ARCCOSINE', use_clamp=use_clamp).value)

    def arctan(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='ARCTANGENT', use_clamp=use_clamp).value)

    def arctan2(self, value1=None, use_clamp=False):
        return Float(NodeMath(value0=self, value1=value1, operation='ARCTAN2', use_clamp=use_clamp).value)

    def sinh(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='SINH', use_clamp=use_clamp).value)

    def cosh(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='COSH', use_clamp=use_clamp).value)

    def tanh(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='TANH', use_clamp=use_clamp).value)

    def radians(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='RADIANS', use_clamp=use_clamp).value)

    def degrees(self, use_clamp=False):
        return Float(NodeMath(value0=self, operation='DEGREES', use_clamp=use_clamp).value)

    def switch(self, switch=None, true=None):
        return Float(NodeSwitch(false=self, switch=switch, true=true, input_type='FLOAT').output)

    def to_viewer(self, geometry=None):
        return NodeViewer(value=self, geometry=geometry, data_type='FLOAT')

    def to_integer(self, rounding_mode='ROUND'):
        return Integer(NodeFloattoInteger(float=self, rounding_mode=rounding_mode).integer)

    def to_string(self, decimals=None):
        return String(NodeValuetoString(value=self, decimals=decimals).string)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curve(self, value=None, mapping=None):
        return self.stack(NodeFloatCurve(factor=self, value=value, mapping=mapping))


# ==============================================================================================================
# Data class Vector

class Vector(bcls.Vector):
    """ Socket data class Vector

    Constructors
    ------------
        Combine              : (cls) ShaderNodeCombineXYZ     
        Random               : FunctionNodeRandomValue  (data_type = FLOAT_VECTOR)

    Node properties
    ---------------
        separate             : node ShaderNodeSeparateXYZ
        x                    : separate.x
        y                    : separate.y
        z                    : separate.z


    Methods
    -------
        absolute             : ShaderNodeVectorMath     (operation = ABSOLUTE)
        add                  : ShaderNodeVectorMath     (operation = ADD)
        align_to_vector      : (Vector) FunctionNodeAlignEulerToVector
        ceil                 : ShaderNodeVectorMath     (operation = CEIL)
        cos                  : ShaderNodeVectorMath     (operation = COSINE)
        cross                : ShaderNodeVectorMath     (operation = CROSS_PRODUCT)
        distance             : ShaderNodeVectorMath     (operation = DISTANCE)
        divide               : ShaderNodeVectorMath     (operation = DIVIDE)
        dot                  : ShaderNodeVectorMath     (operation = DOT_PRODUCT)
        faceforward          : ShaderNodeVectorMath     (operation = FACEFORWARD)
        floor                : ShaderNodeVectorMath     (operation = FLOOR)
        fraction             : ShaderNodeVectorMath     (operation = FRACTION)
        length               : ShaderNodeVectorMath     (operation = LENGTH)
        max                  : ShaderNodeVectorMath     (operation = MAXIMUM)
        min                  : ShaderNodeVectorMath     (operation = MINIMUM)
        modulo               : ShaderNodeVectorMath     (operation = MODULO)
        multiply             : ShaderNodeVectorMath     (operation = MULTIPLY)
        multiply_add         : ShaderNodeVectorMath     (operation = MULTIPLY_ADD)
        normalize            : ShaderNodeVectorMath     (operation = NORMALIZE)
        project              : ShaderNodeVectorMath     (operation = PROJECT)
        reflect              : ShaderNodeVectorMath     (operation = REFLECT)
        refract              : ShaderNodeVectorMath     (operation = REFRACT)
        rotate               : (Vector) ShaderNodeVectorRotate   
        scale                : ShaderNodeVectorMath     (operation = SCALE)
        sin                  : ShaderNodeVectorMath     (operation = SINE)
        snap                 : ShaderNodeVectorMath     (operation = SNAP)
        subtract             : ShaderNodeVectorMath     (operation = SUBTRACT)
        switch               : GeometryNodeSwitch       (input_type = VECTOR)
        tan                  : ShaderNodeVectorMath     (operation = TANGENT)
        to_viewer            : node GeometryNodeViewer(data_type = FLOAT_VECTOR)
        wrap                 : ShaderNodeVectorMath     (operation = WRAP)

    Stacked methods
    ---------------
        curves               : node ShaderNodeVectorCurve

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        return Vector(NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        return Vector(NodeCombineXYZ(x=x, y=y, z=z).vector)


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    # ---------- Node SeparateXYZ

    @property
    def separate(self):
        if not hasattr(self, 'separate_'):
            self.separate_ = NodeSeparateXYZ(vector=self)
        return self.separate_

    @property
    def x(self):
        if not hasattr(self, 'x_'):
            self.x_ = self.separate.x
        return self.x_

    @property
    def y(self):
        if not hasattr(self, 'y_'):
            self.y_ = self.separate.y
        return self.y_

    @property
    def z(self):
        if not hasattr(self, 'z_'):
            self.z_ = self.separate.z
        return self.z_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='ADD').vector)

    def subtract(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='SUBTRACT').vector)

    def multiply(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='MULTIPLY').vector)

    def divide(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='DIVIDE').vector)

    def multiply_add(self, vector1=None, vector=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, vector=vector, operation='MULTIPLY_ADD').vector)

    def cross(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT').vector)

    def project(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='PROJECT').vector)

    def reflect(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='REFLECT').vector)

    def refract(self, vector1=None, scale=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT').vector)

    def faceforward(self, vector1=None, vector=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, vector=vector, operation='FACEFORWARD').vector)

    def dot(self, vector1=None):
        return Float(NodeVectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT').value)

    def distance(self, vector1=None):
        return Float(NodeVectorMath(vector0=self, vector1=vector1, operation='DISTANCE').value)

    def length(self):
        return Float(NodeVectorMath(vector0=self, operation='LENGTH').value)

    def scale(self, scale=None):
        return Vector(NodeVectorMath(vector0=self, scale=scale, operation='SCALE').vector)

    def normalize(self):
        return Vector(NodeVectorMath(vector0=self, operation='NORMALIZE').vector)

    def absolute(self):
        return Vector(NodeVectorMath(vector0=self, operation='ABSOLUTE').vector)

    def min(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='MINIMUM').vector)

    def max(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='MAXIMUM').vector)

    def floor(self):
        return Vector(NodeVectorMath(vector0=self, operation='FLOOR').vector)

    def ceil(self):
        return Vector(NodeVectorMath(vector0=self, operation='CEIL').vector)

    def fraction(self):
        return Vector(NodeVectorMath(vector0=self, operation='FRACTION').vector)

    def modulo(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='MODULO').vector)

    def wrap(self, vector1=None, vector=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, vector=vector, operation='WRAP').vector)

    def snap(self, vector1=None):
        return Vector(NodeVectorMath(vector0=self, vector1=vector1, operation='SNAP').vector)

    def sin(self):
        return Vector(NodeVectorMath(vector0=self, operation='SINE').vector)

    def cos(self):
        return Vector(NodeVectorMath(vector0=self, operation='COSINE').vector)

    def tan(self):
        return Vector(NodeVectorMath(vector0=self, operation='TANGENT').vector)

    def switch(self, switch=None, true=None):
        return Vector(NodeSwitch(false=self, switch=switch, true=true, input_type='VECTOR').output)

    def to_viewer(self, geometry=None):
        return NodeViewer(value=self, geometry=geometry, data_type='FLOAT_VECTOR')

    def rotate(self, center=None, axis=None, angle=None, invert=False, rotation_type='AXIS_ANGLE'):
        return Vector(NodeVectorRotate(vector=self, center=center, axis=axis, angle=angle, invert=invert, rotation_type=rotation_type).vector)

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        return Vector(NodeAlignEulertoVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None, mapping=None):
        return self.stack(NodeVectorCurves(vector=self, fac=fac, mapping=mapping))


# ==============================================================================================================
# Data class Color

class Color(bcls.Color):
    """ Socket data class Color

    Constructors
    ------------
        Combine              : (cls) ShaderNodeCombineRGB     

    Node properties
    ---------------
        separate             : node ShaderNodeSeparateRGB
        r                    : separate.r
        g                    : separate.g
        b                    : separate.b


    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = RGBA)
        to_viewer            : node GeometryNodeViewer(data_type = FLOAT_COLOR)

    Stacked methods
    ---------------
        curves               : node ShaderNodeRGBCurve

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None):
        return Color(NodeCombineRGB(r=r, g=g, b=b).image)


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    # ---------- Node SeparateRGB

    @property
    def separate(self):
        if not hasattr(self, 'separate_'):
            self.separate_ = NodeSeparateRGB(image=self)
        return self.separate_

    @property
    def r(self):
        if not hasattr(self, 'r_'):
            self.r_ = self.separate.r
        return self.r_

    @property
    def g(self):
        if not hasattr(self, 'g_'):
            self.g_ = self.separate.g
        return self.g_

    @property
    def b(self):
        if not hasattr(self, 'b_'):
            self.b_ = self.separate.b
        return self.b_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Color(NodeSwitch(false=self, switch=switch, true=true, input_type='RGBA').output)

    def to_viewer(self, geometry=None):
        return NodeViewer(value=self, geometry=geometry, data_type='FLOAT_COLOR')


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None, mapping=None):
        return self.stack(NodeRGBCurves(color=self, fac=fac, mapping=mapping))


# ==============================================================================================================
# Data class String

class String(bcls.String):
    """ Socket data class String

    Properties
    ----------
        length               : (Integer) FunctionNodeStringLength 

    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = STRING)
        to_curves            : (Curve) GeometryNodeStringToCurves

    Stacked methods
    ---------------
        replace              : node FunctionNodeReplaceString
        slice                : node FunctionNodeSliceString

    """


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def length(self):
        return Integer(NodeStringLength(string=self).length)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return String(NodeSwitch(false=self, switch=switch, true=true, input_type='STRING').output)

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        node = NodeStringtoCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, align_x=align_x, align_y=align_y, font=font, overflow=overflow, pivot_mode=pivot_mode)
        return Sockets(curve_instances=Geometry(node.curve_instances), line=Integer(node.line), pivot_point=Vector(node.pivot_point))


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def replace(self, find=None, replace=None):
        return self.stack(NodeReplaceString(string=self, find=find, replace=replace))

    def slice(self, position=None, length=None):
        return self.stack(NodeSliceString(string=self, position=position, length=length))


# ==============================================================================================================
# Data class Geometry

class Geometry(bcls.Geometry):
    """ Socket data class Geometry

    Node properties
    ---------------
        bound_box            : node GeometryNodeBoundBox
        box                  : bound_box.bounding_box
        box_min              : bound_box.min
        box_max              : bound_box.max

        components           : node GeometryNodeSeparateComponents
        mesh_component       : components.mesh
        points_component     : components.point_cloud
        curve_component      : components.curve
        volume_component     : components.volume
        instances_component  : components.instances


    Attributes
    ----------
        ID                   : GeometryNodeInputID      
        capture_ID           : Integer on domain POINT
        ID                   : Integer on domain POINT

        index                : GeometryNodeInputIndex   
        capture_index        : Integer on domain POINT
        index                : Integer on domain POINT

        is_viewport          : GeometryNodeIsViewport   
        capture_is_viewport  : Boolean on domain POINT
        is_viewport          : Boolean on domain POINT

        normal               : GeometryNodeInputNormal  
        capture_normal       : Vector on domain POINT
        point_normal         : Vector on domain POINT
        edge_normal          : Vector on domain EDGE
        face_normal          : Vector on domain FACE
        corner_normal        : Vector on domain CORNER
        curve_normal         : Vector on domain CURVE
        instance_normal      : Vector on domain INSTANCE

        position             : GeometryNodeInputPosition
        capture_position     : Vector on domain POINT
        position             : Vector on domain POINT

        tangent              : GeometryNodeInputTangent 
        capture_tangent      : Vector on domain POINT
        point_tangent        : Vector on domain POINT
        edge_tangent         : Vector on domain EDGE
        face_tangent         : Vector on domain FACE
        corner_tangent       : Vector on domain CORNER
        curve_tangent        : Vector on domain CURVE
        instance_tangent     : Vector on domain INSTANCE


    Methods
    -------
        attribute_domain_size : (Integer) GeometryNodeAttributeDomainSize
        attribute_remove     : GeometryNodeAttributeRemove
        attribute_statistic  : (Float) GeometryNodeAttributeStatistic
        capture_attribute    : GeometryNodeCaptureAttribute
        components           : GeometryNodeSeparateGeometry
        convex_hull          : (Mesh) GeometryNodeConvexHull   
        join                 : (Geometry) GeometryNodeJoinGeometry 
        switch               : GeometryNodeSwitch       (input_type = GEOMETRY)
        to_instance          : (Instances) GeometryNodeGeometryToInstance

    Stacked methods
    ---------------
        delete_geometry      : node GeometryNodeDeleteGeometry
        merge_by_distance    : node GeometryNodeMergeByDistance
        realize_instances    : node GeometryNodeRealizeInstances
        replace_material     : node GeometryNodeReplaceMaterial
        scale_elements       : node GeometryNodeScaleElements
        set_ID               : node GeometryNodeSetID
        set_material         : node GeometryNodeSetMaterial
        set_material_index   : node GeometryNodeSetMaterialIndex
        set_position         : node GeometryNodeSetPosition
        set_shade_smooth     : node GeometryNodeSetShadeSmooth
        transform            : node GeometryNodeTransform

    """


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    # ---------- Node BoundingBox

    @property
    def bound_box(self):
        if not hasattr(self, 'bound_box_'):
            self.bound_box_ = NodeBoundingBox(geometry=self)
        return self.bound_box_

    @property
    def box(self):
        if not hasattr(self, 'box_'):
            self.box_ = self.bound_box.bounding_box
        return self.box_

    @property
    def box_min(self):
        if not hasattr(self, 'box_min_'):
            self.box_min_ = self.bound_box.min
        return self.box_min_

    @property
    def box_max(self):
        if not hasattr(self, 'box_max_'):
            self.box_max_ = self.bound_box.max
        return self.box_max_

    # ---------- Node SeparateComponents

    @property
    def components(self):
        if not hasattr(self, 'components_'):
            self.components_ = NodeSeparateComponents(geometry=self)
        return self.components_

    @property
    def mesh_component(self):
        if not hasattr(self, 'mesh_component_'):
            self.mesh_component_ = self.components.mesh
        return self.mesh_component_

    @property
    def points_component(self):
        if not hasattr(self, 'points_component_'):
            self.points_component_ = self.components.point_cloud
        return self.points_component_

    @property
    def curve_component(self):
        if not hasattr(self, 'curve_component_'):
            self.curve_component_ = self.components.curve
        return self.curve_component_

    @property
    def volume_component(self):
        if not hasattr(self, 'volume_component_'):
            self.volume_component_ = self.components.volume
        return self.volume_component_

    @property
    def instances_component(self):
        if not hasattr(self, 'instances_component_'):
            self.instances_component_ = self.components.instances
        return self.instances_component_


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputNormal

    def capture_normal(self, domain='POINT'):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    @property
    def point_normal(self):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='POINT').outputs[0])

    @property
    def edge_normal(self):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[0])

    @property
    def face_normal(self):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='FACE').outputs[0])

    @property
    def corner_normal(self):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_normal(self):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_normal(self):
        return Vector(NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='INSTANCE').outputs[0])

    # ---------- Attribute GeometryNodeInputTangent

    def capture_tangent(self, domain='POINT'):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    @property
    def point_tangent(self):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='POINT').outputs[0])

    @property
    def edge_tangent(self):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[0])

    @property
    def face_tangent(self):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='FACE').outputs[0])

    @property
    def corner_tangent(self):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_tangent(self):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_tangent(self):
        return Vector(NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='INSTANCE').outputs[0])

    # ---------- Attribute GeometryNodeInputID

    def capture_ID(self, domain='POINT'):
        return Integer(NodeID(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def ID(self):
        return Integer(NodeID(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    # ---------- Attribute GeometryNodeInputIndex

    def capture_index(self, domain='POINT'):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def index(self):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    # ---------- Attribute GeometryNodeInputPosition

    def capture_position(self, domain='POINT'):
        return Vector(NodePosition(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    @property
    def position(self):
        return Vector(NodePosition(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='POINT').outputs[0])

    # ---------- Attribute GeometryNodeIsViewport

    def capture_is_viewport(self, domain='POINT'):
        return Boolean(NodeIsViewport(owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    @property
    def is_viewport(self):
        return Boolean(NodeIsViewport(owner_socket=self.socket, data_type='BOOLEAN', domain='POINT').outputs[0])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Geometry(NodeSwitch(false=self, switch=switch, true=true, input_type='GEOMETRY').output)

    def attribute_domain_size(self, component='MESH'):
        node = NodeDomainSize(geometry=self, component=component)
        return Sockets(point_count=Integer(node.point_count), edge_count=Integer(node.edge_count), face_count=Integer(node.face_count), face_corner_count=Integer(node.face_corner_count))

    def attribute_remove(*attribute, self):
        return Geometry(NodeAttributeRemove(*attribute, geometry=self).geometry)

    def attribute_statistic(self, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
        node = NodeAttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type, domain=domain)
        return Sockets(mean=Float(node.mean), median=Float(node.median), sum=Float(node.sum), min=Float(node.min), max=Float(node.max), range=Float(node.range), standard_deviation=Float(node.standard_deviation), variance=Float(node.variance))

    def components(self, selection=None, domain='POINT'):
        node = NodeSeparateGeometry(geometry=self, selection=selection, domain=domain)
        return Sockets(selection=Geometry(node.selection), inverted=Geometry(node.inverted))

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT'):
        node = NodeCaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain)
        return Sockets(geometry=Geometry(node.geometry), attribute=Float(node.attribute))

    def convex_hull(self):
        return Geometry(NodeConvexHull(geometry=self).convex_hull)

    def to_instance(self, *geometry):
        return Geometry(NodeGeometrytoInstance(self, *geometry).instances)

    def join(self, *geometry):
        return Geometry(NodeJoinGeometry(self, *geometry).geometry)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        return self.stack(NodeDeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))

    def merge_by_distance(self, selection=None, distance=None):
        return self.stack(NodeMergebyDistance(geometry=self, selection=selection, distance=distance))

    def realize_instances(self, legacy_behavior=False):
        return self.stack(NodeRealizeInstances(geometry=self, legacy_behavior=legacy_behavior))

    def replace_material(self, old=None, new=None):
        return self.stack(NodeReplaceMaterial(geometry=self, old=old, new=new))

    def scale_elements(self, selection=None, scale=None, center=None, domain='FACE', scale_mode='UNIFORM'):
        return self.stack(NodeScaleElements(geometry=self, selection=selection, scale=scale, center=center, domain=domain, scale_mode=scale_mode))

    def set_ID(self, selection=None, ID=None):
        return self.stack(NodeSetID(geometry=self, selection=selection, ID=ID))

    def set_material(self, selection=None, material=None):
        return self.stack(NodeSetMaterial(geometry=self, selection=selection, material=material))

    def set_material_index(self, selection=None, material_index=None):
        return self.stack(NodeSetMaterialIndex(geometry=self, selection=selection, material_index=material_index))

    def set_position(self, selection=None, position=None, offset=None):
        return self.stack(NodeSetPosition(geometry=self, selection=selection, position=position, offset=offset))

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        return self.stack(NodeSetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))

    def transform(self, translation=None, rotation=None, scale=None):
        return self.stack(NodeTransform(geometry=self, translation=translation, rotation=rotation, scale=scale))


# ==============================================================================================================
# Data class Spline

class Spline(Geometry):
    """ Socket data class Spline

    Attributes
    ----------
        cyclic               : GeometryNodeInputSplineCyclic
        capture_cyclic       : Boolean on domain CURVE
        cyclic               : Boolean on domain CURVE

        length               : GeometryNodeSplineLength 
        capture_length       : Float on domain CURVE
        length               : Float on domain CURVE
        capture_point_count  : Integer on domain CURVE
        point_count          : Integer on domain CURVE

        parameter            : GeometryNodeSplineParameter
        capture_parameter_factor : Float on domain CURVE
        parameter_factor     : Float on domain CURVE
        capture_parameter_length : Float on domain CURVE
        parameter_length     : Float on domain CURVE
        capture_parameter_index : Integer on domain CURVE
        parameter_index      : Integer on domain CURVE

        resolution           : GeometryNodeInputSplineResolution
        capture_resolution   : Integer on domain CURVE
        resolution           : Integer on domain CURVE


    Stacked methods
    ---------------
        set_cyclic           : node GeometryNodeSetSplineCyclic
        set_resolution       : node GeometryNodeSetSplineResolution

    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputSplineCyclic

    def capture_cyclic(self, domain='CURVE'):
        return Boolean(NodeIsSplineCyclic(owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    @property
    def cyclic(self):
        return Boolean(NodeIsSplineCyclic(owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputSplineResolution

    def capture_resolution(self, domain='CURVE'):
        return Integer(NodeSplineResolution(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def resolution(self):
        return Integer(NodeSplineResolution(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeSplineLength

    def capture_length(self, domain='CURVE'):
        return Float(NodeSplineLength(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def length(self):
        return Float(NodeSplineLength(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    def capture_point_count(self, domain='CURVE'):
        return Integer(NodeSplineLength(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def point_count(self):
        return Integer(NodeSplineLength(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[1])

    # ---------- Attribute GeometryNodeSplineParameter

    def capture_parameter_factor(self, domain='CURVE'):
        return Float(NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def parameter_factor(self):
        return Float(NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    def capture_parameter_length(self, domain='CURVE'):
        return Float(NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[1])

    @property
    def parameter_length(self):
        return Float(NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[1])

    def capture_parameter_index(self, domain='CURVE'):
        return Integer(NodeSplineParameter(owner_socket=self.socket, data_type='INT', domain=domain).outputs[2])

    @property
    def parameter_index(self):
        return Integer(NodeSplineParameter(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[2])


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_cyclic(self, selection=None, cyclic=None):
        return self.stack(NodeSetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic))

    def set_resolution(self, selection=None, resolution=None):
        return self.stack(NodeSetSplineResolution(geometry=self, selection=selection, resolution=resolution))


# ==============================================================================================================
# Data class Curve

class Curve(Spline):
    """ Socket data class Curve

    Constructors
    ------------
        BezierSegment        : (cls) GeometryNodeCurvePrimitiveBezierSegment
        Circle               : (cls) GeometryNodeCurvePrimitiveCircle
        Line                 : (cls) GeometryNodeCurvePrimitiveLine
        QuadraticBezier      : (cls) GeometryNodeCurveQuadraticBezier
        Quadrilateral        : (cls) GeometryNodeCurvePrimitiveQuadrilateral
        Spiral               : (cls) GeometryNodeCurveSpiral  
        Star                 : (cls) GeometryNodeCurveStar    

    Attributes
    ----------
        ID                   : GeometryNodeInputID      
        spline_ID            : Integer on domain SPLINE

        endpoint_selection   : GeometryNodeCurveEndpointSelection
        capture_endpoint_selection : Boolean on domain CURVE
        endpoint_selection   : Boolean on domain CURVE

        handle_positions     : GeometryNodeInputCurveHandlePositions
        capture_handle_positions_left : Vector on domain CURVE
        handle_positions_left : Vector on domain CURVE
        capture_handle_positions_right : Vector on domain CURVE
        handle_positions_right : Vector on domain CURVE

        handle_type_selection : GeometryNodeCurveHandleTypeSelection
        capture_handle_type_selection : Boolean on domain CURVE
        handle_type_selection : Boolean on domain CURVE

        index                : GeometryNodeInputIndex   
        spline_index         : Integer on domain SPLINE

        radius               : GeometryNodeInputRadius  
        capture_radius       : Float on domain CURVE
        radius               : Float on domain CURVE

        tilt                 : GeometryNodeInputCurveTilt
        capture_tilt         : Float on domain CURVE
        tilt                 : Float on domain CURVE


    Methods
    -------
        length               : (Float) GeometryNodeCurveLength  
        sample               : node GeometryNodeSampleCurve
        to_mesh              : (Mesh) GeometryNodeCurveToMesh  
        to_points            : (Points) GeometryNodeCurveToPoints

    Stacked methods
    ---------------
        fill                 : node GeometryNodeFillCurve
        fillet               : node GeometryNodeFilletCurve
        resample             : node GeometryNodeResampleCurve
        reverse              : node GeometryNodeReverseCurve
        set_handle_positions : node GeometryNodeSetCurveHandlePositions
        set_handles          : node GeometryNodeCurveSetHandles
        set_radius           : node GeometryNodeSetCurveRadius
        set_spline_type      : node GeometryNodeCurveSplineType
        set_tilt             : node GeometryNodeSetCurveTilt
        subdivide            : node GeometryNodeSubdivideCurve
        trim                 : node GeometryNodeTrimCurve

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        return Geometry(NodeBezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)

    @classmethod
    def Circle(cls, resolution=None, radius=None, mode='RADIUS'):
        return Geometry(NodeCurveCircle(resolution=resolution, radius=radius, mode=mode).curve)

    @classmethod
    def Line(cls, start=None, end=None, mode='POINTS'):
        return Geometry(NodeCurveLine(start=start, end=end, mode=mode).curve)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, mode='RECTANGLE'):
        return Geometry(NodeQuadrilateral(width=width, height=height, mode=mode).curve)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        return Geometry(NodeQuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        node = NodeStar(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)
        return Sockets(curve=Geometry(node.curve), outer_points=Boolean(node.outer_points))

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        return Geometry(NodeSpiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputID

    @property
    def spline_ID(self):
        return Integer(NodeID(owner_socket=self.socket, data_type='INT', domain='SPLINE').outputs[0])

    # ---------- Attribute GeometryNodeInputIndex

    @property
    def spline_index(self):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain='SPLINE').outputs[0])

    # ---------- Attribute GeometryNodeCurveEndpointSelection

    def capture_endpoint_selection(self, start_size=None, end_size=None, domain='CURVE'):
        return Boolean(NodeEndpointSelection(start_size=start_size, end_size=end_size, owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    def endpoint_selection(self, start_size=None, end_size=None):
        return Boolean(NodeEndpointSelection(start_size=start_size, end_size=end_size, owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeCurveHandleTypeSelection

    def capture_handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, domain='CURVE'):
        return Boolean(NodeHandleTypeSelection(handle_type=handle_type, mode=mode, owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        return Boolean(NodeHandleTypeSelection(handle_type=handle_type, mode=mode, owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputCurveTilt

    def capture_tilt(self, domain='CURVE'):
        return Float(NodeCurveTilt(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def tilt(self):
        return Float(NodeCurveTilt(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputRadius

    def capture_radius(self, domain='CURVE'):
        return Float(NodeRadius(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def radius(self):
        return Float(NodeRadius(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputCurveHandlePositions

    def capture_handle_positions_left(self, relative=None, domain='CURVE'):
        return Vector(NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    def handle_positions_left(self, relative=None):
        return Vector(NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[0])

    def capture_handle_positions_right(self, relative=None, domain='CURVE'):
        return Vector(NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[1])

    def handle_positions_right(self, relative=None):
        return Vector(NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[1])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, profile_curve=None, fill_caps=None):
        return Geometry(NodeCurvetoMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).mesh)

    def to_points(self, count=None, mode='COUNT'):
        node = NodeCurvetoPoints(curve=self, count=count, mode=mode)
        return Sockets(points=Geometry(node.points), tangent=Vector(node.tangent), normal=Vector(node.normal), rotation=Vector(node.rotation))

    def sample(self, length=None, mode='LENGTH'):
        node = NodeSampleCurve(curve=self, length=length, mode=mode)
        return Sockets(position=Vector(node.position), tangent=Vector(node.tangent), normal=Vector(node.normal))

    def length(self):
        return Float(NodeCurveLength(curve=self).length)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_handles(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        return self.stack(NodeSetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode))

    def set_spline_type(self, selection=None, spline_type='POLY'):
        return self.stack(NodeSetSplineType(curve=self, selection=selection, spline_type=spline_type))

    def fill(self, mode='TRIANGLES'):
        return self.stack(NodeFillCurve(curve=self, mode=mode))

    def fillet(self, radius=None, limit_radius=None, mode='BEZIER'):
        return self.stack(NodeFilletCurve(curve=self, radius=radius, limit_radius=limit_radius, mode=mode))

    def resample(self, selection=None, count=None, mode='COUNT'):
        return self.stack(NodeResampleCurve(curve=self, selection=selection, count=count, mode=mode))

    def reverse(self, selection=None):
        return self.stack(NodeReverseCurve(curve=self, selection=selection))

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT'):
        return self.stack(NodeSetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode))

    def set_radius(self, selection=None, radius=None):
        return self.stack(NodeSetCurveRadius(curve=self, selection=selection, radius=radius))

    def set_tilt(self, selection=None, tilt=None):
        return self.stack(NodeSetCurveTilt(curve=self, selection=selection, tilt=tilt))

    def subdivide(self, cuts=None):
        return self.stack(NodeSubdivideCurve(curve=self, cuts=cuts))

    def trim(self, start=None, end=None, mode='FACTOR'):
        return self.stack(NodeTrimCurve(curve=self, start=start, end=end, mode=mode))


# ==============================================================================================================
# Data class Mesh

class Mesh(Geometry):
    """ Socket data class Mesh

    Constructors
    ------------
        Circle               : (cls) GeometryNodeMeshCircle   
        Cone                 : (cls) GeometryNodeMeshCone     
        Cube                 : (cls) GeometryNodeMeshCube     
        Cylinder             : (cls) GeometryNodeMeshCylinder 
        Grid                 : (cls) GeometryNodeMeshGrid     
        IcoSphere            : (cls) GeometryNodeMeshIcoSphere
        Line                 : (cls) GeometryNodeMeshLine     
        UVSphere             : (cls) GeometryNodeMeshUVSphere 

    Attributes
    ----------
        ID                   : GeometryNodeInputID      
        face_ID              : Integer on domain FACE
        corner_ID            : Integer on domain CORNER
        edge_ID              : Integer on domain EDGE

        edge_angle           : GeometryNodeInputMeshEdgeAngle
        capture_edge_angle_unsigned_angle : Float on domain EDGE
        edge_angle_unsigned_angle : Float on domain EDGE
        capture_edge_angle_signed_angle : Float on domain EDGE
        edge_angle_signed_angle : Float on domain EDGE

        edge_neighbors       : GeometryNodeInputMeshEdgeNeighbors
        capture_edge_neighbors : Integer on domain EDGE
        edge_neighbors       : Integer on domain EDGE

        edge_vertices        : GeometryNodeInputMeshEdgeVertices
        capture_edge_vertices_vertex_index_1 : Integer on domain EDGE
        edge_vertices_vertex_index_1 : Integer on domain EDGE
        capture_edge_vertices_vertex_index_2 : Integer on domain EDGE
        edge_vertices_vertex_index_2 : Integer on domain EDGE
        capture_edge_vertices_position_1 : Vector on domain EDGE
        edge_vertices_position_1 : Vector on domain EDGE
        capture_edge_vertices_position_2 : Vector on domain EDGE
        edge_vertices_position_2 : Vector on domain EDGE

        face_area            : GeometryNodeInputMeshFaceArea
        capture_face_area    : Float on domain FACE
        face_area            : Float on domain FACE

        face_neighbors       : GeometryNodeInputMeshFaceNeighbors
        capture_face_neighbors_vertex_count : Integer on domain FACE
        face_neighbors_vertex_count : Integer on domain FACE
        capture_face_neighbors_face_count : Integer on domain FACE
        face_neighbors_face_count : Integer on domain FACE

        index                : GeometryNodeInputIndex   
        face_index           : Integer on domain FACE
        corner_index         : Integer on domain CORNER
        edge_index           : Integer on domain EDGE

        island               : GeometryNodeInputMeshIsland
        capture_island_island_index : Integer on domain FACE
        island_island_index  : Integer on domain FACE
        capture_island_island_count : Integer on domain FACE
        island_island_count  : Integer on domain FACE

        material_index       : GeometryNodeInputMaterialIndex
        capture_material_index : Integer on domain FACE
        material_index       : Integer on domain FACE

        shade_smooth         : GeometryNodeInputShadeSmooth
        capture_shade_smooth : Boolean on domain FACE
        shade_smooth         : Boolean on domain FACE

        vertex_neighbors     : GeometryNodeInputMeshVertexNeighbors
        capture_vertex_neighbors_vertex_count : Integer on domain POINT
        vertex_neighbors_vertex_count : Integer on domain POINT
        capture_vertex_neighbors_face_count : Integer on domain POINT
        vertex_neighbors_face_count : Integer on domain POINT


    Methods
    -------
        difference           : GeometryNodeMeshBoolean  (operation = DIFFERENCE)
        distribute_points_on_faces : (Points) GeometryNodeDistributePointsOnFaces
        intersect            : GeometryNodeMeshBoolean  (operation = INTERSECT)
        to_curve             : (Curve) GeometryNodeMeshToCurve  
        to_curve             : (Points) GeometryNodeMeshToPoints 
        union                : GeometryNodeMeshBoolean  (operation = UNION)

    Stacked methods
    ---------------
        dual                 : node GeometryNodeDualMesh
        extrude              : node GeometryNodeExtrudeMesh
        flip_faces           : node GeometryNodeFlipFaces
        split_edges          : node GeometryNodeSplitEdges
        subdivide            : node GeometryNodeSubdivideMesh
        subdivision_surface  : node GeometryNodeSubdivisionSurface
        triangulate          : node GeometryNodeTriangulate

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        return Geometry(NodeMeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        node = NodeCone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)
        return Sockets(mesh=Geometry(node.mesh), top=Boolean(node.top), bottom=Boolean(node.bottom), side=Boolean(node.side))

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        return Geometry(NodeCube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).mesh)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        node = NodeCylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)
        return Sockets(mesh=Geometry(node.mesh), top=Boolean(node.top), side=Boolean(node.side), bottom=Boolean(node.bottom))

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        return Geometry(NodeGrid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).mesh)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        return Geometry(NodeIcoSphere(radius=radius, subdivisions=subdivisions).mesh)

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        return Geometry(NodeMeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        return Geometry(NodeUVSphere(segments=segments, rings=rings, radius=radius).mesh)


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputID

    @property
    def face_ID(self):
        return Integer(NodeID(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def corner_ID(self):
        return Integer(NodeID(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def edge_ID(self):
        return Integer(NodeID(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    # ---------- Attribute GeometryNodeInputIndex

    @property
    def face_index(self):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def corner_index(self):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def edge_index(self):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    # ---------- Attribute GeometryNodeInputMeshEdgeNeighbors

    def capture_edge_neighbors(self, domain='EDGE'):
        return Integer(NodeEdgeNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def edge_neighbors(self):
        return Integer(NodeEdgeNeighbors(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    # ---------- Attribute GeometryNodeInputMeshFaceArea

    def capture_face_area(self, domain='FACE'):
        return Float(NodeFaceArea(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def face_area(self):
        return Float(NodeFaceArea(owner_socket=self.socket, data_type='VALUE', domain='FACE').outputs[0])

    # ---------- Attribute GeometryNodeInputMeshEdgeAngle

    def capture_edge_angle_unsigned_angle(self, domain='EDGE'):
        return Float(NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def edge_angle_unsigned_angle(self):
        return Float(NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain='EDGE').outputs[0])

    def capture_edge_angle_signed_angle(self, domain='EDGE'):
        return Float(NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[1])

    @property
    def edge_angle_signed_angle(self):
        return Float(NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain='EDGE').outputs[1])

    # ---------- Attribute GeometryNodeInputMeshEdgeVertices

    def capture_edge_vertices_vertex_index_1(self, domain='EDGE'):
        return Integer(NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def edge_vertices_vertex_index_1(self):
        return Integer(NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    def capture_edge_vertices_vertex_index_2(self, domain='EDGE'):
        return Integer(NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def edge_vertices_vertex_index_2(self):
        return Integer(NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[1])

    def capture_edge_vertices_position_1(self, domain='EDGE'):
        return Vector(NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[2])

    @property
    def edge_vertices_position_1(self):
        return Vector(NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[2])

    def capture_edge_vertices_position_2(self, domain='EDGE'):
        return Vector(NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[3])

    @property
    def edge_vertices_position_2(self):
        return Vector(NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[3])

    # ---------- Attribute GeometryNodeInputMeshFaceNeighbors

    def capture_face_neighbors_vertex_count(self, domain='FACE'):
        return Integer(NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def face_neighbors_vertex_count(self):
        return Integer(NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    def capture_face_neighbors_face_count(self, domain='FACE'):
        return Integer(NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def face_neighbors_face_count(self):
        return Integer(NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[1])

    # ---------- Attribute GeometryNodeInputMeshIsland

    def capture_island_island_index(self, domain='FACE'):
        return Integer(NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def island_island_index(self):
        return Integer(NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    def capture_island_island_count(self, domain='FACE'):
        return Integer(NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def island_island_count(self):
        return Integer(NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[1])

    # ---------- Attribute GeometryNodeInputMeshVertexNeighbors

    def capture_vertex_neighbors_vertex_count(self, domain='POINT'):
        return Integer(NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def vertex_neighbors_vertex_count(self):
        return Integer(NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    def capture_vertex_neighbors_face_count(self, domain='POINT'):
        return Integer(NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def vertex_neighbors_face_count(self):
        return Integer(NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[1])

    # ---------- Attribute GeometryNodeInputMaterialIndex

    def capture_material_index(self, domain='FACE'):
        return Integer(NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def material_index(self):
        return Integer(NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    # ---------- Attribute GeometryNodeInputShadeSmooth

    def capture_shade_smooth(self, domain='FACE'):
        return Boolean(NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    @property
    def shade_smooth(self):
        return Boolean(NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='FACE').outputs[0])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        return Geometry(NodeMeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').mesh)

    def union(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        return Geometry(NodeMeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').mesh)

    def difference(*mesh_2, self, self_intersection=None, hole_tolerant=None):
        return Geometry(NodeMeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE').mesh)

    def to_curve(self, selection=None):
        return Geometry(NodeMeshtoCurve(mesh=self, selection=selection).curve)

    def to_curve(self, selection=None, position=None, radius=None, mode='VERTICES'):
        return Geometry(NodeMeshtoPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).points)

    def distribute_points_on_faces(self, selection=None, density=None, seed=None, distribute_method='RANDOM'):
        node = NodeDistributePointsonFaces(mesh=self, selection=selection, density=density, seed=seed, distribute_method=distribute_method)
        return Sockets(points=Geometry(node.points), normal=Vector(node.normal), rotation=Vector(node.rotation))


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def split_edges(self, selection=None):
        return self.stack(NodeSplitEdges(mesh=self, selection=selection))

    def subdivide(self, level=None):
        return self.stack(NodeSubdivideMesh(mesh=self, level=level))

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        return self.stack(NodeSubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        return self.stack(NodeTriangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))

    def dual(self, keep_boundaries=None):
        return self.stack(NodeDualMesh(mesh=self, keep_boundaries=keep_boundaries))

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        return self.stack(NodeExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode))

    def flip_faces(self, selection=None):
        return self.stack(NodeFlipFaces(mesh=self, selection=selection))


# ==============================================================================================================
# Data class Points

class Points(Mesh):
    """ Socket data class Points

    Methods
    -------
        instance_on_points   : (Instances) GeometryNodeInstanceOnPoints
        to_vertices          : (Mesh) GeometryNodePointsToVertices
        to_volume            : (Volume) GeometryNodePointsToVolume

    Stacked methods
    ---------------
        set_radius           : node GeometryNodeSetPointRadius

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        return Geometry(NodeInstanceonPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)

    def to_vertices(self, selection=None):
        return Geometry(NodePointstoVertices(points=self, selection=selection).mesh)

    def to_volume(self, density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        return Geometry(NodePointstoVolume(points=self, density=density, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_radius(self, selection=None, radius=None):
        return self.stack(NodeSetPointRadius(points=self, selection=selection, radius=radius))


# ==============================================================================================================
# Data class Instances

class Instances(Mesh):
    """ Socket data class Instances

    Attributes
    ----------
        index                : GeometryNodeInputIndex   
        capture_index        : Integer on domain INSTANCE
        index                : Integer on domain INSTANCE


    Methods
    -------
        to_points            : (Points) GeometryNodeInstancesToPoints

    Stacked methods
    ---------------
        rotate               : node GeometryNodeRotateInstances
        scale                : node GeometryNodeScaleInstances
        translate            : node GeometryNodeTranslateInstances

    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputIndex

    def capture_index(self, domain='INSTANCE'):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def index(self):
        return Integer(NodeIndex(owner_socket=self.socket, data_type='INT', domain='INSTANCE').outputs[0])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_points(self, selection=None, position=None, radius=None):
        return Geometry(NodeInstancestoPoints(instances=self, selection=selection, position=position, radius=radius).points)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        return self.stack(NodeRotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        return self.stack(NodeScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        return self.stack(NodeTranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))


# ==============================================================================================================
# Data class Volume

class Volume(Mesh):
    """ Socket data class Volume

    Methods
    -------
        to_mesh              : (Mesh) GeometryNodeVolumeToMesh 

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, threshold=None, adaptivity=None, resolution_mode='GRID'):
        return Geometry(NodeVolumetoMesh(volume=self, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh)


# ==============================================================================================================
# Data class Collection

class Collection(bcls.Collection):
    """ Socket data class Collection

    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = COLLECTION)

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Collection(NodeSwitch(false=self, switch=switch, true=true, input_type='COLLECTION').output)


# ==============================================================================================================
# Data class Object

class Object(bcls.Object):
    """ Socket data class Object

    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = OBJECT)

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Object(NodeSwitch(false=self, switch=switch, true=true, input_type='OBJECT').output)


# ==============================================================================================================
# Data class Texture

class Texture(bcls.Texture):
    """ Socket data class Texture

    Constructors
    ------------
        Brick                : (cls) ShaderNodeTexBrick       
        Checker              : (cls) ShaderNodeTexChecker     
        Gradient             : (cls) ShaderNodeTexGradient    
        Image                : (cls) GeometryNodeImageTexture 
        Magic                : (cls) ShaderNodeTexMagic       
        Musgrave             : (cls) ShaderNodeTexMusgrave    
        Noise                : (cls) ShaderNodeTexNoise       
        Voronoi              : (cls) ShaderNodeTexVoronoi     
        Wave                 : (cls) ShaderNodeTexWave        
        WhiteNoise           : (cls) ShaderNodeTexWhiteNoise  

    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = TEXTURE)

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Brick(cls, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        node = NodeBrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Checker(cls, vector=None, color1=None, color2=None, scale=None):
        node = NodeCheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Gradient(cls, vector=None, gradient_type='LINEAR'):
        node = NodeGradientTexture(vector=vector, gradient_type=gradient_type)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Magic(cls, vector=None, scale=None, distortion=None, turbulence_depth=2):
        node = NodeMagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Musgrave(cls, vector=None, scale=None, detail=None, dimension=None, lacunarity=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        return Float(NodeMusgraveTexture(vector=vector, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).fac)

    @classmethod
    def Noise(cls, vector=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        node = NodeNoiseTexture(vector=vector, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)
        return Sockets(fac=Float(node.fac), color=Color(node.color))

    @classmethod
    def Voronoi(cls, vector=None, scale=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        node = NodeVoronoiTexture(vector=vector, scale=scale, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return Sockets(distance=Float(node.distance), color=Color(node.color), position=Vector(node.position))

    @classmethod
    def Wave(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        node = NodeWaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def WhiteNoise(cls, vector=None, noise_dimensions='3D'):
        node = NodeWhiteNoiseTexture(vector=vector, noise_dimensions=noise_dimensions)
        return Sockets(value=Float(node.value), color=Color(node.color))

    @classmethod
    def Image(cls, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        node = NodeImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        return Sockets(color=Color(node.color), alpha=Float(node.alpha))


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Texture(NodeSwitch(false=self, switch=switch, true=true, input_type='TEXTURE').output)


# ==============================================================================================================
# Data class Material

class Material(bcls.Material):
    """ Socket data class Material

    Methods
    -------
        selection            : (Boolean) GeometryNodeMaterialSelection
        switch               : GeometryNodeSwitch       (input_type = MATERIAL)

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Material(NodeSwitch(false=self, switch=switch, true=true, input_type='MATERIAL').output)

    def selection(self):
        return Boolean(NodeMaterialSelection(material=self).selection)


# ==============================================================================================================
# Data class Image

class Image(bcls.Image):
    """ Socket data class Image

    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = IMAGE)

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        return Image(NodeSwitch(false=self, switch=switch, true=true, input_type='IMAGE').output)

