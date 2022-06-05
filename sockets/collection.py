import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Collection

class Collection(dsock.Collection):
    """ Class Collection
    

    | Inherits from: dsock.Collection 
    

    Methods
    =======
    - **self.meth_name** : CollectionInfo geometry (Geometry) 
    - **self.meth_name** : Switch output (Collection) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = collection.switch(switch1, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Collection (self) 
            - switch1 : Boolean 
            - true    : Collection 
        

            Fixed parameters
            ----------------
            - input_type : 'COLLECTION' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='COLLECTION') 
        

        Returns
        =======
                Collection 
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='COLLECTION').output

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ info
        

        | Node: CollectionInfo 
        

            v = collection.info(separate_children, reset_children, transform_space) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - collection        : Collection (self) 
            - separate_children : Boolean 
            - reset_children    : Boolean 
        

            Parameters arguments
            --------------------
            - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE] 
        

        Node creation
        =============
        

            node = nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children,
            transform_space=transform_space) 
        

        Returns
        =======
                Geometry 
        """

        return nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry


