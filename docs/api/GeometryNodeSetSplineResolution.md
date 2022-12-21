# Node Set Spline Resolution

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
- geonodes name: `SetSplineResolution`
- bl_idname: `GeometryNodeSetSplineResolution`

```python
from geonodes import nodes

node = nodes.SetSplineResolution(geometry=None, selection=None, resolution=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **resolution**: [Integer](Integer.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Spline](Spline.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4fa200>>](Spline.md#set_resolution)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x16d4fa1d0>>](Spline.md#resolution)
