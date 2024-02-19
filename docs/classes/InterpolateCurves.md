# class InterpolateCurves (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : InterpolateCurves
 - bl_idname : GeometryNodeInterpolateCurves

Node parameters

Input sockets
 - guide_curves : Geometry
 - guide_up : Vect
 - guide_group_id : Int
 - points : Geometry
 - point_up : Vect
 - point_group_id : Int
 - max_neighbors : Int

Output sockets
 - curves : Geometry
 - closest_index : Int
 - closest_weight : Float

### Header

``` python
def InterpolateCurves(self, guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None, node_label=None, node_color=None):
```

## Implementations

o Geometry : [interpolate_curves](#interpolate_curves) 

