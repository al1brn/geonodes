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

## InstanceOnPoints <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def InstanceOnPoints(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- points: Points
<sub>Go to [top](#class-Instances)</sub>- selection: Boolean
<sub>Go to [top](#class-Instances)</sub>- instance: Geometry
<sub>Go to [top](#class-Instances)</sub>- pick_instance: Boolean
<sub>Go to [top](#class-Instances)</sub>- instance_index: Integer
<sub>Go to [top](#class-Instances)</sub>- rotation: Vector
<sub>Go to [top](#class-Instances)</sub>- scale: Vector
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'instances'<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## domain_size <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def domain_size(self):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Instances)</sub>Node implemented as property.

<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'instance_count'<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## on_points

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- points: Points
<sub>Go to [top](#class-Instances)</sub>- selection: Boolean
<sub>Go to [top](#class-Instances)</sub>- pick_instance: Boolean
<sub>Go to [top](#class-Instances)</sub>- instance_index: Integer
<sub>Go to [top](#class-Instances)</sub>- rotation: Vector
<sub>Go to [top](#class-Instances)</sub>- scale: Vector
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'instances'<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## realize

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def realize(self, geometry=None, legacy_behavior=False):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- geometry: Geometry
<sub>Go to [top](#class-Instances)</sub>- legacy_behavior (bool): False
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'geometry'<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## rotate

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- selection: Boolean
<sub>Go to [top](#class-Instances)</sub>- rotation: Vector
<sub>Go to [top](#class-Instances)</sub>- pivot_point: Vector
<sub>Go to [top](#class-Instances)</sub>- local_space: Boolean
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>- node with sockets ['instances']
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## rotation <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def rotation(self):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html) )

<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'rotation'<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## scale <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def scale(self):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html) )

<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'scale'<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## set_scale

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def set_scale(self, selection=None, scale=None, center=None, local_space=None):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- selection: Boolean
<sub>Go to [top](#class-Instances)</sub>- scale: Vector
<sub>Go to [top](#class-Instances)</sub>- center: Vector
<sub>Go to [top](#class-Instances)</sub>- local_space: Boolean
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>- node with sockets ['instances']
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## to_points

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def to_points(self, selection=None, position=None, radius=None):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- selection: Boolean
<sub>Go to [top](#class-Instances)</sub>- position: Vector
<sub>Go to [top](#class-Instances)</sub>- radius: Float
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>  socket 'points'<sub>Go to [top](#class-Instances)</sub> of class Points
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>## translate

<sub>Go to [top](#class-Instances)</sub>```python
<sub>Go to [top](#class-Instances)</sub>def translate(self, selection=None, translation=None, local_space=None):

<sub>Go to [top](#class-Instances)</sub>```
<sub>Go to [top](#class-Instances)</sub>Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html) )

<sub>Go to [top](#class-Instances)</sub>### Args:
<sub>Go to [top](#class-Instances)</sub>- selection: Boolean
<sub>Go to [top](#class-Instances)</sub>- translation: Vector
<sub>Go to [top](#class-Instances)</sub>- local_space: Boolean
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>### Returns:

<sub>Go to [top](#class-Instances)</sub>- node with sockets ['instances']
<sub>Go to [top](#class-Instances)</sub>
<sub>Go to [top](#class-Instances)</sub>