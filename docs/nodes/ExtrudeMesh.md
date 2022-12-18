
# Node ExtrudeMesh

> Geometry node name: [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)<br>
  Blender type: [Extrude Mesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean
- offset : Vector
- offset_scale : Float
- individual : Boolean

### Parameters

- mode : str (default = 'FACES') in ('VERTICES', 'EDGES', 'FACES')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
- top : Boolean
- side : Boolean
