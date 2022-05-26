import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Integer

class Integer(dsock.Integer):
    """ Data socket Integer

    Constructors
    ------------
        Random               : value (Integer)
    Methods
    -------
        abs                  : value (Float)
        accumulate_field     : Sockets [leading (Integer), trailing (Integer), total (Integer)]
        add                  : value (Float)
        arccos               : value (Float)
        arcsin               : value (Float)
        arctan               : value (Float)
        arctan2              : value (Float)
        ceil                 : value (Float)
        compare              : value (Float)
        cos                  : value (Float)
        cosh                 : value (Float)
        degrees              : value (Float)
        divide               : value (Float)
        exp                  : value (Float)
        field_at_index       : value (Integer)
        floor                : value (Float)
        fract                : value (Float)
        greater_than         : value (Float)
        inverse_sqrt         : value (Float)
        less_than            : value (Float)
        log                  : value (Float)
        max                  : value (Float)
        min                  : value (Float)
        modulo               : value (Float)
        multiply             : value (Float)
        multiply_add         : value (Float)
        pingpong             : value (Float)
        pow                  : value (Float)
        radians              : value (Float)
        round                : value (Float)
        sign                 : value (Float)
        sin                  : value (Float)
        sinh                 : value (Float)
        smooth_max           : value (Float)
        smooth_min           : value (Float)
        snap                 : value (Float)
        sqrt                 : value (Float)
        subtract             : value (Float)
        switch               : output (Integer)
        tan                  : value (Float)
        tanh                 : value (Float)
        trunc                : value (Float)
        wrap                 : value (Float)
    """

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, probability=None, ID=None, seed=None):
        """Call node NodeRandomValue (FunctionNodeRandomValue)

        Sockets arguments
        -----------------
            min            : Integer
            max            : Integer
            probability    : Float
            ID             : Integer
            seed           : Integer

        Fixed parameters
        ----------------
            data_type      : 'INT'

        Returns
        -------
            Integer
        """

        return cls(nodes.NodeRandomValue(min=min, max=max, probability=probability, ID=ID, seed=seed, data_type='INT').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ADD'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ADD').value

    def subtract(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SUBTRACT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SUBTRACT').value

    def multiply(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MULTIPLY').value

    def divide(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'DIVIDE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='DIVIDE').value

    def multiply_add(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

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

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

    def pow(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'POWER'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='POWER').value

    def log(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'LOGARITHM'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='LOGARITHM').value

    def sqrt(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SQRT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SQRT').value

    def inverse_sqrt(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'INVERSE_SQRT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='INVERSE_SQRT').value

    def abs(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ABSOLUTE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ABSOLUTE').value

    def exp(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'EXPONENT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='EXPONENT').value

    def min(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'MINIMUM'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MINIMUM').value

    def max(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'MAXIMUM'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MAXIMUM').value

    def less_than(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'LESS_THAN'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='LESS_THAN').value

    def greater_than(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'GREATER_THAN'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='GREATER_THAN').value

    def sign(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SIGN'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SIGN').value

    def compare(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

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

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='COMPARE').value

    def smooth_min(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

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

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN').value

    def smooth_max(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

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

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX').value

    def round(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ROUND'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ROUND').value

    def floor(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'FLOOR'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='FLOOR').value

    def ceil(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'CEIL'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='CEIL').value

    def trunc(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'TRUNC'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='TRUNC').value

    def fract(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'FRACT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='FRACT').value

    def modulo(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'MODULO'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='MODULO').value

    def wrap(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

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

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='WRAP').value

    def snap(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SNAP'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SNAP').value

    def pingpong(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'PINGPONG'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='PINGPONG').value

    def sin(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SINE').value

    def cos(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'COSINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='COSINE').value

    def tan(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'TANGENT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='TANGENT').value

    def arcsin(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ARCSINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ARCSINE').value

    def arccos(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ARCCOSINE'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ARCCOSINE').value

    def arctan(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ARCTANGENT'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ARCTANGENT').value

    def arctan2(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'ARCTAN2'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='ARCTAN2').value

    def sinh(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'SINH'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='SINH').value

    def cosh(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'COSH'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='COSH').value

    def tanh(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'TANH'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='TANH').value

    def radians(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'RADIANS'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='RADIANS').value

    def degrees(self, value1=None, value2=None):
        """Call node NodeMath (ShaderNodeMath)

        Sockets arguments
        -----------------
            value0         : Float (self)
            value1         : Float
            value2         : Float

        Fixed parameters
        ----------------
            operation      : 'DEGREES'

        Returns
        -------
            Float
        """

        return nodes.NodeMath(value0=self, value1=value1, value2=value2, operation='DEGREES').value

    def switch(self, switch0=None, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Integer (self)
            switch0        : Boolean
            switch1        : Boolean
            true           : Integer

        Fixed parameters
        ----------------
            input_type     : 'INT'

        Returns
        -------
            Integer
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, switch1=switch1, true=true, input_type='INT').output

    def accumulate_field(self, group_index=None, domain='POINT'):
        """Call node NodeAccumulateField (GeometryNodeAccumulateField)

        Sockets arguments
        -----------------
            value          : Integer (self)
            group_index    : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'INT'

        Returns
        -------
            Sockets [leading (Integer), trailing (Integer), total (Integer)]
        """

        return nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """Call node NodeFieldAtIndex (GeometryNodeFieldAtIndex)

        Sockets arguments
        -----------------
            value          : Integer (self)
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'INT'

        Returns
        -------
            Integer
        """

        return nodes.NodeFieldAtIndex(value=self, index=index, data_type='INT', domain=domain).value


