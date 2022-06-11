
# Node MagicTexture

> Geometry node name: [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/magic_texture.html)<br>
  Blender type: [Magic Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2, label=None)
```



## Arguments


### Input sockets

vector : Vector
- scale : Float
- distortion : Float

### Parameters

turbulence_depth : int (default = 2)

### Node label

- label : Geometry node display label (default=None)

## Output sockets

color : Color
- fac : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Texture) [Magic](section:Data socket Texture/Magic) : Static method

