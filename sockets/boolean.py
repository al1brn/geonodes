import geonodes as gn
from geonodes.core import socket as bcls
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ----------------------------------------------------------------------------------------------------
# Argument is a vector

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ----------------------------------------------------------------------------------------------------
# Sockets outputs

class Sockets(bcls.Sockets):
    pass


# ==============================================================================================================
# Data class Boolean

class Boolean(bcls.Boolean):
    """ Socket data class Boolean

    Constructors
    ------------
        Random               : Boolean

    Methods
    -------
        b_and                : Boolean
        b_not                : Boolean
        b_or                 : Boolean
        field_at_index       : Boolean
        imply                : Boolean
        nand                 : Boolean
        nimply               : Boolean
        nor                  : Boolean
        switch               : Boolean
        xnor                 : Boolean
        xor                  : Boolean

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        """ Constructor Random using node NodeRandomValue

        Arguments
        ---------
            probability     : Float
            ID              : Integer
            seed            : Integer

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.NodeRandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').output


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def b_and(self, boolean1=None):
        """ Method b_and using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'AND'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='AND').output

    def b_or(self, boolean1=None):
        """ Method b_or using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'OR'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='OR').output

    def b_not(self):
        """ Method b_not using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'NOT'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, operation='NOT').output

    def nand(self, boolean1=None):
        """ Method nand using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'NAND'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').output

    def nor(self, boolean1=None):
        """ Method nor using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'NOR'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').output

    def xnor(self, boolean1=None):
        """ Method xnor using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'XNOR'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').output

    def xor(self, boolean1=None):
        """ Method xor using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'XOR'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').output

    def imply(self, boolean1=None):
        """ Method imply using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'IMPLY'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').output

    def nimply(self, boolean1=None):
        """ Method nimply using node NodeBooleanMath

        Arguments
        ---------
            boolean0        : Boolean: self socket
            boolean1        : Boolean

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'NIMPLY'

        Returns
        -------
            Boolean
        """

        return nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').output

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index using node NodeFieldatIndex

        Arguments
        ---------
            value           : Float: self socket
            index           : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.NodeFieldatIndex(value=self, index=index, data_type='BOOLEAN', domain=domain).output

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'BOOLEAN'

        Returns
        -------
            Boolean
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='BOOLEAN').output



