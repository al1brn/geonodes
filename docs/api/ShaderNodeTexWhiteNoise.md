# Node *White Noise Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
- geonodes name: `WhiteNoiseTexture`
- bl_idname: `ShaderNodeTexWhiteNoise`

```python
from geonodes import nodes

node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)

#### Node parameter arguments:

- **noise_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')

### Output sockets:

- **value** : [Float](Float.md)
- **color** : [Color](Color.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [white_noise](Texture.md#white_noise) | `@staticmethod`<br> `def white_noise(vector=None, w=None, noise_dimensions='3D'):` |
| [white_noise_1D](Texture.md#white_noise_1D) | `@staticmethod`<br> `def white_noise_1D(w=None):` |
| [white_noise_2D](Texture.md#white_noise_2D) | `@staticmethod`<br> `def white_noise_2D(vector=None):` |
| [white_noise_3D](Texture.md#white_noise_3D) | `@staticmethod`<br> `def white_noise_3D(vector=None):` |
| [white_noise_4D](Texture.md#white_noise_4D) | `@staticmethod`<br> `def white_noise_4D(vector=None, w=None):` |

<sub>Go to [top](#node-White-Noise-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

