# class Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

- [domain_size](#domain_size-property)

## Class methods

- [Points](#Points-classmethod)


## Methods

- [instance_on_points](#instance_on_points)
- [set_point_radius](#set_point_radius)
- [to_vertices](#to_vertices)
- [to_volume](#to_volume)
- [to_volume_amount](#to_volume_amount)
- [to_volume_size](#to_volume_size)

## Points <sub>*classmethod*</sub>

```python
def Points(cls, count=None, position=None, radius=None):

```
> Node: [Points](GeometryNodePoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)

#### Args:
- count: Integer
- position: Vector
- radius: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePoints.webp)

#### Returns:
- socket `geometry`

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

#### Returns:
- socket `instances`

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_point_radius

```python
def set_point_radius(self, selection=None, radius=None):

```
> Node: [Set Point Radius](GeometryNodeSetPointRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

#### Args:
- selection: Boolean
- radius: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPointRadius.webp)

#### Returns:
- self

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_vertices

```python
def to_vertices(self, points=None, selection=None):

```
> Node: [Points to Vertices](GeometryNodePointsToVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

#### Args:
- points: Points
- selection: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVertices.webp)

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- radius: Float
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVolume.webp)

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume_amount

```python
def to_volume_amount(self, density=None, voxel_amount=None, radius=None):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_amount: Float
- radius: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVolume.webp)

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume_size

```python
def to_volume_size(self, density=None, voxel_size=None, radius=None):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- radius: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVolume.webp)

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

