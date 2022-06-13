import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Object

class Object(dsock.Object):
    """ 

    Data socket Object
    ------------------
        > Inherits from dsock.Object
          
        <sub>go to index</sub>
        
        
    

        Properties
        ----------
            - geometry : geometry (Geometry) = info.geometry
            - info : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
            - location : location (Vector) = info.location
            - rotation : rotation (Vector) = info.rotation
            - scale : scale (Vector) = info.scale
    

        Methods
        -------
            - switch : output (Object)
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
        """ > Node: ObjectInfo
          
        <sub>go to: top index
        blender ref GeometryNodeObjectInfo
        node ref Object Info </sub>
                                  
        ```python
        v = object.info
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - object : Object (self)
                    - as_instance : Boolean## Parameters
                    - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]## Fixed parameters
                    - label:f"{self.node_chain_label}.info"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
            ```
    

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
            
        """

        if self.info_ is None:
            self.info_ = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
        return self.info_

    @property
    def location(self, as_instance=None, transform_space='ORIGINAL'):
        """ > Node: ObjectInfo
          
        <sub>go to: top index
        blender ref GeometryNodeObjectInfo
        node ref Object Info </sub>
                                  
        ```python
        v = object.location
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - object : Object (self)
                    - as_instance : Boolean## Parameters
                    - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]## Fixed parameters
                    - label:f"{self.node_chain_label}.location"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.location")
            ```
    

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
            
        """

        return self.info.location

    @property
    def rotation(self, as_instance=None, transform_space='ORIGINAL'):
        """ > Node: ObjectInfo
          
        <sub>go to: top index
        blender ref GeometryNodeObjectInfo
        node ref Object Info </sub>
                                  
        ```python
        v = object.rotation
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - object : Object (self)
                    - as_instance : Boolean## Parameters
                    - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]## Fixed parameters
                    - label:f"{self.node_chain_label}.rotation"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.rotation")
            ```
    

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
            
        """

        return self.info.rotation

    @property
    def scale(self, as_instance=None, transform_space='ORIGINAL'):
        """ > Node: ObjectInfo
          
        <sub>go to: top index
        blender ref GeometryNodeObjectInfo
        node ref Object Info </sub>
                                  
        ```python
        v = object.scale
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - object : Object (self)
                    - as_instance : Boolean## Parameters
                    - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]## Fixed parameters
                    - label:f"{self.node_chain_label}.scale"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.scale")
            ```
    

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
            
        """

        return self.info.scale

    @property
    def geometry(self, as_instance=None, transform_space='ORIGINAL'):
        """ > Node: ObjectInfo
          
        <sub>go to: top index
        blender ref GeometryNodeObjectInfo
        node ref Object Info </sub>
                                  
        ```python
        v = object.geometry
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - object : Object (self)
                    - as_instance : Boolean## Parameters
                    - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]## Fixed parameters
                    - label:f"{self.node_chain_label}.geometry"
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.geometry")
            ```
    

        Returns
        -------
            Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
            
        """

        return self.info.geometry


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = object.switch(switch1, true)
        ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - false : Object (self)
                    - switch1 : Boolean
                    - true : Object## Fixed parameters
                    - input_type : 'OBJECT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT')
            ```
    

        Returns
        -------
            Object
            
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT').output


