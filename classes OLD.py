from geonodes import baseclasses as bcls
from geonodes import nodes

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ========================================================================================================================
# Functions

def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
    return Vector(nodes.NodeAlignEulertoVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).outputs[0])

def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='EQUAL'):
    return Boolean(nodes.NodeCompare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).outputs[0])

def rotate_euler(rotation=None, rotate_by=None, space='OBJECT'):
    return Vector(nodes.NodeRotateEuler(rotation=rotation, rotate_by=rotate_by, space=space).outputs[0])

def accumulate_field(value=None, group_index=None, data_type='FLOAT', domain='POINT'):
    return nodes.NodeAccumulateField(value=value, group_index=group_index, data_type=data_type, domain=domain)

def atribute_transfer(source=None, attribute=None, source_position=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED'):
    return NODE(nodes.NodeTransferAttribute(source=source, attribute=attribute, source_position=source_position, data_type=data_type, domain=domain, mapping=mapping).outputs[1])

def curve_arc(resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, mode='RADIUS'):
    return nodes.NodeArc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode=mode)

def field_at_index(index=None, value=None, data_type='FLOAT', domain='POINT'):
    return Float(nodes.NodeFieldatIndex(index=index, value=value, data_type=data_type, domain=domain).outputs[0])

def proximity(target=None, source_position=None, target_element='FACES'):
    return nodes.NodeGeometryProximity(target=target, source_position=source_position, target_element=target_element)

def raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):
    return nodes.NodeRaycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type, mapping=mapping)

def join_strings(*strings, delimiter=None):
    return String(nodes.NodeJoinStrings(*strings, delimiter=delimiter).outputs[0])

def clamp(value=None, min=None, max=None, clamp_type='MINMAX'):
    return Float(nodes.NodeClamp(value=value, min=min, max=max, clamp_type=clamp_type).outputs[0])

def combine_rgb(r=None, g=None, b=None):
    return Color(nodes.NodeCombineRGB(r=r, g=g, b=b).outputs[0])

def combine_xyz(x=None, y=None, z=None):
    return Vector(nodes.NodeCombineXYZ(x=x, y=y, z=z).outputs[0])

def map_range(value=None, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR'):
    return nodes.NodeMapRange(value=value, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)

def mixRGB(fac=None, color1=None, color2=None, blend_type='MIX', use_alpha=False, use_clamp=False):
    return Color(nodes.NodeMix(fac=fac, color1=color1, color2=color2, blend_type=blend_type, use_alpha=use_alpha, use_clamp=use_clamp).outputs[0])

def color_ramp(fac=None, color_ramp=None):
    return nodes.NodeColorRamp(fac=fac, color_ramp=color_ramp)

# ------------------------------------------------------------------------------------------------------------------------
# Boolean math

def b_and(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='AND').outputs[0])

def b_or(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='OR').outputs[0])

def b_not(boolean0=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, operation='NOT').outputs[0])

def nand(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NAND').outputs[0])

def nor(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NOR').outputs[0])

def xnor(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XNOR').outputs[0])

def xor(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XOR').outputs[0])

def imply(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='IMPLY').outputs[0])

def nimply(boolean0=None, boolean1=None):
    return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NIMPLY').outputs[0])

# ------------------------------------------------------------------------------------------------------------------------
# Generate random values

def random_float(min=None, max=None, ID=None, seed=None):
    return Value(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').outputs[1])

def random_integer(min=None, max=None, ID=None, seed=None):
    return Value(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').outputs[2])

def random_vector(min=None, max=None, ID=None, seed=None):
    return Value(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').outputs[0])

def random_boolean(probability=None, ID=None, seed=None):
    return Value(nodes.NodeRandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').outputs[3])

# ------------------------------------------------------------------------------------------------------------------------
# Switch values

def switch_float(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='FLOAT').outputs[0])

def switch_integer(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='INT').outputs[1])

def switch_boolean(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='BOOLEAN').outputs[2])

def switch_vector(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='VECTOR').outputs[3])

def switch_string(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='STRING').outputs[5])

def switch_color(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='RGBA').outputs[4])

def switch_object(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='OBJECT').outputs[7])

def switch_image(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='IMAGE').outputs[11])

def switch_geometry(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='GEOMETRY').outputs[6])

def switch_collection(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='COLLECTION').outputs[8])

def switch_texture(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='TEXTURE').outputs[9])

def switch_material(switch=None, false=None, true=None):
    return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='MATERIAL').outputs[10])

# ------------------------------------------------------------------------------------------------------------------------
# Math operations and functions

def add(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_add(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='ADD').outputs[0])

def substract(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_substract(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

def multiply(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_multiply(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

def divide(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_divide(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

def multiply_add(value0=None, value1=None, value=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_multiply_add(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, value=value, use_clamp=use_clamp, operation='MULTIPLY_ADD').outputs[0])

def pow(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='POWER').outputs[0])

def log(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='LOGARITHM').outputs[0])

def sqrt(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='SQRT').outputs[0])

def inverse_sqrt(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='INVERSE_SQRT').outputs[0])

def abs(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='ABSOLUTE').outputs[0])

def exp(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='EXPONENT').outputs[0])

def min(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_min(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='MINIMUM').outputs[0])

def max(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_max(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='MAXIMUM').outputs[0])

def less_than(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='LESS_THAN').outputs[0])

def greater_than(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='GREATER_THAN').outputs[0])

def sign(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='SIGN').outputs[0])

def compare(value0=None, value1=None, value=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, value=value, use_clamp=use_clamp, operation='COMPARE').outputs[0])

def smooth_min(value0=None, value1=None, value=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, value=value, use_clamp=use_clamp, operation='SMOOTH_MIN').outputs[0])

def smooth_max(value0=None, value1=None, value=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, value=value, use_clamp=use_clamp, operation='SMOOTH_MAX').outputs[0])

def round(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='ROUND').outputs[0])

