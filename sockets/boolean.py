import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Boolean

class Boolean(dsock.Boolean):
    """ Class Boolean
    

    | Inherits from: dsock.Boolean 
    

    Constructors
    ============
    - Random : value (Boolean) 
    

    Methods
    =======
    - b_and              : boolean (Boolean) 
    - b_not              : boolean (Boolean) 
    - b_or               : boolean (Boolean) 
    - capture_attribute  : Sockets      [geometry (Geometry), attribute (Boolean)] 
    - field_at_index     : value (Boolean) 
    - imply              : boolean (Boolean) 
    - nand               : boolean (Boolean) 
    - nimply             : boolean (Boolean) 
    - nor                : boolean (Boolean) 
    - raycast            : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float),
      attribute (Boolean)] 
    - switch             : output (Boolean) 
    - transfer_attribute : attribute (Boolean) 
    - xnor               : boolean (Boolean) 
    - xor                : boolean (Boolean) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        """ Random
        

        | Node: RandomValue 
        

            v = Boolean.Random(probability, ID, seed) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - probability : Float 
            - ID          : Integer 
            - seed        : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'BOOLEAN' 
        

        Node creation
        =============
        

            node = nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN') 
        

        Returns
        =======
                Boolean 
        """

        return cls(nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """ transfer_attribute
        

        | Node: TransferAttribute 
        

            v = boolean.transfer_attribute(source, source_position, index, domain, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Boolean (self) 
            - source          : Geometry 
            - source_position : Vector 
            - index           : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'BOOLEAN' 
        

            Parameters arguments
            --------------------
            - domain  : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX] 
        

        Node creation
        =============
        

            node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index,
            data_type='BOOLEAN', domain=domain, mapping=mapping) 
        

        Returns
        =======
                Boolean 
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """ capture_attribute
        

        | Node: CaptureAttribute 
        

            v = boolean.capture_attribute(geometry, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value    : Boolean (self) 
            - geometry : Geometry 
        

            Fixed parameters
            ----------------
            - data_type : 'BOOLEAN' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain) 
        

        Returns
        =======
                Sockets [geometry (Geometry), attribute (Boolean)] 
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """ field_at_index
        

        | Node: FieldAtIndex 
        

            v = boolean.field_at_index(index, domain) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - value : Boolean (self) 
            - index : Integer 
        

            Fixed parameters
            ----------------
            - data_type : 'BOOLEAN' 
        

            Parameters arguments
            --------------------
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE] 
        

        Node creation
        =============
        

            node = nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain) 
        

        Returns
        =======
                Boolean 
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ raycast
        

        | Node: Raycast 
        

            v = boolean.raycast(target_geometry, source_position, ray_direction, ray_length, mapping) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - attribute       : Boolean (self) 
            - target_geometry : Geometry 
            - source_position : Vector 
            - ray_direction   : Vector 
            - ray_length      : Float 
        

            Fixed parameters
            ----------------
            - data_type : 'BOOLEAN' 
        

            Parameters arguments
            --------------------
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST] 
        

        Node creation
        =============
        

            node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position,
            ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping) 
        

        Returns
        =======
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute
                (Boolean)] 
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping)

    def switch(self, false=None, true=None):
        """ switch
        

        | Node: Switch 
        

            v = boolean.switch(false, true) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - switch0 : Boolean (self) 
            - false   : Boolean 
            - true    : Boolean 
        

            Fixed parameters
            ----------------
            - input_type : 'BOOLEAN' 
        

        Node creation
        =============
        

            node = nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN').output

    def b_and(self, boolean1=None):
        """ b_and
        

        | Node: BooleanMath 
        

            v = boolean.b_and(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'AND' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean

    def b_or(self, boolean1=None):
        """ b_or
        

        | Node: BooleanMath 
        

            v = boolean.b_or(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'OR' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean

    def b_not(self):
        """ b_not
        

        | Node: BooleanMath 
        

            v = boolean.b_not() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
        

            Fixed parameters
            ----------------
            - operation : 'NOT' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, operation='NOT') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, operation='NOT').boolean

    def nand(self, boolean1=None):
        """ nand
        

        | Node: BooleanMath 
        

            v = boolean.nand(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'NAND' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean

    def nor(self, boolean1=None):
        """ nor
        

        | Node: BooleanMath 
        

            v = boolean.nor(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'NOR' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean

    def xnor(self, boolean1=None):
        """ xnor
        

        | Node: BooleanMath 
        

            v = boolean.xnor(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'XNOR' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean

    def xor(self, boolean1=None):
        """ xor
        

        | Node: BooleanMath 
        

            v = boolean.xor(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'XOR' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean

    def imply(self, boolean1=None):
        """ imply
        

        | Node: BooleanMath 
        

            v = boolean.imply(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'IMPLY' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean

    def nimply(self, boolean1=None):
        """ nimply
        

        | Node: BooleanMath 
        

            v = boolean.nimply(boolean1) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - boolean0 : Boolean (self) 
            - boolean1 : Boolean 
        

            Fixed parameters
            ----------------
            - operation : 'NIMPLY' 
        

        Node creation
        =============
        

            node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY') 
        

        Returns
        =======
                Boolean 
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean


