# Node IsViewport

- Node name : 'Is Viewport'
- bl_idname : [GeometryNodeIsViewport](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)


``` python
IsViewport(node_label=None, node_color=None, **kwargs)
```
## Implementation

- Functions : [is_viewport](/docs/GeoNodes/GeoNodesTree.md#is_viewport)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeIsViewport', node_label=node_label, node_color=node_color, **kwargs)
```
