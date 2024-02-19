# class Triangulate (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : Triangulate
 - bl_idname : GeometryNodeTriangulate

Node parameters
 - ngon_method : 'BEAUTY'
 - quad_method : 'SHORTEST_DIAGONAL'

Input sockets
 - mesh : Geometry
 - selection : Bool
 - minimum_vertices : Int

Output sockets
 - mesh : Geometry

### Header

``` python
def Triangulate(self, mesh=None, minimum_vertices=None, selection=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None):
```

## Implementations

o functions : [triangulate](#triangulate)
o Geometry : [triangulate](#triangulate) 

