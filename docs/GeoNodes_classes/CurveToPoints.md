# class CurveToPoints (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : CurveToPoints
 - bl_idname : GeometryNodeCurveToPoints

Node parameters
 - mode : 'COUNT'

Input sockets
 - curve : Geometry
 - count : Int
 - length : Float

Output sockets
 - points : Geometry
 - tangent : Vect
 - normal : Vect
 - rotation : Vect

### Header

``` python
def CurveToPoints(self, curve=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None):
```

## Implementations

o Geometry : [curve_to_points](/docs/GeoNodes_classes/Geometry.md#curve_to_points) 

