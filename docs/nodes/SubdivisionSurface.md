
# Node SubdivisionSurface

> Geometry node name: [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html)<br>
  Blender type: [Subdivision Surface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SubdivisionSurface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- level : Integer
- edge_crease : Float
- vertex_crease : Float

### Parameters

- boundary_smooth : str (default = 'ALL') in ('PRESERVE_CORNERS', 'ALL')
- uv_smooth : str (default = 'PRESERVE_BOUNDARIES') in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
