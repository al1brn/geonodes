# Node MeshLine

- Node name : 'Mesh Line'
- bl_idname : [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)


``` python
MeshLine(count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- count : None
- start_location : None
- offset : None
- count_mode : 'TOTAL'
- mode : 'OFFSET'

## Implementation

- Functions : [mesh_line](/docs/GeoNodes/GeoNodesTree.md#mesh_line)

## Init

``` python
def __init__(self, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshLine', node_label=node_label, node_color=node_color, **kwargs)

    self.count_mode      = count_mode
    self.mode            = mode
    self.count           = count
    self.start_location  = start_location
    self.offset          = offset
```
