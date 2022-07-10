
# Data socket String

> Inherits from dsock.String
  
<sub>go to [index](/docs/index.md)</sub>



## Properties

- [length](#length) : length (Integer)

## Methods

- [equal](#equal) : result (Boolean)
- [not_equal](#not_equal) : result (Boolean)
- [replace](#replace) : string (String)
- [slice](#slice) : string (String)
- [switch](#switch) : output (String)
- [to_curves](#to_curves) : Sockets      [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]

## length

Geometry node [*String Length*].



  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StringLength`
  
  
  .. blid:: FunctionNodeStringLength
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StringLength(string=self, label=f"{self.node_chain_label}.length")
    

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: String
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    String
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'STRING'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='STRING', label=node_label, node_color=node_color)
    

## equal

Geometry node [*Compare*].


  Args:
    b: String
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'STRING'
  - mode = 'ELEMENT'
  - operation = 'EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
    

## not_equal

Geometry node [*Compare*].


  Args:
    b: String
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Compare`
  
  - data_type = 'STRING'
  - mode = 'ELEMENT'
  - operation = 'NOT_EQUAL'
    
  .. blid:: FunctionNodeCompare
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
    

## replace

Geometry node [*Replace String*].


  Args:
    find: String
    replace: String
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    String
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ReplaceString`
  
  
  .. blid:: FunctionNodeReplaceString
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ReplaceString(string=self, find=find, replace=replace, label=node_label, node_color=node_color)
    

## slice

Geometry node [*Slice String*].


  Args:
    position: Integer
    length: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    String
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SliceString`
  
  
  .. blid:: FunctionNodeSliceString
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SliceString(string=self, position=position, length=length, label=node_label, node_color=node_color)
    

## to_curves

Geometry node [*String to Curves*].


  Args:
    size: Float
    character_spacing: Float
    word_spacing: Float
    line_spacing: Float
    text_box_width: Float
    text_box_height: Float
    align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
    align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
    overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
    pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StringToCurves`
  
  
  .. blid:: GeometryNodeStringToCurves
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode, label=node_label, node_color=node_color)
    
