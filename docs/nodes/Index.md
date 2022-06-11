
# Node Index

> Geometry node name: [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/index.html)<br>
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

- index : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[capture_index](/docs/sockets/Geometry.md#capture_index) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[index](/docs/sockets/Geometry.md#index) : Attribute
- [Instances](/docs/sockets/Instances.md).[instance_index](/docs/sockets/Instances.md#instance_index) : Attribute
- [Spline](/docs/sockets/Spline.md).[spline_index](/docs/sockets/Spline.md#spline_index) : Attribute
- [Spline](/docs/sockets/Spline.md).[spline_position](/docs/sockets/Spline.md#spline_position) : Attribute
  
