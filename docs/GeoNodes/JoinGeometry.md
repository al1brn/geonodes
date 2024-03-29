# Node JoinGeometry

- Node name : 'Join Geometry'
- bl_idname : [GeometryNodeJoinGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)


``` python
JoinGeometry(*args, geometry=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [join_geometry](/docs/GeoNodes/socket_GEOMETRY.md#join_geometry)
- Functions : [join_geometry](/docs/GeoNodes/GeoNodesTree.md#join_geometry)

## Init

``` python
def __init__(self, *args, geometry=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeJoinGeometry', node_label=node_label, node_color=node_color, **kwargs)

    self._set_multi_input(*args)
    self.geometry        = geometry
```
