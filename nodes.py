from .basenode import Socket, SocketIn, Sockets, Node, Attribute

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeAlignEulerToVector

class NodeAlignEulertoVector(Node):

    """ Node class FunctionNodeAlignEulerToVector

    Input sockets
    -------------

        0: rotation             Vector
        1: factor               Float
        2: vector               Vector

    Parameters
    ----------

        axis        : 'X' in ('X', 'Y', 'Z') 
        pivot_axis  : 'AUTO' in ('AUTO', 'X', 'Y', 'Z') 

    Output sockets
    --------------

        0: rotation             Vector

    """

    PARAMETERS = ['axis', 'pivot_axis']

    def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

        super().__init__('FunctionNodeAlignEulerToVector', name='Align Euler to Vector')

        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotation'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'factor'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))

        self.outputs.add(Socket (self, 'NodeSocketVectorEuler'  , 'rotation'     ))

        self.socket_out_name = 'rotation'

        # ----- Parameters

        self.axis            = axis
        self.pivot_axis      = pivot_axis
        self.check_parameters()

        # ----- Input sockets

        self.irotation       = rotation
        self.ifactor         = factor
        self.ivector         = vector

        self.socket_in_name = 'irotation'

    def __repr__(self):
        s = f"Node 'AlignEulertoVector' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   rotation        : {self.irotation}"
        s += f"\n   factor          : {self.ifactor}"
        s += f"\n   vector          : {self.ivector}"
        s += '\nParameters'
        s += f"\n   axis            : {self.axis}"
        s += f"\n   pivot_axis      : {self.pivot_axis}"
        s += '\nOutput sockets'
        s +=  "\n   rotation        : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('X', 'Y', 'Z') 
        if self.axis not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeAlignEulertoVector'.\n 'axis' is '{self.axis}'.\n Authorized values are {valids}.")
        valids = ('AUTO', 'X', 'Y', 'Z') 
        if self.pivot_axis not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeAlignEulertoVector'.\n 'pivot_axis' is '{self.pivot_axis}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def rotation(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def irotation(self):
        return self.inputs[0]

    @irotation.setter
    def irotation(self, value):
        self.inputs[0].plug(value)

    @property
    def ifactor(self):
        return self.inputs[1]

    @ifactor.setter
    def ifactor(self, value):
        self.inputs[1].plug(value)

    @property
    def ivector(self):
        return self.inputs[2]

    @ivector.setter
    def ivector(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeBooleanMath

class NodeBooleanMath(Node):

    """ Node class FunctionNodeBooleanMath

    Input sockets
    -------------

        0: boolean0             Boolean
        1: boolean1             Boolean

    Parameters
    ----------

        operation   : 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY') 

    Output sockets
    --------------

        0: boolean              Boolean

    """

    PARAMETERS = ['operation']

    def __init__(self, boolean0=None, boolean1=None, operation='AND'):

        super().__init__('FunctionNodeBooleanMath', name='Boolean Math')

        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'boolean0'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'boolean1'     ))

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'boolean'      ))

        self.socket_out_name = 'boolean'

        # ----- Parameters

        self.operation       = operation
        self.check_parameters()

        # ----- Input sockets

        self.iboolean0       = boolean0
        self.iboolean1       = boolean1

        self.socket_in_name = 'iboolean0'

    def __repr__(self):
        s = f"Node 'BooleanMath' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   boolean0        : {self.iboolean0}"
        s += f"\n   boolean1        : {self.iboolean1}"
        s += '\nParameters'
        s += f"\n   operation       : {self.operation}"
        s += '\nOutput sockets'
        s +=  "\n   boolean         : Boolean"
        return s + "\n"

    def check_parameters(self):
        valids = ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY') 
        if self.operation not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeBooleanMath'.\n 'operation' is '{self.operation}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def boolean(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iboolean0(self):
        return self.inputs[0]

    @iboolean0.setter
    def iboolean0(self, value):
        self.inputs[0].plug(value)

    @property
    def iboolean1(self):
        return self.inputs[1]

    @iboolean1.setter
    def iboolean1(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeCompare

class NodeCompare(Node):

    """ Node class FunctionNodeCompare

    Input sockets
    -------------

        0: a                    Float
        1: b                    Float
        2: a                    Integer
        3: b                    Integer
        4: a                    Vector
        5: b                    Vector
        6: a                    Color
        7: b                    Color
        8: a                    String
        9: b                    String
        10: c                    Float
        11: angle                Float
        12: epsilon              Float

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA') 
        mode        : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION') 
        operation   : 'EQUAL' in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL') 

    Output sockets
    --------------

        0: result               Boolean

    """

    PARAMETERS = ['data_type', 'mode', 'operation']

    def __init__(self, a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='EQUAL'):

        super().__init__('FunctionNodeCompare', name='Compare')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'a'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'b'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'a'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'b'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'a'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'b'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'a'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'b'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'a'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'b'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'c'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'angle'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'epsilon'      ))

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'result'       ))

        self.socket_out_name = 'result'

        # ----- Parameters

        self.data_type       = data_type
        self.mode            = mode
        self.operation       = operation
        self.check_parameters()

        # ----- Input sockets

        self.ia              = a
        self.ib              = b
        self.ic              = c
        self.iangle          = angle
        self.iepsilon        = epsilon

        self.socket_in_name = 'ia'

    def __repr__(self):
        s = f"Node 'Compare' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   a               : {self.ia}"
        s += f"\n   b               : {self.ib}"
        s += f"\n   c               : {self.ic}"
        s += f"\n   angle           : {self.iangle}"
        s += f"\n   epsilon         : {self.iepsilon}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   mode            : {self.mode}"
        s += f"\n   operation       : {self.operation}"
        s += '\nOutput sockets'
        s +=  "\n   result          : Boolean"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCompare'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCompare'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")
        valids = ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL') 
        if self.operation not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCompare'.\n 'operation' is '{self.operation}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def result(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ia(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[0]
        elif (self.data_type == 'INT'):
            return self.inputs[2]
        elif (self.data_type == 'VECTOR'):
            return self.inputs[4]
        elif (self.data_type == 'RGBA'):
            return self.inputs[6]
        elif (self.data_type == 'STRING'):
            return self.inputs[8]

    @ia.setter
    def ia(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[0].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'VECTOR'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'RGBA'):
            self.inputs[6].plug(value)
        elif (self.data_type == 'STRING'):
            self.inputs[8].plug(value)

    @property
    def ib(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[1]
        elif (self.data_type == 'INT'):
            return self.inputs[3]
        elif (self.data_type == 'VECTOR'):
            return self.inputs[5]
        elif (self.data_type == 'RGBA'):
            return self.inputs[7]
        elif (self.data_type == 'STRING'):
            return self.inputs[9]

    @ib.setter
    def ib(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'VECTOR'):
            self.inputs[5].plug(value)
        elif (self.data_type == 'RGBA'):
            self.inputs[7].plug(value)
        elif (self.data_type == 'STRING'):
            self.inputs[9].plug(value)

    @property
    def ic(self):
        return self.inputs[10]

    @ic.setter
    def ic(self, value):
        self.inputs[10].plug(value)

    @property
    def iangle(self):
        return self.inputs[11]

    @iangle.setter
    def iangle(self, value):
        self.inputs[11].plug(value)

    @property
    def iepsilon(self):
        return self.inputs[12]

    @iepsilon.setter
    def iepsilon(self, value):
        self.inputs[12].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeFloatToInt

class NodeFloattoInteger(Node):

    """ Node class FunctionNodeFloatToInt

    Input sockets
    -------------

        0: float                Float

    Parameters
    ----------

        rounding_mode: 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE') 

    Output sockets
    --------------

        0: integer              Integer

    """

    PARAMETERS = ['rounding_mode']

    def __init__(self, float=None, rounding_mode='ROUND'):

        super().__init__('FunctionNodeFloatToInt', name='Float to Integer')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'float'        ))

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'integer'      ))

        self.socket_out_name = 'integer'

        # ----- Parameters

        self.rounding_mode   = rounding_mode
        self.check_parameters()

        # ----- Input sockets

        self.ifloat          = float

        self.socket_in_name = 'ifloat'

    def __repr__(self):
        s = f"Node 'FloattoInteger' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   float           : {self.ifloat}"
        s += '\nParameters'
        s += f"\n   rounding_mode   : {self.rounding_mode}"
        s += '\nOutput sockets'
        s +=  "\n   integer         : Integer"
        return s + "\n"

    def check_parameters(self):
        valids = ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE') 
        if self.rounding_mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeFloattoInteger'.\n 'rounding_mode' is '{self.rounding_mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def integer(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ifloat(self):
        return self.inputs[0]

    @ifloat.setter
    def ifloat(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeInputBool

class NodeBoolean(Node):

    """ Node class FunctionNodeInputBool

    Parameters
    ----------

        boolean_    : False

    Output sockets
    --------------

        0: boolean              Boolean

    """

    PARAMETERS = ['boolean_']

    def __init__(self, boolean=False):

        super().__init__('FunctionNodeInputBool', name='Boolean')

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'boolean'      ))

        self.socket_out_name = 'boolean'

        # ----- Parameters

        self.boolean_        = boolean
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Boolean' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   boolean         : {self.boolean}"
        s += '\nOutput sockets'
        s +=  "\n   boolean         : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def boolean(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeInputColor

class NodeColor(Node):

    """ Node class FunctionNodeInputColor

    Output sockets
    --------------

        0: color                Color

    """

    PARAMETERS = []

    def __init__(self):

        super().__init__('FunctionNodeInputColor', name='Color')

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))

        self.socket_out_name = 'color'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Color' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeInputInt

class NodeInteger(Node):

    """ Node class FunctionNodeInputInt

    Parameters
    ----------

        integer_    : 0

    Output sockets
    --------------

        0: integer              Integer

    """

    PARAMETERS = ['integer_']

    def __init__(self, integer=0):

        super().__init__('FunctionNodeInputInt', name='Integer')

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'integer'      ))

        self.socket_out_name = 'integer'

        # ----- Parameters

        self.integer_        = integer
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Integer' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   integer         : {self.integer}"
        s += '\nOutput sockets'
        s +=  "\n   integer         : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def integer(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeInputSpecialCharacters

class NodeSpecialCharacters(Node):

    """ Node class FunctionNodeInputSpecialCharacters

    Output sockets
    --------------

        0: line_break           String
        1: tab                  String

    """

    PARAMETERS = []

    def __init__(self):

        super().__init__('FunctionNodeInputSpecialCharacters', name='Special Characters')

        self.outputs.add(Socket (self, 'NodeSocketString'       , 'line_break'   ))
        self.outputs.add(Socket (self, 'NodeSocketString'       , 'tab'          ))

        self.socket_out_name = 'line_break'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'SpecialCharacters' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   line_break      : String"
        s +=  "\n   tab             : String"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def line_break(self):
        return self.outputs[0]

    @property
    def tab(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeInputString

class NodeString(Node):

    """ Node class FunctionNodeInputString

    Parameters
    ----------

        string_     : ''

    Output sockets
    --------------

        0: string               String

    """

    PARAMETERS = ['string_']

    def __init__(self, string=''):

        super().__init__('FunctionNodeInputString', name='String')

        self.outputs.add(Socket (self, 'NodeSocketString'       , 'string'       ))

        self.socket_out_name = 'string'

        # ----- Parameters

        self.string_         = string
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'String' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   string          : {self.string}"
        s += '\nOutput sockets'
        s +=  "\n   string          : String"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def string(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeInputVector

class NodeVector(Node):

    """ Node class FunctionNodeInputVector

    Parameters
    ----------

        vector_     : <Vector (0.0000, 0.0000, 0.0000)>

    Output sockets
    --------------

        0: vector               Vector

    """

    PARAMETERS = ['vector_']

    def __init__(self, vector=(0.0, 0.0, 0.0)):

        super().__init__('FunctionNodeInputVector', name='Vector')

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'vector'       ))

        self.socket_out_name = 'vector'

        # ----- Parameters

        self.vector_         = vector
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Vector' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   vector          : {self.vector}"
        s += '\nOutput sockets'
        s +=  "\n   vector          : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vector(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeRandomValue

