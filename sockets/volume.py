import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Volume

class Volume(Geometry):
    """ Class Volume
    

    | Inherits from: Geometry 
    

    Methods
    =======
    - to_mesh : mesh (Mesh) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ to_mesh
        

        | Node: VolumeToMesh 
        

            v = volume.to_mesh(voxel_size, voxel_amount, threshold, adaptivity, resolution_mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - volume       : Volume (self) 
            - voxel_size   : Float 
            - voxel_amount : Float 
            - threshold    : Float 
            - adaptivity   : Float 
        

            Parameters arguments
            --------------------
            - resolution_mode : 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE] 
        

        Returns
        =======
                Mesh 
        """

        return nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh


