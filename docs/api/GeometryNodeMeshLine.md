# Node Mesh Line

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
- geonodes name: `MeshLine`
- bl_idname: `GeometryNodeMeshLine`

```python
from geonodes import nodes

node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```

### Args:

#### Input socket arguments:

- **count**: [Integer](Integer.md)
- **resolution**: [Float](Float.md)
- **start_location**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

#### Node parameter arguments:

- **count_mode** (str): default = 'TOTAL' in ('TOTAL', 'RESOLUTION')
- **mode** (str): default = 'OFFSET' in ('OFFSET', 'END_POINTS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16e378340>>](Mesh.md#Line-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16e3797e0>>](Mesh.md#LineEndPoints-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16e378430>>](Mesh.md#LineOffset-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16e3783d0>>](Mesh.md#LineEndPointsResolution-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16e3783a0>>](Mesh.md#LineOffsetResolution-classmethod)
