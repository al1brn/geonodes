import geonodes as gn
from geonodes.core import socket as bcls
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ----------------------------------------------------------------------------------------------------
# Argument is a vector

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ----------------------------------------------------------------------------------------------------
# Sockets outputs

class Sockets(bcls.Sockets):
    pass


# ==============================================================================================================
# Data class String

class String(bcls.String):
    """ Socket data class String

    Properties
    ----------
        length               : Integer

    Methods
    -------
        join                 : String
        slice                : String
        switch               : String
        to_curves            : Sockets [curve_instances (Geometry), line (Integer), pivot_point (Vector)]

    Stacked methods
    ---------------
        replace              : String

    """


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def length(self):
        """ Property length using node NodeStringLength

        Arguments
        ---------
            string          : String: self socket

        Returns
        -------
            Integer
        """

        if not hasattr(self.top, 'length_'):
            self.top.length_ = nodes.NodeStringLength(string=self).output
        return self.top.length_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def join(self, *strings, delimiter=None):
        """ Method join using node NodeJoinStrings

        Arguments
        ---------
            strings         : String (multi input): self socket
            delimiter       : String

        Returns
        -------
            String
        """

        return nodes.NodeJoinStrings(self, *strings, delimiter=delimiter).output

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'STRING'

        Returns
        -------
            String
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='STRING').output

    def slice(self, position=None, length=None):
        """ Method slice using node NodeSliceString

        Arguments
        ---------
            string          : String: self socket
            position        : Integer
            length          : Integer

        Returns
        -------
            String
        """

        return nodes.NodeSliceString(string=self, position=position, length=length).output

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """ Method to_curves using node NodeStringtoCurves

        Arguments
        ---------
            string          : String: self socket
            size            : Float
            character_spacing : Float
            word_spacing    : Float
            line_spacing    : Float
            text_box_width  : Float
            text_box_height : Float

            align_x         : str
            align_y         : str
            overflow        : str
            pivot_mode      : str

        Returns
        -------
            Sockets [curve_instances (Geometry), line (Integer), pivot_point (Vector)]
        """

        return nodes.NodeStringtoCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def replace(self, find=None, replace=None):
        """ Stacked method replace using node NodeReplaceString

        Arguments
        ---------
            string          : String: self socket
            find            : String
            replace         : String

        Returns
        -------
            String
        """

        return self.stack(nodes.NodeReplaceString(string=self, find=find, replace=replace))



