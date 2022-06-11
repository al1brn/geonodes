
# Node SeparateComponents

> Geometry node name: [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_components.html)<br>
  Blender type: [Separate Components](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateComponents(geometry=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry

### Node label

- label : Geometry node display label (default=None)

## Output sockets

mesh : Mesh
- point_cloud : Geometry
- curve : Curve
- volume : Volume
- instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [components](section:Data socket Geometry/components) : Property
- [class_name](section:Data socket Geometry) [curve_component](section:Data socket Geometry/curve_component) : Property
- [class_name](section:Data socket Geometry) [instances_component](section:Data socket Geometry/instances_component) : Property
- [class_name](section:Data socket Geometry) [mesh_component](section:Data socket Geometry/mesh_component) : Property
- [class_name](section:Data socket Geometry) [points_component](section:Data socket Geometry/points_component) : Property
- [class_name](section:Data socket Geometry) [volume_component](section:Data socket Geometry/volume_component) : Property
  
