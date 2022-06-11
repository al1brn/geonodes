
# Node IsShadeSmooth

> Geometry node name: [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/is_shade_smooth.html)<br>
  Blender type: [Is Shade Smooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.IsShadeSmooth(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

smooth : Boolean

## Data sockets

> Data socket classes implementing this node.
  
[Mesh](/docs/sockets/Mesh.md).[capture_shade_smooth](/docs/sockets/Mesh.md#capture_shade_smooth) : Capture attribute
- [Mesh](/docs/sockets/Mesh.md).[shade_smooth](/docs/sockets/Mesh.md#shade_smooth) : Attribute
  
