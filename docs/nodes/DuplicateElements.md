
# Node DuplicateElements

> Geometry node name: [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)<br>
  Blender type: [Duplicate Elements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- amount : Integer

### Parameters

- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
- duplicate_index : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[duplicate_elements](/docs/sockets/Geometry.md#duplicate_elements) : Method
- [Geometry](/docs/sockets/Geometry.md).[duplicate_points](/docs/sockets/Geometry.md#duplicate_points) : Method
- [Instances](/docs/sockets/Instances.md).[duplicate_instances](/docs/sockets/Instances.md#duplicate_instances) : Method
- [Mesh](/docs/sockets/Mesh.md).[duplicate_edges](/docs/sockets/Mesh.md#duplicate_edges) : Method
- [Mesh](/docs/sockets/Mesh.md).[duplicate_faces](/docs/sockets/Mesh.md#duplicate_faces) : Method
- [Spline](/docs/sockets/Spline.md).[duplicate_splines](/docs/sockets/Spline.md#duplicate_splines) : Method
  
