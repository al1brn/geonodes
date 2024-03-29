# Node StoreNamedGrid

- Node name : 'Store Named Grid'
- bl_idname : [GeometryNodeStoreNamedGrid](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedGrid.html)


``` python
StoreNamedGrid(volume=None, name=None, grid=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- volume : None
- name : None
- grid : None
- data_type : 'FLOAT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, volume=None, name=None, grid=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeStoreNamedGrid', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.volume          = volume
    self.name            = name
    self.grid            = grid
```
