
# Data socket Collection

> Inherits from dsock.Collection
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [info](#info) : geometry (Geometry)
- [switch](#switch) : output (Collection)

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Collection
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Collection
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'COLLECTION'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='COLLECTION', label=node_label, node_color=node_color)
    

## info

Geometry node [*Collection Info*].


  Args:
    separate_children: Boolean
    reset_children: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CollectionInfo`
  
  
  .. blid:: GeometryNodeCollectionInfo
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, label=node_label, node_color=node_color)
    
