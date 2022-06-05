
# Class Instances

> Inherits from: ***Geometry***

## Attributes



- [**instance_index**](#instance_index) : [Index](../nodes/Index.md) Integer = capture_index(domain='INSTANCE')



## Methods



- [**to_points**](#to_points) : [InstancesToPoints](../nodes/InstancesToPoints.md) points (Points)



## Stacked methods



- [**rotate**](#rotate) : [RotateInstances](../nodes/RotateInstances.md) Instances
- [**scale**](#scale) : [ScaleInstances](../nodes/ScaleInstances.md) Instances
- [**translate**](#translate) : [TranslateInstances](../nodes/TranslateInstances.md) Instances



## Methods reference


### instance_index

> Node: [Index](../nodes/{self.node_name}.md)

```python
v = instances.instance_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.Index()
```


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



#### Node creation


```python
node = nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space)
```


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



#### Node creation


```python
node = nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space)
```


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



#### Node creation


```python
node = nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius)
```


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



#### Node creation


```python
node = nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space)
```


#### Returns

    self
