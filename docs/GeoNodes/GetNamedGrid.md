# Node GetNamedGrid

- Node name : 'Get Named Grid'
- bl_idname : [GeometryNodeGetNamedGrid](https://docs.blender.org/api/current/bpy.types.GeometryNodeGetNamedGrid.html)


``` python
GetNamedGrid(volume=None, name=None, remove=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- volume : None
- name : None
- remove : None
- data_type : 'FLOAT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, volume=None, name=None, remove=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeGetNamedGrid', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.volume          = volume
    self.name            = name
    self.remove          = remove
```
