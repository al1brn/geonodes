# class Instance

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

- [count](#count-property)
- [rotation](#rotation-property)
- [scale](#scale-property)



## Methods

- [delete](#delete)
- [duplicate](#duplicate)
- [rotate](#rotate)
- [separate](#separate)
- [set_scale](#set_scale)
- [to_points](#to_points)
- [translate](#translate)

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `instance_count`

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete

```python
def delete(self, mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## duplicate

```python
def duplicate(self, amount=None):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rotate

```python
def rotate(self, rotation=None, pivot_point=None, local_space=None):

```
> Node: [Rotate Instances](GeometryNodeRotateInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)

#### Args:
- rotation: Vector
- pivot_point: Vector
- local_space: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rotation <sub>*property*</sub>

```python
def rotation(self):

```
> Node: [Instance Rotation](GeometryNodeInputInstanceRotation.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)

#### Returns:
- socket `rotation`

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale <sub>*property*</sub>

```python
def scale(self):

```
> Node: [Instance Scale](GeometryNodeInputInstanceScale.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)

#### Returns:
- socket `scale`

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## separate

```python
def separate(self, geometry=None):

```
> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_scale

```python
def set_scale(self, scale=None, center=None, local_space=None):

```
> Node: [Scale Instances](GeometryNodeScaleInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)

#### Args:
- scale: Vector
- center: Vector
- local_space: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, position=None, radius=None):

```
> Node: [Instances to Points](GeometryNodeInstancesToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)

#### Args:
- position: Vector
- radius: Float

#### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## translate

```python
def translate(self, translation=None, local_space=None):

```
> Node: [Translate Instances](GeometryNodeTranslateInstances.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)

#### Args:
- translation: Vector
- local_space: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

