#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-09-16
@author: Generated from generator module
Blender version: 3.3.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Texture

class Texture(dsock.Texture):
    """ Data class Texture
    """

    def copy(self):

        return Texture(self)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, node_label = None, node_color = None):
        """ Geometry node [*Brick Texture*].
        
        
            Args:
                vector: Vector
                color1: Color
                color2: Color
                mortar: Color
                scale: Float
                mortar_size: Float
                mortar_smooth: Float
                bias: Float
                brick_width: Float
                row_height: Float
                offset (float): 0.5
                offset_frequency (int): 2
                squash (float): 1.0
                squash_frequency (int): 2
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [color (Color), fac (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BrickTexture`
            
            
            .. blid:: ShaderNodeTexBrick
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency, label=node_label, node_color=node_color)
                
        """

        return nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency, label=node_label, node_color=node_color)

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None, node_label = None, node_color = None):
        """ Geometry node [*Checker Texture*].
        
        
            Args:
                vector: Vector
                color1: Color
                color2: Color
                scale: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [color (Color), fac (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CheckerTexture`
            
            
            .. blid:: ShaderNodeTexChecker
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale, label=node_label, node_color=node_color)
                
        """

        return nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale, label=node_label, node_color=node_color)

    @staticmethod
    def Gradient(vector=None, gradient_type='LINEAR', node_label = None, node_color = None):
        """ Geometry node [*Gradient Texture*].
        
        
            Args:
                vector: Vector
                gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [color (Color), fac (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.GradientTexture`
            
            
            .. blid:: ShaderNodeTexGradient
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.GradientTexture(vector=vector, gradient_type=gradient_type, label=node_label, node_color=node_color)
                
        """

        return nodes.GradientTexture(vector=vector, gradient_type=gradient_type, label=node_label, node_color=node_color)

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None, turbulence_depth=2, node_label = None, node_color = None):
        """ Geometry node [*Magic Texture*].
        
        
            Args:
                vector: Vector
                scale: Float
                distortion: Float
                turbulence_depth (int): 2
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [color (Color), fac (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MagicTexture`
            
            
            .. blid:: ShaderNodeTexMagic
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth, label=node_label, node_color=node_color)
                
        """

        return nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth, label=node_label, node_color=node_color)

    @staticmethod
    def Musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', node_label = None, node_color = None):
        """ Geometry node [*Musgrave Texture*].
        
        
            Args:
                vector: Vector
                w: Float
                scale: Float
                detail: Float
                dimension: Float
                lacunarity: Float
                offset: Float
                gain: Float
                musgrave_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
                musgrave_type (str): 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MusgraveTexture`
            
            
            .. blid:: ShaderNodeTexMusgrave
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type, label=node_label, node_color=node_color)
                
        """

        return nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type, label=node_label, node_color=node_color).fac

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', node_label = None, node_color = None):
        """ Geometry node [*Noise Texture*].
        
        
            Args:
                vector: Vector
                w: Float
                scale: Float
                detail: Float
                roughness: Float
                distortion: Float
                noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [fac (Float), color (Color)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.NoiseTexture`
            
            
            .. blid:: ShaderNodeTexNoise
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)
                
        """

        return nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', node_label = None, node_color = None):
        """ Geometry node [*Voronoi Texture*].
        
        
            Args:
                vector: Vector
                w: Float
                scale: Float
                smoothness: Float
                exponent: Float
                randomness: Float
                distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
                feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
                voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VoronoiTexture`
            
            
            .. blid:: ShaderNodeTexVoronoi
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions, label=node_label, node_color=node_color)
                
        """

        return nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions, label=node_label, node_color=node_color)

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', node_label = None, node_color = None):
        """ Geometry node [*Wave Texture*].
        
        
            Args:
                vector: Vector
                scale: Float
                distortion: Float
                detail: Float
                detail_scale: Float
                detail_roughness: Float
                phase_offset: Float
                bands_direction (str): 'X' in [X, Y, Z, DIAGONAL]
                rings_direction (str): 'X' in [X, Y, Z, SPHERICAL]
                wave_profile (str): 'SIN' in [SIN, SAW, TRI]
                wave_type (str): 'BANDS' in [BANDS, RINGS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [color (Color), fac (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.WaveTexture`
            
            
            .. blid:: ShaderNodeTexWave
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type, label=node_label, node_color=node_color)
                
        """

        return nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type, label=node_label, node_color=node_color)

    @staticmethod
    def WhiteNoise(vector=None, w=None, noise_dimensions='3D', node_label = None, node_color = None):
        """ Geometry node [*White Noise Texture*].
        
        
            Args:
                vector: Vector
                w: Float
                noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [value (Float), color (Color)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.WhiteNoiseTexture`
            
            
            .. blid:: ShaderNodeTexWhiteNoise
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)
                
        """

        return nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)

    @staticmethod
    def Image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', node_label = None, node_color = None):
        """ Geometry node [*Image Texture*].
        
        
            Args:
                image: Image
                vector: Vector
                frame: Integer
                extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
                interpolation (str): 'Linear' in [Linear, Closest, Cubic]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [color (Color), alpha (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ImageTexture`
            
            
            .. blid:: GeometryNodeImageTexture
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation, label=node_label, node_color=node_color)
                
        """

        return nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation, label=node_label, node_color=node_color)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Texture
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Texture
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'TEXTURE'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='TEXTURE', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='TEXTURE', label=node_label, node_color=node_color).output


