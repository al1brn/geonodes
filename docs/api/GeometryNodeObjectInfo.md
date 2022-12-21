# Node Object Info

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
- geonodes name: `ObjectInfo`
- bl_idname: `GeometryNodeObjectInfo`

```python
from geonodes import nodes

node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL')
```

### Args:

#### Input socket arguments:

- **object**: [Object](Object.md)
- **as_instance**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **transform_space** (str): default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')

### Output sockets:

- **location** : [Vector](Vector.md)
- **rotation** : [Vector](Vector.md)
- **scale** : [Vector](Vector.md)
- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Object](Object.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f92d0>>](Object.md#info)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f92a0>>](Object.md#location)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f9270>>](Object.md#rotation)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f9240>>](Object.md#scale)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f9210>>](Object.md#geometry)
