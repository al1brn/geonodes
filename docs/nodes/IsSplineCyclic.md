
# Node IsSplineCyclic

> Geometry node name: [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html)<br>
  Blender type: [Is Spline Cyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------```python
from geonodes import nodes
node = nodes.IsSplineCyclic(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- cyclic : Boolean

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_cyclic](/docs/sockets/Spline.md#capture_cyclic) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[cyclic](/docs/sockets/Spline.md#cyclic) : Attribute
  
