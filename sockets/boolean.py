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
        """Call node RandomValue (FunctionNodeRandomValue)

        Sockets arguments
        -----------------
            probability    : Float
            ID             : Integer
            seed           : Integer

        Fixed parameters
        ----------------
            data_type      : 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return cls(nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            attribute      : Boolean (self)
            source         : Geometry
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """Call node CaptureAttribute (GeometryNodeCaptureAttribute)

        Sockets arguments
        -----------------
            value          : Boolean (self)
            geometry       : Geometry

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'BOOLEAN'

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Boolean)]
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """Call node FieldAtIndex (GeometryNodeFieldAtIndex)

        Sockets arguments
        -----------------
            value          : Boolean (self)
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """Call node Raycast (GeometryNodeRaycast)

        Sockets arguments
        -----------------
            attribute      : Boolean (self)
            target_geometry: Geometry
            source_position: Vector
            ray_direction  : Vector
            ray_length     : Float

        Parameters arguments
        --------------------
            mapping        : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

        Fixed parameters
        ----------------
            data_type      : 'BOOLEAN'

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping)

    def switch(self, false=None, true=None):
        """Call node Switch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            switch0        : Boolean (self)
            false          : Boolean
            true           : Boolean

        Fixed parameters
        ----------------
            input_type     : 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN').output

    def b_and(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'AND'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean

    def b_or(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'OR'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean

    def b_not(self):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)

        Fixed parameters
        ----------------
            operation      : 'NOT'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, operation='NOT').boolean

    def nand(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'NAND'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean

    def nor(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'NOR'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean

    def xnor(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'XNOR'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean

    def xor(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'XOR'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean

    def imply(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'IMPLY'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean

    def nimply(self, boolean1=None):
        """Call node BooleanMath (FunctionNodeBooleanMath)

        Sockets arguments
        -----------------
            boolean0       : Boolean (self)
            boolean1       : Boolean

        Fixed parameters
        ----------------
            operation      : 'NIMPLY'

        Returns
        -------
            Boolean
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean


