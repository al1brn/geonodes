# class Cone (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : Cone
 - bl_idname : GeometryNodeMeshCone

Node parameters
 - fill_type : 'NGON'

Input sockets
 - vertices : Int
 - side_segments : Int
 - fill_segments : Int
 - radius_top : Float
 - radius_bottom : Float
 - depth : Float

Output sockets
 - mesh : Geometry
 - top : Bool
 - bottom : Bool
 - side : Bool
 - uv_map : Vect

### Header

``` python
def Cone(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', node_label=None, node_color=None):
```

## Implementations


