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
# Data class Texture

class Texture(bcls.Texture):
    """ Socket data class Texture

    Static methods
    --------------
        Brick                : Sockets [color (Color), fac (Float)]
        Checker              : Sockets [color (Color), fac (Float)]
        Gradient             : Sockets [color (Color), fac (Float)]
        Image                : Sockets [color (Color), alpha (Float)]
        Magic                : Sockets [color (Color), fac (Float)]
        Musgrave             : Float
        Noise                : Sockets [fac (Float), color (Color)]
        Voronoi              : Sockets [distance (Float), color (Color), position (Vector)]
        Wave                 : Sockets [color (Color), fac (Float)]
        WhiteNoise           : Sockets [value (Float), color (Color)]

    Methods
    -------
        switch               : Texture

    """


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """ Static method Brick using node NodeBrickTexture

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

            offset          : float
            offset_frequency : int
            squash          : float
            squash_frequency : int

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.NodeBrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency).output

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None):
        """ Static method Checker using node NodeCheckerTexture

        Arguments
        ---------
            vector          : Vector
            color1          : Color
            color2          : Color
            scale           : Float

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.NodeCheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale).output

    @staticmethod
    def Gradient(vector=None, gradient_type='LINEAR'):
        """ Static method Gradient using node NodeGradientTexture

        Arguments
        ---------
            vector          : Vector

            gradient_type   : str

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.NodeGradientTexture(vector=vector, gradient_type=gradient_type).output

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None, turbulence_depth=2):
        """ Static method Magic using node NodeMagicTexture

        Arguments
        ---------
            vector          : Vector
            scale           : Float
            distortion      : Float

            turbulence_depth : int

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.NodeMagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth).output

    @staticmethod
    def Musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        """ Static method Musgrave using node NodeMusgraveTexture

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

            musgrave_dimensions : str
            musgrave_type   : str

        Returns
        -------
            Float
        """

        return nodes.NodeMusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).output

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        """ Static method Noise using node NodeNoiseTexture

        Arguments
        ---------
            vector          : Vector
            w               : Float
            scale           : Float
            detail          : Float
            roughness       : Float
            distortion      : Float

            noise_dimensions : str

        Returns
        -------
            Sockets [fac (Float), color (Color)]
        """

        return nodes.NodeNoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions).output

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """ Static method Voronoi using node NodeVoronoiTexture

        Arguments
        ---------
            vector          : Vector
            w               : Float
            scale           : Float
            smoothness      : Float
            exponent        : Float
            randomness      : Float

            distance        : str
            feature         : str
            voronoi_dimensions : str

        Returns
        -------
            Sockets [distance (Float), color (Color), position (Vector)]
        """

        return nodes.NodeVoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions).output

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """ Static method Wave using node NodeWaveTexture

        Arguments
        ---------
            vector          : Vector
            scale           : Float
            distortion      : Float
            detail          : Float
            detail_scale    : Float
            detail_roughness : Float
            phase_offset    : Float

            bands_direction : str
            rings_direction : str
            wave_profile    : str
            wave_type       : str

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.NodeWaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type).output

    @staticmethod
    def WhiteNoise(vector=None, w=None, noise_dimensions='3D'):
        """ Static method WhiteNoise using node NodeWhiteNoiseTexture

        Arguments
        ---------
            vector          : Vector
            w               : Float

            noise_dimensions : str

        Returns
        -------
            Sockets [value (Float), color (Color)]
        """

        return nodes.NodeWhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions).output

    @staticmethod
    def Image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """ Static method Image using node NodeImageTexture

        Arguments
        ---------
            image           : Image
            vector          : Vector
            frame           : Integer

            extension       : str
            interpolation   : str

        Returns
        -------
            Sockets [color (Color), alpha (Float)]
        """

        return nodes.NodeImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation).output


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'TEXTURE'

        Returns
        -------
            Texture
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='TEXTURE').output



