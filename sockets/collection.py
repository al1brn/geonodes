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
# Data class Collection

class Collection(bcls.Collection):
    """ Socket data class Collection

    Methods
    -------
        info                 : Geometry
        switch               : Collection

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
            input_type      : node parameter set to 'COLLECTION'

        Returns
        -------
            Collection
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='COLLECTION').output

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ Method info using node NodeCollectionInfo

        Arguments
        ---------
            collection      : Collection: self socket
            separate_children : Boolean
            reset_children  : Boolean

            transform_space : str

        Returns
        -------
            Geometry
        """

        return nodes.NodeCollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).output



