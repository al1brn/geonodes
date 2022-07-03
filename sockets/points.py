#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-07-03
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
    """ 

    Data socket Points
    ------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Properties
        ----------
            - domain_size : point_count (Integer)
            - point_count : point_count (Integer)
    

        Methods
        -------
            - instance_on_points : instances (Instances)
            - set_radius : points (Points)
            - to_vertices : mesh (Mesh)
            - to_volume : volume (Volume)
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
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = points.domain_size
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'POINTCLOUD'
            - label:f"{self.node_chain_label}.domain_size"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.domain_size")
            ```
    

        Returns
        -------
            Integer
            
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.domain_size").point_count
        return self.domain_size_

    @property
    def point_count(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = points.point_count
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'POINTCLOUD'
            - label:f"{self.node_chain_label}.point_count"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.point_count")
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.domain_size.point_count


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_radius(self, selection=None, radius=None, node_label = None, node_color = None):
        """ > Node: SetPointRadius
          
        <sub>go to: top index
        blender ref GeometryNodeSetPointRadius
        node ref Set Point Radius </sub>
                                  
        ```python
        v = points.set_radius(selection, radius, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - points : Points (self)
            - selection : Boolean
            - radius : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetPointRadius(points=self, selection=selection, radius=radius, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Points
            
        """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius, label=node_label, node_color=node_color))

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, node_label = None, node_color = None):
        """ > Node: InstanceOnPoints
          
        <sub>go to: top index
        blender ref GeometryNodeInstanceOnPoints
        node ref Instance on Points </sub>
                                  
        ```python
        v = points.instance_on_points(selection, instance, pick_instance, instance_index, rotation, scale, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - points : Points (self)
            - selection : Boolean
            - instance : Geometry
            - pick_instance : Boolean
            - instance_index : Integer
            - rotation : Vector
            - scale : Vector## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color).instances

    def to_vertices(self, selection=None, node_label = None, node_color = None):
        """ > Node: PointsToVertices
          
        <sub>go to: top index
        blender ref GeometryNodePointsToVertices
        node ref Points to Vertices </sub>
                                  
        ```python
        v = points.to_vertices(selection, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - points : Points (self)
            - selection : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.PointsToVertices(points=self, selection=selection, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.PointsToVertices(points=self, selection=selection, label=node_label, node_color=node_color).mesh

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', node_label = None, node_color = None):
        """ > Node: PointsToVolume
          
        <sub>go to: top index
        blender ref GeometryNodePointsToVolume
        node ref Points to Volume </sub>
                                  
        ```python
        v = points.to_volume(density, voxel_size, voxel_amount, radius, resolution_mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - points : Points (self)
            - density : Float
            - voxel_size : Float
            - voxel_amount : Float
            - radius : Float## Parameters
            - resolution_mode : 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Volume
            
        """

        return nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode, label=node_label, node_color=node_color).volume


