# Curve

Curve is a subclass of [Geometry](Geometry.md).

Use Curve type to access methods specific to curves.

A Mesh has two [domains](domain.md):
- `points` of type [ControlPoint](ControlPoint.md)
- `splines` of type [Spline](Spline.md)

## Initialization

A Curve can be initialized:
- by typecasting another geometry
- or by using a constructor such as `Line`, `Circle`, `Spiral`

```python
import geonodes as gn

with gn.Tree("Test") as tree:

    # Typecasting the tree input geometry
    
    curve = gn.Curve(tree.ig) # Hope it is really a curve
    
    # We create a cube
    
    circle = gn.Curve.Circle()
    circle.set_position(offset=(0, 0, 2))
    
    # We return the two meshes
    
    tree.og = curve + circle
```

## Examples

### To mesh conversion

Use `to_mesh` method to transform the curve into a [Mesh](Mesh.md).

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # Which radius do you want
    
    radius = gn.Float.Input(.1, "Radius", min_value=0.001, description="The curve radius")

    # Let's start from a spiral    
    spiral = gn.Curve.Spiral()
    
    # To mesh
    
    mesh = spiral.to_mesh(gn.Curve.Circle(radius=radius), fill_caps=True)
    mesh.faces.shade_smooth = True
    
    # Done
    tree.og = mesh
```

