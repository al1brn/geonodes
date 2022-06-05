import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Material

class Material(dsock.Material):
    """ Class Material
    

    | Inherits from: dsock.Material 
    

    Methods
    =======
    - selection : selection (Boolean) 
    - switch    : output (Material) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = material.switch(switch1, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Material (self) 
            - switch1 : Boolean 
            - true    : Material 
        

            Fixed parameters
            ----------------
            - input_type : 'MATERIAL' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='MATERIAL') 
        

        Returns
        =======
                Material 
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='MATERIAL').output

    def selection(self):
        """ selection
        

        | Node: MaterialSelection 
        

            v = material.selection() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - material : Material (self) 
        

        Node creation
        =============
        

            node = nodes.MaterialSelection(material=self) 
        

        Returns
        =======
                Boolean 
        """

        return nodes.MaterialSelection(material=self).selection


