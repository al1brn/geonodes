# Node RemoveNamedAttribute

- Node name : 'Remove Named Attribute'
- bl_idname : [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
RemoveNamedAttribute(geometry=None, name=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- name : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [remove_named_attribute](/docs/GeoNodes/Geometry.md#remove_named_attribute)

## Init

``` python
def __init__(self, geometry=None, name=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeRemoveAttribute', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
    self.name            = name
```
