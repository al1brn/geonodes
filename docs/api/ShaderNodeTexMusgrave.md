# Node Musgrave Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
- geonodes name: `MusgraveTexture`
- bl_idname: `ShaderNodeTexMusgrave`

```python
from geonodes import nodes

node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM')
```

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)
- **scale**: [Float](Float.md)
- **detail**: [Float](Float.md)
- **dimension**: [Float](Float.md)
- **lacunarity**: [Float](Float.md)
- **offset**: [Float](Float.md)
- **gain**: [Float](Float.md)

#### Node parameter arguments:

- **musgrave_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')
- **musgrave_type** (str): default = 'FBM' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')

### Output sockets:

- **fac** : [Float](Float.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0c40>>](Texture.md#musgrave-staticmethod)
