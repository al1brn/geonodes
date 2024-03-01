# Node Material

- Node name : 'Material'
- bl_idname : [Material](https://docs.blender.org/api/current/bpy.types.Material.html)


``` python
Material(material=None, node_label=None, node_color=None)
```
##### Arguments

- material : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, material=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputMaterial', node_label=node_label, node_color=node_color)

    self.material        = material
```
