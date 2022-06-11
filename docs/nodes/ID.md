
# Node ID

> Geometry node name: [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/id.html)<br>
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

ID : Integer

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [ID](section:Data socket Geometry/ID) : Attribute
- [class_name](section:Data socket Geometry) [capture_ID](section:Data socket Geometry/capture_ID) : Capture attribute
- [class_name](section:Data socket Spline) [spline_ID](section:Data socket Spline/spline_ID) : Attribute
  
