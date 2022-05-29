import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Object

class Object(dsock.Object):
    """ Data socket Object

    Properties
    ----------
        info                      : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

    Methods
    -------
        switch                    : output       (Object)
    """

    def reset_properties(self):
        self.info_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """Call node ObjectInfo (GeometryNodeObjectInfo)

        Sockets arguments
        -----------------
            object         : Object (self)
            as_instance    : Boolean

        Parameters arguments
        --------------------
            transform_space: 'ORIGINAL' in [ORIGINAL, RELATIVE]

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
        """

        if self.info_ is None:
            self.info_ = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
        return self.info_


    @property
    def location(self):
        return self.info.location

    @property
    def rotation(self):
        return self.info.rotation

    @property
    def scale(self):
        return self.info.scale

    @property
    def geometry(self):
        return self.info.geometry


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """Call node Switch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Object (self)
            switch1        : Boolean
            true           : Object

        Fixed parameters
        ----------------
            input_type     : 'OBJECT'

        Returns
        -------
            Object
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT').output


