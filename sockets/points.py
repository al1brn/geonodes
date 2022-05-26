import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Points

class Points(gn.Mesh):
    """ Data socket Points

    Methods
    -------
        instance_on_points   : instances (Geometry)
        to_vertices          : mesh (Geometry)
        to_volume            : volume (Geometry)
    Stacked methods
    ---------------
        set_radius           : Points
    """

    # ----------------------------------------------------------------------------------------------------
    # Methods

    def instance_on_points(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """Call node NodeInstanceOnPoints (GeometryNodeInstanceOnPoints)

        Sockets arguments
        -----------------
            points         : Geometry
            selection      : Boolean
            instance       : Geometry
            pick_instance  : Boolean
            instance_index : Integer
            rotation       : Vector
            scale          : Vector
        Returns
        -------
            Geometry
        """

        return nodes.NodeInstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances

    def to_vertices(points=None, selection=None):
        """Call node NodePointsToVertices (GeometryNodePointsToVertices)

        Sockets arguments
        -----------------
            points         : Geometry
            selection      : Boolean
        Returns
        -------
            Geometry
        """

        return nodes.NodePointsToVertices(points=points, selection=selection).mesh

    def to_volume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """Call node NodePointsToVolume (GeometryNodePointsToVolume)

        Sockets arguments
        -----------------
            points         : Geometry
            density        : Float
            voxel_size     : Float
            voxel_amount   : Float
            radius         : Float

        Parameters arguments
        --------------------
            resolution_mode: 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
        Returns
        -------
            Geometry
        """

        return nodes.NodePointsToVolume(points=points, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_radius(points=None, selection=None, radius=None):
        """Call node NodeSetPointRadius (GeometryNodeSetPointRadius)

        Sockets arguments
        -----------------
            points         : Geometry
            selection      : Boolean
            radius         : Float
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetPointRadius(points=points, selection=selection, radius=radius))


