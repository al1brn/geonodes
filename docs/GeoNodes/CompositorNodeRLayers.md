# Node RenderLayers

- Node name : 'Render Layers'
- bl_idname : CompositorNodeRLayers


``` python
RenderLayers(layer='ViewLayer', scene=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- layer : ViewLayer
- scene : <bpy_struct, Scene("Scene.001") at 0x114266e08>
- tag_need_exec : <bpy_func CompositorNodeRLayers.tag_need_exec()>

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, layer='ViewLayer', scene=None, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeRLayers', node_label=node_label, node_color=node_color)

    self.layer           = layer
    self.scene           = scene
    self.tag_need_exec   = tag_need_exec
```
