import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Collection

class Collection(dsock.Collection):
    """ 

    Data socket Collection
    ----------------------
        > Inherits from dsock.Collection
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - info : geometry (Geometry)
            - switch : output (Collection)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
        
        ```python
                v = collection.switch(switch1, true)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - false : Collection (self)
                    - switch1 : Boolean
                    - true : Collection## Fixed parameters
                    - input_type : 'COLLECTION'
    

        Node creation
        -------------
            ```python
                    from geondes import nodes
                    nodes.Switch(false=self, switch1=switch1, true=true, input_type='COLLECTION')
                    ```
    

        Returns
        -------
            Collection
            
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='COLLECTION').output

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """ > Node: CollectionInfo
          
        <sub>go to: top index
        blender ref GeometryNodeCollectionInfo
        node ref Collection Info </sub>
        
        ```python
                v = collection.info(separate_children, reset_children, transform_space)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - collection : Collection (self)
                    - separate_children : Boolean
                    - reset_children : Boolean## Parameters
                    - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]
    

        Node creation
        -------------
            ```python
                    from geondes import nodes
                    nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space)
                    ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry


