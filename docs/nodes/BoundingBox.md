
# Node BoundingBox

> Geometry node name: [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/bounding_box.html)<br>
  Blender type: [Bounding Box](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BoundingBox(geometry=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry

### Node label

- label : Geometry node display label (default=None)

## Output sockets

bounding_box : Geometry
- min : Vector
- max : Vector

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [bound_box](section:Data socket Geometry/bound_box) : Property
- [class_name](section:Data socket Geometry) [box](section:Data socket Geometry/box) : Property
- [class_name](section:Data socket Geometry) [box_max](section:Data socket Geometry/box_max) : Property
- [class_name](section:Data socket Geometry) [box_min](section:Data socket Geometry/box_min) : Property
  
