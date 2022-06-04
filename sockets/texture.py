import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Texture

class Texture(dsock.Texture):
    """ Class Texture
    

    | Inherits from: dsock.Texture 
    

    Static methods
    ==============
    - Brick      : Sockets      [color (Color), fac (Float)] 
    - Checker    : Sockets      [color (Color), fac (Float)] 
    - Gradient   : Sockets      [color (Color), fac (Float)] 
    - Image      : Sockets      [color (Color), alpha (Float)] 
    - Magic      : Sockets      [color (Color), fac (Float)] 
    - Musgrave   : fac (Float) 
    - Noise      : Sockets      [fac (Float), color (Color)] 
    - Voronoi    : Sockets      [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
    - Wave       : Sockets      [color (Color), fac (Float)] 
    - WhiteNoise : Sockets      [value (Float), color (Color)] 
    

    Methods
    =======
    - switch : output (Texture) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """Call node BrickTexture (ShaderNodeTexBrick)

        Sockets arguments
        -----------------
            vector         : Vector
            color1         : Color
            color2         : Color
            mortar         : Color
            scale          : Float
            mortar_size    : Float
            mortar_smooth  : Float
            bias           : Float
            brick_width    : Float
            row_height     : Float

        Parameters arguments
        --------------------
            offset         : 0.5
            offset_frequency: 2
            squash         : 1.0
            squash_frequency: 2

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None):
        """Call node CheckerTexture (ShaderNodeTexChecker)

        Sockets arguments
        -----------------
            vector         : Vector
            color1         : Color
            color2         : Color
            scale          : Float

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)

    @staticmethod
    def Gradient(vector=None, gradient_type='LINEAR'):
        """Call node GradientTexture (ShaderNodeTexGradient)

        Sockets arguments
        -----------------
            vector         : Vector

        Parameters arguments
        --------------------
            gradient_type  : 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.GradientTexture(vector=vector, gradient_type=gradient_type)

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None, turbulence_depth=2):
        """Call node MagicTexture (ShaderNodeTexMagic)

        Sockets arguments
        -----------------
            vector         : Vector
            scale          : Float
            distortion     : Float

        Parameters arguments
        --------------------
            turbulence_depth: 2

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)

    @staticmethod
    def Musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        """Call node MusgraveTexture (ShaderNodeTexMusgrave)

        Sockets arguments
        -----------------
            vector         : Vector
            w              : Float
            scale          : Float
            detail         : Float
            dimension      : Float
            lacunarity     : Float
            offset         : Float
            gain           : Float

        Parameters arguments
        --------------------
            musgrave_dimensions: '3D' in [1D, 2D, 3D, 4D]
            musgrave_type  : 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]

        Returns
        -------
            Float
        """

        return nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).fac

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        """Call node NoiseTexture (ShaderNodeTexNoise)

        Sockets arguments
        -----------------
            vector         : Vector
            w              : Float
            scale          : Float
            detail         : Float
            roughness      : Float
            distortion     : Float

        Parameters arguments
        --------------------
            noise_dimensions: '3D' in [1D, 2D, 3D, 4D]

        Returns
        -------
            Sockets [fac (Float), color (Color)]
        """

        return nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """Call node VoronoiTexture (ShaderNodeTexVoronoi)

        Sockets arguments
        -----------------
            vector         : Vector
            w              : Float
            scale          : Float
            smoothness     : Float
            exponent       : Float
            randomness     : Float

        Parameters arguments
        --------------------
            distance       : 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            feature        : 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            voronoi_dimensions: '3D' in [1D, 2D, 3D, 4D]

        Returns
        -------
            Sockets [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
        """

        return nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """Call node WaveTexture (ShaderNodeTexWave)

        Sockets arguments
        -----------------
            vector         : Vector
            scale          : Float
            distortion     : Float
            detail         : Float
            detail_scale   : Float
            detail_roughness: Float
            phase_offset   : Float

        Parameters arguments
        --------------------
            bands_direction: 'X' in [X, Y, Z, DIAGONAL]
            rings_direction: 'X' in [X, Y, Z, SPHERICAL]
            wave_profile   : 'SIN' in [SIN, SAW, TRI]
            wave_type      : 'BANDS' in [BANDS, RINGS]

        Returns
        -------
            Sockets [color (Color), fac (Float)]
        """

        return nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)

    @staticmethod
    def WhiteNoise(vector=None, w=None, noise_dimensions='3D'):
        """Call node WhiteNoiseTexture (ShaderNodeTexWhiteNoise)

        Sockets arguments
        -----------------
            vector         : Vector
            w              : Float

        Parameters arguments
        --------------------
            noise_dimensions: '3D' in [1D, 2D, 3D, 4D]

        Returns
        -------
            Sockets [value (Float), color (Color)]
        """

        return nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)

    @staticmethod
    def Image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """Call node ImageTexture (GeometryNodeImageTexture)

        Sockets arguments
        -----------------
            image          : Image
            vector         : Vector
            frame          : Integer

        Parameters arguments
        --------------------
            extension      : 'REPEAT' in [REPEAT, EXTEND, CLIP]
            interpolation  : 'Linear' in [Linear, Closest, Cubic]

        Returns
        -------
            Sockets [color (Color), alpha (Float)]
        """

        return nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """Call node Switch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Texture (self)
            switch1        : Boolean
            true           : Texture

        Fixed parameters
        ----------------
            input_type     : 'TEXTURE'

        Returns
        -------
            Texture
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='TEXTURE').output


