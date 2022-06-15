#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-15
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
from geonodes.core.domains import Domain
from geonodes import PointDomain, EdgeDomain, FaceDomain, CornerDomain, CurveDomain

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
        
        
    

        Methods
        -------
            - instance_on_points : instances (Instances)
            - set_radius : points (Points)
            - to_vertices : mesh (Mesh)
            - to_volume : volume (Volume)
    """

    def init_domains(self):
        self.point = PointDomain(self)


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


