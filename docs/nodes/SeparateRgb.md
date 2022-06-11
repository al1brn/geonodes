
# Node SeparateRgb

> Geometry node name: [Separate RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_rgb.html)<br>
  Blender type: [Separate RGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateRgb(image=None, label=None)
```



## Arguments


### Input sockets

image : Color

### Node label

- label : Geometry node display label (default=None)

## Output sockets

r : Float
- g : Float
- b : Float

## Data sockets

> Data socket classes implementing this node.
  
[Color](/docs/sockets/Color.md) [b](/docs/sockets/Color.md#b) : Property
- [Color](/docs/sockets/Color.md) [g](/docs/sockets/Color.md#g) : Property
- [Color](/docs/sockets/Color.md) [r](/docs/sockets/Color.md#r) : Property
- [Color](/docs/sockets/Color.md) [separate](/docs/sockets/Color.md#separate) : Property
  
