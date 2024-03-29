# Node DistributePointsInVolume

- Node name : 'Distribute Points in Volume'
- bl_idname : [GeometryNodeDistributePointsInVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)


``` python
DistributePointsInVolume(volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- volume : None
- density : None
- seed : None
- spacing : None
- threshold : None
- mode : 'DENSITY_RANDOM'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [distribute_points_in_volume](/docs/GeoNodes/socket_GEOMETRY.md#distribute_points_in_volume)

## Init

``` python
def __init__(self, volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeDistributePointsInVolume', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.volume          = volume
    self.density         = density
    self.seed            = seed
    self.spacing         = spacing
    self.threshold       = threshold
```