def floor(value0=None, use_clamp=False):
    if is_vector(value0):
        return vector_floor(value0)
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='FLOOR').outputs[0])

def ceil(value0=None, use_clamp=False):
    if is_vector(value0):
        return vector_ceil(value0)
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='CEIL').outputs[0])

def trunc(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='TRUNC').outputs[0])

def fract(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='FRACT').outputs[0])

def modulo(value0=None, value1=None, use_clamp=False):
    if is_vector(value0) or is_vector(value1):
        return vector_modulo(value0, value1)
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='MODULO').outputs[0])

def wrap(value0=None, value1=None, value=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, value=value, use_clamp=use_clamp, operation='WRAP').outputs[0])

def snap(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='SNAP').outputs[0])

def pingpong(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='PINGPONG').outputs[0])

def sin(value0=None, use_clamp=False):
    if is_vector(value0):
        return vector_sin(value0)
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='SINE').outputs[0])

def cos(value0=None, use_clamp=False):
    if is_vector(value0):
        return vector_cos(value0)
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='COSINE').outputs[0])

def tan(value0=None, use_clamp=False):
    if is_vector(value0):
        return vector_tan(value0)
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='TANGENT').outputs[0])

def arcsin(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='ARCSINE').outputs[0])

def arccos(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='ARCCOSINE').outputs[0])

def arctan(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='ARCTANGENT').outputs[0])

def arctan2(value0=None, value1=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, value1=value1, use_clamp=use_clamp, operation='ARCTAN2').outputs[0])

def sinh(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='SINH').outputs[0])

def cosh(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='COSH').outputs[0])

def tanh(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='TANH').outputs[0])

def radians(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='RADIANS').outputs[0])

def degrees(value0=None, use_clamp=False):
    return Float(nodes.NodeMath(value0=value0, use_clamp=use_clamp, operation='DEGREES').outputs[0])

# ------------------------------------------------------------------------------------------------------------------------
# Vector math operations and functions

def vector_add(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='ADD')

def vector_subtract(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT')

def vector_multiply(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY')

def vector_divide(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE')

def vector_multiply_add(vector0=None, vector1=None, vector=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector=vector, operation='MULTIPLY_ADD')

def cross(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT')

def project(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='PROJECT')

def reflect(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='REFLECT')

def refract(vector0=None, vector1=None, scale=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT')

def faceforward(vector0=None, vector1=None, vector=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector=vector, operation='FACEFORWARD')

def dot(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT')

def distance(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE')

def length(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='LENGTH')

def scale(vector0=None, scale=None):
    return nodes.NodeVectorMath(vector0=vector0, scale=scale, operation='SCALE')

def normalize(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='NORMALIZE')

def absolute(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='ABSOLUTE')

def vector_min(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM')

def vector_max(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM')

def vector_floor(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='FLOOR')

def vector_ceil(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='CEIL')

def vector_fraction(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='FRACTION')

def vector_modulo(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MODULO')

def wrap(vector0=None, vector1=None, vector=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector=vector, operation='WRAP')

def snap(vector0=None, vector1=None):
    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='SNAP')

def vector_sin(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='SINE')

def vector_cos(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='COSINE')

def vector_tan(vector0=None):
    return nodes.NodeVectorMath(vector0=vector0, operation='TANGENT')

# ------------------------------------------------------------------------------------------------------------------------
# Geometry combination

def intersect(*mesh_2, self_intersection=None, hole_tolerant=None):
    return Mesh(nodes.NodeMeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT').outputs[0])

def union(*mesh_2, self_intersection=None, hole_tolerant=None):
    return Mesh(nodes.NodeMeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION').outputs[0])

def difference(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None):
    return Mesh(nodes.NodeMeshBoolean(*mesh_2, mesh_1=mesh_1, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE').outputs[0])

# ========================================================================================================================
# Data classes

# ------------------------------------------------------------------------------------------------------------------------
# class Float

class Float(bcls.Float):

    def to_integer(self, rounding_mode='ROUND'):
        return Integer(nodes.NodeFloattoInteger(float=self, rounding_mode=rounding_mode).outputs[0])

    def to_string(self, decimals=None):
        return String(nodes.NodeValuetoString(value=self, decimals=decimals).outputs[0])

    def curve(self, value=None, mapping=None):
        return Float(nodes.NodeFloatCurve(factor=self, value=value, mapping=mapping).outputs[0])

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        return cls(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT').outputs[1])

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Float(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='FLOAT').outputs[0])

    def to_viewer(self, value=None):
        return nodes.NodeViewer(geometry=self, value=value, data_type='FLOAT')

    def add(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='ADD').outputs[0])

    def __add__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='ADD').outputs[0])

    def __radd__(self, value0=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='ADD').outputs[0])

    def substract(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

    def __sub__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

    def __rsub__(self, value0=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

    def multiply(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

    def __mul__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

    def __rmul__(self, value0=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

    def divide(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

    def __truediv__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

    def __rtruediv__(self, value0=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

    def multiply_add(self, value1=None, value=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='MULTIPLY_ADD').outputs[0])

    def pow(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='POWER').outputs[0])

    def __pow__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='POWER').outputs[0])

    def __rpow__(self, value0=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='POWER').outputs[0])

    def log(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='LOGARITHM').outputs[0])

    def sqrt(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SQRT').outputs[0])

    def inverse_sqrt(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='INVERSE_SQRT').outputs[0])

    def abs(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ABSOLUTE').outputs[0])

    def __abs__(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ABSOLUTE').outputs[0])

    def exp(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='EXPONENT').outputs[0])

    def min(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MINIMUM').outputs[0])

    def max(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MAXIMUM').outputs[0])

    def less_than(self, value1=None, use_clamp=False):
        return Boolean(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='LESS_THAN').outputs[0])

    def greater_than(self, value1=None, use_clamp=False):
        return Boolean(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='GREATER_THAN').outputs[0])

    def sign(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SIGN').outputs[0])

    def compare(self, value1=None, value=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='COMPARE').outputs[0])

    def smooth_min(self, value1=None, value=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='SMOOTH_MIN').outputs[0])

    def smooth_max(self, value1=None, value=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='SMOOTH_MAX').outputs[0])

    def round(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ROUND').outputs[0])

    def __round__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ROUND').outputs[0])

    def floor(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='FLOOR').outputs[0])

    def __floor__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='FLOOR').outputs[0])

    def ceil(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='CEIL').outputs[0])

    def __ceil__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='CEIL').outputs[0])

    def trunc(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='TRUNC').outputs[0])

    def fract(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='FRACT').outputs[0])

    def modulo(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MODULO').outputs[0])

    def __mod__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MODULO').outputs[0])

    def wrap(self, value1=None, value=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='WRAP').outputs[0])

    def snap(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='SNAP').outputs[0])

    def pingpong(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='PINGPONG').outputs[0])

    def sin(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SINE').outputs[0])

    def cos(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='COSINE').outputs[0])

    def tan(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='TANGENT').outputs[0])

    def arcsin(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ARCSINE').outputs[0])

    def arccos(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ARCCOSINE').outputs[0])

    def arctan(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ARCTANGENT').outputs[0])

    def arctan2(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='ARCTAN2').outputs[0])

    def sinh(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SINH').outputs[0])

    def cosh(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='COSH').outputs[0])

    def tanh(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='TANH').outputs[0])

    def radians(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='RADIANS').outputs[0])

    def degrees(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='DEGREES').outputs[0])

    def __neg__(self):
        return self.multiply(-1)

