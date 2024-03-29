# Node Material

- Node name : 'Material'
- bl_idname : [GeometryNodeInputMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)


``` python
Material(material=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- material : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, material=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMaterial', node_label=node_label, node_color=node_color, **kwargs)

    self.material        = material
```
