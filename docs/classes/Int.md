# class Int (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : INT
 - bl_idname : NodeSocketInt

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
 - [equal](#equal) : Compare, a=self, data_type='INT', operation='EQUAL'
 - [evaluate_at_index](#evaluate_at_index) : EvaluateAtIndex, value=self
 - [evaluate_on_domain](#evaluate_on_domain) : EvaluateOnDomain, value=self
 - [exp](#exp) : Math, value=self, operation='EXPONENT'
 - [face_group_boundaries](#face_group_boundaries) : FaceGroupBoundaries, face_group_id=self, return socket
 - [face_of_corner](#face_of_corner) : FaceOfCorner, corner_index=self
 - [float_curve](#float_curve) : FloatCurve, value=self
 - [floor](#floor) : Math, value=self, operation='FLOOR'
 - [floored_modulo](#floored_modulo) : Math, value=self, operation='FLOORED_MODULO'
 - [fract](#fract) : Math, value=self, operation='FRACT'
 - [greater_equal](#greater_equal) : Compare, a=self, data_type='INT', operation='GREATER_EQUAL'
 - [greater_than](#greater_than) : Compare, a=self, data_type='INT', operation='GREATER_THAN'
 - [image_info](#image_info) : ImageInfo, frame=self
 - [index_of_nearest](#index_of_nearest) : IndexOfNearest, group_id=self
 - [inverse_sqrt](#inverse_sqrt) : Math, value=self, operation='INVERSE_SQRT'
 - [less_equal](#less_equal) : Compare, a=self, data_type='INT', operation='LESS_EQUAL'
 - [less_than](#less_than) : Compare, a=self, data_type='INT', operation='LESS_THAN'
 - [log](#log) : Math, value=self, operation='LOGARITHM'
 - [map_range](#map_range) : MapRange, value=self
 - [math](#math) : Math, value=self
 - [math_compare](#math_compare) : Math, value=self, operation='COMPARE'
 - [math_greater_than](#math_greater_than) : Math, value=self, operation='GREATER_THAN'
 - [math_less_than](#math_less_than) : Math, value=self, operation='LESS_THAN'
 - [max](#max) : Math, value=self, operation='MAXIMUM'
 - [min](#min) : Math, value=self, operation='MINIMUM'
 - [mix](#mix) : Mix, a=self
 - [mod](#mod) : Math, value=self, operation='MODULO'
 - [multiply](#multiply) : Math, value=self, operation='MULTIPLY'
 - [multiply_add](#multiply_add) : Math, value=self, operation='MULTIPLY_ADD'
 - [not_equal](#not_equal) : Compare, a=self, data_type='INT', operation='NOT_EQUAL'
 - [offset_corner_in_face](#offset_corner_in_face) : OffsetCornerInFace, corner_index=self
 - [offset_point_in_curve](#offset_point_in_curve) : OffsetPointInCurve, point_index=self
 - [pingpong](#pingpong) : Math, value=self, operation='PINGPONG'
 - [points_of_curve](#points_of_curve) : PointsOfCurve, curve_index=self
 - [power](#power) : Math, value=self, operation='POWER'
 - [radians](#radians) : Math, value=self, operation='RADIANS'
 - [random_value](#random_value) : RandomValue, min=self
 - [raycast](#raycast) : Raycast, attribute=self
 - [repeat_input](#repeat_input) : RepeatInput, iterations=self, return node
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
 - [switch](#switch) : Switch, false=self, input_type='INT'
 - [tan](#tan) : Math, value=self, operation='TANGENT'
 - [tanh](#tanh) : Math, value=self, operation='TANH'
 - [trunc](#trunc) : Math, value=self, operation='TRUNC'
 - [vertex_of_corner](#vertex_of_corner) : VertexOfCorner, corner_index=self
 - [wrap](#wrap) : Math, value=self, operation='WRAP'

## Methods

### abs

Math, value=self, operation='ABSOLUTE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### accumulate_field

AccumulateField, value=self

Node
 - class_name : [AccumulateField](/docs/classes/AccumulateField.md)
 - bl_idname : GeometryNodeAccumulateField

### add

Math, value=self, operation='ADD'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### arccos

Math, value=self, operation='ARCCOSINE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### arcsin

Math, value=self, operation='ARCSINE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### arctan

Math, value=self, operation='ARCTANGENT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### arctan2

Math, value=self, operation='ARCTAN2'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### attribute_statistic

AttributeStatistic, attribute=self

Node
 - class_name : [AttributeStatistic](/docs/classes/AttributeStatistic.md)
 - bl_idname : GeometryNodeAttributeStatistic

### blur_attribute

BlurAttribute, value=self

Node
 - class_name : [BlurAttribute](/docs/classes/BlurAttribute.md)
 - bl_idname : GeometryNodeBlurAttribute

### ceil

Math, value=self, operation='CEIL'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### clamp

Clamp, value=self

Node
 - class_name : [Clamp](/docs/classes/Clamp.md)
 - bl_idname : ShaderNodeClamp

### color_ramp

ColorRamp, fac=self

Node
 - class_name : [ColorRamp](/docs/classes/ColorRamp.md)
 - bl_idname : ShaderNodeValToRGB

### corners_of_edge

CornersOfEdge, edge_index=self

Node
 - class_name : [CornersOfEdge](/docs/classes/CornersOfEdge.md)
 - bl_idname : GeometryNodeCornersOfEdge

### corners_of_face

CornersOfFace, face_index=self

Node
 - class_name : [CornersOfFace](/docs/classes/CornersOfFace.md)
 - bl_idname : GeometryNodeCornersOfFace

### corners_of_vertex

CornersOfVertex, vertex_index=self

Node
 - class_name : [CornersOfVertex](/docs/classes/CornersOfVertex.md)
 - bl_idname : GeometryNodeCornersOfVertex

### cos

Math, value=self, operation='COSINE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### cosh

Math, value=self, operation='COSH'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### curve_of_point

CurveOfPoint, point_index=self

Node
 - class_name : [CurveOfPoint](/docs/classes/CurveOfPoint.md)
 - bl_idname : GeometryNodeCurveOfPoint

### degrees

Math, value=self, operation='DEGREES'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### divide

Math, value=self, operation='DIVIDE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### edges_of_corner

EdgesOfCorner, corner_index=self

Node
 - class_name : [EdgesOfCorner](/docs/classes/EdgesOfCorner.md)
 - bl_idname : GeometryNodeEdgesOfCorner

### edges_of_vertex

EdgesOfVertex, vertex_index=self

Node
 - class_name : [EdgesOfVertex](/docs/classes/EdgesOfVertex.md)
 - bl_idname : GeometryNodeEdgesOfVertex

### equal

Compare, a=self, data_type='INT', operation='EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### evaluate_at_index

EvaluateAtIndex, value=self

Node
 - class_name : [EvaluateAtIndex](/docs/classes/EvaluateAtIndex.md)
 - bl_idname : GeometryNodeFieldAtIndex

### evaluate_on_domain

EvaluateOnDomain, value=self

Node
 - class_name : [EvaluateOnDomain](/docs/classes/EvaluateOnDomain.md)
 - bl_idname : GeometryNodeFieldOnDomain

### exp

Math, value=self, operation='EXPONENT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### face_group_boundaries

FaceGroupBoundaries, face_group_id=self, return socket

Node
 - class_name : [FaceGroupBoundaries](/docs/classes/FaceGroupBoundaries.md)
 - bl_idname : GeometryNodeMeshFaceSetBoundaries

### face_of_corner

FaceOfCorner, corner_index=self

Node
 - class_name : [FaceOfCorner](/docs/classes/FaceOfCorner.md)
 - bl_idname : GeometryNodeFaceOfCorner

### float_curve

FloatCurve, value=self

Node
 - class_name : [FloatCurve](/docs/classes/FloatCurve.md)
 - bl_idname : ShaderNodeFloatCurve

### floor

Math, value=self, operation='FLOOR'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### floored_modulo

Math, value=self, operation='FLOORED_MODULO'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### fract

Math, value=self, operation='FRACT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### greater_equal

Compare, a=self, data_type='INT', operation='GREATER_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### greater_than

Compare, a=self, data_type='INT', operation='GREATER_THAN'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### image_info

ImageInfo, frame=self

Node
 - class_name : [ImageInfo](/docs/classes/ImageInfo.md)
 - bl_idname : GeometryNodeImageInfo

### index_of_nearest

IndexOfNearest, group_id=self

Node
 - class_name : [IndexOfNearest](/docs/classes/IndexOfNearest.md)
 - bl_idname : GeometryNodeIndexOfNearest

### inverse_sqrt

Math, value=self, operation='INVERSE_SQRT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### less_equal

Compare, a=self, data_type='INT', operation='LESS_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### less_than

Compare, a=self, data_type='INT', operation='LESS_THAN'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### log

Math, value=self, operation='LOGARITHM'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### map_range

MapRange, value=self

Node
 - class_name : [MapRange](/docs/classes/MapRange.md)
 - bl_idname : ShaderNodeMapRange

### math

Math, value=self

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### math_compare

Math, value=self, operation='COMPARE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### math_greater_than

Math, value=self, operation='GREATER_THAN'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### math_less_than

Math, value=self, operation='LESS_THAN'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### max

Math, value=self, operation='MAXIMUM'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### min

Math, value=self, operation='MINIMUM'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### mix

Mix, a=self

Node
 - class_name : [Mix](/docs/classes/Mix.md)
 - bl_idname : ShaderNodeMix

### mod

Math, value=self, operation='MODULO'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### multiply

Math, value=self, operation='MULTIPLY'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### multiply_add

Math, value=self, operation='MULTIPLY_ADD'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### not_equal

Compare, a=self, data_type='INT', operation='NOT_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### offset_corner_in_face

OffsetCornerInFace, corner_index=self

Node
 - class_name : [OffsetCornerInFace](/docs/classes/OffsetCornerInFace.md)
 - bl_idname : GeometryNodeOffsetCornerInFace

### offset_point_in_curve

OffsetPointInCurve, point_index=self

Node
 - class_name : [OffsetPointInCurve](/docs/classes/OffsetPointInCurve.md)
 - bl_idname : GeometryNodeOffsetPointInCurve

### pingpong

Math, value=self, operation='PINGPONG'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### points_of_curve

PointsOfCurve, curve_index=self

Node
 - class_name : [PointsOfCurve](/docs/classes/PointsOfCurve.md)
 - bl_idname : GeometryNodePointsOfCurve

### power

Math, value=self, operation='POWER'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### radians

Math, value=self, operation='RADIANS'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### random_value

RandomValue, min=self

Node
 - class_name : [RandomValue](/docs/classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

### raycast

Raycast, attribute=self

Node
 - class_name : [Raycast](/docs/classes/Raycast.md)
 - bl_idname : GeometryNodeRaycast

### repeat_input

RepeatInput, iterations=self, return node

Node
 - class_name : [RepeatInput](/docs/classes/RepeatInput.md)
 - bl_idname : GeometryNodeRepeatInput

### round

Math, value=self, operation='ROUND'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### sample_curve

SampleCurve, value=self

Node
 - class_name : [SampleCurve](/docs/classes/SampleCurve.md)
 - bl_idname : GeometryNodeSampleCurve

### sample_index

SampleIndex, value=self

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### sample_nearest_surface

SampleNearestSurface, value=self

Node
 - class_name : [SampleNearestSurface](/docs/classes/SampleNearestSurface.md)
 - bl_idname : GeometryNodeSampleNearestSurface

### sample_uv_surface

SampleUVSurface, value=self

Node
 - class_name : [SampleUVSurface](/docs/classes/SampleUVSurface.md)
 - bl_idname : GeometryNodeSampleUVSurface

### sample_volume

SampleVolume, grid=self

Node
 - class_name : [SampleVolume](/docs/classes/SampleVolume.md)
 - bl_idname : GeometryNodeSampleVolume

### shortest_edge_paths

ShortestEdgePaths, edge_cost=self

Node
 - class_name : [ShortestEdgePaths](/docs/classes/ShortestEdgePaths.md)
 - bl_idname : GeometryNodeInputShortestEdgePaths

### sign

Math, value=self, operation='SIGN'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### sin

Math, value=self, operation='SINE'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### sinh

Math, value=self, operation='SINH'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### smooth_max

Math, value=self, operation='SMOOTH_MAX'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### smooth_min

Math, value=self, operation='SMOOTH_MIN'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### snap

Math, value=self, operation='SNAP'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### sqrt

Math, value=self, operation='SQRT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### subtract

Math, value=self, operation='SUBTRACT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### switch

Switch, false=self, input_type='INT'

Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

### tan

Math, value=self, operation='TANGENT'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### tanh

Math, value=self, operation='TANH'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### trunc

Math, value=self, operation='TRUNC'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath

### vertex_of_corner

VertexOfCorner, corner_index=self

Node
 - class_name : [VertexOfCorner](/docs/classes/VertexOfCorner.md)
 - bl_idname : GeometryNodeVertexOfCorner

### wrap

Math, value=self, operation='WRAP'

Node
 - class_name : [Math](/docs/classes/Math.md)
 - bl_idname : ShaderNodeMath
