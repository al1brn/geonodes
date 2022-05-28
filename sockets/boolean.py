import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Boolean

class Boolean(dsock.Boolean):
    """ Data socket Boolean

    Constructors
    ------------
        Random                    : value        (Boolean)

    Methods
    -------
        b_and                     : boolean      (Boolean)
        b_not                     : boolean      (Boolean)
        b_or                      : boolean      (Boolean)
        field_at_index            : value        (Boolean)
        imply                     : boolean      (Boolean)
        nand                      : boolean      (Boolean)
        nimply                    : boolean      (Boolean)
        nor                       : boolean      (Boolean)
        switch                    : output       (Boolean)
        xnor                      : boolean      (Boolean)
        xor                       : boolean      (Boolean)
    """

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        """Call node NodeRandomValue (FunctionNodeRandomValue)

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

        return cls(nodes.NodeRandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def b_and(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean

    def b_or(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean

    def b_not(self):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, operation='NOT').boolean

    def nand(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean

    def nor(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean

    def xnor(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean

    def xor(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean

    def imply(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean

    def nimply(self, boolean1=None):
        """Call node NodeBooleanMath (FunctionNodeBooleanMath)

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

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean

    def field_at_index(self, index=None, domain='POINT'):
        """Call node NodeFieldAtIndex (GeometryNodeFieldAtIndex)

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

        return nodes.NodeFieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain).value

    def switch(self, switch0=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Boolean (self)
            switch0        : Boolean
            true           : Boolean

        Fixed parameters
        ----------------
            input_type     : 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, true=true, input_type='BOOLEAN').output


