
# Class SubdivisionSurface

> Geometry node name: _'Subdivision Surface'_<br>Blender type:  **GeometryNodeSubdivisionSurface**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.SubdivisionSurface(mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None)
```


### Arguments


#### Input sockets



- **mesh** : _Mesh_
- **level** : _Integer_
- **crease** : _Float_



#### Parameters



- **boundary_smooth** : _'ALL'_ in ('PRESERVE_CORNERS', 'ALL')
- **uv_smooth** : _'PRESERVE_BOUNDARIES'_ in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node




- [Mesh](../sockets/Mesh.md) [subdivision_surface](../sockets/Mesh.md#subdivision_surface) : Method


