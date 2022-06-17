#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-17
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
# Data class String

class String(dsock.String):
    """ 

    Data socket String
    ------------------
        > Inherits from dsock.String
          
        <sub>go to index</sub>
        
        
    

        Properties
        ----------
            - length : length (Integer)
    

        Methods
        -------
            - average : result (Boolean)
            - direction : result (Boolean)
            - dot_product : result (Boolean)
            - element : result (Boolean)
            - join : string (String)
            - length : result (Boolean)
            - replace : string (String)
            - slice : string (String)
            - switch : output (String)
            - to_curves : Sockets      [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
    """


    def reset_properties(self):

        super().reset_properties()

        self.length_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def length(self):
        """ > Node: StringLength
          
        <sub>go to: top index
        blender ref FunctionNodeStringLength
        node ref String Length </sub>
                                  
        ```python
        v = string.length
        ```
    

        Arguments
        ---------
            ## Sockets
            - string : String (self)## Fixed parameters
            - label:f"{self.node_chain_label}.length"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.StringLength(string=self, label=f"{self.node_chain_label}.length")
            ```
    

        Returns
        -------
            Integer
            
        """

        if self.length_ is None:
            self.length_ = nodes.StringLength(string=self, label=f"{self.node_chain_label}.length").length
        return self.length_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = string.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : String (self)
            - switch : Boolean
            - true : String## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'STRING'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='STRING', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='STRING', label=node_label, node_color=node_color).output

    def element(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = string.element(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : String (self)
            - b : String## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'STRING'
            - mode : 'ELEMENT'
            - operation : 'ELEMENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT', label=node_label, node_color=node_color).result

    def length(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = string.length(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : String (self)
            - b : String## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'STRING'
            - mode : 'ELEMENT'
            - operation : 'LENGTH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH', label=node_label, node_color=node_color).result

    def average(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = string.average(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : String (self)
            - b : String## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'STRING'
            - mode : 'ELEMENT'
            - operation : 'AVERAGE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE', label=node_label, node_color=node_color).result

    def dot_product(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = string.dot_product(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : String (self)
            - b : String## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'STRING'
            - mode : 'ELEMENT'
            - operation : 'DOT_PRODUCT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT', label=node_label, node_color=node_color).result

    def direction(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = string.direction(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : String (self)
            - b : String## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'STRING'
            - mode : 'ELEMENT'
            - operation : 'DIRECTION'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION', label=node_label, node_color=node_color).result

    def join(self, *strings, delimiter=None, node_label = None, node_color = None):
        """ > Node: JoinStrings
          
        <sub>go to: top index
        blender ref GeometryNodeStringJoin
        node ref Join Strings </sub>
                                  
        ```python
        v = string.join(strings_1, strings_2, strings_3, delimiter, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - strings : *String (self)
            - delimiter : String## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.JoinStrings(self, *strings, delimiter=delimiter, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.JoinStrings(self, *strings, delimiter=delimiter, label=node_label, node_color=node_color).string

    def replace(self, find=None, replace=None, node_label = None, node_color = None):
        """ > Node: ReplaceString
          
        <sub>go to: top index
        blender ref FunctionNodeReplaceString
        node ref Replace String </sub>
                                  
        ```python
        v = string.replace(find, replace, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - string : String (self)
            - find : String
            - replace : String## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ReplaceString(string=self, find=find, replace=replace, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            String
            
        """

        return self.stack(nodes.ReplaceString(string=self, find=find, replace=replace, label=node_label, node_color=node_color))

    def slice(self, position=None, length=None, node_label = None, node_color = None):
        """ > Node: SliceString
          
        <sub>go to: top index
        blender ref FunctionNodeSliceString
        node ref Slice String </sub>
                                  
        ```python
        v = string.slice(position, length, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - string : String (self)
            - position : Integer
            - length : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SliceString(string=self, position=position, length=length, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.SliceString(string=self, position=position, length=length, label=node_label, node_color=node_color).string

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', node_label = None, node_color = None):
        """ > Node: StringToCurves
          
        <sub>go to: top index
        blender ref GeometryNodeStringToCurves
        node ref String to Curves </sub>
                                  
        ```python
        v = string.to_curves(size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height, align_x, align_y, overflow, pivot_mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - string : String (self)
            - size : Float
            - character_spacing : Float
            - word_spacing : Float
            - line_spacing : Float
            - text_box_width : Float
            - text_box_height : Float## Parameters
            - align_x : 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
            - align_y : 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
            - overflow : 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
            - pivot_mode : 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
            
        """

        return nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode, label=node_label, node_color=node_color)


