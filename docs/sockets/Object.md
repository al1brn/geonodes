
# Data socket Object

> Inherits from dsock.Object
  
<sub>go to [index](/docs/index.md)</sub>



## Properties

- [geometry](#geometry) : geometry (Geometry) = info.geometry
- [info](#info) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [location](#location) : location (Vector) = info.location
- [rotation](#rotation) : rotation (Vector) = info.rotation
- [scale](#scale) : scale (Vector) = info.scale

## Methods

- [switch](#switch) : output (Object)

## info

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    
  Returns:
    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
    

## location

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    
  Returns:
    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.location")
    

## rotation

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    
  Returns:
    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.rotation")
    

## scale

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    
  Returns:
    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.scale")
    

## geometry

Geometry node [*Object Info*].


  Args:
    as_instance: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    
  Returns:
    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ObjectInfo`
  
  
  .. blid:: GeometryNodeObjectInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.geometry")
    

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
    
