# class Raycast (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : Raycast
 - bl_idname : GeometryNodeRaycast

Node parameters
 - data_type : 'FLOAT'
 - mapping : 'INTERPOLATED'

Input sockets
 - target_geometry : Geometry
 - attribute : Vect
 - attribute_1 : Float
 - attribute_2 : Col
 - attribute_3 : Bool
 - attribute_4 : Int
 - attribute_5 : Rot
 - source_position : Vect
 - ray_direction : Vect
 - ray_length : Float

Output sockets
 - is_hit : Bool
 - hit_position : Vect
 - hit_normal : Vect
 - hit_distance : Float
 - attribute : Vect
 - attribute_1 : Float
 - attribute_2 : Col
 - attribute_3 : Bool
 - attribute_4 : Int
 - attribute_5 : Rot

### Header

``` python
def Raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', node_label=None, node_color=None):
```

## Implementations

o Float : [raycast](/docs/classes/raycast.md) 
o Int : [raycast](/docs/classes/raycast.md) 

