import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Volume

class Volume(gn.Mesh):
    """ Data socket Volume

    Methods
    -------
        to_mesh                   : mesh         (Geometry)
    """

    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """Call node NodeVolumeToMesh (GeometryNodeVolumeToMesh)

        Sockets arguments
        -----------------
            volume         : Geometry
            voxel_size     : Float
            voxel_amount   : Float
            threshold      : Float
            adaptivity     : Float

        Parameters arguments
        --------------------
            resolution_mode: 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]

        Returns
        -------
            Geometry
        """

        return nodes.NodeVolumeToMesh(volume=volume, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh


