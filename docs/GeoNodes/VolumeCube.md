# Node VolumeCube

- Node name : 'Volume Cube'
- bl_idname : [GeometryNodeVolumeCube](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)


``` python
VolumeCube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- density : None
- background : None
- min : None
- max : None
- resolution_x : None
- resolution_y : None
- resolution_z : None

## Implementation

- Functions : [volume_cube](/docs/GeoNodes/GeoNodesTree.md#volume_cube)

## Init

``` python
def __init__(self, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeVolumeCube', node_label=node_label, node_color=node_color, **kwargs)

    self.density         = density
    self.background      = background
    self.min             = min
    self.max             = max
    self.resolution_x    = resolution_x
    self.resolution_y    = resolution_y
    self.resolution_z    = resolution_z
```
