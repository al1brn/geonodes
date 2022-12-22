# Geometry

**Geometry** is the root class for:
- [Mesh](Mesh.md)
- [Curve](Curve.md)
- [Points](Points.md)
- [Instances](Instances.md)
- [Volume](Volume.md)

## Initialization

Geometry is not initialized directly.

## Input / Output

The default input geometry is read from the current Tree with property `input_geometry` (or with its short version `ig`).

The resulting geometry to output set with the current Tree property 'output_geometry` (or with is short version `og`).

The *do nothing* default tree is the following:

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    tree.og = tree.ig
```

## Examples

### Joining geometry

Three syntaxes are possible to join geometries:
- using the global function `join_geometry`
- using the Geometry method `join` (the geometry instance is part of the joining)
- using the operator `+`

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # ----- Let's create some geometries
    
    circle = gn.Curve.Circle().set_position(offset=(0, 0, -2))
    cube   = gn.Mesh.Cube().set_position(offset=(0, 0, 2))
    volume = gn.Volume.Cube()
    
    # Global function
    
    geo = gn.join_geometry(circle, cube)
    
    # Geometry method
    
    geo.join(cube)
    
    # + operator
    
    geo = geo + volume
    
    # As a result
    
    tree.og = geo
```







