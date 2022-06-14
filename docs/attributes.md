# Fields

> Fields are implemented as _Data Socket_ properties

Be sure to be familiar with fields: [Blender reference documentation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html).

## Geometry property

Fields such as [Index](/docs/nodes/Index.md) or [Position](/docs/nodes/Position.md)
represents a value (Integer, Float, Vector...) associated to a domain (Point, Edge,...) of a geometry.

In a Blender tree, the geometry a field belongs to is found by following the links forwards and backwards (see [Blender Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html).

> A field is a geometry property

In **geonodes**, fields are implemented as properties of class Geometry.
In the following example, we need the [Index](/docs/nodes/Index.md) and the [Position](/docs/nodes/Position.md) of a sphere.
The corresponding nodes are created by referencing the corresponding properties `sphere.index` and `sphere.position`.

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    sphere = gn.Mesh.IcoSphere(subdivisions=2)
    
    loc = sphere.position     # Field Position
    loc.z += sphere.index/10  # Field Index
    
    sphere.set_position(position=loc)
    
    tree.output_geometry = sphere
```

The resulting tree is given below:

<img src="/docs/images/field_1.png" width="400">

## Capture attribute

When the tree is closed, the nodes fields are reviews