# ------------------------------------------------------------------------------------------------------------------------
# class Integer

class Integer(bcls.Integer):

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        return cls(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT').outputs[2])

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Integer(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='INT').outputs[1])

    def to_viewer(self, value=None):
        return nodes.NodeViewer(geometry=self, value=value, data_type='INT')

    def add(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='ADD').outputs[0])

    def __add__(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='ADD').outputs[0])

    def __radd__(self, value0=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='ADD').outputs[0])

    def substract(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

    def __sub__(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

    def __rsub__(self, value0=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='SUBTRACT').outputs[0])

    def multiply(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

    def __mul__(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

    def __rmul__(self, value0=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='MULTIPLY').outputs[0])

    def divide(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

    def __truediv__(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

    def __rtruediv__(self, value0=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='DIVIDE').outputs[0])

    def multiply_add(self, value1=None, value=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='MULTIPLY_ADD').outputs[0])

    def pow(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='POWER').outputs[0])

    def __pow__(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='POWER').outputs[0])

    def __rpow__(self, value0=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=value0, value1=self, use_clamp=use_clamp, operation='POWER').outputs[0])

    def log(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='LOGARITHM').outputs[0])

    def sqrt(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SQRT').outputs[0])

    def inverse_sqrt(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='INVERSE_SQRT').outputs[0])

    def abs(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ABSOLUTE').outputs[0])

    def __abs__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ABSOLUTE').outputs[0])

    def exp(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='EXPONENT').outputs[0])

    def min(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MINIMUM').outputs[0])

    def max(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MAXIMUM').outputs[0])

    def less_than(self, value1=None, use_clamp=False):
        return Boolean(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='LESS_THAN').outputs[0])

    def greater_than(self, value1=None, use_clamp=False):
        return Boolean(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='GREATER_THAN').outputs[0])

    def sign(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SIGN').outputs[0])

    def compare(self, value1=None, value=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='COMPARE').outputs[0])

    def smooth_min(self, value1=None, value=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='SMOOTH_MIN').outputs[0])

    def smooth_max(self, value1=None, value=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='SMOOTH_MAX').outputs[0])

    def round(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ROUND').outputs[0])

    def __round__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ROUND').outputs[0])

    def floor(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='FLOOR').outputs[0])

    def __floor__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='FLOOR').outputs[0])

    def ceil(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='CEIL').outputs[0])

    def __ceil__(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='CEIL').outputs[0])

    def trunc(self, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='TRUNC').outputs[0])

    def fract(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='FRACT').outputs[0])

    def modulo(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MODULO').outputs[0])

    def __mod__(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='MODULO').outputs[0])

    def wrap(self, value1=None, value=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, value=value, use_clamp=use_clamp, operation='WRAP').outputs[0])

    def snap(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='SNAP').outputs[0])

    def pingpong(self, value1=None, use_clamp=False):
        return Integer(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='PINGPONG').outputs[0])

    def sin(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SINE').outputs[0])

    def cos(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='COSINE').outputs[0])

    def tan(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='TANGENT').outputs[0])

    def arcsin(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ARCSINE').outputs[0])

    def arccos(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ARCCOSINE').outputs[0])

    def arctan(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='ARCTANGENT').outputs[0])

    def arctan2(self, value1=None, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, value1=value1, use_clamp=use_clamp, operation='ARCTAN2').outputs[0])

    def sinh(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='SINH').outputs[0])

    def cosh(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='COSH').outputs[0])

    def tanh(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='TANH').outputs[0])

    def radians(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='RADIANS').outputs[0])

    def degrees(self, use_clamp=False):
        return Float(nodes.NodeMath(value0=self, use_clamp=use_clamp, operation='DEGREES').outputs[0])

    def __neg__(self):
        return self.multiply(-1)

# ------------------------------------------------------------------------------------------------------------------------
# class Boolean

