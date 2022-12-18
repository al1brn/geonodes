
# Node Cone

> Geometry node name: [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html)<br>
  Blender type: [Cone](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None, node_color=None)
```



## Arguments


### Input sockets

- vertices : Integer
- side_segments : Integer
- fill_segments : Integer
- radius_top : Float
- radius_bottom : Float
- depth : Float

### Parameters

- fill_type : str (default = 'NGON') in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
- top : Boolean
- bottom : Boolean
- side : Boolean
