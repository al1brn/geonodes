
# Node ConvexHull

> Geometry node name: [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/convex_hull.html)<br>
  Blender type: [Convex Hull](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ConvexHull(geometry=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry

### Node label

- label : Geometry node display label (default=None)

## Output sockets

convex_hull : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [convex_hull](section:Data socket Geometry/convex_hull) : Method