class Boolean(bcls.Boolean):

    def b_and(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='AND').outputs[0])

    def __mul__(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='AND').outputs[0])

    def __rmul__(self, boolean0=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=self, operation='AND').outputs[0])

    def b_or(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='OR').outputs[0])

    def __add__(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='OR').outputs[0])

    def __radd__(self, boolean0=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=boolean0, boolean1=self, operation='OR').outputs[0])

    def b_not(self):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, operation='NOT').outputs[0])

    def __invert__(self):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, operation='NOT').outputs[0])

    def nand(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').outputs[0])

    def nor(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').outputs[0])

    def xnor(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').outputs[0])

    def xor(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').outputs[0])

    def imply(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').outputs[0])

    def nimply(self, boolean1=None):
        return Boolean(nodes.NodeBooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').outputs[0])

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        return cls(nodes.NodeRandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').outputs[3])

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Boolean(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='BOOLEAN').outputs[2])

    def to_viewer(self, value=None):
        return nodes.NodeViewer(geometry=self, value=value, data_type='BOOLEAN')

    def __neg__(self):
        return self.b_not()

# ------------------------------------------------------------------------------------------------------------------------
# class String

class String(bcls.String):

    @classmethod
    def Special(cls):
        return nodes.NodeSpecialCharacters()

    def replace(self, find=None, replace=None):
        self.stack(nodes.NodeReplaceString(string=self.connector, find=find, replace=replace))
        return self

    def slice(self, position=None, length=None):
        self.stack(nodes.NodeSliceString(string=self.connector, position=position, length=length))
        return self

    def length(self):
        return Integer(nodes.NodeStringLength(string=self).outputs[0])

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        return nodes.NodeStringtoCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, align_x=align_x, align_y=align_y, font=font, overflow=overflow, pivot_mode=pivot_mode)

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return String(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='STRING').outputs[5])

# ------------------------------------------------------------------------------------------------------------------------
# class Vector

class Vector(bcls.Vector):

    @property
    def separate(self):
        if not hasattr(self.top, 'separate_'):
            self.top.separate_ = nodes.NodeSeparateXYZ(self.connector)
            self.top.separate_.prop_of = self.node
        return self.top.separate_

    @property
    def x(self):
        if not hasattr(self.top, 'x_'):
            self.top.x_ = Float(self.top.separate.x)
        return self.top.x_

    @x.setter
    def x(self, value):
        _ = self.separate
        self.top.x_ = value

    @property
    def y(self):
        if not hasattr(self.top, 'y_'):
            self.top.y_ = Float(self.top.separate.y)
        return self.top.y_

    @y.setter
    def y(self, value):
        _ = self.separate
        self.top.y_ = value

    @property
    def z(self):
        if not hasattr(self.top, 'z_'):
            self.top.z_ = Float(self.top.separate.z)
        return self.top.z_

    @z.setter
    def z(self, value):
        _ = self.separate
        self.top.z_ = value

    def curves(self, vector=None, mapping=None):
        self.stack(nodes.NodeVectorCurves(fac=self.connector, vector=vector, mapping=mapping))
        return self

    def rotate(self, center=None, axis=None, angle=None, invert=False, rotation_type='AXIS_ANGLE'):
        self.stack(nodes.NodeVectorRotate(vector=self.connector, center=center, axis=axis, angle=angle, invert=invert, rotation_type=rotation_type))
        return self

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        return cls(nodes.NodeRandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR').outputs[0])

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Vector(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='VECTOR').outputs[3])

    def to_viewer(self, value=None):
        return nodes.NodeViewer(geometry=self, value=value, data_type='FLOAT_VECTOR')

    def add(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='ADD')

    def __add__(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='ADD')

    def __radd__(self, vector0=None):
        return nodes.NodeVectorMath(vector0=vector0, vector1=self, operation='ADD')

    def subtract(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SUBTRACT')

    def __sub__(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SUBTRACT')

    def __rsub__(self, vector0=None):
        return nodes.NodeVectorMath(vector0=vector0, vector1=self, operation='SUBTRACT')

    def multiply(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MULTIPLY')

    def __mul__(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MULTIPLY')

    def __rmul__(self, vector0=None):
        return nodes.NodeVectorMath(vector0=vector0, vector1=self, operation='MULTIPLY')

    def divide(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DIVIDE')

    def __truediv__(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DIVIDE')

    def __rtruediv__(self, vector0=None):
        return nodes.NodeVectorMath(vector0=vector0, vector1=self, operation='DIVIDE')

    def multiply_add(self, vector1=None, vector=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector=vector, operation='MULTIPLY_ADD')

    def cross(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT')

    def project(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='PROJECT')

    def reflect(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='REFLECT')

    def refract(self, vector1=None, scale=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT')

    def faceforward(self, vector1=None, vector=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector=vector, operation='FACEFORWARD')

    def dot(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT')

    def distance(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='DISTANCE')

    def length(self):
        return nodes.NodeVectorMath(vector0=self, operation='LENGTH')

    def scale(self, scale=None):
        return nodes.NodeVectorMath(vector0=self, scale=scale, operation='SCALE')

    def normalize(self):
        return nodes.NodeVectorMath(vector0=self, operation='NORMALIZE')

    def absolute(self):
        return nodes.NodeVectorMath(vector0=self, operation='ABSOLUTE')

    def min(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MINIMUM')

    def max(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MAXIMUM')

    def floor(self):
        return nodes.NodeVectorMath(vector0=self, operation='FLOOR')

    def __floor__(self):
        return nodes.NodeVectorMath(vector0=self, operation='FLOOR')

    def ceil(self):
        return nodes.NodeVectorMath(vector0=self, operation='CEIL')

    def __ceil__(self):
        return nodes.NodeVectorMath(vector0=self, operation='CEIL')

    def fraction(self):
        return nodes.NodeVectorMath(vector0=self, operation='FRACTION')

    def modulo(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MODULO')

    def __mod__(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='MODULO')

    def wrap(self, vector1=None, vector=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, vector=vector, operation='WRAP')

    def snap(self, vector1=None):
        return nodes.NodeVectorMath(vector0=self, vector1=vector1, operation='SNAP')

    def sin(self):
        return nodes.NodeVectorMath(vector0=self, operation='SINE')

    def cos(self):
        return nodes.NodeVectorMath(vector0=self, operation='COSINE')

    def tan(self):
        return nodes.NodeVectorMath(vector0=self, operation='TANGENT')

    def __neg__(self):
        return self.multiply(-1)

# ------------------------------------------------------------------------------------------------------------------------
# class Color

class Color(bcls.Color):

    @property
    def separate(self):
        if not hasattr(self.top, 'separate_'):
            self.top.separate_ = nodes.NodeSeparateRGB(self.connector)
            self.top.separate_.prop_of = self.node
        return self.top.separate_

    @property
    def r(self):
        if not hasattr(self.top, 'r_'):
            self.top.r_ = Float(self.top.separate.r)
        return self.top.r_

    @property
    def g(self):
        if not hasattr(self.top, 'g_'):
            self.top.g_ = Float(self.top.separate.g)
        return self.top.g_

    @property
    def b(self):
        if not hasattr(self.top, 'b_'):
            self.top.b_ = Float(self.top.separate.b)
        return self.top.b_

    def curves(self, color=None, mapping=None):
        self.stack(nodes.NodeRGBCurves(fac=self.connector, color=color, mapping=mapping))
        return self

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Color(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='RGBA').outputs[4])

    def to_viewer(self, value=None):
        return nodes.NodeViewer(geometry=self, value=value, data_type='FLOAT_COLOR')

# ------------------------------------------------------------------------------------------------------------------------
# class Geometry

class Geometry(bcls.Geometry):

    @property
    def point_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    @property
    def edge_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def face_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def corner_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def curve_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[0])

    @property
    def instance_ID(self):
        return Integer(nodes.NodeID(owner_socket=self.socket, data_type='INT', domain='INSTANCE').outputs[0])

    @property
    def point_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    @property
    def edge_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def face_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def corner_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def curve_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[0])

    @property
    def instance_index(self):
        return Integer(nodes.NodeIndex(owner_socket=self.socket, data_type='INT', domain='INSTANCE').outputs[0])

    @property
    def point_material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    @property
    def edge_material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def face_material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def corner_material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='CORNER').outputs[0])

    @property
    def curve_material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[0])

    @property
    def instance_material_index(self):
        return Integer(nodes.NodeMaterialIndex(owner_socket=self.socket, data_type='INT', domain='INSTANCE').outputs[0])

    @property
    def point_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='VECTOR', domain='POINT').outputs[0])

    @property
    def edge_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='VECTOR', domain='EDGE').outputs[0])

    @property
    def face_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='VECTOR', domain='FACE').outputs[0])

    @property
    def corner_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_normal(self):
        return Vector(nodes.NodeNormal(owner_socket=self.socket, data_type='VECTOR', domain='INSTANCE').outputs[0])

    @property
    def point_position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='VECTOR', domain='POINT').outputs[0])

    @property
    def edge_position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='VECTOR', domain='EDGE').outputs[0])

    @property
    def face_position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='VECTOR', domain='FACE').outputs[0])

    @property
    def corner_position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_position(self):
        return Vector(nodes.NodePosition(owner_socket=self.socket, data_type='VECTOR', domain='INSTANCE').outputs[0])

    @property
    def point_shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='POINT').outputs[0])

    @property
    def edge_shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='EDGE').outputs[0])

    @property
    def face_shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='FACE').outputs[0])

    @property
    def corner_shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='CORNER').outputs[0])

    @property
    def curve_shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    @property
    def instance_shade_smooth(self):
        return Boolean(nodes.NodeIsShadeSmooth(owner_socket=self.socket, data_type='BOOLEAN', domain='INSTANCE').outputs[0])

    @property
    def point_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='VECTOR', domain='POINT').outputs[0])

    @property
    def edge_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='VECTOR', domain='EDGE').outputs[0])

    @property
    def face_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='VECTOR', domain='FACE').outputs[0])

    @property
    def corner_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='VECTOR', domain='CORNER').outputs[0])

    @property
    def curve_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='VECTOR', domain='CURVE').outputs[0])

    @property
    def instance_tangent(self):
        return Vector(nodes.NodeCurveTangent(owner_socket=self.socket, data_type='VECTOR', domain='INSTANCE').outputs[0])

    @property
    def is_viewport(self):
        return Boolean(nodes.NodeIsViewport(owner_socket=self.socket, data_type='BOOLEAN', domain='POINT').outputs[0])

    @property
    def bound_box(self):
        if not hasattr(self.top, 'bound_box_'):
            self.top.bound_box_ = nodes.NodeBoundingBox(self.connector)
            self.top.bound_box_.prop_of = self.node
        return self.top.bound_box_

    @property
    def box(self):
        if not hasattr(self.top, 'box_'):
            self.top.box_ = Geometry(self.top.bound_box.bounding_box)
        return self.top.box_

    @property
    def box_min(self):
        if not hasattr(self.top, 'box_min_'):
            self.top.box_min_ = Vector(self.top.bound_box.min)
        return self.top.box_min_

    @property
    def box_max(self):
        if not hasattr(self.top, 'box_max_'):
            self.top.box_max_ = Vector(self.top.bound_box.max)
        return self.top.box_max_

    @property
    def components(self):
        if not hasattr(self.top, 'components_'):
            self.top.components_ = nodes.NodeSeparateComponents(self.connector)
            self.top.components_.prop_of = self.node
        return self.top.components_

    @property
    def mesh_component(self):
        if not hasattr(self.top, 'mesh_component_'):
            self.top.mesh_component_ = Geometry(self.top.components.mesh)
        return self.top.mesh_component_

    @property
    def points_component(self):
        if not hasattr(self.top, 'points_component_'):
            self.top.points_component_ = Geometry(self.top.components.point_cloud)
        return self.top.points_component_

    @property
    def curve_component(self):
        if not hasattr(self.top, 'curve_component_'):
            self.top.curve_component_ = Geometry(self.top.components.curve)
        return self.top.curve_component_

    @property
    def volume_component(self):
        if not hasattr(self.top, 'volume_component_'):
            self.top.volume_component_ = Geometry(self.top.components.volume)
        return self.top.volume_component_

    @property
    def instances_component(self):
        if not hasattr(self.top, 'instances_component_'):
            self.top.instances_component_ = Geometry(self.top.components.instances)
        return self.top.instances_component_

    def delete_geometry(self, selection=None, domain='POINT', mode='ALL'):
        self.stack(nodes.NodeDeleteGeometry(geometry=self.connector, selection=selection, domain=domain, mode=mode))
        return self

    def merge_by_distance(self, selection=None, distance=None):
        self.stack(nodes.NodeMergebyDistance(geometry=self.connector, selection=selection, distance=distance))
        return self

    def realize_instances(self, legacy_behavior=False):
        self.stack(nodes.NodeRealizeInstances(geometry=self.connector, legacy_behavior=legacy_behavior))
        return self

    def replace_material(self, old=None, new=None):
        self.stack(nodes.NodeReplaceMaterial(geometry=self.connector, old=old, new=new))
        return self

    def scale_elements(self, selection=None, scale=None, center=None, domain='FACE', scale_mode='UNIFORM'):
        self.stack(nodes.NodeScaleElements(geometry=self.connector, selection=selection, scale=scale, center=center, domain=domain, scale_mode=scale_mode))
        return self

    def set_ID(self, selection=None, ID=None):
        self.stack(nodes.NodeSetID(geometry=self.connector, selection=selection, ID=ID))
        return self

    def set_material(self, selection=None, material=None):
        self.stack(nodes.NodeSetMaterial(geometry=self.connector, selection=selection, material=material))
        return self

    def set_material_index(self, selection=None, material_index=None):
        self.stack(nodes.NodeSetMaterialIndex(geometry=self.connector, selection=selection, material_index=material_index))
        return self

    def set_position(self, selection=None, position=None, offset=None):
        self.stack(nodes.NodeSetPosition(geometry=self.connector, selection=selection, position=position, offset=offset))
        return self

    def set_shade_smooth(self, selection=None, shade_smooth=None):
        self.stack(nodes.NodeSetShadeSmooth(geometry=self.connector, selection=selection, shade_smooth=shade_smooth))
        return self

    def transform(self, translation=None, rotation=None, scale=None):
        self.stack(nodes.NodeTransform(geometry=self.connector, translation=translation, rotation=rotation, scale=scale))
        return self

    def attribute_domain_size(self, component='MESH'):
        return nodes.NodeDomainSize(geometry=self, component=component)

    def attribute_remove(self, *attribute):
        return Geometry(nodes.NodeAttributeRemove(*attribute, geometry=self).outputs[0])

    def attribute_statistic(self, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
        return nodes.NodeAttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type, domain=domain)

    def components(self, selection=None, domain='POINT'):
        return nodes.NodeSeparateGeometry(geometry=self, selection=selection, domain=domain)

    def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT'):
        return nodes.NodeCaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain)

    def convex_hull(self):
        return Geometry(nodes.NodeConvexHull(geometry=self).outputs[0])

    def to_instance(self, *geometry):
        return Instances(nodes.NodeGeometrytoInstance(self, *geometry).outputs[0])

    def join(self, *geometry):
        return Geometry(nodes.NodeJoinGeometry(self, *geometry).outputs[0])

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Geometry(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='GEOMETRY').outputs[6])

