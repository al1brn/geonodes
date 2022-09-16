
# Data socket Points

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Points](#points) : geometry (Geometry)

## Properties

- [domain_size](#domain_size) : point_count (Integer)
- [point_count](#point_count) : point_count (Integer)

## Methods

- [instance_on_points](#instance_on_points) : instances (Instances)
- [set_radius](#set_radius) : points (Points)
- [to_vertices](#to_vertices) : mesh (Mesh)
- [to_volume](#to_volume) : volume (Volume)

## Points

Geometry node [*Points*].


  Args:
    count: Integer
    position: Vector
    radius: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Points`
  
  
  .. blid:: GeometryNodePoints
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Points(count=count, position=position, radius=radius, label=node_label, node_color=node_color)
    

## domain_size

Geometry node [*Domain Size*].



  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'POINTCLOUD'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.domain_size")
    

## point_count

Geometry node [*Domain Size*].



  Returns:
    Integer
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'POINTCLOUD'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='POINTCLOUD', label=f"{self.node_chain_label}.point_count")
    

## set_radius

Geometry node [*Set Point Radius*].


  Args:
    selection: Boolean
    radius: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Points
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetPointRadius`
  
  
  .. blid:: GeometryNodeSetPointRadius
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetPointRadius(points=self, selection=selection, radius=radius, label=node_label, node_color=node_color)
    

## instance_on_points

Geometry node [*Instance on Points*].


  Args:
    selection: Boolean
    instance: Geometry
    pick_instance: Boolean
    instance_index: Integer
    rotation: Vector
    scale: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Instances
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.InstanceOnPoints`
  
  
  .. blid:: GeometryNodeInstanceOnPoints
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
    

## to_vertices

Geometry node [*Points to Vertices*].


  Args:
    selection: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.PointsToVertices`
  
  
  .. blid:: GeometryNodePointsToVertices
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.PointsToVertices(points=self, selection=selection, label=node_label, node_color=node_color)
    

## to_volume

Geometry node [*Points to Volume*].


  Args:
    density: Float
    voxel_size: Float
    voxel_amount: Float
    radius: Float
    resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Volume
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.PointsToVolume`
  
  
  .. blid:: GeometryNodePointsToVolume
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode, label=node_label, node_color=node_color)
    
