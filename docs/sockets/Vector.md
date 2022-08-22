
# Data socket Vector

> Inherits from dsock.Vector
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [AlignToVector](#aligntovector) : rotation (Vector)
- [Combine](#combine) : vector (Vector)
- [Random](#random) : value (Vector)
- [RotateEuler](#rotateeuler) : rotation (Vector)

## Properties

- [separate](#separate) : Sockets      [x (Float), y (Float), z (Float)]

## Methods

- [absolute](#absolute) : vector (Vector)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Vector), trailing (Vector), total (Vector)]
- [add](#add) : vector (Vector)
- [align_to_vector](#align_to_vector) : rotation (Vector)
- [attribute_statistic](#attribute_statistic) : Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
- [average_equal](#average_equal) : result (Boolean)
- [average_greater_equal](#average_greater_equal) : result (Boolean)
- [average_greater_than](#average_greater_than) : result (Boolean)
- [average_less_equal](#average_less_equal) : result (Boolean)
- [average_less_than](#average_less_than) : result (Boolean)
- [average_not_equal](#average_not_equal) : result (Boolean)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Vector)]
- [ceil](#ceil) : vector (Vector)
- [cos](#cos) : vector (Vector)
- [cross](#cross) : vector (Vector)
- [curves](#curves) : vector (Vector)
- [direction_equal](#direction_equal) : result (Boolean)
- [direction_greater_equal](#direction_greater_equal) : result (Boolean)
- [direction_greater_than](#direction_greater_than) : result (Boolean)
- [direction_less_equal](#direction_less_equal) : result (Boolean)
- [direction_less_than](#direction_less_than) : result (Boolean)
- [direction_not_equal](#direction_not_equal) : result (Boolean)
- [distance](#distance) : value (Float)
- [divide](#divide) : vector (Vector)
- [dot](#dot) : value (Float)
- [dot_product_equal](#dot_product_equal) : result (Boolean)
- [dot_product_greater_equal](#dot_product_greater_equal) : result (Boolean)
- [dot_product_greater_than](#dot_product_greater_than) : result (Boolean)
- [dot_product_less_equal](#dot_product_less_equal) : result (Boolean)
- [dot_product_less_than](#dot_product_less_than) : result (Boolean)
- [dot_product_not_equal](#dot_product_not_equal) : result (Boolean)
- [element_equal](#element_equal) : result (Boolean)
- [element_greater_equal](#element_greater_equal) : result (Boolean)
- [element_greater_than](#element_greater_than) : result (Boolean)
- [element_less_equal](#element_less_equal) : result (Boolean)
- [element_less_than](#element_less_than) : result (Boolean)
- [element_not_equal](#element_not_equal) : result (Boolean)
- [equal](#equal) : result (Boolean)
- [faceforward](#faceforward) : vector (Vector)
- [field_at_index](#field_at_index) : value (Vector)
- [floor](#floor) : vector (Vector)
- [fraction](#fraction) : vector (Vector)
- [greater_equal](#greater_equal) : result (Boolean)
- [greater_than](#greater_than) : result (Boolean)
- [length](#length) : value (Float)
- [length_equal](#length_equal) : result (Boolean)
- [length_greater_equal](#length_greater_equal) : result (Boolean)
- [length_greater_than](#length_greater_than) : result (Boolean)
- [length_less_equal](#length_less_equal) : result (Boolean)
- [length_less_than](#length_less_than) : result (Boolean)
- [length_not_equal](#length_not_equal) : result (Boolean)
- [less_equal](#less_equal) : result (Boolean)
- [less_than](#less_than) : result (Boolean)
- [map_range](#map_range) : vector (Vector)
- [max](#max) : vector (Vector)
- [min](#min) : vector (Vector)
- [modulo](#modulo) : vector (Vector)
- [multiply](#multiply) : vector (Vector)
- [multiply_add](#multiply_add) : vector (Vector)
- [normalize](#normalize) : vector (Vector)
- [not_equal](#not_equal) : result (Boolean)
- [project](#project) : vector (Vector)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
- [reflect](#reflect) : vector (Vector)
- [refract](#refract) : vector (Vector)
- [rotate](#rotate) : vector (Vector)
- [rotate_euler](#rotate_euler) : rotation (Vector)
- [scale](#scale) : vector (Vector)
- [sin](#sin) : vector (Vector)
- [snap](#snap) : vector (Vector)
- [subtract](#subtract) : vector (Vector)
- [switch](#switch) : output (Vector)
- [tan](#tan) : vector (Vector)
- [wrap](#wrap) : vector (Vector)

## Random

Geometry node [*Random Value*].


  Args:
    min: Vector
    max: Vector
    ID: Integer
    seed: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RandomValue`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: FunctionNodeRandomValue
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color)
    

## Combine

Geometry node [*Combine XYZ*].


  Args:
    x: Float
    y: Float
    z: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CombineXyz`
  
  
  .. blid:: ShaderNodeCombineXYZ
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CombineXyz(x=x, y=y, z=z, label=node_label, node_color=node_color)
    

## AlignToVector

Geometry node [*Align Euler to Vector*].


  Args:
    rotation: Vector
    factor: Float
    vector: Vector
    axis (str): 'X' in [X, Y, Z]
    pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AlignEulerToVector`
  
  
  .. blid:: FunctionNodeAlignEulerToVector
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
    

## RotateEuler

Geometry node [*Rotate Euler*].


  Args:
    rotation: Vector
    rotate_by: Vector
    axis: Vector
    angle: Float
    space (str): 'OBJECT' in [OBJECT, LOCAL]
    type (str): 'EULER' in [AXIS_ANGLE, EULER]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RotateEuler`
  
  
  .. blid:: FunctionNodeRotateEuler
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RotateEuler(rotation=rotation, rotate_by=rotate_by, axis=axis, angle=angle, space=space, type=type, label=node_label, node_color=node_color)
    

## separate

Geometry node [*Separate XYZ*].



  Returns:
    Sockets [x (Float), y (Float), z (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateXyz`
  
  
  .. blid:: ShaderNodeSeparateXYZ
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
    

## accumulate_field

Geometry node [*Accumulate Field*].


  Args:
    group_index: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [leading (Vector), trailing (Vector), total (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AccumulateField`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: GeometryNodeAccumulateField
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
    

## attribute_statistic

Geometry node [*Attribute Statistic*].


  Args:
    geometry: Geometry
    selection: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AttributeStatistic`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: GeometryNodeAttributeStatistic
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
    

## capture_attribute

Geometry node [*Capture Attribute*].


  Args:
    geometry: Geometry
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), attribute (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: GeometryNodeCaptureAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
    

## field_at_index

Geometry node [*Field at Index*].


  Args:
    index: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: GeometryNodeFieldAtIndex
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
    

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
    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Raycast`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: GeometryNodeRaycast
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, label=node_label, node_color=node_color)
    

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'VECTOR'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='VECTOR', label=node_label, node_color=node_color)
    

## map_range

Geometry node [*Map Range*].


  Args:
    from_min: Vector
    from_max: Vector
    to_min: Vector
    to_max: Vector
    clamp (bool): True
    interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MapRange`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: ShaderNodeMapRange
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type, label=node_label, node_color=node_color)
    

## less_than

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    angle: Float
    mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN', label=node_label, node_color=node_color)
    

## less_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    angle: Float
    mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## greater_than

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    angle: Float
    mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## greater_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    angle: Float
    mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    angle: Float
    epsilon: Float
    mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', label=node_label, node_color=node_color)
    

## not_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    angle: Float
    epsilon: Float
    mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## element_less_than

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'ELEMENT'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## length_less_than

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'LENGTH'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## average_less_than

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'AVERAGE'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## dot_product_less_than

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DOT_PRODUCT'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## direction_less_than

Geometry node [*Compare*].


  Args:
    b: Vector
    angle: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DIRECTION'
  - operation = 'LESS_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='LESS_THAN', label=node_label, node_color=node_color)
    

## element_less_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'ELEMENT'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## length_less_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'LENGTH'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## average_less_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'AVERAGE'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## dot_product_less_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DOT_PRODUCT'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## direction_less_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    angle: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DIRECTION'
  - operation = 'LESS_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='LESS_EQUAL', label=node_label, node_color=node_color)
    

## element_greater_than

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'ELEMENT'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## length_greater_than

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'LENGTH'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## average_greater_than

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'AVERAGE'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## dot_product_greater_than

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DOT_PRODUCT'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## direction_greater_than

Geometry node [*Compare*].


  Args:
    b: Vector
    angle: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DIRECTION'
  - operation = 'GREATER_THAN'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='GREATER_THAN', label=node_label, node_color=node_color)
    

## element_greater_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'ELEMENT'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## length_greater_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'LENGTH'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='LENGTH', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## average_greater_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'AVERAGE'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='VECTOR', mode='AVERAGE', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## dot_product_greater_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DOT_PRODUCT'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## direction_greater_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    angle: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DIRECTION'
  - operation = 'GREATER_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, angle=angle, data_type='VECTOR', mode='DIRECTION', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
    

## element_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'ELEMENT'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
    

## length_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'LENGTH'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='EQUAL', label=node_label, node_color=node_color)
    

## average_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'AVERAGE'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='EQUAL', label=node_label, node_color=node_color)
    

## dot_product_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DOT_PRODUCT'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='EQUAL', label=node_label, node_color=node_color)
    

## direction_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    angle: Float
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DIRECTION'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='EQUAL', label=node_label, node_color=node_color)
    

## element_not_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'ELEMENT'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## length_not_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'LENGTH'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## average_not_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'AVERAGE'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## dot_product_not_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    c: Float
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DOT_PRODUCT'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, c=c, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## direction_not_equal

Geometry node [*Compare*].


  Args:
    b: Vector
    angle: Float
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'VECTOR'
  - mode = 'DIRECTION'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## add

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'ADD'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD', label=node_label, node_color=node_color)
    

## subtract

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'SUBTRACT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color)
    

## multiply

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'MULTIPLY'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color)
    

## divide

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'DIVIDE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color)
    

## multiply_add

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    vector2: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'MULTIPLY_ADD'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
    

## cross

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'CROSS_PRODUCT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color)
    

## project

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'PROJECT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color)
    

## reflect

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'REFLECT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color)
    

## refract

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    scale: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'REFRACT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color)
    

## faceforward

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    vector2: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'FACEFORWARD'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color)
    

## dot

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'DOT_PRODUCT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color)
    

## distance

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'DISTANCE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color)
    

## length

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'LENGTH'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='LENGTH', label=node_label, node_color=node_color)
    

## scale

Geometry node [*Vector Math*].


  Args:
    scale: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'SCALE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, scale=scale, operation='SCALE', label=node_label, node_color=node_color)
    

## normalize

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'NORMALIZE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='NORMALIZE', label=node_label, node_color=node_color)
    

## absolute

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'ABSOLUTE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
    

## min

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'MINIMUM'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color)
    

## max

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'MAXIMUM'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color)
    

## floor

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'FLOOR'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='FLOOR', label=node_label, node_color=node_color)
    

## ceil

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'CEIL'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='CEIL', label=node_label, node_color=node_color)
    

## fraction

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'FRACTION'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='FRACTION', label=node_label, node_color=node_color)
    

## modulo

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'MODULO'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color)
    

## wrap

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    vector2: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'WRAP'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color)
    

## snap

Geometry node [*Vector Math*].


  Args:
    vector1: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'SNAP'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color)
    

## sin

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'SINE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='SINE', label=node_label, node_color=node_color)
    

## cos

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'COSINE'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='COSINE', label=node_label, node_color=node_color)
    

## tan

Geometry node [*Vector Math*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorMath`
  
  - operation = 'TANGENT'
    
  .. blid:: ShaderNodeVectorMath
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorMath(vector0=self, operation='TANGENT', label=node_label, node_color=node_color)
    

## curves

Geometry node [*Vector Curves*].


  Args:
    fac: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorCurves`
  
  
  .. blid:: ShaderNodeVectorCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorCurves(vector=self, fac=fac, label=node_label, node_color=node_color)
    

## align_to_vector

Geometry node [*Align Euler to Vector*].


  Args:
    factor: Float
    vector: Vector
    axis (str): 'X' in [X, Y, Z]
    pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.AlignEulerToVector`
  
  
  .. blid:: FunctionNodeAlignEulerToVector
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
    

## rotate_euler

Geometry node [*Rotate Euler*].


  Args:
    rotate_by: Vector
    axis: Vector
    angle: Float
    space (str): 'OBJECT' in [OBJECT, LOCAL]
    type (str): 'EULER' in [AXIS_ANGLE, EULER]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RotateEuler`
  
  
  .. blid:: FunctionNodeRotateEuler
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, space=space, type=type, label=node_label, node_color=node_color)
    

## rotate

Geometry node [*Vector Rotate*].


  Args:
    center: Vector
    axis: Vector
    angle: Float
    rotation: Vector
    invert (bool): False
    rotation_type (str): 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Vector
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VectorRotate`
  
  
  .. blid:: ShaderNodeVectorRotate
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, label=node_label, node_color=node_color)
    
