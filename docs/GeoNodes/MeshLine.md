# Node MeshLine

- Node name : 'Mesh Line'
- bl_idname : [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
MeshLine(count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label=None, node_color=None)
```
##### Arguments

- count : None
- start_location : None
- offset : None
- count_mode : 'TOTAL'
- mode : 'OFFSET'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshLine', node_label=node_label, node_color=node_color)

    self.count_mode      = count_mode
    self.mode            = mode
    self.count           = count
    self.start_location  = start_location
    self.offset          = offset
```
