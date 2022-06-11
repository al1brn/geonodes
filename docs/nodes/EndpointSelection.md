
# Node EndpointSelection

> Geometry node name: [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html)<br>
  Blender type: [Endpoint Selection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EndpointSelection(start_size=None, end_size=None, label=None)
```



## Arguments


### Input sockets

- start_size : Integer
- end_size : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- selection : Boolean

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_endpoint_selection](/docs/sockets/Spline.md#capture_endpoint_selection) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[endpoint_selection](/docs/sockets/Spline.md#endpoint_selection) : Attribute
  
