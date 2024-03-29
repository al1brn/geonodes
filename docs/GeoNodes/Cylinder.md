# Node Cylinder

- Node name : 'Cylinder'
- bl_idname : [GeometryNodeMeshCylinder](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)


``` python
Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vertices : None
- side_segments : None
- fill_segments : None
- radius : None
- depth : None
- fill_type : 'NGON'

## Implementation

- Functions : [cylinder](/docs/GeoNodes/GeoNodesTree.md#cylinder)

## Init

``` python
def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshCylinder', node_label=node_label, node_color=node_color, **kwargs)

    self.fill_type       = fill_type
    self.vertices        = vertices
    self.side_segments   = side_segments
    self.fill_segments   = fill_segments
    self.radius          = radius
    self.depth           = depth
```
