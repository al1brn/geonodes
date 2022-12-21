# Node Set Shade Smooth

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)
- geonodes name: `SetShadeSmooth`
- bl_idname: `GeometryNodeSetShadeSmooth`

```python
from geonodes import nodes

node = nodes.SetShadeSmooth(geometry=None, selection=None, shade_smooth=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **shade_smooth**: [Boolean](Boolean.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [set_shade_smooth](Mesh.md#set_shade_smooth)
#### class [Face](Face.md)

 - [set_shade_smooth](Face.md#set_shade_smooth)
 - [shade_smooth](Face.md#shade_smooth)