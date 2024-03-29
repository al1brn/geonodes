# Node RenderLayers

- Node name : 'Render Layers'
- bl_idname : [CompositorNodeRLayers](https://docs.blender.org/api/current/bpy.types.CompositorNodeRLayers.html)


``` python
RenderLayers(layer='ViewLayer', scene=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- layer : ViewLayer
- scene : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, layer='ViewLayer', scene=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeRLayers', node_label=node_label, node_color=node_color, **kwargs)

    self.layer           = layer
    self.scene           = scene
    self.tag_need_exec   = tag_need_exec
```
