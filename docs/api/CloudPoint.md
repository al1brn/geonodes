# class CloudPoint

## Properties

- [radius](#radius-property)



## Methods

- [domain_size](#domain_size)
- [instance_on_points](#instance_on_points)
- [to_vertices](#to_vertices)

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

<sub>Go to [top](#class-CloudPoint) [data structure](../structure.md)</sub>

## instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-CloudPoint) [data structure](../structure.md)</sub>

## radius <sub>*property*</sub>

```python
def radius(self):

```
Node [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html) )

### Returns:
- socket `radius`

<sub>Go to [top](#class-CloudPoint) [data structure](../structure.md)</sub>

## radius <sub>*etter*</sub>

```python
def radius(self, attr_value):

```
Node [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html) )

Node implemented as property setter.

        ###Args:
- attr_value: radius


<sub>Go to [top](#class-CloudPoint) [data structure](../structure.md)</sub>

## to_vertices

```python
def to_vertices(self, points=None):

```
Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html) )

### Args:
- points: Points

### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-CloudPoint) [data structure](../structure.md)</sub>

