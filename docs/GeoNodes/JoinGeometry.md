# Node JoinGeometry

- Node name : 'Join Geometry'
- bl_idname : [GeometryNodeJoinGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)


``` python
JoinGeometry(*args, geometry=None, node_label=None, node_color=None)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [join_geometry](/docs/GeoNodes/GEOMETRY.md#join_geometry) [join_geometry](/docs/GeoNodes/GEOMETRY.md#join_geometry)
- Functions : [join_geometry](/docs/GeoNodes/GeoNodesTree.md#join_geometry) [join_geometry](/docs/GeoNodes/GeoNodesTree.md#join_geometry)

## Init

``` python
def __init__(self, *args, geometry=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeJoinGeometry', node_label=node_label, node_color=node_color)

    self._set_multi_input(*args)
    self.geometry        = geometry
```
