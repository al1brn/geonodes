
# Node WhiteNoiseTexture

> Geometry node name: [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)<br>
  Blender type: [White Noise Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- w : Float

### Parameters

- noise_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- value : Float
- color : Color
