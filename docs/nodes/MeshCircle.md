
# Node MeshCircle

> Geometry node name: [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html)<br>
  Blender type: [Mesh Circle](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE', label=None, node_color=None)
```



## Arguments


### Input sockets

- vertices : Integer
- radius : Float

### Parameters

- fill_type : str (default = 'NONE') in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
