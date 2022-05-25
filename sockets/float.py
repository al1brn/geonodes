import geonodes as gn
from geonodes.core import socket as bcls
from geonodes.nodes import nodes
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
# Data class Float

class Float(bcls.Float):
    """ Socket data class Float

    Constructors
    ------------
        Random               : Float

    Methods
    -------
        abs                  : Float
        accumulate_field     : Sockets [leading (Float), trailing (Float), total (Float)]
        add                  : Float
        arccos               : Float
        arcsin               : Float
        arctan               : Float
        arctan2              : Float
        ceil                 : Integer
        color_ramp           : Sockets [color (Color), alpha (Float)]
        compare              : Boolean
        cos                  : Float
        cosh                 : Float
        degrees              : Float
        divide               : Float
        exp                  : Float
        field_at_index       : Float
        floor                : Integer
        fract                : Float
        greater_than         : Boolean
        inverse_sqrt         : Float
        less_than            : Boolean
        log                  : Float
        max                  : Float
        min                  : Float
        modulo               : Float
        multiply             : Float
        multiply_add         : Float
        pingpong             : Float
        pow                  : Float
        radians              : Float
        round                : Integer
        sign                 : Integer
        sin                  : Float
        sinh                 : Float
        smooth_max           : Float
        smooth_min           : Float
        snap                 : Float
        sqrt                 : Float
        subtract             : Float
        switch               : Float
        tan                  : Float
        tanh                 : Float
        to_integer           : Integer
        to_string            : String
        trunc                : Integer
        wrap                 : Float

    Stacked methods
    ---------------
        clamp                : Float
        curve                : Float
        map_range            : Float

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Constructor Random using node NodeRandomValue

        Arguments
        ---------
            min             : Vector
            max             : Vector
            ID              : Integer
            seed            : Integer

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').output


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, value1=None, use_clamp=False):
        """ Method add using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ADD'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='ADD', use_clamp=use_clamp).output

    def subtract(self, value1=None, use_clamp=False):
        """ Method subtract using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SUBTRACT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='SUBTRACT', use_clamp=use_clamp).output

    def multiply(self, value1=None, use_clamp=False):
        """ Method multiply using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MULTIPLY'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='MULTIPLY', use_clamp=use_clamp).output

    def divide(self, value1=None, use_clamp=False):
        """ Method divide using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'DIVIDE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='DIVIDE', use_clamp=use_clamp).output

    def multiply_add(self, value1=None, value2=None, use_clamp=False):
        """ Method multiply_add using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float
            value2          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MULTIPLY_ADD'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', use_clamp=use_clamp).output

    def pow(self, value1=None, use_clamp=False):
        """ Method pow using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'POWER'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='POWER', use_clamp=use_clamp).output

    def log(self, value1=None, use_clamp=False):
        """ Method log using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'LOGARITHM'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='LOGARITHM', use_clamp=use_clamp).output

    def sqrt(self, use_clamp=False):
        """ Method sqrt using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SQRT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='SQRT', use_clamp=use_clamp).output

    def inverse_sqrt(self, use_clamp=False):
        """ Method inverse_sqrt using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'INVERSE_SQRT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='INVERSE_SQRT', use_clamp=use_clamp).output

    def abs(self, use_clamp=False):
        """ Method abs using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ABSOLUTE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='ABSOLUTE', use_clamp=use_clamp).output

    def exp(self, use_clamp=False):
        """ Method exp using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'EXPONENT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='EXPONENT', use_clamp=use_clamp).output

    def min(self, value1=None, use_clamp=False):
        """ Method min using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MINIMUM'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='MINIMUM', use_clamp=use_clamp).output

    def max(self, value1=None, use_clamp=False):
        """ Method max using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MAXIMUM'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='MAXIMUM', use_clamp=use_clamp).output

    def less_than(self, value1=None, use_clamp=False):
        """ Method less_than using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'LESS_THAN'

        Returns
        -------
            Boolean
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='LESS_THAN', use_clamp=use_clamp).output

    def greater_than(self, value1=None, use_clamp=False):
        """ Method greater_than using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'GREATER_THAN'

        Returns
        -------
            Boolean
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='GREATER_THAN', use_clamp=use_clamp).output

    def sign(self, use_clamp=False):
        """ Method sign using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SIGN'

        Returns
        -------
            Integer
        """

        return nodes.NodeMath(value0=self, operation='SIGN', use_clamp=use_clamp).output

    def compare(self, value1=None, value2=None, use_clamp=False):
        """ Method compare using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float
            value2          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'COMPARE'

        Returns
        -------
            Boolean
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='COMPARE', use_clamp=use_clamp).output

    def smooth_min(self, value1=None, value2=None, use_clamp=False):
        """ Method smooth_min using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float
            value2          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SMOOTH_MIN'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', use_clamp=use_clamp).output

    def smooth_max(self, value1=None, value2=None, use_clamp=False):
        """ Method smooth_max using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float
            value2          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SMOOTH_MAX'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', use_clamp=use_clamp).output

    def round(self, use_clamp=False):
        """ Method round using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ROUND'

        Returns
        -------
            Integer
        """

        return nodes.NodeMath(value0=self, operation='ROUND', use_clamp=use_clamp).output

    def floor(self, use_clamp=False):
        """ Method floor using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'FLOOR'

        Returns
        -------
            Integer
        """

        return nodes.NodeMath(value0=self, operation='FLOOR', use_clamp=use_clamp).output

    def ceil(self, use_clamp=False):
        """ Method ceil using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'CEIL'

        Returns
        -------
            Integer
        """

        return nodes.NodeMath(value0=self, operation='CEIL', use_clamp=use_clamp).output

    def trunc(self, use_clamp=False):
        """ Method trunc using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'TRUNC'

        Returns
        -------
            Integer
        """

        return nodes.NodeMath(value0=self, operation='TRUNC', use_clamp=use_clamp).output

    def fract(self, use_clamp=False):
        """ Method fract using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'FRACT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='FRACT', use_clamp=use_clamp).output

    def modulo(self, value1=None, use_clamp=False):
        """ Method modulo using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MODULO'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='MODULO', use_clamp=use_clamp).output

    def wrap(self, value1=None, value2=None, use_clamp=False):
        """ Method wrap using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float
            value2          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'WRAP'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='WRAP', use_clamp=use_clamp).output

    def snap(self, value1=None, use_clamp=False):
        """ Method snap using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SNAP'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='SNAP', use_clamp=use_clamp).output

    def pingpong(self, value1=None, use_clamp=False):
        """ Method pingpong using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'PINGPONG'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='PINGPONG', use_clamp=use_clamp).output

    def sin(self, use_clamp=False):
        """ Method sin using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='SINE', use_clamp=use_clamp).output

    def cos(self, use_clamp=False):
        """ Method cos using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'COSINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='COSINE', use_clamp=use_clamp).output

    def tan(self, use_clamp=False):
        """ Method tan using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'TANGENT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='TANGENT', use_clamp=use_clamp).output

    def arcsin(self, use_clamp=False):
        """ Method arcsin using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ARCSINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='ARCSINE', use_clamp=use_clamp).output

    def arccos(self, use_clamp=False):
        """ Method arccos using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ARCCOSINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='ARCCOSINE', use_clamp=use_clamp).output

    def arctan(self, use_clamp=False):
        """ Method arctan using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ARCTANGENT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='ARCTANGENT', use_clamp=use_clamp).output

    def arctan2(self, value1=None, use_clamp=False):
        """ Method arctan2 using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket
            value1          : Float

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ARCTAN2'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, operation='ARCTAN2', use_clamp=use_clamp).output

    def sinh(self, use_clamp=False):
        """ Method sinh using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SINH'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='SINH', use_clamp=use_clamp).output

    def cosh(self, use_clamp=False):
        """ Method cosh using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'COSH'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='COSH', use_clamp=use_clamp).output

    def tanh(self, use_clamp=False):
        """ Method tanh using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'TANH'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='TANH', use_clamp=use_clamp).output

    def radians(self, use_clamp=False):
        """ Method radians using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'RADIANS'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='RADIANS', use_clamp=use_clamp).output

    def degrees(self, use_clamp=False):
        """ Method degrees using node NodeMath

        Arguments
        ---------
            value0          : Float: self socket

            use_clamp       : bool

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'DEGREES'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, operation='DEGREES', use_clamp=use_clamp).output

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='FLOAT').output

    def to_integer(self, rounding_mode='ROUND'):
        """ Method to_integer using node NodeFloattoInteger

        Arguments
        ---------
            float           : Float: self socket

            rounding_mode   : str

        Returns
        -------
            Integer
        """

        return nodes.NodeFloattoInteger(float=self, rounding_mode=rounding_mode).output

    def to_string(self, decimals=None):
        """ Method to_string using node NodeValuetoString

        Arguments
        ---------
            value           : Float: self socket
            decimals        : Integer

        Returns
        -------
            String
        """

        return nodes.NodeValuetoString(value=self, decimals=decimals).output

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ Method accumulate_field using node NodeAccumulateField

        Arguments
        ---------
            value           : Vector: self socket
            group_index     : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT'

        Returns
        -------
            Sockets [leading (Float), trailing (Float), total (Float)]
        """

        return nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain).output

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index using node NodeFieldatIndex

        Arguments
        ---------
            value           : Float: self socket
            index           : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT'

        Returns
        -------
            Float
        """

        return nodes.NodeFieldatIndex(value=self, index=index, data_type='FLOAT', domain=domain).output

    def color_ramp(self):
        """ Method color_ramp using node NodeColorRamp

        Arguments
        ---------
            fac             : Float: self socket

        Returns
        -------
            Sockets [color (Color), alpha (Float)]
        """

        return nodes.NodeColorRamp(fac=self).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curve(self, value=None):
        """ Stacked method curve using node NodeFloatCurve

        Arguments
        ---------
            factor          : Float: self socket
            value           : Float

        Returns
        -------
            Float
        """

        return self.stack(nodes.NodeFloatCurve(factor=self, value=value))

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        """ Stacked method clamp using node NodeClamp

        Arguments
        ---------
            value           : Float: self socket
            min             : Float
            max             : Float

            clamp_type      : str

        Returns
        -------
            Float
        """

        return self.stack(nodes.NodeClamp(value=self, min=min, max=max, clamp_type=clamp_type))

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """ Stacked method map_range using node NodeMapRange

        Arguments
        ---------
            value           : Float: self socket
            from_min        : Float
            from_max        : Float
            to_min          : Float
            to_max          : Float
            steps           : Float

            clamp           : bool
            interpolation_type : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT'

        Returns
        -------
            Float
        """

        return self.stack(nodes.NodeMapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type))



