# class Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- points: Points
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

#### Returns:
- socket `instances`

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

#### Returns:
- socket `instance_count`

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## on_points

```python
def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- points: Points
- selection: Boolean
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

#### Returns:
- socket `instances`

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## realize

```python
def realize(self, geometry=None, legacy_behavior=False):

```
> Node: [Realize Instances](GeometryNodeRealizeInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)

#### Args:
- geometry: Geometry
- legacy_behavior (bool): False

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRealizeInstances.webp)

#### Returns:
- socket `geometry`

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rotate

```python
def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):

```
> Node: [Rotate Instances](GeometryNodeRotateInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)

#### Args:
- selection: Boolean
- rotation: Vector
- pivot_point: Vector
- local_space: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRotateInstances.webp)

#### Returns:
- self

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rotation <sub>*property*</sub>

```python
def rotation(self):

```
> Node: [Instance Rotation](GeometryNodeInputInstanceRotation.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputInstanceRotation.webp)

#### Returns:
- socket `rotation`

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale <sub>*property*</sub>

```python
def scale(self):

```
> Node: [Instance Scale](GeometryNodeInputInstanceScale.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputInstanceScale.webp)

#### Returns:
- socket `scale`

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_scale

```python
def set_scale(self, selection=None, scale=None, center=None, local_space=None):

```
> Node: [Scale Instances](GeometryNodeScaleInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)

#### Args:
- selection: Boolean
- scale: Vector
- center: Vector
- local_space: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleInstances.webp)

#### Returns:
- self

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, selection=None, position=None, radius=None):

```
> Node: [Instances to Points](GeometryNodeInstancesToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)

#### Args:
- selection: Boolean
- position: Vector
- radius: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstancesToPoints.webp)

#### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## translate

```python
def translate(self, selection=None, translation=None, local_space=None):

```
> Node: [Translate Instances](GeometryNodeTranslateInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)

#### Args:
- selection: Boolean
- translation: Vector
- local_space: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTranslateInstances.webp)

#### Returns:
- self

<sub>Go to [top](#class-Instances) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

