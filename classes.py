from geonodes import baseclasses as bcls
from geonodes import nodes

import logging
logger = logging.Logger('geonodes')

# ----------------------------------------------------------------------------------------------------
# Argument is a vector

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ----------------------------------------------------------------------------------------------------
# Sockets outputs

class Sockets(bcls.Sockets):
    pass


# ==============================================================================================================
# Global functions

def b_and(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='AND').boolean)

def b_or(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='OR').boolean)

def b_not(boolean0=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, operation='NOT').boolean)

def nand(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NAND').boolean)

def nor(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NOR').boolean)

def xnor(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XNOR').boolean)

def xor(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XOR').boolean)

def imply(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='IMPLY').boolean)

def nimply(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NIMPLY').boolean)

def add(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='ADD', use_clamp=use_clamp).value)

def substract(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='SUBTRACT', use_clamp=use_clamp).value)

def multiply(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='MULTIPLY', use_clamp=use_clamp).value)

def divide(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, operation='DIVIDE', use_clamp=use_clamp).value)

def multiply_add(value0=None, value1=None, value2=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD', use_clamp=use_clamp).value)

def pow(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='POWER', use_clamp=use_clamp).value)

def log(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, operation='LOGARITHM', use_clamp=use_clamp).value)

def sqrt(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='SQRT', use_clamp=use_clamp).value)

def inverse_sqrt(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='INVERSE_SQRT', use_clamp=use_clamp).value)

def abs(value0=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, operation='ABSOLUTE', use_clamp=use_clamp).value)

def exp(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='EXPONENT', use_clamp=use_clamp).value)

def min(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='MINIMUM', use_clamp=use_clamp).value)

def max(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='MAXIMUM', use_clamp=use_clamp).value)

def less_than(value0=None, value1=None, use_clamp=False):
    return Boolean(nodes.NodeMath(value0=value0, value1=value1, operation='LESS_THAN', use_clamp=use_clamp).value)

def greater_than(value0=None, value1=None, use_clamp=False):
    return Boolean(nodes.NodeMath(value0=value0, value1=value1, operation='GREATER_THAN', use_clamp=use_clamp).value)

def sign(value0=None, use_clamp=False):
    return Integer(nodes.NodeMath(value0=value0, operation='SIGN', use_clamp=use_clamp).value)

def compare(value0=None, value1=None, value2=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='COMPARE', use_clamp=use_clamp).value)

def smooth_min(value0=None, value1=None, value2=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN', use_clamp=use_clamp).value)

def smooth_max(value0=None, value1=None, value2=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX', use_clamp=use_clamp).value)

def round(value0=None, use_clamp=False):
    return Integer(nodes.NodeMath(value0=value0, operation='ROUND', use_clamp=use_clamp).value)

def floor(value0=None, use_clamp=False):
    return Integer(nodes.NodeMath(value0=value0, operation='FLOOR', use_clamp=use_clamp).value)

def ceil(value0=None, use_clamp=False):
    return Integer(nodes.NodeMath(value0=value0, operation='CEIL', use_clamp=use_clamp).value)

def trunc(value0=None, use_clamp=False):
    return Integer(nodes.NodeMath(value0=value0, operation='TRUNC', use_clamp=use_clamp).value)

def fract(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='FRACT', use_clamp=use_clamp).value)

def modulo(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='MODULO', use_clamp=use_clamp).value)

def wrap(value0=None, value1=None, value2=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='WRAP', use_clamp=use_clamp).value)

def snap(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, operation='SNAP', use_clamp=use_clamp).value)

def pingpong(value0=None, value1=None, use_clamp=False):
    return GLOBAL(nodes.NodeMath(value0=value0, value1=value1, operation='PINGPONG', use_clamp=use_clamp).value)

def sin(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='SINE', use_clamp=use_clamp).value)

def cos(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='COSINE', use_clamp=use_clamp).value)

def tan(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='TANGENT', use_clamp=use_clamp).value)

def arcsin(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='ARCSINE', use_clamp=use_clamp).value)

def arccos(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='ARCCOSINE', use_clamp=use_clamp).value)

def arctan(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='ARCTANGENT', use_clamp=use_clamp).value)

def arctan2(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, operation='ARCTAN2', use_clamp=use_clamp).value)

def sinh(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='SINH', use_clamp=use_clamp).value)

def cosh(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='COSH', use_clamp=use_clamp).value)

def tanh(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='TANH', use_clamp=use_clamp).value)

def radians(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='RADIANS', use_clamp=use_clamp).value)

def degrees(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, operation='DEGREES', use_clamp=use_clamp).value)

def vector_add(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='ADD').vector)

def vector_subtract(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT').vector)

def vector_multiply(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY').vector)

def vector_divide(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE').vector)

def vector_multiply_add(vector0=None, vector1=None, vector2=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector)

def cross(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT').vector)

def project(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='PROJECT').vector)

def reflect(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='REFLECT').vector)

def refract(vector0=None, vector1=None, scale=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT').vector)

def faceforward(vector0=None, vector1=None, vector2=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector)

def dot(vector0=None, vector1=None):
    return Float(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT').value)

def distance(vector0=None, vector1=None):
    return Float(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE').value)

def length(vector0=None):
    return Float(nodes.NodeVectorMath(vector0=vector0, operation='LENGTH').value)

def scale(vector0=None, scale=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, scale=scale, operation='SCALE').vector)

def normalize(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='NORMALIZE').vector)

def absolute(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='ABSOLUTE').vector)

def vector_min(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM').vector)

def vector_max(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM').vector)

def vector_floor(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='FLOOR').vector)

def vector_ceil(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='CEIL').vector)

def vector_fraction(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='FRACTION').vector)

def vector_modulo(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MODULO').vector)

def wrap(vector0=None, vector1=None, vector2=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP').vector)

def snap(vector0=None, vector1=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='SNAP').vector)

def vector_sin(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='SINE').vector)

def vector_cos(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='COSINE').vector)

def vector_tan(vector0=None):
    return Vector(nodes.NodeVectorMath(vector0=vector0, operation='TANGENT').vector)

def compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='EQUAL'):
    return Boolean(nodes.NodeCompare(a=a, b=b, c=c, angle=angle, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).result)

def join_strings(*strings, delimiter=None):
    return String(nodes.NodeJoinStrings(*strings, delimiter=delimiter).string)

def accumulate_field(value=None, group_index=None, data_type='FLOAT', domain='POINT'):
    node = nodes.NodeAccumulateField(value=value, group_index=group_index, data_type=data_type, domain=domain)
    return Sockets(leading=Float(node.leading), trailing=Float(node.trailing), total=Float(node.total))

def field_at_index(index=None, value=None, data_type='FLOAT', domain='POINT'):
    return Float(nodes.NodeFieldatIndex(index=index, value=value, data_type=data_type, domain=domain).value)

