# Node DeleteGeometry

- Node name : 'Delete Geometry'
- bl_idname : [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- domain : 'POINT'
- mode : 'ALL'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [delete_geometry](/docs/GeoNodes/Geometry.md#delete_geometry)

## Init

``` python
def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeDeleteGeometry', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.mode            = mode
    self.geometry        = geometry
    self.selection       = selection
```
