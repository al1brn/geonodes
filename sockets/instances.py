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
# Data class Instances

class Instances(gn.Mesh):
    """ Socket data class Instances

    Attributes
    ----------
        capture_index        : Integer
        index                : Integer

    Methods
    -------
        to_points            : Points

    Stacked methods
    ---------------
        rotate               : Instances
        scale                : Instances
        translate            : Instances

    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    def capture_index(self, domain='INSTANCE'):
        """ Attribute capture_index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def index(self):
        """ Attribute index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_points(self, selection=None, position=None, radius=None):
        """ Method to_points using node NodeInstancestoPoints

        Arguments
        ---------
            instances       : Instances: self socket
            selection       : Boolean
            position        : Vector
            radius          : Float

        Returns
        -------
            Points
        """

        return nodes.NodeInstancestoPoints(instances=self, selection=selection, position=position, radius=radius).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ Stacked method rotate using node NodeRotateInstances

        Arguments
        ---------
            instances       : Instances: self socket
            selection       : Boolean
            rotation        : Vector
            pivot_point     : Vector
            local_space     : Boolean

        Returns
        -------
            Instances
        """

        return self.stack(nodes.NodeRotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        """ Stacked method scale using node NodeScaleInstances

        Arguments
        ---------
            instances       : Instances: self socket
            selection       : Boolean
            scale           : Vector
            center          : Vector
            local_space     : Boolean

        Returns
        -------
            Instances
        """

        return self.stack(nodes.NodeScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        """ Stacked method translate using node NodeTranslateInstances

        Arguments
        ---------
            instances       : Instances: self socket
            selection       : Boolean
            translation     : Vector
            local_space     : Boolean

        Returns
        -------
            Instances
        """

        return self.stack(nodes.NodeTranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))



