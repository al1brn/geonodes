
# Data socket Color

> Inherits from dsock.Color
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Combine](#combine) : color (Color)
- [CombineHSL](#combinehsl) : color (Color)
- [CombineHSV](#combinehsv) : color (Color)
- [CombineRGB](#combinergb) : color (Color)

## Methods

- [brighter](#brighter) : result (Boolean)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Color)]
- [curves](#curves) : color (Color)
- [darker](#darker) : result (Boolean)
- [equal](#equal) : result (Boolean)
- [field_at_index](#field_at_index) : value (Color)
- [not_equal](#not_equal) : result (Boolean)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
- [separate_color](#separate_color) : Sockets      [red (Float), green (Float), blue (Float), alpha (Float)]
- [switch](#switch) : output (Color)

## Combine

Geometry node [*Combine Color*].


  Args:
    red: Float
    green: Float
    blue: Float
    alpha: Float
    mode (str): 'RGB' in [RGB, HSV, HSL]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CombineColor`
  
  
  .. blid:: FunctionNodeCombineColor
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode=mode, label=node_label, node_color=node_color)
    

## CombineRGB

Geometry node [*Combine Color*].


  Args:
    red: Float
    green: Float
    blue: Float
    alpha: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CombineColor`
  
  - mode = 'RGB'
    
  .. blid:: FunctionNodeCombineColor
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB', label=node_label, node_color=node_color)
    

## CombineHSV

Geometry node [*Combine Color*].


  Args:
    red: Float
    green: Float
    blue: Float
    alpha: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CombineColor`
  
  - mode = 'HSV'
    
  .. blid:: FunctionNodeCombineColor
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV', label=node_label, node_color=node_color)
    

## CombineHSL

Geometry node [*Combine Color*].


  Args:
    red: Float
    green: Float
    blue: Float
    alpha: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CombineColor`
  
  - mode = 'HSL'
    
  .. blid:: FunctionNodeCombineColor
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSL', label=node_label, node_color=node_color)
    

## capture_attribute

Geometry node [*Capture Attribute*].


  Args:
    geometry: Geometry
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), attribute (Color)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
  
  - data_type = 'FLOAT_COLOR'
    
  .. blid:: GeometryNodeCaptureAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
    

## field_at_index

Geometry node [*Field at Index*].


  Args:
    index: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
  
  - data_type = 'FLOAT_COLOR'
    
  .. blid:: GeometryNodeFieldAtIndex
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
    

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
    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Raycast`
  
  - data_type = 'FLOAT_COLOR'
    
  .. blid:: GeometryNodeRaycast
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping, label=node_label, node_color=node_color)
    

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Color
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'RGBA'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='RGBA', label=node_label, node_color=node_color)
    

## equal

Geometry node [*Compare*].


  Args:
    b: Color
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'RGBA'
  - mode = 'ELEMENT'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
    

## not_equal

Geometry node [*Compare*].


  Args:
    b: Color
    epsilon: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'RGBA'
  - mode = 'ELEMENT'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## brighter

Geometry node [*Compare*].


  Args:
    b: Color
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'RGBA'
  - mode = 'ELEMENT'
  - operation = 'BRIGHTER'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER', label=node_label, node_color=node_color)
    

## darker

Geometry node [*Compare*].


  Args:
    b: Color
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'RGBA'
  - mode = 'ELEMENT'
  - operation = 'DARKER'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER', label=node_label, node_color=node_color)
    

## separate_color

Geometry node [*Separate Color*].


  Args:
    mode (str): 'RGB' in [RGB, HSV, HSL]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [red (Float), green (Float), blue (Float), alpha (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateColor`
  
  
  .. blid:: FunctionNodeSeparateColor
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateColor(color=self, mode=mode, label=node_label, node_color=node_color)
    

## curves

Geometry node [*RGB Curves*].


  Args:
    fac: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Color
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RgbCurves`
  
  
  .. blid:: ShaderNodeRGBCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RgbCurves(color=self, fac=fac, label=node_label, node_color=node_color)
    
