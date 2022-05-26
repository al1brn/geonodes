import geonodes as gn
from geonodes.core import datasocket as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Vector

class Vector(dsock.Vector):
    """ Data socket Vector

    Constructors
    ------------
        AlignToVector        : rotation (Vector)
        Combine              : vector (Vector)
        Random               : value (Vector)
    Properties
    ----------
        separate             : Sockets [x (Float), y (Float), z (Float)]
    Methods
    -------
        absolute             : vector (Vector)
        accumulate_field     : Sockets [leading (Vector), trailing (Vector), total (Vector)]
        add                  : vector (Vector)
        ceil                 : vector (Vector)
        cos                  : vector (Vector)
        cross                : vector (Vector)
        distance             : value (Float)
        divide               : vector (Vector)
        dot                  : value (Float)
        faceforward          : vector (Vector)
        field_at_index       : value (Vector)
        floor                : vector (Vector)
        fraction             : vector (Vector)
        length               : value (Float)
        max                  : vector (Vector)
        min                  : vector (Vector)
        modulo               : vector (Vector)
        multiply             : vector (Vector)
        multiply_add         : vector (Vector)
        normalize            : vector (Vector)
        project              : vector (Vector)
        reflect              : vector (Vector)
        refract              : vector (Vector)
        rotate               : vector (Vector)
        scale                : vector (Vector)
        sin                  : vector (Vector)
        snap                 : vector (Vector)
        subtract             : vector (Vector)
        switch               : output (Vector)
        tan                  : vector (Vector)
        wrap                 : vector (Vector)
    Stacked methods
    ---------------
        align_to_vector      : Vector
        curves               : Vector
        map_range            : Vector
        rotate_euler         : Vector
    """

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, probability=None, ID=None, seed=None):
        """Call node NodeRandomValue (FunctionNodeRandomValue)

        Sockets arguments
        -----------------
            min            : Vector
            max            : Vector
            probability    : Float
            ID             : Integer
            seed           : Integer

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return cls(nodes.NodeRandomValue(min=min, max=max, probability=probability, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """Call node NodeCombineXyz (ShaderNodeCombineXYZ)

        Sockets arguments
        -----------------
            x              : Float
            y              : Float
            z              : Float
        Returns
        -------
            Vector
        """

        return cls(nodes.NodeCombineXyz(x=x, y=y, z=z).vector)

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """Call node NodeAlignEulerToVector (FunctionNodeAlignEulerToVector)

        Sockets arguments
        -----------------
            rotation       : Vector
            factor         : Float
            vector         : Vector

        Parameters arguments
        --------------------
            axis           : 'X' in [X, Y, Z]
            pivot_axis     : 'AUTO' in [AUTO, X, Y, Z]
        Returns
        -------
            Vector
        """

        return cls(nodes.NodeAlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """Call node NodeSeparateXyz (ShaderNodeSeparateXYZ)

        Sockets arguments
        -----------------
            vector         : Vector (self)
        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
        """

        if self.separate_ is None:
            self.separate_ = nodes.NodeSeparateXyz(vector=self)
        return self.separate_


    @property
    def x(self):
        return self.separate.x

    @property
    def y(self):
        return self.separate.y

    @property
    def z(self):
        return self.separate.z


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'ADD'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='ADD').vector

    def subtract(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'SUBTRACT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='SUBTRACT').vector

    def multiply(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='MULTIPLY').vector

    def divide(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'DIVIDE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='DIVIDE').vector

    def multiply_add(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY_ADD'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='MULTIPLY_ADD').vector

    def cross(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'CROSS_PRODUCT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='CROSS_PRODUCT').vector

    def project(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'PROJECT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='PROJECT').vector

    def reflect(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'REFLECT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='REFLECT').vector

    def refract(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'REFRACT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='REFRACT').vector

    def faceforward(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'FACEFORWARD'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='FACEFORWARD').vector

    def dot(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'DOT_PRODUCT'

        Returns
        -------
            Float
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='DOT_PRODUCT').value

    def distance(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'DISTANCE'

        Returns
        -------
            Float
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='DISTANCE').value

    def length(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'LENGTH'

        Returns
        -------
            Float
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='LENGTH').value

    def scale(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'SCALE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='SCALE').vector

    def normalize(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'NORMALIZE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='NORMALIZE').vector

    def absolute(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'ABSOLUTE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='ABSOLUTE').vector

    def min(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'MINIMUM'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='MINIMUM').vector

    def max(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'MAXIMUM'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='MAXIMUM').vector

    def floor(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'FLOOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='FLOOR').vector

    def ceil(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'CEIL'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='CEIL').vector

    def fraction(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'FRACTION'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='FRACTION').vector

    def modulo(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'MODULO'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='MODULO').vector

    def wrap(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'WRAP'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='WRAP').vector

    def snap(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'SNAP'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='SNAP').vector

    def sin(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'SINE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='SINE').vector

    def cos(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'COSINE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='COSINE').vector

    def tan(self, vector1=None, vector2=None, scale=None):
        """Call node NodeVectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'TANGENT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, scale=scale, operation='TANGENT').vector

    def switch(self, switch0=None, switch1=None, true=None):
        """Call node NodeSwitch (GeometryNodeSwitch)

        Sockets arguments
        -----------------
            false          : Vector (self)
            switch0        : Boolean
            switch1        : Boolean
            true           : Vector

        Fixed parameters
        ----------------
            input_type     : 'VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeSwitch(false=self, switch0=switch0, switch1=switch1, true=true, input_type='VECTOR').output

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
        """Call node NodeVectorRotate (ShaderNodeVectorRotate)

        Sockets arguments
        -----------------
            vector         : Vector (self)
            center         : Vector
            axis           : Vector
            angle          : Float
            rotation       : Vector

        Parameters arguments
        --------------------
            invert         : False
            rotation_type  : 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]
        Returns
        -------
            Vector
        """

        return nodes.NodeVectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type).vector

    def accumulate_field(self, group_index=None, domain='POINT'):
        """Call node NodeAccumulateField (GeometryNodeAccumulateField)

        Sockets arguments
        -----------------
            value          : Vector (self)
            group_index    : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Sockets [leading (Vector), trailing (Vector), total (Vector)]
        """

        return nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """Call node NodeFieldAtIndex (GeometryNodeFieldAtIndex)

        Sockets arguments
        -----------------
            value          : Vector (self)
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeFieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain).value


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """Call node NodeVectorCurves (ShaderNodeVectorCurve)

        Sockets arguments
        -----------------
            vector         : Vector (self)
            fac            : Float
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeVectorCurves(vector=self, fac=fac))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """Call node NodeAlignEulerToVector (FunctionNodeAlignEulerToVector)

        Sockets arguments
        -----------------
            rotation       : Vector (self)
            factor         : Float
            vector         : Vector

        Parameters arguments
        --------------------
            axis           : 'X' in [X, Y, Z]
            pivot_axis     : 'AUTO' in [AUTO, X, Y, Z]
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeAlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))

    def rotate_euler(self, rotate_by=None, axis=None, angle=None, space='OBJECT'):
        """Call node NodeRotateEuler (FunctionNodeRotateEuler)

        Sockets arguments
        -----------------
            rotation       : Vector (self)
            rotate_by      : Vector
            axis           : Vector
            angle          : Float

        Parameters arguments
        --------------------
            space          : 'OBJECT' in [OBJECT, LOCAL]
        Returns
        -------
            self

        """

        return self.stack(nodes.NodeRotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, space=space))

    def map_range(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR'):
        """Call node NodeMapRange (ShaderNodeMapRange)

        Sockets arguments
        -----------------
            vector         : Vector (self)
            value          : Float
            from_min       : Vector
            from_max       : Vector
            to_min         : Vector
            to_max         : Vector

        Parameters arguments
        --------------------
            clamp          : True
            interpolation_type: 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeMapRange(vector=self, value=value, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type))


