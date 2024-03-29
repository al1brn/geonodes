# Node RemoveNamedAttribute

- Node name : 'Remove Named Attribute'
- bl_idname : [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)


``` python
RemoveNamedAttribute(geometry=None, name=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- name : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [remove_named_attribute](/docs/GeoNodes/socket_GEOMETRY.md#remove_named_attribute)

## Init

``` python
def __init__(self, geometry=None, name=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeRemoveAttribute', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.name            = name
```
