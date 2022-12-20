# class CloudPoint

## Properties

- [radius](#radius-property)



## Methods

- [domain_size](#domain_size)
- [instance_on_points](#instance_on_points)
- [to_vertices](#to_vertices)

## domain_size

<sub>Go to [top](#class-CloudPoint)</sub>```python
<sub>Go to [top](#class-CloudPoint)</sub>def __len__(self):

<sub>Go to [top](#class-CloudPoint)</sub>```
<sub>Go to [top](#class-CloudPoint)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-CloudPoint)</sub>### Args:
<sub>Go to [top](#class-CloudPoint)</sub>- geometry: Geometry
<sub>Go to [top](#class-CloudPoint)</sub>- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>### Returns:

<sub>Go to [top](#class-CloudPoint)</sub>- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>## instance_on_points

<sub>Go to [top](#class-CloudPoint)</sub>```python
<sub>Go to [top](#class-CloudPoint)</sub>def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-CloudPoint)</sub>```
<sub>Go to [top](#class-CloudPoint)</sub>Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-CloudPoint)</sub>### Args:
<sub>Go to [top](#class-CloudPoint)</sub>- instance: Geometry
<sub>Go to [top](#class-CloudPoint)</sub>- pick_instance: Boolean
<sub>Go to [top](#class-CloudPoint)</sub>- instance_index: Integer
<sub>Go to [top](#class-CloudPoint)</sub>- rotation: Vector
<sub>Go to [top](#class-CloudPoint)</sub>- scale: Vector
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>### Returns:

<sub>Go to [top](#class-CloudPoint)</sub>  socket 'instances'<sub>Go to [top](#class-CloudPoint)</sub> of class Instances
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>## radius <span style="color:blue">*property*</span>

<sub>Go to [top](#class-CloudPoint)</sub>```python
<sub>Go to [top](#class-CloudPoint)</sub>def radius(self):

<sub>Go to [top](#class-CloudPoint)</sub>```
<sub>Go to [top](#class-CloudPoint)</sub>Node [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html) )

<sub>Go to [top](#class-CloudPoint)</sub>### Returns:

<sub>Go to [top](#class-CloudPoint)</sub>  socket 'radius'<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>## radius <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-CloudPoint)</sub>```python
<sub>Go to [top](#class-CloudPoint)</sub>def radius(self, attr_value):

<sub>Go to [top](#class-CloudPoint)</sub>```
<sub>Go to [top](#class-CloudPoint)</sub>Node [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html) )

<sub>Go to [top](#class-CloudPoint)</sub>Node implemented as property setter.

<sub>Go to [top](#class-CloudPoint)</sub>        ###Args:<sub>Go to [top](#class-CloudPoint)</sub>- attr_value: radius
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>## to_vertices

<sub>Go to [top](#class-CloudPoint)</sub>```python
<sub>Go to [top](#class-CloudPoint)</sub>def to_vertices(self, points=None):

<sub>Go to [top](#class-CloudPoint)</sub>```
<sub>Go to [top](#class-CloudPoint)</sub>Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html) )

<sub>Go to [top](#class-CloudPoint)</sub>### Args:
<sub>Go to [top](#class-CloudPoint)</sub>- points: Points
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>### Returns:

<sub>Go to [top](#class-CloudPoint)</sub>  socket 'mesh'<sub>Go to [top](#class-CloudPoint)</sub> of class Mesh
<sub>Go to [top](#class-CloudPoint)</sub>
<sub>Go to [top](#class-CloudPoint)</sub>