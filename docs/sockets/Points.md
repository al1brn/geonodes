
# Class Points

> Inherits from: ***Geometry***

## Methods



- instance_on_points : instances (Instances)
- to_vertices : mesh (Mesh)
- to_volume : volume (Volume)



## Stacked methods



- set_radius : Points



## Methods


### instance_on_points

> Node: [InstanceOnPoints](../nodes/{self.node_name}.md)

```python
v = points.instance_on_points(selection, instance, pick_instance, instance_index, rotation, scale)
```


#### Arguments


##### Sockets arguments



- points : Points (self)
- selection : Boolean
- instance : Geometry
- pick_instance : Boolean
- instance_index : Integer
- rotation : Vector
- scale : Vector



#### Returns

    Instances

### set_radius

> Node: [SetPointRadius](../nodes/{self.node_name}.md)

```python
points.set_radius(selection, radius)
```


#### Arguments


##### Sockets arguments



- points : Points (self)
- selection : Boolean
- radius : Float



#### Returns

    self

### to_vertices

> Node: [PointsToVertices](../nodes/{self.node_name}.md)

```python
v = points.to_vertices(selection)
```


#### Arguments


##### Sockets arguments



- points : Points (self)
- selection : Boolean



#### Returns

    Mesh

### to_volume

> Node: [PointsToVolume](../nodes/{self.node_name}.md)

```python
v = points.to_volume(density, voxel_size, voxel_amount, radius, resolution_mode)
```


#### Arguments


##### Sockets arguments



- points : Points (self)
- density : Float
- voxel_size : Float
- voxel_amount : Float
- radius : Float



##### Parameters arguments



- resolution_mode : 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]



#### Returns

    Volume
