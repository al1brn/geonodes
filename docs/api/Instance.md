# class Instance

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

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def __len__(self):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Instance)</sub>

### Args:
<sub>Go to [top](#class-Instance)</sub>

- geometry: Geometry
<sub>Go to [top](#class-Instance)</sub>

- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

## rotate

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def rotate(self, rotation=None, pivot_point=None, local_space=None):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html) )

<sub>Go to [top](#class-Instance)</sub>

### Args:
<sub>Go to [top](#class-Instance)</sub>

- rotation: Vector
<sub>Go to [top](#class-Instance)</sub>

- pivot_point: Vector
<sub>Go to [top](#class-Instance)</sub>

- local_space: Boolean
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

- node with sockets ['instances']
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

## rotation <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def rotation(self):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html) )

<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

  socket 'rotation'<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

## scale <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def scale(self):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html) )

<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

  socket 'scale'<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

## set_scale

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def set_scale(self, scale=None, center=None, local_space=None):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html) )

<sub>Go to [top](#class-Instance)</sub>

### Args:
<sub>Go to [top](#class-Instance)</sub>

- scale: Vector
<sub>Go to [top](#class-Instance)</sub>

- center: Vector
<sub>Go to [top](#class-Instance)</sub>

- local_space: Boolean
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

- node with sockets ['instances']
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

## to_points

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def to_points(self, position=None, radius=None):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html) )

<sub>Go to [top](#class-Instance)</sub>

### Args:
<sub>Go to [top](#class-Instance)</sub>

- position: Vector
<sub>Go to [top](#class-Instance)</sub>

- radius: Float
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

  socket 'points'<sub>Go to [top](#class-Instance)</sub>

 of class Points
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

## translate

<sub>Go to [top](#class-Instance)</sub>

```python
<sub>Go to [top](#class-Instance)</sub>

def translate(self, translation=None, local_space=None):

<sub>Go to [top](#class-Instance)</sub>

```
<sub>Go to [top](#class-Instance)</sub>

Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html) )

<sub>Go to [top](#class-Instance)</sub>

### Args:
<sub>Go to [top](#class-Instance)</sub>

- translation: Vector
<sub>Go to [top](#class-Instance)</sub>

- local_space: Boolean
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

### Returns:

<sub>Go to [top](#class-Instance)</sub>

- node with sockets ['instances']
<sub>Go to [top](#class-Instance)</sub>


<sub>Go to [top](#class-Instance)</sub>

