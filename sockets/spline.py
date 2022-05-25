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
# Data class Spline

class Spline(gn.Geometry):
    """ Socket data class Spline

    Attributes
    ----------
        capture_cyclic       : Boolean
        capture_length       : Sockets [length (Float), point_count (Integer)]
        capture_parameter_factor : Sockets [factor (Float), length (Float), index (Integer)]
        capture_parameter_index : Sockets [factor (Float), length (Float), index (Integer)]
        capture_parameter_length : Sockets [factor (Float), length (Float), index (Integer)]
        capture_point_count  : Sockets [length (Float), point_count (Integer)]
        capture_resolution   : Integer
        cyclic               : Boolean
        length               : Sockets [length (Float), point_count (Integer)]
        parameter_factor     : Sockets [factor (Float), length (Float), index (Integer)]
        parameter_index      : Sockets [factor (Float), length (Float), index (Integer)]
        parameter_length     : Sockets [factor (Float), length (Float), index (Integer)]
        point_count          : Sockets [length (Float), point_count (Integer)]
        resolution           : Integer

    Stacked methods
    ---------------
        set_cyclic           : Spline
        set_resolution       : Spline

    """


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    def capture_cyclic(self, domain='CURVE'):
        """ Attribute capture_cyclic using node NodeIsSplineCyclic

        Arguments
        ---------

        Returns
        -------
            Boolean
        """

        return nodes.Attribute().output

    @property
    def cyclic(self):
        """ Attribute cyclic using node NodeIsSplineCyclic

        Arguments
        ---------

        Returns
        -------
            Boolean
        """

        return nodes.Attribute().output

    def capture_resolution(self, domain='CURVE'):
        """ Attribute capture_resolution using node NodeSplineResolution

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def resolution(self):
        """ Attribute resolution using node NodeSplineResolution

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    def capture_length(self, domain='CURVE'):
        """ Attribute capture_length using node NodeSplineLength

        Arguments
        ---------

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
        """

        return nodes.Attribute().output

    def length(self):
        """ Attribute length using node NodeSplineLength

        Arguments
        ---------

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_point_count(self, domain='CURVE'):
        """ Attribute capture_point_count using node NodeSplineLength

        Arguments
        ---------

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
        """

        return nodes.Attribute().output

    def point_count(self):
        """ Attribute point_count using node NodeSplineLength

        Arguments
        ---------

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
        """

        return nodes.Attribute().output

    def capture_parameter_factor(self, domain='CURVE'):
        """ Attribute capture_parameter_factor using node NodeSplineParameter

        Arguments
        ---------

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        return nodes.Attribute().output

    def parameter_factor(self):
        """ Attribute parameter_factor using node NodeSplineParameter

        Arguments
        ---------

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        return nodes.Attribute().output

    def capture_parameter_length(self, domain='CURVE'):
        """ Attribute capture_parameter_length using node NodeSplineParameter

        Arguments
        ---------

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        return nodes.Attribute().output

    def parameter_length(self):
        """ Attribute parameter_length using node NodeSplineParameter

        Arguments
        ---------

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        return nodes.Attribute().output

    def capture_parameter_index(self, domain='CURVE'):
        """ Attribute capture_parameter_index using node NodeSplineParameter

        Arguments
        ---------

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        return nodes.Attribute().output

    def parameter_index(self):
        """ Attribute parameter_index using node NodeSplineParameter

        Arguments
        ---------

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
        """

        return nodes.Attribute().output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_cyclic(self, selection=None, cyclic=None):
        """ Stacked method set_cyclic using node NodeSetSplineCyclic

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            cyclic          : Boolean

        Returns
        -------
            Spline
        """

        return self.stack(nodes.NodeSetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic))

    def set_resolution(self, selection=None, resolution=None):
        """ Stacked method set_resolution using node NodeSetSplineResolution

        Arguments
        ---------
            geometry        : Geometry: self socket
            selection       : Boolean
            resolution      : Integer

        Returns
        -------
            Spline
        """

        return self.stack(nodes.NodeSetSplineResolution(geometry=self, selection=selection, resolution=resolution))



