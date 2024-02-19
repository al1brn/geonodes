# class DomainSize (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : DomainSize
 - bl_idname : GeometryNodeAttributeDomainSize

Node parameters
 - component : 'MESH'

Input sockets
 - geometry : Geometry

Output sockets
 - point_count : Int
 - edge_count : Int
 - face_count : Int
 - face_corner_count : Int
 - spline_count : Int
 - instance_count : Int

### Header

``` python
def DomainSize(self, geometry=None, component='MESH', node_label=None, node_color=None):
```

## Implementations

o Geometry : [domain_size](#domain_size) 

