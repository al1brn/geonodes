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

### UV Mapping from curve factor

In the following example, we use the curve parameter to build the UV map of a torus.
Here the UV mapping is stored as corner named attribute 'uv_map' into the geometry.
It can be accessed through **Attribute** material shader node.


```python
import geonodes as gn

with gn.Tree("Torus") as tree:
    
    segms = gn.Integer.Input(32, "Segments",     min_value=3)
    rings = gn.Integer.Input(32, "Rings",        min_value=3)
    R     = gn.Float.Input(1.,   "Major radius", min_value=0.001)
    r     = gn.Float.Input(.25,   "Minor radius", min_value=0.001)
    mat   = gn.Material.Input(None)
    
    with tree.layout("Base torus"):
    
        major = gn.Curve.Circle(resolution=rings, radius=R)
        minor = gn.Curve.Circle(resolution=segms, radius=r)
        
        u = major.points.parameter_factor
        v = minor.points.parameter_factor
    
        major.points.set_named_float("u", u)
        minor.points.set_named_float("v", v)
        
        torus = major.to_mesh(profile_curve=minor)
        
    with tree.layout("UV Mapping"):
        
        u = torus.get_named_float("u")
        v = torus.get_named_float("v")
        
        torus.corners.set_named_vector("uv_map", (u, 1 - v, 0))
        
        torus.remove_named_attribute("u")
        torus.remove_named_attribute("v")
        
        torus.faces.material = mat
    
        
    tree.og = torus
```

