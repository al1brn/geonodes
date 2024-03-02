# Node Fresnel

- Node name : 'Fresnel'
- bl_idname : [ShaderNodeFresnel](https://docs.blender.org/api/current/bpy.types.ShaderNodeFresnel.html)


``` python
Fresnel(ior=None, normal=None, node_label=None, node_color=None)
```
##### Arguments

- ior : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, ior=None, normal=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeFresnel', node_label=node_label, node_color=node_color)

    self.ior             = ior
    self.normal          = normal
```
