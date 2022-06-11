import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Volume

class Volume(gn.Geometry):
    """ 

    Data socket Volume
    ------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - to_mesh : VolumeToMesh, mesh (Mesh)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ > Node: VolumeToMesh
          
        <sub>go to: top index
        blender ref GeometryNodeVolumeToMesh
        node ref Volume to Mesh </sub>
        
        ```python
        v = volume.to_mesh(voxel_size, voxel_amount, threshold, adaptivity, resolution_mode)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - volume : Volume (self)
                - voxel_size : Float
                - voxel_amount : Float
                - threshold : Float
                - adaptivity : Float
    

            Parameters
            ----------
                - resolution_mode : 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]
    

        Node creation
        -------------
            ```python
            nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh


