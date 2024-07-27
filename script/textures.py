#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : textures
-----------------
- Create the textures

```  python
# Create a noise texture
noise_node = Texture.Noise()
```

classes
-------
- Texture       : Implements the texture nodes creation
    - Brick
    - Checker
    - Gradient
    - Image
    - Magic
    - Noise
    - Voronoi
    - Wave
    - WhiteNoise


functions
---------

updates
-------
- creation : 2024/07/23
"""

from .treeclass import Node

class Texture:
    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None,
        bias=None, brick_width=None, row_height=None):
        return Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar,
            'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height})

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None):
        return Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})

    @staticmethod
    def Gradient(vector=None):
        return Node('Gradient Texture', {'Vector': vector})

    @staticmethod
    def Image(image=None, vector=None, frame=None, interpolation='Linear', extension='REPEAT'):
        # interpolation in ('Linear', 'Closest', 'Cubic')
        # extension in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
        return Node('Image Texture', {'Image': image, 'Vector': vector, 'Frame': frame},
            interpolation=interpolation, extension=extension)

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None):
        return Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion})

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, offset=None, gain=None, distortion=None,
        dim='3D', noise_type='FBM'):
        # noise_dimensions in ('1D', '2D', '3D', '4D')
        # noise_type in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
        return Node('Noise Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail,
            'Roughness': roughness, 'Lacunarity': lacunarity, 'Offset': offset,
            'Gain': gain, 'Distortion': distortion}, noise_dimensions=dim, noise_type=noise_type)

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, smoothness=None,
        exponent=None, randomness=None, dim='3D', feature='F1', distance='EUCLIDEAN'):
        # voronoi_dimensions in ('1D', '2D', '3D', '4D')
        # feature in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
        # distance in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
        return Node('Voronoi Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness,
            'Lacunarity': lacunarity, 'Smoothness': smoothness, 'Exponent': exponent, 'Randomness': randomness},
            voronoi_dimensions=dim, feature=feature, distance=distance)

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None,
        wave_type = 'BANDS', bands_direction='X', wave_profile='SIN'):
        # wave_type in ('BANDS', 'RINGS')
        # bands_direction in ('X', 'Y', 'Z', 'DIAGONAL')
        # wave_profile in ('SIN', 'SAW', 'TRI')
        return Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail,
            'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset},
            wave_type=wave_type, bands_direction=bands_direction, wave_profile=wave_profile)

    @staticmethod
    def WhiteNoise(vector=None, w=None, dim='3D'):
        # noise_dimensions in ('1D', '2D', '3D', '4D')
        return Node('White Noise Texture', {'Vector': vector, 'W': w}, noise_dimensions=dim)