def collection_info(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
    return Geometry(nodes.NodeCollectionInfo(collection=Collection.blender_collection(collection), separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry)

def object_info(object=None, as_instance=None, transform_space='ORIGINAL'):
    node = nodes.NodeObjectInfo(object=Object.blender_object(object), as_instance=as_instance, transform_space=transform_space)
    return Sockets(location=Vector(node.location), rotation=Vector(node.rotation), scale=Vector(node.scale), geometry=Geometry(node.geometry))

def scene():
    node = nodes.NodeSceneTime()
    return Sockets(seconds=Float(node.seconds), frame=Float(node.frame))


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
        field_at_index       : (Boolean) GeometryNodeFieldAtIndex (data_type = BOOLEAN)
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
        """ Method Random

        Arguments
        ---------
            probability     : Float
            ID              : Integer
            seed            : Integer
            data_type       : node parameter set to 'BOOLEAN'
        """

        return Boolean(nodes.NodeRandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def b_and(self, boolean1=None):
        """ Method b_and

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'AND'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean)

    def b_or(self, boolean1=None):
        """ Method b_or

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'OR'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean)

    def b_not(self):
        """ Method b_not

        Arguments
        ---------
            boolean0        : Boolean
            operation       : node parameter set to 'NOT'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, operation='NOT').boolean)

    def nand(self, boolean1=None):
        """ Method nand

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'NAND'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean)

    def nor(self, boolean1=None):
        """ Method nor

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'NOR'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean)

    def xnor(self, boolean1=None):
        """ Method xnor

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'XNOR'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean)

    def xor(self, boolean1=None):
        """ Method xor

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'XOR'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean)

    def imply(self, boolean1=None):
        """ Method imply

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'IMPLY'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean)

    def nimply(self, boolean1=None):
        """ Method nimply

        Arguments
        ---------
            boolean0        : Boolean
            boolean1        : Boolean
            operation       : node parameter set to 'NIMPLY'
        """

        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean)

    def switch(self, false=None, true=None):
        """ Method switch

        Arguments
        ---------
            switch          : Boolean
            false           : Float
            true            : Float
            input_type      : node parameter set to 'BOOLEAN'
        """

        return Boolean(nodes.NodeSwitch(switch=self, false=false, true=true, input_type='BOOLEAN').output)

    def to_viewer(self, geometry=None):
        """ Method to_viewer

        Arguments
        ---------
            value           : Float
            geometry        : Geometry
            data_type       : node parameter set to 'BOOLEAN'
        """

        return nodes.NodeViewer(value=self, geometry=geometry, data_type='BOOLEAN')

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index

        Arguments
        ---------
            value           : Float
            index           : Integer
            data_type       : node parameter set to 'BOOLEAN'
            domain          : node parameter
        """

        return Boolean(nodes.NodeFieldatIndex(value=self, index=index, data_type='BOOLEAN', domain=domain).value)


# ==============================================================================================================
# Data class Integer

class Integer(bcls.Integer):
    """ Socket data class Integer

    Constructors
    ------------
        Random               : FunctionNodeRandomValue  (data_type = INT)

    Methods
    -------
        abs                  : (Integer) ShaderNodeMath           (operation = ABSOLUTE)
        accumulate_field     : GeometryNodeAccumulateField(data_type = INT)
        add                  : (Integer) ShaderNodeMath           (operation = ADD)
        arccos               : (Float) ShaderNodeMath           (operation = ARCCOSINE)
        arcsin               : (Float) ShaderNodeMath           (operation = ARCSINE)
        arctan               : (Float) ShaderNodeMath           (operation = ARCTANGENT)
        arctan2              : (Float) ShaderNodeMath           (operation = ARCTAN2)
        ceil                 : (Integer) ShaderNodeMath           (operation = CEIL)
        compare              : ShaderNodeMath           (operation = COMPARE)
        compare              : FunctionNodeCompare      (data_type = INT)
        cos                  : (Float) ShaderNodeMath           (operation = COSINE)
        cosh                 : (Float) ShaderNodeMath           (operation = COSH)
        degrees              : (Float) ShaderNodeMath           (operation = DEGREES)
        divide               : (Float) ShaderNodeMath           (operation = DIVIDE)
        exp                  : (Float) ShaderNodeMath           (operation = EXPONENT)
        field_at_index       : (Integer) GeometryNodeFieldAtIndex (data_type = INT)
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
        """ Method Random

        Arguments
        ---------
            min             : Vector
            max             : Vector
            ID              : Integer
            seed            : Integer
            data_type       : node parameter set to 'INT'
        """

        return Integer(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, value1=None, use_clamp=False):
        """ Method add

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'ADD'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='ADD', use_clamp=use_clamp).value)

    def substract(self, value1=None, use_clamp=False):
        """ Method substract

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'SUBTRACT'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='SUBTRACT', use_clamp=use_clamp).value)

    def multiply(self, value1=None, use_clamp=False):
        """ Method multiply

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MULTIPLY'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='MULTIPLY', use_clamp=use_clamp).value)

    def divide(self, value1=None, use_clamp=False):
        """ Method divide

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'DIVIDE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='DIVIDE', use_clamp=use_clamp).value)

    def multiply_add(self, value1=None, value2=None, use_clamp=False):
        """ Method multiply_add

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'MULTIPLY_ADD'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', use_clamp=use_clamp).value)

    def pow(self, value1=None, use_clamp=False):
        """ Method pow

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'POWER'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='POWER', use_clamp=use_clamp).value)

    def log(self, value1=None, use_clamp=False):
        """ Method log

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'LOGARITHM'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='LOGARITHM', use_clamp=use_clamp).value)

    def sqrt(self, use_clamp=False):
        """ Method sqrt

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SQRT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='SQRT', use_clamp=use_clamp).value)

    def inverse_sqrt(self, use_clamp=False):
        """ Method inverse_sqrt

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'INVERSE_SQRT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='INVERSE_SQRT', use_clamp=use_clamp).value)

    def abs(self, use_clamp=False):
        """ Method abs

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ABSOLUTE'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='ABSOLUTE', use_clamp=use_clamp).value)

    def exp(self, use_clamp=False):
        """ Method exp

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'EXPONENT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='EXPONENT', use_clamp=use_clamp).value)

    def min(self, value1=None, use_clamp=False):
        """ Method min

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MINIMUM'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='MINIMUM', use_clamp=use_clamp).value)

    def max(self, value1=None, use_clamp=False):
        """ Method max

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MAXIMUM'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='MAXIMUM', use_clamp=use_clamp).value)

    def less_than(self, value1=None, use_clamp=False):
        """ Method less_than

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'LESS_THAN'
            use_clamp       : node parameter
        """

        return Boolean(nodes.NodeMath(value0=self, value1=value1, operation='LESS_THAN', use_clamp=use_clamp).value)

    def greater_than(self, value1=None, use_clamp=False):
        """ Method greater_than

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'GREATER_THAN'
            use_clamp       : node parameter
        """

        return Boolean(nodes.NodeMath(value0=self, value1=value1, operation='GREATER_THAN', use_clamp=use_clamp).value)

    def sign(self, use_clamp=False):
        """ Method sign

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SIGN'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='SIGN', use_clamp=use_clamp).value)

    def compare(self, value1=None, value2=None, use_clamp=False):
        """ Method compare

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'COMPARE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='COMPARE', use_clamp=use_clamp).value)

    def smooth_min(self, value1=None, value2=None, use_clamp=False):
        """ Method smooth_min

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'SMOOTH_MIN'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', use_clamp=use_clamp).value)

    def smooth_max(self, value1=None, value2=None, use_clamp=False):
        """ Method smooth_max

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'SMOOTH_MAX'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', use_clamp=use_clamp).value)

    def round(self, use_clamp=False):
        """ Method round

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ROUND'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='ROUND', use_clamp=use_clamp).value)

    def floor(self, use_clamp=False):
        """ Method floor

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'FLOOR'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='FLOOR', use_clamp=use_clamp).value)

    def ceil(self, use_clamp=False):
        """ Method ceil

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'CEIL'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='CEIL', use_clamp=use_clamp).value)

    def trunc(self, use_clamp=False):
        """ Method trunc

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'TRUNC'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='TRUNC', use_clamp=use_clamp).value)

    def fract(self, use_clamp=False):
        """ Method fract

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'FRACT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='FRACT', use_clamp=use_clamp).value)

    def modulo(self, value1=None, use_clamp=False):
        """ Method modulo

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MODULO'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='MODULO', use_clamp=use_clamp).value)

    def wrap(self, value1=None, value2=None, use_clamp=False):
        """ Method wrap

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'WRAP'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='WRAP', use_clamp=use_clamp).value)

    def snap(self, value1=None, use_clamp=False):
        """ Method snap

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'SNAP'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='SNAP', use_clamp=use_clamp).value)

    def pingpong(self, value1=None, use_clamp=False):
        """ Method pingpong

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'PINGPONG'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, value1=value1, operation='PINGPONG', use_clamp=use_clamp).value)

    def sin(self, use_clamp=False):
        """ Method sin

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='SINE', use_clamp=use_clamp).value)

    def cos(self, use_clamp=False):
        """ Method cos

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'COSINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='COSINE', use_clamp=use_clamp).value)

    def tan(self, use_clamp=False):
        """ Method tan

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'TANGENT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='TANGENT', use_clamp=use_clamp).value)

    def arcsin(self, use_clamp=False):
        """ Method arcsin

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ARCSINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ARCSINE', use_clamp=use_clamp).value)

    def arccos(self, use_clamp=False):
        """ Method arccos

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ARCCOSINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ARCCOSINE', use_clamp=use_clamp).value)

    def arctan(self, use_clamp=False):
        """ Method arctan

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ARCTANGENT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ARCTANGENT', use_clamp=use_clamp).value)

    def arctan2(self, value1=None, use_clamp=False):
        """ Method arctan2

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'ARCTAN2'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='ARCTAN2', use_clamp=use_clamp).value)

    def sinh(self, use_clamp=False):
        """ Method sinh

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SINH'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='SINH', use_clamp=use_clamp).value)

    def cosh(self, use_clamp=False):
        """ Method cosh

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'COSH'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='COSH', use_clamp=use_clamp).value)

    def tanh(self, use_clamp=False):
        """ Method tanh

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'TANH'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='TANH', use_clamp=use_clamp).value)

    def radians(self, use_clamp=False):
        """ Method radians

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'RADIANS'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='RADIANS', use_clamp=use_clamp).value)

    def degrees(self, use_clamp=False):
        """ Method degrees

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'DEGREES'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='DEGREES', use_clamp=use_clamp).value)

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'INT'
        """

        return Integer(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='INT').output)

    def compare(self, b=None, mode='ELEMENT', operation='EQUAL'):
        """ Method compare

        Arguments
        ---------
            a               : Float
            b               : Float
            data_type       : node parameter set to 'INT'
            mode            : node parameter
            operation       : node parameter
        """

        return Boolean(nodes.NodeCompare(a=self, b=b, data_type='INT', mode=mode, operation=operation).result)

    def to_viewer(self, geometry=None):
        """ Method to_viewer

        Arguments
        ---------
            value           : Float
            geometry        : Geometry
            data_type       : node parameter set to 'INT'
        """

        return nodes.NodeViewer(value=self, geometry=geometry, data_type='INT')

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ Method accumulate_field

        Arguments
        ---------
            value           : Vector
            group_index     : Integer
            data_type       : node parameter set to 'INT'
            domain          : node parameter
        """

        node = nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain)
        return Sockets(leading=Integer(node.leading), trailing=Integer(node.trailing), total=Integer(node.total))

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index

        Arguments
        ---------
            value           : Float
            index           : Integer
            data_type       : node parameter set to 'INT'
            domain          : node parameter
        """

        return Integer(nodes.NodeFieldatIndex(value=self, index=index, data_type='INT', domain=domain).value)


# ==============================================================================================================
# Data class Float

class Float(bcls.Float):
    """ Socket data class Float

    Constructors
    ------------
        Random               : FunctionNodeRandomValue  (data_type = FLOAT)

    Methods
    -------
        abs                  : (Float) ShaderNodeMath           (operation = ABSOLUTE)
        accumulate_field     : GeometryNodeAccumulateField(data_type = FLOAT)
        add                  : (Float) ShaderNodeMath           (operation = ADD)
        arccos               : (Float) ShaderNodeMath           (operation = ARCCOSINE)
        arcsin               : (Float) ShaderNodeMath           (operation = ARCSINE)
        arctan               : (Float) ShaderNodeMath           (operation = ARCTANGENT)
        arctan2              : (Float) ShaderNodeMath           (operation = ARCTAN2)
        ceil                 : (Integer) ShaderNodeMath           (operation = CEIL)
        color_ramp           : ShaderNodeValToRGB       
        compare              : ShaderNodeMath           (operation = COMPARE)
        compare              : FunctionNodeCompare      (data_type = FLOAT)
        cos                  : (Float) ShaderNodeMath           (operation = COSINE)
        cosh                 : (Float) ShaderNodeMath           (operation = COSH)
        degrees              : (Float) ShaderNodeMath           (operation = DEGREES)
        divide               : (Float) ShaderNodeMath           (operation = DIVIDE)
        exp                  : (Float) ShaderNodeMath           (operation = EXPONENT)
        field_at_index       : (Float) GeometryNodeFieldAtIndex (data_type = FLOAT)
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
        clamp                : node ShaderNodeClamp
        curve                : node ShaderNodeFloatCurve
        map_range            : node ShaderNodeMapRange(data_type = FLOAT)

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Method Random

        Arguments
        ---------
            min             : Vector
            max             : Vector
            ID              : Integer
            seed            : Integer
            data_type       : node parameter set to 'FLOAT'
        """

        return Float(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, value1=None, use_clamp=False):
        """ Method add

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'ADD'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='ADD', use_clamp=use_clamp).value)

    def substract(self, value1=None, use_clamp=False):
        """ Method substract

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'SUBTRACT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='SUBTRACT', use_clamp=use_clamp).value)

    def multiply(self, value1=None, use_clamp=False):
        """ Method multiply

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MULTIPLY'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='MULTIPLY', use_clamp=use_clamp).value)

    def divide(self, value1=None, use_clamp=False):
        """ Method divide

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'DIVIDE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='DIVIDE', use_clamp=use_clamp).value)

    def multiply_add(self, value1=None, value2=None, use_clamp=False):
        """ Method multiply_add

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'MULTIPLY_ADD'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', use_clamp=use_clamp).value)

    def pow(self, value1=None, use_clamp=False):
        """ Method pow

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'POWER'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='POWER', use_clamp=use_clamp).value)

    def log(self, value1=None, use_clamp=False):
        """ Method log

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'LOGARITHM'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='LOGARITHM', use_clamp=use_clamp).value)

    def sqrt(self, use_clamp=False):
        """ Method sqrt

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SQRT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='SQRT', use_clamp=use_clamp).value)

    def inverse_sqrt(self, use_clamp=False):
        """ Method inverse_sqrt

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'INVERSE_SQRT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='INVERSE_SQRT', use_clamp=use_clamp).value)

    def abs(self, use_clamp=False):
        """ Method abs

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ABSOLUTE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ABSOLUTE', use_clamp=use_clamp).value)

    def exp(self, use_clamp=False):
        """ Method exp

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'EXPONENT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='EXPONENT', use_clamp=use_clamp).value)

    def min(self, value1=None, use_clamp=False):
        """ Method min

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MINIMUM'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='MINIMUM', use_clamp=use_clamp).value)

    def max(self, value1=None, use_clamp=False):
        """ Method max

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MAXIMUM'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='MAXIMUM', use_clamp=use_clamp).value)

    def less_than(self, value1=None, use_clamp=False):
        """ Method less_than

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'LESS_THAN'
            use_clamp       : node parameter
        """

        return Boolean(nodes.NodeMath(value0=self, value1=value1, operation='LESS_THAN', use_clamp=use_clamp).value)

    def greater_than(self, value1=None, use_clamp=False):
        """ Method greater_than

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'GREATER_THAN'
            use_clamp       : node parameter
        """

        return Boolean(nodes.NodeMath(value0=self, value1=value1, operation='GREATER_THAN', use_clamp=use_clamp).value)

    def sign(self, use_clamp=False):
        """ Method sign

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SIGN'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='SIGN', use_clamp=use_clamp).value)

    def compare(self, value1=None, value2=None, use_clamp=False):
        """ Method compare

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'COMPARE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='COMPARE', use_clamp=use_clamp).value)

    def smooth_min(self, value1=None, value2=None, use_clamp=False):
        """ Method smooth_min

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'SMOOTH_MIN'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', use_clamp=use_clamp).value)

    def smooth_max(self, value1=None, value2=None, use_clamp=False):
        """ Method smooth_max

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'SMOOTH_MAX'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', use_clamp=use_clamp).value)

    def round(self, use_clamp=False):
        """ Method round

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ROUND'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='ROUND', use_clamp=use_clamp).value)

    def floor(self, use_clamp=False):
        """ Method floor

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'FLOOR'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='FLOOR', use_clamp=use_clamp).value)

    def ceil(self, use_clamp=False):
        """ Method ceil

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'CEIL'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='CEIL', use_clamp=use_clamp).value)

    def trunc(self, use_clamp=False):
        """ Method trunc

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'TRUNC'
            use_clamp       : node parameter
        """

        return Integer(nodes.NodeMath(value0=self, operation='TRUNC', use_clamp=use_clamp).value)

    def fract(self, use_clamp=False):
        """ Method fract

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'FRACT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='FRACT', use_clamp=use_clamp).value)

    def modulo(self, value1=None, use_clamp=False):
        """ Method modulo

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'MODULO'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='MODULO', use_clamp=use_clamp).value)

    def wrap(self, value1=None, value2=None, use_clamp=False):
        """ Method wrap

        Arguments
        ---------
            value0          : Float
            value1          : Float
            value2          : Float
            operation       : node parameter set to 'WRAP'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='WRAP', use_clamp=use_clamp).value)

    def snap(self, value1=None, use_clamp=False):
        """ Method snap

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'SNAP'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='SNAP', use_clamp=use_clamp).value)

    def pingpong(self, value1=None, use_clamp=False):
        """ Method pingpong

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'PINGPONG'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='PINGPONG', use_clamp=use_clamp).value)

    def sin(self, use_clamp=False):
        """ Method sin

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='SINE', use_clamp=use_clamp).value)

    def cos(self, use_clamp=False):
        """ Method cos

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'COSINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='COSINE', use_clamp=use_clamp).value)

    def tan(self, use_clamp=False):
        """ Method tan

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'TANGENT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='TANGENT', use_clamp=use_clamp).value)

    def arcsin(self, use_clamp=False):
        """ Method arcsin

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ARCSINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ARCSINE', use_clamp=use_clamp).value)

    def arccos(self, use_clamp=False):
        """ Method arccos

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ARCCOSINE'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ARCCOSINE', use_clamp=use_clamp).value)

    def arctan(self, use_clamp=False):
        """ Method arctan

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'ARCTANGENT'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='ARCTANGENT', use_clamp=use_clamp).value)

    def arctan2(self, value1=None, use_clamp=False):
        """ Method arctan2

        Arguments
        ---------
            value0          : Float
            value1          : Float
            operation       : node parameter set to 'ARCTAN2'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, value1=value1, operation='ARCTAN2', use_clamp=use_clamp).value)

    def sinh(self, use_clamp=False):
        """ Method sinh

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'SINH'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='SINH', use_clamp=use_clamp).value)

    def cosh(self, use_clamp=False):
        """ Method cosh

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'COSH'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='COSH', use_clamp=use_clamp).value)

    def tanh(self, use_clamp=False):
        """ Method tanh

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'TANH'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='TANH', use_clamp=use_clamp).value)

    def radians(self, use_clamp=False):
        """ Method radians

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'RADIANS'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='RADIANS', use_clamp=use_clamp).value)

    def degrees(self, use_clamp=False):
        """ Method degrees

        Arguments
        ---------
            value0          : Float
            operation       : node parameter set to 'DEGREES'
            use_clamp       : node parameter
        """

        return Float(nodes.NodeMath(value0=self, operation='DEGREES', use_clamp=use_clamp).value)

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'FLOAT'
        """

        return Float(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='FLOAT').output)

    def compare(self, b=None, epsilon=None, mode='ELEMENT', operation='EQUAL'):
        """ Method compare

        Arguments
        ---------
            a               : Float
            b               : Float
            epsilon         : Float
            data_type       : node parameter set to 'FLOAT'
            mode            : node parameter
            operation       : node parameter
        """

        return Boolean(nodes.NodeCompare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode=mode, operation=operation).result)

    def to_viewer(self, geometry=None):
        """ Method to_viewer

        Arguments
        ---------
            value           : Float
            geometry        : Geometry
            data_type       : node parameter set to 'FLOAT'
        """

        return nodes.NodeViewer(value=self, geometry=geometry, data_type='FLOAT')

    def to_integer(self, rounding_mode='ROUND'):
        """ Method to_integer

        Arguments
        ---------
            float           : Float
            rounding_mode   : node parameter
        """

        return Integer(nodes.NodeFloattoInteger(float=self, rounding_mode=rounding_mode).integer)

    def to_string(self, decimals=None):
        """ Method to_string

        Arguments
        ---------
            value           : Float
            decimals        : Integer
        """

        return String(nodes.NodeValuetoString(value=self, decimals=decimals).string)

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ Method accumulate_field

        Arguments
        ---------
            value           : Vector
            group_index     : Integer
            data_type       : node parameter set to 'FLOAT'
            domain          : node parameter
        """

        node = nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain)
        return Sockets(leading=Float(node.leading), trailing=Float(node.trailing), total=Float(node.total))

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index

        Arguments
        ---------
            value           : Float
            index           : Integer
            data_type       : node parameter set to 'FLOAT'
            domain          : node parameter
        """

        return Float(nodes.NodeFieldatIndex(value=self, index=index, data_type='FLOAT', domain=domain).value)

    def color_ramp(self):
        """ Method color_ramp

        Arguments
        ---------
            fac             : Float
        """

        node = nodes.NodeColorRamp(fac=self)
        return Sockets(color=Color(node.color), alpha=Float(node.alpha))


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curve(self, value=None):
        """ Method curve

        Arguments
        ---------
            factor          : Float
            value           : Float
        """

        return self.stack(nodes.NodeFloatCurve(factor=self, value=value))

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        """ Method clamp

        Arguments
        ---------
            value           : Float
            min             : Float
            max             : Float
            clamp_type      : node parameter
        """

        return self.stack(nodes.NodeClamp(value=self, min=min, max=max, clamp_type=clamp_type))

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """ Method map_range

        Arguments
        ---------
            value           : Float
            from_min        : Float
            from_max        : Float
            to_min          : Float
            to_max          : Float
            steps           : Float
            clamp           : node parameter
            data_type       : node parameter set to 'FLOAT'
            interpolation_type : node parameter
        """

        return self.stack(nodes.NodeMapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type))


