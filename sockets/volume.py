#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-12-12
@author: Generated from generator module
Blender version: 3.4.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Volume

class Volume(gn.Geometry):
    """ Data class Volume
    """

    def copy(self):

        return Volume(self)


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None, node_label = None, node_color = None):
        """ Geometry node [*Volume Cube*].
        
        
            Args:
                density: Float
                background: Float
                min: Vector
                max: Vector
                resolution_x: Integer
                resolution_y: Integer
                resolution_z: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Volume
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VolumeCube`
            
            
            .. blid:: GeometryNodeVolumeCube
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VolumeCube(density=density, background=background, min=min, max=max, resolution_x=resolution_x, resolution_y=resolution_y, resolution_z=resolution_z, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.VolumeCube(density=density, background=background, min=min, max=max, resolution_x=resolution_x, resolution_y=resolution_y, resolution_z=resolution_z, label=node_label, node_color=node_color).volume)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', node_label = None, node_color = None):
        """ Geometry node [*Volume to Mesh*].
        
        
            Args:
                voxel_size: Float
                voxel_amount: Float
                threshold: Float
                adaptivity: Float
                resolution_mode (str): 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.VolumeToMesh`
            
            
            .. blid:: GeometryNodeVolumeToMesh
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode, label=node_label, node_color=node_color)
                
        """

        return nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode, label=node_label, node_color=node_color).mesh


    def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):
        """ Distribute points in volume.
        
        Args:
            volume (DataSocket): Volume
            density (DataSocket): Float
            seed (DataSocket): Integer
            spacing (DataSocket): Vector
            threshold (DataSocket): Float
            mode (str): Node parameter, default = 'DENSITY_RANDOM' in ('DENSITY_RANDOM', 'DENSITY_GRID')
            node_color (color): Node color
            node_label (str): Node label
    
    
        Output sockets:
            - **points** : Points
        """
        
        return nodes.DistributePointsInVolume(volume=self, density=density, seed=seed, spacing=spacing, threshold=threshold, mode=mode).points

