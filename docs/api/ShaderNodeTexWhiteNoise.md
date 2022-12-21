# Node White Noise Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
- geonodes name: `WhiteNoiseTexture`
- bl_idname: `ShaderNodeTexWhiteNoise`

```python
from geonodes import nodes

node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D')
```

#### Input socket arguments:

- `vector`: [Vector](Vector.md)
- `w`: [Float](Float.md)

#### Node parameter arguments:

- noise_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')

#### Output sockets:

- **value** : [Float](Float.md)
- **color** : [Color](Color.md)

