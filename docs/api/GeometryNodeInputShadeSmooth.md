# Node Is Shade Smooth

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
- geonodes name: `IsShadeSmooth`
- bl_idname: `GeometryNodeInputShadeSmooth`

```python
from geonodes import nodes

node = nodes.IsShadeSmooth()
```

### Output sockets:

- **smooth** : [Boolean](Boolean.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [is_shade_smooth](Mesh.md#is_shade_smooth)
#### class [Face](Face.md)

 - [shade_smooth](Face.md#shade_smooth-property)