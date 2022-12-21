# Node Noise Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
- geonodes name: `NoiseTexture`
- bl_idname: `ShaderNodeTexNoise`

```python
from geonodes import nodes

node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D')
```

#### Input socket arguments:

- vector: Vector
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

#### Node parameter arguments:

- noise_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')

#### Output sockets:

- **fac** : Float
- **color** : Color

