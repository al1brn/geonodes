
# Data socket Instances

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Attributes

- [instance_index](#instance_index) : [Index](docs/nodes/Index.md), Integer = capture_index(domain='INSTANCE')

## Methods

- [rotate](#rotate) : [RotateInstances](docs/nodes/RotateInstances.md), instances (Instances)
- [scale](#scale) : [ScaleInstances](docs/nodes/ScaleInstances.md), instances (Instances)
- [to_points](#to_points) : [InstancesToPoints](docs/nodes/InstancesToPoints.md), points (Points)
- [translate](#translate) : [TranslateInstances](docs/nodes/TranslateInstances.md), instances (Instances)

## instance_index

> Node: [Index](docs/nodes/Index.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
node ref [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/index.html) </sub>

```python
v = instances.instance_index(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
nodes.Index()
```

### Returns

Integer


## rotate

> Node: [RotateInstances](docs/nodes/RotateInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeRotateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
node ref [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/rotate_instances.html) </sub>

```python
v = instances.rotate(selection, rotation, pivot_point, local_space)
```

### Arguments


#### Sockets

- instances : Instances (self)
- selection : Boolean
- rotation : Vector
- pivot_point : Vector
- local_space : Boolean

### Node creation

```python
nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space)
```

### Returns

Instances


## scale

> Node: [ScaleInstances](docs/nodes/ScaleInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeScaleInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
node ref [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/scale_instances.html) </sub>

```python
v = instances.scale(selection, scale, center, local_space)
```

### Arguments


#### Sockets

- instances : Instances (self)
- selection : Boolean
- scale : Vector
- center : Vector
- local_space : Boolean

### Node creation

```python
nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space)
```

### Returns

Instances


## translate

> Node: [TranslateInstances](docs/nodes/TranslateInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeTranslateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
node ref [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/translate_instances.html) </sub>

```python
v = instances.translate(selection, translation, local_space)
```

### Arguments


#### Sockets

- instances : Instances (self)
- selection : Boolean
- translation : Vector
- local_space : Boolean

### Node creation

```python
nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space)
```

### Returns

Instances


## to_points

> Node: [InstancesToPoints](docs/nodes/InstancesToPoints.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeInstancesToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
node ref [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/instances_to_points.html) </sub>

```python
v = instances.to_points(selection, position, radius)
```

### Arguments


#### Sockets

- instances : Instances (self)
- selection : Boolean
- position : Vector
- radius : Float

### Node creation

```python
nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius)
```

### Returns

Points

