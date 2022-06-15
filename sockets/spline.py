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
from geonodes import Point, Edge, Face, Corner, Curve

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Spline

class Spline(gn.Geometry):
    """ 

    Data socket Spline
    ------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - duplicate_splines : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - set_cyclic : geometry (Geometry)
            - set_resolution : geometry (Geometry)
    """

    def init_domains(self):
        self.point  = Point(self)
        self.spline = Curve(self)

    @property
    def control_point(self):
        return self.point


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_cyclic(self, selection=None, cyclic=None, node_label = None, node_color = None):
        """ > Node: SetSplineCyclic
          
        <sub>go to: top index
        blender ref GeometryNodeSetSplineCyclic
        node ref Set Spline Cyclic </sub>
                                  
        ```python
        v = spline.set_cyclic(selection, cyclic, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - cyclic : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color))

    def set_resolution(self, selection=None, resolution=None, node_label = None, node_color = None):
        """ > Node: SetSplineResolution
          
        <sub>go to: top index
        blender ref GeometryNodeSetSplineResolution
        node ref Set Spline Resolution </sub>
                                  
        ```python
        v = spline.set_resolution(selection, resolution, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - resolution : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color))

    def duplicate_splines(self, selection=None, amount=None, node_label = None, node_color = None):
        """ > Node: DuplicateElements
          
        <sub>go to: top index
        blender ref GeometryNodeDuplicateElements
        node ref Duplicate Elements </sub>
                                  
        ```python
        v = spline.duplicate_splines(selection, amount, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - amount : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - domain : 'SPLINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), duplicate_index (Integer)]
            
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)


