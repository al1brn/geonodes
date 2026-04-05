# Generated 2026-04-05 12:44:34

from __future__ import annotations
from .. sockettype import SocketType
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Texture(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    @classmethod
    def Brick(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2):
        """ > Node <&Node Brick Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        color1 : Color, optional
            socket 'Color1' (id: Color1)
        
        color2 : Color, optional
            socket 'Color2' (id: Color2)
        
        mortar : Color, optional
            socket 'Mortar' (id: Mortar)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        mortar_size : Float, optional
            socket 'Mortar Size' (id: Mortar Size)
        
        mortar_smooth : Float, optional
            socket 'Mortar Smooth' (id: Mortar Smooth)
        
        bias : Float, optional
            socket 'Bias' (id: Bias)
        
        brick_width : Float, optional
            socket 'Brick Width' (id: Brick Width)
        
        row_height : Float, optional
            socket 'Row Height' (id: Row Height)
        
        offset : float
            parameter `offset`
        
        offset_frequency : int
            parameter `offset_frequency`
        
        squash : float
            parameter `squash`
        
        squash_frequency : int
            parameter `squash_frequency`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        node = Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node._out

    @classmethod
    def Checker(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None):
        """ > Node <&Node Checker Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        color1 : Color, optional
            socket 'Color1' (id: Color1)
        
        color2 : Color, optional
            socket 'Color2' (id: Color2)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        node = Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return node._out

    @classmethod
    def Gabor(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    gabor_type: Literal['2D', '3D'] = '2D'):
        """ > Node <&Node Gabor Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        frequency : Float, optional
            socket 'Frequency' (id: Frequency)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        orientation : Float, optional
            socket 'Orientation' (id: Orientation 2D)
        
        gabor_type : Literal['2D', '3D']
            parameter `gabor_type`
        

        Returns
        -------
        Float
            peer sockets: phase_ (Float), intensity_ (Float)

        """
        utils.check_enum_arg('Gabor Texture', 'gabor_type', gabor_type, 'Gabor', ('2D', '3D'))
        node = Node('Gabor Texture', {'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation 2D': orientation}, gabor_type=gabor_type)
        return node._out

    @classmethod
    def Gradient(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR'):
        """ > Node <&Node Gradient Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        gradient_type : Literal['Linear', 'Quadratic', 'Easing', 'Diagonal', 'Spherical', 'Quadratic Sphere', 'Radial']
            parameter `gradient_type`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        utils.check_enum_arg('Gradient Texture', 'gradient_type', gradient_type, 'Gradient', ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'))
        node = Node('Gradient Texture', {'Vector': vector}, gradient_type=gradient_type)
        return node._out

    @classmethod
    def Magic(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2):
        """ > Node <&Node Magic Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        turbulence_depth : int
            parameter `turbulence_depth`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        node = Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return node._out

    @classmethod
    def Noise(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True):
        """ > Node <&Node Noise Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        lacunarity : Float, optional
            socket 'Lacunarity' (id: Lacunarity)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        noise_dimensions : Literal['1D', '2D', '3D', '4D']
            parameter `noise_dimensions`
        
        noise_type : Literal['Multifractal', 'Ridged Multifractal', 'Hybrid Multifractal', 'fBM', 'Hetero Terrain']
            parameter `noise_type`
        
        normalize : bool
            parameter `normalize`
        

        Returns
        -------
        Float
            peer sockets: color_ (Color)

        """
        utils.check_enum_arg('Noise Texture', 'noise_dimensions', noise_dimensions, 'Noise', ('1D', '2D', '3D', '4D'))
        utils.check_enum_arg('Noise Texture', 'noise_type', noise_type, 'Noise', ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'))
        node = Node('Noise Texture', {'Vector': vector, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Distortion': distortion}, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize)
        return node._out

    @classmethod
    def Voronoi(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&Node Voronoi Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        lacunarity : Float, optional
            socket 'Lacunarity' (id: Lacunarity)
        
        randomness : Float, optional
            socket 'Randomness' (id: Randomness)
        
        distance : Literal['Euclidean', 'Manhattan', 'Chebychev', 'Minkowski']
            parameter `distance`
        
        feature : Literal['F1', 'F2', 'Smooth F1', 'Distance to Edge', 'N-Sphere Radius']
            parameter `feature`
        
        normalize : bool
            parameter `normalize`
        
        voronoi_dimensions : Literal['1D', '2D', '3D', '4D']
            parameter `voronoi_dimensions`
        

        Returns
        -------
        Float
            peer sockets: color_ (Color), position_ (Vector)

        """
        utils.check_enum_arg('Voronoi Texture', 'distance', distance, 'Voronoi', ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'))
        utils.check_enum_arg('Voronoi Texture', 'feature', feature, 'Voronoi', ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'))
        utils.check_enum_arg('Voronoi Texture', 'voronoi_dimensions', voronoi_dimensions, 'Voronoi', ('1D', '2D', '3D', '4D'))
        node = Node('Voronoi Texture', {'Vector': vector, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Randomness': randomness}, distance=distance, feature=feature, normalize=normalize, voronoi_dimensions=voronoi_dimensions)
        return node._out

    @classmethod
    def Wave(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS'):
        """ > Node <&Node Wave Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        detail_scale : Float, optional
            socket 'Detail Scale' (id: Detail Scale)
        
        detail_roughness : Float, optional
            socket 'Detail Roughness' (id: Detail Roughness)
        
        phase_offset : Float, optional
            socket 'Phase Offset' (id: Phase Offset)
        
        bands_direction : Literal['X', 'Y', 'Z', 'Diagonal']
            parameter `bands_direction`
        
        rings_direction : Literal['X', 'Y', 'Z', 'Spherical']
            parameter `rings_direction`
        
        wave_profile : Literal['Sine', 'Saw', 'Triangle']
            parameter `wave_profile`
        
        wave_type : Literal['Bands', 'Rings']
            parameter `wave_type`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        utils.check_enum_arg('Wave Texture', 'bands_direction', bands_direction, 'Wave', ('X', 'Y', 'Z', 'DIAGONAL'))
        utils.check_enum_arg('Wave Texture', 'rings_direction', rings_direction, 'Wave', ('X', 'Y', 'Z', 'SPHERICAL'))
        utils.check_enum_arg('Wave Texture', 'wave_profile', wave_profile, 'Wave', ('SIN', 'SAW', 'TRI'))
        utils.check_enum_arg('Wave Texture', 'wave_type', wave_type, 'Wave', ('BANDS', 'RINGS'))
        node = Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node._out

    @classmethod
    def WhiteNoise(cls,
                    vector: Vector = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&Node White Noise Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        noise_dimensions : Literal['1D', '2D', '3D', '4D']
            parameter `noise_dimensions`
        

        Returns
        -------
        Float
            peer sockets: color_ (Color)

        """
        utils.check_enum_arg('White Noise Texture', 'noise_dimensions', noise_dimensions, 'WhiteNoise', ('1D', '2D', '3D', '4D'))
        node = Node('White Noise Texture', {'Vector': vector}, noise_dimensions=noise_dimensions)
        return node._out

