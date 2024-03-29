# Node GeometryToInstance

- Node name : 'Geometry to Instance'
- bl_idname : [GeometryNodeGeometryToInstance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)


``` python
GeometryToInstance(*args, geometry=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [geometry_to_instance](/docs/GeoNodes/socket_GEOMETRY.md#geometry_to_instance)

## Init

``` python
def __init__(self, *args, geometry=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeGeometryToInstance', node_label=node_label, node_color=node_color, **kwargs)

    self._set_multi_input(*args)
    self.geometry        = geometry
```
