
# Data socket Integer

> Inherits from dsock.Integer
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Random](#random) : value (Integer)

## Methods

- [abs](#abs) : value (Float)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Integer), trailing (Integer), total (Integer)]
- [arccos](#arccos) : value (Float)
- [arcsin](#arcsin) : value (Float)
- [arctan](#arctan) : value (Float)
- [arctan2](#arctan2) : value (Float)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Integer)]
- [ceil](#ceil) : value (Float)
- [compare](#compare) : value (Float)
- [cos](#cos) : value (Float)
- [cosh](#cosh) : value (Float)
- [degrees](#degrees) : value (Float)
- [equal](#equal) : result (Boolean)
- [exp](#exp) : value (Float)
- [field_at_index](#field_at_index) : value (Integer)
- [floor](#floor) : value (Float)
- [fract](#fract) : value (Float)
- [greater_equal](#greater_equal) : result (Boolean)
- [greater_than](#greater_than) : result (Boolean)
- [inverse_sqrt](#inverse_sqrt) : value (Float)
- [less_equal](#less_equal) : result (Boolean)
- [less_than](#less_than) : result (Boolean)
- [log](#log) : value (Float)
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
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
- [round](#round) : value (Float)
- [sign](#sign) : value (Float)
- [sin](#sin) : value (Float)
- [sinh](#sinh) : value (Float)
- [smooth_max](#smooth_max) : value (Float)
- [smooth_min](#smooth_min) : value (Float)
- [snap](#snap) : value (Float)
- [sqrt](#sqrt) : value (Float)
- [switch](#switch) : output (Integer)
- [tan](#tan) : value (Float)
- [tanh](#tanh) : value (Float)
- [trunc](#trunc) : value (Float)
- [wrap](#wrap) : value (Float)

## Random

Geometry node [*Random Value*].


  Args:
    min: Integer
    max: Integer
    ID: Integer
    seed: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RandomValue`
  
  - data_type = 'INT'
    
  .. blid:: FunctionNodeRandomValue
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT', label=node_label, node_color=node_color)
    

## accumulate_field

Geometry node [*Accumulate Field*].


  Args:
    group_index: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [leading (Integer), trailing (Integer), total (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AccumulateField`
  
  - data_type = 'INT'
    
  .. blid:: GeometryNodeAccumulateField
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain, label=node_label, node_color=node_color)
    

## capture_attribute

Geometry node [*Capture Attribute*].


  Args:
    geometry: Geometry
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), attribute (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
  
  - data_type = 'INT'
    
  .. blid:: GeometryNodeCaptureAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain, label=node_label, node_color=node_color)
    

## field_at_index

Geometry node [*Field at Index*].


  Args:
    value: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
  
  - data_type = 'INT'
    
  .. blid:: GeometryNodeFieldAtIndex
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
    

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
    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Raycast`
  
  - data_type = 'INT'
    
  .. blid:: GeometryNodeRaycast
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, label=node_label, node_color=node_color)
    

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'INT'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='INT', label=node_label, node_color=node_color)
    

## less_than

Geometry node [*Compare*].


  Args:
    b: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'INT'
  - mode = 'ELEMENT'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## less_equal

Geometry node [*Compare*].


  Args:
    b: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'INT'
  - mode = 'ELEMENT'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## greater_than

Geometry node [*Compare*].


  Args:
    b: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'INT'
  - mode = 'ELEMENT'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## greater_equal

Geometry node [*Compare*].


  Args:
    b: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'INT'
  - mode = 'ELEMENT'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## equal

Geometry node [*Compare*].


  Args:
    b: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'INT'
  - mode = 'ELEMENT'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
    

## not_equal

Geometry node [*Compare*].


  Args:
    b: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'INT'
  - mode = 'ELEMENT'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

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
    
