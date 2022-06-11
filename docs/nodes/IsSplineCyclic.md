
# Node IsSplineCyclic

> Geometry node name: [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/is_spline_cyclic.html)<br>
  Blender type: [Is Spline Cyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.IsSplineCyclic(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

cyclic : Boolean

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Spline) [capture_cyclic](section:Data socket Spline/capture_cyclic) : Capture attribute
- [class_name](section:Data socket Spline) [cyclic](section:Data socket Spline/cyclic) : Attribute
  
