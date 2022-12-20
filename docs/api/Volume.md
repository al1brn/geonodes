# class Volume


## Class methods

- [Cube](#Cube-classmethod)


## Methods

- [distribute_points](#distribute_points)
- [distribute_points_grid](#distribute_points_grid)
- [distribute_points_random](#distribute_points_random)
- [to_mesh](#to_mesh)

## Cube <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Volume)</sub>

```python
<sub>Go to [top](#class-Volume)</sub>

def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):

<sub>Go to [top](#class-Volume)</sub>

```
<sub>Go to [top](#class-Volume)</sub>

Node [Volume Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html) )

<sub>Go to [top](#class-Volume)</sub>

### Args:
<sub>Go to [top](#class-Volume)</sub>

- density: Float
<sub>Go to [top](#class-Volume)</sub>

- background: Float
<sub>Go to [top](#class-Volume)</sub>

- min: Vector
<sub>Go to [top](#class-Volume)</sub>

- max: Vector
<sub>Go to [top](#class-Volume)</sub>

- resolution_x: Integer
<sub>Go to [top](#class-Volume)</sub>

- resolution_y: Integer
<sub>Go to [top](#class-Volume)</sub>

- resolution_z: Integer
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

### Returns:

<sub>Go to [top](#class-Volume)</sub>

  socket 'volume'<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

## distribute_points

<sub>Go to [top](#class-Volume)</sub>

```python
<sub>Go to [top](#class-Volume)</sub>

def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):

<sub>Go to [top](#class-Volume)</sub>

```
<sub>Go to [top](#class-Volume)</sub>

Node [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html) )

<sub>Go to [top](#class-Volume)</sub>

### Args:
<sub>Go to [top](#class-Volume)</sub>

- density: Float
<sub>Go to [top](#class-Volume)</sub>

- seed: Integer
<sub>Go to [top](#class-Volume)</sub>

- spacing: Vector
<sub>Go to [top](#class-Volume)</sub>

- threshold: Float
<sub>Go to [top](#class-Volume)</sub>

- mode (str): 'DENSITY_RANDOM' in [DENSITY_RANDOM, DENSITY_GRID]
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

### Returns:

<sub>Go to [top](#class-Volume)</sub>

  socket 'points'<sub>Go to [top](#class-Volume)</sub>

 of class Points
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

## distribute_points_grid

<sub>Go to [top](#class-Volume)</sub>

```python
<sub>Go to [top](#class-Volume)</sub>

def distribute_points_grid(self, spacing=None, threshold=None):

<sub>Go to [top](#class-Volume)</sub>

```
<sub>Go to [top](#class-Volume)</sub>

Node [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html) )

<sub>Go to [top](#class-Volume)</sub>

### Args:
<sub>Go to [top](#class-Volume)</sub>

- spacing: Vector
<sub>Go to [top](#class-Volume)</sub>

- threshold: Float
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

### Returns:

<sub>Go to [top](#class-Volume)</sub>

  socket 'points'<sub>Go to [top](#class-Volume)</sub>

 of class Points
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

## distribute_points_random

<sub>Go to [top](#class-Volume)</sub>

```python
<sub>Go to [top](#class-Volume)</sub>

def distribute_points_random(self, density=None, seed=None):

<sub>Go to [top](#class-Volume)</sub>

```
<sub>Go to [top](#class-Volume)</sub>

Node [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html) )

<sub>Go to [top](#class-Volume)</sub>

### Args:
<sub>Go to [top](#class-Volume)</sub>

- density: Float
<sub>Go to [top](#class-Volume)</sub>

- seed: Integer
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

### Returns:

<sub>Go to [top](#class-Volume)</sub>

  socket 'points'<sub>Go to [top](#class-Volume)</sub>

 of class Points
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

## to_mesh

<sub>Go to [top](#class-Volume)</sub>

```python
<sub>Go to [top](#class-Volume)</sub>

def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):

<sub>Go to [top](#class-Volume)</sub>

```
<sub>Go to [top](#class-Volume)</sub>

Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html) )

<sub>Go to [top](#class-Volume)</sub>

### Args:
<sub>Go to [top](#class-Volume)</sub>

- voxel_size: Float
<sub>Go to [top](#class-Volume)</sub>

- voxel_amount: Float
<sub>Go to [top](#class-Volume)</sub>

- threshold: Float
<sub>Go to [top](#class-Volume)</sub>

- adaptivity: Float
<sub>Go to [top](#class-Volume)</sub>

- resolution_mode (str): 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

### Returns:

<sub>Go to [top](#class-Volume)</sub>

  socket 'mesh'<sub>Go to [top](#class-Volume)</sub>

 of class Mesh
<sub>Go to [top](#class-Volume)</sub>


<sub>Go to [top](#class-Volume)</sub>