# ==============================================================================================================
# Data class Vector

class Vector(bcls.Vector):
    """ Socket data class Vector

    Constructors
    ------------
        AlignToVector        : (cls) FunctionNodeAlignEulerToVector
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
        accumulate_field     : GeometryNodeAccumulateField(data_type = FLOAT_VECTOR)
        add                  : ShaderNodeVectorMath     (operation = ADD)
        ceil                 : ShaderNodeVectorMath     (operation = CEIL)
        compare              : FunctionNodeCompare      (data_type = VECTOR)
        cos                  : ShaderNodeVectorMath     (operation = COSINE)
        cross                : ShaderNodeVectorMath     (operation = CROSS_PRODUCT)
        distance             : ShaderNodeVectorMath     (operation = DISTANCE)
        divide               : ShaderNodeVectorMath     (operation = DIVIDE)
        dot                  : ShaderNodeVectorMath     (operation = DOT_PRODUCT)
        faceforward          : ShaderNodeVectorMath     (operation = FACEFORWARD)
        field_at_index       : (Vector) GeometryNodeFieldAtIndex (data_type = FLOAT_VECTOR)
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
        substract            : ShaderNodeVectorMath     (operation = SUBTRACT)
        switch               : GeometryNodeSwitch       (input_type = VECTOR)
        tan                  : ShaderNodeVectorMath     (operation = TANGENT)
        to_viewer            : node GeometryNodeViewer(data_type = FLOAT_VECTOR)
        wrap                 : ShaderNodeVectorMath     (operation = WRAP)

    Stacked methods
    ---------------
        align_to_vector      : node FunctionNodeAlignEulerToVector
        curves               : node ShaderNodeVectorCurve
        map_range            : node ShaderNodeMapRange(data_type = FLOAT_VECTOR)
        rotate_euler         : node FunctionNodeRotateEuler

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Method Random

        Arguments
        ---------
            min             : Vector
            max             : Vector
            ID              : Integer
            seed            : Integer
            data_type       : node parameter set to 'FLOAT_VECTOR'
        """

        return Vector(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """ Method Combine

        Arguments
        ---------
            x               : Float
            y               : Float
            z               : Float
        """

        return cls(nodes.NodeCombineXYZ(x=x, y=y, z=z).vector)

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ Method AlignToVector

        Arguments
        ---------
            rotation        : Vector
            factor          : Float
            vector          : Vector
            axis            : node parameter
            pivot_axis      : node parameter
        """

        return cls(nodes.NodeAlignEulertoVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    # ---------- Node SeparateXYZ

    @property
    def separate(self):
        if not hasattr(self.top, 'separate_'):
            self.top.separate_ = nodes.NodeSeparateXYZ(self)
            self.top.separate_.prop_of = self.node
        return self.top.separate_

    @property
    def x(self):
        if not hasattr(self.top, 'x_'):
            self.top.x_ = Float(self.top.separate.x)
        return self.top.x_

    @x.setter
    def x(self, value):
        _ = self.separate
        self.top.x_ = value

    @property
    def y(self):
        if not hasattr(self.top, 'y_'):
            self.top.y_ = Float(self.top.separate.y)
        return self.top.y_

    @y.setter
    def y(self, value):
        _ = self.separate
        self.top.y_ = value

    @property
    def z(self):
        if not hasattr(self.top, 'z_'):
            self.top.z_ = Float(self.top.separate.z)
        return self.top.z_

    @z.setter
    def z(self, value):
        _ = self.separate
        self.top.z_ = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, vector1=None):
        """ Method add

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'ADD'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='ADD').vector)

    def substract(self, vector1=None):
        """ Method substract

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'SUBTRACT'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SUBTRACT').vector)

    def multiply(self, vector1=None):
        """ Method multiply

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'MULTIPLY'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MULTIPLY').vector)

    def divide(self, vector1=None):
        """ Method divide

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'DIVIDE'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DIVIDE').vector)

    def multiply_add(self, vector1=None, vector2=None):
        """ Method multiply_add

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            vector2         : Vector
            operation       : node parameter set to 'MULTIPLY_ADD'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector)

    def cross(self, vector1=None):
        """ Method cross

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'CROSS_PRODUCT'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT').vector)

    def project(self, vector1=None):
        """ Method project

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'PROJECT'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='PROJECT').vector)

    def reflect(self, vector1=None):
        """ Method reflect

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'REFLECT'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='REFLECT').vector)

    def refract(self, vector1=None, scale=None):
        """ Method refract

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            scale           : Float
            operation       : node parameter set to 'REFRACT'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT').vector)

    def faceforward(self, vector1=None, vector2=None):
        """ Method faceforward

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            vector2         : Vector
            operation       : node parameter set to 'FACEFORWARD'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector)

    def dot(self, vector1=None):
        """ Method dot

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'DOT_PRODUCT'
        """

        return Float(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT').value)

    def distance(self, vector1=None):
        """ Method distance

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'DISTANCE'
        """

        return Float(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DISTANCE').value)

    def length(self):
        """ Method length

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'LENGTH'
        """

        return Float(nodes.NodeVectorMath(vector0=self, operation='LENGTH').value)

    def scale(self, scale=None):
        """ Method scale

        Arguments
        ---------
            vector0         : Vector
            scale           : Float
            operation       : node parameter set to 'SCALE'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, scale=scale, operation='SCALE').vector)

    def normalize(self):
        """ Method normalize

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'NORMALIZE'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='NORMALIZE').vector)

    def absolute(self):
        """ Method absolute

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'ABSOLUTE'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='ABSOLUTE').vector)

    def min(self, vector1=None):
        """ Method min

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'MINIMUM'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MINIMUM').vector)

    def max(self, vector1=None):
        """ Method max

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'MAXIMUM'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MAXIMUM').vector)

    def floor(self):
        """ Method floor

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'FLOOR'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='FLOOR').vector)

    def ceil(self):
        """ Method ceil

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'CEIL'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='CEIL').vector)

    def fraction(self):
        """ Method fraction

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'FRACTION'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='FRACTION').vector)

    def modulo(self, vector1=None):
        """ Method modulo

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'MODULO'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MODULO').vector)

    def wrap(self, vector1=None, vector2=None):
        """ Method wrap

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            vector2         : Vector
            operation       : node parameter set to 'WRAP'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP').vector)

    def snap(self, vector1=None):
        """ Method snap

        Arguments
        ---------
            vector0         : Vector
            vector1         : Vector
            operation       : node parameter set to 'SNAP'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SNAP').vector)

    def sin(self):
        """ Method sin

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'SINE'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='SINE').vector)

    def cos(self):
        """ Method cos

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'COSINE'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='COSINE').vector)

    def tan(self):
        """ Method tan

        Arguments
        ---------
            vector0         : Vector
            operation       : node parameter set to 'TANGENT'
        """

        return Vector(nodes.NodeVectorMath(vector0=self, operation='TANGENT').vector)

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'VECTOR'
        """

        return Vector(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='VECTOR').output)

    def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='EQUAL'):
        """ Method compare

        Arguments
        ---------
            a               : Float
            b               : Float
            c               : Float
            angle           : Float
            epsilon         : Float
            data_type       : node parameter set to 'VECTOR'
            mode            : node parameter
            operation       : node parameter
        """

        return Boolean(nodes.NodeCompare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation=operation).result)

    def to_viewer(self, geometry=None):
        """ Method to_viewer

        Arguments
        ---------
            value           : Float
            geometry        : Geometry
            data_type       : node parameter set to 'FLOAT_VECTOR'
        """

        return nodes.NodeViewer(value=self, geometry=geometry, data_type='FLOAT_VECTOR')

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
        """ Method rotate

        Arguments
        ---------
            vector          : Vector
            center          : Vector
            axis            : Vector
            angle           : Float
            rotation        : Vector
            invert          : node parameter
            rotation_type   : node parameter
        """

        return Vector(nodes.NodeVectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type).vector)

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ Method accumulate_field

        Arguments
        ---------
            value           : Vector
            group_index     : Integer
            data_type       : node parameter set to 'FLOAT_VECTOR'
            domain          : node parameter
        """

        node = nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)
        return Sockets(leading=Vector(node.leading), trailing=Vector(node.trailing), total=Vector(node.total))

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index

        Arguments
        ---------
            value           : Float
            index           : Integer
            data_type       : node parameter set to 'FLOAT_VECTOR'
            domain          : node parameter
        """

        return Vector(nodes.NodeFieldatIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain).value)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """ Method curves

        Arguments
        ---------
            vector          : Vector
            fac             : Float
        """

        return self.stack(nodes.NodeVectorCurves(vector=self, fac=fac))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ Method align_to_vector

        Arguments
        ---------
            rotation        : Vector
            factor          : Float
            vector          : Vector
            axis            : node parameter
            pivot_axis      : node parameter
        """

        return self.stack(nodes.NodeAlignEulertoVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))

    def rotate_euler(self, rotate_by=None, axis=None, angle=None, space='OBJECT'):
        """ Method rotate_euler

        Arguments
        ---------
            rotation        : Vector
            rotate_by       : Vector
            axis            : Vector
            angle           : Float
            space           : node parameter
        """

        return self.stack(nodes.NodeRotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, space=space))

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """ Method map_range

        Arguments
        ---------
            vector          : Vector
            from_min        : Float
            from_max        : Float
            to_min          : Float
            to_max          : Float
            steps           : Float
            clamp           : node parameter
            data_type       : node parameter set to 'FLOAT_VECTOR'
            interpolation_type : node parameter
        """

        return self.stack(nodes.NodeMapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type))


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
        compare              : FunctionNodeCompare      (data_type = RGBA)
        field_at_index       : (Color) GeometryNodeFieldAtIndex (data_type = FLOAT_COLOR)
        mix                  : ShaderNodeMixRGB         
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
        """ Method Combine

        Arguments
        ---------
            r               : Float
            g               : Float
            b               : Float
        """

        return cls(nodes.NodeCombineRGB(r=r, g=g, b=b).image)


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    # ---------- Node SeparateRGB

    @property
    def separate(self):
        if not hasattr(self.top, 'separate_'):
            self.top.separate_ = nodes.NodeSeparateRGB(self)
            self.top.separate_.prop_of = self.node
        return self.top.separate_

    @property
    def r(self):
        if not hasattr(self.top, 'r_'):
            self.top.r_ = Float(self.top.separate.r)
        return self.top.r_

    @r.setter
    def r(self, value):
        _ = self.separate
        self.top.r_ = value

    @property
    def g(self):
        if not hasattr(self.top, 'g_'):
            self.top.g_ = Float(self.top.separate.g)
        return self.top.g_

    @g.setter
    def g(self, value):
        _ = self.separate
        self.top.g_ = value

    @property
    def b(self):
        if not hasattr(self.top, 'b_'):
            self.top.b_ = Float(self.top.separate.b)
        return self.top.b_

    @b.setter
    def b(self, value):
        _ = self.separate
        self.top.b_ = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'RGBA'
        """

        return Color(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='RGBA').output)

    def compare(self, b=None, epsilon=None, mode='ELEMENT', operation='EQUAL'):
        """ Method compare

        Arguments
        ---------
            a               : Float
            b               : Float
            epsilon         : Float
            data_type       : node parameter set to 'RGBA'
            mode            : node parameter
            operation       : node parameter
        """

        return Boolean(nodes.NodeCompare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode=mode, operation=operation).result)

    def to_viewer(self, geometry=None):
        """ Method to_viewer

        Arguments
        ---------
            value           : Float
            geometry        : Geometry
            data_type       : node parameter set to 'FLOAT_COLOR'
        """

        return nodes.NodeViewer(value=self, geometry=geometry, data_type='FLOAT_COLOR')

    def mix(self, fac=None, color2=None, blend_type='MIX', use_alpha=False, use_clamp=False):
        """ Method mix

        Arguments
        ---------
            color1          : Color
            fac             : Float
            color2          : Color
            blend_type      : node parameter
            use_alpha       : node parameter
            use_clamp       : node parameter
        """

        return Color(nodes.NodeMix(color1=self, fac=fac, color2=color2, blend_type=blend_type, use_alpha=use_alpha, use_clamp=use_clamp).color)

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index

        Arguments
        ---------
            value           : Float
            index           : Integer
            data_type       : node parameter set to 'FLOAT_COLOR'
            domain          : node parameter
        """

        return Color(nodes.NodeFieldatIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain).value)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """ Method curves

        Arguments
        ---------
            color           : Color
            fac             : Float
        """

        return self.stack(nodes.NodeRGBCurves(color=self, fac=fac))


