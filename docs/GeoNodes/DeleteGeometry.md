# Node DeleteGeometry

- Node name : 'Delete Geometry'
- bl_idname : [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)


``` python
DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- domain : 'POINT'
- mode : 'ALL'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [delete_geometry](/docs/GeoNodes/socket_GEOMETRY.md#delete_geometry)

## Init

``` python
def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeDeleteGeometry', node_label=node_label, node_color=node_color, **kwargs)

    self.domain          = domain
    self.mode            = mode
    self.geometry        = geometry
    self.selection       = selection
```
