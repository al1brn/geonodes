# class Arc (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
----
 - Class name : Arc
 - bl_idname : GeometryNodeCurveArc

Node parameters
---------------
 - mode : 'RADIUS'

Input sockets
-------------
 - resolution : Int
 - start : Vect
 - middle : Vect
 - end : Vect
 - radius : Float
 - start_angle : Float
 - sweep_angle : Float
 - offset_angle : Float
 - connect_center : Bool
 - invert_arc : Bool

Output sockets
--------------
 - curve : Geometry
 - center : Vect
 - normal : Vect
 - radius : Float

### Header

``` python
def Arc(self, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, start=None, middle=None, end=None, offset_angle=None, mode='RADIUS', node_label=None, node_color=None):
```

## Implementations


