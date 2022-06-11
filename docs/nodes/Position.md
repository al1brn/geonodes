
# Node Position

> Geometry node name: [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/position.html)<br>
  Blender type: [Position](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Position(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- position : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[capture_position](/docs/sockets/Geometry.md#capture_position) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[position](/docs/sockets/Geometry.md#position) : Attribute
  
