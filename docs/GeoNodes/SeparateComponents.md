# Node SeparateComponents

- Node name : 'Separate Components'
- bl_idname : [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)


``` python
SeparateComponents(geometry=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [separate_components](/docs/GeoNodes/socket_GEOMETRY.md#separate_components)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSeparateComponents', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
```
