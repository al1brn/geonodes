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
# Data class Color

class Color(bcls.Color):
    """ Socket data class Color

    Constructors
    ------------
        Combine              : Color

    Properties
    ----------
        separate             : Sockets [r (Float), g (Float), b (Float)]

    Node properties
    ---------------
        b                    : Float
        g                    : Float
        r                    : Float

    Methods
    -------
        field_at_index       : Color
        mix                  : Color
        switch               : Color

    Stacked methods
    ---------------
        curves               : Color

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None):
        """ Constructor Combine using node NodeCombineRGB

        Arguments
        ---------
            r               : Float
            g               : Float
            b               : Float

        Returns
        -------
            Color
        """

        return nodes.NodeCombineRGB(r=r, g=g, b=b).output


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ Property separate using node NodeSeparateRGB

        Arguments
        ---------
            image           : Color: self socket

        Returns
        -------
            Sockets [r (Float), g (Float), b (Float)]
        """

        if not hasattr(self.top, 'separate_'):
            self.top.separate_ = nodes.NodeSeparateRGB(image=self).output
        return self.top.separate_


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    @property
    def r(self):
        """ Node property r using node NodeSeparateRGB on output socket r

        Arguments
        ---------
            image           : Color: self socket

        Returns
        -------
            Float
        """

        return self.separate.r

    @property
    def g(self):
        """ Node property g using node NodeSeparateRGB on output socket g

        Arguments
        ---------
            image           : Color: self socket

        Returns
        -------
            Float
        """

        return self.separate.g

    @property
    def b(self):
        """ Node property b using node NodeSeparateRGB on output socket b

        Arguments
        ---------
            image           : Color: self socket

        Returns
        -------
            Float
        """

        return self.separate.b


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def mix(self, fac=None, color2=None, blend_type='MIX', use_alpha=False, use_clamp=False):
        """ Method mix using node NodeMix

        Arguments
        ---------
            color1          : Color: self socket
            fac             : Float
            color2          : Color

            blend_type      : str
            use_alpha       : bool
            use_clamp       : bool

        Returns
        -------
            Color
        """

        return nodes.NodeMix(color1=self, fac=fac, color2=color2, blend_type=blend_type, use_alpha=use_alpha, use_clamp=use_clamp).output

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index using node NodeFieldatIndex

        Arguments
        ---------
            value           : Float: self socket
            index           : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_COLOR'

        Returns
        -------
            Color
        """

        return nodes.NodeFieldatIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain).output

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'RGBA'

        Returns
        -------
            Color
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='RGBA').output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """ Stacked method curves using node NodeRGBCurves

        Arguments
        ---------
            color           : Color: self socket
            fac             : Float

        Returns
        -------
            Color
        """

        return self.stack(nodes.NodeRGBCurves(color=self, fac=fac))



