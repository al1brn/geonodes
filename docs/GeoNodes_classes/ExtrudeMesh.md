# class ExtrudeMesh (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : ExtrudeMesh
 - bl_idname : GeometryNodeExtrudeMesh

Node parameters
 - mode : 'FACES'

Input sockets
 - mesh : Geometry
 - selection : Bool
 - offset : Vect
 - offset_scale : Float
 - individual : Bool

Output sockets
 - mesh : Geometry
 - top : Bool
 - side : Bool

### Header

``` python
def ExtrudeMesh(self, mesh=None, offset=None, offset_scale=None, individual=None, selection=None, mode='FACES', node_label=None, node_color=None):
```

## Implementations

o Geometry : [extrude_mesh](/docs/GeoNodes_classes/Geometry.md#extrude_mesh)


