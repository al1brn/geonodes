
# Data socket Object

> Inherits from dsock.Object
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [geometry](#geometry) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [info](#info) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [location](#location) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [rotation](#rotation) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [scale](#scale) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [switch](#switch) : output (Object)

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Object
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Object
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'OBJECT'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='OBJECT', label=node_label, node_color=node_color)
    

## info

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color)
    

## location

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    location in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).location
    

## rotation

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    rotation in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).rotation
    

## scale

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    scale in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).scale
    

## geometry

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    geometry in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).geometry
    
