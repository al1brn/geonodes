
# Node MeshLine

> Geometry node name: [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)<br>
  Blender type: [Mesh Line](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None, node_color=None)
```



## Arguments


### Input sockets

- count : Integer
- resolution : Float
- start_location : Vector
- offset : Vector

### Parameters

- count_mode : str (default = 'TOTAL') in ('TOTAL', 'RESOLUTION')
- mode : str (default = 'OFFSET') in ('OFFSET', 'END_POINTS')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
