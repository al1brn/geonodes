# class Points

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

## Points <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def Points(cls, count=None, position=None, radius=None):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- count: Integer
<sub>Go to [top](#class-Points)</sub>

- position: Vector
<sub>Go to [top](#class-Points)</sub>

- radius: Float
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'geometry'<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## domain_size <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def domain_size(self):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Points)</sub>

Node implemented as property.

<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'point_count'<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## instance_on_points

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- selection: Boolean
<sub>Go to [top](#class-Points)</sub>

- instance: Geometry
<sub>Go to [top](#class-Points)</sub>

- pick_instance: Boolean
<sub>Go to [top](#class-Points)</sub>

- instance_index: Integer
<sub>Go to [top](#class-Points)</sub>

- rotation: Vector
<sub>Go to [top](#class-Points)</sub>

- scale: Vector
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'instances'<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## set_point_radius

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def set_point_radius(self, selection=None, radius=None):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- selection: Boolean
<sub>Go to [top](#class-Points)</sub>

- radius: Float
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

- node with sockets ['points']
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## to_vertices

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def to_vertices(self, points=None, selection=None):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- points: Points
<sub>Go to [top](#class-Points)</sub>

- selection: Boolean
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'mesh'<sub>Go to [top](#class-Points)</sub>

 of class Mesh
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## to_volume

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- density: Float
<sub>Go to [top](#class-Points)</sub>

- voxel_size: Float
<sub>Go to [top](#class-Points)</sub>

- voxel_amount: Float
<sub>Go to [top](#class-Points)</sub>

- radius: Float
<sub>Go to [top](#class-Points)</sub>

- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'volume'<sub>Go to [top](#class-Points)</sub>

 of class Volume
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## to_volume_amount

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def to_volume_amount(self, density=None, voxel_amount=None, radius=None):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- density: Float
<sub>Go to [top](#class-Points)</sub>

- voxel_amount: Float
<sub>Go to [top](#class-Points)</sub>

- radius: Float
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'volume'<sub>Go to [top](#class-Points)</sub>

 of class Volume
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

## to_volume_size

<sub>Go to [top](#class-Points)</sub>

```python
<sub>Go to [top](#class-Points)</sub>

def to_volume_size(self, density=None, voxel_size=None, radius=None):

<sub>Go to [top](#class-Points)</sub>

```
<sub>Go to [top](#class-Points)</sub>

Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html) )

<sub>Go to [top](#class-Points)</sub>

### Args:
<sub>Go to [top](#class-Points)</sub>

- density: Float
<sub>Go to [top](#class-Points)</sub>

- voxel_size: Float
<sub>Go to [top](#class-Points)</sub>

- radius: Float
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

### Returns:

<sub>Go to [top](#class-Points)</sub>

  socket 'volume'<sub>Go to [top](#class-Points)</sub>

 of class Volume
<sub>Go to [top](#class-Points)</sub>


<sub>Go to [top](#class-Points)</sub>

