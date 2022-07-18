#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-07-17
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
# Data class Points

class Points(gn.Geometry):
    """ Data class Points
    """

    def copy(self):

        return Points(self)

    def init_domains(self):
        self.points = domains.CloudPoint(self)

    @property
    def point(self):
        return self.points


    def reset_properties(self):

        super().reset_properties()

        self.domain_size_ = None

        self.point_count_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def domain_size(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'POINTCLOUD'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.domain_size")
                
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.domain_size").point_count
        return self.domain_size_

    @property
    def point_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'POINTCLOUD'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.point_count")
                
        """

        return self.domain_size.point_count


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_radius(self, selection=None, radius=None, node_label = None, node_color = None):
        """ Geometry node [*Set Point Radius*].
        
        
            Args:
                selection: Boolean
                radius: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Points
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetPointRadius`
            
            
            .. blid:: GeometryNodeSetPointRadius
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetPointRadius(points=self, selection=selection, radius=radius, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius, label=node_label, node_color=node_color))

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, node_label = None, node_color = None):
        """ Geometry node [*Instance on Points*].
        
        
            Args:
                selection: Boolean
                instance: Geometry
                pick_instance: Boolean
                instance_index: Integer
                rotation: Vector
                scale: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Instances
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.InstanceOnPoints`
            
            
            .. blid:: GeometryNodeInstanceOnPoints
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
                
        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color).instances

    def to_vertices(self, selection=None, node_label = None, node_color = None):
        """ Geometry node [*Points to Vertices*].
        
        
            Args:
                selection: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.PointsToVertices`
            
            
            .. blid:: GeometryNodePointsToVertices
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.PointsToVertices(points=self, selection=selection, label=node_label, node_color=node_color)
                
        """

        return nodes.PointsToVertices(points=self, selection=selection, label=node_label, node_color=node_color).mesh

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', node_label = None, node_color = None):
        """ Geometry node [*Points to Volume*].
        
        
            Args:
                density: Float
                voxel_size: Float
                voxel_amount: Float
                radius: Float
                resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Volume
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.PointsToVolume`
            
            
            .. blid:: GeometryNodePointsToVolume
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode, label=node_label, node_color=node_color)
                
        """

        return nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode, label=node_label, node_color=node_color).volume


