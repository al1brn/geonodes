# class Points

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

# Points

**Points** is a subclass of [Geometry](Geometry.md).

Use **Points** type to access methods specific to cloud of points.

A **Points** has only one [domain](domain.md):
- `points` of type [CloudPoint](CloudPoint.md)

## Initialization

A **Points** can be initialized:
- by typecasting another geometry
- or by using the constructor `Points`

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    points = gn.Points.Points(count=100)
    points.points.position = gn.random_vector(min=(-1, -1, -1), max=(1, 1, 1))
    
    tree.og = points
```

## Examples

### Points distribution

Points can be distrubuted on a [Mesh](mesh.md) using the method `distribute_points_random` or `distribute_points_random` of
the domain `faces`.

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # ----- User parameter
    
    density = gn.Float.Input(10, "Density")
    
    # ----- Let's go
    
    # The mesh to distribute points on
    mesh = gn.Mesh.IcoSphere(subdivisions=1)
    
    # Let's distribute the points
    points, _, _ = mesh.faces.distribute_points_random(density=density)
    
    tree.og = points
```

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

#### Returns:
- socket `geometry`

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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

#### Returns:
- socket `instances`

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_point_radius

```python
def set_point_radius(self, selection=None, radius=None):

```
> Node: [Set Point Radius](GeometryNodeSetPointRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

#### Args:
- selection: Boolean
- radius: Float

#### Returns:
- self

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_vertices

```python
def to_vertices(self, points=None, selection=None):

```
> Node: [Points to Vertices](GeometryNodePointsToVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

#### Args:
- points: Points
- selection: Boolean

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume_amount

```python
def to_volume_amount(self, density=None, voxel_amount=None, radius=None):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_amount: Float
- radius: Float

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume_size

```python
def to_volume_size(self, density=None, voxel_size=None, radius=None):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- radius: Float

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

