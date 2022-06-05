import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Image

class Image(dsock.Image):
    """ Class Image
    

    | Inherits from: dsock.Image 
    

    Methods
    =======
    - switch : Switch output (Image) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = image.switch(switch1, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Image (self) 
            - switch1 : Boolean 
            - true    : Image 
        

            Fixed parameters
            ----------------
            - input_type : 'IMAGE' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE') 
        

        Returns
        =======
                Image 
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE').output


