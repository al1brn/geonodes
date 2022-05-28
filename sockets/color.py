import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Color

class Color(dsock.Color):
    """ Data socket Color

    Constructors
    ------------
        Combine                   : image        (Color)

    Properties
    ----------
        separate                  : Sockets      [r (Float), g (Float), b (Float)]

    Methods
    -------
        add                       : color        (Color)
        burn                      : color        (Color)
        darken                    : color        (Color)
        difference                : color        (Color)
        divide                    : color        (Color)
        dodge                     : color        (Color)
        field_at_index            : value        (Color)
        hue                       : color        (Color)
        lighten                   : color        (Color)
        linear_light              : color        (Color)
        mix                       : color        (Color)
        mix                       : color        (Color)
        mix_color                 : color        (Color)
        multiply                  : color        (Color)
        overlay                   : color        (Color)
        saturation                : color        (Color)
        screen                    : color        (Color)
        soft_light                : color        (Color)
        subtract                  : color        (Color)
        switch                    : output       (Color)
        value                     : color        (Color)

    Stacked methods
    ---------------
        curves                    : Color
    """

    def reset_properties(self):
        self.separate_ = None

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
            self.separate_ = nodes.NodeSeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
        return self.separate_


    @property
    def r(self):
        return self.separate.r

    @r.setter
    def r(self, value):
        self.separate.r = value

    @property
    def g(self):
        return self.separate.g

    @g.setter
    def g(self, value):
        self.separate.g = value

    @property
    def b(self):
        return self.separate.b

    @b.setter
    def b(self, value):
        self.separate.b = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def mix(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'MIX'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

    def darken(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DARKEN'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

    def multiply(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'MULTIPLY'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

    def burn(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'BURN'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

    def lighten(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'LIGHTEN'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

    def screen(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SCREEN'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

    def dodge(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DODGE'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

    def add(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'ADD'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

    def overlay(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'OVERLAY'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

    def soft_light(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SOFT_LIGHT'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

    def linear_light(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'LINEAR_LIGHT'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

    def difference(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DIFFERENCE'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

    def subtract(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SUBTRACT'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

    def divide(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'DIVIDE'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

    def hue(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'HUE'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

    def saturation(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'SATURATION'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

    def mix_color(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'COLOR'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

    def value(self, color2=None, fac=None, use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            use_alpha      : False

        Fixed parameters
        ----------------
            blend_type     : 'VALUE'

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color

    def mix(self, color2=None, fac=None, blend_type='MIX', use_alpha=False):
        """Call node NodeMix (ShaderNodeMixRGB)

        Sockets arguments
        -----------------
            color1         : Color (self)
            color2         : Color
            fac            : Float

        Parameters arguments
        --------------------
            blend_type     : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
            use_alpha      : False

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha).color

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

    def switch(self, switch0=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Color (self)
            switch0        : Boolean
            true           : Color

        Fixed parameters
        ----------------
            input_type     : 'RGBA'

        Returns
        -------
            Color
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, true=true, input_type='RGBA').output


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


