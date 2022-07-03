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
# Data class Instances

class Instances(gn.Geometry):
    """ 

    Data socket Instances
    ---------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Static methods
        --------------
            - FromGeometries : instances (Instances)
            - InstanceOnPoints : instances (Instances)
    

        Properties
        ----------
            - domain_size : instance_count (Integer)
            - instance_count : instance_count (Integer)
    

        Methods
        -------
            - duplicate_instances : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - realize : geometry (Geometry)
            - rotate : instances (Instances)
            - scale : instances (Instances)
            - to_points : points (Points)
            - translate : instances (Instances)
    """


    def copy(self):

        return Instances(self)

    def init_domains(self):
        self.insts = domains.Instance(self)

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
        """ > Node: InstanceOnPoints
          
        <sub>go to: top index
        blender ref GeometryNodeInstanceOnPoints
        node ref Instance on Points </sub>
                                  
        ```python
        v = Instances.InstanceOnPoints(points, selection, instance, pick_instance, instance_index, rotation, scale, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - points : Points
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
            nodes.InstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return nodes.InstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color).instances

    @staticmethod
    def FromGeometries(*geometry, node_label = None, node_color = None):
        """ > Node: GeometryToInstance
          
        <sub>go to: top index
        blender ref GeometryNodeGeometryToInstance
        node ref Geometry to Instance </sub>
                                  
        ```python
        v = Instances.FromGeometries(geometry_1, geometry_2, geometry_3, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : *Geometry## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.GeometryToInstance(*geometry, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return nodes.GeometryToInstance(*geometry, label=node_label, node_color=node_color).instances


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def domain_size(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = instances.domain_size
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'INSTANCES'
            - label:f"{self.node_chain_label}.domain_size"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='INSTANCES', label=f"{self.node_chain_label}.domain_size")
            ```
    

        Returns
        -------
            Integer
            
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='INSTANCES', label=f"{self.node_chain_label}.domain_size").instance_count
        return self.domain_size_

    @property
    def instance_count(self):
        """ > Node: DomainSize
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeDomainSize
        node ref Domain Size </sub>
                                  
        ```python
        v = instances.instance_count
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Fixed parameters
            - component : 'INSTANCES'
            - label:f"{self.node_chain_label}.instance_count"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DomainSize(geometry=self, component='INSTANCES', label=f"{self.node_chain_label}.instance_count")
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.domain_size.instance_count


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None, node_label = None, node_color = None):
        """ > Node: RotateInstances
          
        <sub>go to: top index
        blender ref GeometryNodeRotateInstances
        node ref Rotate Instances </sub>
                                  
        ```python
        v = instances.rotate(selection, rotation, pivot_point, local_space, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - instances : Instances (self)
            - selection : Boolean
            - rotation : Vector
            - pivot_point : Vector
            - local_space : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space, label=node_label, node_color=node_color))

    def scale(self, selection=None, scale=None, center=None, local_space=None, node_label = None, node_color = None):
        """ > Node: ScaleInstances
          
        <sub>go to: top index
        blender ref GeometryNodeScaleInstances
        node ref Scale Instances </sub>
                                  
        ```python
        v = instances.scale(selection, scale, center, local_space, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - instances : Instances (self)
            - selection : Boolean
            - scale : Vector
            - center : Vector
            - local_space : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space, label=node_label, node_color=node_color))

    def translate(self, selection=None, translation=None, local_space=None, node_label = None, node_color = None):
        """ > Node: TranslateInstances
          
        <sub>go to: top index
        blender ref GeometryNodeTranslateInstances
        node ref Translate Instances </sub>
                                  
        ```python
        v = instances.translate(selection, translation, local_space, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - instances : Instances (self)
            - selection : Boolean
            - translation : Vector
            - local_space : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Instances
            
        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space, label=node_label, node_color=node_color))

    def realize(self, legacy_behavior=False, node_label = None, node_color = None):
        """ > Node: RealizeInstances
          
        <sub>go to: top index
        blender ref GeometryNodeRealizeInstances
        node ref Realize Instances </sub>
                                  
        ```python
        v = instances.realize(legacy_behavior, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)## Parameters
            - legacy_behavior : False
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color).geometry

    def to_points(self, selection=None, position=None, radius=None, node_label = None, node_color = None):
        """ > Node: InstancesToPoints
          
        <sub>go to: top index
        blender ref GeometryNodeInstancesToPoints
        node ref Instances to Points </sub>
                                  
        ```python
        v = instances.to_points(selection, position, radius, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - instances : Instances (self)
            - selection : Boolean
            - position : Vector
            - radius : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Points
            
        """

        return nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius, label=node_label, node_color=node_color).points

    def duplicate_instances(self, selection=None, amount=None, node_label = None, node_color = None):
        """ > Node: DuplicateElements
          
        <sub>go to: top index
        blender ref GeometryNodeDuplicateElements
        node ref Duplicate Elements </sub>
                                  
        ```python
        v = instances.duplicate_instances(selection, amount, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - amount : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - domain : 'INSTANCE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='INSTANCE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), duplicate_index (Integer)]
            
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='INSTANCE', label=node_label, node_color=node_color)


