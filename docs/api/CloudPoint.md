# class CloudPoint

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

- [radius](#radius-property)



## Methods

- [instance_on_points](#instance_on_points)
- [len](#len)
- [to_vertices](#to_vertices)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

#### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-CloudPoint) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## len

```python
def __len__(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-CloudPoint) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## radius <sub>*property*</sub>

```python
def radius(self):

```
> Node: [Radius](GeometryNodeInputRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputRadius.webp)

#### Returns:
- socket `radius`

<sub>Go to [top](#class-CloudPoint) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## radius <sub>*etter*</sub>

```python
def radius(self, attr_value):

```
> Node: [Set Point Radius](GeometryNodeSetPointRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

Node implemented as property setter.

#### Args:
- attr_value: radius

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPointRadius.webp)


<sub>Go to [top](#class-CloudPoint) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_vertices

```python
def to_vertices(self, points=None):

```
> Node: [Points to Vertices](GeometryNodePointsToVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

#### Args:
- points: Points

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVertices.webp)

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-CloudPoint) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

