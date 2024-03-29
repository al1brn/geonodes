# Node NamedLayerSelection

- Node name : 'Named Layer Selection'
- bl_idname : [GeometryNodeInputNamedLayerSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedLayerSelection.html)


``` python
NamedLayerSelection(name=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- name : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, name=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputNamedLayerSelection', node_label=node_label, node_color=node_color, **kwargs)

    self.name            = name
```
