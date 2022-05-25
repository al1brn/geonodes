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
# Data class Material

class Material(bcls.Material):
    """ Socket data class Material

    Methods
    -------
        selection            : Boolean
        switch               : Material

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'MATERIAL'

        Returns
        -------
            Material
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='MATERIAL').output

    def selection(self):
        """ Method selection using node NodeMaterialSelection

        Arguments
        ---------
            material        : Material: self socket

        Returns
        -------
            Boolean
        """

        return nodes.NodeMaterialSelection(material=self).output



