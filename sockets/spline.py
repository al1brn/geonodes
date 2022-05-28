import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Spline

class Spline(gn.Geometry):
    """ Data socket Spline

    Attribute captures
    ------------------
        capture_cyclic            : cyclic       (Boolean)
        capture_length            : Sockets      [length (Float), point_count (Integer)]
        capture_parameter         : Sockets      [factor (Float), length (Float), index (Integer)]
        capture_resolution        : resolution   (Integer)

    Attributes
    ----------
        cyclic                    : Boolean   = capture_cyclic(domain='CURVE')
        factor                    : Float     = capture_parameter(domain='CURVE').factor
        length                    : Float     = capture_length(domain='CURVE').length
        parameter_index           : Integer   = capture_parameter(domain='CURVE').index
        parameter_length          : Float     = capture_parameter(domain='CURVE').length
        point_count               : Integer   = capture_length(domain='CURVE').point_count
        resolution                : Integer   = capture_resolution(domain='CURVE')

    Stacked methods
    ---------------
        set_cyclic                : Spline
        set_resolution            : Spline
    """

    # ----------------------------------------------------------------------------------------------------
    # Attribute captures

    def capture_cyclic(self, domain='CURVE'):
        """Call node NodeIsSplineCyclic (GeometryNodeInputSplineCyclic)

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_cyclic_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeIsSplineCyclic()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).cyclic

    def capture_resolution(self, domain='CURVE'):
        """Call node NodeSplineResolution (GeometryNodeInputSplineResolution)

        Returns
        -------
            Integer
        """

        attr_name = 'capture_resolution_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeSplineResolution()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).resolution

    def capture_length(self, domain='CURVE'):
        """Call node NodeSplineLength (GeometryNodeSplineLength)

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
        """

        attr_name = 'capture_length_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeSplineLength()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)

    def capture_parameter(self, domain='CURVE'):
        """Call node NodeSplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        attr_name = 'capture_parameter_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeSplineParameter()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def cyclic(self):
        """Call node NodeIsSplineCyclic (GeometryNodeInputSplineCyclic)

        Returns
        -------
            Boolean
        """

        return self.capture_cyclic(domain='CURVE')

    @property
    def resolution(self):
        """Call node NodeSplineResolution (GeometryNodeInputSplineResolution)

        Returns
        -------
            Integer
        """

        return self.capture_resolution(domain='CURVE')

    @property
    def length(self):
        """Call node NodeSplineLength (GeometryNodeSplineLength)

        Returns
        -------
            Float
        """

        return self.capture_length(domain='CURVE').output_sockets[0]

    @property
    def point_count(self):
        """Call node NodeSplineLength (GeometryNodeSplineLength)

        Returns
        -------
            Integer
        """

        return self.capture_length(domain='CURVE').output_sockets[1]

    @property
    def factor(self):
        """Call node NodeSplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Float
        """

        return self.capture_parameter(domain='CURVE').output_sockets[0]

    @property
    def parameter_length(self):
        """Call node NodeSplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Float
        """

        return self.capture_parameter(domain='CURVE').output_sockets[1]

    @property
    def parameter_index(self):
        """Call node NodeSplineParameter (GeometryNodeSplineParameter)

        Returns
        -------
            Integer
        """

        return self.capture_parameter(domain='CURVE').output_sockets[2]


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_cyclic(geometry=None, selection=None, cyclic=None):
        """Call node NodeSetSplineCyclic (GeometryNodeSetSplineCyclic)

        Sockets arguments
        -----------------
            geometry       : Geometry
            selection      : Boolean
            cyclic         : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetSplineCyclic(geometry=geometry, selection=selection, cyclic=cyclic))

    def set_resolution(geometry=None, selection=None, resolution=None):
        """Call node NodeSetSplineResolution (GeometryNodeSetSplineResolution)

        Sockets arguments
        -----------------
            geometry       : Geometry
            selection      : Boolean
            resolution     : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetSplineResolution(geometry=geometry, selection=selection, resolution=resolution))


