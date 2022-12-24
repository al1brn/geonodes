# class Points

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

**Points** is a subclass of [Geometry](Geometry.md).

Use **Points** type to access methods specific to cloud of points.

A **Points** has only one [domain](domain.md):
- `points` of type [CloudPoint](CloudPoint.md)
> see [examples](#examples)

## Properties

- [domain_size](#domain_size)

## Class methods

- [Points](#Points)


## Methods

- [instance_on_points](#instance_on_points)
- [set_point_radius](#set_point_radius)
- [to_vertices](#to_vertices)
- [to_volume](#to_volume)
- [to_volume_amount](#to_volume_amount)
- [to_volume_size](#to_volume_size)

## Examples

### Initialization

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
