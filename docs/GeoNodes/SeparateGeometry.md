# Node SeparateGeometry

- Node name : 'Separate Geometry'
- bl_idname : [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)


``` python
SeparateGeometry(geometry=None, selection=None, domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [separate_geometry](/docs/GeoNodes/socket_GEOMETRY.md#separate_geometry) [separate_geometry](/docs/GeoNodes/socket_GEOMETRY.md#separate_geometry)

## Init

``` python
def __init__(self, geometry=None, selection=None, domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSeparateGeometry', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
```
