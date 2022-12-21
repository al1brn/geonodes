# Node Image Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
- geonodes name: `ImageTexture`
- bl_idname: `GeometryNodeImageTexture`

```python
from geonodes import nodes

node = nodes.ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```

### Args:

#### Input socket arguments:

- **image**: [Image](Image.md)
- **vector**: [Vector](Vector.md)
- **frame**: [Integer](Integer.md)

#### Node parameter arguments:

- **extension** (str): default = 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP')
- **interpolation** (str): default = 'Linear' in ('Linear', 'Closest', 'Cubic')

### Output sockets:

- **color** : [Color](Color.md)
- **alpha** : [Float](Float.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2e00>>](Image.md#texture)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b2950>>](Texture.md#image-staticmethod)
