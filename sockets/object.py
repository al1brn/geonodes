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
# Data class Object

class Object(bcls.Object):
    """ Socket data class Object

    Properties
    ----------
        info                 : Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

    Methods
    -------
        switch               : Object

    """


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """ Property info using node NodeObjectInfo

        Arguments
        ---------
            object          : Object: self socket
            as_instance     : Boolean

            transform_space : str

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
        """

        if not hasattr(self.top, 'info_'):
            self.top.info_ = nodes.NodeObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space).output
        return self.top.info_


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
            input_type      : node parameter set to 'OBJECT'

        Returns
        -------
            Object
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='OBJECT').output



