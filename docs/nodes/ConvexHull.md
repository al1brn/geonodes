
# Node ConvexHull

> Geometry node name: [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html)<br>
  Blender type: [Convex Hull](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ConvexHull(geometry=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- convex_hull : Geometry
