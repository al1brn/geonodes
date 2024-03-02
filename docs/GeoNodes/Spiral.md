# Node Spiral

- Node name : 'Spiral'
- bl_idname : [GeometryNodeCurveSpiral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)


``` python
Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, node_label=None, node_color=None)
```
##### Arguments

- resolution : None
- rotations : None
- start_radius : None
- end_radius : None
- height : None
- reverse : None

## Implementation

- Functions : [spiral](/docs/GeoNodes/GeoNodesTree.md#spiral) [spiral](/docs/GeoNodes/GeoNodesTree.md#spiral)

## Init

``` python
def __init__(self, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeCurveSpiral', node_label=node_label, node_color=node_color)

    self.resolution      = resolution
    self.rotations       = rotations
    self.start_radius    = start_radius
    self.end_radius      = end_radius
    self.height          = height
    self.reverse         = reverse
```
