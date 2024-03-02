# Node Levels

- Node name : 'Levels'
- bl_idname : [CompositorNodeLevels](https://docs.blender.org/api/current/bpy.types.CompositorNodeLevels.html)


``` python
Levels(image=None, channel='COMBINED_RGB', tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- channel : 'COMBINED_RGB'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, channel='COMBINED_RGB', tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeLevels', node_label=node_label, node_color=node_color)

    self.channel         = channel
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
