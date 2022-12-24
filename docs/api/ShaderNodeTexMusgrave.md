# Node *Musgrave Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
- geonodes name: `MusgraveTexture`
- bl_idname: `ShaderNodeTexMusgrave`

```python
from geonodes import nodes

node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMusgrave.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [musgrave](Texture.md#musgrave) | `@staticmethod`<br> `def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):` |

<sub>Go to [top](#node-Musgrave-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

