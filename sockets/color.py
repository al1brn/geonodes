import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Color

class Color(dsock.Color):
    """ Data socket Color

    Constructors
    ------------
        Combine              : image (Color)
    Properties
    ----------
        separate             : Sockets [r (Float), g (Float), b (Float)]
    Methods
    -------
        field_at_index       : value (Color)
        mix                  : color (Color)
        switch               : output (Color)
    Stacked methods
    ---------------
        curves               : Color
    """

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None):
        """Call node NodeCombineRgb (ShaderNodeCombineRGB)

        Sockets arguments
        -----------------
            r              : Float
            g              : Float
            b              : Float
        Returns
        -------
            Color
        """

        return cls(nodes.NodeCombineRgb(r=r, g=g, b=b).image)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """Call node NodeSeparateRgb (ShaderNodeSeparateRGB)

        Sockets arguments
        -----------------
            image          : Color (self)
        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
        """

        if self.separate_ is None:
            self.separate_ = nodes.NodeSeparateRgb(image=self)
        return self.separate_


    @property
    def r(self):
        return self.separate.r

    @property
    def g(self):
        return self.separate.g

    @property
    def b(self):
        return self.separate.b


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def mix(self, fac=None, color2=None, blend_type='MIX', use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            fac            : Float
            color2         : Color

        Parameters arguments
        --------------------
            blend_type     : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
            use_alpha      : False
        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, fac=fac, color2=color2, blend_type=blend_type, use_alpha=use_alpha).color

    def field_at_index(self, index=None, domain='POINT'):
        """Call node NodeFieldAtIndex (GeometryNodeFieldAtIndex)

        Sockets arguments
        -----------------
            value          : Color (self)
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_COLOR'

        Returns
        -------
            Color
        """

        return nodes.NodeFieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain).value

    def switch(self, switch0=None, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Color (self)
            switch0        : Boolean
            switch1        : Boolean
            true           : Color

        Fixed parameters
        ----------------
            input_type     : 'RGBA'

        Returns
        -------
            Color
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, switch1=switch1, true=true, input_type='RGBA').output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """Call node NodeRgbCurves (ShaderNodeRGBCurve)

        Sockets arguments
        -----------------
            color          : Color (self)
            fac            : Float
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeRgbCurves(color=self, fac=fac))


