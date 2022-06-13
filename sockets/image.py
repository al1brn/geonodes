import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Image

class Image(dsock.Image):
    """ 

    Data socket Image
    -----------------
        > Inherits from dsock.Image
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - switch : output (Image)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = image.switch(switch1, true)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Image (self)
            - switch1 : Boolean
            - true : Image## Fixed parameters
            - input_type : 'IMAGE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE')
            ```
    

        Returns
        -------
            Image
            
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE').output


