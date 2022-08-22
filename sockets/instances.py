#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-21
@author: Generated from generator module
Blender version: 3.2.2
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Instances

class Instances(gn.Geometry):
    """ Data class Instances
    """

    def copy(self):

        return Instances(self)

    def init_domains(self):
        self.insts  = domains.Instance(self)

    @property
    def instance(self):
        return self.insts



    def reset_properties(self):

        super().reset_properties()

        self.domain_size_ = None

        self.instance_count_ = None

    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, node_label = None, node_color = None):
        """ Geometry node [*Instance on Points*].
        
        
            Args:
                points: Points
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
                nodes.InstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
                
        """

        return nodes.InstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color).instances

    @staticmethod
    def FromGeometries(*geometry, node_label = None, node_color = None):
        """ Geometry node [*Geometry to Instance*].
        
        
            Args:
                geometry: <m>Geometry
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Instances
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.GeometryToInstance`
            
            
            .. blid:: GeometryNodeGeometryToInstance
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.GeometryToInstance(*geometry, label=node_label, node_color=node_color)
                
        """

        return nodes.GeometryToInstance(*geometry, label=node_label, node_color=node_color).instances


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def domain_size(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'INSTANCES'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='INSTANCES', label=f"{self.node_chain_label}.domain_size")
                
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='INSTANCES', label=f"{self.node_chain_label}.domain_size").instance_count
        return self.domain_size_

    @property
    def instance_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'INSTANCES'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='INSTANCES', label=f"{self.node_chain_label}.instance_count")
                
        """

        return self.domain_size.instance_count


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None, node_label = None, node_color = None):
        """ Geometry node [*Rotate Instances*].
        
        
            Args:
                selection: Boolean
                rotation: Vector
                pivot_point: Vector
                local_space: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Instances
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RotateInstances`
            
            
            .. blid:: GeometryNodeRotateInstances
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space, label=node_label, node_color=node_color))

    def scale(self, selection=None, scale=None, center=None, local_space=None, node_label = None, node_color = None):
        """ Geometry node [*Scale Instances*].
        
        
            Args:
                selection: Boolean
                scale: Vector
                center: Vector
                local_space: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Instances
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ScaleInstances`
            
            
            .. blid:: GeometryNodeScaleInstances
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space, label=node_label, node_color=node_color))

    def translate(self, selection=None, translation=None, local_space=None, node_label = None, node_color = None):
        """ Geometry node [*Translate Instances*].
        
        
            Args:
                selection: Boolean
                translation: Vector
                local_space: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Instances
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TranslateInstances`
            
            
            .. blid:: GeometryNodeTranslateInstances
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space, label=node_label, node_color=node_color))

    def realize(self, legacy_behavior=False, node_label = None, node_color = None):
        """ Geometry node [*Realize Instances*].
        
        
            Args:
                legacy_behavior (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RealizeInstances`
            
            
            .. blid:: GeometryNodeRealizeInstances
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color)
                
        """

        return nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color).geometry

    def to_points(self, selection=None, position=None, radius=None, node_label = None, node_color = None):
        """ Geometry node [*Instances to Points*].
        
        
            Args:
                selection: Boolean
                position: Vector
                radius: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Points
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.InstancesToPoints`
            
            
            .. blid:: GeometryNodeInstancesToPoints
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius, label=node_label, node_color=node_color)
                
        """

        return nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius, label=node_label, node_color=node_color).points

    def duplicate_instances(self, selection=None, amount=None, node_label = None, node_color = None):
        """ Geometry node [*Duplicate Elements*].
        
        
            Args:
                selection: Boolean
                amount: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), duplicate_index (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DuplicateElements`
            
                - domain = 'INSTANCE'
                  
            .. blid:: GeometryNodeDuplicateElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='INSTANCE', label=node_label, node_color=node_color)
                
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='INSTANCE', label=node_label, node_color=node_color)


