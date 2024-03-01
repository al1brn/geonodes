# Node ObjectInfo

- Node name : 'Object Info'
- bl_idname : [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)


``` python
ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', node_label=None, node_color=None)
```
##### Arguments

- object : None
- as_instance : None
- transform_space : 'ORIGINAL'

## Implementation

- [Object](/docs/GeoNodes/Object.md) : [object_info](/docs/GeoNodes/Object.md#object_info)

## Init

``` python
def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeObjectInfo', node_label=node_label, node_color=node_color)

    self.transform_space = transform_space
    self.object          = object
    self.as_instance     = as_instance
```
