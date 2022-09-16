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
# Data class String

class String(dsock.String):
    """ Data class String
    """

    def copy(self):

        return String(self)


    def reset_properties(self):

        super().reset_properties()

        self.length_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def length(self):
        """ Geometry node [*String Length*].
        
        
        
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StringLength`
            
            
            .. blid:: FunctionNodeStringLength
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StringLength(string=self, label=f"{self.node_chain_label}.length")
                
        """

        if self.length_ is None:
            self.length_ = nodes.StringLength(string=self, label=f"{self.node_chain_label}.length").length
        return self.length_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: String
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                String
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'STRING'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='STRING', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='STRING', label=node_label, node_color=node_color).output

    def equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: String
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'STRING'
                - mode = 'ELEMENT'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: String
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'STRING'
                - mode = 'ELEMENT'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def replace(self, find=None, replace=None, node_label = None, node_color = None):
        """ Geometry node [*Replace String*].
        
        
            Args:
                find: String
                replace: String
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                String
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ReplaceString`
            
            
            .. blid:: FunctionNodeReplaceString
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ReplaceString(string=self, find=find, replace=replace, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.ReplaceString(string=self, find=find, replace=replace, label=node_label, node_color=node_color))

    def slice(self, position=None, length=None, node_label = None, node_color = None):
        """ Geometry node [*Slice String*].
        
        
            Args:
                position: Integer
                length: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                String
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SliceString`
            
            
            .. blid:: FunctionNodeSliceString
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SliceString(string=self, position=position, length=length, label=node_label, node_color=node_color)
                
        """

        return nodes.SliceString(string=self, position=position, length=length, label=node_label, node_color=node_color).string

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', node_label = None, node_color = None):
        """ Geometry node [*String to Curves*].
        
        
            Args:
                size: Float
                character_spacing: Float
                word_spacing: Float
                line_spacing: Float
                text_box_width: Float
                text_box_height: Float
                align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
                align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
                overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
                pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.StringToCurves`
            
            
            .. blid:: GeometryNodeStringToCurves
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode, label=node_label, node_color=node_color)
                
        """

        return nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode, label=node_label, node_color=node_color)