# ==============================================================================================================
# Data class String

class String(bcls.String):
    """ Socket data class String

    Properties
    ----------
        length               : (Integer) FunctionNodeStringLength 

    Methods
    -------
        compare              : FunctionNodeCompare      (data_type = STRING)
        join                 : GeometryNodeStringJoin   
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
        """ Method length

        Arguments
        ---------
            string          : String
        """

        return Integer(nodes.NodeStringLength(string=self).length)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'STRING'
        """

        return String(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='STRING').output)

    def compare(self, b=None, mode='ELEMENT', operation='EQUAL'):
        """ Method compare

        Arguments
        ---------
            a               : Float
            b               : Float
            data_type       : node parameter set to 'STRING'
            mode            : node parameter
            operation       : node parameter
        """

        return Boolean(nodes.NodeCompare(a=self, b=b, data_type='STRING', mode=mode, operation=operation).result)

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """ Method to_curves

        Arguments
        ---------
            string          : String
            size            : Float
            character_spacing : Float
            word_spacing    : Float
            line_spacing    : Float
            text_box_width  : Float
            text_box_height : Float
            align_x         : node parameter
            align_y         : node parameter
            overflow        : node parameter
            pivot_mode      : node parameter
        """

        node = nodes.NodeStringtoCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
        return Sockets(curve_instances=Geometry(node.curve_instances), line=Integer(node.line), pivot_point=Vector(node.pivot_point))

    def join(self, *strings, delimiter=None):
        """ Method join

        Arguments
        ---------
            strings         : String (multi input)
            delimiter       : String
        """

        return String(nodes.NodeJoinStrings(self, *strings, delimiter=delimiter).string)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def replace(self, find=None, replace=None):
        """ Method replace

        Arguments
        ---------
            string          : String
            find            : String
            replace         : String
        """

        return self.stack(nodes.NodeReplaceString(string=self, find=find, replace=replace))

    def slice(self, position=None, length=None):
        """ Method slice

        Arguments
        ---------
            string          : String
            position        : Integer
            length          : Integer
        """

        return self.stack(nodes.NodeSliceString(string=self, position=position, length=length))


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
        proximity            : GeometryNodeProximity    
        raycast              : GeometryNodeRaycast      
        switch               : GeometryNodeSwitch       (input_type = GEOMETRY)
        to_instance          : (Instances) GeometryNodeGeometryToInstance
        transfer_boolean     : GeometryNodeAttributeTransfer(data_type = BOOLEAN)
        transfer_color       : GeometryNodeAttributeTransfer(data_type = FLOAT_COLOR)
        transfer_float       : GeometryNodeAttributeTransfer(data_type = FLOAT)
        transfer_integer     : GeometryNodeAttributeTransfer(data_type = INT)
        transfer_vector      : GeometryNodeAttributeTransfer(data_type = FLOAT_VECTOR)

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
        if not hasattr(self.top, 'bound_box_'):
            self.top.bound_box_ = nodes.NodeBoundingBox(self)
            self.top.bound_box_.prop_of = self.node
        return self.top.bound_box_

    @property
    def box(self):
        if not hasattr(self.top, 'box_'):
            self.top.box_ = Geometry(self.top.bound_box.bounding_box)
        return self.top.box_

    @box.setter
    def box(self, value):
        _ = self.bound_box
        self.top.box_ = value

    @property
    def box_min(self):
        if not hasattr(self.top, 'box_min_'):
            self.top.box_min_ = Vector(self.top.bound_box.min)
        return self.top.box_min_

    @box_min.setter
    def box_min(self, value):
        _ = self.bound_box
        self.top.box_min_ = value

    @property
    def box_max(self):
        if not hasattr(self.top, 'box_max_'):
            self.top.box_max_ = Vector(self.top.bound_box.max)
        return self.top.box_max_

    @box_max.setter
    def box_max(self, value):
        _ = self.bound_box
        self.top.box_max_ = value

    # ---------- Node SeparateComponents

    @property
    def components(self):
        if not hasattr(self.top, 'components_'):
            self.top.components_ = nodes.NodeSeparateComponents(self)
            self.top.components_.prop_of = self.node
        return self.top.components_

    @property
    def mesh_component(self):
        if not hasattr(self.top, 'mesh_component_'):
            self.top.mesh_component_ = Mesh(self.top.components.mesh)
        return self.top.mesh_component_

    @mesh_component.setter
    def mesh_component(self, value):
        _ = self.components
        self.top.mesh_component_ = value

    @property
    def points_component(self):
        if not hasattr(self.top, 'points_component_'):
            self.top.points_component_ = Geometry(self.top.components.point_cloud)
        return self.top.points_component_

    @points_component.setter
    def points_component(self, value):
        _ = self.components
        self.top.points_component_ = value

    @property
    def curve_component(self):
        if not hasattr(self.top, 'curve_component_'):
            self.top.curve_component_ = Curve(self.top.components.curve)
        return self.top.curve_component_

    @curve_component.setter
    def curve_component(self, value):
        _ = self.components
        self.top.curve_component_ = value

    @property
    def volume_component(self):
        if not hasattr(self.top, 'volume_component_'):
            self.top.volume_component_ = Volume(self.top.components.volume)
        return self.top.volume_component_

    @volume_component.setter
    def volume_component(self, value):
        _ = self.components
        self.top.volume_component_ = value

    @property
    def instances_component(self):
        if not hasattr(self.top, 'instances_component_'):
            self.top.instances_component_ = Instances(self.top.components.instances)
        return self.top.instances_component_

    @instances_component.setter
    def instances_component(self, value):
        _ = self.components
        self.top.instances_component_ = value


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputNormal

    def capture_normal(self, domain='POINT'):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    @property
    def point_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='POINT').outputs[0])

    @property
    def edge_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[0])

    @property
    def face_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='FACE').outputs[0])

    @property
    def corner_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='INSTANCE').outputs[0])

    # ---------- Attribute GeometryNodeInputTangent

    def capture_tangent(self, domain='POINT'):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    @property
    def point_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='POINT').outputs[0])

    @property
    def edge_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[0])

    @property
    def face_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='FACE').outputs[0])

    @property
    def corner_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='INSTANCE').outputs[0])

    # ---------- Attribute GeometryNodeInputID

    def capture_ID(self, domain='POINT'):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    # ---------- Attribute GeometryNodeInputIndex

    def capture_index(self, domain='POINT'):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    # ---------- Attribute GeometryNodeInputPosition

    def capture_position(self, domain='POINT'):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    @property
    def position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='POINT').outputs[0])

    # ---------- Attribute GeometryNodeIsViewport

    def capture_is_viewport(self, domain='POINT'):
        return Boolean(nodes.NodeIsViewport(owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    @property
    def is_viewport(self):
        return Boolean(nodes.NodeIsViewport(owner_socket=self.socket, data_type='BOOLEAN', domain='POINT').outputs[0])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'GEOMETRY'
        """

        return Geometry(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='GEOMETRY').output)

    def transfer_boolean(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_boolean

        Arguments
        ---------
            source          : Geometry
            attribute       : Vector
            source_position : Vector
            index           : Integer
            data_type       : node parameter set to 'BOOLEAN'
            domain          : node parameter
            mapping         : node parameter
        """

        return Boolean(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute)

    def transfer_integer(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_integer

        Arguments
        ---------
            source          : Geometry
            attribute       : Vector
            source_position : Vector
            index           : Integer
            data_type       : node parameter set to 'INT'
            domain          : node parameter
            mapping         : node parameter
        """

        return Integer(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping).attribute)

    def transfer_float(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_float

        Arguments
        ---------
            source          : Geometry
            attribute       : Vector
            source_position : Vector
            index           : Integer
            data_type       : node parameter set to 'FLOAT'
            domain          : node parameter
            mapping         : node parameter
        """

        return Float(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping).attribute)

    def transfer_vector(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_vector

        Arguments
        ---------
            source          : Geometry
            attribute       : Vector
            source_position : Vector
            index           : Integer
            data_type       : node parameter set to 'FLOAT_VECTOR'
            domain          : node parameter
            mapping         : node parameter
        """

        return Vector(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute)

    def transfer_color(self, attribute=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ Method transfer_color

        Arguments
        ---------
            source          : Geometry
            attribute       : Vector
            source_position : Vector
            index           : Integer
            data_type       : node parameter set to 'FLOAT_COLOR'
            domain          : node parameter
            mapping         : node parameter
        """

        return Color(nodes.NodeTransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping).attribute)

    def attribute_domain_size(self, component='MESH'):
        """ Method attribute_domain_size

        Arguments
        ---------
            geometry        : Geometry
            component       : node parameter
        """

        node = nodes.NodeDomainSize(geometry=self, component=component)
        return Sockets(point_count=Integer(node.point_count), edge_count=Integer(node.edge_count), face_count=Integer(node.face_count), face_corner_count=Integer(node.face_corner_count))

    def attribute_remove(self, *attribute):
        """ Method attribute_remove

        Arguments
        ---------
            geometry        : Geometry
            attribute       : String (multi input)
        """

        return Geometry(nodes.NodeAttributeRemove(*attribute, geometry=self).geometry)

    def attribute_statistic(self, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
        """ Method attribute_statistic

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            attribute       : Float
            data_type       : node parameter
            domain          : node parameter
        """

        node = nodes.NodeAttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type, domain=domain)
        return Sockets(mean=Float(node.mean), median=Float(node.median), sum=Float(node.sum), min=Float(node.min), max=Float(node.max), range=Float(node.range), standard_deviation=Float(node.standard_deviation), variance=Float(node.variance))

    def components(self, selection=None, domain='POINT'):
        """ Method components

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            domain          : node parameter
        """

        node = nodes.NodeSeparateGeometry(geometry=self, selection=selection, domain=domain)
        return Sockets(selection=Geometry(node.selection), inverted=Geometry(node.inverted))

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT'):
        """ Method capture_attribute

        Arguments
        ---------
            geometry        : Geometry
            value           : Vector
            data_type       : node parameter
            domain          : node parameter
        """

        node = nodes.NodeCaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain)
        return Sockets(geometry=Geometry(node.geometry), attribute=Float(node.attribute))

    def convex_hull(self):
        """ Method convex_hull

        Arguments
        ---------
            geometry        : Geometry
        """

        return Mesh(nodes.NodeConvexHull(geometry=self).convex_hull)

    def to_instance(self, *geometry):
        """ Method to_instance

        Arguments
        ---------
            geometry        : Geometry (multi input)
        """

        return Instances(nodes.NodeGeometrytoInstance(self, *geometry).instances)

    def join(self, *geometry):
        """ Method join

        Arguments
        ---------
            geometry        : Geometry (multi input)
        """

        return Geometry(nodes.NodeJoinGeometry(self, *geometry).geometry)

    def proximity(self, source_position=None, target_element='FACES'):
        """ Method proximity

        Arguments
        ---------
            target          : Geometry
            source_position : Vector
            target_element  : node parameter
        """

        node = nodes.NodeGeometryProximity(target=self, source_position=source_position, target_element=target_element)
        return Sockets(position=Vector(node.position), distance=Float(node.distance))

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):
        """ Method raycast

        Arguments
        ---------
            target_geometry : Geometry
            attribute       : Vector
            source_position : Vector
            ray_direction   : Vector
            ray_length      : Float
            data_type       : node parameter
            mapping         : node parameter
        """

        node = nodes.NodeRaycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type, mapping=mapping)
        return Sockets(is_hit=Boolean(node.is_hit), hit_position=Vector(node.hit_position), hit_normal=Vector(node.hit_normal), hit_distance=Float(node.hit_distance), attribute=Float(node.attribute))


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        """ Method delete_geometry

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            domain          : node parameter
            mode            : node parameter
        """

        return self.stack(nodes.NodeDeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))

    def merge_by_distance(self, selection=None, distance=None):
        """ Method merge_by_distance

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            distance        : Float
        """

        return self.stack(nodes.NodeMergebyDistance(geometry=self, selection=selection, distance=distance))

    def realize_instances(self, legacy_behavior=False):
        """ Method realize_instances

        Arguments
        ---------
            geometry        : Geometry
            legacy_behavior : node parameter
        """

        return self.stack(nodes.NodeRealizeInstances(geometry=self, legacy_behavior=legacy_behavior))

    def replace_material(self, old=None, new=None):
        """ Method replace_material

        Arguments
        ---------
            geometry        : Geometry
            old             : Material
            new             : Material
        """

        return self.stack(nodes.NodeReplaceMaterial(geometry=self, old=old, new=new))

    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """ Method scale_elements

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            scale           : Float
            center          : Vector
            axis            : Vector
            domain          : node parameter
            scale_mode      : node parameter
        """

        return self.stack(nodes.NodeScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))

    def set_ID(self, selection=None, ID=None):
        """ Method set_ID

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            ID              : Integer
        """

        return self.stack(nodes.NodeSetID(geometry=self, selection=selection, ID=ID))

    def set_material(self, selection=None, material=None):
        """ Method set_material

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            material        : Material
        """

        return self.stack(nodes.NodeSetMaterial(geometry=self, selection=selection, material=material))

    def set_material_index(self, selection=None, material_index=None):
        """ Method set_material_index

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            material_index  : Integer
        """

        return self.stack(nodes.NodeSetMaterialIndex(geometry=self, selection=selection, material_index=material_index))

    def set_position(self, selection=None, position=None, offset=None):
        """ Method set_position

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            position        : Vector
            offset          : Vector
        """

        return self.stack(nodes.NodeSetPosition(geometry=self, selection=selection, position=position, offset=offset))

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """ Method set_shade_smooth

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            shade_smooth    : Boolean
        """

        return self.stack(nodes.NodeSetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))

    def transform(self, translation=None, rotation=None, scale=None):
        """ Method transform

        Arguments
        ---------
            geometry        : Geometry
            translation     : Vector
            rotation        : Vector
            scale           : Vector
        """

        return self.stack(nodes.NodeTransform(geometry=self, translation=translation, rotation=rotation, scale=scale))


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
        return Boolean(nodes.NodeIsSplineCyclic(owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    @property
    def cyclic(self):
        return Boolean(nodes.NodeIsSplineCyclic(owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputSplineResolution

    def capture_resolution(self, domain='CURVE'):
        return Integer(nodes.NodeSplineResolution(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def resolution(self):
        return Integer(nodes.NodeSplineResolution(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeSplineLength

    def capture_length(self, domain='CURVE'):
        return Float(nodes.NodeSplineLength(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def length(self):
        return Float(nodes.NodeSplineLength(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    def capture_point_count(self, domain='CURVE'):
        return Integer(nodes.NodeSplineLength(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def point_count(self):
        return Integer(nodes.NodeSplineLength(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[1])

    # ---------- Attribute GeometryNodeSplineParameter

    def capture_parameter_factor(self, domain='CURVE'):
        return Float(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def parameter_factor(self):
        return Float(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    def capture_parameter_length(self, domain='CURVE'):
        return Float(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[1])

    @property
    def parameter_length(self):
        return Float(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[1])

    def capture_parameter_index(self, domain='CURVE'):
        return Integer(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='INT', domain=domain).outputs[2])

    @property
    def parameter_index(self):
        return Integer(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[2])


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_cyclic(self, selection=None, cyclic=None):
        """ Method set_cyclic

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            cyclic          : Boolean
        """

        return self.stack(nodes.NodeSetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic))

    def set_resolution(self, selection=None, resolution=None):
        """ Method set_resolution

        Arguments
        ---------
            geometry        : Geometry
            selection       : Boolean
            resolution      : Integer
        """

        return self.stack(nodes.NodeSetSplineResolution(geometry=self, selection=selection, resolution=resolution))


# ==============================================================================================================
# Data class Curve

class Curve(Spline):
    """ Socket data class Curve

    Constructors
    ------------
        ArcFromRadius        : (cls) GeometryNodeCurveArc     (mode = RADIUS)
        BezierSegment        : (cls) GeometryNodeCurvePrimitiveBezierSegment
        Circle               : (cls) GeometryNodeCurvePrimitiveCircle
        Line                 : (cls) GeometryNodeCurvePrimitiveLine
        QuadraticBezier      : (cls) GeometryNodeCurveQuadraticBezier
        Quadrilateral        : (cls) GeometryNodeCurvePrimitiveQuadrilateral
        Spiral               : (cls) GeometryNodeCurveSpiral  
        Star                 : (cls) GeometryNodeCurveStar    

    Static methods
    --------------
        ArcFromPoints        : GeometryNodeCurveArc     (mode = POINTS)

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
        """ Method BezierSegment

        Arguments
        ---------
            resolution      : Integer
            start           : Vector
            start_handle    : Vector
            end_handle      : Vector
            end             : Vector
            mode            : node parameter
        """

        return cls(nodes.NodeBezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)

    @classmethod
    def Circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):
        """ Method Circle

        Arguments
        ---------
            resolution      : Integer
            point_1         : Vector
            point_2         : Vector
            point_3         : Vector
            radius          : Float
            mode            : node parameter
        """

        return cls(nodes.NodeCurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode).curve)

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None, mode='POINTS'):
        """ Method Line

        Arguments
        ---------
            start           : Vector
            end             : Vector
            direction       : Vector
            length          : Float
            mode            : node parameter
        """

        return cls(nodes.NodeCurveLine(start=start, end=end, direction=direction, length=length, mode=mode).curve)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """ Method Quadrilateral

        Arguments
        ---------
            width           : Float
            height          : Float
            bottom_width    : Float
            top_width       : Float
            offset          : Float
            bottom_height   : Float
            top_height      : Float
            point_1         : Vector
            point_2         : Vector
            point_3         : Vector
            point_4         : Vector
            mode            : node parameter
        """

        return cls(nodes.NodeQuadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).curve)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ Method QuadraticBezier

        Arguments
        ---------
            resolution      : Integer
            start           : Vector
            middle          : Vector
            end             : Vector
        """

        return cls(nodes.NodeQuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ Method Star

        Arguments
        ---------
            points          : Points
            inner_radius    : Float
            outer_radius    : Float
            twist           : Float
        """

        node = nodes.NodeStar(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)
        return Sockets(curve=Curve(node.curve), outer_points=Boolean(node.outer_points))

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ Method Spiral

        Arguments
        ---------
            resolution      : Integer
            rotations       : Float
            start_radius    : Float
            end_radius      : Float
            height          : Float
            reverse         : Boolean
        """

        return cls(nodes.NodeSpiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)

    @classmethod
    def ArcFromRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """ Method ArcFromRadius

        Arguments
        ---------
            resolution      : Integer
            radius          : Float
            start_angle     : Float
            sweep_angle     : Float
            connect_center  : Boolean
            invert_arc      : Boolean
            mode            : node parameter set to 'RADIUS'
        """

        return cls(nodes.NodeArc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').curve)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def ArcFromPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """ Method ArcFromPoints

        Arguments
        ---------
            resolution      : Integer
            start           : Vector
            middle          : Vector
            end             : Vector
            offset_angle    : Float
            connect_center  : Boolean
            invert_arc      : Boolean
            mode            : node parameter set to 'POINTS'
        """

        node = nodes.NodeArc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')
        return Sockets(curve=Curve(node.curve), center=Vector(node.center), normal=Vector(node.normal), radius=Float(node.radius))


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputID

    @property
    def spline_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='SPLINE').outputs[0])

    # ---------- Attribute GeometryNodeInputIndex

    @property
    def spline_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='SPLINE').outputs[0])

    # ---------- Attribute GeometryNodeCurveEndpointSelection

    def capture_endpoint_selection(self, start_size=None, end_size=None, domain='CURVE'):
        return Boolean(nodes.NodeEndpointSelection(start_size=start_size, end_size=end_size, owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    def endpoint_selection(self, start_size=None, end_size=None):
        return Boolean(nodes.NodeEndpointSelection(start_size=start_size, end_size=end_size, owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeCurveHandleTypeSelection

    def capture_handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, domain='CURVE'):
        return Boolean(nodes.NodeHandleTypeSelection(handle_type=handle_type, mode=mode, owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        return Boolean(nodes.NodeHandleTypeSelection(handle_type=handle_type, mode=mode, owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputCurveTilt

    def capture_tilt(self, domain='CURVE'):
        return Float(nodes.NodeCurveTilt(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def tilt(self):
        return Float(nodes.NodeCurveTilt(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputRadius

    def capture_radius(self, domain='CURVE'):
        return Float(nodes.NodeRadius(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def radius(self):
        return Float(nodes.NodeRadius(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    # ---------- Attribute GeometryNodeInputCurveHandlePositions

    def capture_handle_positions_left(self, relative=None, domain='CURVE'):
        return Vector(nodes.NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[0])

    def handle_positions_left(self, relative=None):
        return Vector(nodes.NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[0])

    def capture_handle_positions_right(self, relative=None, domain='CURVE'):
        return Vector(nodes.NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[1])

    def handle_positions_right(self, relative=None):
        return Vector(nodes.NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='CURVE').outputs[1])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ Method to_mesh

        Arguments
        ---------
            curve           : Curve
            profile_curve   : Geometry
            fill_caps       : Boolean
        """

        return Mesh(nodes.NodeCurvetoMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).mesh)

    def to_points(self, count=None, length=None, mode='COUNT'):
        """ Method to_points

        Arguments
        ---------
            curve           : Curve
            count           : Integer
            length          : Float
            mode            : node parameter
        """

        node = nodes.NodeCurvetoPoints(curve=self, count=count, length=length, mode=mode)
        return Sockets(points=Points(node.points), tangent=Vector(node.tangent), normal=Vector(node.normal), rotation=Vector(node.rotation))

    def sample(self, factor=None, length=None, mode='LENGTH'):
        """ Method sample

        Arguments
        ---------
            curve           : Curve
            factor          : Float
            length          : Float
            mode            : node parameter
        """

        node = nodes.NodeSampleCurve(curve=self, factor=factor, length=length, mode=mode)
        return Sockets(position=Vector(node.position), tangent=Vector(node.tangent), normal=Vector(node.normal))

    def length(self):
        """ Method length

        Arguments
        ---------
            curve           : Curve
        """

        return Float(nodes.NodeCurveLength(curve=self).length)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_handles(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ Method set_handles

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
            handle_type     : node parameter
            mode            : node parameter
        """

        return self.stack(nodes.NodeSetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode))

    def set_spline_type(self, selection=None, spline_type='POLY'):
        """ Method set_spline_type

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
            spline_type     : node parameter
        """

        return self.stack(nodes.NodeSetSplineType(curve=self, selection=selection, spline_type=spline_type))

    def fill(self, mode='TRIANGLES'):
        """ Method fill

        Arguments
        ---------
            curve           : Curve
            mode            : node parameter
        """

        return self.stack(nodes.NodeFillCurve(curve=self, mode=mode))

    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """ Method fillet

        Arguments
        ---------
            curve           : Curve
            count           : Integer
            radius          : Float
            limit_radius    : Boolean
            mode            : node parameter
        """

        return self.stack(nodes.NodeFilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode))

    def resample(self, selection=None, count=None, length=None, mode='COUNT'):
        """ Method resample

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
            count           : Integer
            length          : Float
            mode            : node parameter
        """

        return self.stack(nodes.NodeResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode))

    def reverse(self, selection=None):
        """ Method reverse

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
        """

        return self.stack(nodes.NodeReverseCurve(curve=self, selection=selection))

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT'):
        """ Method set_handle_positions

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
            position        : Vector
            offset          : Vector
            mode            : node parameter
        """

        return self.stack(nodes.NodeSetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode))

    def set_radius(self, selection=None, radius=None):
        """ Method set_radius

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
            radius          : Float
        """

        return self.stack(nodes.NodeSetCurveRadius(curve=self, selection=selection, radius=radius))

    def set_tilt(self, selection=None, tilt=None):
        """ Method set_tilt

        Arguments
        ---------
            curve           : Curve
            selection       : Boolean
            tilt            : Float
        """

        return self.stack(nodes.NodeSetCurveTilt(curve=self, selection=selection, tilt=tilt))

    def subdivide(self, cuts=None):
        """ Method subdivide

        Arguments
        ---------
            curve           : Curve
            cuts            : Integer
        """

        return self.stack(nodes.NodeSubdivideCurve(curve=self, cuts=cuts))

    def trim(self, start=None, end=None, mode='FACTOR'):
        """ Method trim

        Arguments
        ---------
            curve           : Curve
            start           : Float
            end             : Float
            mode            : node parameter
        """

        return self.stack(nodes.NodeTrimCurve(curve=self, start=start, end=end, mode=mode))


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
        corner_ID            : Integer on domain CORNER
        edge_ID              : Integer on domain EDGE
        face_ID              : Integer on domain FACE

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
        corner_index         : Integer on domain CORNER
        edge_index           : Integer on domain EDGE
        face_index           : Integer on domain FACE

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
        extrude              : GeometryNodeExtrudeMesh  
        intersect            : GeometryNodeMeshBoolean  (operation = INTERSECT)
        to_curve             : (Curve) GeometryNodeMeshToCurve  
        to_points            : (Points) GeometryNodeMeshToPoints 
        union                : GeometryNodeMeshBoolean  (operation = UNION)

    Stacked methods
    ---------------
        dual                 : node GeometryNodeDualMesh
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
        """ Method Circle

        Arguments
        ---------
            vertices        : Integer
            radius          : Float
            fill_type       : node parameter
        """

        return cls(nodes.NodeMeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """ Method Cone

        Arguments
        ---------
            vertices        : Integer
            side_segments   : Integer
            fill_segments   : Integer
            radius_top      : Float
            radius_bottom   : Float
            depth           : Float
            fill_type       : node parameter
        """

        node = nodes.NodeCone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)
        return Sockets(mesh=Mesh(node.mesh), top=Boolean(node.top), bottom=Boolean(node.bottom), side=Boolean(node.side))

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """ Method Cube

        Arguments
        ---------
            size            : Vector
            vertices_x      : Integer
            vertices_y      : Integer
            vertices_z      : Integer
        """

        return cls(nodes.NodeCube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).mesh)

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """ Method Cylinder

        Arguments
        ---------
            vertices        : Integer
            side_segments   : Integer
            fill_segments   : Integer
            radius          : Float
            depth           : Float
            fill_type       : node parameter
        """

        node = nodes.NodeCylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)
        return Sockets(mesh=Mesh(node.mesh), top=Boolean(node.top), side=Boolean(node.side), bottom=Boolean(node.bottom))

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """ Method Grid

        Arguments
        ---------
            size_x          : Float
            size_y          : Float
            vertices_x      : Integer
            vertices_y      : Integer
        """

        return cls(nodes.NodeGrid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).mesh)

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """ Method IcoSphere

        Arguments
        ---------
            radius          : Float
            subdivisions    : Integer
        """

        return cls(nodes.NodeIcoSphere(radius=radius, subdivisions=subdivisions).mesh)

    @classmethod
    def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """ Method Line

        Arguments
        ---------
            count           : Integer
            resolution      : Float
            start_location  : Vector
            offset          : Vector
            count_mode      : node parameter
            mode            : node parameter
        """

        return cls(nodes.NodeMeshLine(count=count, resolution=resolution, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """ Method UVSphere

        Arguments
        ---------
            segments        : Integer
            rings           : Integer
            radius          : Float
        """

        return cls(nodes.NodeUVSphere(segments=segments, rings=rings, radius=radius).mesh)


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    # ---------- Attribute GeometryNodeInputID

    @property
    def corner_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def edge_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def face_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    # ---------- Attribute GeometryNodeInputIndex

    @property
    def corner_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def edge_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def face_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    # ---------- Attribute GeometryNodeInputMeshEdgeNeighbors

    def capture_edge_neighbors(self, domain='EDGE'):
        return Integer(nodes.NodeEdgeNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def edge_neighbors(self):
        return Integer(nodes.NodeEdgeNeighbors(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    # ---------- Attribute GeometryNodeInputMeshFaceArea

    def capture_face_area(self, domain='FACE'):
        return Float(nodes.NodeFaceArea(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def face_area(self):
        return Float(nodes.NodeFaceArea(owner_socket=self.socket, data_type='VALUE', domain='FACE').outputs[0])

    # ---------- Attribute GeometryNodeInputMeshEdgeAngle

    def capture_edge_angle_unsigned_angle(self, domain='EDGE'):
        return Float(nodes.NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[0])

    @property
    def edge_angle_unsigned_angle(self):
        return Float(nodes.NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain='EDGE').outputs[0])

    def capture_edge_angle_signed_angle(self, domain='EDGE'):
        return Float(nodes.NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain=domain).outputs[1])

    @property
    def edge_angle_signed_angle(self):
        return Float(nodes.NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain='EDGE').outputs[1])

    # ---------- Attribute GeometryNodeInputMeshEdgeVertices

    def capture_edge_vertices_vertex_index_1(self, domain='EDGE'):
        return Integer(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def edge_vertices_vertex_index_1(self):
        return Integer(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    def capture_edge_vertices_vertex_index_2(self, domain='EDGE'):
        return Integer(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def edge_vertices_vertex_index_2(self):
        return Integer(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[1])

    def capture_edge_vertices_position_1(self, domain='EDGE'):
        return Vector(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[2])

    @property
    def edge_vertices_position_1(self):
        return Vector(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[2])

    def capture_edge_vertices_position_2(self, domain='EDGE'):
        return Vector(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain=domain).outputs[3])

    @property
    def edge_vertices_position_2(self):
        return Vector(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='FLOAT_VECTOR', domain='EDGE').outputs[3])

    # ---------- Attribute GeometryNodeInputMeshFaceNeighbors

    def capture_face_neighbors_vertex_count(self, domain='FACE'):
        return Integer(nodes.NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def face_neighbors_vertex_count(self):
        return Integer(nodes.NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    def capture_face_neighbors_face_count(self, domain='FACE'):
        return Integer(nodes.NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def face_neighbors_face_count(self):
        return Integer(nodes.NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[1])

    # ---------- Attribute GeometryNodeInputMeshIsland

    def capture_island_island_index(self, domain='FACE'):
        return Integer(nodes.NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def island_island_index(self):
        return Integer(nodes.NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    def capture_island_island_count(self, domain='FACE'):
        return Integer(nodes.NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def island_island_count(self):
        return Integer(nodes.NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[1])

    # ---------- Attribute GeometryNodeInputMeshVertexNeighbors

    def capture_vertex_neighbors_vertex_count(self, domain='POINT'):
        return Integer(nodes.NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def vertex_neighbors_vertex_count(self):
        return Integer(nodes.NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    def capture_vertex_neighbors_face_count(self, domain='POINT'):
        return Integer(nodes.NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain=domain).outputs[1])

    @property
    def vertex_neighbors_face_count(self):
        return Integer(nodes.NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[1])

    # ---------- Attribute GeometryNodeInputMaterialIndex

    def capture_material_index(self, domain='FACE'):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    # ---------- Attribute GeometryNodeInputShadeSmooth

    def capture_shade_smooth(self, domain='FACE'):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain=domain).outputs[0])

    @property
    def shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='FACE').outputs[0])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def intersect(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """ Method intersect

        Arguments
        ---------
            mesh_2          : Geometry (multi input)
            self_intersection : Boolean
            hole_tolerant   : Boolean
            operation       : node parameter set to 'INTERSECT'
        """

        return Mesh(nodes.NodeMeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').mesh)

    def union(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """ Method union

        Arguments
        ---------
            mesh_2          : Geometry (multi input)
            self_intersection : Boolean
            hole_tolerant   : Boolean
            operation       : node parameter set to 'UNION'
        """

        return Mesh(nodes.NodeMeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').mesh)

    def difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """ Method difference

        Arguments
        ---------
            mesh_1          : Geometry
            mesh_2          : Geometry (multi input)
            self_intersection : Boolean
            hole_tolerant   : Boolean
            operation       : node parameter set to 'DIFFERENCE'
        """

        return Mesh(nodes.NodeMeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE').mesh)

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """ Method extrude

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
            offset          : Vector
            offset_scale    : Float
            individual      : Boolean
            mode            : node parameter
        """

        node = nodes.NodeExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)
        return Sockets(mesh=Mesh(node.mesh), top=Boolean(node.top), side=Boolean(node.side))

    def to_curve(self, selection=None):
        """ Method to_curve

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
        """

        return Curve(nodes.NodeMeshtoCurve(mesh=self, selection=selection).curve)

    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):
        """ Method to_points

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
            position        : Vector
            radius          : Float
            mode            : node parameter
        """

        return Points(nodes.NodeMeshtoPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).points)

    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """ Method distribute_points_on_faces

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
            distance_min    : Float
            density_max     : Float
            density         : Float
            density_factor  : Float
            seed            : Integer
            distribute_method : node parameter
        """

        node = nodes.NodeDistributePointsonFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method)
        return Sockets(points=Points(node.points), normal=Vector(node.normal), rotation=Vector(node.rotation))


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def split_edges(self, selection=None):
        """ Method split_edges

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
        """

        return self.stack(nodes.NodeSplitEdges(mesh=self, selection=selection))

    def subdivide(self, level=None):
        """ Method subdivide

        Arguments
        ---------
            mesh            : Mesh
            level           : Integer
        """

        return self.stack(nodes.NodeSubdivideMesh(mesh=self, level=level))

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """ Method subdivision_surface

        Arguments
        ---------
            mesh            : Mesh
            level           : Integer
            crease          : Float
            boundary_smooth : node parameter
            uv_smooth       : node parameter
        """

        return self.stack(nodes.NodeSubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ Method triangulate

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
            minimum_vertices : Integer
            ngon_method     : node parameter
            quad_method     : node parameter
        """

        return self.stack(nodes.NodeTriangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))

    def dual(self, keep_boundaries=None):
        """ Method dual

        Arguments
        ---------
            mesh            : Mesh
            keep_boundaries : Boolean
        """

        return self.stack(nodes.NodeDualMesh(mesh=self, keep_boundaries=keep_boundaries))

    def flip_faces(self, selection=None):
        """ Method flip_faces

        Arguments
        ---------
            mesh            : Mesh
            selection       : Boolean
        """

        return self.stack(nodes.NodeFlipFaces(mesh=self, selection=selection))


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
        """ Method instance_on_points

        Arguments
        ---------
            points          : Points
            selection       : Boolean
            instance        : Geometry
            pick_instance   : Boolean
            instance_index  : Integer
            rotation        : Vector
            scale           : Vector
        """

        return Instances(nodes.NodeInstanceonPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)

    def to_vertices(self, selection=None):
        """ Method to_vertices

        Arguments
        ---------
            points          : Points
            selection       : Boolean
        """

        return Mesh(nodes.NodePointstoVertices(points=self, selection=selection).mesh)

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ Method to_volume

        Arguments
        ---------
            points          : Points
            density         : Float
            voxel_size      : Float
            voxel_amount    : Float
            radius          : Float
            resolution_mode : node parameter
        """

        return Volume(nodes.NodePointstoVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_radius(self, selection=None, radius=None):
        """ Method set_radius

        Arguments
        ---------
            points          : Points
            selection       : Boolean
            radius          : Float
        """

        return self.stack(nodes.NodeSetPointRadius(points=self, selection=selection, radius=radius))


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
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain=domain).outputs[0])

    @property
    def index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='INSTANCE').outputs[0])


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_points(self, selection=None, position=None, radius=None):
        """ Method to_points

        Arguments
        ---------
            instances       : Instances
            selection       : Boolean
            position        : Vector
            radius          : Float
        """

        return Points(nodes.NodeInstancestoPoints(instances=self, selection=selection, position=position, radius=radius).points)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ Method rotate

        Arguments
        ---------
            instances       : Instances
            selection       : Boolean
            rotation        : Vector
            pivot_point     : Vector
            local_space     : Boolean
        """

        return self.stack(nodes.NodeRotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        """ Method scale

        Arguments
        ---------
            instances       : Instances
            selection       : Boolean
            scale           : Vector
            center          : Vector
            local_space     : Boolean
        """

        return self.stack(nodes.NodeScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        """ Method translate

        Arguments
        ---------
            instances       : Instances
            selection       : Boolean
            translation     : Vector
            local_space     : Boolean
        """

        return self.stack(nodes.NodeTranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))


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

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ Method to_mesh

        Arguments
        ---------
            volume          : Volume
            voxel_size      : Float
            voxel_amount    : Float
            threshold       : Float
            adaptivity      : Float
            resolution_mode : node parameter
        """

        return Mesh(nodes.NodeVolumetoMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh)


# ==============================================================================================================
# Data class Collection

class Collection(bcls.Collection):
    """ Socket data class Collection

    Methods
    -------
        info                 : GeometryNodeCollectionInfo
        switch               : GeometryNodeSwitch       (input_type = COLLECTION)

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'COLLECTION'
        """

        return Collection(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='COLLECTION').output)

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ Method info

        Arguments
        ---------
            collection      : Collection
            separate_children : Boolean
            reset_children  : Boolean
            transform_space : node parameter
        """

        return Geometry(nodes.NodeCollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry)


# ==============================================================================================================
# Data class Object

class Object(bcls.Object):
    """ Socket data class Object

    Node properties
    ---------------
        info                 : node GeometryNodeObjectInfo
        location             : info.location
        rotation             : info.rotation
        scale                : info.scale
        geometry             : info.geometry


    Methods
    -------
        switch               : GeometryNodeSwitch       (input_type = OBJECT)

    """


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    # ---------- Node ObjectInfo

    @property
    def info(self):
        if not hasattr(self.top, 'info_'):
            self.top.info_ = nodes.NodeObjectInfo(self)
            self.top.info_.prop_of = self.node
        return self.top.info_

    @property
    def location(self):
        if not hasattr(self.top, 'location_'):
            self.top.location_ = Vector(self.top.info.location)
        return self.top.location_

    @location.setter
    def location(self, value):
        _ = self.info
        self.top.location_ = value

    @property
    def rotation(self):
        if not hasattr(self.top, 'rotation_'):
            self.top.rotation_ = Vector(self.top.info.rotation)
        return self.top.rotation_

    @rotation.setter
    def rotation(self, value):
        _ = self.info
        self.top.rotation_ = value

    @property
    def scale(self):
        if not hasattr(self.top, 'scale_'):
            self.top.scale_ = Vector(self.top.info.scale)
        return self.top.scale_

    @scale.setter
    def scale(self, value):
        _ = self.info
        self.top.scale_ = value

    @property
    def geometry(self):
        if not hasattr(self.top, 'geometry_'):
            self.top.geometry_ = Geometry(self.top.info.geometry)
        return self.top.geometry_

    @geometry.setter
    def geometry(self, value):
        _ = self.info
        self.top.geometry_ = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'OBJECT'
        """

        return Object(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='OBJECT').output)


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
        """ Method Brick

        Arguments
        ---------
            vector          : Vector
            color1          : Color
            color2          : Color
            mortar          : Color
            scale           : Float
            mortar_size     : Float
            mortar_smooth   : Float
            bias            : Float
            brick_width     : Float
            row_height      : Float
            offset          : node parameter
            offset_frequency : node parameter
            squash          : node parameter
            squash_frequency : node parameter
        """

        node = nodes.NodeBrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Checker(cls, vector=None, color1=None, color2=None, scale=None):
        """ Method Checker

        Arguments
        ---------
            vector          : Vector
            color1          : Color
            color2          : Color
            scale           : Float
        """

        node = nodes.NodeCheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Gradient(cls, vector=None, gradient_type='LINEAR'):
        """ Method Gradient

        Arguments
        ---------
            vector          : Vector
            gradient_type   : node parameter
        """

        node = nodes.NodeGradientTexture(vector=vector, gradient_type=gradient_type)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Magic(cls, vector=None, scale=None, distortion=None, turbulence_depth=2):
        """ Method Magic

        Arguments
        ---------
            vector          : Vector
            scale           : Float
            distortion      : Float
            turbulence_depth : node parameter
        """

        node = nodes.NodeMagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def Musgrave(cls, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        """ Method Musgrave

        Arguments
        ---------
            vector          : Vector
            w               : Float
            scale           : Float
            detail          : Float
            dimension       : Float
            lacunarity      : Float
            offset          : Float
            gain            : Float
            musgrave_dimensions : node parameter
            musgrave_type   : node parameter
        """

        return cls(nodes.NodeMusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).fac)

    @classmethod
    def Noise(cls, vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        """ Method Noise

        Arguments
        ---------
            vector          : Vector
            w               : Float
            scale           : Float
            detail          : Float
            roughness       : Float
            distortion      : Float
            noise_dimensions : node parameter
        """

        node = nodes.NodeNoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)
        return Sockets(fac=Float(node.fac), color=Color(node.color))

    @classmethod
    def Voronoi(cls, vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """ Method Voronoi

        Arguments
        ---------
            vector          : Vector
            w               : Float
            scale           : Float
            smoothness      : Float
            exponent        : Float
            randomness      : Float
            distance        : node parameter
            feature         : node parameter
            voronoi_dimensions : node parameter
        """

        node = nodes.NodeVoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return Sockets(distance=Float(node.distance), color=Color(node.color), position=Vector(node.position))

    @classmethod
    def Wave(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """ Method Wave

        Arguments
        ---------
            vector          : Vector
            scale           : Float
            distortion      : Float
            detail          : Float
            detail_scale    : Float
            detail_roughness : Float
            phase_offset    : Float
            bands_direction : node parameter
            rings_direction : node parameter
            wave_profile    : node parameter
            wave_type       : node parameter
        """

        node = nodes.NodeWaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return Sockets(color=Color(node.color), fac=Float(node.fac))

    @classmethod
    def WhiteNoise(cls, vector=None, w=None, noise_dimensions='3D'):
        """ Method WhiteNoise

        Arguments
        ---------
            vector          : Vector
            w               : Float
            noise_dimensions : node parameter
        """

        node = nodes.NodeWhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)
        return Sockets(value=Float(node.value), color=Color(node.color))

    @classmethod
    def Image(cls, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """ Method Image

        Arguments
        ---------
            image           : Image
            vector          : Vector
            frame           : Integer
            extension       : node parameter
            interpolation   : node parameter
        """

        node = nodes.NodeImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        return Sockets(color=Color(node.color), alpha=Float(node.alpha))


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'TEXTURE'
        """

        return Texture(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='TEXTURE').output)


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
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'MATERIAL'
        """

        return Material(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='MATERIAL').output)

    def selection(self):
        """ Method selection

        Arguments
        ---------
            material        : Material
        """

        return Boolean(nodes.NodeMaterialSelection(material=self).selection)


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
        """ Method switch

        Arguments
        ---------
            false           : Float
            switch          : Boolean
            true            : Float
            input_type      : node parameter set to 'IMAGE'
        """

        return Image(nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='IMAGE').output)

