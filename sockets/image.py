import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Image

class Image(dsock.Image):
    """ Data socket Image

    Methods
    -------
        switch               : output (Image)
    """

    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch0=None, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Image (self)
            switch0        : Boolean
            switch1        : Boolean
            true           : Image

        Fixed parameters
        ----------------
            input_type     : 'IMAGE'

        Returns
        -------
            Image
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, switch1=switch1, true=true, input_type='IMAGE').output


