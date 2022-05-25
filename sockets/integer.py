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
# Data class Integer

class Integer(bcls.Integer):
    """ Socket data class Integer

    Constructors
    ------------
        Random               : Integer

    Methods
    -------
        abs                  : Integer
        accumulate_field     : Sockets [leading (Integer), trailing (Integer), total (Integer)]
        add                  : Integer
        arccos               : Float
        arcsin               : Float
        arctan               : Float
        arctan2              : Float
        ceil                 : Integer
        compare              : Boolean
        cos                  : Float
        cosh                 : Float
        degrees              : Float
        divide               : Float
        exp                  : Float
        field_at_index       : Integer
        floor                : Integer
        fract                : Float
        greater_than         : Boolean
        inverse_sqrt         : Float
        less_than            : Boolean
        log                  : Float
        max                  : Integer
        min                  : Integer
        modulo               : Integer
        multiply             : Integer
        multiply_add         : Integer
        pingpong             : Integer
        pow                  : Integer
        radians              : Float
        round                : Integer
        sign                 : Integer
        sin                  : Float
        sinh                 : Float
        smooth_max           : Integer
        smooth_min           : Integer
        snap                 : Integer
        sqrt                 : Float
        subtract             : Integer
        switch               : Integer
        tan                  : Float
        tanh                 : Float
        trunc                : Integer
        wrap                 : Integer

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
            data_type       : node parameter set to 'INT'

        Returns
        -------
            Integer
        """

        return nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').output


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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            Integer
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
            input_type      : node parameter set to 'INT'

        Returns
        -------
            Integer
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='INT').output

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ Method accumulate_field using node NodeAccumulateField

        Arguments
        ---------
            value           : Vector: self socket
            group_index     : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'INT'

        Returns
        -------
            Sockets [leading (Integer), trailing (Integer), total (Integer)]
        """

        return nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain).output

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index using node NodeFieldatIndex

        Arguments
        ---------
            value           : Float: self socket
            index           : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'INT'

        Returns
        -------
            Integer
        """

        return nodes.NodeFieldatIndex(value=self, index=index, data_type='INT', domain=domain).output



