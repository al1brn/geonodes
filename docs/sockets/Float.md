
# Data socket Float

> Inherits from dsock.Float
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Random](#random) : value (Float)

## Methods

- [abs](#abs) : value (Float)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Float), trailing (Float), total (Float)]
- [arccos](#arccos) : value (Float)
- [arcsin](#arcsin) : value (Float)
- [arctan](#arctan) : value (Float)
- [arctan2](#arctan2) : value (Float)
- [attribute_statistic](#attribute_statistic) : Sockets      [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Float)]
- [ceil](#ceil) : value (Float)
- [clamp](#clamp) : result (Float)
- [color_ramp](#color_ramp) : Sockets      [color (Color), alpha (Float)]
- [compare](#compare) : value (Float)
- [cos](#cos) : value (Float)
- [cosh](#cosh) : value (Float)
- [curve](#curve) : value (Float)
- [degrees](#degrees) : value (Float)
- [equal](#equal) : result (Boolean)
- [exp](#exp) : value (Float)
- [field_at_index](#field_at_index) : value (Float)
- [floor](#floor) : value (Float)
- [fract](#fract) : value (Float)
- [greater_equal](#greater_equal) : result (Boolean)
- [greater_than](#greater_than) : result (Boolean)
- [inverse_sqrt](#inverse_sqrt) : value (Float)
- [less_equal](#less_equal) : result (Boolean)
- [less_than](#less_than) : result (Boolean)
- [log](#log) : value (Float)
- [map_range](#map_range) : result (Float)
- [math_greater_than](#math_greater_than) : value (Float)
- [math_less_than](#math_less_than) : value (Float)
- [max](#max) : value (Float)
- [min](#min) : value (Float)
- [modulo](#modulo) : value (Float)
- [multiply_add](#multiply_add) : value (Float)
- [not_equal](#not_equal) : result (Boolean)
- [pingpong](#pingpong) : value (Float)
- [pow](#pow) : value (Float)
- [radians](#radians) : value (Float)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
- [round](#round) : value (Float)
- [sign](#sign) : value (Float)
- [sin](#sin) : value (Float)
- [sinh](#sinh) : value (Float)
- [smooth_max](#smooth_max) : value (Float)
- [smooth_min](#smooth_min) : value (Float)
- [snap](#snap) : value (Float)
- [sqrt](#sqrt) : value (Float)
- [switch](#switch) : output (Float)
- [tan](#tan) : value (Float)
- [tanh](#tanh) : value (Float)
- [to_integer](#to_integer) : integer (Integer)
- [to_string](#to_string) : string (String)
- [trunc](#trunc) : value (Float)
- [wrap](#wrap) : value (Float)

## Random

Geometry node [*Random Value*].


  Args:
    min: Float
    max: Float
    ID: Integer
    seed: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RandomValue`
  
  - data_type = 'FLOAT'
    
  .. blid:: FunctionNodeRandomValue
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT', label=node_label, node_color=node_color)
    

## accumulate_field

Geometry node [*Accumulate Field*].


  Args:
    group_index: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [leading (Float), trailing (Float), total (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AccumulateField`
  
  - data_type = 'FLOAT'
    
  .. blid:: GeometryNodeAccumulateField
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
    

## attribute_statistic

Geometry node [*Attribute Statistic*].


  Args:
    geometry: Geometry
    selection: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AttributeStatistic`
  
  - data_type = 'FLOAT'
    
  .. blid:: GeometryNodeAttributeStatistic
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
    

## capture_attribute

Geometry node [*Capture Attribute*].


  Args:
    geometry: Geometry
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), attribute (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
  
  - data_type = 'FLOAT'
    
  .. blid:: GeometryNodeCaptureAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
    

## field_at_index

Geometry node [*Field at Index*].


  Args:
    index: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
  
  - data_type = 'FLOAT'
    
  .. blid:: GeometryNodeFieldAtIndex
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
    

## raycast

Geometry node [*Raycast*].


  Args:
    target_geometry: Geometry
    source_position: Vector
    ray_direction: Vector
    ray_length: Float
    mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Raycast`
  
  - data_type = 'FLOAT'
    
  .. blid:: GeometryNodeRaycast
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping, label=node_label, node_color=node_color)
    

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'FLOAT'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='FLOAT', label=node_label, node_color=node_color)
    

## map_range

Geometry node [*Map Range*].


  Args:
    from_min: Float
    from_max: Float
    to_min: Float
    to_max: Float
    clamp (bool): True
    interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MapRange`
  
  - data_type = 'FLOAT'
    
  .. blid:: ShaderNodeMapRange
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type, label=node_label, node_color=node_color)
    

## less_than

Geometry node [*Compare*].


  Args:
    b: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'FLOAT'
  - mode = 'ELEMENT'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## less_equal

Geometry node [*Compare*].


  Args:
    b: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'FLOAT'
  - mode = 'ELEMENT'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## greater_than

Geometry node [*Compare*].


  Args:
    b: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'FLOAT'
  - mode = 'ELEMENT'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## greater_equal

Geometry node [*Compare*].


  Args:
    b: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'FLOAT'
  - mode = 'ELEMENT'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## equal

Geometry node [*Compare*].


  Args:
    b: Float
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'FLOAT'
  - mode = 'ELEMENT'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
    

## not_equal

Geometry node [*Compare*].


  Args:
    b: Float
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'FLOAT'
  - mode = 'ELEMENT'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## multiply_add

Geometry node [*Math*].


  Args:
    value1: Float
    value2: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'MULTIPLY_ADD'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
    

## pow

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'POWER'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='POWER', label=node_label, node_color=node_color)
    

## log

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'LOGARITHM'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color)
    

## sqrt

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SQRT'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='SQRT', label=node_label, node_color=node_color)
    

## inverse_sqrt

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'INVERSE_SQRT'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='INVERSE_SQRT', label=node_label, node_color=node_color)
    

## abs

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'ABSOLUTE'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
    

## exp

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'EXPONENT'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='EXPONENT', label=node_label, node_color=node_color)
    

## min

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'MINIMUM'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color)
    

## max

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'MAXIMUM'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color)
    

## math_less_than

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'LESS_THAN'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color)
    

## math_greater_than

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'GREATER_THAN'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## sign

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SIGN'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='SIGN', label=node_label, node_color=node_color)
    

## compare

Geometry node [*Math*].


  Args:
    value1: Float
    value2: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'COMPARE'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color)
    

## smooth_min

Geometry node [*Math*].


  Args:
    value1: Float
    value2: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SMOOTH_MIN'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color)
    

## smooth_max

Geometry node [*Math*].


  Args:
    value1: Float
    value2: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SMOOTH_MAX'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color)
    

## round

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'ROUND'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='ROUND', label=node_label, node_color=node_color)
    

## floor

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'FLOOR'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='FLOOR', label=node_label, node_color=node_color)
    

## ceil

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'CEIL'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='CEIL', label=node_label, node_color=node_color)
    

## trunc

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'TRUNC'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='TRUNC', label=node_label, node_color=node_color)
    

## fract

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'FRACT'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='FRACT', label=node_label, node_color=node_color)
    

## modulo

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'MODULO'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='MODULO', label=node_label, node_color=node_color)
    

## wrap

Geometry node [*Math*].


  Args:
    value1: Float
    value2: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'WRAP'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color)
    

## snap

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SNAP'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='SNAP', label=node_label, node_color=node_color)
    

## pingpong

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'PINGPONG'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color)
    

## sin

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SINE'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='SINE', label=node_label, node_color=node_color)
    

## cos

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'COSINE'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='COSINE', label=node_label, node_color=node_color)
    

## tan

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'TANGENT'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='TANGENT', label=node_label, node_color=node_color)
    

## arcsin

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'ARCSINE'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='ARCSINE', label=node_label, node_color=node_color)
    

## arccos

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'ARCCOSINE'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='ARCCOSINE', label=node_label, node_color=node_color)
    

## arctan

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'ARCTANGENT'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='ARCTANGENT', label=node_label, node_color=node_color)
    

## arctan2

Geometry node [*Math*].


  Args:
    value1: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'ARCTAN2'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color)
    

## sinh

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'SINH'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='SINH', label=node_label, node_color=node_color)
    

## cosh

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'COSH'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='COSH', label=node_label, node_color=node_color)
    

## tanh

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'TANH'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='TANH', label=node_label, node_color=node_color)
    

## radians

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'RADIANS'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='RADIANS', label=node_label, node_color=node_color)
    

## degrees

Geometry node [*Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Math`
  
  - operation = 'DEGREES'
    
  .. blid:: ShaderNodeMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Math(value0=self, operation='DEGREES', label=node_label, node_color=node_color)
    

## to_integer

Geometry node [*Float to Integer*].


  Args:
    rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FloatToInteger`
  
  
  .. blid:: FunctionNodeFloatToInt
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FloatToInteger(float=self, rounding_mode=rounding_mode, label=node_label, node_color=node_color)
    

## to_string

Geometry node [*Value to String*].


  Args:
    decimals: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    String
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ValueToString`
  
  
  .. blid:: FunctionNodeValueToString
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ValueToString(value=self, decimals=decimals, label=node_label, node_color=node_color)
    

## color_ramp

Geometry node [*ColorRamp*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [color (Color), alpha (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ColorRamp`
  
  
  .. blid:: ShaderNodeValToRGB
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ColorRamp(fac=self, label=node_label, node_color=node_color)
    

## curve

Geometry node [*Float Curve*].


  Args:
    factor: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FloatCurve`
  
  
  .. blid:: ShaderNodeFloatCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FloatCurve(value=self, factor=factor, label=node_label, node_color=node_color)
    

## clamp

Geometry node [*Clamp*].


  Args:
    min: Float
    max: Float
    clamp_type (str): 'MINMAX' in [MINMAX, RANGE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Clamp`
  
  
  .. blid:: ShaderNodeClamp
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type, label=node_label, node_color=node_color)
    
