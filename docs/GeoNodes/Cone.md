# Node Cone

- Node name : 'Cone'
- bl_idname : [GeometryNodeMeshCone](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)


``` python
Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vertices : None
- side_segments : None
- fill_segments : None
- radius_top : None
- radius_bottom : None
- depth : None
- fill_type : 'NGON'

## Implementation

- Functions : [cone](/docs/GeoNodes/GeoNodesTree.md#cone)

## Init

``` python
def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshCone', node_label=node_label, node_color=node_color, **kwargs)

    self.fill_type       = fill_type
    self.vertices        = vertices
    self.side_segments   = side_segments
    self.fill_segments   = fill_segments
    self.radius_top      = radius_top
    self.radius_bottom   = radius_bottom
    self.depth           = depth
```
