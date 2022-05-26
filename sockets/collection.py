import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Collection

class Collection(dsock.Collection):
    """ Data socket Collection

    Methods
    -------
        info                 : geometry (Geometry)
        switch               : output (Collection)
    """

    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch0=None, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Collection (self)
            switch0        : Boolean
            switch1        : Boolean
            true           : Collection

        Fixed parameters
        ----------------
            input_type     : 'COLLECTION'

        Returns
        -------
            Collection
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, switch1=switch1, true=true, input_type='COLLECTION').output

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """Call node NodeCollectionInfo (GeometryNodeCollectionInfo)

        Sockets arguments
        -----------------
            collection     : Collection (self)
            separate_children: Boolean
            reset_children : Boolean

        Parameters arguments
        --------------------
            transform_space: 'ORIGINAL' in [ORIGINAL, RELATIVE]
        Returns
        -------
            Geometry
        """

        return nodes.NodeCollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry


