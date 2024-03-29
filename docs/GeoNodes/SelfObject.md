# Node SelfObject

- Node name : 'Self Object'
- bl_idname : [GeometryNodeSelfObject](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)


``` python
SelfObject(node_label=None, node_color=None, **kwargs)
```
## Implementation

- Functions : [self_object](/docs/GeoNodes/GeoNodesTree.md#self_object)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSelfObject', node_label=node_label, node_color=node_color, **kwargs)
```
