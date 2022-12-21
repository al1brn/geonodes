# Node Set Spline Resolution

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetSplineResolution`

```python
from geonodes import nodes

node = nodes.SetSplineResolution(geometry=None, selection=None, resolution=None)
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- resolution: Integer

#### Output sockets:

- **geometry** : Geometry

