
# Data socket Points

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [instance_on_points](#instance_on_points) : instances (Instances)
- [set_radius](#set_radius) : points (Points)
- [to_vertices](#to_vertices) : mesh (Mesh)
- [to_volume](#to_volume) : volume (Volume)

## set_radius

> Node: [SetPointRadius](/docs/nodes/SetPointRadius.md)
  
<sub>go to: [top](#data-socket-points) [index](/docs/index.md)
blender ref [GeometryNodeSetPointRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
node ref [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) </sub>

```python
v = points.set_radius(selection, radius)
```

### Arguments

## Sockets
- points : Points (self)
- selection : Boolean
- radius : Float

### Node creation

```python
from geondes import nodes
nodes.SetPointRadius(points=self, selection=selection, radius=radius)
```

### Returns

Points


## instance_on_points

> Node: [InstanceOnPoints](/docs/nodes/InstanceOnPoints.md)
  
<sub>go to: [top](#data-socket-points) [index](/docs/index.md)
blender ref [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
node ref [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) </sub>

```python
v = points.instance_on_points(selection, instance, pick_instance, instance_index, rotation, scale)
```

### Arguments

## Sockets
- points : Points (self)
- selection : Boolean
- instance : Geometry
- pick_instance : Boolean
- instance_index : Integer
- rotation : Vector
- scale : Vector

### Node creation

```python
from geondes import nodes
nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale)
```

### Returns

Instances


## to_vertices

> Node: [PointsToVertices](/docs/nodes/PointsToVertices.md)
  
<sub>go to: [top](#data-socket-points) [index](/docs/index.md)
blender ref [GeometryNodePointsToVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
node ref [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) </sub>

```python
v = points.to_vertices(selection)
```

### Arguments

## Sockets
- points : Points (self)
- selection : Boolean

### Node creation

```python
from geondes import nodes
nodes.PointsToVertices(points=self, selection=selection)
```

### Returns

Mesh


## to_volume

> Node: [PointsToVolume](/docs/nodes/PointsToVolume.md)
  
<sub>go to: [top](#data-socket-points) [index](/docs/index.md)
blender ref [GeometryNodePointsToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)
node ref [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) </sub>

```python
v = points.to_volume(density, voxel_size, voxel_amount, radius, resolution_mode)
```

### Arguments

## Sockets
- points : Points (self)
- density : Float
- voxel_size : Float
- voxel_amount : Float
- radius : Float## Parameters
- resolution_mode : 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

### Node creation

```python
from geondes import nodes
nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode)
```

### Returns

Volume

