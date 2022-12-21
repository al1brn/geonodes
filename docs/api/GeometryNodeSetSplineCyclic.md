# Node Set Spline Cyclic

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetSplineCyclic`

```python
from geonodes import nodes

node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None)
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- cyclic: Boolean

#### Output sockets:

- **geometry** : Geometry

