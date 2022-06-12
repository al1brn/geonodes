
# Node SeparateComponents

> Geometry node name: [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)<br>
  Blender type: [Separate Components](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------```python
from geonodes import nodes
node = nodes.SeparateComponents(geometry=None, label=None)
```



## Arguments


### Input sockets

- geometry : Geometry

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- mesh : Mesh
- point_cloud : Geometry
- curve : Curve
- volume : Volume
- instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[components](/docs/sockets/Geometry.md#components) : Property
- [Geometry](/docs/sockets/Geometry.md).[curve_component](/docs/sockets/Geometry.md#curve_component) : Property
- [Geometry](/docs/sockets/Geometry.md).[instances_component](/docs/sockets/Geometry.md#instances_component) : Property
- [Geometry](/docs/sockets/Geometry.md).[mesh_component](/docs/sockets/Geometry.md#mesh_component) : Property
- [Geometry](/docs/sockets/Geometry.md).[points_component](/docs/sockets/Geometry.md#points_component) : Property
- [Geometry](/docs/sockets/Geometry.md).[volume_component](/docs/sockets/Geometry.md#volume_component) : Property
  
