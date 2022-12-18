
# Node NoiseTexture

> Geometry node name: [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)<br>
  Blender type: [Noise Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- w : Float
- scale : Float
- detail : Float
- roughness : Float
- distortion : Float

### Parameters

- noise_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- fac : Float
- color : Color
