
# Node ID

> Geometry node name: [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)<br>
  Blender type: [ID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ID(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- ID : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[ID](/docs/sockets/Geometry.md#id) : Attribute
- [Geometry](/docs/sockets/Geometry.md).[capture_ID](/docs/sockets/Geometry.md#capture_id) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[spline_ID](/docs/sockets/Spline.md#spline_id) : Attribute
  
