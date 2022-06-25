#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-24
@author: Generated from generator module
Blender version: 3.2.0
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
    """ 

    Data socket Texture
    -------------------
        > Inherits from dsock.Texture
          
        <sub>go to index</sub>
        
        
    

        Static methods
        --------------
            - Brick : Sockets      [color (Color), fac (Float)]
            - Checker : Sockets      [color (Color), fac (Float)]
            - Gradient : Sockets      [color (Color), fac (Float)]
            - Image : Sockets      [color (Color), alpha (Float)]
            - Magic : Sockets      [color (Color), fac (Float)]
            - Musgrave : fac (Float)
            - Noise : Sockets      [fac (Float), color (Color)]
            - Voronoi : Sockets      [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
            - Wave : Sockets      [color (Color), fac (Float)]
            - WhiteNoise : Sockets      [value (Float), color (Color)]
    

        Methods
        -------
            - switch : output (Texture)
    """


    def copy(self):

        return Texture(self)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, node_label = None, node_color = None):
        """ > Node: BrickTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexBrick
        node ref Brick Texture </sub>
                                  
        ```python
        v = Texture.Brick(vector, color1, color2, mortar, scale, mortar_size, mortar_smooth, bias, brick_width, row_height, offset, offset_frequency, squash, squash_frequency, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - color1 : Color
            - color2 : Color
            - mortar : Color
            - scale : Float
            - mortar_size : Float
            - mortar_smooth : Float
            - bias : Float
            - brick_width : Float
            - row_height : Float## Parameters
            - offset : 0.5
            - offset_frequency : 2
            - squash : 1.0
            - squash_frequency : 2
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), fac (Float)]
            
        """

        return nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency, label=node_label, node_color=node_color)

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None, node_label = None, node_color = None):
        """ > Node: CheckerTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexChecker
        node ref Checker Texture </sub>
                                  
        ```python
        v = Texture.Checker(vector, color1, color2, scale, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - color1 : Color
            - color2 : Color
            - scale : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), fac (Float)]
            
        """

        return nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale, label=node_label, node_color=node_color)

    @staticmethod
    def Gradient(vector=None, gradient_type='LINEAR', node_label = None, node_color = None):
        """ > Node: GradientTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexGradient
        node ref Gradient Texture </sub>
                                  
        ```python
        v = Texture.Gradient(vector, gradient_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector## Parameters
            - gradient_type : 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.GradientTexture(vector=vector, gradient_type=gradient_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), fac (Float)]
            
        """

        return nodes.GradientTexture(vector=vector, gradient_type=gradient_type, label=node_label, node_color=node_color)

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None, turbulence_depth=2, node_label = None, node_color = None):
        """ > Node: MagicTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexMagic
        node ref Magic Texture </sub>
                                  
        ```python
        v = Texture.Magic(vector, scale, distortion, turbulence_depth, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - scale : Float
            - distortion : Float## Parameters
            - turbulence_depth : 2
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), fac (Float)]
            
        """

        return nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth, label=node_label, node_color=node_color)

    @staticmethod
    def Musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', node_label = None, node_color = None):
        """ > Node: MusgraveTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexMusgrave
        node ref Musgrave Texture </sub>
                                  
        ```python
        v = Texture.Musgrave(vector, w, scale, detail, dimension, lacunarity, offset, gain, musgrave_dimensions, musgrave_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - w : Float
            - scale : Float
            - detail : Float
            - dimension : Float
            - lacunarity : Float
            - offset : Float
            - gain : Float## Parameters
            - musgrave_dimensions : '3D' in [1D, 2D, 3D, 4D]
            - musgrave_type : 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type, label=node_label, node_color=node_color).fac

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', node_label = None, node_color = None):
        """ > Node: NoiseTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexNoise
        node ref Noise Texture </sub>
                                  
        ```python
        v = Texture.Noise(vector, w, scale, detail, roughness, distortion, noise_dimensions, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - w : Float
            - scale : Float
            - detail : Float
            - roughness : Float
            - distortion : Float## Parameters
            - noise_dimensions : '3D' in [1D, 2D, 3D, 4D]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [fac (Float), color (Color)]
            
        """

        return nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', node_label = None, node_color = None):
        """ > Node: VoronoiTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexVoronoi
        node ref Voronoi Texture </sub>
                                  
        ```python
        v = Texture.Voronoi(vector, w, scale, smoothness, exponent, randomness, distance, feature, voronoi_dimensions, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - w : Float
            - scale : Float
            - smoothness : Float
            - exponent : Float
            - randomness : Float## Parameters
            - distance : 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
            - feature : 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
            - voronoi_dimensions : '3D' in [1D, 2D, 3D, 4D]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
            
        """

        return nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions, label=node_label, node_color=node_color)

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', node_label = None, node_color = None):
        """ > Node: WaveTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexWave
        node ref Wave Texture </sub>
                                  
        ```python
        v = Texture.Wave(vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset, bands_direction, rings_direction, wave_profile, wave_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - scale : Float
            - distortion : Float
            - detail : Float
            - detail_scale : Float
            - detail_roughness : Float
            - phase_offset : Float## Parameters
            - bands_direction : 'X' in [X, Y, Z, DIAGONAL]
            - rings_direction : 'X' in [X, Y, Z, SPHERICAL]
            - wave_profile : 'SIN' in [SIN, SAW, TRI]
            - wave_type : 'BANDS' in [BANDS, RINGS]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), fac (Float)]
            
        """

        return nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type, label=node_label, node_color=node_color)

    @staticmethod
    def WhiteNoise(vector=None, w=None, noise_dimensions='3D', node_label = None, node_color = None):
        """ > Node: WhiteNoiseTexture
          
        <sub>go to: top index
        blender ref ShaderNodeTexWhiteNoise
        node ref White Noise Texture </sub>
                                  
        ```python
        v = Texture.WhiteNoise(vector, w, noise_dimensions, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - vector : Vector
            - w : Float## Parameters
            - noise_dimensions : '3D' in [1D, 2D, 3D, 4D]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [value (Float), color (Color)]
            
        """

        return nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions, label=node_label, node_color=node_color)

    @staticmethod
    def Image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', node_label = None, node_color = None):
        """ > Node: ImageTexture
          
        <sub>go to: top index
        blender ref GeometryNodeImageTexture
        node ref Image Texture </sub>
                                  
        ```python
        v = Texture.Image(image, vector, frame, extension, interpolation, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - image : Image
            - vector : Vector
            - frame : Integer## Parameters
            - extension : 'REPEAT' in [REPEAT, EXTEND, CLIP]
            - interpolation : 'Linear' in [Linear, Closest, Cubic]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), alpha (Float)]
            
        """

        return nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation, label=node_label, node_color=node_color)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = texture.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Texture (self)
            - switch : Boolean
            - true : Texture## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'TEXTURE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='TEXTURE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Texture
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='TEXTURE', label=node_label, node_color=node_color).output