# ------------------------------------------------------------------------------------------------------------------------
# class Curve

class Curve(Geometry):

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        return cls(nodes.NodeBezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).outputs[0])

    @classmethod
    def Circle(cls, resolution=None, radius=None, mode='RADIUS'):
        return nodes.NodeCurveCircle(resolution=resolution, radius=radius, mode=mode)

    @classmethod
    def Line(cls, start=None, end=None, mode='POINTS'):
        return cls(nodes.NodeCurveLine(start=start, end=end, mode=mode).outputs[0])

    @classmethod
    def Quadrilateral(cls, width=None, height=None, mode='RECTANGLE'):
        return cls(nodes.NodeQuadrilateral(width=width, height=height, mode=mode).outputs[0])

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        return cls(nodes.NodeQuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).outputs[0])

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        return nodes.NodeStar(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        return cls(nodes.NodeSpiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).outputs[0])

    def endpoint_selection(self, start_size=None, end_size=None):
        return Boolean(nodes.NodeEndpointSelection(start_size=start_size, end_size=end_size, owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        return Boolean(nodes.NodeHandleTypeSelection(handle_type=handle_type, mode=mode, owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    @property
    def tilt(self):
        return Float(nodes.NodeCurveTilt(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    @property
    def radius(self):
        return Float(nodes.NodeRadius(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    def handle_positions_left(self, relative=None):
        return Vector(nodes.NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='VECTOR', domain='CURVE').outputs[0])

    def handle_positions_right(self, relative=None):
        return Vector(nodes.NodeCurveHandlePositions(relative=relative, owner_socket=self.socket, data_type='VECTOR', domain='CURVE').outputs[1])

    def set_handles(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        self.stack(nodes.NodeSetHandleType(curve=self.connector, selection=selection, handle_type=handle_type, mode=mode))
        return self

    def set_spline_type(self, selection=None, spline_type='POLY'):
        self.stack(nodes.NodeSetSplineType(curve=self.connector, selection=selection, spline_type=spline_type))
        return self

    def fill(self, mode='TRIANGLES'):
        self.stack(nodes.NodeFillCurve(curve=self.connector, mode=mode))
        return self

    def fillet(self, radius=None, limit_radius=None, mode='BEZIER'):
        self.stack(nodes.NodeFilletCurve(curve=self.connector, radius=radius, limit_radius=limit_radius, mode=mode))
        return self

    def resample(self, selection=None, count=None, mode='COUNT'):
        self.stack(nodes.NodeResampleCurve(curve=self.connector, selection=selection, count=count, mode=mode))
        return self

    def reverse(self, selection=None):
        self.stack(nodes.NodeReverseCurve(curve=self.connector, selection=selection))
        return self

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT'):
        self.stack(nodes.NodeSetHandlePositions(curve=self.connector, selection=selection, position=position, offset=offset, mode=mode))
        return self

    def set_radius(self, selection=None, radius=None):
        self.stack(nodes.NodeSetCurveRadius(curve=self.connector, selection=selection, radius=radius))
        return self

    def set_tilt(self, selection=None, tilt=None):
        self.stack(nodes.NodeSetCurveTilt(curve=self.connector, selection=selection, tilt=tilt))
        return self

    def subdivide(self, cuts=None):
        self.stack(nodes.NodeSubdivideCurve(curve=self.connector, cuts=cuts))
        return self

    def trim(self, start=None, end=None, mode='FACTOR'):
        self.stack(nodes.NodeTrimCurve(curve=self.connector, start=start, end=end, mode=mode))
        return self

    def to_mesh(self, profile_curve=None, fill_caps=None):
        return Mesh(nodes.NodeCurvetoMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).outputs[0])

    def to_points(self, count=None, mode='COUNT'):
        return nodes.NodeCurvetoPoints(curve=self, count=count, mode=mode)

    def sample(self, length=None, mode='LENGTH'):
        return nodes.NodeSampleCurve(curve=self, length=length, mode=mode)

    @property
    def length(self):
        if not hasattr(self.top, 'length_'):
            self.top.length_ = nodes.NodeCurveLength(self.connector)
            self.top.length_.prop_of = self.node
        return self.top.length_

    @property
    def F(self):
        if not hasattr(self.top, 'F_'):
            self.top.F_ = Float(self.top.length.length)
        return self.top.F_

# ------------------------------------------------------------------------------------------------------------------------
# class Spline

class Spline(Curve):

    @property
    def cyclic(self):
        return Boolean(nodes.NodeIsSplineCyclic(owner_socket=self.socket, data_type='BOOLEAN', domain='CURVE').outputs[0])

    @property
    def resolution(self):
        return Integer(nodes.NodeSplineResolution(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[0])

    @property
    def length_length(self):
        return Float(nodes.NodeSplineLength(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    @property
    def length_point_count(self):
        return Integer(nodes.NodeSplineLength(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[1])

    @property
    def parameter_factor(self):
        return Float(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[0])

    @property
    def parameter_length(self):
        return Float(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='VALUE', domain='CURVE').outputs[1])

    @property
    def parameter_index(self):
        return Integer(nodes.NodeSplineParameter(owner_socket=self.socket, data_type='INT', domain='CURVE').outputs[2])

    def set_cyclic(self, selection=None, cyclic=None):
        self.stack(nodes.NodeSetSplineCyclic(geometry=self.connector, selection=selection, cyclic=cyclic))
        return self

    def set_resolution(self, selection=None, resolution=None):
        self.stack(nodes.NodeSetSplineResolution(geometry=self.connector, selection=selection, resolution=resolution))
        return self

# ------------------------------------------------------------------------------------------------------------------------
# class Mesh

class Mesh(Geometry):

    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        return cls(nodes.NodeMeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).outputs[0])

    @classmethod
    def Cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        return nodes.NodeCone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)

    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        return cls(nodes.NodeCube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).outputs[0])

    @classmethod
    def Cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        return nodes.NodeCylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)

    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        return cls(nodes.NodeGrid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).outputs[0])

    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        return cls(nodes.NodeIcoSphere(radius=radius, subdivisions=subdivisions).outputs[0])

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        return cls(nodes.NodeMeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).outputs[0])

    def to_curve(self, selection=None):
        return Curve(nodes.NodeMeshtoCurve(mesh=self, selection=selection).outputs[0])

    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):
        return Points(nodes.NodeMeshtoPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).outputs[0])

    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        return cls(nodes.NodeUVSphere(segments=segments, rings=rings, radius=radius).outputs[0])

    @property
    def edge_neighbors(self):
        return Integer(nodes.NodeEdgeNeighbors(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def face_area(self):
        return Float(nodes.NodeFaceArea(owner_socket=self.socket, data_type='VALUE', domain='FACE').outputs[0])

    @property
    def edge_angle_unsigned_angle(self):
        return Float(nodes.NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain='EDGE').outputs[0])

    @property
    def edge_angle_signed_angle(self):
        return Float(nodes.NodeEdgeAngle(owner_socket=self.socket, data_type='VALUE', domain='EDGE').outputs[1])

    @property
    def edge_vertices_vertex_index_1(self):
        return Integer(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[0])

    @property
    def edge_vertices_vertex_index_2(self):
        return Integer(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='INT', domain='EDGE').outputs[1])

    @property
    def edge_vertices_position_1(self):
        return Vector(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='VECTOR', domain='EDGE').outputs[2])

    @property
    def edge_vertices_position_2(self):
        return Vector(nodes.NodeEdgeVertices(owner_socket=self.socket, data_type='VECTOR', domain='EDGE').outputs[3])

    @property
    def face_neighbors_vertex_count(self):
        return Integer(nodes.NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def face_neighbors_face_count(self):
        return Integer(nodes.NodeFaceNeighbors(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[1])

    @property
    def island_island_index(self):
        return Integer(nodes.NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[0])

    @property
    def island_island_count(self):
        return Integer(nodes.NodeMeshIsland(owner_socket=self.socket, data_type='INT', domain='FACE').outputs[1])

    @property
    def vertex_neighbors_vertex_count(self):
        return Integer(nodes.NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[0])

    @property
    def vertex_neighbors_face_count(self):
        return Integer(nodes.NodeVertexNeighbors(owner_socket=self.socket, data_type='INT', domain='POINT').outputs[1])

    def split_edges(self, selection=None):
        self.stack(nodes.NodeSplitEdges(mesh=self.connector, selection=selection))
        return self

    def subdivide(self, level=None):
        self.stack(nodes.NodeSubdivideMesh(mesh=self.connector, level=level))
        return self

    def subdivision_surface(self, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        self.stack(nodes.NodeSubdivisionSurface(mesh=self.connector, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))
        return self

    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        self.stack(nodes.NodeTriangulate(mesh=self.connector, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))
        return self

    def dual(self, keep_boundaries=None):
        self.stack(nodes.NodeDualMesh(mesh=self.connector, keep_boundaries=keep_boundaries))
        return self

    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        self.stack(nodes.NodeExtrudeMesh(mesh=self.connector, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode))
        return self

    def flip_faces(self, selection=None):
        self.stack(nodes.NodeFlipFaces(mesh=self.connector, selection=selection))
        return self

    @classmethod
    def DistributePointsOnFaces(cls, mesh=None, selection=None, density=None, seed=None, distribute_method='RANDOM'):
        return nodes.NodeDistributePointsonFaces(mesh=mesh, selection=selection, density=density, seed=seed, distribute_method=distribute_method)

# ------------------------------------------------------------------------------------------------------------------------
# class Points

class Points(Mesh):

    def set_radius(self, selection=None, radius=None):
        self.stack(nodes.NodeSetPointRadius(points=self.connector, selection=selection, radius=radius))
        return self

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        return Instances(nodes.NodeInstanceonPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).outputs[0])

    def to_vertices(self, selection=None):
        return Mesh(nodes.NodePointstoVertices(points=self, selection=selection).outputs[0])

    def to_volume(self, density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        return Volume(nodes.NodePointstoVolume(points=self, density=density, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).outputs[0])

# ------------------------------------------------------------------------------------------------------------------------
# class Instances

class Instances(Mesh):

    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        self.stack(nodes.NodeRotateInstances(instances=self.connector, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))
        return self

    def scale(self, selection=None, scale=None, center=None, local_space=None):
        self.stack(nodes.NodeScaleInstances(instances=self.connector, selection=selection, scale=scale, center=center, local_space=local_space))
        return self

    def translate(self, selection=None, translation=None, local_space=None):
        self.stack(nodes.NodeTranslateInstances(instances=self.connector, selection=selection, translation=translation, local_space=local_space))
        return self

    def to_points(self, selection=None, position=None, radius=None):
        return Points(nodes.NodeInstancestoPoints(instances=self, selection=selection, position=position, radius=radius).outputs[0])

# ------------------------------------------------------------------------------------------------------------------------
# class Volume

class Volume(Geometry):

    def to_mesh(self, threshold=None, adaptivity=None, resolution_mode='GRID'):
        return Mesh(nodes.NodeVolumetoMesh(volume=self, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).outputs[0])

# ------------------------------------------------------------------------------------------------------------------------
# class Collection

class Collection(bcls.Collection):

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Collection(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='COLLECTION').outputs[8])

# ------------------------------------------------------------------------------------------------------------------------
# class Object

class Object(bcls.Object):

    @property
    def info(self):
        if not hasattr(self.top, 'info_'):
            self.top.info_ = nodes.NodeObjectInfo(self.connector)
            self.top.info_.prop_of = self.node
        return self.top.info_

    @property
    def location(self):
        if not hasattr(self.top, 'location_'):
            self.top.location_ = Vector(self.top.info.location)
        return self.top.location_

    @property
    def rotation(self):
        if not hasattr(self.top, 'rotation_'):
            self.top.rotation_ = Vector(self.top.info.rotation)
        return self.top.rotation_

    @property
    def scale(self):
        if not hasattr(self.top, 'scale_'):
            self.top.scale_ = Vector(self.top.info.scale)
        return self.top.scale_

    @property
    def geometry(self):
        if not hasattr(self.top, 'geometry_'):
            self.top.geometry_ = Geometry(self.top.info.geometry)
        return self.top.geometry_

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Object(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='OBJECT').outputs[7])

# ------------------------------------------------------------------------------------------------------------------------
# class Image

class Image(bcls.Image):

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Image(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='IMAGE').outputs[11])

# ------------------------------------------------------------------------------------------------------------------------
# class Material

class Material(bcls.Material):

    def selection(self):
        return Boolean(nodes.NodeMaterialSelection(material=self).outputs[0])

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Material(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='MATERIAL').outputs[10])

