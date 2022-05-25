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
# Data class Points

class Points(gn.Mesh):
    """ Socket data class Points

    Methods
    -------
        instance_on_points   : Instances
        to_vertices          : Mesh
        to_volume            : Volume

    Stacked methods
    ---------------
        set_radius           : Points

    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Method instance_on_points using node NodeInstanceonPoints

        Arguments
        ---------
            points          : Points: self socket
            selection       : Boolean
            instance        : Geometry
            pick_instance   : Boolean
            instance_index  : Integer
            rotation        : Vector
            scale           : Vector

        Returns
        -------
            Instances
        """

        return nodes.NodeInstanceonPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).output

    def to_vertices(self, selection=None):
        """ Method to_vertices using node NodePointstoVertices

        Arguments
        ---------
            points          : Points: self socket
            selection       : Boolean

        Returns
        -------
            Mesh
        """

        return nodes.NodePointstoVertices(points=self, selection=selection).output

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ Method to_volume using node NodePointstoVolume

        Arguments
        ---------
            points          : Points: self socket
            density         : Float
            voxel_size      : Float
            voxel_amount    : Float
            radius          : Float

            resolution_mode : str

        Returns
        -------
            Volume
        """

        return nodes.NodePointstoVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_radius(self, selection=None, radius=None):
        """ Stacked method set_radius using node NodeSetPointRadius

        Arguments
        ---------
            points          : Points: self socket
            selection       : Boolean
            radius          : Float

        Returns
        -------
            Points
        """

        return self.stack(nodes.NodeSetPointRadius(points=self, selection=selection, radius=radius))



