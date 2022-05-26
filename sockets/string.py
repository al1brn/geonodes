import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class String

class String(dsock.String):
    """ Data socket String

    Properties
    ----------
        length               : length (Integer)
    Methods
    -------
        join                 : string (String)
        slice                : string (String)
        switch               : output (String)
        to_curves            : Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
    Stacked methods
    ---------------
        replace              : String
    """

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def length(self):
        """Call node NodeStringLength (FunctionNodeStringLength)

        Sockets arguments
        -----------------
            string         : String (self)
        Returns
        -------
            Integer
        """

        if self.length_ is None:
            self.length_ = nodes.NodeStringLength(string=self).length
        return self.length_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def join(self, *strings, delimiter=None):
        """Call node NodeJoinStrings (GeometryNodeStringJoin)

        Sockets arguments
        -----------------
            strings        : *String (self)
            delimiter      : String
        Returns
        -------
            String
        """

        return nodes.NodeJoinStrings(self, *strings, delimiter=delimiter).string

    def switch(self, switch0=None, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : String (self)
            switch0        : Boolean
            switch1        : Boolean
            true           : String

        Fixed parameters
        ----------------
            input_type     : 'STRING'

        Returns
        -------
            String
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, switch1=switch1, true=true, input_type='STRING').output

    def slice(self, position=None, length=None):
        """Call node NodeSliceString (FunctionNodeSliceString)

        Sockets arguments
        -----------------
            string         : String (self)
            position       : Integer
            length         : Integer
        Returns
        -------
            String
        """

        return nodes.NodeSliceString(string=self, position=position, length=length).string

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """Call node NodeStringToCurves (GeometryNodeStringToCurves)

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

        return nodes.NodeStringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def replace(self, find=None, replace=None):
        """Call node NodeReplaceString (FunctionNodeReplaceString)

        Sockets arguments
        -----------------
            string         : String (self)
            find           : String
            replace        : String
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeReplaceString(string=self, find=find, replace=replace))