# ------------------------------------------------------------------------------------------------------------------------
# class Texture

class Texture(bcls.Texture):

    @classmethod
    def Brick(cls, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        return nodes.NodeBrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)

    @classmethod
    def Checker(cls, vector=None, color1=None, color2=None, scale=None):
        return nodes.NodeCheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)

    @classmethod
    def Gradient(cls, vector=None, gradient_type='LINEAR'):
        return nodes.NodeGradientTexture(vector=vector, gradient_type=gradient_type)

    @classmethod
    def Magic(cls, vector=None, scale=None, distortion=None, turbulence_depth=2):
        return nodes.NodeMagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)

    @classmethod
    def Musgrave(cls, vector=None, scale=None, detail=None, dimension=None, lacunarity=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        return cls(nodes.NodeMusgraveTexture(vector=vector, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).outputs[0])

    @classmethod
    def Noise(cls, vector=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        return nodes.NodeNoiseTexture(vector=vector, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)

    @classmethod
    def Voronoi(cls, vector=None, scale=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        return nodes.NodeVoronoiTexture(vector=vector, scale=scale, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)

    @classmethod
    def Wave(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        return nodes.NodeWaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)

    @classmethod
    def WhiteNoise(cls, vector=None, noise_dimensions='3D'):
        return nodes.NodeWhiteNoiseTexture(vector=vector, noise_dimensions=noise_dimensions)

    @classmethod
    def Image(cls, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        return nodes.NodeImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)

    @staticmethod
    def switch(switch=None, false=None, true=None):
        return Texture(nodes.NodeSwitch(switch=switch, false=false, true=true, input_type='TEXTURE').outputs[9])

