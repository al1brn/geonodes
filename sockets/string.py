import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

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
    

            Sockets
            -------
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

    def switch(self, switch0=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
        
        ```python
        v = string.switch(switch0, true)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - false : String (self)
                    - switch0 : Boolean
                    - true : String## Fixed parameters
                    - input_type : 'STRING'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch0=switch0, true=true, input_type='STRING')
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.Switch(false=self, switch0=switch0, true=true, input_type='STRING').output

    def element(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        
        ```python
        v = string.element(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : String (self)
                    - b : String## Fixed parameters
                    - data_type : 'STRING'
                    - mode : 'ELEMENT'
                    - operation : 'ELEMENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT').result

    def length(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        
        ```python
        v = string.length(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : String (self)
                    - b : String## Fixed parameters
                    - data_type : 'STRING'
                    - mode : 'ELEMENT'
                    - operation : 'LENGTH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH').result

    def average(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        
        ```python
        v = string.average(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : String (self)
                    - b : String## Fixed parameters
                    - data_type : 'STRING'
                    - mode : 'ELEMENT'
                    - operation : 'AVERAGE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE').result

    def dot_product(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        
        ```python
        v = string.dot_product(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : String (self)
                    - b : String## Fixed parameters
                    - data_type : 'STRING'
                    - mode : 'ELEMENT'
                    - operation : 'DOT_PRODUCT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT').result

    def direction(self, b=None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
        
        ```python
        v = string.direction(b)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - a : String (self)
                    - b : String## Fixed parameters
                    - data_type : 'STRING'
                    - mode : 'ELEMENT'
                    - operation : 'DIRECTION'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION').result

    def join(self, *strings, delimiter=None):
        """ > Node: JoinStrings
          
        <sub>go to: top index
        blender ref GeometryNodeStringJoin
        node ref Join Strings </sub>
        
        ```python
        v = string.join(strings_1, strings_2, strings_3, delimiter)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - strings : *String (self)
                    - delimiter : String
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.JoinStrings(self, *strings, delimiter=delimiter)
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.JoinStrings(self, *strings, delimiter=delimiter).string

    def replace(self, find=None, replace=None):
        """ > Node: ReplaceString
          
        <sub>go to: top index
        blender ref FunctionNodeReplaceString
        node ref Replace String </sub>
        
        ```python
        v = string.replace(find, replace)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - string : String (self)
                    - find : String
                    - replace : String
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ReplaceString(string=self, find=find, replace=replace)
            ```
    

        Returns
        -------
            String
            
        """

        return self.stack(nodes.ReplaceString(string=self, find=find, replace=replace))

    def slice(self, position=None, length=None):
        """ > Node: SliceString
          
        <sub>go to: top index
        blender ref FunctionNodeSliceString
        node ref Slice String </sub>
        
        ```python
        v = string.slice(position, length)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - string : String (self)
                    - position : Integer
                    - length : Integer
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SliceString(string=self, position=position, length=length)
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.SliceString(string=self, position=position, length=length).string

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """ > Node: StringToCurves
          
        <sub>go to: top index
        blender ref GeometryNodeStringToCurves
        node ref String to Curves </sub>
        
        ```python
        v = string.to_curves(size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height, align_x, align_y, overflow, pivot_mode)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
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
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
            ```
    

        Returns
        -------
            Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
            
        """

        return nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)


