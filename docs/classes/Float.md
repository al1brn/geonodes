# class Float (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : VALUE
 - bl_idname : NodeSocketFloat

Methods
 - [abs](#abs) : Math, value=self, operation='ABSOLUTE'
 - [accumulate_field](#accumulate_field) : AccumulateField, value=self
 - [add](#add) : Math, value=self, operation='ADD'
 - [arccos](#arccos) : Math, value=self, operation='ARCCOSINE'
 - [arcsin](#arcsin) : Math, value=self, operation='ARCSINE'
 - [arctan](#arctan) : Math, value=self, operation='ARCTANGENT'
 - [arctan2](#arctan2) : Math, value=self, operation='ARCTAN2'
 - [attribute_statistic](#attribute_statistic) : AttributeStatistic, attribute=self
 - [blur_attribute](#blur_attribute) : BlurAttribute, value=self
 - [ceil](#ceil) : Math, value=self, operation='CEIL'
 - [clamp](#clamp) : Clamp, value=self
 - [color_ramp](#color_ramp) : ColorRamp, fac=self
 - [corners_of_edge](#corners_of_edge) : CornersOfEdge, edge_index=self
 - [corners_of_face](#corners_of_face) : CornersOfFace, face_index=self
 - [corners_of_vertex](#corners_of_vertex) : CornersOfVertex, vertex_index=self
 - [cos](#cos) : Math, value=self, operation='COSINE'
 - [cosh](#cosh) : Math, value=self, operation='COSH'
 - [curve_of_point](#curve_of_point) : CurveOfPoint, point_index=self
 - [degrees](#degrees) : Math, value=self, operation='DEGREES'
 - [divide](#divide) : Math, value=self, operation='DIVIDE'
 - [edges_of_corner](#edges_of_corner) : EdgesOfCorner, corner_index=self
 - [edges_of_vertex](#edges_of_vertex) : EdgesOfVertex, vertex_index=self
 - [equal](#equal) : Compare, a=self, data_type='FLOAT', operation='EQUAL'
 - [evaluate_at_index](#evaluate_at_index) : EvaluateAtIndex, value=self
 - [evaluate_on_domain](#evaluate_on_domain) : EvaluateOnDomain, value=self
 - [exp](#exp) : Math, value=self, operation='EXPONENT'
 - [face_of_corner](#face_of_corner) : FaceOfCorner, corner_index=self
 - [float_curve](#float_curve) : FloatCurve, value=self
 - [float_to_integer](#float_to_integer) : FloatToInteger, float=self, return socket
 - [floor](#floor) : Math, value=self, operation='FLOOR'
 - [floored_modulo](#floored_modulo) : Math, value=self, operation='FLOORED_MODULO'
 - [fract](#fract) : Math, value=self, operation='FRACT'
 - [greater_equal](#greater_equal) : Compare, a=self, data_type='FLOAT', operation='GREATER_EQUAL'
 - [greater_than](#greater_than) : Compare, a=self, data_type='FLOAT', operation='GREATER_THAN'
 - [image_info](#image_info) : ImageInfo, frame=self
 - [index_of_nearest](#index_of_nearest) : IndexOfNearest, group_id=self
 - [inverse_sqrt](#inverse_sqrt) : Math, value=self, operation='INVERSE_SQRT'
 - [is_face_planar](#is_face_planar) : IsFacePlanar, threshold=self, return socket
 - [less_equal](#less_equal) : Compare, a=self, data_type='FLOAT', operation='LESS_EQUAL'
 - [less_than](#less_than) : Compare, a=self, data_type='FLOAT', operation='LESS_THAN'
 - [log](#log) : Math, value=self, operation='LOGARITHM'
 - [map_range](#map_range) : MapRange, value=self
 - [math](#math) : Math, value=self
 - [math_compare](#math_compare) : Math, value=self, operation='COMPARE'
 - [math_greater_than](#math_greater_than) : Math, value=self, operation='GREATER_THAN'
 - [math_less_than](#math_less_than) : Math, value=self, operation='LESS_THAN'
 - [max](#max) : Math, value=self, operation='MAXIMUM'
 - [min](#min) : Math, value=self, operation='MINIMUM'
 - [mix](#mix) : Mix, a=self, data_type='FLOAT'
 - [mod](#mod) : Math, value=self, operation='MODULO'
 - [multiply](#multiply) : Math, value=self, operation='MULTIPLY'
 - [multiply_add](#multiply_add) : Math, value=self, operation='MULTIPLY_ADD'
 - [not_equal](#not_equal) : Compare, a=self, data_type='FLOAT', operation='NOT_EQUAL'
 - [offset_corner_in_face](#offset_corner_in_face) : OffsetCornerInFace, corner_index=self
 - [offset_point_in_curve](#offset_point_in_curve) : OffsetPointInCurve, point_index=self
 - [pingpong](#pingpong) : Math, value=self, operation='PINGPONG'
 - [points_of_curve](#points_of_curve) : PointsOfCurve, curve_index=self
 - [power](#power) : Math, value=self, operation='POWER'
 - [radians](#radians) : Math, value=self, operation='RADIANS'
 - [random_value](#random_value) : RandomValue, min=self
 - [raycast](#raycast) : Raycast, attribute=self
 - [round](#round) : Math, value=self, operation='ROUND'
 - [sample_curve](#sample_curve) : SampleCurve, value=self
 - [sample_index](#sample_index) : SampleIndex, value=self
 - [sample_nearest_surface](#sample_nearest_surface) : SampleNearestSurface, value=self
 - [sample_uv_surface](#sample_uv_surface) : SampleUVSurface, value=self
 - [sample_volume](#sample_volume) : SampleVolume, grid=self
 - [shortest_edge_paths](#shortest_edge_paths) : ShortestEdgePaths, edge_cost=self
 - [sign](#sign) : Math, value=self, operation='SIGN'
 - [sin](#sin) : Math, value=self, operation='SINE'
 - [sinh](#sinh) : Math, value=self, operation='SINH'
 - [smooth_max](#smooth_max) : Math, value=self, operation='SMOOTH_MAX'
 - [smooth_min](#smooth_min) : Math, value=self, operation='SMOOTH_MIN'
 - [snap](#snap) : Math, value=self, operation='SNAP'
 - [sqrt](#sqrt) : Math, value=self, operation='SQRT'
 - [subtract](#subtract) : Math, value=self, operation='SUBTRACT'
 - [switch](#switch) : Switch, false=self, input_type='FLOAT'
 - [tan](#tan) : Math, value=self, operation='TANGENT'
 - [tanh](#tanh) : Math, value=self, operation='TANH'
 - [trunc](#trunc) : Math, value=self, operation='TRUNC'
 - [vertex_of_corner](#vertex_of_corner) : VertexOfCorner, corner_index=self
 - [wrap](#wrap) : Math, value=self, operation='WRAP'

## Methods

### abs

> Math, value=self, operation='ABSOLUTE'

``` python
def abs(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ABSOLUTE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### accumulate_field

> AccumulateField, value=self

``` python
def accumulate_field(self, group_id=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [AccumulateField](/docs/classes/AccumulateField.md)
 - bl_idname : GeometryNodeAccumulateField

Arguments
 - group_id : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - group_id : group_id
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

### add

> Math, value=self, operation='ADD'

``` python
def add(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arccos

> Math, value=self, operation='ARCCOSINE'

``` python
def arccos(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ARCCOSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arcsin

> Math, value=self, operation='ARCSINE'

``` python
def arcsin(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ARCSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arctan

> Math, value=self, operation='ARCTANGENT'

``` python
def arctan(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ARCTANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arctan2

> Math, value=self, operation='ARCTAN2'

``` python
def arctan2(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'ARCTAN2'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### attribute_statistic

> AttributeStatistic, attribute=self

``` python
def attribute_statistic(self, geometry=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [AttributeStatistic](/docs/classes/AttributeStatistic.md)
 - bl_idname : GeometryNodeAttributeStatistic

Arguments
 - geometry : None
 - selection : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - attribute : self
 - selection : self._get_selection(selection)
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

### blur_attribute

> BlurAttribute, value=self

``` python
def blur_attribute(self, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [BlurAttribute](/docs/classes/BlurAttribute.md)
 - bl_idname : GeometryNodeBlurAttribute

Arguments
 - iterations : None
 - weight : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - iterations : iterations
 - weight : weight
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

### ceil

> Math, value=self, operation='CEIL'

``` python
def ceil(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'CEIL'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### clamp

> Clamp, value=self

``` python
def clamp(self, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None):
```
Node
 - class_name : [Clamp](/docs/classes/Clamp.md)
 - bl_idname : ShaderNodeClamp

Arguments
 - min : None
 - max : None
 - clamp_type : 'MINMAX'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - min : min
 - max : max
 - clamp_type : clamp_type
 - node_label : node_label
 - node_color : node_color

### color_ramp

> ColorRamp, fac=self

``` python
def color_ramp(self, color_ramp=None, node_label=None, node_color=None):
```
Node
 - class_name : [ColorRamp](/docs/classes/ColorRamp.md)
 - bl_idname : ShaderNodeValToRGB

Arguments
 - color_ramp
 - node_label : None
 - node_color : None

Node initialization
 - fac : self
 - color_ramp : color_ramp
 - node_label : node_label
 - node_color : node_color

### corners_of_edge

> CornersOfEdge, edge_index=self

``` python
def corners_of_edge(self, weights=None, sort_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [CornersOfEdge](/docs/classes/CornersOfEdge.md)
 - bl_idname : GeometryNodeCornersOfEdge

Arguments
 - weights : None
 - sort_index : None
 - node_label : None
 - node_color : None

Node initialization
 - edge_index : self
 - weights : weights
 - sort_index : sort_index
 - node_label : node_label
 - node_color : node_color

### corners_of_face

> CornersOfFace, face_index=self

``` python
def corners_of_face(self, weights=None, sort_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [CornersOfFace](/docs/classes/CornersOfFace.md)
 - bl_idname : GeometryNodeCornersOfFace

Arguments
 - weights : None
 - sort_index : None
 - node_label : None
 - node_color : None

Node initialization
 - face_index : self
 - weights : weights
 - sort_index : sort_index
 - node_label : node_label
 - node_color : node_color

### corners_of_vertex

> CornersOfVertex, vertex_index=self

``` python
def corners_of_vertex(self, weights=None, sort_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [CornersOfVertex](/docs/classes/CornersOfVertex.md)
 - bl_idname : GeometryNodeCornersOfVertex

Arguments
 - weights : None
 - sort_index : None
 - node_label : None
 - node_color : None

Node initialization
 - vertex_index : self
 - weights : weights
 - sort_index : sort_index
 - node_label : node_label
 - node_color : node_color

### cos

> Math, value=self, operation='COSINE'

``` python
def cos(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'COSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### cosh

> Math, value=self, operation='COSH'

``` python
def cosh(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'COSH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### curve_of_point

> CurveOfPoint, point_index=self

``` python
def curve_of_point(self, node_label=None, node_color=None):
```
Node
 - class_name : [CurveOfPoint](/docs/classes/CurveOfPoint.md)
 - bl_idname : GeometryNodeCurveOfPoint

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - point_index : self
 - node_label : node_label
 - node_color : node_color

### degrees

> Math, value=self, operation='DEGREES'

``` python
def degrees(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'DEGREES'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### divide

> Math, value=self, operation='DIVIDE'

``` python
def divide(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'DIVIDE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### edges_of_corner

> EdgesOfCorner, corner_index=self

``` python
def edges_of_corner(self, node_label=None, node_color=None):
```
Node
 - class_name : [EdgesOfCorner](/docs/classes/EdgesOfCorner.md)
 - bl_idname : GeometryNodeEdgesOfCorner

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - corner_index : self
 - node_label : node_label
 - node_color : node_color

### edges_of_vertex

> EdgesOfVertex, vertex_index=self

``` python
def edges_of_vertex(self, weights=None, sort_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [EdgesOfVertex](/docs/classes/EdgesOfVertex.md)
 - bl_idname : GeometryNodeEdgesOfVertex

Arguments
 - weights : None
 - sort_index : None
 - node_label : None
 - node_color : None

Node initialization
 - vertex_index : self
 - weights : weights
 - sort_index : sort_index
 - node_label : node_label
 - node_color : node_color

### equal

> Compare, a=self, data_type='FLOAT', operation='EQUAL'

``` python
def equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - epsilon : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - epsilon : epsilon
 - data_type : 'FLOAT'
 - mode : mode
 - operation : 'EQUAL'
 - node_label : node_label
 - node_color : node_color

### evaluate_at_index

> EvaluateAtIndex, value=self

``` python
def evaluate_at_index(self, index=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [EvaluateAtIndex](/docs/classes/EvaluateAtIndex.md)
 - bl_idname : GeometryNodeFieldAtIndex

Arguments
 - index : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - index : index
 - value : self
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

### evaluate_on_domain

> EvaluateOnDomain, value=self

``` python
def evaluate_on_domain(self, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [EvaluateOnDomain](/docs/classes/EvaluateOnDomain.md)
 - bl_idname : GeometryNodeFieldOnDomain

Arguments
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

### exp

> Math, value=self, operation='EXPONENT'

``` python
def exp(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'EXPONENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### face_of_corner

> FaceOfCorner, corner_index=self

``` python
def face_of_corner(self, node_label=None, node_color=None):
```
Node
 - class_name : [FaceOfCorner](/docs/classes/FaceOfCorner.md)
 - bl_idname : GeometryNodeFaceOfCorner

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - corner_index : self
 - node_label : node_label
 - node_color : node_color

### float_curve

> FloatCurve, value=self

``` python
def float_curve(self, factor=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [FloatCurve](/docs/classes/FloatCurve.md)
 - bl_idname : ShaderNodeFloatCurve

Arguments
 - factor : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - value : self
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

### float_to_integer

> FloatToInteger, float=self, return socket

``` python
def float_to_integer(self, rounding_mode='ROUND', node_label=None, node_color=None):
```
Node
 - class_name : [FloatToInteger](/docs/classes/FloatToInteger.md)
 - bl_idname : FunctionNodeFloatToInt

Arguments
 - rounding_mode : 'ROUND'
 - node_label : None
 - node_color : None

Node initialization
 - float : self
 - rounding_mode : rounding_mode
 - node_label : node_label
 - node_color : node_color

### floor

> Math, value=self, operation='FLOOR'

``` python
def floor(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'FLOOR'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### floored_modulo

> Math, value=self, operation='FLOORED_MODULO'

``` python
def floored_modulo(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'FLOORED_MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### fract

> Math, value=self, operation='FRACT'

``` python
def fract(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'FRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### greater_equal

> Compare, a=self, data_type='FLOAT', operation='GREATER_EQUAL'

``` python
def greater_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'FLOAT'
 - mode : mode
 - operation : 'GREATER_EQUAL'
 - node_label : node_label
 - node_color : node_color

### greater_than

> Compare, a=self, data_type='FLOAT', operation='GREATER_THAN'

``` python
def greater_than(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'FLOAT'
 - mode : mode
 - operation : 'GREATER_THAN'
 - node_label : node_label
 - node_color : node_color

### image_info

> ImageInfo, frame=self

``` python
def image_info(self, image=None, node_label=None, node_color=None):
```
Node
 - class_name : [ImageInfo](/docs/classes/ImageInfo.md)
 - bl_idname : GeometryNodeImageInfo

Arguments
 - image : None
 - node_label : None
 - node_color : None

Node initialization
 - image : image
 - frame : self
 - node_label : node_label
 - node_color : node_color

### index_of_nearest

> IndexOfNearest, group_id=self

``` python
def index_of_nearest(self, position=None, node_label=None, node_color=None):
```
Node
 - class_name : [IndexOfNearest](/docs/classes/IndexOfNearest.md)
 - bl_idname : GeometryNodeIndexOfNearest

Arguments
 - position : None
 - node_label : None
 - node_color : None

Node initialization
 - position : position
 - group_id : self
 - node_label : node_label
 - node_color : node_color

### inverse_sqrt

> Math, value=self, operation='INVERSE_SQRT'

``` python
def inverse_sqrt(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'INVERSE_SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### is_face_planar

> IsFacePlanar, threshold=self, return socket

``` python
def is_face_planar(self, node_label=None, node_color=None):
```
Node
 - class_name : [IsFacePlanar](/docs/classes/IsFacePlanar.md)
 - bl_idname : GeometryNodeInputMeshFaceIsPlanar

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - threshold : self
 - node_label : node_label
 - node_color : node_color

### less_equal

> Compare, a=self, data_type='FLOAT', operation='LESS_EQUAL'

``` python
def less_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'FLOAT'
 - mode : mode
 - operation : 'LESS_EQUAL'
 - node_label : node_label
 - node_color : node_color

### less_than

> Compare, a=self, data_type='FLOAT', operation='LESS_THAN'

``` python
def less_than(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'FLOAT'
 - mode : mode
 - operation : 'LESS_THAN'
 - node_label : node_label
 - node_color : node_color

### log

> Math, value=self, operation='LOGARITHM'

``` python
def log(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'LOGARITHM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### map_range

> MapRange, value=self

``` python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, vector=None, steps=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', node_label=None, node_color=None):
```
Node
 - class_name : [MapRange](/docs/classes/MapRange.md)
 - bl_idname : ShaderNodeMapRange

Arguments
 - from_min : None
 - from_max : None
 - to_min : None
 - to_max : None
 - vector : None
 - steps : None
 - clamp : True
 - data_type : 'FLOAT'
 - interpolation_type : 'LINEAR'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - from_min : from_min
 - from_max : from_max
 - to_min : to_min
 - to_max : to_max
 - vector : vector
 - steps : steps
 - clamp : clamp
 - data_type : data_type
 - interpolation_type : interpolation_type
 - node_label : node_label
 - node_color : node_color

### math

> Math, value=self

``` python
def math(self, value=None, value_1=None, operation='ADD', use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - operation : 'ADD'
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : operation
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### math_compare

> Math, value=self, operation='COMPARE'

``` python
def math_compare(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'COMPARE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### math_greater_than

> Math, value=self, operation='GREATER_THAN'

``` python
def math_greater_than(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'GREATER_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### math_less_than

> Math, value=self, operation='LESS_THAN'

``` python
def math_less_than(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'LESS_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### max

> Math, value=self, operation='MAXIMUM'

``` python
def max(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MAXIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### min

> Math, value=self, operation='MINIMUM'

``` python
def min(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MINIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### mix

> Mix, a=self, data_type='FLOAT'

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - blend_type : 'MIX'
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : blend_type
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'FLOAT'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mod

> Math, value=self, operation='MODULO'

``` python
def mod(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### multiply

> Math, value=self, operation='MULTIPLY'

``` python
def multiply(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MULTIPLY'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### multiply_add

> Math, value=self, operation='MULTIPLY_ADD'

``` python
def multiply_add(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'MULTIPLY_ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### not_equal

> Compare, a=self, data_type='FLOAT', operation='NOT_EQUAL'

``` python
def not_equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - epsilon : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - epsilon : epsilon
 - data_type : 'FLOAT'
 - mode : mode
 - operation : 'NOT_EQUAL'
 - node_label : node_label
 - node_color : node_color

### offset_corner_in_face

> OffsetCornerInFace, corner_index=self

``` python
def offset_corner_in_face(self, offset=None, node_label=None, node_color=None):
```
Node
 - class_name : [OffsetCornerInFace](/docs/classes/OffsetCornerInFace.md)
 - bl_idname : GeometryNodeOffsetCornerInFace

Arguments
 - offset : None
 - node_label : None
 - node_color : None

Node initialization
 - corner_index : self
 - offset : offset
 - node_label : node_label
 - node_color : node_color

### offset_point_in_curve

> OffsetPointInCurve, point_index=self

``` python
def offset_point_in_curve(self, offset=None, node_label=None, node_color=None):
```
Node
 - class_name : [OffsetPointInCurve](/docs/classes/OffsetPointInCurve.md)
 - bl_idname : GeometryNodeOffsetPointInCurve

Arguments
 - offset : None
 - node_label : None
 - node_color : None

Node initialization
 - point_index : self
 - offset : offset
 - node_label : node_label
 - node_color : node_color

### pingpong

> Math, value=self, operation='PINGPONG'

``` python
def pingpong(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'PINGPONG'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### points_of_curve

> PointsOfCurve, curve_index=self

``` python
def points_of_curve(self, weights=None, sort_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [PointsOfCurve](/docs/classes/PointsOfCurve.md)
 - bl_idname : GeometryNodePointsOfCurve

Arguments
 - weights : None
 - sort_index : None
 - node_label : None
 - node_color : None

Node initialization
 - curve_index : self
 - weights : weights
 - sort_index : sort_index
 - node_label : node_label
 - node_color : node_color

### power

> Math, value=self, operation='POWER'

``` python
def power(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'POWER'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### radians

> Math, value=self, operation='RADIANS'

``` python
def radians(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'RADIANS'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### random_value

> RandomValue, min=self

``` python
def random_value(self, max=None, ID=None, seed=None, probability=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [RandomValue](/docs/classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

Arguments
 - max : None
 - ID : None
 - seed : None
 - probability : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - min : self
 - max : max
 - ID : ID
 - seed : seed
 - probability : probability
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

### raycast

> Raycast, attribute=self

``` python
def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', node_label=None, node_color=None):
```
Node
 - class_name : [Raycast](/docs/classes/Raycast.md)
 - bl_idname : GeometryNodeRaycast

Arguments
 - target_geometry : None
 - source_position : None
 - ray_direction : None
 - ray_length : None
 - data_type : 'FLOAT'
 - mapping : 'INTERPOLATED'
 - node_label : None
 - node_color : None

Node initialization
 - target_geometry : target_geometry
 - attribute : self
 - source_position : source_position
 - ray_direction : ray_direction
 - ray_length : ray_length
 - data_type : data_type
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

### round

> Math, value=self, operation='ROUND'

``` python
def round(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ROUND'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sample_curve

> SampleCurve, value=self

``` python
def sample_curve(self, curves=None, factor=None, curve_index=None, length=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, node_label=None, node_color=None):
```
Node
 - class_name : [SampleCurve](/docs/classes/SampleCurve.md)
 - bl_idname : GeometryNodeSampleCurve

Arguments
 - curves : None
 - factor : None
 - curve_index : None
 - length : None
 - data_type : 'FLOAT'
 - mode : 'FACTOR'
 - use_all_curves : False
 - node_label : None
 - node_color : None

Node initialization
 - curves : curves
 - value : self
 - factor : factor
 - curve_index : curve_index
 - length : length
 - data_type : data_type
 - mode : mode
 - use_all_curves : use_all_curves
 - node_label : node_label
 - node_color : node_color

### sample_index

> SampleIndex, value=self

``` python
def sample_index(self, geometry=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - geometry : None
 - index : None
 - clamp : False
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - value : self
 - index : index
 - clamp : clamp
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

### sample_nearest_surface

> SampleNearestSurface, value=self

``` python
def sample_nearest_surface(self, mesh=None, sample_position=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleNearestSurface](/docs/classes/SampleNearestSurface.md)
 - bl_idname : GeometryNodeSampleNearestSurface

Arguments
 - mesh : None
 - sample_position : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - value : self
 - sample_position : sample_position
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

### sample_uv_surface

> SampleUVSurface, value=self

``` python
def sample_uv_surface(self, mesh=None, source_uv_map=None, sample_uv=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleUVSurface](/docs/classes/SampleUVSurface.md)
 - bl_idname : GeometryNodeSampleUVSurface

Arguments
 - mesh : None
 - source_uv_map : None
 - sample_uv : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - value : self
 - source_uv_map : source_uv_map
 - sample_uv : sample_uv
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

### sample_volume

> SampleVolume, grid=self

``` python
def sample_volume(self, volume=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR', node_label=None, node_color=None):
```
Node
 - class_name : [SampleVolume](/docs/classes/SampleVolume.md)
 - bl_idname : GeometryNodeSampleVolume

Arguments
 - volume : None
 - position : None
 - grid_type : 'FLOAT'
 - interpolation_mode : 'TRILINEAR'
 - node_label : None
 - node_color : None

Node initialization
 - volume : volume
 - grid : self
 - position : position
 - grid_type : grid_type
 - interpolation_mode : interpolation_mode
 - node_label : node_label
 - node_color : node_color

### shortest_edge_paths

> ShortestEdgePaths, edge_cost=self

``` python
def shortest_edge_paths(self, end_vertex=None, node_label=None, node_color=None):
```
Node
 - class_name : [ShortestEdgePaths](/docs/classes/ShortestEdgePaths.md)
 - bl_idname : GeometryNodeInputShortestEdgePaths

Arguments
 - end_vertex : None
 - node_label : None
 - node_color : None

Node initialization
 - end_vertex : end_vertex
 - edge_cost : self
 - node_label : node_label
 - node_color : node_color

### sign

> Math, value=self, operation='SIGN'

``` python
def sign(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SIGN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sin

> Math, value=self, operation='SINE'

``` python
def sin(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sinh

> Math, value=self, operation='SINH'

``` python
def sinh(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SINH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### smooth_max

> Math, value=self, operation='SMOOTH_MAX'

``` python
def smooth_max(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'SMOOTH_MAX'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### smooth_min

> Math, value=self, operation='SMOOTH_MIN'

``` python
def smooth_min(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'SMOOTH_MIN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### snap

> Math, value=self, operation='SNAP'

``` python
def snap(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'SNAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sqrt

> Math, value=self, operation='SQRT'

``` python
def sqrt(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### subtract

> Math, value=self, operation='SUBTRACT'

``` python
def subtract(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'SUBTRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### switch

> Switch, false=self, input_type='FLOAT'

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - true : None
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : self
 - true : true
 - input_type : 'FLOAT'
 - node_label : node_label
 - node_color : node_color

### tan

> Math, value=self, operation='TANGENT'

``` python
def tan(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'TANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### tanh

> Math, value=self, operation='TANH'

``` python
def tanh(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'TANH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### trunc

> Math, value=self, operation='TRUNC'

``` python
def trunc(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'TRUNC'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### vertex_of_corner

> VertexOfCorner, corner_index=self

``` python
def vertex_of_corner(self, node_label=None, node_color=None):
```
Node
 - class_name : [VertexOfCorner](/docs/classes/VertexOfCorner.md)
 - bl_idname : GeometryNodeVertexOfCorner

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - corner_index : self
 - node_label : node_label
 - node_color : node_color

### wrap

> Math, value=self, operation='WRAP'

``` python
def wrap(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'WRAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color
