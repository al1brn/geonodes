
# Node Cylinder

> Geometry node name: [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html)<br>
  Blender type: [Cylinder](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None, node_color=None)
```



## Arguments


### Input sockets

- vertices : Integer
- side_segments : Integer
- fill_segments : Integer
- radius : Float
- depth : Float

### Parameters

- fill_type : str (default = 'NGON') in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
- top : Boolean
- side : Boolean
- bottom : Boolean
