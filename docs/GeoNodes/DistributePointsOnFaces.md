# Node DistributePointsOnFaces

- Node name : 'Distribute Points on Faces'
- bl_idname : [GeometryNodeDistributePointsOnFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)


``` python
DistributePointsOnFaces(mesh=None, selection=None, density=None, seed=None, distance_min=None, density_max=None, density_factor=None, distribute_method='RANDOM', use_legacy_normal=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None
- density : None
- seed : None
- distance_min : None
- density_max : None
- density_factor : None
- distribute_method : 'RANDOM'
- use_legacy_normal : False

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [distribute_points_on_faces](/docs/GeoNodes/socket_GEOMETRY.md#distribute_points_on_faces)

## Init

``` python
def __init__(self, mesh=None, selection=None, density=None, seed=None, distance_min=None, density_max=None, density_factor=None, distribute_method='RANDOM', use_legacy_normal=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeDistributePointsOnFaces', node_label=node_label, node_color=node_color, **kwargs)

    self.distribute_method = distribute_method
    self.use_legacy_normal = use_legacy_normal
    self.mesh            = mesh
    self.selection       = selection
    self.density         = density
    self.seed            = seed
    self.distance_min    = distance_min
    self.density_max     = density_max
    self.density_factor  = density_factor
```
