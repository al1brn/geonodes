
# Data socket Instances

> Inherits from gn.Geometry, Domain
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [duplicate_instances](#duplicate_instances) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [realize](#realize) : geometry (Geometry)
- [rotate](#rotate) : instances (Instances)
- [scale](#scale) : instances (Instances)
- [to_points](#to_points) : points (Points)
- [translate](#translate) : instances (Instances)

## rotate

> Node: [RotateInstances](/docs/nodes/RotateInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeRotateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
node ref [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) </sub>
                          
```python
v = instances.rotate(selection, rotation, pivot_point, local_space, node_label = None, node_color = None)
```

### Arguments

## Sockets
- instances : Instances (self)
- selection : Boolean
- rotation : Vector
- pivot_point : Vector
- local_space : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space, label=node_label, node_color=node_color)
```

### Returns

Instances


## scale

> Node: [ScaleInstances](/docs/nodes/ScaleInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeScaleInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
node ref [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) </sub>
                          
```python
v = instances.scale(selection, scale, center, local_space, node_label = None, node_color = None)
```

### Arguments

## Sockets
- instances : Instances (self)
- selection : Boolean
- scale : Vector
- center : Vector
- local_space : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space, label=node_label, node_color=node_color)
```

### Returns

Instances


## translate

> Node: [TranslateInstances](/docs/nodes/TranslateInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeTranslateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
node ref [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) </sub>
                          
```python
v = instances.translate(selection, translation, local_space, node_label = None, node_color = None)
```

### Arguments

## Sockets
- instances : Instances (self)
- selection : Boolean
- translation : Vector
- local_space : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space, label=node_label, node_color=node_color)
```

### Returns

Instances


## realize

> Node: [RealizeInstances](/docs/nodes/RealizeInstances.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeRealizeInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
node ref [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) </sub>
                          
```python
v = instances.realize(legacy_behavior, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)## Parameters
- legacy_behavior : False
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior, label=node_label, node_color=node_color)
```

### Returns

Geometry


## to_points

> Node: [InstancesToPoints](/docs/nodes/InstancesToPoints.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeInstancesToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
node ref [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) </sub>
                          
```python
v = instances.to_points(selection, position, radius, node_label = None, node_color = None)
```

### Arguments

## Sockets
- instances : Instances (self)
- selection : Boolean
- position : Vector
- radius : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius, label=node_label, node_color=node_color)
```

### Returns

Points


## duplicate_instances

> Node: [DuplicateElements](/docs/nodes/DuplicateElements.md)
  
<sub>go to: [top](#data-socket-instances) [index](/docs/index.md)
blender ref [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
node ref [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) </sub>
                          
```python
v = instances.duplicate_instances(selection, amount, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- amount : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- domain : 'INSTANCE'

### Node creation

```python
from geondes import nodes
nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='INSTANCE', label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), duplicate_index (Integer)]

