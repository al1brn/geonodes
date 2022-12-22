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






