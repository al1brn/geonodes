import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Vector

class Vector(dsock.Vector):
    """ Class Vector
    

    | Inherits from: dsock.Vector 
    

    Constructors
    ============
    - AlignToVector : rotation (Vector) 
    - Combine       : vector (Vector) 
    - Random        : value (Vector) 
    

    Properties
    ==========
    - separate : Sockets      [x (Float), y (Float), z (Float)] 
    

    Methods
    =======
    - absolute            : vector (Vector) 
    - accumulate_field    : Sockets      [leading (Vector), trailing (Vector), total (Vector)] 
    - add                 : vector (Vector) 
    - attribute_statistic : Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector),
      range (Vector), standard_deviation (Vector), variance (Vector)] 
    - capture_attribute   : Sockets      [geometry (Geometry), attribute (Vector)] 
    - ceil                : vector (Vector) 
    - cos                 : vector (Vector) 
    - cross               : vector (Vector) 
    - distance            : value (Float) 
    - divide              : vector (Vector) 
    - dot                 : value (Float) 
    - equal               : result (Boolean) 
    - faceforward         : vector (Vector) 
    - field_at_index      : value (Vector) 
    - floor               : vector (Vector) 
    - fraction            : vector (Vector) 
    - greater_equal       : result (Boolean) 
    - greater_than        : result (Boolean) 
    - length              : value (Float) 
    - less_equal          : result (Boolean) 
    - less_than           : result (Boolean) 
    - map_range           : vector (Vector) 
    - max                 : vector (Vector) 
    - min                 : vector (Vector) 
    - modulo              : vector (Vector) 
    - multiply            : vector (Vector) 
    - multiply_add        : vector (Vector) 
    - normalize           : vector (Vector) 
    - not_equal           : result (Boolean) 
    - project             : vector (Vector) 
    - raycast             : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float),
      attribute (Vector)] 
    - reflect             : vector (Vector) 
    - refract             : vector (Vector) 
    - rotate              : vector (Vector) 
    - scale               : vector (Vector) 
    - sin                 : vector (Vector) 
    - snap                : vector (Vector) 
    - subtract            : vector (Vector) 
    - tan                 : vector (Vector) 
    - transfer_attribute  : attribute (Vector) 
    - wrap                : vector (Vector) 
    

    Stacked methods
    ===============
    - align_to_vector : Vector 
    - curves          : Vector 
    - rotate_euler    : Vector 
    """


    def reset_properties(self):
        self.separate_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """Call node RandomValue (FunctionNodeRandomValue)

        Sockets arguments
        -----------------
            min            : Vector
            max            : Vector
            ID             : Integer
            seed           : Integer

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value)

    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """Call node CombineXyz (ShaderNodeCombineXYZ)

        Sockets arguments
        -----------------
            x              : Float
            y              : Float
            z              : Float

        Returns
        -------
            Vector
        """

        return cls(nodes.CombineXyz(x=x, y=y, z=z).vector)

    @classmethod
    def AlignToVector(cls, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """Call node AlignEulerToVector (FunctionNodeAlignEulerToVector)

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

        return cls(nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """Call node SeparateXyz (ShaderNodeSeparateXYZ)

        Sockets arguments
        -----------------
            vector         : Vector (self)

        Returns
        -------
            Sockets [x (Float), y (Float), z (Float)]
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
        return self.separate_


    @property
    def x(self):
        return self.separate.x

    @x.setter
    def x(self, value):
        self.separate.x = value

    @property
    def y(self):
        return self.separate.y

    @y.setter
    def y(self, value):
        self.separate.y = value

    @property
    def z(self):
        return self.separate.z

    @z.setter
    def z(self, value):
        self.separate.z = value


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT'):
        """Call node AccumulateField (GeometryNodeAccumulateField)

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

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT'):
        """Call node AttributeStatistic (GeometryNodeAttributeStatistic)

        Sockets arguments
        -----------------
            attribute      : Vector (self)
            geometry       : Geometry
            selection      : Boolean

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain)

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
        """Call node TransferAttribute (GeometryNodeAttributeTransfer)

        Sockets arguments
        -----------------
            attribute      : Vector (self)
            source         : Geometry
            source_position: Vector
            index          : Integer

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            mapping        : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Vector
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping).attribute

    def capture_attribute(self, geometry=None, domain='POINT'):
        """Call node CaptureAttribute (GeometryNodeCaptureAttribute)

        Sockets arguments
        -----------------
            value          : Vector (self)
            geometry       : Geometry

        Parameters arguments
        --------------------
            domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Vector)]
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain)

    def field_at_index(self, index=None, domain='POINT'):
        """Call node FieldAtIndex (GeometryNodeFieldAtIndex)

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

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """Call node Raycast (GeometryNodeRaycast)

        Sockets arguments
        -----------------
            attribute      : Vector (self)
            target_geometry: Geometry
            source_position: Vector
            ray_direction  : Vector
            ray_length     : Float

        Parameters arguments
        --------------------
            mapping        : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

        Fixed parameters
        ----------------
            data_type      : 'FLOAT_VECTOR'

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping)

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR'):
        """Call node MapRange (ShaderNodeMapRange)

        Sockets arguments
        -----------------
            vector         : Vector (self)
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
            Vector
        """

        return nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type).vector

    def less_than(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Vector (self)
            b              : Vector
            c              : Float
            angle          : Float

        Parameters arguments
        --------------------
            mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

        Fixed parameters
        ----------------
            data_type      : 'VECTOR'
            operation      : 'LESS_THAN'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN').result

    def less_equal(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Vector (self)
            b              : Vector
            c              : Float
            angle          : Float

        Parameters arguments
        --------------------
            mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

        Fixed parameters
        ----------------
            data_type      : 'VECTOR'
            operation      : 'LESS_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL').result

    def greater_than(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Vector (self)
            b              : Vector
            c              : Float
            angle          : Float

        Parameters arguments
        --------------------
            mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

        Fixed parameters
        ----------------
            data_type      : 'VECTOR'
            operation      : 'GREATER_THAN'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN').result

    def greater_equal(self, b=None, c=None, angle=None, mode='ELEMENT'):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Vector (self)
            b              : Vector
            c              : Float
            angle          : Float

        Parameters arguments
        --------------------
            mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

        Fixed parameters
        ----------------
            data_type      : 'VECTOR'
            operation      : 'GREATER_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL').result

    def equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT'):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Vector (self)
            b              : Vector
            c              : Float
            angle          : Float
            epsilon        : Float

        Parameters arguments
        --------------------
            mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

        Fixed parameters
        ----------------
            data_type      : 'VECTOR'
            operation      : 'EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL').result

    def not_equal(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT'):
        """Call node Compare (FunctionNodeCompare)

        Sockets arguments
        -----------------
            a              : Vector (self)
            b              : Vector
            c              : Float
            angle          : Float
            epsilon        : Float

        Parameters arguments
        --------------------
            mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

        Fixed parameters
        ----------------
            data_type      : 'VECTOR'
            operation      : 'NOT_EQUAL'

        Returns
        -------
            Boolean
        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL').result

    def add(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'ADD'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD').vector

    def subtract(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'SUBTRACT'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT').vector

    def multiply(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY').vector

    def divide(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'DIVIDE'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE').vector

    def multiply_add(self, vector1=None, vector2=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector

        Fixed parameters
        ----------------
            operation      : 'MULTIPLY_ADD'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector

    def cross(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'CROSS_PRODUCT'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT').vector

    def project(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'PROJECT'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT').vector

    def reflect(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'REFLECT'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT').vector

    def refract(self, vector1=None, scale=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'REFRACT'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT').vector

    def faceforward(self, vector1=None, vector2=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector

        Fixed parameters
        ----------------
            operation      : 'FACEFORWARD'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector

    def dot(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'DOT_PRODUCT'

        Returns
        -------
            Float
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT').value

    def distance(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'DISTANCE'

        Returns
        -------
            Float
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE').value

    def length(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'LENGTH'

        Returns
        -------
            Float
        """

        return nodes.VectorMath(vector0=self, operation='LENGTH').value

    def scale(self, scale=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            scale          : Float

        Fixed parameters
        ----------------
            operation      : 'SCALE'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, scale=scale, operation='SCALE').vector

    def normalize(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'NORMALIZE'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='NORMALIZE').vector

    def absolute(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'ABSOLUTE'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='ABSOLUTE').vector

    def min(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'MINIMUM'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM').vector

    def max(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'MAXIMUM'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM').vector

    def floor(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'FLOOR'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='FLOOR').vector

    def ceil(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'CEIL'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='CEIL').vector

    def fraction(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'FRACTION'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='FRACTION').vector

    def modulo(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'MODULO'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO').vector

    def wrap(self, vector1=None, vector2=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector
            vector2        : Vector

        Fixed parameters
        ----------------
            operation      : 'WRAP'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP').vector

    def snap(self, vector1=None):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)
            vector1        : Vector

        Fixed parameters
        ----------------
            operation      : 'SNAP'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP').vector

    def sin(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'SINE'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='SINE').vector

    def cos(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'COSINE'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='COSINE').vector

    def tan(self):
        """Call node VectorMath (ShaderNodeVectorMath)

        Sockets arguments
        -----------------
            vector0        : Vector (self)

        Fixed parameters
        ----------------
            operation      : 'TANGENT'

        Returns
        -------
            Vector
        """

        return nodes.VectorMath(vector0=self, operation='TANGENT').vector

    def rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
        """Call node VectorRotate (ShaderNodeVectorRotate)

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

        return nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type).vector


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def curves(self, fac=None):
        """Call node VectorCurves (ShaderNodeVectorCurve)

        Sockets arguments
        -----------------
            vector         : Vector (self)
            fac            : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.VectorCurves(vector=self, fac=fac))

    def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """Call node AlignEulerToVector (FunctionNodeAlignEulerToVector)

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

        return self.stack(nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))

    def rotate_euler(self, rotate_by=None, space='OBJECT'):
        """Call node RotateEuler (FunctionNodeRotateEuler)

        Sockets arguments
        -----------------
            rotation       : Vector (self)
            rotate_by      : Vector

        Parameters arguments
        --------------------
            space          : 'OBJECT' in [OBJECT, LOCAL]

        Returns
        -------
            self

        """

        return self.stack(nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space))


