
# Node BoundingBox

> Geometry node name: [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html)<br>
  Blender type: [Bounding Box](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BoundingBox(geometry=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- bounding_box : Geometry
- min : Vector
- max : Vector
