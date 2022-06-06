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
    Index 
    

    Static methods
    ==============
    - **Brick**      : BrickTexture Sockets      [color (Color), fac (Float)] 
    - **Checker**    : CheckerTexture Sockets      [color (Color), fac (Float)] 
    - **Gradient**   : GradientTexture Sockets      [color (Color), fac (Float)] 
    - **Image**      : ImageTexture Sockets      [color (Color), alpha (Float)] 
    - **Magic**      : MagicTexture Sockets      [color (Color), fac (Float)] 
    - **Musgrave**   : MusgraveTexture fac (Float) 
    - **Noise**      : NoiseTexture Sockets      [fac (Float), color (Color)] 
    - **Voronoi**    : VoronoiTexture Sockets      [distance (Float), color (Color), position (Vector), w (Float),
      radius (Float)] 
    - **Wave**       : WaveTexture Sockets      [color (Color), fac (Float)] 
    - **WhiteNoise** : WhiteNoiseTexture Sockets      [value (Float), color (Color)] 
    

    Methods
    =======
    - **switch** : Switch output (Texture) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """ Brick
        

        | Node: BrickTexture 
        Top Index 
        

            v = Texture.Brick(vector, color1, color2, mortar, scale, mortar_size, mortar_smooth, bias, brick_width,
            row_height, offset, offset_frequency, squash, squash_frequency) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector        : Vector 
            - color1        : Color 
            - color2        : Color 
            - mortar        : Color 
            - scale         : Float 
            - mortar_size   : Float 
            - mortar_smooth : Float 
            - bias          : Float 
            - brick_width   : Float 
            - row_height    : Float 
        

            Parameters arguments
            --------------------
            - offset           : 0.5 
            - offset_frequency : 2 
            - squash           : 1.0 
            - squash_frequency : 2 
        

        Node creation
        =============
        

            node = nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size,
            mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset,
            offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency) 
        

        Returns
        =======
                Sockets [color (Color), fac (Float)] 
        """

        return nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None):
        """ Checker
        

        | Node: CheckerTexture 
        Top Index 
        

            v = Texture.Checker(vector, color1, color2, scale) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector : Vector 
            - color1 : Color 
            - color2 : Color 
            - scale  : Float 
        

        Node creation
        =============
        

            node = nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale) 
        

        Returns
        =======
                Sockets [color (Color), fac (Float)] 
        """

        return nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)

    @staticmethod
    def Gradient(vector=None, gradient_type='LINEAR'):
        """ Gradient
        

        | Node: GradientTexture 
        Top Index 
        

            v = Texture.Gradient(vector, gradient_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector : Vector 
        

            Parameters arguments
            --------------------
            - gradient_type : 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]
        

        Node creation
        =============
        

            node = nodes.GradientTexture(vector=vector, gradient_type=gradient_type) 
        

        Returns
        =======
                Sockets [color (Color), fac (Float)] 
        """

        return nodes.GradientTexture(vector=vector, gradient_type=gradient_type)

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None, turbulence_depth=2):
        """ Magic
        

        | Node: MagicTexture 
        Top Index 
        

            v = Texture.Magic(vector, scale, distortion, turbulence_depth) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector     : Vector 
            - scale      : Float 
            - distortion : Float 
        

            Parameters arguments
            --------------------
            - turbulence_depth : 2 
        

        Node creation
        =============
        

            node = nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
        

        Returns
        =======
                Sockets [color (Color), fac (Float)] 
        """

        return nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)

    @staticmethod
    def Musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        """ Musgrave
        

        | Node: MusgraveTexture 
        Top Index 
        

            v = Texture.Musgrave(vector, w, scale, detail, dimension, lacunarity, offset, gain, musgrave_dimensions,
            musgrave_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector     : Vector 
            - w          : Float 
            - scale      : Float 
            - detail     : Float 
            - dimension  : Float 
            - lacunarity : Float 
            - offset     : Float 
            - gain       : Float 
        

            Parameters arguments
            --------------------
            - musgrave_dimensions : '3D' in [1D, 2D, 3D, 4D] 
            - musgrave_type       : 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]
        

        Node creation
        =============
        

            node = nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity,
            offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type) 
        

        Returns
        =======
                Float 
        """

        return nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).fac

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        """ Noise
        

        | Node: NoiseTexture 
        Top Index 
        

            v = Texture.Noise(vector, w, scale, detail, roughness, distortion, noise_dimensions) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector     : Vector 
            - w          : Float 
            - scale      : Float 
            - detail     : Float 
            - roughness  : Float 
            - distortion : Float 
        

            Parameters arguments
            --------------------
            - noise_dimensions : '3D' in [1D, 2D, 3D, 4D] 
        

        Node creation
        =============
        

            node = nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion,
            noise_dimensions=noise_dimensions) 
        

        Returns
        =======
                Sockets [fac (Float), color (Color)] 
        """

        return nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """ Voronoi
        

        | Node: VoronoiTexture 
        Top Index 
        

            v = Texture.Voronoi(vector, w, scale, smoothness, exponent, randomness, distance, feature, voronoi_dimensions)
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector     : Vector 
            - w          : Float 
            - scale      : Float 
            - smoothness : Float 
            - exponent   : Float 
            - randomness : Float 
        

            Parameters arguments
            --------------------
            - distance           : 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI] 
            - feature            : 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS] 
            - voronoi_dimensions : '3D' in [1D, 2D, 3D, 4D] 
        

        Node creation
        =============
        

            node = nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent,
            randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions) 
        

        Returns
        =======
                Sockets [distance (Float), color (Color), position (Vector), w (Float), radius (Float)] 
        """

        return nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """ Wave
        

        | Node: WaveTexture 
        Top Index 
        

            v = Texture.Wave(vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset, bands_direction,
            rings_direction, wave_profile, wave_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector           : Vector 
            - scale            : Float 
            - distortion       : Float 
            - detail           : Float 
            - detail_scale     : Float 
            - detail_roughness : Float 
            - phase_offset     : Float 
        

            Parameters arguments
            --------------------
            - bands_direction : 'X' in [X, Y, Z, DIAGONAL] 
            - rings_direction : 'X' in [X, Y, Z, SPHERICAL] 
            - wave_profile    : 'SIN' in [SIN, SAW, TRI] 
            - wave_type       : 'BANDS' in [BANDS, RINGS] 
        

        Node creation
        =============
        

            node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale,
            detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction,
            wave_profile=wave_profile, wave_type=wave_type) 
        

        Returns
        =======
                Sockets [color (Color), fac (Float)] 
        """

        return nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)

    @staticmethod
    def WhiteNoise(vector=None, w=None, noise_dimensions='3D'):
        """ WhiteNoise
        

        | Node: WhiteNoiseTexture 
        Top Index 
        

            v = Texture.WhiteNoise(vector, w, noise_dimensions) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - vector : Vector 
            - w      : Float 
        

            Parameters arguments
            --------------------
            - noise_dimensions : '3D' in [1D, 2D, 3D, 4D] 
        

        Node creation
        =============
        

            node = nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions) 
        

        Returns
        =======
                Sockets [value (Float), color (Color)] 
        """

        return nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)

    @staticmethod
    def Image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """ Image
        

        | Node: ImageTexture 
        Top Index 
        

            v = Texture.Image(image, vector, frame, extension, interpolation) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - image  : Image 
            - vector : Vector 
            - frame  : Integer 
        

            Parameters arguments
            --------------------
            - extension     : 'REPEAT' in [REPEAT, EXTEND, CLIP] 
            - interpolation : 'Linear' in [Linear, Closest, Cubic] 
        

        Node creation
        =============
        

            node = nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        

        Returns
        =======
                Sockets [color (Color), alpha (Float)] 
        """

        return nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        Top Index 
        

            v = texture.switch(switch1, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Texture (self) 
            - switch1 : Boolean 
            - true    : Texture 
        

            Fixed parameters
            ----------------
            - input_type : 'TEXTURE' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='TEXTURE') 
        

        Returns
        =======
                Texture 
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='TEXTURE').output


