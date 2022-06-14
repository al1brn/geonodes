
# Node Radius

> Geometry node name: [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)<br>
  Blender type: [Radius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Radius(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- radius : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[capture_radius](/docs/sockets/Geometry.md#capture_radius) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[radius](/docs/sockets/Geometry.md#radius) : Attribute
  
