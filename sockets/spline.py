import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Spline

class Spline(gn.Geometry):
    """ Data socket Spline

    Stacked methods
    ---------------
        set_cyclic           : Spline
        set_resolution       : Spline
    """

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


