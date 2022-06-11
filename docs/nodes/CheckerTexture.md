
# Node CheckerTexture

> Geometry node name: [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/checker_texture.html)<br>
  Blender type: [Checker Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CheckerTexture(vector=None, color1=None, color2=None, scale=None, label=None)
```



## Arguments


### Input sockets

vector : Vector
- color1 : Color
- color2 : Color
- scale : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

color : Color
- fac : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](docs/sockets/Texture.md) [Checker](docs/sockets/Texture.md#checker) : Static method

