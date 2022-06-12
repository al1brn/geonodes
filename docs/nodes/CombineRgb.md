
# Node CombineRgb

> Geometry node name: [Combine RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_rgb.html)<br>
  Blender type: [Combine RGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.CombineRgb(r=None, g=None, b=None, label=None)
```



## Arguments


### Input sockets

- r : Float
- g : Float
- b : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- image : Color

## Data sockets

> Data socket classes implementing this node.
  
  
- [Color](/docs/sockets/Color.md).[Combine](/docs/sockets/Color.md#combine) : Constructor
  
