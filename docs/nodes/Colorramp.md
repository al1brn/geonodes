
# Node Colorramp

> Geometry node name: [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)<br>
  Blender type: [ColorRamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Colorramp(fac=None, label=None)
```



## Arguments


### Input sockets

- fac : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- color : Color
- alpha : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Float](/docs/sockets/Float.md).[color_ramp](/docs/sockets/Float.md#color_ramp) : Method
  
