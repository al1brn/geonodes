
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
