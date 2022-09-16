#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-09-16
@author: Generated from generator module
Blender version: 3.3.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Curves

class Curves(gn.Geometry):
    """ Data class Curves
    """

    def copy(self):

        return Curves(self)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def deform_on_surface(self, node_label = None, node_color = None):
        """ Geometry node [*Deform Curves on Surface*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curves
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DeformCurvesOnSurface`
            
            
            .. blid:: GeometryNodeDeformCurvesOnSurface
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DeformCurvesOnSurface(curves=self, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.DeformCurvesOnSurface(curves=self, label=node_label, node_color=node_color))


