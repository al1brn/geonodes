# class Instance

> [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)

## Properties

- [rotation](#rotation-property)
- [scale](#scale-property)



## Methods

- [domain_size](#domain_size)
- [rotate](#rotate)
- [set_scale](#set_scale)
- [to_points](#to_points)
- [translate](#translate)

## domain_size

```python
def __len__(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## rotate

```python
def rotate(self, rotation=None, pivot_point=None, local_space=None):

```
Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html) )

### Args:
- rotation: Vector
- pivot_point: Vector
- local_space: Boolean

### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## rotation <sub>*property*</sub>

```python
def rotation(self):

```
Node [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html) )

### Returns:
- socket `rotation`

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## scale <sub>*property*</sub>

```python
def scale(self):

```
Node [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html) )

### Returns:
- socket `scale`

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## set_scale

```python
def set_scale(self, scale=None, center=None, local_space=None):

```
Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html) )

### Args:
- scale: Vector
- center: Vector
- local_space: Boolean

### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, position=None, radius=None):

```
Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html) )

### Args:
- position: Vector
- radius: Float

### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## translate

```python
def translate(self, translation=None, local_space=None):

```
Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html) )

### Args:
- translation: Vector
- local_space: Boolean

### Returns:
- self

<sub>Go to [top](#class-Instance) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>
