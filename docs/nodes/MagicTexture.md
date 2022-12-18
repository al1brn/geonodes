
# Node MagicTexture

> Geometry node name: [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)<br>
  Blender type: [Magic Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2, label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- scale : Float
- distortion : Float

### Parameters

- turbulence_depth : int (default = 2)

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- color : Color
- fac : Float
