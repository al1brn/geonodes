import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Material

class Material(dsock.Material):
    """ 

    Data socket Material
    --------------------
        > Inherits from dsock.Material
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - selection : selection (Boolean)
            - switch : output (Material)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch1=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
                ```python
                v = material.switch(switch1, true)
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - false : Material (self)
                    - switch1 : Boolean
                    - true : Material## Fixed parameters
                    - input_type : 'MATERIAL'
                      
                        Node creation
                        -------------
                                
                                ```python
                                from geondes import nodes
                                nodes.Switch(false=self, switch1=switch1, true=true, input_type='MATERIAL')
                                ```
    

        Returns
        -------
            Material
            
        """

        return nodes.Switch(false=self, switch1=switch1, true=true, input_type='MATERIAL').output

    def selection(self):
        """ > Node: MaterialSelection
          
        <sub>go to: top index
        blender ref GeometryNodeMaterialSelection
        node ref Material Selection </sub>
                                  
                ```python
                v = material.selection()
                ```
    

        Arguments
        ---------
    

            Sockets
            -------
                - material : Material (self)
                  
                    Node creation
                    -------------
                            
                            ```python
                            from geondes import nodes
                            nodes.MaterialSelection(material=self)
                            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.MaterialSelection(material=self).selection