class NodeRandomValue(Node):

    """ Node class FunctionNodeRandomValue

    Input sockets
    -------------

        0: min                  Vector
        1: max                  Vector
        2: min                  Float
        3: max                  Float
        4: min                  Integer
        5: max                  Integer
        6: probability          Float
        7: ID                   Integer
        8: seed                 Integer

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN') 

    Output sockets
    --------------

        0: value                Vector
        1: value                Float
        2: value                Integer
        3: value                Boolean

    """

    PARAMETERS = ['data_type']

    def __init__(self, min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT'):

        super().__init__('FunctionNodeRandomValue', name='Random Value')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'min'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'max'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'min'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'max'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'min'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'max'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'probability'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'ID'           ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'seed'         ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'value'        ))

        self.socket_out_name = 'value'

        # ----- Parameters

        self.data_type       = data_type
        self.check_parameters()

        # ----- Input sockets

        self.imin            = min
        self.imax            = max
        self.iprobability    = probability
        self.iID             = ID
        self.iseed           = seed

        self.socket_in_name = 'imin'

    def __repr__(self):
        s = f"Node 'RandomValue' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   min             : {self.imin}"
        s += f"\n   max             : {self.imax}"
        s += f"\n   probability     : {self.iprobability}"
        s += f"\n   ID              : {self.iID}"
        s += f"\n   seed            : {self.iseed}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += '\nOutput sockets'
        s +=  "\n   value           : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeRandomValue'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def value(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[0]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[1]
        elif (self.data_type == 'INT'):
            return self.outputs[2]
        elif (self.data_type == 'BOOLEAN'):
            return self.outputs[3]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imin(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[0]
        elif (self.data_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.data_type == 'INT'):
            return self.inputs[4]

    @imin.setter
    def imin(self, value):
        if (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[0].plug(value)
        elif (self.data_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[4].plug(value)

    @property
    def imax(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[1]
        elif (self.data_type == 'FLOAT'):
            return self.inputs[3]
        elif (self.data_type == 'INT'):
            return self.inputs[5]

    @imax.setter
    def imax(self, value):
        if (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'FLOAT'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[5].plug(value)

    @property
    def iprobability(self):
        return self.inputs[6]

    @iprobability.setter
    def iprobability(self, value):
        self.inputs[6].plug(value)

    @property
    def iID(self):
        return self.inputs[7]

    @iID.setter
    def iID(self, value):
        self.inputs[7].plug(value)

    @property
    def iseed(self):
        return self.inputs[8]

    @iseed.setter
    def iseed(self, value):
        self.inputs[8].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeReplaceString

class NodeReplaceString(Node):

    """ Node class FunctionNodeReplaceString

    Input sockets
    -------------

        0: string               String
        1: find                 String
        2: replace              String

    Output sockets
    --------------

        0: string               String

    """

    PARAMETERS = []

    def __init__(self, string=None, find=None, replace=None):

        super().__init__('FunctionNodeReplaceString', name='Replace String')

        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'string'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'find'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'replace'      ))

        self.outputs.add(Socket (self, 'NodeSocketString'       , 'string'       ))

        self.socket_out_name = 'string'

        # ----- Input sockets

        self.istring         = string
        self.ifind           = find
        self.ireplace        = replace

        self.socket_in_name = 'istring'

    def __repr__(self):
        s = f"Node 'ReplaceString' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   string          : {self.istring}"
        s += f"\n   find            : {self.ifind}"
        s += f"\n   replace         : {self.ireplace}"
        s += '\nOutput sockets'
        s +=  "\n   string          : String"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def string(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def istring(self):
        return self.inputs[0]

    @istring.setter
    def istring(self, value):
        self.inputs[0].plug(value)

    @property
    def ifind(self):
        return self.inputs[1]

    @ifind.setter
    def ifind(self, value):
        self.inputs[1].plug(value)

    @property
    def ireplace(self):
        return self.inputs[2]

    @ireplace.setter
    def ireplace(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeRotateEuler

class NodeRotateEuler(Node):

    """ Node class FunctionNodeRotateEuler

    Input sockets
    -------------

        0: rotation             Vector
        1: rotate_by            Vector
        2: axis                 Vector
        3: angle                Float

    Parameters
    ----------

        space       : 'OBJECT' in ('OBJECT', 'LOCAL') 

    Output sockets
    --------------

        0: rotation             Vector

    """

    PARAMETERS = ['space']

    def __init__(self, rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT'):

        super().__init__('FunctionNodeRotateEuler', name='Rotate Euler')

        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotation'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotate_by'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorXYZ'    , 'axis'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'angle'        ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'rotation'     ))

        self.socket_out_name = 'rotation'

        # ----- Parameters

        self.space           = space
        self.check_parameters()

        # ----- Input sockets

        self.irotation       = rotation
        self.irotate_by      = rotate_by
        self.iaxis           = axis
        self.iangle          = angle

        self.socket_in_name = 'irotation'

    def __repr__(self):
        s = f"Node 'RotateEuler' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   rotation        : {self.irotation}"
        s += f"\n   rotate_by       : {self.irotate_by}"
        s += f"\n   axis            : {self.iaxis}"
        s += f"\n   angle           : {self.iangle}"
        s += '\nParameters'
        s += f"\n   space           : {self.space}"
        s += '\nOutput sockets'
        s +=  "\n   rotation        : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('OBJECT', 'LOCAL') 
        if self.space not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeRotateEuler'.\n 'space' is '{self.space}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def rotation(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def irotation(self):
        return self.inputs[0]

    @irotation.setter
    def irotation(self, value):
        self.inputs[0].plug(value)

    @property
    def irotate_by(self):
        return self.inputs[1]

    @irotate_by.setter
    def irotate_by(self, value):
        self.inputs[1].plug(value)

    @property
    def iaxis(self):
        return self.inputs[2]

    @iaxis.setter
    def iaxis(self, value):
        self.inputs[2].plug(value)

    @property
    def iangle(self):
        return self.inputs[3]

    @iangle.setter
    def iangle(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeSliceString

class NodeSliceString(Node):

    """ Node class FunctionNodeSliceString

    Input sockets
    -------------

        0: string               String
        1: position             Integer
        2: length               Integer

    Output sockets
    --------------

        0: string               String

    """

    PARAMETERS = []

    def __init__(self, string=None, position=None, length=None):

        super().__init__('FunctionNodeSliceString', name='Slice String')

        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'string'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'position'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'length'       ))

        self.outputs.add(Socket (self, 'NodeSocketString'       , 'string'       ))

        self.socket_out_name = 'string'

        # ----- Input sockets

        self.istring         = string
        self.iposition       = position
        self.ilength         = length

        self.socket_in_name = 'istring'

    def __repr__(self):
        s = f"Node 'SliceString' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   string          : {self.istring}"
        s += f"\n   position        : {self.iposition}"
        s += f"\n   length          : {self.ilength}"
        s += '\nOutput sockets'
        s +=  "\n   string          : String"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def string(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def istring(self):
        return self.inputs[0]

    @istring.setter
    def istring(self, value):
        self.inputs[0].plug(value)

    @property
    def iposition(self):
        return self.inputs[1]

    @iposition.setter
    def iposition(self, value):
        self.inputs[1].plug(value)

    @property
    def ilength(self):
        return self.inputs[2]

    @ilength.setter
    def ilength(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeStringLength

class NodeStringLength(Node):

    """ Node class FunctionNodeStringLength

    Input sockets
    -------------

        0: string               String

    Output sockets
    --------------

        0: length               Integer

    """

    PARAMETERS = []

    def __init__(self, string=None):

        super().__init__('FunctionNodeStringLength', name='String Length')

        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'string'       ))

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'length'       ))

        self.socket_out_name = 'length'

        # ----- Input sockets

        self.istring         = string

        self.socket_in_name = 'istring'

    def __repr__(self):
        s = f"Node 'StringLength' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   string          : {self.istring}"
        s += '\nOutput sockets'
        s +=  "\n   length          : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def length(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def istring(self):
        return self.inputs[0]

    @istring.setter
    def istring(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class FunctionNodeValueToString

class NodeValuetoString(Node):

    """ Node class FunctionNodeValueToString

    Input sockets
    -------------

        0: value                Float
        1: decimals             Integer

    Output sockets
    --------------

        0: string               String

    """

    PARAMETERS = []

    def __init__(self, value=None, decimals=None):

        super().__init__('FunctionNodeValueToString', name='Value to String')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'decimals'     ))

        self.outputs.add(Socket (self, 'NodeSocketString'       , 'string'       ))

        self.socket_out_name = 'string'

        # ----- Input sockets

        self.ivalue          = value
        self.idecimals       = decimals

        self.socket_in_name = 'ivalue'

    def __repr__(self):
        s = f"Node 'ValuetoString' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   value           : {self.ivalue}"
        s += f"\n   decimals        : {self.idecimals}"
        s += '\nOutput sockets'
        s +=  "\n   string          : String"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def string(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivalue(self):
        return self.inputs[0]

    @ivalue.setter
    def ivalue(self, value):
        self.inputs[0].plug(value)

    @property
    def idecimals(self):
        return self.inputs[1]

    @idecimals.setter
    def idecimals(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeAccumulateField

class NodeAccumulateField(Node):

    """ Node class GeometryNodeAccumulateField

    Input sockets
    -------------

        0: value                Vector
        1: value                Float
        2: value                Integer
        3: group_index          Integer

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR') 
        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 

    Output sockets
    --------------

        0: leading              Vector
        1: leading              Float
        2: leading              Integer
        3: trailing             Vector
        4: trailing             Float
        5: trailing             Integer
        6: total                Vector
        7: total                Float
        8: total                Integer

    """

    PARAMETERS = ['data_type', 'domain']

    def __init__(self, value=None, group_index=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeAccumulateField', name='Accumulate Field')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'group_index'  ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'leading'      ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'leading'      ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'leading'      ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'trailing'     ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'trailing'     ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'trailing'     ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'total'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'total'        ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'total'        ))

        self.socket_out_name = 'leading'

        # ----- Parameters

        self.data_type       = data_type
        self.domain          = domain
        self.check_parameters()

        # ----- Input sockets

        self.ivalue          = value
        self.igroup_index    = group_index

        self.socket_in_name = 'ivalue'

    def __repr__(self):
        s = f"Node 'AccumulateField' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   value           : {self.ivalue}"
        s += f"\n   group_index     : {self.igroup_index}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   domain          : {self.domain}"
        s += '\nOutput sockets'
        s +=  "\n   leading         : variable"
        s +=  "\n   trailing        : variable"
        s +=  "\n   total           : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeAccumulateField'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeAccumulateField'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def leading(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[0]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[1]
        elif (self.data_type == 'INT'):
            return self.outputs[2]
        self.check_parameters()

    @property
    def trailing(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[3]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[4]
        elif (self.data_type == 'INT'):
            return self.outputs[5]
        self.check_parameters()

    @property
    def total(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[6]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[7]
        elif (self.data_type == 'INT'):
            return self.outputs[8]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivalue(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[0]
        elif (self.data_type == 'FLOAT'):
            return self.inputs[1]
        elif (self.data_type == 'INT'):
            return self.inputs[2]

    @ivalue.setter
    def ivalue(self, value):
        if (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[0].plug(value)
        elif (self.data_type == 'FLOAT'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[2].plug(value)

    @property
    def igroup_index(self):
        return self.inputs[3]

    @igroup_index.setter
    def igroup_index(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeAttributeDomainSize

class NodeDomainSize(Node):

    """ Node class GeometryNodeAttributeDomainSize

    Input sockets
    -------------

        0: geometry             Geometry

    Parameters
    ----------

        component   : 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES') 

    Output sockets
    --------------

        0: point_count          Integer
        1: edge_count           Integer
        2: face_count           Integer
        3: face_corner_count    Integer
        4: spline_count         Integer
        5: instance_count       Integer

    """

    PARAMETERS = ['component']

    def __init__(self, geometry=None, component='MESH'):

        super().__init__('GeometryNodeAttributeDomainSize', name='Domain Size')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'point_count'  ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'edge_count'   ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'face_count'   ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'face_corner_count'))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'spline_count' ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'instance_count'))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'point_count'

        # ----- Parameters

        self.component       = component
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'DomainSize' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nParameters'
        s += f"\n   component       : {self.component}"
        s += '\nOutput sockets'
        s +=  "\n   point_count     : Integer"
        s +=  "\n   edge_count      : Integer"
        s +=  "\n   face_count      : Integer"
        s +=  "\n   face_corner_count : Integer"
        s +=  "\n   spline_count    : Integer"
        s +=  "\n   instance_count  : Integer"
        return s + "\n"

    def check_parameters(self):
        valids = ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES') 
        if self.component not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeDomainSize'.\n 'component' is '{self.component}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def point_count(self):
        return self.outputs[0]

    @property
    def edge_count(self):
        return self.outputs[1]

    @property
    def face_count(self):
        return self.outputs[2]

    @property
    def face_corner_count(self):
        return self.outputs[3]

    @property
    def spline_count(self):
        return self.outputs[4]

    @property
    def instance_count(self):
        return self.outputs[5]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeAttributeRemove

class NodeAttributeRemove(Node):

    """ Node class GeometryNodeAttributeRemove

    Input sockets
    -------------

        0: geometry             Geometry
        1: attribute            String

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, *attribute, geometry=None):

        super().__init__('GeometryNodeAttributeRemove', name='Attribute Remove')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'attribute'    , is_multi_input=True))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iattribute      = attribute

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'AttributeRemove' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   attribute       : {self.iattribute}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iattribute(self):
        return self.inputs[1]

    @iattribute.setter
    def iattribute(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeAttributeStatistic

class NodeAttributeStatistic(Node):

    """ Node class GeometryNodeAttributeStatistic

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: attribute            Float
        3: attribute            Vector

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR') 
        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 

    Output sockets
    --------------

        0: mean                 Float
        1: median               Float
        2: sum                  Float
        3: min                  Float
        4: max                  Float
        5: range                Float
        6: standard_deviation   Float
        7: variance             Float
        8: mean                 Vector
        9: median               Vector
        10: sum                  Vector
        11: min                  Vector
        12: max                  Vector
        13: range                Vector
        14: standard_deviation   Vector
        15: variance             Vector

    """

    PARAMETERS = ['data_type', 'domain']

    def __init__(self, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeAttributeStatistic', name='Attribute Statistic')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'attribute'    ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'mean'         ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'median'       ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'sum'          ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'min'          ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'max'          ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'range'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'standard_deviation'))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'variance'     ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'mean'         ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'median'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'sum'          ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'min'          ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'max'          ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'range'        ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'standard_deviation'))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'variance'     ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'mean'

        # ----- Parameters

        self.data_type       = data_type
        self.domain          = domain
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.iattribute      = attribute

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'AttributeStatistic' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   attribute       : {self.iattribute}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   domain          : {self.domain}"
        s += '\nOutput sockets'
        s +=  "\n   mean            : variable"
        s +=  "\n   median          : variable"
        s +=  "\n   sum             : variable"
        s +=  "\n   min             : variable"
        s +=  "\n   max             : variable"
        s +=  "\n   range           : variable"
        s +=  "\n   standard_deviation : variable"
        s +=  "\n   variance        : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'FLOAT_VECTOR') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeAttributeStatistic'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeAttributeStatistic'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mean(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[0]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[8]
        self.check_parameters()

    @property
    def median(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[1]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[9]
        self.check_parameters()

    @property
    def sum(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[2]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[10]
        self.check_parameters()

    @property
    def min(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[3]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[11]
        self.check_parameters()

    @property
    def max(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[4]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[12]
        self.check_parameters()

    @property
    def range(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[5]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[13]
        self.check_parameters()

    @property
    def standard_deviation(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[6]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[14]
        self.check_parameters()

    @property
    def variance(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[7]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[15]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iattribute(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[3]

    @iattribute.setter
    def iattribute(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeAttributeTransfer

class NodeTransferAttribute(Node):

    """ Node class GeometryNodeAttributeTransfer

    Input sockets
    -------------

        0: source               Geometry
        1: attribute            Vector
        2: attribute            Float
        3: attribute            Color
        4: attribute            Boolean
        5: attribute            Integer
        6: source_position      Vector
        7: index                Integer

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
        mapping     : 'NEAREST_FACE_INTERPOLATED' in ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX') 

    Output sockets
    --------------

        0: attribute            Vector
        1: attribute            Float
        2: attribute            Color
        3: attribute            Boolean
        4: attribute            Integer

    """

    PARAMETERS = ['data_type', 'domain', 'mapping']

    def __init__(self, source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):

        super().__init__('GeometryNodeAttributeTransfer', name='Transfer Attribute')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'source'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'source_position'))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'index'        ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'attribute'    ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'attribute'

        # ----- Parameters

        self.data_type       = data_type
        self.domain          = domain
        self.mapping         = mapping
        self.check_parameters()

        # ----- Input sockets

        self.isource         = source
        self.iattribute      = attribute
        self.isource_position = source_position
        self.iindex          = index

        self.socket_in_name = 'isource'

    def __repr__(self):
        s = f"Node 'TransferAttribute' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   source          : {self.isource}"
        s += f"\n   attribute       : {self.iattribute}"
        s += f"\n   source_position : {self.isource_position}"
        s += f"\n   index           : {self.iindex}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   domain          : {self.domain}"
        s += f"\n   mapping         : {self.mapping}"
        s += '\nOutput sockets'
        s +=  "\n   attribute       : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeTransferAttribute'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeTransferAttribute'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")
        valids = ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX') 
        if self.mapping not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeTransferAttribute'.\n 'mapping' is '{self.mapping}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def attribute(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[0]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[1]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.outputs[2]
        elif (self.data_type == 'BOOLEAN'):
            return self.outputs[3]
        elif (self.data_type == 'INT'):
            return self.outputs[4]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def isource(self):
        return self.inputs[0]

    @isource.setter
    def isource(self, value):
        self.inputs[0].plug(value)

    @property
    def iattribute(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[1]
        elif (self.data_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.inputs[3]
        elif (self.data_type == 'BOOLEAN'):
            return self.inputs[4]
        elif (self.data_type == 'INT'):
            return self.inputs[5]

    @iattribute.setter
    def iattribute(self, value):
        if (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_COLOR'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'BOOLEAN'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[5].plug(value)

    @property
    def isource_position(self):
        return self.inputs[6]

    @isource_position.setter
    def isource_position(self, value):
        self.inputs[6].plug(value)

    @property
    def iindex(self):
        return self.inputs[7]

    @iindex.setter
    def iindex(self, value):
        self.inputs[7].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeBoundBox

class NodeBoundingBox(Node):

    """ Node class GeometryNodeBoundBox

    Input sockets
    -------------

        0: geometry             Geometry

    Output sockets
    --------------

        0: bounding_box         Geometry
        1: min                  Vector
        2: max                  Vector

    """

    PARAMETERS = []

    def __init__(self, geometry=None):

        super().__init__('GeometryNodeBoundBox', name='Bounding Box')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'bounding_box' ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'min'          ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'max'          ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'bounding_box'

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'BoundingBox' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nOutput sockets'
        s +=  "\n   bounding_box    : Geometry"
        s +=  "\n   min             : Vector"
        s +=  "\n   max             : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def bounding_box(self):
        return self.outputs[0]

    @property
    def min(self):
        return self.outputs[1]

    @property
    def max(self):
        return self.outputs[2]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCaptureAttribute

class NodeCaptureAttribute(Node):

    """ Node class GeometryNodeCaptureAttribute

    Input sockets
    -------------

        0: geometry             Geometry
        1: value                Vector
        2: value                Float
        3: value                Color
        4: value                Boolean
        5: value                Integer

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 

    Output sockets
    --------------

        0: geometry             Geometry
        1: attribute            Vector
        2: attribute            Float
        3: attribute            Color
        4: attribute            Boolean
        5: attribute            Integer

    """

    PARAMETERS = ['data_type', 'domain']

    def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeCaptureAttribute', name='Capture Attribute')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'value'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'attribute'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Parameters

        self.data_type       = data_type
        self.domain          = domain
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry
        self.ivalue          = value

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'CaptureAttribute' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   value           : {self.ivalue}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   domain          : {self.domain}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        s +=  "\n   attribute       : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCaptureAttribute'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCaptureAttribute'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    @property
    def attribute(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[1]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[2]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.outputs[3]
        elif (self.data_type == 'BOOLEAN'):
            return self.outputs[4]
        elif (self.data_type == 'INT'):
            return self.outputs[5]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def ivalue(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[1]
        elif (self.data_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.inputs[3]
        elif (self.data_type == 'BOOLEAN'):
            return self.inputs[4]
        elif (self.data_type == 'INT'):
            return self.inputs[5]

    @ivalue.setter
    def ivalue(self, value):
        if (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_COLOR'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'BOOLEAN'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCollectionInfo

class NodeCollectionInfo(Node):

    """ Node class GeometryNodeCollectionInfo

    Input sockets
    -------------

        0: collection           Collection
        1: separate_children    Boolean
        2: reset_children       Boolean

    Parameters
    ----------

        transform_space: 'ORIGINAL' in ('ORIGINAL', 'RELATIVE') 

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = ['transform_space']

    def __init__(self, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):

        super().__init__('GeometryNodeCollectionInfo', name='Collection Info')

        self.inputs.add(SocketIn(self, 'NodeSocketCollection'   , 'collection'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'separate_children'))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'reset_children'))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Parameters

        self.transform_space = transform_space
        self.check_parameters()

        # ----- Input sockets

        self.icollection     = collection
        self.iseparate_children = separate_children
        self.ireset_children = reset_children

        self.socket_in_name = 'icollection'

    def __repr__(self):
        s = f"Node 'CollectionInfo' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   collection      : {self.icollection}"
        s += f"\n   separate_children : {self.iseparate_children}"
        s += f"\n   reset_children  : {self.ireset_children}"
        s += '\nParameters'
        s += f"\n   transform_space : {self.transform_space}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('ORIGINAL', 'RELATIVE') 
        if self.transform_space not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCollectionInfo'.\n 'transform_space' is '{self.transform_space}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icollection(self):
        return self.inputs[0]

    @icollection.setter
    def icollection(self, value):
        self.inputs[0].plug(value)

    @property
    def iseparate_children(self):
        return self.inputs[1]

    @iseparate_children.setter
    def iseparate_children(self, value):
        self.inputs[1].plug(value)

    @property
    def ireset_children(self):
        return self.inputs[2]

    @ireset_children.setter
    def ireset_children(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeConvexHull

class NodeConvexHull(Node):

    """ Node class GeometryNodeConvexHull

    Input sockets
    -------------

        0: geometry             Geometry

    Output sockets
    --------------

        0: convex_hull          Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None):

        super().__init__('GeometryNodeConvexHull', name='Convex Hull')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'convex_hull'  ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'convex_hull'

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'ConvexHull' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nOutput sockets'
        s +=  "\n   convex_hull     : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def convex_hull(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveArc

class NodeArc(Node):

    """ Node class GeometryNodeCurveArc

    Input sockets
    -------------

        0: resolution           Integer
        1: start                Vector
        2: middle               Vector
        3: end                  Vector
        4: radius               Float
        5: start_angle          Float
        6: sweep_angle          Float
        7: offset_angle         Float
        8: connect_center       Boolean
        9: invert_arc           Boolean

    Parameters
    ----------

        mode        : 'RADIUS' in ('POINTS', 'RADIUS') 

    Output sockets
    --------------

        0: curve                Geometry
        1: center               Vector
        2: normal               Vector
        3: radius               Float

    """

    PARAMETERS = ['mode']

    def __init__(self, resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS'):

        super().__init__('GeometryNodeCurveArc', name='Arc')

        self.inputs.add(SocketIn(self, 'NodeSocketIntUnsigned'  , 'resolution'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'start'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'middle'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'end'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'start_angle'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'sweep_angle'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'offset_angle' ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'connect_center'))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'invert_arc'   ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'center'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'normal'       ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'radius'       ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.iresolution     = resolution
        self.istart          = start
        self.imiddle         = middle
        self.iend            = end
        self.iradius         = radius
        self.istart_angle    = start_angle
        self.isweep_angle    = sweep_angle
        self.ioffset_angle   = offset_angle
        self.iconnect_center = connect_center
        self.iinvert_arc     = invert_arc

        self.socket_in_name = 'iresolution'

    def __repr__(self):
        s = f"Node 'Arc' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   resolution      : {self.iresolution}"
        s += f"\n   start           : {self.istart}"
        s += f"\n   middle          : {self.imiddle}"
        s += f"\n   end             : {self.iend}"
        s += f"\n   radius          : {self.iradius}"
        s += f"\n   start_angle     : {self.istart_angle}"
        s += f"\n   sweep_angle     : {self.isweep_angle}"
        s += f"\n   offset_angle    : {self.ioffset_angle}"
        s += f"\n   connect_center  : {self.iconnect_center}"
        s += f"\n   invert_arc      : {self.iinvert_arc}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        s +=  "\n   center          : Vector"
        s +=  "\n   normal          : Vector"
        s +=  "\n   radius          : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('POINTS', 'RADIUS') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeArc'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    @property
    def center(self):
        return self.outputs[1]

    @property
    def normal(self):
        return self.outputs[2]

    @property
    def radius(self):
        return self.outputs[3]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iresolution(self):
        return self.inputs[0]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[0].plug(value)

    @property
    def istart(self):
        return self.inputs[1]

    @istart.setter
    def istart(self, value):
        self.inputs[1].plug(value)

    @property
    def imiddle(self):
        return self.inputs[2]

    @imiddle.setter
    def imiddle(self, value):
        self.inputs[2].plug(value)

    @property
    def iend(self):
        return self.inputs[3]

    @iend.setter
    def iend(self, value):
        self.inputs[3].plug(value)

    @property
    def iradius(self):
        return self.inputs[4]

    @iradius.setter
    def iradius(self, value):
        self.inputs[4].plug(value)

    @property
    def istart_angle(self):
        return self.inputs[5]

    @istart_angle.setter
    def istart_angle(self, value):
        self.inputs[5].plug(value)

    @property
    def isweep_angle(self):
        return self.inputs[6]

    @isweep_angle.setter
    def isweep_angle(self, value):
        self.inputs[6].plug(value)

    @property
    def ioffset_angle(self):
        return self.inputs[7]

    @ioffset_angle.setter
    def ioffset_angle(self, value):
        self.inputs[7].plug(value)

    @property
    def iconnect_center(self):
        return self.inputs[8]

    @iconnect_center.setter
    def iconnect_center(self, value):
        self.inputs[8].plug(value)

    @property
    def iinvert_arc(self):
        return self.inputs[9]

    @iinvert_arc.setter
    def iinvert_arc(self, value):
        self.inputs[9].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeCurveEndpointSelection

class NodeEndpointSelection(Attribute):

    """ Node class GeometryNodeCurveEndpointSelection

    Input sockets
    -------------

        0: start_size           Integer
        1: end_size             Integer

    Output sockets
    --------------

        0: selection            Boolean

    """

    PARAMETERS = []

    def __init__(self, start_size=None, end_size=None, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeCurveEndpointSelection', name='Endpoint Selection', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'start_size'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'end_size'     ))

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'selection'    ))

        self.socket_out_name = 'selection'

        # ----- Input sockets

        self.istart_size     = start_size
        self.iend_size       = end_size

        self.socket_in_name = 'istart_size'

    def __repr__(self):
        s = f"Node 'EndpointSelection' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   start_size      : {self.istart_size}"
        s += f"\n   end_size        : {self.iend_size}"
        s += '\nOutput sockets'
        s +=  "\n   selection       : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def selection(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def istart_size(self):
        return self.inputs[0]

    @istart_size.setter
    def istart_size(self, value):
        self.inputs[0].plug(value)

    @property
    def iend_size(self):
        return self.inputs[1]

    @iend_size.setter
    def iend_size(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeCurveHandleTypeSelection

class NodeHandleTypeSelection(Attribute):

    """ Node class GeometryNodeCurveHandleTypeSelection

    Parameters
    ----------

        handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN') 
        mode        : {'RIGHT', 'LEFT'}

    Output sockets
    --------------

        0: selection            Boolean

    """

    PARAMETERS = ['handle_type', 'mode']

    def __init__(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeCurveHandleTypeSelection', name='Handle Type Selection', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'selection'    ))

        self.socket_out_name = 'selection'

        # ----- Parameters

        self.handle_type     = handle_type
        self.mode            = mode
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'HandleTypeSelection' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   handle_type     : {self.handle_type}"
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   selection       : Boolean"
        return s + "\n"

    def check_parameters(self):
        valids = ('FREE', 'AUTO', 'VECTOR', 'ALIGN') 
        if self.handle_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeHandleTypeSelection'.\n 'handle_type' is '{self.handle_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def selection(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveLength

class NodeCurveLength(Node):

    """ Node class GeometryNodeCurveLength

    Input sockets
    -------------

        0: curve                Geometry

    Output sockets
    --------------

        0: length               Float

    """

    PARAMETERS = []

    def __init__(self, curve=None):

        super().__init__('GeometryNodeCurveLength', name='Curve Length')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'length'       ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'length'

        # ----- Input sockets

        self.icurve          = curve

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'CurveLength' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += '\nOutput sockets'
        s +=  "\n   length          : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def length(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurvePrimitiveBezierSegment

class NodeBezierSegment(Node):

    """ Node class GeometryNodeCurvePrimitiveBezierSegment

    Input sockets
    -------------

        0: resolution           Integer
        1: start                Vector
        2: start_handle         Vector
        3: end_handle           Vector
        4: end                  Vector

    Parameters
    ----------

        mode        : 'POSITION' in ('POSITION', 'OFFSET') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):

        super().__init__('GeometryNodeCurvePrimitiveBezierSegment', name='Bezier Segment')

        self.inputs.add(SocketIn(self, 'NodeSocketIntUnsigned'  , 'resolution'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'start'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'start_handle' ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'end_handle'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'end'          ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.iresolution     = resolution
        self.istart          = start
        self.istart_handle   = start_handle
        self.iend_handle     = end_handle
        self.iend            = end

        self.socket_in_name = 'iresolution'

    def __repr__(self):
        s = f"Node 'BezierSegment' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   resolution      : {self.iresolution}"
        s += f"\n   start           : {self.istart}"
        s += f"\n   start_handle    : {self.istart_handle}"
        s += f"\n   end_handle      : {self.iend_handle}"
        s += f"\n   end             : {self.iend}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('POSITION', 'OFFSET') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeBezierSegment'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iresolution(self):
        return self.inputs[0]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[0].plug(value)

    @property
    def istart(self):
        return self.inputs[1]

    @istart.setter
    def istart(self, value):
        self.inputs[1].plug(value)

    @property
    def istart_handle(self):
        return self.inputs[2]

    @istart_handle.setter
    def istart_handle(self, value):
        self.inputs[2].plug(value)

    @property
    def iend_handle(self):
        return self.inputs[3]

    @iend_handle.setter
    def iend_handle(self, value):
        self.inputs[3].plug(value)

    @property
    def iend(self):
        return self.inputs[4]

    @iend.setter
    def iend(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurvePrimitiveCircle

class NodeCurveCircle(Node):

    """ Node class GeometryNodeCurvePrimitiveCircle

    Input sockets
    -------------

        0: resolution           Integer
        1: point_1              Vector
        2: point_2              Vector
        3: point_3              Vector
        4: radius               Float

    Parameters
    ----------

        mode        : 'RADIUS' in ('POINTS', 'RADIUS') 

    Output sockets
    --------------

        0: curve                Geometry
        1: center               Vector

    """

    PARAMETERS = ['mode']

    def __init__(self, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):

        super().__init__('GeometryNodeCurvePrimitiveCircle', name='Curve Circle')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'resolution'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'point_1'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'point_2'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'point_3'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'center'       ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.iresolution     = resolution
        self.ipoint_1        = point_1
        self.ipoint_2        = point_2
        self.ipoint_3        = point_3
        self.iradius         = radius

        self.socket_in_name = 'iresolution'

    def __repr__(self):
        s = f"Node 'CurveCircle' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   resolution      : {self.iresolution}"
        s += f"\n   point_1         : {self.ipoint_1}"
        s += f"\n   point_2         : {self.ipoint_2}"
        s += f"\n   point_3         : {self.ipoint_3}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        s +=  "\n   center          : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('POINTS', 'RADIUS') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCurveCircle'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    @property
    def center(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iresolution(self):
        return self.inputs[0]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[0].plug(value)

    @property
    def ipoint_1(self):
        return self.inputs[1]

    @ipoint_1.setter
    def ipoint_1(self, value):
        self.inputs[1].plug(value)

    @property
    def ipoint_2(self):
        return self.inputs[2]

    @ipoint_2.setter
    def ipoint_2(self, value):
        self.inputs[2].plug(value)

    @property
    def ipoint_3(self):
        return self.inputs[3]

    @ipoint_3.setter
    def ipoint_3(self, value):
        self.inputs[3].plug(value)

    @property
    def iradius(self):
        return self.inputs[4]

    @iradius.setter
    def iradius(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurvePrimitiveLine

class NodeCurveLine(Node):

    """ Node class GeometryNodeCurvePrimitiveLine

    Input sockets
    -------------

        0: start                Vector
        1: end                  Vector
        2: direction            Vector
        3: length               Float

    Parameters
    ----------

        mode        : 'POINTS' in ('POINTS', 'DIRECTION') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS'):

        super().__init__('GeometryNodeCurvePrimitiveLine', name='Curve Line')

        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'start'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'end'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'direction'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'length'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.istart          = start
        self.iend            = end
        self.idirection      = direction
        self.ilength         = length

        self.socket_in_name = 'istart'

    def __repr__(self):
        s = f"Node 'CurveLine' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   start           : {self.istart}"
        s += f"\n   end             : {self.iend}"
        s += f"\n   direction       : {self.idirection}"
        s += f"\n   length          : {self.ilength}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('POINTS', 'DIRECTION') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCurveLine'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def istart(self):
        return self.inputs[0]

    @istart.setter
    def istart(self, value):
        self.inputs[0].plug(value)

    @property
    def iend(self):
        return self.inputs[1]

    @iend.setter
    def iend(self, value):
        self.inputs[1].plug(value)

    @property
    def idirection(self):
        return self.inputs[2]

    @idirection.setter
    def idirection(self, value):
        self.inputs[2].plug(value)

    @property
    def ilength(self):
        return self.inputs[3]

    @ilength.setter
    def ilength(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurvePrimitiveQuadrilateral

class NodeQuadrilateral(Node):

    """ Node class GeometryNodeCurvePrimitiveQuadrilateral

    Input sockets
    -------------

        0: width                Float
        1: height               Float
        2: bottom_width         Float
        3: top_width            Float
        4: offset               Float
        5: bottom_height        Float
        6: top_height           Float
        7: point_1              Vector
        8: point_2              Vector
        9: point_3              Vector
        10: point_4              Vector

    Parameters
    ----------

        mode        : 'RECTANGLE' in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):

        super().__init__('GeometryNodeCurvePrimitiveQuadrilateral', name='Quadrilateral')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'width'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'height'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'bottom_width' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'top_width'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'offset'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'bottom_height'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'top_height'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'point_1'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'point_2'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'point_3'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'point_4'      ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.iwidth          = width
        self.iheight         = height
        self.ibottom_width   = bottom_width
        self.itop_width      = top_width
        self.ioffset         = offset
        self.ibottom_height  = bottom_height
        self.itop_height     = top_height
        self.ipoint_1        = point_1
        self.ipoint_2        = point_2
        self.ipoint_3        = point_3
        self.ipoint_4        = point_4

        self.socket_in_name = 'iwidth'

    def __repr__(self):
        s = f"Node 'Quadrilateral' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   width           : {self.iwidth}"
        s += f"\n   height          : {self.iheight}"
        s += f"\n   bottom_width    : {self.ibottom_width}"
        s += f"\n   top_width       : {self.itop_width}"
        s += f"\n   offset          : {self.ioffset}"
        s += f"\n   bottom_height   : {self.ibottom_height}"
        s += f"\n   top_height      : {self.itop_height}"
        s += f"\n   point_1         : {self.ipoint_1}"
        s += f"\n   point_2         : {self.ipoint_2}"
        s += f"\n   point_3         : {self.ipoint_3}"
        s += f"\n   point_4         : {self.ipoint_4}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeQuadrilateral'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iwidth(self):
        return self.inputs[0]

    @iwidth.setter
    def iwidth(self, value):
        self.inputs[0].plug(value)

    @property
    def iheight(self):
        return self.inputs[1]

    @iheight.setter
    def iheight(self, value):
        self.inputs[1].plug(value)

    @property
    def ibottom_width(self):
        return self.inputs[2]

    @ibottom_width.setter
    def ibottom_width(self, value):
        self.inputs[2].plug(value)

    @property
    def itop_width(self):
        return self.inputs[3]

    @itop_width.setter
    def itop_width(self, value):
        self.inputs[3].plug(value)

    @property
    def ioffset(self):
        return self.inputs[4]

    @ioffset.setter
    def ioffset(self, value):
        self.inputs[4].plug(value)

    @property
    def ibottom_height(self):
        return self.inputs[5]

    @ibottom_height.setter
    def ibottom_height(self, value):
        self.inputs[5].plug(value)

    @property
    def itop_height(self):
        return self.inputs[6]

    @itop_height.setter
    def itop_height(self, value):
        self.inputs[6].plug(value)

    @property
    def ipoint_1(self):
        return self.inputs[7]

    @ipoint_1.setter
    def ipoint_1(self, value):
        self.inputs[7].plug(value)

    @property
    def ipoint_2(self):
        return self.inputs[8]

    @ipoint_2.setter
    def ipoint_2(self, value):
        self.inputs[8].plug(value)

    @property
    def ipoint_3(self):
        return self.inputs[9]

    @ipoint_3.setter
    def ipoint_3(self, value):
        self.inputs[9].plug(value)

    @property
    def ipoint_4(self):
        return self.inputs[10]

    @ipoint_4.setter
    def ipoint_4(self, value):
        self.inputs[10].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveQuadraticBezier

class NodeQuadraticBezier(Node):

    """ Node class GeometryNodeCurveQuadraticBezier

    Input sockets
    -------------

        0: resolution           Integer
        1: start                Vector
        2: middle               Vector
        3: end                  Vector

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, resolution=None, start=None, middle=None, end=None):

        super().__init__('GeometryNodeCurveQuadraticBezier', name='Quadratic Bezier')

        self.inputs.add(SocketIn(self, 'NodeSocketIntUnsigned'  , 'resolution'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'start'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'middle'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'end'          ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.iresolution     = resolution
        self.istart          = start
        self.imiddle         = middle
        self.iend            = end

        self.socket_in_name = 'iresolution'

    def __repr__(self):
        s = f"Node 'QuadraticBezier' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   resolution      : {self.iresolution}"
        s += f"\n   start           : {self.istart}"
        s += f"\n   middle          : {self.imiddle}"
        s += f"\n   end             : {self.iend}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iresolution(self):
        return self.inputs[0]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[0].plug(value)

    @property
    def istart(self):
        return self.inputs[1]

    @istart.setter
    def istart(self, value):
        self.inputs[1].plug(value)

    @property
    def imiddle(self):
        return self.inputs[2]

    @imiddle.setter
    def imiddle(self, value):
        self.inputs[2].plug(value)

    @property
    def iend(self):
        return self.inputs[3]

    @iend.setter
    def iend(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveSetHandles

class NodeSetHandleType(Node):

    """ Node class GeometryNodeCurveSetHandles

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean

    Parameters
    ----------

        handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN') 
        mode        : {'RIGHT', 'LEFT'}

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['handle_type', 'mode']

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

        super().__init__('GeometryNodeCurveSetHandles', name='Set Handle Type')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.handle_type     = handle_type
        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SetHandleType' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nParameters'
        s += f"\n   handle_type     : {self.handle_type}"
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('FREE', 'AUTO', 'VECTOR', 'ALIGN') 
        if self.handle_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSetHandleType'.\n 'handle_type' is '{self.handle_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveSpiral

class NodeSpiral(Node):

    """ Node class GeometryNodeCurveSpiral

    Input sockets
    -------------

        0: resolution           Integer
        1: rotations            Float
        2: start_radius         Float
        3: end_radius           Float
        4: height               Float
        5: reverse              Boolean

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):

        super().__init__('GeometryNodeCurveSpiral', name='Spiral')

        self.inputs.add(SocketIn(self, 'NodeSocketIntUnsigned'  , 'resolution'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'rotations'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'start_radius' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'end_radius'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'height'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'reverse'      ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.iresolution     = resolution
        self.irotations      = rotations
        self.istart_radius   = start_radius
        self.iend_radius     = end_radius
        self.iheight         = height
        self.ireverse        = reverse

        self.socket_in_name = 'iresolution'

    def __repr__(self):
        s = f"Node 'Spiral' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   resolution      : {self.iresolution}"
        s += f"\n   rotations       : {self.irotations}"
        s += f"\n   start_radius    : {self.istart_radius}"
        s += f"\n   end_radius      : {self.iend_radius}"
        s += f"\n   height          : {self.iheight}"
        s += f"\n   reverse         : {self.ireverse}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iresolution(self):
        return self.inputs[0]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[0].plug(value)

    @property
    def irotations(self):
        return self.inputs[1]

    @irotations.setter
    def irotations(self, value):
        self.inputs[1].plug(value)

    @property
    def istart_radius(self):
        return self.inputs[2]

    @istart_radius.setter
    def istart_radius(self, value):
        self.inputs[2].plug(value)

    @property
    def iend_radius(self):
        return self.inputs[3]

    @iend_radius.setter
    def iend_radius(self, value):
        self.inputs[3].plug(value)

    @property
    def iheight(self):
        return self.inputs[4]

    @iheight.setter
    def iheight(self, value):
        self.inputs[4].plug(value)

    @property
    def ireverse(self):
        return self.inputs[5]

    @ireverse.setter
    def ireverse(self, value):
        self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveSplineType

class NodeSetSplineType(Node):

    """ Node class GeometryNodeCurveSplineType

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean

    Parameters
    ----------

        spline_type : 'POLY' in ('BEZIER', 'NURBS', 'POLY') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['spline_type']

    def __init__(self, curve=None, selection=None, spline_type='POLY'):

        super().__init__('GeometryNodeCurveSplineType', name='Set Spline Type')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.spline_type     = spline_type
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SetSplineType' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nParameters'
        s += f"\n   spline_type     : {self.spline_type}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('BEZIER', 'NURBS', 'POLY') 
        if self.spline_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSetSplineType'.\n 'spline_type' is '{self.spline_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveStar

class NodeStar(Node):

    """ Node class GeometryNodeCurveStar

    Input sockets
    -------------

        0: points               Integer
        1: inner_radius         Float
        2: outer_radius         Float
        3: twist                Float

    Output sockets
    --------------

        0: curve                Geometry
        1: outer_points         Boolean

    """

    PARAMETERS = []

    def __init__(self, points=None, inner_radius=None, outer_radius=None, twist=None):

        super().__init__('GeometryNodeCurveStar', name='Star')

        self.inputs.add(SocketIn(self, 'NodeSocketIntUnsigned'  , 'points'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'inner_radius' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'outer_radius' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'twist'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'outer_points' ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.ipoints         = points
        self.iinner_radius   = inner_radius
        self.iouter_radius   = outer_radius
        self.itwist          = twist

        self.socket_in_name = 'ipoints'

    def __repr__(self):
        s = f"Node 'Star' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   points          : {self.ipoints}"
        s += f"\n   inner_radius    : {self.iinner_radius}"
        s += f"\n   outer_radius    : {self.iouter_radius}"
        s += f"\n   twist           : {self.itwist}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        s +=  "\n   outer_points    : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    @property
    def outer_points(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ipoints(self):
        return self.inputs[0]

    @ipoints.setter
    def ipoints(self, value):
        self.inputs[0].plug(value)

    @property
    def iinner_radius(self):
        return self.inputs[1]

    @iinner_radius.setter
    def iinner_radius(self, value):
        self.inputs[1].plug(value)

    @property
    def iouter_radius(self):
        return self.inputs[2]

    @iouter_radius.setter
    def iouter_radius(self, value):
        self.inputs[2].plug(value)

    @property
    def itwist(self):
        return self.inputs[3]

    @itwist.setter
    def itwist(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveToMesh

class NodeCurvetoMesh(Node):

    """ Node class GeometryNodeCurveToMesh

    Input sockets
    -------------

        0: curve                Geometry
        1: profile_curve        Geometry
        2: fill_caps            Boolean

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, curve=None, profile_curve=None, fill_caps=None):

        super().__init__('GeometryNodeCurveToMesh', name='Curve to Mesh')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'profile_curve'))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'fill_caps'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.icurve          = curve
        self.iprofile_curve  = profile_curve
        self.ifill_caps      = fill_caps

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'CurvetoMesh' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   profile_curve   : {self.iprofile_curve}"
        s += f"\n   fill_caps       : {self.ifill_caps}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iprofile_curve(self):
        return self.inputs[1]

    @iprofile_curve.setter
    def iprofile_curve(self, value):
        self.inputs[1].plug(value)

    @property
    def ifill_caps(self):
        return self.inputs[2]

    @ifill_caps.setter
    def ifill_caps(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeCurveToPoints

class NodeCurvetoPoints(Node):

    """ Node class GeometryNodeCurveToPoints

    Input sockets
    -------------

        0: curve                Geometry
        1: count                Integer
        2: length               Float

    Parameters
    ----------

        mode        : 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH') 

    Output sockets
    --------------

        0: points               Geometry
        1: tangent              Vector
        2: normal               Vector
        3: rotation             Vector

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, count=None, length=None, mode='COUNT'):

        super().__init__('GeometryNodeCurveToPoints', name='Curve to Points')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'count'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'length'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'points'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'tangent'      ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'normal'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'rotation'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'points'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.icount          = count
        self.ilength         = length

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'CurvetoPoints' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   count           : {self.icount}"
        s += f"\n   length          : {self.ilength}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   points          : Geometry"
        s +=  "\n   tangent         : Vector"
        s +=  "\n   normal          : Vector"
        s +=  "\n   rotation        : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('EVALUATED', 'COUNT', 'LENGTH') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCurvetoPoints'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def points(self):
        return self.outputs[0]

    @property
    def tangent(self):
        return self.outputs[1]

    @property
    def normal(self):
        return self.outputs[2]

    @property
    def rotation(self):
        return self.outputs[3]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def icount(self):
        return self.inputs[1]

    @icount.setter
    def icount(self, value):
        self.inputs[1].plug(value)

    @property
    def ilength(self):
        return self.inputs[2]

    @ilength.setter
    def ilength(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeDeleteGeometry

class NodeDeleteGeometry(Node):

    """ Node class GeometryNodeDeleteGeometry

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean

    Parameters
    ----------

        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE') 
        mode        : 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE') 

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = ['domain', 'mode']

    def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL'):

        super().__init__('GeometryNodeDeleteGeometry', name='Delete Geometry')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Parameters

        self.domain          = domain
        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'DeleteGeometry' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nParameters'
        s += f"\n   domain          : {self.domain}"
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeDeleteGeometry'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")
        valids = ('ALL', 'EDGE_FACE', 'ONLY_FACE') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeDeleteGeometry'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeDistributePointsOnFaces

class NodeDistributePointsonFaces(Node):

    """ Node class GeometryNodeDistributePointsOnFaces

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean
        2: distance_min         Float
        3: density_max          Float
        4: density              Float
        5: density_factor       Float
        6: seed                 Integer

    Parameters
    ----------

        distribute_method: 'RANDOM' in ('RANDOM', 'POISSON') 

    Output sockets
    --------------

        0: points               Geometry
        1: normal               Vector
        2: rotation             Vector

    """

    PARAMETERS = ['distribute_method']

    def __init__(self, mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):

        super().__init__('GeometryNodeDistributePointsOnFaces', name='Distribute Points on Faces')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'distance_min' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'density_max'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'density'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'density_factor'))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'seed'         ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'points'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'normal'       ))
        self.outputs.add(Socket (self, 'NodeSocketVectorEuler'  , 'rotation'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'points'

        # ----- Parameters

        self.distribute_method = distribute_method
        self.check_parameters()

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection
        self.idistance_min   = distance_min
        self.idensity_max    = density_max
        self.idensity        = density
        self.idensity_factor = density_factor
        self.iseed           = seed

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'DistributePointsonFaces' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   distance_min    : {self.idistance_min}"
        s += f"\n   density_max     : {self.idensity_max}"
        s += f"\n   density         : {self.idensity}"
        s += f"\n   density_factor  : {self.idensity_factor}"
        s += f"\n   seed            : {self.iseed}"
        s += '\nParameters'
        s += f"\n   distribute_method : {self.distribute_method}"
        s += '\nOutput sockets'
        s +=  "\n   points          : Geometry"
        s +=  "\n   normal          : Vector"
        s +=  "\n   rotation        : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('RANDOM', 'POISSON') 
        if self.distribute_method not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeDistributePointsonFaces'.\n 'distribute_method' is '{self.distribute_method}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def points(self):
        return self.outputs[0]

    @property
    def normal(self):
        return self.outputs[1]

    @property
    def rotation(self):
        return self.outputs[2]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def idistance_min(self):
        return self.inputs[2]

    @idistance_min.setter
    def idistance_min(self, value):
        self.inputs[2].plug(value)

    @property
    def idensity_max(self):
        return self.inputs[3]

    @idensity_max.setter
    def idensity_max(self, value):
        self.inputs[3].plug(value)

    @property
    def idensity(self):
        return self.inputs[4]

    @idensity.setter
    def idensity(self, value):
        self.inputs[4].plug(value)

    @property
    def idensity_factor(self):
        return self.inputs[5]

    @idensity_factor.setter
    def idensity_factor(self, value):
        self.inputs[5].plug(value)

    @property
    def iseed(self):
        return self.inputs[6]

    @iseed.setter
    def iseed(self, value):
        self.inputs[6].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeDualMesh

class NodeDualMesh(Node):

    """ Node class GeometryNodeDualMesh

    Input sockets
    -------------

        0: mesh                 Geometry
        1: keep_boundaries      Boolean

    Output sockets
    --------------

        0: dual_mesh            Geometry

    """

    PARAMETERS = []

    def __init__(self, mesh=None, keep_boundaries=None):

        super().__init__('GeometryNodeDualMesh', name='Dual Mesh')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'keep_boundaries'))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'dual_mesh'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'dual_mesh'

        # ----- Input sockets

        self.imesh           = mesh
        self.ikeep_boundaries = keep_boundaries

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'DualMesh' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   keep_boundaries : {self.ikeep_boundaries}"
        s += '\nOutput sockets'
        s +=  "\n   dual_mesh       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def dual_mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def ikeep_boundaries(self):
        return self.inputs[1]

    @ikeep_boundaries.setter
    def ikeep_boundaries(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeExtrudeMesh

class NodeExtrudeMesh(Node):

    """ Node class GeometryNodeExtrudeMesh

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean
        2: offset               Vector
        3: offset_scale         Float
        4: individual           Boolean

    Parameters
    ----------

        mode        : 'FACES' in ('VERTICES', 'EDGES', 'FACES') 

    Output sockets
    --------------

        0: mesh                 Geometry
        1: top                  Boolean
        2: side                 Boolean

    """

    PARAMETERS = ['mode']

    def __init__(self, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):

        super().__init__('GeometryNodeExtrudeMesh', name='Extrude Mesh')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'offset'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'offset_scale' ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'individual'   ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'top'          ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'side'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection
        self.ioffset         = offset
        self.ioffset_scale   = offset_scale
        self.iindividual     = individual

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'ExtrudeMesh' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   offset          : {self.ioffset}"
        s += f"\n   offset_scale    : {self.ioffset_scale}"
        s += f"\n   individual      : {self.iindividual}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        s +=  "\n   top             : Boolean"
        s +=  "\n   side            : Boolean"
        return s + "\n"

    def check_parameters(self):
        valids = ('VERTICES', 'EDGES', 'FACES') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeExtrudeMesh'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    @property
    def top(self):
        return self.outputs[1]

    @property
    def side(self):
        return self.outputs[2]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def ioffset(self):
        return self.inputs[2]

    @ioffset.setter
    def ioffset(self, value):
        self.inputs[2].plug(value)

    @property
    def ioffset_scale(self):
        return self.inputs[3]

    @ioffset_scale.setter
    def ioffset_scale(self, value):
        self.inputs[3].plug(value)

    @property
    def iindividual(self):
        return self.inputs[4]

    @iindividual.setter
    def iindividual(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeFieldAtIndex

class NodeFieldatIndex(Node):

    """ Node class GeometryNodeFieldAtIndex

    Input sockets
    -------------

        0: index                Integer
        1: value                Float
        2: value                Integer
        3: value                Vector
        4: value                Color
        5: value                Boolean

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 

    Output sockets
    --------------

        0: value                Float
        1: value                Integer
        2: value                Vector
        3: value                Color
        4: value                Boolean

    """

    PARAMETERS = ['data_type', 'domain']

    def __init__(self, index=None, value=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeFieldAtIndex', name='Field at Index')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'index'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'value'        ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'value'        ))

        self.socket_out_name = 'value'

        # ----- Parameters

        self.data_type       = data_type
        self.domain          = domain
        self.check_parameters()

        # ----- Input sockets

        self.iindex          = index
        self.ivalue          = value

        self.socket_in_name = 'iindex'

    def __repr__(self):
        s = f"Node 'FieldatIndex' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   index           : {self.iindex}"
        s += f"\n   value           : {self.ivalue}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   domain          : {self.domain}"
        s += '\nOutput sockets'
        s +=  "\n   value           : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeFieldatIndex'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeFieldatIndex'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def value(self):
        if (self.data_type == 'FLOAT'):
            return self.outputs[0]
        elif (self.data_type == 'INT'):
            return self.outputs[1]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[2]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.outputs[3]
        elif (self.data_type == 'BOOLEAN'):
            return self.outputs[4]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iindex(self):
        return self.inputs[0]

    @iindex.setter
    def iindex(self, value):
        self.inputs[0].plug(value)

    @property
    def ivalue(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[1]
        elif (self.data_type == 'INT'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[3]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.inputs[4]
        elif (self.data_type == 'BOOLEAN'):
            return self.inputs[5]

    @ivalue.setter
    def ivalue(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'FLOAT_COLOR'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'BOOLEAN'):
            self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeFillCurve

class NodeFillCurve(Node):

    """ Node class GeometryNodeFillCurve

    Input sockets
    -------------

        0: curve                Geometry

    Parameters
    ----------

        mode        : 'TRIANGLES' in ('TRIANGLES', 'NGONS') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, mode='TRIANGLES'):

        super().__init__('GeometryNodeFillCurve', name='Fill Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'FillCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('TRIANGLES', 'NGONS') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeFillCurve'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeFilletCurve

class NodeFilletCurve(Node):

    """ Node class GeometryNodeFilletCurve

    Input sockets
    -------------

        0: curve                Geometry
        1: count                Integer
        2: radius               Float
        3: limit_radius         Boolean

    Parameters
    ----------

        mode        : 'BEZIER' in ('BEZIER', 'POLY') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER'):

        super().__init__('GeometryNodeFilletCurve', name='Fillet Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'count'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'limit_radius' ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.icount          = count
        self.iradius         = radius
        self.ilimit_radius   = limit_radius

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'FilletCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   count           : {self.icount}"
        s += f"\n   radius          : {self.iradius}"
        s += f"\n   limit_radius    : {self.ilimit_radius}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('BEZIER', 'POLY') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeFilletCurve'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def icount(self):
        return self.inputs[1]

    @icount.setter
    def icount(self, value):
        self.inputs[1].plug(value)

    @property
    def iradius(self):
        return self.inputs[2]

    @iradius.setter
    def iradius(self, value):
        self.inputs[2].plug(value)

    @property
    def ilimit_radius(self):
        return self.inputs[3]

    @ilimit_radius.setter
    def ilimit_radius(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeFlipFaces

class NodeFlipFaces(Node):

    """ Node class GeometryNodeFlipFaces

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, mesh=None, selection=None):

        super().__init__('GeometryNodeFlipFaces', name='Flip Faces')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'FlipFaces' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeGeometryToInstance

class NodeGeometrytoInstance(Node):

    """ Node class GeometryNodeGeometryToInstance

    Input sockets
    -------------

        0: geometry             Geometry

    Output sockets
    --------------

        0: instances            Geometry

    """

    PARAMETERS = []

    def __init__(self, *geometry):

        super().__init__('GeometryNodeGeometryToInstance', name='Geometry to Instance')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     , is_multi_input=True))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'instances'    ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'instances'

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'GeometrytoInstance' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nOutput sockets'
        s +=  "\n   instances       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def instances(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeGroup

class NodeGroup(Node):

    """ Node class GeometryNodeGroup

    Parameters
    ----------

        node_tree   : None

    """

    PARAMETERS = ['node_tree']

    def __init__(self, node_tree=None):

        super().__init__('GeometryNodeGroup', name='Group')

        self.socket_out_name = None

        # ----- Parameters

        self.node_tree       = node_tree
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Group' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   node_tree       : {self.node_tree}"
        return s + "\n"

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeImageTexture

class NodeImageTexture(Node):

    """ Node class GeometryNodeImageTexture

    Input sockets
    -------------

        0: image                Image
        1: vector               Vector
        2: frame                Integer

    Parameters
    ----------

        extension   : 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP') 
        interpolation: 'Linear' in ('Linear', 'Closest', 'Cubic') 

    Output sockets
    --------------

        0: color                Color
        1: alpha                Float

    """

    PARAMETERS = ['extension', 'interpolation']

    def __init__(self, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

        super().__init__('GeometryNodeImageTexture', name='Image Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketImage'        , 'image'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'frame'        ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'alpha'        ))

        self.socket_out_name = 'color'

        # ----- Parameters

        self.extension       = extension
        self.interpolation   = interpolation
        self.check_parameters()

        # ----- Input sockets

        self.iimage          = image
        self.ivector         = vector
        self.iframe          = frame

        self.socket_in_name = 'iimage'

    def __repr__(self):
        s = f"Node 'ImageTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   image           : {self.iimage}"
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   frame           : {self.iframe}"
        s += '\nParameters'
        s += f"\n   extension       : {self.extension}"
        s += f"\n   interpolation   : {self.interpolation}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   alpha           : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('REPEAT', 'EXTEND', 'CLIP') 
        if self.extension not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeImageTexture'.\n 'extension' is '{self.extension}'.\n Authorized values are {valids}.")
        valids = ('Linear', 'Closest', 'Cubic') 
        if self.interpolation not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeImageTexture'.\n 'interpolation' is '{self.interpolation}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def alpha(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iimage(self):
        return self.inputs[0]

    @iimage.setter
    def iimage(self, value):
        self.inputs[0].plug(value)

    @property
    def ivector(self):
        return self.inputs[1]

    @ivector.setter
    def ivector(self, value):
        self.inputs[1].plug(value)

    @property
    def iframe(self):
        return self.inputs[2]

    @iframe.setter
    def iframe(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputCurveHandlePositions

class NodeCurveHandlePositions(Attribute):

    """ Node class GeometryNodeInputCurveHandlePositions

    Input sockets
    -------------

        0: relative             Boolean

    Output sockets
    --------------

        0: left                 Vector
        1: right                Vector

    """

    PARAMETERS = []

    def __init__(self, relative=None, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputCurveHandlePositions', name='Curve Handle Positions', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'relative'     ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'left'         ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'right'        ))

        self.socket_out_name = 'left'

        # ----- Input sockets

        self.irelative       = relative

        self.socket_in_name = 'irelative'

    def __repr__(self):
        s = f"Node 'CurveHandlePositions' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   relative        : {self.irelative}"
        s += '\nOutput sockets'
        s +=  "\n   left            : Vector"
        s +=  "\n   right           : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def left(self):
        return self.outputs[0]

    @property
    def right(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def irelative(self):
        return self.inputs[0]

    @irelative.setter
    def irelative(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputCurveTilt

class NodeCurveTilt(Attribute):

    """ Node class GeometryNodeInputCurveTilt

    Output sockets
    --------------

        0: tilt                 Float

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputCurveTilt', name='Curve Tilt', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'tilt'         ))

        self.socket_out_name = 'tilt'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'CurveTilt' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   tilt            : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def tilt(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputID

class NodeID(Attribute):

    """ Node class GeometryNodeInputID

    Output sockets
    --------------

        0: ID                   Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputID', name='ID', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'ID'           ))

        self.socket_out_name = 'ID'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'ID' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   ID              : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def ID(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputIndex

class NodeIndex(Attribute):

    """ Node class GeometryNodeInputIndex

    Output sockets
    --------------

        0: index                Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputIndex', name='Index', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'index'        ))

        self.socket_out_name = 'index'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Index' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   index           : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def index(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeInputMaterial

class NodeMaterial(Node):

    """ Node class GeometryNodeInputMaterial

    Parameters
    ----------

        material_   : None

    Output sockets
    --------------

        0: material             Material

    """

    PARAMETERS = ['material_']

    def __init__(self, material=None):

        super().__init__('GeometryNodeInputMaterial', name='Material')

        self.outputs.add(Socket (self, 'NodeSocketMaterial'     , 'material'     ))

        self.socket_out_name = 'material'

        # ----- Parameters

        self.material_       = material
        self.check_parameters()

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Material' ({self.unique_id})"
        s += '\nParameters'
        s += f"\n   material        : {self.material}"
        s += '\nOutput sockets'
        s +=  "\n   material        : Material"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def material(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMaterialIndex

class NodeMaterialIndex(Attribute):

    """ Node class GeometryNodeInputMaterialIndex

    Output sockets
    --------------

        0: material_index       Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMaterialIndex', name='Material Index', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'material_index'))

        self.socket_out_name = 'material_index'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'MaterialIndex' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   material_index  : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def material_index(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshEdgeAngle

class NodeEdgeAngle(Attribute):

    """ Node class GeometryNodeInputMeshEdgeAngle

    Output sockets
    --------------

        0: unsigned_angle       Float
        1: signed_angle         Float

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshEdgeAngle', name='Edge Angle', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'unsigned_angle'))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'signed_angle' ))

        self.socket_out_name = 'unsigned_angle'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'EdgeAngle' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   unsigned_angle  : Float"
        s +=  "\n   signed_angle    : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def unsigned_angle(self):
        return self.outputs[0]

    @property
    def signed_angle(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshEdgeNeighbors

class NodeEdgeNeighbors(Attribute):

    """ Node class GeometryNodeInputMeshEdgeNeighbors

    Output sockets
    --------------

        0: face_count           Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', name='Edge Neighbors', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'face_count'   ))

        self.socket_out_name = 'face_count'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'EdgeNeighbors' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   face_count      : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def face_count(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshEdgeVertices

class NodeEdgeVertices(Attribute):

    """ Node class GeometryNodeInputMeshEdgeVertices

    Output sockets
    --------------

        0: vertex_index_1       Integer
        1: vertex_index_2       Integer
        2: position_1           Vector
        3: position_2           Vector

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshEdgeVertices', name='Edge Vertices', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'vertex_index_1'))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'vertex_index_2'))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'position_1'   ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'position_2'   ))

        self.socket_out_name = 'vertex_index_1'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'EdgeVertices' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   vertex_index_1  : Integer"
        s +=  "\n   vertex_index_2  : Integer"
        s +=  "\n   position_1      : Vector"
        s +=  "\n   position_2      : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vertex_index_1(self):
        return self.outputs[0]

    @property
    def vertex_index_2(self):
        return self.outputs[1]

    @property
    def position_1(self):
        return self.outputs[2]

    @property
    def position_2(self):
        return self.outputs[3]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshFaceArea

class NodeFaceArea(Attribute):

    """ Node class GeometryNodeInputMeshFaceArea

    Output sockets
    --------------

        0: area                 Float

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshFaceArea', name='Face Area', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'area'         ))

        self.socket_out_name = 'area'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'FaceArea' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   area            : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def area(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshFaceNeighbors

class NodeFaceNeighbors(Attribute):

    """ Node class GeometryNodeInputMeshFaceNeighbors

    Output sockets
    --------------

        0: vertex_count         Integer
        1: face_count           Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshFaceNeighbors', name='Face Neighbors', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'vertex_count' ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'face_count'   ))

        self.socket_out_name = 'vertex_count'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'FaceNeighbors' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   vertex_count    : Integer"
        s +=  "\n   face_count      : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vertex_count(self):
        return self.outputs[0]

    @property
    def face_count(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshIsland

class NodeMeshIsland(Attribute):

    """ Node class GeometryNodeInputMeshIsland

    Output sockets
    --------------

        0: island_index         Integer
        1: island_count         Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshIsland', name='Mesh Island', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'island_index' ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'island_count' ))

        self.socket_out_name = 'island_index'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'MeshIsland' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   island_index    : Integer"
        s +=  "\n   island_count    : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def island_index(self):
        return self.outputs[0]

    @property
    def island_count(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputMeshVertexNeighbors

class NodeVertexNeighbors(Attribute):

    """ Node class GeometryNodeInputMeshVertexNeighbors

    Output sockets
    --------------

        0: vertex_count         Integer
        1: face_count           Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputMeshVertexNeighbors', name='Vertex Neighbors', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'vertex_count' ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'face_count'   ))

        self.socket_out_name = 'vertex_count'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'VertexNeighbors' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   vertex_count    : Integer"
        s +=  "\n   face_count      : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vertex_count(self):
        return self.outputs[0]

    @property
    def face_count(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputNormal

class NodeNormal(Attribute):

    """ Node class GeometryNodeInputNormal

    Output sockets
    --------------

        0: normal               Vector

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputNormal', name='Normal', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'normal'       ))

        self.socket_out_name = 'normal'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Normal' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   normal          : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def normal(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputPosition

class NodePosition(Attribute):

    """ Node class GeometryNodeInputPosition

    Output sockets
    --------------

        0: position             Vector

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputPosition', name='Position', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'position'     ))

        self.socket_out_name = 'position'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Position' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   position        : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def position(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputRadius

class NodeRadius(Attribute):

    """ Node class GeometryNodeInputRadius

    Output sockets
    --------------

        0: radius               Float

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputRadius', name='Radius', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'radius'       ))

        self.socket_out_name = 'radius'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Radius' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   radius          : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def radius(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeInputSceneTime

class NodeSceneTime(Node):

    """ Node class GeometryNodeInputSceneTime

    Output sockets
    --------------

        0: seconds              Float
        1: frame                Float

    """

    PARAMETERS = []

    def __init__(self):

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time')

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'seconds'      ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'frame'        ))

        self.socket_out_name = 'seconds'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'SceneTime' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   seconds         : Float"
        s +=  "\n   frame           : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def seconds(self):
        return self.outputs[0]

    @property
    def frame(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputShadeSmooth

class NodeIsShadeSmooth(Attribute):

    """ Node class GeometryNodeInputShadeSmooth

    Output sockets
    --------------

        0: smooth               Boolean

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputShadeSmooth', name='Is Shade Smooth', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'smooth'       ))

        self.socket_out_name = 'smooth'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'IsShadeSmooth' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   smooth          : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def smooth(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputSplineCyclic

class NodeIsSplineCyclic(Attribute):

    """ Node class GeometryNodeInputSplineCyclic

    Output sockets
    --------------

        0: cyclic               Boolean

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputSplineCyclic', name='Is Spline Cyclic', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'cyclic'       ))

        self.socket_out_name = 'cyclic'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'IsSplineCyclic' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   cyclic          : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def cyclic(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputSplineResolution

class NodeSplineResolution(Attribute):

    """ Node class GeometryNodeInputSplineResolution

    Output sockets
    --------------

        0: resolution           Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputSplineResolution', name='Spline Resolution', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'resolution'   ))

        self.socket_out_name = 'resolution'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'SplineResolution' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   resolution      : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def resolution(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeInputTangent

class NodeCurveTangent(Attribute):

    """ Node class GeometryNodeInputTangent

    Output sockets
    --------------

        0: tangent              Vector

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeInputTangent', name='Curve Tangent', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'tangent'      ))

        self.socket_out_name = 'tangent'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'CurveTangent' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   tangent         : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def tangent(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeInstanceOnPoints

class NodeInstanceonPoints(Node):

    """ Node class GeometryNodeInstanceOnPoints

    Input sockets
    -------------

        0: points               Geometry
        1: selection            Boolean
        2: instance             Geometry
        3: pick_instance        Boolean
        4: instance_index       Integer
        5: rotation             Vector
        6: scale                Vector

    Output sockets
    --------------

        0: instances            Geometry

    """

    PARAMETERS = []

    def __init__(self, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

        super().__init__('GeometryNodeInstanceOnPoints', name='Instance on Points')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'points'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'instance'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'pick_instance'))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'instance_index'))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotation'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorXYZ'    , 'scale'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'instances'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'instances'

        # ----- Input sockets

        self.ipoints         = points
        self.iselection      = selection
        self.iinstance       = instance
        self.ipick_instance  = pick_instance
        self.iinstance_index = instance_index
        self.irotation       = rotation
        self.iscale          = scale

        self.socket_in_name = 'ipoints'

    def __repr__(self):
        s = f"Node 'InstanceonPoints' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   points          : {self.ipoints}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   instance        : {self.iinstance}"
        s += f"\n   pick_instance   : {self.ipick_instance}"
        s += f"\n   instance_index  : {self.iinstance_index}"
        s += f"\n   rotation        : {self.irotation}"
        s += f"\n   scale           : {self.iscale}"
        s += '\nOutput sockets'
        s +=  "\n   instances       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def instances(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ipoints(self):
        return self.inputs[0]

    @ipoints.setter
    def ipoints(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iinstance(self):
        return self.inputs[2]

    @iinstance.setter
    def iinstance(self, value):
        self.inputs[2].plug(value)

    @property
    def ipick_instance(self):
        return self.inputs[3]

    @ipick_instance.setter
    def ipick_instance(self, value):
        self.inputs[3].plug(value)

    @property
    def iinstance_index(self):
        return self.inputs[4]

    @iinstance_index.setter
    def iinstance_index(self, value):
        self.inputs[4].plug(value)

    @property
    def irotation(self):
        return self.inputs[5]

    @irotation.setter
    def irotation(self, value):
        self.inputs[5].plug(value)

    @property
    def iscale(self):
        return self.inputs[6]

    @iscale.setter
    def iscale(self, value):
        self.inputs[6].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeInstancesToPoints

class NodeInstancestoPoints(Node):

    """ Node class GeometryNodeInstancesToPoints

    Input sockets
    -------------

        0: instances            Geometry
        1: selection            Boolean
        2: position             Vector
        3: radius               Float

    Output sockets
    --------------

        0: points               Geometry

    """

    PARAMETERS = []

    def __init__(self, instances=None, selection=None, position=None, radius=None):

        super().__init__('GeometryNodeInstancesToPoints', name='Instances to Points')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'instances'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'position'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'points'       ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'points'

        # ----- Input sockets

        self.iinstances      = instances
        self.iselection      = selection
        self.iposition       = position
        self.iradius         = radius

        self.socket_in_name = 'iinstances'

    def __repr__(self):
        s = f"Node 'InstancestoPoints' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   instances       : {self.iinstances}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   position        : {self.iposition}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nOutput sockets'
        s +=  "\n   points          : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def points(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iinstances(self):
        return self.inputs[0]

    @iinstances.setter
    def iinstances(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iposition(self):
        return self.inputs[2]

    @iposition.setter
    def iposition(self, value):
        self.inputs[2].plug(value)

    @property
    def iradius(self):
        return self.inputs[3]

    @iradius.setter
    def iradius(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeIsViewport

class NodeIsViewport(Attribute):

    """ Node class GeometryNodeIsViewport

    Output sockets
    --------------

        0: is_viewport          Boolean

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeIsViewport', name='Is Viewport', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'is_viewport'  ))

        self.socket_out_name = 'is_viewport'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'IsViewport' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   is_viewport     : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def is_viewport(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeJoinGeometry

class NodeJoinGeometry(Node):

    """ Node class GeometryNodeJoinGeometry

    Input sockets
    -------------

        0: geometry             Geometry

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, *geometry):

        super().__init__('GeometryNodeJoinGeometry', name='Join Geometry')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     , is_multi_input=True))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'JoinGeometry' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMaterialSelection

class NodeMaterialSelection(Node):

    """ Node class GeometryNodeMaterialSelection

    Input sockets
    -------------

        0: material             Material

    Output sockets
    --------------

        0: selection            Boolean

    """

    PARAMETERS = []

    def __init__(self, material=None):

        super().__init__('GeometryNodeMaterialSelection', name='Material Selection')

        self.inputs.add(SocketIn(self, 'NodeSocketMaterial'     , 'material'     ))

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'selection'    ))

        self.socket_out_name = 'selection'

        # ----- Input sockets

        self.imaterial       = material

        self.socket_in_name = 'imaterial'

    def __repr__(self):
        s = f"Node 'MaterialSelection' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   material        : {self.imaterial}"
        s += '\nOutput sockets'
        s +=  "\n   selection       : Boolean"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def selection(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imaterial(self):
        return self.inputs[0]

    @imaterial.setter
    def imaterial(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMergeByDistance

class NodeMergebyDistance(Node):

    """ Node class GeometryNodeMergeByDistance

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: distance             Float

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, distance=None):

        super().__init__('GeometryNodeMergeByDistance', name='Merge by Distance')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'distance'     ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.idistance       = distance

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'MergebyDistance' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   distance        : {self.idistance}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def idistance(self):
        return self.inputs[2]

    @idistance.setter
    def idistance(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshBoolean

class NodeMeshBoolean(Node):

    """ Node class GeometryNodeMeshBoolean

    Input sockets
    -------------

        0: mesh_1               Geometry
        1: mesh_2               Geometry
        2: self_intersection    Boolean
        3: hole_tolerant        Boolean

    Parameters
    ----------

        operation   : 'DIFFERENCE' in ('INTERSECT', 'UNION', 'DIFFERENCE') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['operation']

    def __init__(self, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE'):

        super().__init__('GeometryNodeMeshBoolean', name='Mesh Boolean')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh_1'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh_2'       , is_multi_input=True))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'self_intersection'))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'hole_tolerant'))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.operation       = operation
        self.check_parameters()

        # ----- Input sockets

        self.imesh_1         = mesh_1
        self.imesh_2         = mesh_2
        self.iself_intersection = self_intersection
        self.ihole_tolerant  = hole_tolerant

        self.socket_in_name = 'imesh_2'

    def __repr__(self):
        s = f"Node 'MeshBoolean' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh_1          : {self.imesh_1}"
        s += f"\n   mesh_2          : {self.imesh_2}"
        s += f"\n   self_intersection : {self.iself_intersection}"
        s += f"\n   hole_tolerant   : {self.ihole_tolerant}"
        s += '\nParameters'
        s += f"\n   operation       : {self.operation}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('INTERSECT', 'UNION', 'DIFFERENCE') 
        if self.operation not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMeshBoolean'.\n 'operation' is '{self.operation}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh_1(self):
        return self.inputs[0]

    @imesh_1.setter
    def imesh_1(self, value):
        self.inputs[0].plug(value)

    @property
    def imesh_2(self):
        return self.inputs[1]

    @imesh_2.setter
    def imesh_2(self, value):
        self.inputs[1].plug(value)

    @property
    def iself_intersection(self):
        return self.inputs[2]

    @iself_intersection.setter
    def iself_intersection(self, value):
        self.inputs[2].plug(value)

    @property
    def ihole_tolerant(self):
        return self.inputs[3]

    @ihole_tolerant.setter
    def ihole_tolerant(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshCircle

class NodeMeshCircle(Node):

    """ Node class GeometryNodeMeshCircle

    Input sockets
    -------------

        0: vertices             Integer
        1: radius               Float

    Parameters
    ----------

        fill_type   : 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['fill_type']

    def __init__(self, vertices=None, radius=None, fill_type='NONE'):

        super().__init__('GeometryNodeMeshCircle', name='Mesh Circle')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.fill_type       = fill_type
        self.check_parameters()

        # ----- Input sockets

        self.ivertices       = vertices
        self.iradius         = radius

        self.socket_in_name = 'ivertices'

    def __repr__(self):
        s = f"Node 'MeshCircle' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vertices        : {self.ivertices}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nParameters'
        s += f"\n   fill_type       : {self.fill_type}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('NONE', 'NGON', 'TRIANGLE_FAN') 
        if self.fill_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMeshCircle'.\n 'fill_type' is '{self.fill_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivertices(self):
        return self.inputs[0]

    @ivertices.setter
    def ivertices(self, value):
        self.inputs[0].plug(value)

    @property
    def iradius(self):
        return self.inputs[1]

    @iradius.setter
    def iradius(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshCone

class NodeCone(Node):

    """ Node class GeometryNodeMeshCone

    Input sockets
    -------------

        0: vertices             Integer
        1: side_segments        Integer
        2: fill_segments        Integer
        3: radius_top           Float
        4: radius_bottom        Float
        5: depth                Float

    Parameters
    ----------

        fill_type   : 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN') 

    Output sockets
    --------------

        0: mesh                 Geometry
        1: top                  Boolean
        2: bottom               Boolean
        3: side                 Boolean

    """

    PARAMETERS = ['fill_type']

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):

        super().__init__('GeometryNodeMeshCone', name='Cone')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'side_segments'))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'fill_segments'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius_top'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius_bottom'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'depth'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'top'          ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'bottom'       ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'side'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.fill_type       = fill_type
        self.check_parameters()

        # ----- Input sockets

        self.ivertices       = vertices
        self.iside_segments  = side_segments
        self.ifill_segments  = fill_segments
        self.iradius_top     = radius_top
        self.iradius_bottom  = radius_bottom
        self.idepth          = depth

        self.socket_in_name = 'ivertices'

    def __repr__(self):
        s = f"Node 'Cone' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vertices        : {self.ivertices}"
        s += f"\n   side_segments   : {self.iside_segments}"
        s += f"\n   fill_segments   : {self.ifill_segments}"
        s += f"\n   radius_top      : {self.iradius_top}"
        s += f"\n   radius_bottom   : {self.iradius_bottom}"
        s += f"\n   depth           : {self.idepth}"
        s += '\nParameters'
        s += f"\n   fill_type       : {self.fill_type}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        s +=  "\n   top             : Boolean"
        s +=  "\n   bottom          : Boolean"
        s +=  "\n   side            : Boolean"
        return s + "\n"

    def check_parameters(self):
        valids = ('NONE', 'NGON', 'TRIANGLE_FAN') 
        if self.fill_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCone'.\n 'fill_type' is '{self.fill_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    @property
    def top(self):
        return self.outputs[1]

    @property
    def bottom(self):
        return self.outputs[2]

    @property
    def side(self):
        return self.outputs[3]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivertices(self):
        return self.inputs[0]

    @ivertices.setter
    def ivertices(self, value):
        self.inputs[0].plug(value)

    @property
    def iside_segments(self):
        return self.inputs[1]

    @iside_segments.setter
    def iside_segments(self, value):
        self.inputs[1].plug(value)

    @property
    def ifill_segments(self):
        return self.inputs[2]

    @ifill_segments.setter
    def ifill_segments(self, value):
        self.inputs[2].plug(value)

    @property
    def iradius_top(self):
        return self.inputs[3]

    @iradius_top.setter
    def iradius_top(self, value):
        self.inputs[3].plug(value)

    @property
    def iradius_bottom(self):
        return self.inputs[4]

    @iradius_bottom.setter
    def iradius_bottom(self, value):
        self.inputs[4].plug(value)

    @property
    def idepth(self):
        return self.inputs[5]

    @idepth.setter
    def idepth(self, value):
        self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshCube

class NodeCube(Node):

    """ Node class GeometryNodeMeshCube

    Input sockets
    -------------

        0: size                 Vector
        1: vertices_x           Integer
        2: vertices_y           Integer
        3: vertices_z           Integer

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None):

        super().__init__('GeometryNodeMeshCube', name='Cube')

        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'size'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices_x'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices_y'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices_z'   ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.isize           = size
        self.ivertices_x     = vertices_x
        self.ivertices_y     = vertices_y
        self.ivertices_z     = vertices_z

        self.socket_in_name = 'isize'

    def __repr__(self):
        s = f"Node 'Cube' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   size            : {self.isize}"
        s += f"\n   vertices_x      : {self.ivertices_x}"
        s += f"\n   vertices_y      : {self.ivertices_y}"
        s += f"\n   vertices_z      : {self.ivertices_z}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def isize(self):
        return self.inputs[0]

    @isize.setter
    def isize(self, value):
        self.inputs[0].plug(value)

    @property
    def ivertices_x(self):
        return self.inputs[1]

    @ivertices_x.setter
    def ivertices_x(self, value):
        self.inputs[1].plug(value)

    @property
    def ivertices_y(self):
        return self.inputs[2]

    @ivertices_y.setter
    def ivertices_y(self, value):
        self.inputs[2].plug(value)

    @property
    def ivertices_z(self):
        return self.inputs[3]

    @ivertices_z.setter
    def ivertices_z(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshCylinder

class NodeCylinder(Node):

    """ Node class GeometryNodeMeshCylinder

    Input sockets
    -------------

        0: vertices             Integer
        1: side_segments        Integer
        2: fill_segments        Integer
        3: radius               Float
        4: depth                Float

    Parameters
    ----------

        fill_type   : 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN') 

    Output sockets
    --------------

        0: mesh                 Geometry
        1: top                  Boolean
        2: side                 Boolean
        3: bottom               Boolean

    """

    PARAMETERS = ['fill_type']

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):

        super().__init__('GeometryNodeMeshCylinder', name='Cylinder')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'side_segments'))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'fill_segments'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'depth'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'top'          ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'side'         ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'bottom'       ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.fill_type       = fill_type
        self.check_parameters()

        # ----- Input sockets

        self.ivertices       = vertices
        self.iside_segments  = side_segments
        self.ifill_segments  = fill_segments
        self.iradius         = radius
        self.idepth          = depth

        self.socket_in_name = 'ivertices'

    def __repr__(self):
        s = f"Node 'Cylinder' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vertices        : {self.ivertices}"
        s += f"\n   side_segments   : {self.iside_segments}"
        s += f"\n   fill_segments   : {self.ifill_segments}"
        s += f"\n   radius          : {self.iradius}"
        s += f"\n   depth           : {self.idepth}"
        s += '\nParameters'
        s += f"\n   fill_type       : {self.fill_type}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        s +=  "\n   top             : Boolean"
        s +=  "\n   side            : Boolean"
        s +=  "\n   bottom          : Boolean"
        return s + "\n"

    def check_parameters(self):
        valids = ('NONE', 'NGON', 'TRIANGLE_FAN') 
        if self.fill_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeCylinder'.\n 'fill_type' is '{self.fill_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    @property
    def top(self):
        return self.outputs[1]

    @property
    def side(self):
        return self.outputs[2]

    @property
    def bottom(self):
        return self.outputs[3]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivertices(self):
        return self.inputs[0]

    @ivertices.setter
    def ivertices(self, value):
        self.inputs[0].plug(value)

    @property
    def iside_segments(self):
        return self.inputs[1]

    @iside_segments.setter
    def iside_segments(self, value):
        self.inputs[1].plug(value)

    @property
    def ifill_segments(self):
        return self.inputs[2]

    @ifill_segments.setter
    def ifill_segments(self, value):
        self.inputs[2].plug(value)

    @property
    def iradius(self):
        return self.inputs[3]

    @iradius.setter
    def iradius(self, value):
        self.inputs[3].plug(value)

    @property
    def idepth(self):
        return self.inputs[4]

    @idepth.setter
    def idepth(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshGrid

class NodeGrid(Node):

    """ Node class GeometryNodeMeshGrid

    Input sockets
    -------------

        0: size_x               Float
        1: size_y               Float
        2: vertices_x           Integer
        3: vertices_y           Integer

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None):

        super().__init__('GeometryNodeMeshGrid', name='Grid')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'size_x'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'size_y'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices_x'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'vertices_y'   ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.isize_x         = size_x
        self.isize_y         = size_y
        self.ivertices_x     = vertices_x
        self.ivertices_y     = vertices_y

        self.socket_in_name = 'isize_x'

    def __repr__(self):
        s = f"Node 'Grid' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   size_x          : {self.isize_x}"
        s += f"\n   size_y          : {self.isize_y}"
        s += f"\n   vertices_x      : {self.ivertices_x}"
        s += f"\n   vertices_y      : {self.ivertices_y}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def isize_x(self):
        return self.inputs[0]

    @isize_x.setter
    def isize_x(self, value):
        self.inputs[0].plug(value)

    @property
    def isize_y(self):
        return self.inputs[1]

    @isize_y.setter
    def isize_y(self, value):
        self.inputs[1].plug(value)

    @property
    def ivertices_x(self):
        return self.inputs[2]

    @ivertices_x.setter
    def ivertices_x(self, value):
        self.inputs[2].plug(value)

    @property
    def ivertices_y(self):
        return self.inputs[3]

    @ivertices_y.setter
    def ivertices_y(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshIcoSphere

class NodeIcoSphere(Node):

    """ Node class GeometryNodeMeshIcoSphere

    Input sockets
    -------------

        0: radius               Float
        1: subdivisions         Integer

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, radius=None, subdivisions=None):

        super().__init__('GeometryNodeMeshIcoSphere', name='Ico Sphere')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'subdivisions' ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.iradius         = radius
        self.isubdivisions   = subdivisions

        self.socket_in_name = 'iradius'

    def __repr__(self):
        s = f"Node 'IcoSphere' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   radius          : {self.iradius}"
        s += f"\n   subdivisions    : {self.isubdivisions}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iradius(self):
        return self.inputs[0]

    @iradius.setter
    def iradius(self, value):
        self.inputs[0].plug(value)

    @property
    def isubdivisions(self):
        return self.inputs[1]

    @isubdivisions.setter
    def isubdivisions(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshLine

class NodeMeshLine(Node):

    """ Node class GeometryNodeMeshLine

    Input sockets
    -------------

        0: count                Integer
        1: resolution           Float
        2: start_location       Vector
        3: offset               Vector

    Parameters
    ----------

        count_mode  : 'TOTAL' in ('TOTAL', 'RESOLUTION') 
        mode        : 'OFFSET' in ('OFFSET', 'END_POINTS') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['count_mode', 'mode']

    def __init__(self, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):

        super().__init__('GeometryNodeMeshLine', name='Mesh Line')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'count'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'resolution'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'start_location'))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'offset'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.count_mode      = count_mode
        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icount          = count
        self.iresolution     = resolution
        self.istart_location = start_location
        self.ioffset         = offset

        self.socket_in_name = 'icount'

    def __repr__(self):
        s = f"Node 'MeshLine' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   count           : {self.icount}"
        s += f"\n   resolution      : {self.iresolution}"
        s += f"\n   start_location  : {self.istart_location}"
        s += f"\n   offset          : {self.ioffset}"
        s += '\nParameters'
        s += f"\n   count_mode      : {self.count_mode}"
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('TOTAL', 'RESOLUTION') 
        if self.count_mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMeshLine'.\n 'count_mode' is '{self.count_mode}'.\n Authorized values are {valids}.")
        valids = ('OFFSET', 'END_POINTS') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMeshLine'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icount(self):
        return self.inputs[0]

    @icount.setter
    def icount(self, value):
        self.inputs[0].plug(value)

    @property
    def iresolution(self):
        return self.inputs[1]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[1].plug(value)

    @property
    def istart_location(self):
        return self.inputs[2]

    @istart_location.setter
    def istart_location(self, value):
        self.inputs[2].plug(value)

    @property
    def ioffset(self):
        return self.inputs[3]

    @ioffset.setter
    def ioffset(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshToCurve

class NodeMeshtoCurve(Node):

    """ Node class GeometryNodeMeshToCurve

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, mesh=None, selection=None):

        super().__init__('GeometryNodeMeshToCurve', name='Mesh to Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'MeshtoCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshToPoints

class NodeMeshtoPoints(Node):

    """ Node class GeometryNodeMeshToPoints

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean
        2: position             Vector
        3: radius               Float

    Parameters
    ----------

        mode        : 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS') 

    Output sockets
    --------------

        0: points               Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, mesh=None, selection=None, position=None, radius=None, mode='VERTICES'):

        super().__init__('GeometryNodeMeshToPoints', name='Mesh to Points')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'position'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'points'       ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'points'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection
        self.iposition       = position
        self.iradius         = radius

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'MeshtoPoints' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   position        : {self.iposition}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   points          : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('VERTICES', 'EDGES', 'FACES', 'CORNERS') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMeshtoPoints'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def points(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iposition(self):
        return self.inputs[2]

    @iposition.setter
    def iposition(self, value):
        self.inputs[2].plug(value)

    @property
    def iradius(self):
        return self.inputs[3]

    @iradius.setter
    def iradius(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeMeshUVSphere

class NodeUVSphere(Node):

    """ Node class GeometryNodeMeshUVSphere

    Input sockets
    -------------

        0: segments             Integer
        1: rings                Integer
        2: radius               Float

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, segments=None, rings=None, radius=None):

        super().__init__('GeometryNodeMeshUVSphere', name='UV Sphere')

        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'segments'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'rings'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.isegments       = segments
        self.irings          = rings
        self.iradius         = radius

        self.socket_in_name = 'isegments'

    def __repr__(self):
        s = f"Node 'UVSphere' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   segments        : {self.isegments}"
        s += f"\n   rings           : {self.irings}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def isegments(self):
        return self.inputs[0]

    @isegments.setter
    def isegments(self, value):
        self.inputs[0].plug(value)

    @property
    def irings(self):
        return self.inputs[1]

    @irings.setter
    def irings(self, value):
        self.inputs[1].plug(value)

    @property
    def iradius(self):
        return self.inputs[2]

    @iradius.setter
    def iradius(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeObjectInfo

class NodeObjectInfo(Node):

    """ Node class GeometryNodeObjectInfo

    Input sockets
    -------------

        0: object               Object
        1: as_instance          Boolean

    Parameters
    ----------

        transform_space: 'ORIGINAL' in ('ORIGINAL', 'RELATIVE') 

    Output sockets
    --------------

        0: location             Vector
        1: rotation             Vector
        2: scale                Vector
        3: geometry             Geometry

    """

    PARAMETERS = ['transform_space']

    def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL'):

        super().__init__('GeometryNodeObjectInfo', name='Object Info')

        self.inputs.add(SocketIn(self, 'NodeSocketObject'       , 'object'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'as_instance'  ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'location'     ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'rotation'     ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'scale'        ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.output_geometry_socket = self.outputs[3]

        self.socket_out_name = 'location'

        # ----- Parameters

        self.transform_space = transform_space
        self.check_parameters()

        # ----- Input sockets

        self.iobject         = object
        self.ias_instance    = as_instance

        self.socket_in_name = 'iobject'

    def __repr__(self):
        s = f"Node 'ObjectInfo' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   object          : {self.iobject}"
        s += f"\n   as_instance     : {self.ias_instance}"
        s += '\nParameters'
        s += f"\n   transform_space : {self.transform_space}"
        s += '\nOutput sockets'
        s +=  "\n   location        : Vector"
        s +=  "\n   rotation        : Vector"
        s +=  "\n   scale           : Vector"
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('ORIGINAL', 'RELATIVE') 
        if self.transform_space not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeObjectInfo'.\n 'transform_space' is '{self.transform_space}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def location(self):
        return self.outputs[0]

    @property
    def rotation(self):
        return self.outputs[1]

    @property
    def scale(self):
        return self.outputs[2]

    @property
    def geometry(self):
        return self.outputs[3]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iobject(self):
        return self.inputs[0]

    @iobject.setter
    def iobject(self, value):
        self.inputs[0].plug(value)

    @property
    def ias_instance(self):
        return self.inputs[1]

    @ias_instance.setter
    def ias_instance(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodePointsToVertices

class NodePointstoVertices(Node):

    """ Node class GeometryNodePointsToVertices

    Input sockets
    -------------

        0: points               Geometry
        1: selection            Boolean

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, points=None, selection=None):

        super().__init__('GeometryNodePointsToVertices', name='Points to Vertices')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'points'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.ipoints         = points
        self.iselection      = selection

        self.socket_in_name = 'ipoints'

    def __repr__(self):
        s = f"Node 'PointstoVertices' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   points          : {self.ipoints}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ipoints(self):
        return self.inputs[0]

    @ipoints.setter
    def ipoints(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodePointsToVolume

class NodePointstoVolume(Node):

    """ Node class GeometryNodePointsToVolume

    Input sockets
    -------------

        0: points               Geometry
        1: density              Float
        2: voxel_size           Float
        3: voxel_amount         Float
        4: radius               Float

    Parameters
    ----------

        resolution_mode: 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE') 

    Output sockets
    --------------

        0: volume               Geometry

    """

    PARAMETERS = ['resolution_mode']

    def __init__(self, points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):

        super().__init__('GeometryNodePointsToVolume', name='Points to Volume')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'points'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'density'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'voxel_size'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'voxel_amount' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'volume'       ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'volume'

        # ----- Parameters

        self.resolution_mode = resolution_mode
        self.check_parameters()

        # ----- Input sockets

        self.ipoints         = points
        self.idensity        = density
        self.ivoxel_size     = voxel_size
        self.ivoxel_amount   = voxel_amount
        self.iradius         = radius

        self.socket_in_name = 'ipoints'

    def __repr__(self):
        s = f"Node 'PointstoVolume' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   points          : {self.ipoints}"
        s += f"\n   density         : {self.idensity}"
        s += f"\n   voxel_size      : {self.ivoxel_size}"
        s += f"\n   voxel_amount    : {self.ivoxel_amount}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nParameters'
        s += f"\n   resolution_mode : {self.resolution_mode}"
        s += '\nOutput sockets'
        s +=  "\n   volume          : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('VOXEL_AMOUNT', 'VOXEL_SIZE') 
        if self.resolution_mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodePointstoVolume'.\n 'resolution_mode' is '{self.resolution_mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def volume(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ipoints(self):
        return self.inputs[0]

    @ipoints.setter
    def ipoints(self, value):
        self.inputs[0].plug(value)

    @property
    def idensity(self):
        return self.inputs[1]

    @idensity.setter
    def idensity(self, value):
        self.inputs[1].plug(value)

    @property
    def ivoxel_size(self):
        return self.inputs[2]

    @ivoxel_size.setter
    def ivoxel_size(self, value):
        self.inputs[2].plug(value)

    @property
    def ivoxel_amount(self):
        return self.inputs[3]

    @ivoxel_amount.setter
    def ivoxel_amount(self, value):
        self.inputs[3].plug(value)

    @property
    def iradius(self):
        return self.inputs[4]

    @iradius.setter
    def iradius(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeProximity

class NodeGeometryProximity(Node):

    """ Node class GeometryNodeProximity

    Input sockets
    -------------

        0: target               Geometry
        1: source_position      Vector

    Parameters
    ----------

        target_element: 'FACES' in ('POINTS', 'EDGES', 'FACES') 

    Output sockets
    --------------

        0: position             Vector
        1: distance             Float

    """

    PARAMETERS = ['target_element']

    def __init__(self, target=None, source_position=None, target_element='FACES'):

        super().__init__('GeometryNodeProximity', name='Geometry Proximity')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'target'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'source_position'))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'position'     ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'distance'     ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'position'

        # ----- Parameters

        self.target_element  = target_element
        self.check_parameters()

        # ----- Input sockets

        self.itarget         = target
        self.isource_position = source_position

        self.socket_in_name = 'itarget'

    def __repr__(self):
        s = f"Node 'GeometryProximity' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   target          : {self.itarget}"
        s += f"\n   source_position : {self.isource_position}"
        s += '\nParameters'
        s += f"\n   target_element  : {self.target_element}"
        s += '\nOutput sockets'
        s +=  "\n   position        : Vector"
        s +=  "\n   distance        : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('POINTS', 'EDGES', 'FACES') 
        if self.target_element not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeGeometryProximity'.\n 'target_element' is '{self.target_element}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def position(self):
        return self.outputs[0]

    @property
    def distance(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def itarget(self):
        return self.inputs[0]

    @itarget.setter
    def itarget(self, value):
        self.inputs[0].plug(value)

    @property
    def isource_position(self):
        return self.inputs[1]

    @isource_position.setter
    def isource_position(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeRaycast

class NodeRaycast(Node):

    """ Node class GeometryNodeRaycast

    Input sockets
    -------------

        0: target_geometry      Geometry
        1: attribute            Vector
        2: attribute            Float
        3: attribute            Color
        4: attribute            Boolean
        5: attribute            Integer
        6: source_position      Vector
        7: ray_direction        Vector
        8: ray_length           Float

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        mapping     : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST') 

    Output sockets
    --------------

        0: is_hit               Boolean
        1: hit_position         Vector
        2: hit_normal           Vector
        3: hit_distance         Float
        4: attribute            Vector
        5: attribute            Float
        6: attribute            Color
        7: attribute            Boolean
        8: attribute            Integer

    """

    PARAMETERS = ['data_type', 'mapping']

    def __init__(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):

        super().__init__('GeometryNodeRaycast', name='Raycast')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'target_geometry'))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'attribute'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'source_position'))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'ray_direction'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'ray_length'   ))

        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'is_hit'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'hit_position' ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'hit_normal'   ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'hit_distance' ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'attribute'    ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'attribute'    ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'is_hit'

        # ----- Parameters

        self.data_type       = data_type
        self.mapping         = mapping
        self.check_parameters()

        # ----- Input sockets

        self.itarget_geometry = target_geometry
        self.iattribute      = attribute
        self.isource_position = source_position
        self.iray_direction  = ray_direction
        self.iray_length     = ray_length

        self.socket_in_name = 'itarget_geometry'

    def __repr__(self):
        s = f"Node 'Raycast' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   target_geometry : {self.itarget_geometry}"
        s += f"\n   attribute       : {self.iattribute}"
        s += f"\n   source_position : {self.isource_position}"
        s += f"\n   ray_direction   : {self.iray_direction}"
        s += f"\n   ray_length      : {self.iray_length}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   mapping         : {self.mapping}"
        s += '\nOutput sockets'
        s +=  "\n   is_hit          : Boolean"
        s +=  "\n   hit_position    : Vector"
        s +=  "\n   hit_normal      : Vector"
        s +=  "\n   hit_distance    : Float"
        s +=  "\n   attribute       : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeRaycast'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('INTERPOLATED', 'NEAREST') 
        if self.mapping not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeRaycast'.\n 'mapping' is '{self.mapping}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def is_hit(self):
        return self.outputs[0]

    @property
    def hit_position(self):
        return self.outputs[1]

    @property
    def hit_normal(self):
        return self.outputs[2]

    @property
    def hit_distance(self):
        return self.outputs[3]

    @property
    def attribute(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.outputs[4]
        elif (self.data_type == 'FLOAT'):
            return self.outputs[5]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.outputs[6]
        elif (self.data_type == 'BOOLEAN'):
            return self.outputs[7]
        elif (self.data_type == 'INT'):
            return self.outputs[8]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def itarget_geometry(self):
        return self.inputs[0]

    @itarget_geometry.setter
    def itarget_geometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iattribute(self):
        if (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[1]
        elif (self.data_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.inputs[3]
        elif (self.data_type == 'BOOLEAN'):
            return self.inputs[4]
        elif (self.data_type == 'INT'):
            return self.inputs[5]

    @iattribute.setter
    def iattribute(self, value):
        if (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_COLOR'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'BOOLEAN'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[5].plug(value)

    @property
    def isource_position(self):
        return self.inputs[6]

    @isource_position.setter
    def isource_position(self, value):
        self.inputs[6].plug(value)

    @property
    def iray_direction(self):
        return self.inputs[7]

    @iray_direction.setter
    def iray_direction(self, value):
        self.inputs[7].plug(value)

    @property
    def iray_length(self):
        return self.inputs[8]

    @iray_length.setter
    def iray_length(self, value):
        self.inputs[8].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeRealizeInstances

class NodeRealizeInstances(Node):

    """ Node class GeometryNodeRealizeInstances

    Input sockets
    -------------

        0: geometry             Geometry

    Parameters
    ----------

        legacy_behavior: False

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = ['legacy_behavior']

    def __init__(self, geometry=None, legacy_behavior=False):

        super().__init__('GeometryNodeRealizeInstances', name='Realize Instances')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Parameters

        self.legacy_behavior = legacy_behavior
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'RealizeInstances' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nParameters'
        s += f"\n   legacy_behavior : {self.legacy_behavior}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeReplaceMaterial

class NodeReplaceMaterial(Node):

    """ Node class GeometryNodeReplaceMaterial

    Input sockets
    -------------

        0: geometry             Geometry
        1: old                  Material
        2: new                  Material

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, old=None, new=None):

        super().__init__('GeometryNodeReplaceMaterial', name='Replace Material')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketMaterial'     , 'old'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketMaterial'     , 'new'          ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iold            = old
        self.inew            = new

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'ReplaceMaterial' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   old             : {self.iold}"
        s += f"\n   new             : {self.inew}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iold(self):
        return self.inputs[1]

    @iold.setter
    def iold(self, value):
        self.inputs[1].plug(value)

    @property
    def inew(self):
        return self.inputs[2]

    @inew.setter
    def inew(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeResampleCurve

class NodeResampleCurve(Node):

    """ Node class GeometryNodeResampleCurve

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean
        2: count                Integer
        3: length               Float

    Parameters
    ----------

        mode        : 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT'):

        super().__init__('GeometryNodeResampleCurve', name='Resample Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'count'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'length'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection
        self.icount          = count
        self.ilength         = length

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'ResampleCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   count           : {self.icount}"
        s += f"\n   length          : {self.ilength}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('EVALUATED', 'COUNT', 'LENGTH') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeResampleCurve'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def icount(self):
        return self.inputs[2]

    @icount.setter
    def icount(self, value):
        self.inputs[2].plug(value)

    @property
    def ilength(self):
        return self.inputs[3]

    @ilength.setter
    def ilength(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeReverseCurve

class NodeReverseCurve(Node):

    """ Node class GeometryNodeReverseCurve

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, curve=None, selection=None):

        super().__init__('GeometryNodeReverseCurve', name='Reverse Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'ReverseCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeRotateInstances

class NodeRotateInstances(Node):

    """ Node class GeometryNodeRotateInstances

    Input sockets
    -------------

        0: instances            Geometry
        1: selection            Boolean
        2: rotation             Vector
        3: pivot_point          Vector
        4: local_space          Boolean

    Output sockets
    --------------

        0: instances            Geometry

    """

    PARAMETERS = []

    def __init__(self, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None):

        super().__init__('GeometryNodeRotateInstances', name='Rotate Instances')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'instances'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotation'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'pivot_point'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'local_space'  ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'instances'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'instances'

        # ----- Input sockets

        self.iinstances      = instances
        self.iselection      = selection
        self.irotation       = rotation
        self.ipivot_point    = pivot_point
        self.ilocal_space    = local_space

        self.socket_in_name = 'iinstances'

    def __repr__(self):
        s = f"Node 'RotateInstances' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   instances       : {self.iinstances}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   rotation        : {self.irotation}"
        s += f"\n   pivot_point     : {self.ipivot_point}"
        s += f"\n   local_space     : {self.ilocal_space}"
        s += '\nOutput sockets'
        s +=  "\n   instances       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def instances(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iinstances(self):
        return self.inputs[0]

    @iinstances.setter
    def iinstances(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def irotation(self):
        return self.inputs[2]

    @irotation.setter
    def irotation(self, value):
        self.inputs[2].plug(value)

    @property
    def ipivot_point(self):
        return self.inputs[3]

    @ipivot_point.setter
    def ipivot_point(self, value):
        self.inputs[3].plug(value)

    @property
    def ilocal_space(self):
        return self.inputs[4]

    @ilocal_space.setter
    def ilocal_space(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSampleCurve

class NodeSampleCurve(Node):

    """ Node class GeometryNodeSampleCurve

    Input sockets
    -------------

        0: curve                Geometry
        1: factor               Float
        2: length               Float

    Parameters
    ----------

        mode        : 'LENGTH' in ('FACTOR', 'LENGTH') 

    Output sockets
    --------------

        0: position             Vector
        1: tangent              Vector
        2: normal               Vector

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, factor=None, length=None, mode='LENGTH'):

        super().__init__('GeometryNodeSampleCurve', name='Sample Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'factor'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'length'       ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'position'     ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'tangent'      ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'normal'       ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = 'position'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.ifactor         = factor
        self.ilength         = length

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SampleCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   factor          : {self.ifactor}"
        s += f"\n   length          : {self.ilength}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   position        : Vector"
        s +=  "\n   tangent         : Vector"
        s +=  "\n   normal          : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('FACTOR', 'LENGTH') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSampleCurve'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def position(self):
        return self.outputs[0]

    @property
    def tangent(self):
        return self.outputs[1]

    @property
    def normal(self):
        return self.outputs[2]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def ifactor(self):
        return self.inputs[1]

    @ifactor.setter
    def ifactor(self, value):
        self.inputs[1].plug(value)

    @property
    def ilength(self):
        return self.inputs[2]

    @ilength.setter
    def ilength(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeScaleElements

class NodeScaleElements(Node):

    """ Node class GeometryNodeScaleElements

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: scale                Float
        3: center               Vector
        4: axis                 Vector

    Parameters
    ----------

        domain      : 'FACE' in ('FACE', 'EDGE') 
        scale_mode  : 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS') 

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = ['domain', 'scale_mode']

    def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):

        super().__init__('GeometryNodeScaleElements', name='Scale Elements')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'center'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'axis'         ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Parameters

        self.domain          = domain
        self.scale_mode      = scale_mode
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.iscale          = scale
        self.icenter         = center
        self.iaxis           = axis

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'ScaleElements' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   center          : {self.icenter}"
        s += f"\n   axis            : {self.iaxis}"
        s += '\nParameters'
        s += f"\n   domain          : {self.domain}"
        s += f"\n   scale_mode      : {self.scale_mode}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('FACE', 'EDGE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeScaleElements'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")
        valids = ('UNIFORM', 'SINGLE_AXIS') 
        if self.scale_mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeScaleElements'.\n 'scale_mode' is '{self.scale_mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iscale(self):
        return self.inputs[2]

    @iscale.setter
    def iscale(self, value):
        self.inputs[2].plug(value)

    @property
    def icenter(self):
        return self.inputs[3]

    @icenter.setter
    def icenter(self, value):
        self.inputs[3].plug(value)

    @property
    def iaxis(self):
        return self.inputs[4]

    @iaxis.setter
    def iaxis(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeScaleInstances

class NodeScaleInstances(Node):

    """ Node class GeometryNodeScaleInstances

    Input sockets
    -------------

        0: instances            Geometry
        1: selection            Boolean
        2: scale                Vector
        3: center               Vector
        4: local_space          Boolean

    Output sockets
    --------------

        0: instances            Geometry

    """

    PARAMETERS = []

    def __init__(self, instances=None, selection=None, scale=None, center=None, local_space=None):

        super().__init__('GeometryNodeScaleInstances', name='Scale Instances')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'instances'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorXYZ'    , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'center'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'local_space'  ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'instances'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'instances'

        # ----- Input sockets

        self.iinstances      = instances
        self.iselection      = selection
        self.iscale          = scale
        self.icenter         = center
        self.ilocal_space    = local_space

        self.socket_in_name = 'iinstances'

    def __repr__(self):
        s = f"Node 'ScaleInstances' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   instances       : {self.iinstances}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   center          : {self.icenter}"
        s += f"\n   local_space     : {self.ilocal_space}"
        s += '\nOutput sockets'
        s +=  "\n   instances       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def instances(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iinstances(self):
        return self.inputs[0]

    @iinstances.setter
    def iinstances(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iscale(self):
        return self.inputs[2]

    @iscale.setter
    def iscale(self, value):
        self.inputs[2].plug(value)

    @property
    def icenter(self):
        return self.inputs[3]

    @icenter.setter
    def icenter(self, value):
        self.inputs[3].plug(value)

    @property
    def ilocal_space(self):
        return self.inputs[4]

    @ilocal_space.setter
    def ilocal_space(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSeparateComponents

class NodeSeparateComponents(Node):

    """ Node class GeometryNodeSeparateComponents

    Input sockets
    -------------

        0: geometry             Geometry

    Output sockets
    --------------

        0: mesh                 Geometry
        1: point_cloud          Geometry
        2: curve                Geometry
        3: volume               Geometry
        4: instances            Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None):

        super().__init__('GeometryNodeSeparateComponents', name='Separate Components')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'point_cloud'  ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'volume'       ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'instances'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.igeometry       = geometry

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SeparateComponents' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        s +=  "\n   point_cloud     : Geometry"
        s +=  "\n   curve           : Geometry"
        s +=  "\n   volume          : Geometry"
        s +=  "\n   instances       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    @property
    def point_cloud(self):
        return self.outputs[1]

    @property
    def curve(self):
        return self.outputs[2]

    @property
    def volume(self):
        return self.outputs[3]

    @property
    def instances(self):
        return self.outputs[4]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSeparateGeometry

class NodeSeparateGeometry(Node):

    """ Node class GeometryNodeSeparateGeometry

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean

    Parameters
    ----------

        domain      : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE') 

    Output sockets
    --------------

        0: selection            Geometry
        1: inverted             Geometry

    """

    PARAMETERS = ['domain']

    def __init__(self, geometry=None, selection=None, domain='POINT'):

        super().__init__('GeometryNodeSeparateGeometry', name='Separate Geometry')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'selection'    ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'inverted'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'selection'

        # ----- Parameters

        self.domain          = domain
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SeparateGeometry' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nParameters'
        s += f"\n   domain          : {self.domain}"
        s += '\nOutput sockets'
        s +=  "\n   selection       : Geometry"
        s +=  "\n   inverted        : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE') 
        if self.domain not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSeparateGeometry'.\n 'domain' is '{self.domain}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def selection(self):
        return self.outputs[0]

    @property
    def inverted(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetCurveHandlePositions

class NodeSetHandlePositions(Node):

    """ Node class GeometryNodeSetCurveHandlePositions

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean
        2: position             Vector
        3: offset               Vector

    Parameters
    ----------

        mode        : 'LEFT' in ('LEFT', 'RIGHT') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, selection=None, position=None, offset=None, mode='LEFT'):

        super().__init__('GeometryNodeSetCurveHandlePositions', name='Set Handle Positions')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'position'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'offset'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection
        self.iposition       = position
        self.ioffset         = offset

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SetHandlePositions' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   position        : {self.iposition}"
        s += f"\n   offset          : {self.ioffset}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('LEFT', 'RIGHT') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSetHandlePositions'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iposition(self):
        return self.inputs[2]

    @iposition.setter
    def iposition(self, value):
        self.inputs[2].plug(value)

    @property
    def ioffset(self):
        return self.inputs[3]

    @ioffset.setter
    def ioffset(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetCurveRadius

class NodeSetCurveRadius(Node):

    """ Node class GeometryNodeSetCurveRadius

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean
        2: radius               Float

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, curve=None, selection=None, radius=None):

        super().__init__('GeometryNodeSetCurveRadius', name='Set Curve Radius')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection
        self.iradius         = radius

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SetCurveRadius' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iradius(self):
        return self.inputs[2]

    @iradius.setter
    def iradius(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetCurveTilt

class NodeSetCurveTilt(Node):

    """ Node class GeometryNodeSetCurveTilt

    Input sockets
    -------------

        0: curve                Geometry
        1: selection            Boolean
        2: tilt                 Float

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, curve=None, selection=None, tilt=None):

        super().__init__('GeometryNodeSetCurveTilt', name='Set Curve Tilt')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'tilt'         ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.icurve          = curve
        self.iselection      = selection
        self.itilt           = tilt

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SetCurveTilt' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   tilt            : {self.itilt}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def itilt(self):
        return self.inputs[2]

    @itilt.setter
    def itilt(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetID

class NodeSetID(Node):

    """ Node class GeometryNodeSetID

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: ID                   Integer

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, ID=None):

        super().__init__('GeometryNodeSetID', name='Set ID')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'ID'           ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.iID             = ID

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetID' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   ID              : {self.iID}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iID(self):
        return self.inputs[2]

    @iID.setter
    def iID(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetMaterial

class NodeSetMaterial(Node):

    """ Node class GeometryNodeSetMaterial

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: material             Material

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, material=None):

        super().__init__('GeometryNodeSetMaterial', name='Set Material')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketMaterial'     , 'material'     ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.imaterial       = material

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetMaterial' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   material        : {self.imaterial}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def imaterial(self):
        return self.inputs[2]

    @imaterial.setter
    def imaterial(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetMaterialIndex

class NodeSetMaterialIndex(Node):

    """ Node class GeometryNodeSetMaterialIndex

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: material_index       Integer

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, material_index=None):

        super().__init__('GeometryNodeSetMaterialIndex', name='Set Material Index')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'material_index'))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.imaterial_index = material_index

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetMaterialIndex' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   material_index  : {self.imaterial_index}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def imaterial_index(self):
        return self.inputs[2]

    @imaterial_index.setter
    def imaterial_index(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetPointRadius

class NodeSetPointRadius(Node):

    """ Node class GeometryNodeSetPointRadius

    Input sockets
    -------------

        0: points               Geometry
        1: selection            Boolean
        2: radius               Float

    Output sockets
    --------------

        0: points               Geometry

    """

    PARAMETERS = []

    def __init__(self, points=None, selection=None, radius=None):

        super().__init__('GeometryNodeSetPointRadius', name='Set Point Radius')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'points'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'radius'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'points'       ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'points'

        # ----- Input sockets

        self.ipoints         = points
        self.iselection      = selection
        self.iradius         = radius

        self.socket_in_name = 'ipoints'

    def __repr__(self):
        s = f"Node 'SetPointRadius' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   points          : {self.ipoints}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   radius          : {self.iradius}"
        s += '\nOutput sockets'
        s +=  "\n   points          : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def points(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ipoints(self):
        return self.inputs[0]

    @ipoints.setter
    def ipoints(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iradius(self):
        return self.inputs[2]

    @iradius.setter
    def iradius(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetPosition

class NodeSetPosition(Node):

    """ Node class GeometryNodeSetPosition

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: position             Vector
        3: offset               Vector

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, position=None, offset=None):

        super().__init__('GeometryNodeSetPosition', name='Set Position')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'position'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'offset'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.iposition       = position
        self.ioffset         = offset

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetPosition' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   position        : {self.iposition}"
        s += f"\n   offset          : {self.ioffset}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iposition(self):
        return self.inputs[2]

    @iposition.setter
    def iposition(self, value):
        self.inputs[2].plug(value)

    @property
    def ioffset(self):
        return self.inputs[3]

    @ioffset.setter
    def ioffset(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetShadeSmooth

class NodeSetShadeSmooth(Node):

    """ Node class GeometryNodeSetShadeSmooth

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: shade_smooth         Boolean

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, shade_smooth=None):

        super().__init__('GeometryNodeSetShadeSmooth', name='Set Shade Smooth')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'shade_smooth' ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.ishade_smooth   = shade_smooth

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetShadeSmooth' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   shade_smooth    : {self.ishade_smooth}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def ishade_smooth(self):
        return self.inputs[2]

    @ishade_smooth.setter
    def ishade_smooth(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetSplineCyclic

class NodeSetSplineCyclic(Node):

    """ Node class GeometryNodeSetSplineCyclic

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: cyclic               Boolean

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, cyclic=None):

        super().__init__('GeometryNodeSetSplineCyclic', name='Set Spline Cyclic')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'cyclic'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.icyclic         = cyclic

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetSplineCyclic' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   cyclic          : {self.icyclic}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def icyclic(self):
        return self.inputs[2]

    @icyclic.setter
    def icyclic(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSetSplineResolution

class NodeSetSplineResolution(Node):

    """ Node class GeometryNodeSetSplineResolution

    Input sockets
    -------------

        0: geometry             Geometry
        1: selection            Boolean
        2: resolution           Integer

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, selection=None, resolution=None):

        super().__init__('GeometryNodeSetSplineResolution', name='Set Spline Resolution')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'resolution'   ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.iselection      = selection
        self.iresolution     = resolution

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'SetSplineResolution' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   resolution      : {self.iresolution}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iresolution(self):
        return self.inputs[2]

    @iresolution.setter
    def iresolution(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeSplineLength

class NodeSplineLength(Attribute):

    """ Node class GeometryNodeSplineLength

    Output sockets
    --------------

        0: length               Float
        1: point_count          Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeSplineLength', name='Spline Length', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'length'       ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'point_count'  ))

        self.socket_out_name = 'length'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'SplineLength' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   length          : Float"
        s +=  "\n   point_count     : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def length(self):
        return self.outputs[0]

    @property
    def point_count(self):
        return self.outputs[1]

# ------------------------------------------------------------------------------------------------------------------------
# Attribute class GeometryNodeSplineParameter

class NodeSplineParameter(Attribute):

    """ Node class GeometryNodeSplineParameter

    Output sockets
    --------------

        0: factor               Float
        1: length               Float
        2: index                Integer

    """

    PARAMETERS = []

    def __init__(self, owner_socket=None, data_type='FLOAT', domain='POINT'):

        super().__init__('GeometryNodeSplineParameter', name='Spline Parameter', owner_socket=owner_socket, data_type=data_type, domain=domain)

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'factor'       ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'length'       ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'index'        ))

        self.socket_out_name = 'factor'

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'SplineParameter' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   factor          : Float"
        s +=  "\n   length          : Float"
        s +=  "\n   index           : Integer"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def factor(self):
        return self.outputs[0]

    @property
    def length(self):
        return self.outputs[1]

    @property
    def index(self):
        return self.outputs[2]

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSplitEdges

class NodeSplitEdges(Node):

    """ Node class GeometryNodeSplitEdges

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, mesh=None, selection=None):

        super().__init__('GeometryNodeSplitEdges', name='Split Edges')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'SplitEdges' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeStringJoin

class NodeJoinStrings(Node):

    """ Node class GeometryNodeStringJoin

    Input sockets
    -------------

        0: delimiter            String
        1: strings              String

    Output sockets
    --------------

        0: string               String

    """

    PARAMETERS = []

    def __init__(self, *strings, delimiter=None):

        super().__init__('GeometryNodeStringJoin', name='Join Strings')

        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'delimiter'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'strings'      , is_multi_input=True))

        self.outputs.add(Socket (self, 'NodeSocketString'       , 'string'       ))

        self.socket_out_name = 'string'

        # ----- Input sockets

        self.idelimiter      = delimiter
        self.istrings        = strings

        self.socket_in_name = 'istrings'

    def __repr__(self):
        s = f"Node 'JoinStrings' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   delimiter       : {self.idelimiter}"
        s += f"\n   strings         : {self.istrings}"
        s += '\nOutput sockets'
        s +=  "\n   string          : String"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def string(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def idelimiter(self):
        return self.inputs[0]

    @idelimiter.setter
    def idelimiter(self, value):
        self.inputs[0].plug(value)

    @property
    def istrings(self):
        return self.inputs[1]

    @istrings.setter
    def istrings(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeStringToCurves

class NodeStringtoCurves(Node):

    """ Node class GeometryNodeStringToCurves

    Input sockets
    -------------

        0: string               String
        1: size                 Float
        2: character_spacing    Float
        3: word_spacing         Float
        4: line_spacing         Float
        5: text_box_width       Float
        6: text_box_height      Float

    Parameters
    ----------

        align_x     : 'LEFT' in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH') 
        align_y     : 'TOP_BASELINE' in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM') 
        overflow    : 'OVERFLOW' in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE') 
        pivot_mode  : 'BOTTOM_LEFT' in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 
                                       'BOTTOM_RIGHT') 

    Output sockets
    --------------

        0: curve_instances      Geometry
        1: remainder            String
        2: line                 Integer
        3: pivot_point          Vector

    """

    PARAMETERS = ['align_x', 'align_y', 'overflow', 'pivot_mode']

    def __init__(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):

        super().__init__('GeometryNodeStringToCurves', name='String to Curves')

        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'string'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'size'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'character_spacing'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'word_spacing' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'line_spacing' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'text_box_width'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'text_box_height'))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve_instances'))
        self.outputs.add(Socket (self, 'NodeSocketString'       , 'remainder'    ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'line'         ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'pivot_point'  ))

        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve_instances'

        # ----- Parameters

        self.align_x         = align_x
        self.align_y         = align_y
        self.overflow        = overflow
        self.pivot_mode      = pivot_mode
        self.check_parameters()

        # ----- Input sockets

        self.istring         = string
        self.isize           = size
        self.icharacter_spacing = character_spacing
        self.iword_spacing   = word_spacing
        self.iline_spacing   = line_spacing
        self.itext_box_width = text_box_width
        self.itext_box_height = text_box_height

        self.socket_in_name = 'istring'

    def __repr__(self):
        s = f"Node 'StringtoCurves' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   string          : {self.istring}"
        s += f"\n   size            : {self.isize}"
        s += f"\n   character_spacing : {self.icharacter_spacing}"
        s += f"\n   word_spacing    : {self.iword_spacing}"
        s += f"\n   line_spacing    : {self.iline_spacing}"
        s += f"\n   text_box_width  : {self.itext_box_width}"
        s += f"\n   text_box_height : {self.itext_box_height}"
        s += '\nParameters'
        s += f"\n   align_x         : {self.align_x}"
        s += f"\n   align_y         : {self.align_y}"
        s += f"\n   overflow        : {self.overflow}"
        s += f"\n   pivot_mode      : {self.pivot_mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve_instances : Geometry"
        s +=  "\n   remainder       : String"
        s +=  "\n   line            : Integer"
        s +=  "\n   pivot_point     : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH') 
        if self.align_x not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeStringtoCurves'.\n 'align_x' is '{self.align_x}'.\n Authorized values are {valids}.")
        valids = ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM') 
        if self.align_y not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeStringtoCurves'.\n 'align_y' is '{self.align_y}'.\n Authorized values are {valids}.")
        valids = ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE') 
        if self.overflow not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeStringtoCurves'.\n 'overflow' is '{self.overflow}'.\n Authorized values are {valids}.")
        valids = ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT') 
        if self.pivot_mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeStringtoCurves'.\n 'pivot_mode' is '{self.pivot_mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve_instances(self):
        return self.outputs[0]

    @property
    def remainder(self):
        return self.outputs[1]

    @property
    def line(self):
        return self.outputs[2]

    @property
    def pivot_point(self):
        return self.outputs[3]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def istring(self):
        return self.inputs[0]

    @istring.setter
    def istring(self, value):
        self.inputs[0].plug(value)

    @property
    def isize(self):
        return self.inputs[1]

    @isize.setter
    def isize(self, value):
        self.inputs[1].plug(value)

    @property
    def icharacter_spacing(self):
        return self.inputs[2]

    @icharacter_spacing.setter
    def icharacter_spacing(self, value):
        self.inputs[2].plug(value)

    @property
    def iword_spacing(self):
        return self.inputs[3]

    @iword_spacing.setter
    def iword_spacing(self, value):
        self.inputs[3].plug(value)

    @property
    def iline_spacing(self):
        return self.inputs[4]

    @iline_spacing.setter
    def iline_spacing(self, value):
        self.inputs[4].plug(value)

    @property
    def itext_box_width(self):
        return self.inputs[5]

    @itext_box_width.setter
    def itext_box_width(self, value):
        self.inputs[5].plug(value)

    @property
    def itext_box_height(self):
        return self.inputs[6]

    @itext_box_height.setter
    def itext_box_height(self, value):
        self.inputs[6].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSubdivideCurve

class NodeSubdivideCurve(Node):

    """ Node class GeometryNodeSubdivideCurve

    Input sockets
    -------------

        0: curve                Geometry
        1: cuts                 Integer

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = []

    def __init__(self, curve=None, cuts=None):

        super().__init__('GeometryNodeSubdivideCurve', name='Subdivide Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'cuts'         ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Input sockets

        self.icurve          = curve
        self.icuts           = cuts

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'SubdivideCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   cuts            : {self.icuts}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def icuts(self):
        return self.inputs[1]

    @icuts.setter
    def icuts(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSubdivideMesh

class NodeSubdivideMesh(Node):

    """ Node class GeometryNodeSubdivideMesh

    Input sockets
    -------------

        0: mesh                 Geometry
        1: level                Integer

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = []

    def __init__(self, mesh=None, level=None):

        super().__init__('GeometryNodeSubdivideMesh', name='Subdivide Mesh')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'level'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Input sockets

        self.imesh           = mesh
        self.ilevel          = level

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'SubdivideMesh' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   level           : {self.ilevel}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def ilevel(self):
        return self.inputs[1]

    @ilevel.setter
    def ilevel(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSubdivisionSurface

class NodeSubdivisionSurface(Node):

    """ Node class GeometryNodeSubdivisionSurface

    Input sockets
    -------------

        0: mesh                 Geometry
        1: level                Integer
        2: crease               Float

    Parameters
    ----------

        boundary_smooth: 'ALL' in ('PRESERVE_CORNERS', 'ALL') 
        uv_smooth   : 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 
                                               'PRESERVE_BOUNDARIES', 'SMOOTH_ALL') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['boundary_smooth', 'uv_smooth']

    def __init__(self, mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):

        super().__init__('GeometryNodeSubdivisionSurface', name='Subdivision Surface')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'level'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'crease'       ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.boundary_smooth = boundary_smooth
        self.uv_smooth       = uv_smooth
        self.check_parameters()

        # ----- Input sockets

        self.imesh           = mesh
        self.ilevel          = level
        self.icrease         = crease

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'SubdivisionSurface' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   level           : {self.ilevel}"
        s += f"\n   crease          : {self.icrease}"
        s += '\nParameters'
        s += f"\n   boundary_smooth : {self.boundary_smooth}"
        s += f"\n   uv_smooth       : {self.uv_smooth}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('PRESERVE_CORNERS', 'ALL') 
        if self.boundary_smooth not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSubdivisionSurface'.\n 'boundary_smooth' is '{self.boundary_smooth}'.\n Authorized values are {valids}.")
        valids = ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 
                 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL') 
        if self.uv_smooth not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSubdivisionSurface'.\n 'uv_smooth' is '{self.uv_smooth}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def ilevel(self):
        return self.inputs[1]

    @ilevel.setter
    def ilevel(self, value):
        self.inputs[1].plug(value)

    @property
    def icrease(self):
        return self.inputs[2]

    @icrease.setter
    def icrease(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeSwitch

class NodeSwitch(Node):

    """ Node class GeometryNodeSwitch

    Input sockets
    -------------

        0: switch               Boolean
        1: switch               Boolean
        2: false                Float
        3: true                 Float
        4: false                Integer
        5: true                 Integer
        6: false                Boolean
        7: true                 Boolean
        8: false                Vector
        9: true                 Vector
        10: false                Color
        11: true                 Color
        12: false                String
        13: true                 String
        14: false                Geometry
        15: true                 Geometry
        16: false                Object
        17: true                 Object
        18: false                Collection
        19: true                 Collection
        20: false                Texture
        21: true                 Texture
        22: false                Material
        23: true                 Material
        24: false                Image
        25: true                 Image

    Parameters
    ----------

        input_type  : 'GEOMETRY' in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 
                                    'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL') 

    Output sockets
    --------------

        0: output               Float
        1: output               Integer
        2: output               Boolean
        3: output               Vector
        4: output               Color
        5: output               String
        6: output               Geometry
        7: output               Object
        8: output               Collection
        9: output               Texture
        10: output               Material
        11: output               Image

    """

    PARAMETERS = ['input_type']

    def __init__(self, switch=None, false=None, true=None, input_type='GEOMETRY'):

        super().__init__('GeometryNodeSwitch', name='Switch')

        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'switch'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'switch'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketString'       , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketObject'       , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketObject'       , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketCollection'   , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketCollection'   , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketTexture'      , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketTexture'      , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketMaterial'     , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketMaterial'     , 'true'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketImage'        , 'false'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketImage'        , 'true'         ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketInt'          , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketBool'         , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketString'       , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketObject'       , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketCollection'   , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketTexture'      , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketMaterial'     , 'output'       ))
        self.outputs.add(Socket (self, 'NodeSocketImage'        , 'output'       ))

        self.input_geometry_socket = self.inputs[14]
        self.output_geometry_socket = self.outputs[6]

        self.socket_out_name = 'output'

        # ----- Parameters

        self.input_type      = input_type
        self.check_parameters()

        # ----- Input sockets

        self.iswitch         = switch
        self.ifalse          = false
        self.itrue           = true

        self.socket_in_name = 'iswitch'

    def __repr__(self):
        s = f"Node 'Switch' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   switch          : {self.iswitch}"
        s += f"\n   false           : {self.ifalse}"
        s += f"\n   true            : {self.itrue}"
        s += '\nParameters'
        s += f"\n   input_type      : {self.input_type}"
        s += '\nOutput sockets'
        s +=  "\n   output          : variable"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 
                 'TEXTURE', 'MATERIAL') 
        if self.input_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeSwitch'.\n 'input_type' is '{self.input_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def output(self):
        if (self.input_type == 'FLOAT'):
            return self.outputs[0]
        elif (self.input_type == 'INT'):
            return self.outputs[1]
        elif (self.input_type == 'BOOLEAN'):
            return self.outputs[2]
        elif (self.input_type == 'VECTOR'):
            return self.outputs[3]
        elif (self.input_type == 'RGBA'):
            return self.outputs[4]
        elif (self.input_type == 'STRING'):
            return self.outputs[5]
        elif (self.input_type == 'GEOMETRY'):
            return self.outputs[6]
        elif (self.input_type == 'OBJECT'):
            return self.outputs[7]
        elif (self.input_type == 'COLLECTION'):
            return self.outputs[8]
        elif (self.input_type == 'TEXTURE'):
            return self.outputs[9]
        elif (self.input_type == 'MATERIAL'):
            return self.outputs[10]
        elif (self.input_type == 'IMAGE'):
            return self.outputs[11]
        self.check_parameters()

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iswitch(self):
        if (self.input_type in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA']):
            return self.inputs[0]
        elif (self.input_type in ['OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL']):
            return self.inputs[1]

    @iswitch.setter
    def iswitch(self, value):
        if (self.input_type in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA']):
            self.inputs[0].plug(value)
        elif (self.input_type in ['OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL']):
            self.inputs[1].plug(value)

    @property
    def ifalse(self):
        if (self.input_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.input_type == 'INT'):
            return self.inputs[4]
        elif (self.input_type == 'BOOLEAN'):
            return self.inputs[6]
        elif (self.input_type == 'VECTOR'):
            return self.inputs[8]
        elif (self.input_type == 'RGBA'):
            return self.inputs[10]
        elif (self.input_type == 'STRING'):
            return self.inputs[12]
        elif (self.input_type == 'GEOMETRY'):
            return self.inputs[14]
        elif (self.input_type == 'OBJECT'):
            return self.inputs[16]
        elif (self.input_type == 'COLLECTION'):
            return self.inputs[18]
        elif (self.input_type == 'TEXTURE'):
            return self.inputs[20]
        elif (self.input_type == 'MATERIAL'):
            return self.inputs[22]
        elif (self.input_type == 'IMAGE'):
            return self.inputs[24]

    @ifalse.setter
    def ifalse(self, value):
        if (self.input_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.input_type == 'INT'):
            self.inputs[4].plug(value)
        elif (self.input_type == 'BOOLEAN'):
            self.inputs[6].plug(value)
        elif (self.input_type == 'VECTOR'):
            self.inputs[8].plug(value)
        elif (self.input_type == 'RGBA'):
            self.inputs[10].plug(value)
        elif (self.input_type == 'STRING'):
            self.inputs[12].plug(value)
        elif (self.input_type == 'GEOMETRY'):
            self.inputs[14].plug(value)
        elif (self.input_type == 'OBJECT'):
            self.inputs[16].plug(value)
        elif (self.input_type == 'COLLECTION'):
            self.inputs[18].plug(value)
        elif (self.input_type == 'TEXTURE'):
            self.inputs[20].plug(value)
        elif (self.input_type == 'MATERIAL'):
            self.inputs[22].plug(value)
        elif (self.input_type == 'IMAGE'):
            self.inputs[24].plug(value)

    @property
    def itrue(self):
        if (self.input_type == 'FLOAT'):
            return self.inputs[3]
        elif (self.input_type == 'INT'):
            return self.inputs[5]
        elif (self.input_type == 'BOOLEAN'):
            return self.inputs[7]
        elif (self.input_type == 'VECTOR'):
            return self.inputs[9]
        elif (self.input_type == 'RGBA'):
            return self.inputs[11]
        elif (self.input_type == 'STRING'):
            return self.inputs[13]
        elif (self.input_type == 'GEOMETRY'):
            return self.inputs[15]
        elif (self.input_type == 'OBJECT'):
            return self.inputs[17]
        elif (self.input_type == 'COLLECTION'):
            return self.inputs[19]
        elif (self.input_type == 'TEXTURE'):
            return self.inputs[21]
        elif (self.input_type == 'MATERIAL'):
            return self.inputs[23]
        elif (self.input_type == 'IMAGE'):
            return self.inputs[25]

    @itrue.setter
    def itrue(self, value):
        if (self.input_type == 'FLOAT'):
            self.inputs[3].plug(value)
        elif (self.input_type == 'INT'):
            self.inputs[5].plug(value)
        elif (self.input_type == 'BOOLEAN'):
            self.inputs[7].plug(value)
        elif (self.input_type == 'VECTOR'):
            self.inputs[9].plug(value)
        elif (self.input_type == 'RGBA'):
            self.inputs[11].plug(value)
        elif (self.input_type == 'STRING'):
            self.inputs[13].plug(value)
        elif (self.input_type == 'GEOMETRY'):
            self.inputs[15].plug(value)
        elif (self.input_type == 'OBJECT'):
            self.inputs[17].plug(value)
        elif (self.input_type == 'COLLECTION'):
            self.inputs[19].plug(value)
        elif (self.input_type == 'TEXTURE'):
            self.inputs[21].plug(value)
        elif (self.input_type == 'MATERIAL'):
            self.inputs[23].plug(value)
        elif (self.input_type == 'IMAGE'):
            self.inputs[25].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeTransform

class NodeTransform(Node):

    """ Node class GeometryNodeTransform

    Input sockets
    -------------

        0: geometry             Geometry
        1: translation          Vector
        2: rotation             Vector
        3: scale                Vector

    Output sockets
    --------------

        0: geometry             Geometry

    """

    PARAMETERS = []

    def __init__(self, geometry=None, translation=None, rotation=None, scale=None):

        super().__init__('GeometryNodeTransform', name='Transform')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'translation'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotation'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorXYZ'    , 'scale'        ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'geometry'     ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'geometry'

        # ----- Input sockets

        self.igeometry       = geometry
        self.itranslation    = translation
        self.irotation       = rotation
        self.iscale          = scale

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'Transform' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   translation     : {self.itranslation}"
        s += f"\n   rotation        : {self.irotation}"
        s += f"\n   scale           : {self.iscale}"
        s += '\nOutput sockets'
        s +=  "\n   geometry        : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def geometry(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def itranslation(self):
        return self.inputs[1]

    @itranslation.setter
    def itranslation(self, value):
        self.inputs[1].plug(value)

    @property
    def irotation(self):
        return self.inputs[2]

    @irotation.setter
    def irotation(self, value):
        self.inputs[2].plug(value)

    @property
    def iscale(self):
        return self.inputs[3]

    @iscale.setter
    def iscale(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeTranslateInstances

class NodeTranslateInstances(Node):

    """ Node class GeometryNodeTranslateInstances

    Input sockets
    -------------

        0: instances            Geometry
        1: selection            Boolean
        2: translation          Vector
        3: local_space          Boolean

    Output sockets
    --------------

        0: instances            Geometry

    """

    PARAMETERS = []

    def __init__(self, instances=None, selection=None, translation=None, local_space=None):

        super().__init__('GeometryNodeTranslateInstances', name='Translate Instances')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'instances'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorTranslation', 'translation'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'local_space'  ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'instances'    ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'instances'

        # ----- Input sockets

        self.iinstances      = instances
        self.iselection      = selection
        self.itranslation    = translation
        self.ilocal_space    = local_space

        self.socket_in_name = 'iinstances'

    def __repr__(self):
        s = f"Node 'TranslateInstances' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   instances       : {self.iinstances}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   translation     : {self.itranslation}"
        s += f"\n   local_space     : {self.ilocal_space}"
        s += '\nOutput sockets'
        s +=  "\n   instances       : Geometry"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def instances(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iinstances(self):
        return self.inputs[0]

    @iinstances.setter
    def iinstances(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def itranslation(self):
        return self.inputs[2]

    @itranslation.setter
    def itranslation(self, value):
        self.inputs[2].plug(value)

    @property
    def ilocal_space(self):
        return self.inputs[3]

    @ilocal_space.setter
    def ilocal_space(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeTriangulate

class NodeTriangulate(Node):

    """ Node class GeometryNodeTriangulate

    Input sockets
    -------------

        0: mesh                 Geometry
        1: selection            Boolean
        2: minimum_vertices     Integer

    Parameters
    ----------

        ngon_method : 'BEAUTY' in ('BEAUTY', 'CLIP') 
        quad_method : 'SHORTEST_DIAGONAL' in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['ngon_method', 'quad_method']

    def __init__(self, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

        super().__init__('GeometryNodeTriangulate', name='Triangulate')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'mesh'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'selection'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'minimum_vertices'))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.ngon_method     = ngon_method
        self.quad_method     = quad_method
        self.check_parameters()

        # ----- Input sockets

        self.imesh           = mesh
        self.iselection      = selection
        self.iminimum_vertices = minimum_vertices

        self.socket_in_name = 'imesh'

    def __repr__(self):
        s = f"Node 'Triangulate' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   mesh            : {self.imesh}"
        s += f"\n   selection       : {self.iselection}"
        s += f"\n   minimum_vertices : {self.iminimum_vertices}"
        s += '\nParameters'
        s += f"\n   ngon_method     : {self.ngon_method}"
        s += f"\n   quad_method     : {self.quad_method}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('BEAUTY', 'CLIP') 
        if self.ngon_method not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeTriangulate'.\n 'ngon_method' is '{self.ngon_method}'.\n Authorized values are {valids}.")
        valids = ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL') 
        if self.quad_method not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeTriangulate'.\n 'quad_method' is '{self.quad_method}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def imesh(self):
        return self.inputs[0]

    @imesh.setter
    def imesh(self, value):
        self.inputs[0].plug(value)

    @property
    def iselection(self):
        return self.inputs[1]

    @iselection.setter
    def iselection(self, value):
        self.inputs[1].plug(value)

    @property
    def iminimum_vertices(self):
        return self.inputs[2]

    @iminimum_vertices.setter
    def iminimum_vertices(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeTrimCurve

class NodeTrimCurve(Node):

    """ Node class GeometryNodeTrimCurve

    Input sockets
    -------------

        0: curve                Geometry
        1: start                Float
        2: end                  Float
        3: start                Float
        4: end                  Float

    Parameters
    ----------

        mode        : 'FACTOR' in ('FACTOR', 'LENGTH') 

    Output sockets
    --------------

        0: curve                Geometry

    """

    PARAMETERS = ['mode']

    def __init__(self, curve=None, start=None, end=None, mode='FACTOR'):

        super().__init__('GeometryNodeTrimCurve', name='Trim Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'curve'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'start'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'end'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'start'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'end'          ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'curve'        ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'curve'

        # ----- Parameters

        self.mode            = mode
        self.check_parameters()

        # ----- Input sockets

        self.icurve          = curve
        self.istart          = start
        self.iend            = end

        self.socket_in_name = 'icurve'

    def __repr__(self):
        s = f"Node 'TrimCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   curve           : {self.icurve}"
        s += f"\n   start           : {self.istart}"
        s += f"\n   end             : {self.iend}"
        s += '\nParameters'
        s += f"\n   mode            : {self.mode}"
        s += '\nOutput sockets'
        s +=  "\n   curve           : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('FACTOR', 'LENGTH') 
        if self.mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeTrimCurve'.\n 'mode' is '{self.mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def curve(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def icurve(self):
        return self.inputs[0]

    @icurve.setter
    def icurve(self, value):
        self.inputs[0].plug(value)

    @property
    def istart(self):
        if (self.mode == 'FACTOR'):
            return self.inputs[1]
        elif (self.mode == 'LENGTH'):
            return self.inputs[3]

    @istart.setter
    def istart(self, value):
        if (self.mode == 'FACTOR'):
            self.inputs[1].plug(value)
        elif (self.mode == 'LENGTH'):
            self.inputs[3].plug(value)

    @property
    def iend(self):
        if (self.mode == 'FACTOR'):
            return self.inputs[2]
        elif (self.mode == 'LENGTH'):
            return self.inputs[4]

    @iend.setter
    def iend(self, value):
        if (self.mode == 'FACTOR'):
            self.inputs[2].plug(value)
        elif (self.mode == 'LENGTH'):
            self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeViewer

class NodeViewer(Node):

    """ Node class GeometryNodeViewer

    Input sockets
    -------------

        0: geometry             Geometry
        1: value                Float
        2: value                Vector
        3: value                Color
        4: value                Integer
        5: value                Boolean

    Parameters
    ----------

        data_type   : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 

    """

    PARAMETERS = ['data_type']

    def __init__(self, geometry=None, value=None, data_type='FLOAT'):

        super().__init__('GeometryNodeViewer', name='Viewer')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketInt'          , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketBool'         , 'value'        ))

        self.input_geometry_socket = self.inputs[0]

        self.socket_out_name = None

        # ----- Parameters

        self.data_type       = data_type
        self.check_parameters()

        # ----- Input sockets

        self.igeometry       = geometry
        self.ivalue          = value

        self.socket_in_name = 'igeometry'

    def __repr__(self):
        s = f"Node 'Viewer' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   geometry        : {self.igeometry}"
        s += f"\n   value           : {self.ivalue}"
        s += '\nParameters'
        s += f"\n   data_type       : {self.data_type}"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeViewer'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def igeometry(self):
        return self.inputs[0]

    @igeometry.setter
    def igeometry(self, value):
        self.inputs[0].plug(value)

    @property
    def ivalue(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[1]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_COLOR'):
            return self.inputs[3]
        elif (self.data_type == 'INT'):
            return self.inputs[4]
        elif (self.data_type == 'BOOLEAN'):
            return self.inputs[5]

    @ivalue.setter
    def ivalue(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_COLOR'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'INT'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'BOOLEAN'):
            self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class GeometryNodeVolumeToMesh

class NodeVolumetoMesh(Node):

    """ Node class GeometryNodeVolumeToMesh

    Input sockets
    -------------

        0: volume               Geometry
        1: voxel_size           Float
        2: voxel_amount         Float
        3: threshold            Float
        4: adaptivity           Float

    Parameters
    ----------

        resolution_mode: 'GRID' in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE') 

    Output sockets
    --------------

        0: mesh                 Geometry

    """

    PARAMETERS = ['resolution_mode']

    def __init__(self, volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):

        super().__init__('GeometryNodeVolumeToMesh', name='Volume to Mesh')

        self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'volume'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatDistance', 'voxel_size'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'voxel_amount' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'threshold'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'adaptivity'   ))

        self.outputs.add(Socket (self, 'NodeSocketGeometry'     , 'mesh'         ))

        self.input_geometry_socket = self.inputs[0]
        self.output_geometry_socket = self.outputs[0]

        self.socket_out_name = 'mesh'

        # ----- Parameters

        self.resolution_mode = resolution_mode
        self.check_parameters()

        # ----- Input sockets

        self.ivolume         = volume
        self.ivoxel_size     = voxel_size
        self.ivoxel_amount   = voxel_amount
        self.ithreshold      = threshold
        self.iadaptivity     = adaptivity

        self.socket_in_name = 'ivolume'

    def __repr__(self):
        s = f"Node 'VolumetoMesh' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   volume          : {self.ivolume}"
        s += f"\n   voxel_size      : {self.ivoxel_size}"
        s += f"\n   voxel_amount    : {self.ivoxel_amount}"
        s += f"\n   threshold       : {self.ithreshold}"
        s += f"\n   adaptivity      : {self.iadaptivity}"
        s += '\nParameters'
        s += f"\n   resolution_mode : {self.resolution_mode}"
        s += '\nOutput sockets'
        s +=  "\n   mesh            : Geometry"
        return s + "\n"

    def check_parameters(self):
        valids = ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE') 
        if self.resolution_mode not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeVolumetoMesh'.\n 'resolution_mode' is '{self.resolution_mode}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def mesh(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivolume(self):
        return self.inputs[0]

    @ivolume.setter
    def ivolume(self, value):
        self.inputs[0].plug(value)

    @property
    def ivoxel_size(self):
        return self.inputs[1]

    @ivoxel_size.setter
    def ivoxel_size(self, value):
        self.inputs[1].plug(value)

    @property
    def ivoxel_amount(self):
        return self.inputs[2]

    @ivoxel_amount.setter
    def ivoxel_amount(self, value):
        self.inputs[2].plug(value)

    @property
    def ithreshold(self):
        return self.inputs[3]

    @ithreshold.setter
    def ithreshold(self, value):
        self.inputs[3].plug(value)

    @property
    def iadaptivity(self):
        return self.inputs[4]

    @iadaptivity.setter
    def iadaptivity(self, value):
        self.inputs[4].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeClamp

class NodeClamp(Node):

    """ Node class ShaderNodeClamp

    Input sockets
    -------------

        0: value                Float
        1: min                  Float
        2: max                  Float

    Parameters
    ----------

        clamp_type  : 'MINMAX' in ('MINMAX', 'RANGE') 

    Output sockets
    --------------

        0: result               Float

    """

    PARAMETERS = ['clamp_type']

    def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX'):

        super().__init__('ShaderNodeClamp', name='Clamp')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'min'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'max'          ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'result'       ))

        self.socket_out_name = 'result'

        # ----- Parameters

        self.clamp_type      = clamp_type
        self.check_parameters()

        # ----- Input sockets

        self.ivalue          = value
        self.imin            = min
        self.imax            = max

        self.socket_in_name = 'ivalue'

    def __repr__(self):
        s = f"Node 'Clamp' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   value           : {self.ivalue}"
        s += f"\n   min             : {self.imin}"
        s += f"\n   max             : {self.imax}"
        s += '\nParameters'
        s += f"\n   clamp_type      : {self.clamp_type}"
        s += '\nOutput sockets'
        s +=  "\n   result          : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('MINMAX', 'RANGE') 
        if self.clamp_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeClamp'.\n 'clamp_type' is '{self.clamp_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def result(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivalue(self):
        return self.inputs[0]

    @ivalue.setter
    def ivalue(self, value):
        self.inputs[0].plug(value)

    @property
    def imin(self):
        return self.inputs[1]

    @imin.setter
    def imin(self, value):
        self.inputs[1].plug(value)

    @property
    def imax(self):
        return self.inputs[2]

    @imax.setter
    def imax(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeCombineRGB

class NodeCombineRGB(Node):

    """ Node class ShaderNodeCombineRGB

    Input sockets
    -------------

        0: r                    Float
        1: g                    Float
        2: b                    Float

    Output sockets
    --------------

        0: image                Color

    """

    PARAMETERS = []

    def __init__(self, r=None, g=None, b=None):

        super().__init__('ShaderNodeCombineRGB', name='Combine RGB')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'r'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'g'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'b'            ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'image'        ))

        self.socket_out_name = 'image'

        # ----- Input sockets

        self.ir              = r
        self.ig              = g
        self.ib              = b

        self.socket_in_name = 'ir'

    def __repr__(self):
        s = f"Node 'CombineRGB' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   r               : {self.ir}"
        s += f"\n   g               : {self.ig}"
        s += f"\n   b               : {self.ib}"
        s += '\nOutput sockets'
        s +=  "\n   image           : Color"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def image(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ir(self):
        return self.inputs[0]

    @ir.setter
    def ir(self, value):
        self.inputs[0].plug(value)

    @property
    def ig(self):
        return self.inputs[1]

    @ig.setter
    def ig(self, value):
        self.inputs[1].plug(value)

    @property
    def ib(self):
        return self.inputs[2]

    @ib.setter
    def ib(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeCombineXYZ

class NodeCombineXYZ(Node):

    """ Node class ShaderNodeCombineXYZ

    Input sockets
    -------------

        0: x                    Float
        1: y                    Float
        2: z                    Float

    Output sockets
    --------------

        0: vector               Vector

    """

    PARAMETERS = []

    def __init__(self, x=None, y=None, z=None):

        super().__init__('ShaderNodeCombineXYZ', name='Combine XYZ')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'x'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'y'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'z'            ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'vector'       ))

        self.socket_out_name = 'vector'

        # ----- Input sockets

        self.ix              = x
        self.iy              = y
        self.iz              = z

        self.socket_in_name = 'ix'

    def __repr__(self):
        s = f"Node 'CombineXYZ' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   x               : {self.ix}"
        s += f"\n   y               : {self.iy}"
        s += f"\n   z               : {self.iz}"
        s += '\nOutput sockets'
        s +=  "\n   vector          : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vector(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ix(self):
        return self.inputs[0]

    @ix.setter
    def ix(self, value):
        self.inputs[0].plug(value)

    @property
    def iy(self):
        return self.inputs[1]

    @iy.setter
    def iy(self, value):
        self.inputs[1].plug(value)

    @property
    def iz(self):
        return self.inputs[2]

    @iz.setter
    def iz(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeFloatCurve

class NodeFloatCurve(Node):

    """ Node class ShaderNodeFloatCurve

    Input sockets
    -------------

        0: factor               Float
        1: value                Float

    Output sockets
    --------------

        0: value                Float

    """

    PARAMETERS = []

    def __init__(self, factor=None, value=None):

        super().__init__('ShaderNodeFloatCurve', name='Float Curve')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'factor'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))

        self.socket_out_name = 'value'

        # ----- Input sockets

        self.ifactor         = factor
        self.ivalue          = value

        self.socket_in_name = 'ifactor'

    def __repr__(self):
        s = f"Node 'FloatCurve' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   factor          : {self.ifactor}"
        s += f"\n   value           : {self.ivalue}"
        s += '\nOutput sockets'
        s +=  "\n   value           : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def value(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ifactor(self):
        return self.inputs[0]

    @ifactor.setter
    def ifactor(self, value):
        self.inputs[0].plug(value)

    @property
    def ivalue(self):
        return self.inputs[1]

    @ivalue.setter
    def ivalue(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeMapRange

class NodeMapRange(Node):

    """ Node class ShaderNodeMapRange

    Input sockets
    -------------

        0: value                Float
        1: from_min             Float
        2: from_max             Float
        3: to_min               Float
        4: to_max               Float
        5: steps                Float
        6: vector               Vector
        7: from_min             Vector
        8: from_max             Vector
        9: to_min               Vector
        10: to_max               Vector
        11: steps                Vector

    Parameters
    ----------

        clamp       : True
        data_type   : 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR') 
        interpolation_type: 'LINEAR' in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP') 

    Output sockets
    --------------

        0: result               Float
        1: vector               Vector

    """

    PARAMETERS = ['clamp', 'data_type', 'interpolation_type']

    def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR'):

        super().__init__('ShaderNodeMapRange', name='Map Range')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'from_min'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'from_max'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'to_min'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'to_max'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'steps'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'from_min'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'from_max'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'to_min'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'to_max'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'steps'        ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'result'       ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'vector'       ))

        self.socket_out_name = 'result'

        # ----- Parameters

        self.clamp           = clamp
        self.data_type       = data_type
        self.interpolation_type = interpolation_type
        self.check_parameters()

        # ----- Input sockets

        self.ivalue          = value
        self.ifrom_min       = from_min
        self.ifrom_max       = from_max
        self.ito_min         = to_min
        self.ito_max         = to_max
        self.isteps          = steps
        self.ivector         = vector

        self.socket_in_name = 'ivalue'

    def __repr__(self):
        s = f"Node 'MapRange' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   value           : {self.ivalue}"
        s += f"\n   from_min        : {self.ifrom_min}"
        s += f"\n   from_max        : {self.ifrom_max}"
        s += f"\n   to_min          : {self.ito_min}"
        s += f"\n   to_max          : {self.ito_max}"
        s += f"\n   steps           : {self.isteps}"
        s += f"\n   vector          : {self.ivector}"
        s += '\nParameters'
        s += f"\n   clamp           : {self.clamp}"
        s += f"\n   data_type       : {self.data_type}"
        s += f"\n   interpolation_type : {self.interpolation_type}"
        s += '\nOutput sockets'
        s +=  "\n   result          : Float"
        s +=  "\n   vector          : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('FLOAT', 'FLOAT_VECTOR') 
        if self.data_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMapRange'.\n 'data_type' is '{self.data_type}'.\n Authorized values are {valids}.")
        valids = ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP') 
        if self.interpolation_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMapRange'.\n 'interpolation_type' is '{self.interpolation_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def result(self):
        return self.outputs[0]

    @property
    def vector(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivalue(self):
        return self.inputs[0]

    @ivalue.setter
    def ivalue(self, value):
        self.inputs[0].plug(value)

    @property
    def ifrom_min(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[1]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[7]

    @ifrom_min.setter
    def ifrom_min(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[1].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[7].plug(value)

    @property
    def ifrom_max(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[2]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[8]

    @ifrom_max.setter
    def ifrom_max(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[2].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[8].plug(value)

    @property
    def ito_min(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[3]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[9]

    @ito_min.setter
    def ito_min(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[3].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[9].plug(value)

    @property
    def ito_max(self):
        if (self.data_type == 'FLOAT'):
            return self.inputs[4]
        elif (self.data_type == 'FLOAT_VECTOR'):
            return self.inputs[10]

    @ito_max.setter
    def ito_max(self, value):
        if (self.data_type == 'FLOAT'):
            self.inputs[4].plug(value)
        elif (self.data_type == 'FLOAT_VECTOR'):
            self.inputs[10].plug(value)

    @property
    def isteps(self):
        if (self.interpolation_type == 'STEPPED'):
            return self.inputs[5]

    @isteps.setter
    def isteps(self, value):
        if (self.interpolation_type == 'STEPPED'):
            self.inputs[5].plug(value)

    @property
    def ivector(self):
        return self.inputs[6]

    @ivector.setter
    def ivector(self, value):
        self.inputs[6].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeMath

class NodeMath(Node):

    """ Node class ShaderNodeMath

    Input sockets
    -------------

        0: value0               Float
        1: value1               Float
        2: value2               Float

    Parameters
    ----------

        operation   : 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 
                               'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 
                               'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 
                               'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 
                               'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 
                               'RADIANS', 'DEGREES') 
        use_clamp   : False

    Output sockets
    --------------

        0: value                Float

    """

    PARAMETERS = ['operation', 'use_clamp']

    def __init__(self, value0=None, value1=None, value2=None, operation='ADD', use_clamp=False):

        super().__init__('ShaderNodeMath', name='Math')

        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value0'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value1'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'value2'       ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))

        self.socket_out_name = 'value'

        # ----- Parameters

        self.operation       = operation
        self.use_clamp       = use_clamp
        self.check_parameters()

        # ----- Input sockets

        self.ivalue0         = value0
        self.ivalue1         = value1
        self.ivalue2         = value2

        self.socket_in_name = 'ivalue0'

    def __repr__(self):
        s = f"Node 'Math' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   value0          : {self.ivalue0}"
        s += f"\n   value1          : {self.ivalue1}"
        s += f"\n   value2          : {self.ivalue2}"
        s += '\nParameters'
        s += f"\n   operation       : {self.operation}"
        s += f"\n   use_clamp       : {self.use_clamp}"
        s += '\nOutput sockets'
        s +=  "\n   value           : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 
                 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 
                 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 
                 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 
                 'COSH', 'TANH', 'RADIANS', 'DEGREES') 
        if self.operation not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMath'.\n 'operation' is '{self.operation}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def value(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivalue0(self):
        return self.inputs[0]

    @ivalue0.setter
    def ivalue0(self, value):
        self.inputs[0].plug(value)

    @property
    def ivalue1(self):
        return self.inputs[1]

    @ivalue1.setter
    def ivalue1(self, value):
        self.inputs[1].plug(value)

    @property
    def ivalue2(self):
        return self.inputs[2]

    @ivalue2.setter
    def ivalue2(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeMixRGB

class NodeMix(Node):

    """ Node class ShaderNodeMixRGB

    Input sockets
    -------------

        0: fac                  Float
        1: color1               Color
        2: color2               Color

    Parameters
    ----------

        blend_type  : 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 
                               'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 
                               'COLOR', 'VALUE') 
        use_alpha   : False
        use_clamp   : False

    Output sockets
    --------------

        0: color                Color

    """

    PARAMETERS = ['blend_type', 'use_alpha', 'use_clamp']

    def __init__(self, fac=None, color1=None, color2=None, blend_type='MIX', use_alpha=False, use_clamp=False):

        super().__init__('ShaderNodeMixRGB', name='Mix')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'fac'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color1'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color2'       ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))

        self.socket_out_name = 'color'

        # ----- Parameters

        self.blend_type      = blend_type
        self.use_alpha       = use_alpha
        self.use_clamp       = use_clamp
        self.check_parameters()

        # ----- Input sockets

        self.ifac            = fac
        self.icolor1         = color1
        self.icolor2         = color2

        self.socket_in_name = 'ifac'

    def __repr__(self):
        s = f"Node 'Mix' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   fac             : {self.ifac}"
        s += f"\n   color1          : {self.icolor1}"
        s += f"\n   color2          : {self.icolor2}"
        s += '\nParameters'
        s += f"\n   blend_type      : {self.blend_type}"
        s += f"\n   use_alpha       : {self.use_alpha}"
        s += f"\n   use_clamp       : {self.use_clamp}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        return s + "\n"

    def check_parameters(self):
        valids = ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 
                 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE') 
        if self.blend_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMix'.\n 'blend_type' is '{self.blend_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ifac(self):
        return self.inputs[0]

    @ifac.setter
    def ifac(self, value):
        self.inputs[0].plug(value)

    @property
    def icolor1(self):
        return self.inputs[1]

    @icolor1.setter
    def icolor1(self, value):
        self.inputs[1].plug(value)

    @property
    def icolor2(self):
        return self.inputs[2]

    @icolor2.setter
    def icolor2(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeRGBCurve

class NodeRGBCurves(Node):

    """ Node class ShaderNodeRGBCurve

    Input sockets
    -------------

        0: fac                  Float
        1: color                Color

    Output sockets
    --------------

        0: color                Color

    """

    PARAMETERS = []

    def __init__(self, fac=None, color=None):

        super().__init__('ShaderNodeRGBCurve', name='RGB Curves')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'fac'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color'        ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))

        self.socket_out_name = 'color'

        # ----- Input sockets

        self.ifac            = fac
        self.icolor          = color

        self.socket_in_name = 'ifac'

    def __repr__(self):
        s = f"Node 'RGBCurves' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   fac             : {self.ifac}"
        s += f"\n   color           : {self.icolor}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ifac(self):
        return self.inputs[0]

    @ifac.setter
    def ifac(self, value):
        self.inputs[0].plug(value)

    @property
    def icolor(self):
        return self.inputs[1]

    @icolor.setter
    def icolor(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeSeparateRGB

class NodeSeparateRGB(Node):

    """ Node class ShaderNodeSeparateRGB

    Input sockets
    -------------

        0: image                Color

    Output sockets
    --------------

        0: r                    Float
        1: g                    Float
        2: b                    Float

    """

    PARAMETERS = []

    def __init__(self, image=None):

        super().__init__('ShaderNodeSeparateRGB', name='Separate RGB')

        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'image'        ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'r'            ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'g'            ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'b'            ))

        self.socket_out_name = 'r'

        # ----- Input sockets

        self.iimage          = image

        self.socket_in_name = 'iimage'

    def __repr__(self):
        s = f"Node 'SeparateRGB' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   image           : {self.iimage}"
        s += '\nOutput sockets'
        s +=  "\n   r               : Float"
        s +=  "\n   g               : Float"
        s +=  "\n   b               : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def r(self):
        return self.outputs[0]

    @property
    def g(self):
        return self.outputs[1]

    @property
    def b(self):
        return self.outputs[2]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def iimage(self):
        return self.inputs[0]

    @iimage.setter
    def iimage(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeSeparateXYZ

class NodeSeparateXYZ(Node):

    """ Node class ShaderNodeSeparateXYZ

    Input sockets
    -------------

        0: vector               Vector

    Output sockets
    --------------

        0: x                    Float
        1: y                    Float
        2: z                    Float

    """

    PARAMETERS = []

    def __init__(self, vector=None):

        super().__init__('ShaderNodeSeparateXYZ', name='Separate XYZ')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'x'            ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'y'            ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'z'            ))

        self.socket_out_name = 'x'

        # ----- Input sockets

        self.ivector         = vector

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'SeparateXYZ' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += '\nOutput sockets'
        s +=  "\n   x               : Float"
        s +=  "\n   y               : Float"
        s +=  "\n   z               : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def x(self):
        return self.outputs[0]

    @property
    def y(self):
        return self.outputs[1]

    @property
    def z(self):
        return self.outputs[2]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexBrick

class NodeBrickTexture(Node):

    """ Node class ShaderNodeTexBrick

    Input sockets
    -------------

        0: vector               Vector
        1: color1               Color
        2: color2               Color
        3: mortar               Color
        4: scale                Float
        5: mortar_size          Float
        6: mortar_smooth        Float
        7: bias                 Float
        8: brick_width          Float
        9: row_height           Float

    Parameters
    ----------

        offset      : 0.5
        offset_frequency: 2
        squash      : 1.0
        squash_frequency: 2

    Output sockets
    --------------

        0: color                Color
        1: fac                  Float

    """

    PARAMETERS = ['offset', 'offset_frequency', 'squash', 'squash_frequency']

    def __init__(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):

        super().__init__('ShaderNodeTexBrick', name='Brick Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color1'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color2'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'mortar'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'mortar_size'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'mortar_smooth'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'bias'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'brick_width'  ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'row_height'   ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))

        self.socket_out_name = 'color'

        # ----- Parameters

        self.offset          = offset
        self.offset_frequency = offset_frequency
        self.squash          = squash
        self.squash_frequency = squash_frequency
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.icolor1         = color1
        self.icolor2         = color2
        self.imortar         = mortar
        self.iscale          = scale
        self.imortar_size    = mortar_size
        self.imortar_smooth  = mortar_smooth
        self.ibias           = bias
        self.ibrick_width    = brick_width
        self.irow_height     = row_height

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'BrickTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   color1          : {self.icolor1}"
        s += f"\n   color2          : {self.icolor2}"
        s += f"\n   mortar          : {self.imortar}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   mortar_size     : {self.imortar_size}"
        s += f"\n   mortar_smooth   : {self.imortar_smooth}"
        s += f"\n   bias            : {self.ibias}"
        s += f"\n   brick_width     : {self.ibrick_width}"
        s += f"\n   row_height      : {self.irow_height}"
        s += '\nParameters'
        s += f"\n   offset          : {self.offset}"
        s += f"\n   offset_frequency : {self.offset_frequency}"
        s += f"\n   squash          : {self.squash}"
        s += f"\n   squash_frequency : {self.squash_frequency}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   fac             : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def fac(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def icolor1(self):
        return self.inputs[1]

    @icolor1.setter
    def icolor1(self, value):
        self.inputs[1].plug(value)

    @property
    def icolor2(self):
        return self.inputs[2]

    @icolor2.setter
    def icolor2(self, value):
        self.inputs[2].plug(value)

    @property
    def imortar(self):
        return self.inputs[3]

    @imortar.setter
    def imortar(self, value):
        self.inputs[3].plug(value)

    @property
    def iscale(self):
        return self.inputs[4]

    @iscale.setter
    def iscale(self, value):
        self.inputs[4].plug(value)

    @property
    def imortar_size(self):
        return self.inputs[5]

    @imortar_size.setter
    def imortar_size(self, value):
        self.inputs[5].plug(value)

    @property
    def imortar_smooth(self):
        return self.inputs[6]

    @imortar_smooth.setter
    def imortar_smooth(self, value):
        self.inputs[6].plug(value)

    @property
    def ibias(self):
        return self.inputs[7]

    @ibias.setter
    def ibias(self, value):
        self.inputs[7].plug(value)

    @property
    def ibrick_width(self):
        return self.inputs[8]

    @ibrick_width.setter
    def ibrick_width(self, value):
        self.inputs[8].plug(value)

    @property
    def irow_height(self):
        return self.inputs[9]

    @irow_height.setter
    def irow_height(self, value):
        self.inputs[9].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexChecker

class NodeCheckerTexture(Node):

    """ Node class ShaderNodeTexChecker

    Input sockets
    -------------

        0: vector               Vector
        1: color1               Color
        2: color2               Color
        3: scale                Float

    Output sockets
    --------------

        0: color                Color
        1: fac                  Float

    """

    PARAMETERS = []

    def __init__(self, vector=None, color1=None, color2=None, scale=None):

        super().__init__('ShaderNodeTexChecker', name='Checker Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color1'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketColor'        , 'color2'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))

        self.socket_out_name = 'color'

        # ----- Input sockets

        self.ivector         = vector
        self.icolor1         = color1
        self.icolor2         = color2
        self.iscale          = scale

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'CheckerTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   color1          : {self.icolor1}"
        s += f"\n   color2          : {self.icolor2}"
        s += f"\n   scale           : {self.iscale}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   fac             : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def fac(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def icolor1(self):
        return self.inputs[1]

    @icolor1.setter
    def icolor1(self, value):
        self.inputs[1].plug(value)

    @property
    def icolor2(self):
        return self.inputs[2]

    @icolor2.setter
    def icolor2(self, value):
        self.inputs[2].plug(value)

    @property
    def iscale(self):
        return self.inputs[3]

    @iscale.setter
    def iscale(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexGradient

class NodeGradientTexture(Node):

    """ Node class ShaderNodeTexGradient

    Input sockets
    -------------

        0: vector               Vector

    Parameters
    ----------

        gradient_type: 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 
                                   'RADIAL') 

    Output sockets
    --------------

        0: color                Color
        1: fac                  Float

    """

    PARAMETERS = ['gradient_type']

    def __init__(self, vector=None, gradient_type='LINEAR'):

        super().__init__('ShaderNodeTexGradient', name='Gradient Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))

        self.socket_out_name = 'color'

        # ----- Parameters

        self.gradient_type   = gradient_type
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'GradientTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += '\nParameters'
        s += f"\n   gradient_type   : {self.gradient_type}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   fac             : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL') 
        if self.gradient_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeGradientTexture'.\n 'gradient_type' is '{self.gradient_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def fac(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexMagic

class NodeMagicTexture(Node):

    """ Node class ShaderNodeTexMagic

    Input sockets
    -------------

        0: vector               Vector
        1: scale                Float
        2: distortion           Float

    Parameters
    ----------

        turbulence_depth: 2

    Output sockets
    --------------

        0: color                Color
        1: fac                  Float

    """

    PARAMETERS = ['turbulence_depth']

    def __init__(self, vector=None, scale=None, distortion=None, turbulence_depth=2):

        super().__init__('ShaderNodeTexMagic', name='Magic Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'distortion'   ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))

        self.socket_out_name = 'color'

        # ----- Parameters

        self.turbulence_depth = turbulence_depth
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.iscale          = scale
        self.idistortion     = distortion

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'MagicTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   distortion      : {self.idistortion}"
        s += '\nParameters'
        s += f"\n   turbulence_depth : {self.turbulence_depth}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   fac             : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def fac(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def iscale(self):
        return self.inputs[1]

    @iscale.setter
    def iscale(self, value):
        self.inputs[1].plug(value)

    @property
    def idistortion(self):
        return self.inputs[2]

    @idistortion.setter
    def idistortion(self, value):
        self.inputs[2].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexMusgrave

class NodeMusgraveTexture(Node):

    """ Node class ShaderNodeTexMusgrave

    Input sockets
    -------------

        0: vector               Vector
        1: w                    Float
        2: scale                Float
        3: detail               Float
        4: dimension            Float
        5: lacunarity           Float
        6: offset               Float
        7: gain                 Float

    Parameters
    ----------

        musgrave_dimensions: '3D' in ('1D', '2D', '3D', '4D') 
        musgrave_type: 'FBM' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN') 

    Output sockets
    --------------

        0: fac                  Float

    """

    PARAMETERS = ['musgrave_dimensions', 'musgrave_type']

    def __init__(self, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):

        super().__init__('ShaderNodeTexMusgrave', name='Musgrave Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'w'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'detail'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'dimension'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'lacunarity'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'offset'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'gain'         ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))

        self.socket_out_name = 'fac'

        # ----- Parameters

        self.musgrave_dimensions = musgrave_dimensions
        self.musgrave_type   = musgrave_type
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.iw              = w
        self.iscale          = scale
        self.idetail         = detail
        self.idimension      = dimension
        self.ilacunarity     = lacunarity
        self.ioffset         = offset
        self.igain           = gain

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'MusgraveTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   w               : {self.iw}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   detail          : {self.idetail}"
        s += f"\n   dimension       : {self.idimension}"
        s += f"\n   lacunarity      : {self.ilacunarity}"
        s += f"\n   offset          : {self.ioffset}"
        s += f"\n   gain            : {self.igain}"
        s += '\nParameters'
        s += f"\n   musgrave_dimensions : {self.musgrave_dimensions}"
        s += f"\n   musgrave_type   : {self.musgrave_type}"
        s += '\nOutput sockets'
        s +=  "\n   fac             : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('1D', '2D', '3D', '4D') 
        if self.musgrave_dimensions not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMusgraveTexture'.\n 'musgrave_dimensions' is '{self.musgrave_dimensions}'.\n Authorized values are {valids}.")
        valids = ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN') 
        if self.musgrave_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeMusgraveTexture'.\n 'musgrave_type' is '{self.musgrave_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def fac(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def iw(self):
        return self.inputs[1]

    @iw.setter
    def iw(self, value):
        self.inputs[1].plug(value)

    @property
    def iscale(self):
        return self.inputs[2]

    @iscale.setter
    def iscale(self, value):
        self.inputs[2].plug(value)

    @property
    def idetail(self):
        return self.inputs[3]

    @idetail.setter
    def idetail(self, value):
        self.inputs[3].plug(value)

    @property
    def idimension(self):
        return self.inputs[4]

    @idimension.setter
    def idimension(self, value):
        self.inputs[4].plug(value)

    @property
    def ilacunarity(self):
        return self.inputs[5]

    @ilacunarity.setter
    def ilacunarity(self, value):
        self.inputs[5].plug(value)

    @property
    def ioffset(self):
        return self.inputs[6]

    @ioffset.setter
    def ioffset(self, value):
        self.inputs[6].plug(value)

    @property
    def igain(self):
        return self.inputs[7]

    @igain.setter
    def igain(self, value):
        self.inputs[7].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexNoise

class NodeNoiseTexture(Node):

    """ Node class ShaderNodeTexNoise

    Input sockets
    -------------

        0: vector               Vector
        1: w                    Float
        2: scale                Float
        3: detail               Float
        4: roughness            Float
        5: distortion           Float

    Parameters
    ----------

        noise_dimensions: '3D' in ('1D', '2D', '3D', '4D') 

    Output sockets
    --------------

        0: fac                  Float
        1: color                Color

    """

    PARAMETERS = ['noise_dimensions']

    def __init__(self, vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):

        super().__init__('ShaderNodeTexNoise', name='Noise Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'w'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'detail'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'roughness'    ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'distortion'   ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))

        self.socket_out_name = 'fac'

        # ----- Parameters

        self.noise_dimensions = noise_dimensions
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.iw              = w
        self.iscale          = scale
        self.idetail         = detail
        self.iroughness      = roughness
        self.idistortion     = distortion

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'NoiseTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   w               : {self.iw}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   detail          : {self.idetail}"
        s += f"\n   roughness       : {self.iroughness}"
        s += f"\n   distortion      : {self.idistortion}"
        s += '\nParameters'
        s += f"\n   noise_dimensions : {self.noise_dimensions}"
        s += '\nOutput sockets'
        s +=  "\n   fac             : Float"
        s +=  "\n   color           : Color"
        return s + "\n"

    def check_parameters(self):
        valids = ('1D', '2D', '3D', '4D') 
        if self.noise_dimensions not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeNoiseTexture'.\n 'noise_dimensions' is '{self.noise_dimensions}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def fac(self):
        return self.outputs[0]

    @property
    def color(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def iw(self):
        return self.inputs[1]

    @iw.setter
    def iw(self, value):
        self.inputs[1].plug(value)

    @property
    def iscale(self):
        return self.inputs[2]

    @iscale.setter
    def iscale(self, value):
        self.inputs[2].plug(value)

    @property
    def idetail(self):
        return self.inputs[3]

    @idetail.setter
    def idetail(self, value):
        self.inputs[3].plug(value)

    @property
    def iroughness(self):
        return self.inputs[4]

    @iroughness.setter
    def iroughness(self, value):
        self.inputs[4].plug(value)

    @property
    def idistortion(self):
        return self.inputs[5]

    @idistortion.setter
    def idistortion(self, value):
        self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexVoronoi

class NodeVoronoiTexture(Node):

    """ Node class ShaderNodeTexVoronoi

    Input sockets
    -------------

        0: vector               Vector
        1: w                    Float
        2: scale                Float
        3: smoothness           Float
        4: exponent             Float
        5: randomness           Float

    Parameters
    ----------

        distance_   : 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI') 
        feature     : 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS') 
        voronoi_dimensions: '3D' in ('1D', '2D', '3D', '4D') 

    Output sockets
    --------------

        0: distance             Float
        1: color                Color
        2: position             Vector
        3: w                    Float
        4: radius               Float

    """

    PARAMETERS = ['distance_', 'feature', 'voronoi_dimensions']

    def __init__(self, vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

        super().__init__('ShaderNodeTexVoronoi', name='Voronoi Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'w'            ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'smoothness'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'exponent'     ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'randomness'   ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'distance'     ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'position'     ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'w'            ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'radius'       ))

        self.socket_out_name = 'distance'

        # ----- Parameters

        self.distance_       = distance
        self.feature         = feature
        self.voronoi_dimensions = voronoi_dimensions
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.iw              = w
        self.iscale          = scale
        self.ismoothness     = smoothness
        self.iexponent       = exponent
        self.irandomness     = randomness

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'VoronoiTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   w               : {self.iw}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   smoothness      : {self.ismoothness}"
        s += f"\n   exponent        : {self.iexponent}"
        s += f"\n   randomness      : {self.irandomness}"
        s += '\nParameters'
        s += f"\n   distance        : {self.distance}"
        s += f"\n   feature         : {self.feature}"
        s += f"\n   voronoi_dimensions : {self.voronoi_dimensions}"
        s += '\nOutput sockets'
        s +=  "\n   distance        : Float"
        s +=  "\n   color           : Color"
        s +=  "\n   position        : Vector"
        s +=  "\n   w               : Float"
        s +=  "\n   radius          : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI') 
        if self.distance not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeVoronoiTexture'.\n 'distance' is '{self.distance_}'.\n Authorized values are {valids}.")
        valids = ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS') 
        if self.feature not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeVoronoiTexture'.\n 'feature' is '{self.feature}'.\n Authorized values are {valids}.")
        valids = ('1D', '2D', '3D', '4D') 
        if self.voronoi_dimensions not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeVoronoiTexture'.\n 'voronoi_dimensions' is '{self.voronoi_dimensions}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def distance(self):
        return self.outputs[0]

    @property
    def color(self):
        return self.outputs[1]

    @property
    def position(self):
        return self.outputs[2]

    @property
    def w(self):
        return self.outputs[3]

    @property
    def radius(self):
        return self.outputs[4]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def iw(self):
        return self.inputs[1]

    @iw.setter
    def iw(self, value):
        self.inputs[1].plug(value)

    @property
    def iscale(self):
        return self.inputs[2]

    @iscale.setter
    def iscale(self, value):
        self.inputs[2].plug(value)

    @property
    def ismoothness(self):
        return self.inputs[3]

    @ismoothness.setter
    def ismoothness(self, value):
        self.inputs[3].plug(value)

    @property
    def iexponent(self):
        return self.inputs[4]

    @iexponent.setter
    def iexponent(self, value):
        self.inputs[4].plug(value)

    @property
    def irandomness(self):
        return self.inputs[5]

    @irandomness.setter
    def irandomness(self, value):
        self.inputs[5].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexWave

class NodeWaveTexture(Node):

    """ Node class ShaderNodeTexWave

    Input sockets
    -------------

        0: vector               Vector
        1: scale                Float
        2: distortion           Float
        3: detail               Float
        4: detail_scale         Float
        5: detail_roughness     Float
        6: phase_offset         Float

    Parameters
    ----------

        bands_direction: 'X' in ('X', 'Y', 'Z', 'DIAGONAL') 
        rings_direction: 'X' in ('X', 'Y', 'Z', 'SPHERICAL') 
        wave_profile: 'SIN' in ('SIN', 'SAW', 'TRI') 
        wave_type   : 'BANDS' in ('BANDS', 'RINGS') 

    Output sockets
    --------------

        0: color                Color
        1: fac                  Float

    """

    PARAMETERS = ['bands_direction', 'rings_direction', 'wave_profile', 'wave_type']

    def __init__(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):

        super().__init__('ShaderNodeTexWave', name='Wave Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'distortion'   ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'detail'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'detail_scale' ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'detail_roughness'))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'phase_offset' ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'fac'          ))

        self.socket_out_name = 'color'

        # ----- Parameters

        self.bands_direction = bands_direction
        self.rings_direction = rings_direction
        self.wave_profile    = wave_profile
        self.wave_type       = wave_type
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.iscale          = scale
        self.idistortion     = distortion
        self.idetail         = detail
        self.idetail_scale   = detail_scale
        self.idetail_roughness = detail_roughness
        self.iphase_offset   = phase_offset

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'WaveTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   scale           : {self.iscale}"
        s += f"\n   distortion      : {self.idistortion}"
        s += f"\n   detail          : {self.idetail}"
        s += f"\n   detail_scale    : {self.idetail_scale}"
        s += f"\n   detail_roughness : {self.idetail_roughness}"
        s += f"\n   phase_offset    : {self.iphase_offset}"
        s += '\nParameters'
        s += f"\n   bands_direction : {self.bands_direction}"
        s += f"\n   rings_direction : {self.rings_direction}"
        s += f"\n   wave_profile    : {self.wave_profile}"
        s += f"\n   wave_type       : {self.wave_type}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   fac             : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('X', 'Y', 'Z', 'DIAGONAL') 
        if self.bands_direction not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeWaveTexture'.\n 'bands_direction' is '{self.bands_direction}'.\n Authorized values are {valids}.")
        valids = ('X', 'Y', 'Z', 'SPHERICAL') 
        if self.rings_direction not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeWaveTexture'.\n 'rings_direction' is '{self.rings_direction}'.\n Authorized values are {valids}.")
        valids = ('SIN', 'SAW', 'TRI') 
        if self.wave_profile not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeWaveTexture'.\n 'wave_profile' is '{self.wave_profile}'.\n Authorized values are {valids}.")
        valids = ('BANDS', 'RINGS') 
        if self.wave_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeWaveTexture'.\n 'wave_type' is '{self.wave_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def fac(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def iscale(self):
        return self.inputs[1]

    @iscale.setter
    def iscale(self, value):
        self.inputs[1].plug(value)

    @property
    def idistortion(self):
        return self.inputs[2]

    @idistortion.setter
    def idistortion(self, value):
        self.inputs[2].plug(value)

    @property
    def idetail(self):
        return self.inputs[3]

    @idetail.setter
    def idetail(self, value):
        self.inputs[3].plug(value)

    @property
    def idetail_scale(self):
        return self.inputs[4]

    @idetail_scale.setter
    def idetail_scale(self, value):
        self.inputs[4].plug(value)

    @property
    def idetail_roughness(self):
        return self.inputs[5]

    @idetail_roughness.setter
    def idetail_roughness(self, value):
        self.inputs[5].plug(value)

    @property
    def iphase_offset(self):
        return self.inputs[6]

    @iphase_offset.setter
    def iphase_offset(self, value):
        self.inputs[6].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeTexWhiteNoise

class NodeWhiteNoiseTexture(Node):

    """ Node class ShaderNodeTexWhiteNoise

    Input sockets
    -------------

        0: vector               Vector
        1: w                    Float

    Parameters
    ----------

        noise_dimensions: '3D' in ('1D', '2D', '3D', '4D') 

    Output sockets
    --------------

        0: value                Float
        1: color                Color

    """

    PARAMETERS = ['noise_dimensions']

    def __init__(self, vector=None, w=None, noise_dimensions='3D'):

        super().__init__('ShaderNodeTexWhiteNoise', name='White Noise Texture')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'w'            ))

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))
        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))

        self.socket_out_name = 'value'

        # ----- Parameters

        self.noise_dimensions = noise_dimensions
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.iw              = w

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'WhiteNoiseTexture' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   w               : {self.iw}"
        s += '\nParameters'
        s += f"\n   noise_dimensions : {self.noise_dimensions}"
        s += '\nOutput sockets'
        s +=  "\n   value           : Float"
        s +=  "\n   color           : Color"
        return s + "\n"

    def check_parameters(self):
        valids = ('1D', '2D', '3D', '4D') 
        if self.noise_dimensions not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeWhiteNoiseTexture'.\n 'noise_dimensions' is '{self.noise_dimensions}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def value(self):
        return self.outputs[0]

    @property
    def color(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def iw(self):
        return self.inputs[1]

    @iw.setter
    def iw(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeValToRGB

class NodeColorRamp(Node):

    """ Node class ShaderNodeValToRGB

    Input sockets
    -------------

        0: fac                  Float

    Output sockets
    --------------

        0: color                Color
        1: alpha                Float

    """

    PARAMETERS = []

    def __init__(self, fac=None):

        super().__init__('ShaderNodeValToRGB', name='ColorRamp')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'fac'          ))

        self.outputs.add(Socket (self, 'NodeSocketColor'        , 'color'        ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'alpha'        ))

        self.socket_out_name = 'color'

        # ----- Input sockets

        self.ifac            = fac

        self.socket_in_name = 'ifac'

    def __repr__(self):
        s = f"Node 'ColorRamp' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   fac             : {self.ifac}"
        s += '\nOutput sockets'
        s +=  "\n   color           : Color"
        s +=  "\n   alpha           : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def color(self):
        return self.outputs[0]

    @property
    def alpha(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ifac(self):
        return self.inputs[0]

    @ifac.setter
    def ifac(self, value):
        self.inputs[0].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeValue

class NodeValue(Node):

    """ Node class ShaderNodeValue

    Output sockets
    --------------

        0: value                Float

    """

    PARAMETERS = []

    def __init__(self, value=0.):

        super().__init__('ShaderNodeValue', name='Value')

        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))

        self.socket_out_name = 'value'

        self.outputs[0].default_value = value

        self.socket_in_name = None

    def __repr__(self):
        s = f"Node 'Value' ({self.unique_id})"
        s += '\nOutput sockets'
        s +=  "\n   value           : Float"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def value(self):
        return self.outputs[0]

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeVectorCurve

class NodeVectorCurves(Node):

    """ Node class ShaderNodeVectorCurve

    Input sockets
    -------------

        0: fac                  Float
        1: vector               Vector

    Output sockets
    --------------

        0: vector               Vector

    """

    PARAMETERS = []

    def __init__(self, fac=None, vector=None):

        super().__init__('ShaderNodeVectorCurve', name='Vector Curves')

        self.inputs.add(SocketIn(self, 'NodeSocketFloatFactor'  , 'fac'          ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'vector'       ))

        self.socket_out_name = 'vector'

        # ----- Input sockets

        self.ifac            = fac
        self.ivector         = vector

        self.socket_in_name = 'ifac'

    def __repr__(self):
        s = f"Node 'VectorCurves' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   fac             : {self.ifac}"
        s += f"\n   vector          : {self.ivector}"
        s += '\nOutput sockets'
        s +=  "\n   vector          : Vector"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vector(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ifac(self):
        return self.inputs[0]

    @ifac.setter
    def ifac(self, value):
        self.inputs[0].plug(value)

    @property
    def ivector(self):
        return self.inputs[1]

    @ivector.setter
    def ivector(self, value):
        self.inputs[1].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeVectorMath

class NodeVectorMath(Node):

    """ Node class ShaderNodeVectorMath

    Input sockets
    -------------

        0: vector0              Vector
        1: vector1              Vector
        2: vector2              Vector
        3: scale                Float

    Parameters
    ----------

        operation   : 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 
                               'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 
                               'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 
                               'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT') 

    Output sockets
    --------------

        0: vector               Vector
        1: value                Float

    """

    PARAMETERS = ['operation']

    def __init__(self, vector0=None, vector1=None, vector2=None, scale=None, operation='ADD'):

        super().__init__('ShaderNodeVectorMath', name='Vector Math')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector0'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector1'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector2'      ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloat'        , 'scale'        ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'vector'       ))
        self.outputs.add(Socket (self, 'NodeSocketFloat'        , 'value'        ))

        self.socket_out_name = 'vector'

        # ----- Parameters

        self.operation       = operation
        self.check_parameters()

        # ----- Input sockets

        self.ivector0        = vector0
        self.ivector1        = vector1
        self.ivector2        = vector2
        self.iscale          = scale

        self.socket_in_name = 'ivector0'

    def __repr__(self):
        s = f"Node 'VectorMath' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector0         : {self.ivector0}"
        s += f"\n   vector1         : {self.ivector1}"
        s += f"\n   vector2         : {self.ivector2}"
        s += f"\n   scale           : {self.iscale}"
        s += '\nParameters'
        s += f"\n   operation       : {self.operation}"
        s += '\nOutput sockets'
        s +=  "\n   vector          : Vector"
        s +=  "\n   value           : Float"
        return s + "\n"

    def check_parameters(self):
        valids = ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 
                 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 
                 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 
                 'TANGENT') 
        if self.operation not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeVectorMath'.\n 'operation' is '{self.operation}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vector(self):
        return self.outputs[0]

    @property
    def value(self):
        return self.outputs[1]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector0(self):
        return self.inputs[0]

    @ivector0.setter
    def ivector0(self, value):
        self.inputs[0].plug(value)

    @property
    def ivector1(self):
        return self.inputs[1]

    @ivector1.setter
    def ivector1(self, value):
        self.inputs[1].plug(value)

    @property
    def ivector2(self):
        return self.inputs[2]

    @ivector2.setter
    def ivector2(self, value):
        self.inputs[2].plug(value)

    @property
    def iscale(self):
        return self.inputs[3]

    @iscale.setter
    def iscale(self, value):
        self.inputs[3].plug(value)

# ------------------------------------------------------------------------------------------------------------------------
# Node class ShaderNodeVectorRotate

class NodeVectorRotate(Node):

    """ Node class ShaderNodeVectorRotate

    Input sockets
    -------------

        0: vector               Vector
        1: center               Vector
        2: axis                 Vector
        3: angle                Float
        4: rotation             Vector

    Parameters
    ----------

        invert      : False
        rotation_type: 'AXIS_ANGLE' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ') 

    Output sockets
    --------------

        0: vector               Vector

    """

    PARAMETERS = ['invert', 'rotation_type']

    def __init__(self, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):

        super().__init__('ShaderNodeVectorRotate', name='Vector Rotate')

        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'vector'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'center'       ))
        self.inputs.add(SocketIn(self, 'NodeSocketVector'       , 'axis'         ))
        self.inputs.add(SocketIn(self, 'NodeSocketFloatAngle'   , 'angle'        ))
        self.inputs.add(SocketIn(self, 'NodeSocketVectorEuler'  , 'rotation'     ))

        self.outputs.add(Socket (self, 'NodeSocketVector'       , 'vector'       ))

        self.socket_out_name = 'vector'

        # ----- Parameters

        self.invert          = invert
        self.rotation_type   = rotation_type
        self.check_parameters()

        # ----- Input sockets

        self.ivector         = vector
        self.icenter         = center
        self.iaxis           = axis
        self.iangle          = angle
        self.irotation       = rotation

        self.socket_in_name = 'ivector'

    def __repr__(self):
        s = f"Node 'VectorRotate' ({self.unique_id})"
        s += '\nInput sockets'
        s += f"\n   vector          : {self.ivector}"
        s += f"\n   center          : {self.icenter}"
        s += f"\n   axis            : {self.iaxis}"
        s += f"\n   angle           : {self.iangle}"
        s += f"\n   rotation        : {self.irotation}"
        s += '\nParameters'
        s += f"\n   invert          : {self.invert}"
        s += f"\n   rotation_type   : {self.rotation_type}"
        s += '\nOutput sockets'
        s +=  "\n   vector          : Vector"
        return s + "\n"

    def check_parameters(self):
        valids = ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ') 
        if self.rotation_type not in valids:
            raise AttributeError(f"\nAttribute error for Node 'NodeVectorRotate'.\n 'rotation_type' is '{self.rotation_type}'.\n Authorized values are {valids}.")

    # --------------------------------------------------------------------------------
    # Output sockets

    @property
    def vector(self):
        return self.outputs[0]

    # --------------------------------------------------------------------------------
    # Input sockets

    @property
    def ivector(self):
        return self.inputs[0]

    @ivector.setter
    def ivector(self, value):
        self.inputs[0].plug(value)

    @property
    def icenter(self):
        return self.inputs[1]

    @icenter.setter
    def icenter(self, value):
        self.inputs[1].plug(value)

    @property
    def iaxis(self):
        return self.inputs[2]

    @iaxis.setter
    def iaxis(self, value):
        self.inputs[2].plug(value)

    @property
    def iangle(self):
        return self.inputs[3]

    @iangle.setter
    def iangle(self, value):
        self.inputs[3].plug(value)

    @property
    def irotation(self):
        return self.inputs[4]

    @irotation.setter
    def irotation(self, value):
        self.inputs[4].plug(value)

