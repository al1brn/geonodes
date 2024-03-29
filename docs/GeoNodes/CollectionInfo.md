# Node CollectionInfo

- Node name : 'Collection Info'
- bl_idname : [GeometryNodeCollectionInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)


``` python
CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- collection : None
- separate_children : None
- reset_children : None
- transform_space : 'ORIGINAL'

## Implementation

- [COLLECTION](/docs/GeoNodes/socket_COLLECTION.md) : [collection_info](/docs/GeoNodes/socket_COLLECTION.md#collection_info)

## Init

``` python
def __init__(self, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCollectionInfo', node_label=node_label, node_color=node_color, **kwargs)

    self.transform_space = transform_space
    self.collection      = collection
    self.separate_children = separate_children
    self.reset_children  = reset_children
```
