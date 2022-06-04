import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class String

class String(dsock.String):
    """ Class String
    

    | Inherits from: dsock.String 
    

    Properties
    ==========
    - length : length (Integer) 
    

    Methods
    =======
    - average     : result (Boolean) 
    - direction   : result (Boolean) 
    - dot_product : result (Boolean) 
    - element     : result (Boolean) 
    - join        : string (String) 
    - length      : result (Boolean) 
    - slice       : string (String) 
    - switch      : output (String) 
    - to_curves   : Sockets      [curve_instances (Geometry), remainder (String), line (Integer), pivot_point
      (Vector)] 
    

    Stacked methods
    ===============
    - replace : String 
    """


    def reset_properties(self):
        self.length_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def length(self):
        """Call node StringLength (FunctionNodeStringLength)

        Sockets arguments
        -----------------
            string         : String (self)

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
        """Call node Switch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : String (self)
            switch0        : Boolean
            true           : String

        Fixed parameters
        ----------------
            input_type     : 'STRING'

        Returns
        -------
            String
        """

        return nodes.Switch(false=self, switch0=switch0, true=true, input_type='STRING').output

    def element(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : String (self)
            b              : String

        Fixed parameters
        ----------------
            data_type      : 'STRING'
            mode           : 'ELEMENT'
            operation      : 'ELEMENT'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT').result

    def length(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : String (self)
            b              : String

        Fixed parameters
        ----------------
            data_type      : 'STRING'
            mode           : 'ELEMENT'
            operation      : 'LENGTH'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH').result

    def average(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : String (self)
            b              : String

        Fixed parameters
        ----------------
            data_type      : 'STRING'
            mode           : 'ELEMENT'
            operation      : 'AVERAGE'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE').result

    def dot_product(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : String (self)
            b              : String

        Fixed parameters
        ----------------
            data_type      : 'STRING'
            mode           : 'ELEMENT'
            operation      : 'DOT_PRODUCT'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT').result

    def direction(self, b=None):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : String (self)
            b              : String

        Fixed parameters
        ----------------
            data_type      : 'STRING'
            mode           : 'ELEMENT'
            operation      : 'DIRECTION'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION').result

    def join(self, *strings, delimiter=None):
        """Call node JoinStrings (GeometryNodeStringJoin)

        Sockets arguments
        -----------------
            strings        : *String (self)
            delimiter      : String

        Returns
        -------
            String
        """

        return nodes.JoinStrings(self, *strings, delimiter=delimiter).string

    def slice(self, position=None, length=None):
        """Call node SliceString (FunctionNodeSliceString)

        Sockets arguments
        -----------------
            string         : String (self)
            position       : Integer
            length         : Integer

        Returns
        -------
            String
        """

        return nodes.SliceString(string=self, position=position, length=length).string

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """Call node StringToCurves (GeometryNodeStringToCurves)

        Sockets arguments
        -----------------
            string         : String (self)
            size           : Float
            character_spacing: Float
            word_spacing   : Float
            line_spacing   : Float
            text_box_width : Float
            text_box_height: Float

        Parameters arguments
        --------------------
            align_x        : 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
            align_y        : 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
            overflow       : 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
            pivot_mode     : 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]

        Returns
        -------
            Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
        """

        return nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def replace(self, find=None, replace=None):
        """Call node ReplaceString (FunctionNodeReplaceString)

        Sockets arguments
        -----------------
            string         : String (self)
            find           : String
            replace        : String

        Returns
        -------
            self

        """

        return self.stack(nodes.ReplaceString(string=self, find=find, replace=replace))


