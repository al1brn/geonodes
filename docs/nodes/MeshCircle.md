
# Node MeshCircle

> Geometry node name: [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mesh_circle.html)<br>
  Blender type: [Mesh Circle](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE', label=None)
```



## Arguments


### Input sockets

- vertices : Integer
- radius : Float

### Parameters

- fill_type : str (default = 'NONE') in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[Circle](/docs/sockets/Mesh.md#circle) : Constructor
  
