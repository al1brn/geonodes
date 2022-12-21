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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x164097e20>>](Spline.md#set_resolution)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x164097df0>>](Spline.md#resolution)
