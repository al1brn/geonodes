import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Object

class Object(dsock.Object):
    """ Class Object
    

    | Inherits from: dsock.Object 
    

    Properties
    ==========
    - **self.meth_name** : ObjectInfo Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry
      (Geometry)] 
    

    Methods
    =======
    - **self.meth_name** : Switch output (Object) 
    """


    def reset_properties(self):
        self.info_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """ info
        

        | Node: ObjectInfo 
        

            v = object.info 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - object      : Object (self) 
            - as_instance : Boolean 
        

            Parameters arguments
            --------------------
            - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE] 
        

            Fixed parameters
            ----------------
            - label:f"{self.node_chain_label}.info" 
        

        Node creation
        =============
        

            node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
        

        Returns
        =======
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)] 
        """

        if self.info_ is None:
            self.info_ = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
        return self.info_


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = object.switch(switch1, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - false   : Object (self) 
            - switch1 : Boolean 
            - true    : Object 
        

            Fixed parameters
            ----------------
            - input_type : 'OBJECT' 
        

        Node creation
        =============
        

            node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT') 
        

        Returns
        =======
                Object 
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT').output


