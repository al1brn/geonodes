# class SubdivisionSurface (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SubdivisionSurface
 - bl_idname : GeometryNodeSubdivisionSurface

Node parameters
 - boundary_smooth : 'ALL'
 - uv_smooth : 'PRESERVE_BOUNDARIES'

Input sockets
 - mesh : Geometry
 - level : Int
 - edge_crease : Float
 - vertex_crease : Float

Output sockets
 - mesh : Geometry

### Header

``` python
def SubdivisionSurface(self, mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None):
```

## Implementations

o functions : [subdivision_surface](/docs/GeoNodes_classes/subdivision_surface.md)
o Geometry : [subdivision_surface](/docs/GeoNodes_classes/subdivision_surface.md) 

