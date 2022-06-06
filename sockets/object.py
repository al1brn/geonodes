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
    Index 
    

    Properties
    ==========
    - **geometry** : ObjectInfo geometry (Geometry) = info.geometry 
    - **info**     : ObjectInfo Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    - **location** : ObjectInfo location (Vector) = info.location 
    - **rotation** : ObjectInfo rotation (Vector) = info.rotation 
    - **scale**    : ObjectInfo scale (Vector) = info.scale 
    

    Methods
    =======
    - **switch** : Switch output (Object) 
    """


    def reset_properties(self):
        self.info_ = None
        self.location_ = None
        self.rotation_ = None
        self.scale_ = None
        self.geometry_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """ info
        

        | Node: ObjectInfo 
        Top Index 
        

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

    @property
    def location(self, as_instance=None, transform_space='ORIGINAL'):
        """ location
        

        | Node: ObjectInfo 
        Top Index 
        

            v = object.location 
        

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
            - label:f"{self.node_chain_label}.location" 
        

        Node creation
        =============
        

            node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.location")
        

        Returns
        =======
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)] 
        """

        return self.info.location

    @property
    def rotation(self, as_instance=None, transform_space='ORIGINAL'):
        """ rotation
        

        | Node: ObjectInfo 
        Top Index 
        

            v = object.rotation 
        

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
            - label:f"{self.node_chain_label}.rotation" 
        

        Node creation
        =============
        

            node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.rotation")
        

        Returns
        =======
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)] 
        """

        return self.info.rotation

    @property
    def scale(self, as_instance=None, transform_space='ORIGINAL'):
        """ scale
        

        | Node: ObjectInfo 
        Top Index 
        

            v = object.scale 
        

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
            - label:f"{self.node_chain_label}.scale" 
        

        Node creation
        =============
        

            node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.scale")
        

        Returns
        =======
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)] 
        """

        return self.info.scale

    @property
    def geometry(self, as_instance=None, transform_space='ORIGINAL'):
        """ geometry
        

        | Node: ObjectInfo 
        Top Index 
        

            v = object.geometry 
        

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
            - label:f"{self.node_chain_label}.geometry" 
        

        Node creation
        =============
        

            node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.geometry")
        

        Returns
        =======
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)] 
        """

        return self.info.geometry


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ switch
        

        | Node: Switch 
        Top Index 
        

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


