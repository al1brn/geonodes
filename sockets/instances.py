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
        to_points                 : points       (Geometry)

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
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='INSTANCE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_points(instances=None, selection=None, position=None, radius=None):
        """Call node NodeInstancesToPoints (GeometryNodeInstancesToPoints)

        Sockets arguments
        -----------------
            instances      : Geometry
            selection      : Boolean
            position       : Vector
            radius         : Float

        Returns
        -------
            Geometry
        """

        return nodes.NodeInstancesToPoints(instances=instances, selection=selection, position=position, radius=radius).points


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def rotate(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None):
        """Call node NodeRotateInstances (GeometryNodeRotateInstances)

        Sockets arguments
        -----------------
            instances      : Geometry
            selection      : Boolean
            rotation       : Vector
            pivot_point    : Vector
            local_space    : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeRotateInstances(instances=instances, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))

    def scale(instances=None, selection=None, scale=None, center=None, local_space=None):
        """Call node NodeScaleInstances (GeometryNodeScaleInstances)

        Sockets arguments
        -----------------
            instances      : Geometry
            selection      : Boolean
            scale          : Vector
            center         : Vector
            local_space    : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeScaleInstances(instances=instances, selection=selection, scale=scale, center=center, local_space=local_space))

    def translate(instances=None, selection=None, translation=None, local_space=None):
        """Call node NodeTranslateInstances (GeometryNodeTranslateInstances)

        Sockets arguments
        -----------------
            instances      : Geometry
            selection      : Boolean
            translation    : Vector
            local_space    : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeTranslateInstances(instances=instances, selection=selection, translation=translation, local_space=local_space))


