import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Instances

class Instances(gn.Mesh):
    """ Data socket Instances

    Attributes
    ----------
        instance_index            : Integer   = capture_index(domain='INSTANCE')

    Methods
    -------
        to_points                 : points       (Points)

    Stacked methods
    ---------------
        rotate                    : Instances
        scale                     : Instances
        translate                 : Instances
    """

    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def instance_index(self):
        """Call node Index (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='INSTANCE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_points(self, selection=None, position=None, radius=None):
        """Call node InstancesToPoints (GeometryNodeInstancesToPoints)

        Sockets arguments
        -----------------
            instances      : Instances (self)
            selection      : Boolean
            position       : Vector
            radius         : Float

        Returns
        -------
            Points
        """

        return nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius).points


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """Call node RotateInstances (GeometryNodeRotateInstances)

        Sockets arguments
        -----------------
            instances      : Instances (self)
            selection      : Boolean
            rotation       : Vector
            pivot_point    : Vector
            local_space    : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        """Call node ScaleInstances (GeometryNodeScaleInstances)

        Sockets arguments
        -----------------
            instances      : Instances (self)
            selection      : Boolean
            scale          : Vector
            center         : Vector
            local_space    : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(self, selection=None, translation=None, local_space=None):
        """Call node TranslateInstances (GeometryNodeTranslateInstances)

        Sockets arguments
        -----------------
            instances      : Instances (self)
            selection      : Boolean
            translation    : Vector
            local_space    : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))


