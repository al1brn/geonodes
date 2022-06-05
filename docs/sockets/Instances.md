
# Class Instances

> Inherits from: ***Geometry***

## Attributes



- [instance_index](#instance_index) : Integer = capture_index(domain='INSTANCE')



## Methods



- [to_points](#to_points) : points (Points)



## Stacked methods



- [rotate](#rotate) : Instances
- [scale](#scale) : Instances
- [translate](#translate) : Instances



## Methods


### instance_index

> Node: [Index](../nodes/{self.node_name}.md)

```python
v = instances.instance_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### rotate

> Node: [RotateInstances](../nodes/{self.node_name}.md)

```python
instances.rotate(selection, rotation, pivot_point, local_space)
```


#### Arguments


##### Sockets arguments



- instances : Instances (self)
- selection : Boolean
- rotation : Vector
- pivot_point : Vector
- local_space : Boolean



#### Returns

    self

### scale

> Node: [ScaleInstances](../nodes/{self.node_name}.md)

```python
instances.scale(selection, scale, center, local_space)
```


#### Arguments


##### Sockets arguments



- instances : Instances (self)
- selection : Boolean
- scale : Vector
- center : Vector
- local_space : Boolean



#### Returns

    self

### to_points

> Node: [InstancesToPoints](../nodes/{self.node_name}.md)

```python
v = instances.to_points(selection, position, radius)
```


#### Arguments


##### Sockets arguments



- instances : Instances (self)
- selection : Boolean
- position : Vector
- radius : Float



#### Returns

    Points

### translate

> Node: [TranslateInstances](../nodes/{self.node_name}.md)

```python
instances.translate(selection, translation, local_space)
```


#### Arguments


##### Sockets arguments



- instances : Instances (self)
- selection : Boolean
- translation : Vector
- local_space : Boolean



#### Returns

    self
