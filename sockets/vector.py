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
# Data class Vector

class Vector(bcls.Vector):
    """ Socket data class Vector

    Constructors
    ------------
        AlignToVector        : Vector
        Combine              : Vector
        Random               : Vector

    Properties
    ----------
        separate             : Sockets [x (Float), y (Float), z (Float)]

    Node properties
    ---------------
        x                    : Float
        y                    : Float
        z                    : Float

    Methods
    -------
        absolute             : Vector
        accumulate_field     : Sockets [leading (Vector), trailing (Vector), total (Vector)]
        add                  : Vector
        ceil                 : Vector
        cos                  : Vector
        cross                : Vector
        distance             : Float
        divide               : Vector
        dot                  : Float
        faceforward          : Vector
        field_at_index       : Vector
        floor                : Vector
        fraction             : Vector
        length               : Float
        max                  : Vector
        min                  : Vector
        modulo               : Vector
        multiply             : Vector
        multiply_add         : Vector
        normalize            : Vector
        project              : Vector
        reflect              : Vector
        refract              : Vector
        rotate               : Vector
        scale                : Vector
        sin                  : Vector
        snap                 : Vector
        subtract             : Vector
        switch               : Vector
        tan                  : Vector
        wrap                 : Vector

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
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """ Constructor Random using node NodeRandomValue

        Arguments
        ---------
            min             : Vector
            max             : Vector
            ID              : Integer
            seed            : Integer

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').output

    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """ Constructor Combine using node NodeCombineXYZ

        Arguments
        ---------
            x               : Float
            y               : Float
            z               : Float

        Returns
        -------
            Vector
        """

        return nodes.NodeCombineXYZ(x=x, y=y, z=z).output

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ Constructor AlignToVector using node NodeAlignEulertoVector

        Arguments
        ---------
            rotation        : Vector
            factor          : Float
            vector          : Vector

            axis            : str
            pivot_axis      : str

        Returns
        -------
            Vector
        """

        return nodes.NodeAlignEulertoVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).output


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ Property separate using node NodeSeparateXYZ

        Arguments
        ---------
            vector          : Vector: self socket

        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
        """

        if not hasattr(self.top, 'separate_'):
            self.top.separate_ = nodes.NodeSeparateXYZ(vector=self).output
        return self.top.separate_


    # ----------------------------------------------------------------------------------------------------
    # Node properties

    @property
    def x(self):
        """ Node property x using node NodeSeparateXYZ on output socket x

        Arguments
        ---------
            vector          : Vector: self socket

        Returns
        -------
            Float
        """

        return self.separate.x

    @property
    def y(self):
        """ Node property y using node NodeSeparateXYZ on output socket y

        Arguments
        ---------
            vector          : Vector: self socket

        Returns
        -------
            Float
        """

        return self.separate.y

    @property
    def z(self):
        """ Node property z using node NodeSeparateXYZ on output socket z

        Arguments
        ---------
            vector          : Vector: self socket

        Returns
        -------
            Float
        """

        return self.separate.z


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def add(self, vector1=None):
        """ Method add using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ADD'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='ADD').output

    def subtract(self, vector1=None):
        """ Method subtract using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SUBTRACT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SUBTRACT').output

    def multiply(self, vector1=None):
        """ Method multiply using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MULTIPLY'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MULTIPLY').output

    def divide(self, vector1=None):
        """ Method divide using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'DIVIDE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DIVIDE').output

    def multiply_add(self, vector1=None, vector2=None):
        """ Method multiply_add using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector
            vector2         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MULTIPLY_ADD'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').output

    def cross(self, vector1=None):
        """ Method cross using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'CROSS_PRODUCT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT').output

    def project(self, vector1=None):
        """ Method project using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'PROJECT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='PROJECT').output

    def reflect(self, vector1=None):
        """ Method reflect using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'REFLECT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='REFLECT').output

    def refract(self, vector1=None, scale=None):
        """ Method refract using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector
            scale           : Float

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'REFRACT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT').output

    def faceforward(self, vector1=None, vector2=None):
        """ Method faceforward using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector
            vector2         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'FACEFORWARD'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD').output

    def dot(self, vector1=None):
        """ Method dot using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'DOT_PRODUCT'

        Returns
        -------
            Float
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT').output

    def distance(self, vector1=None):
        """ Method distance using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'DISTANCE'

        Returns
        -------
            Float
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DISTANCE').output

    def length(self):
        """ Method length using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'LENGTH'

        Returns
        -------
            Float
        """

        return nodes.NodeVectorMath(vector0=self, operation='LENGTH').output

    def scale(self, scale=None):
        """ Method scale using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            scale           : Float

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SCALE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, scale=scale, operation='SCALE').output

    def normalize(self):
        """ Method normalize using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'NORMALIZE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='NORMALIZE').output

    def absolute(self):
        """ Method absolute using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'ABSOLUTE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='ABSOLUTE').output

    def min(self, vector1=None):
        """ Method min using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MINIMUM'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MINIMUM').output

    def max(self, vector1=None):
        """ Method max using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MAXIMUM'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MAXIMUM').output

    def floor(self):
        """ Method floor using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'FLOOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='FLOOR').output

    def ceil(self):
        """ Method ceil using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'CEIL'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='CEIL').output

    def fraction(self):
        """ Method fraction using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'FRACTION'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='FRACTION').output

    def modulo(self, vector1=None):
        """ Method modulo using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'MODULO'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MODULO').output

    def wrap(self, vector1=None, vector2=None):
        """ Method wrap using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector
            vector2         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'WRAP'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP').output

    def snap(self, vector1=None):
        """ Method snap using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket
            vector1         : Vector

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SNAP'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SNAP').output

    def sin(self):
        """ Method sin using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'SINE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='SINE').output

    def cos(self):
        """ Method cos using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'COSINE'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='COSINE').output

    def tan(self):
        """ Method tan using node NodeVectorMath

        Arguments
        ---------
            vector0         : Vector: self socket

        Node parameters settings
        ------------------------
            operation       : node parameter set to 'TANGENT'

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorMath(vector0=self, operation='TANGENT').output

    def switch(self, switch=None, true=None):
        """ Method switch using node NodeSwitch

        Arguments
        ---------
            false           : Float: self socket
            switch          : Boolean
            true            : Float

        Node parameters settings
        ------------------------
            input_type      : node parameter set to 'VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeSwitch(false=self, switch=switch, true=true, input_type='VECTOR').output

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
        """ Method rotate using node NodeVectorRotate

        Arguments
        ---------
            vector          : Vector: self socket
            center          : Vector
            axis            : Vector
            angle           : Float
            rotation        : Vector

            invert          : bool
            rotation_type   : str

        Returns
        -------
            Vector
        """

        return nodes.NodeVectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type).output

    def accumulate_field(self, group_index=None, domain='POINT'):
        """ Method accumulate_field using node NodeAccumulateField

        Arguments
        ---------
            value           : Vector: self socket
            group_index     : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_VECTOR'

        Returns
        -------
            Sockets [leading (Vector), trailing (Vector), total (Vector)]
        """

        return nodes.NodeAccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain).output

    def field_at_index(self, index=None, domain='POINT'):
        """ Method field_at_index using node NodeFieldatIndex

        Arguments
        ---------
            value           : Float: self socket
            index           : Integer

            domain          : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.NodeFieldatIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """ Stacked method curves using node NodeVectorCurves

        Arguments
        ---------
            vector          : Vector: self socket
            fac             : Float

        Returns
        -------
            Vector
        """

        return self.stack(nodes.NodeVectorCurves(vector=self, fac=fac))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """ Stacked method align_to_vector using node NodeAlignEulertoVector

        Arguments
        ---------
            rotation        : Vector: self socket
            factor          : Float
            vector          : Vector

            axis            : str
            pivot_axis      : str

        Returns
        -------
            Vector
        """

        return self.stack(nodes.NodeAlignEulertoVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))

    def rotate_euler(self, rotate_by=None, axis=None, angle=None, space='OBJECT'):
        """ Stacked method rotate_euler using node NodeRotateEuler

        Arguments
        ---------
            rotation        : Vector: self socket
            rotate_by       : Vector
            axis            : Vector
            angle           : Float

            space           : str

        Returns
        -------
            Vector
        """

        return self.stack(nodes.NodeRotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, space=space))

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """ Stacked method map_range using node NodeMapRange

        Arguments
        ---------
            vector          : Vector: self socket
            from_min        : Float
            from_max        : Float
            to_min          : Float
            to_max          : Float
            steps           : Float

            clamp           : bool
            interpolation_type : str

        Node parameters settings
        ------------------------
            data_type       : node parameter set to 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return self.stack(nodes.NodeMapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type))



