
# Node BrickTexture

> Geometry node name: [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)<br>
  Blender type: [Brick Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- color1 : Color
- color2 : Color
- mortar : Color
- scale : Float
- mortar_size : Float
- mortar_smooth : Float
- bias : Float
- brick_width : Float
- row_height : Float

### Parameters

- offset : float (default = 0.5)
- offset_frequency : int (default = 2)
- squash : float (default = 1.0)
- squash_frequency : int (default = 2)

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- color : Color
- fac : Float
