# Fields

> Fields are implemented as _Data Socket_ properties

Be sure to be familiar with fields: [Blender reference documentation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html).

## Geometry property

Fields such as [Index](/docs/nodes/Index.md) or [Position](/docs/nodes/Position.md)
represents a value (Integer, Float, Vector...) associated to a domain (Point, Edge,...) of a geometry.

In a Blender tree, the geometry a field belongs to is found by following the links forwards and backwards (see [Blender Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html).

> A field is a geometry property

In **geonodes**, fields are implemented as properties of class Geometry.
In the following example (extracted from
[Blender documentation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html#field-context)),
we need the [Index](/docs/nodes/Index.md) and the [Position](/docs/nodes/Position.md) of the input geometry.

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    geo = tree.input_geometry
    
    v = geo.position
    v = v.scale(scale=geo.index)
    
    geo.set_position(offset=v, node_color="green")
    
    tree.output_geometry = geo
```

In the resulting tree, Position and Index nodes are fields of the input geometry because their links "join" at node 'Set Position':

<img src="/docs/images/fields_1_tree.png" width="400">

Let's add another 'Set Position' node after the second one, fed by the same offset input:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    geo = tree.input_geometry
    
    v = geo.position
    v = v.scale(scale=geo.index)
    
    geo.set_position(offset=v, node_color="green")
    geo.set_position(offset=v, node_color="blue")
    
    tree.output_geometry = geo
```

*** THE RESULTING TREE IS NOT THE FOLLOWING ***

<img src="/docs/images/fields_1.png" width="400">

Because in the tree above, the fields **Index** and **Position** are evaluated twice, one for 











