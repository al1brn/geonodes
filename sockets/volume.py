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
# Data class Volume

class Volume(gn.Mesh):
    """ Socket data class Volume

    Methods
    -------
        to_mesh              : Mesh

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ Method to_mesh using node NodeVolumetoMesh

        Arguments
        ---------
            volume          : Volume: self socket
            voxel_size      : Float
            voxel_amount    : Float
            threshold       : Float
            adaptivity      : Float

            resolution_mode : str

        Returns
        -------
            Mesh
        """

        return nodes.NodeVolumetoMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).output



