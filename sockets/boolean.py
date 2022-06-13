import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Boolean

class Boolean(dsock.Boolean):
    """ 

    Data socket Boolean
    -------------------
        > Inherits from dsock.Boolean
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Random : value (Boolean)
    

        Methods
        -------
            - b_and : boolean (Boolean)
            - b_not : boolean (Boolean)
            - b_or : boolean (Boolean)
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Boolean)]
            - field_at_index : value (Boolean)
            - imply : boolean (Boolean)
            - nand : boolean (Boolean)
            - nimply : boolean (Boolean)
            - nor : boolean (Boolean)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
            - switch : output (Boolean)
            - transfer_attribute : attribute (Boolean)
            - xnor : boolean (Boolean)
            - xor : boolean (Boolean)
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        """ > Node: RandomValue
          
        <sub>go to: top index
        blender ref FunctionNodeRandomValue
        node ref Random Value </sub>
                                  
        ```python
        v = Boolean.Random(probability, ID, seed)
        ```
    

        Arguments
        ---------
            ## Sockets
            - probability : Float
            - ID : Integer
            - seed : Integer## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return cls(nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = boolean.transfer_attribute(source, source_position, index, domain, mapping)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Boolean (self)
            - source : Geometry
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = boolean.capture_attribute(geometry, domain)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Boolean (self)
            - geometry : Geometry## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Boolean)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
                                  
        ```python
        v = boolean.field_at_index(index, domain)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Boolean (self)
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
                                  
        ```python
        v = boolean.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Boolean (self)
            - target_geometry : Geometry
            - source_position : Vector
            - ray_direction : Vector
            - ray_length : Float## Parameters
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping)
            ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping)

    def switch(self, false=None, true=None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = boolean.switch(false, true)
        ```
    

        Arguments
        ---------
            ## Sockets
            - switch0 : Boolean (self)
            - false : Boolean
            - true : Boolean## Fixed parameters
            - input_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN').output

    def b_and(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.b_and(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'AND'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean

    def b_or(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.b_or(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'OR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean

    def b_not(self):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.b_not()
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)## Fixed parameters
            - operation : 'NOT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, operation='NOT')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, operation='NOT').boolean

    def nand(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.nand(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'NAND'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean

    def nor(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.nor(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'NOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean

    def xnor(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.xnor(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'XNOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean

    def xor(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.xor(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'XOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean

    def imply(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.imply(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'IMPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean

    def nimply(self, boolean1=None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.nimply(boolean1)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Fixed parameters
            - operation : 'NIMPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY')
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean


