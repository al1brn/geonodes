
# Class Points

> Inherits from: ***Geometry***

## Methods



- [**instance_on_points**](#instance_on_points) : [InstanceOnPoints](../nodes/InstanceOnPoints.md) instances (Instances)
- [**to_vertices**](#to_vertices) : [PointsToVertices](../nodes/PointsToVertices.md) mesh (Mesh)
- [**to_volume**](#to_volume) : [PointsToVolume](../nodes/PointsToVolume.md) volume (Volume)



## Stacked methods



- [**set_radius**](#set_radius) : [SetPointRadius](../nodes/SetPointRadius.md) Points



## Methods reference


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



#### Node creation


```python
node = nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale)
```


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



#### Node creation


```python
node = nodes.SetPointRadius(points=self, selection=selection, radius=radius)
```


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



#### Node creation


```python
node = nodes.PointsToVertices(points=self, selection=selection)
```


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



#### Node creation


```python
node = nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode)
```


#### Returns

    Volume
