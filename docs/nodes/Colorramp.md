
# Node Colorramp

> Geometry node name: [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/colorramp.html)<br>
  Blender type: [ColorRamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Colorramp(fac=None, label=None)
```



## Arguments


### Input sockets

fac : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

color : Color
- alpha : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Float) [color_ramp](section:Data socket Float/color_ramp) : Method

