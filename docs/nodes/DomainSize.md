
# Node DomainSize

> Geometry node name: [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)<br>
  Blender type: [Domain Size](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DomainSize(geometry=None, component='MESH', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry

### Parameters

- component : str (default = 'MESH') in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- point_count : Integer
- edge_count : Integer
- face_count : Integer
- face_corner_count : Integer
- spline_count : Integer
- instance_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[domain_size](/docs/sockets/Curve.md#domain_size) : Property
- [Curve](/docs/sockets/Curve.md).[point_count](/docs/sockets/Curve.md#point_count) : Property
- [Curve](/docs/sockets/Curve.md).[spline_count](/docs/sockets/Curve.md#spline_count) : Property
- [Instances](/docs/sockets/Instances.md).[domain_size](/docs/sockets/Instances.md#domain_size) : Property
- [Instances](/docs/sockets/Instances.md).[instance_count](/docs/sockets/Instances.md#instance_count) : Property
- [Mesh](/docs/sockets/Mesh.md).[corner_count](/docs/sockets/Mesh.md#corner_count) : Property
- [Mesh](/docs/sockets/Mesh.md).[domain_size](/docs/sockets/Mesh.md#domain_size) : Property
- [Mesh](/docs/sockets/Mesh.md).[edge_count](/docs/sockets/Mesh.md#edge_count) : Property
- [Mesh](/docs/sockets/Mesh.md).[face_count](/docs/sockets/Mesh.md#face_count) : Property
- [Mesh](/docs/sockets/Mesh.md).[point_count](/docs/sockets/Mesh.md#point_count) : Property
- [Points](/docs/sockets/Points.md).[domain_size](/docs/sockets/Points.md#domain_size) : Property
- [Points](/docs/sockets/Points.md).[point_count](/docs/sockets/Points.md#point_count) : Property
  
