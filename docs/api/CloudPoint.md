# class CloudPoint

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


**Cloud point** is the unique [Domain](Domain.md) of [Points](Points.md) (cloud points). It is implemented as property `points`.
## Properties

- [count](#count-property)
- [radius](#radius-property)



## Methods

- [delete](#delete)
- [duplicate](#duplicate)
- [instance_on_points](#instance_on_points)
- [proximity](#proximity)
- [to_vertices](#to_vertices)

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete

```python
def delete(self, mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## duplicate

```python
def duplicate(self, amount=None):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## proximity

```python
def proximity(self, target=None, source_position=None):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## radius <sub>*property*</sub>

```python
def radius(self):

```
> Node: [Radius](GeometryNodeInputRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## radius <sub>*etter*</sub>

```python
def radius(self, attr_value):

```
> Node: [Set Point Radius](GeometryNodeSetPointRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

Node implemented as property setter.

#### Args:
- attr_value: radius


<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_vertices

```python
def to_vertices(self, points=None):

```
> Node: [Points to Vertices](GeometryNodePointsToVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

#### Args:
- points: Points

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-CloudPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

