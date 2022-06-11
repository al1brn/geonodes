
# Node Index

> Geometry node name: [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/index.html)<br>
  Blender type: [Index](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Index(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

index : Integer

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [capture_index](section:Data socket Geometry/capture_index) : Capture attribute
- [class_name](section:Data socket Geometry) [index](section:Data socket Geometry/index) : Attribute
- [class_name](section:Data socket Instances) [instance_index](section:Data socket Instances/instance_index) : Attribute
- [class_name](section:Data socket Spline) [spline_index](section:Data socket Spline/spline_index) : Attribute
- [class_name](section:Data socket Spline) [spline_position](section:Data socket Spline/spline_position) : Attribute
  
