# Node ObjectInfo

- Node name : 'Object Info'
- bl_idname : [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)


``` python
ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- object : None
- as_instance : None
- transform_space : 'ORIGINAL'

## Implementation

- [OBJECT](/docs/GeoNodes/socket_OBJECT.md) : [object_info](/docs/GeoNodes/socket_OBJECT.md#object_info)

## Init

``` python
def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeObjectInfo', node_label=node_label, node_color=node_color, **kwargs)

    self.transform_space = transform_space
    self.object          = object
    self.as_instance     = as_instance
```
