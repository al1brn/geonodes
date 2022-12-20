# class Instances

## Properties

- [domain_size](#domain_size-property)
- [rotation](#rotation-property)
- [scale](#scale-property)

## Class methods

- [InstanceOnPoints](#InstanceOnPoints-classmethod)


## Methods

- [on_points](#on_points)
- [realize](#realize)
- [rotate](#rotate)
- [set_scale](#set_scale)
- [to_points](#to_points)
- [translate](#translate)

## InstanceOnPoints <sub>*classmethod*</sub>

```python
def InstanceOnPoints(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

### Args:
- points: Points
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:
- socket `instances`

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- socket `instance_count`

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## on_points

```python
def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

### Args:
- points: Points
- selection: Boolean
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:
- socket `instances`

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## realize

```python
def realize(self, geometry=None, legacy_behavior=False):

```
Node [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html) )

### Args:
- geometry: Geometry
- legacy_behavior (bool): False

### Returns:
- socket `geometry`

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## rotate

```python
def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):

```
Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html) )

### Args:
- selection: Boolean
- rotation: Vector
- pivot_point: Vector
- local_space: Boolean

### Returns:
- self

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## rotation <sub>*property*</sub>

```python
def rotation(self):

```
Node [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html) )

### Returns:
- socket `rotation`

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## scale <sub>*property*</sub>

```python
def scale(self):

```
Node [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html) )

### Returns:
- socket `scale`

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## set_scale

```python
def set_scale(self, selection=None, scale=None, center=None, local_space=None):

```
Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html) )

### Args:
- selection: Boolean
- scale: Vector
- center: Vector
- local_space: Boolean

### Returns:
- self

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## to_points

```python
def to_points(self, selection=None, position=None, radius=None):

```
Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html) )

### Args:
- selection: Boolean
- position: Vector
- radius: Float

### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

## translate

```python
def translate(self, selection=None, translation=None, local_space=None):

```
Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html) )

### Args:
- selection: Boolean
- translation: Vector
- local_space: Boolean

### Returns:
- self

<sub>Go to [top](#class-Instances)</sub> [data structure](../structure.md)

