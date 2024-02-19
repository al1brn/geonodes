# class DistributePointsOnFaces (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : DistributePointsOnFaces
 - bl_idname : GeometryNodeDistributePointsOnFaces

Node parameters
 - distribute_method : 'RANDOM'
 - use_legacy_normal : False

Input sockets
 - mesh : Geometry
 - selection : Bool
 - distance_min : Float
 - density_max : Float
 - density : Float
 - density_factor : Float
 - seed : Int

Output sockets
 - points : Geometry
 - normal : Vect
 - rotation : Vect

### Header

``` python
def DistributePointsOnFaces(self, mesh=None, density=None, seed=None, distance_min=None, density_max=None, density_factor=None, selection=None, distribute_method='RANDOM', use_legacy_normal=False, node_label=None, node_color=None):
```

## Implementations

o Geometry : [distribute_points_on_faces](/docs/GeoNodes_classes/distribute_points_on_faces.md) 

