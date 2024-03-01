# Node Viewer

- Node name : 'Viewer'
- bl_idname : [GeometryNodeViewer](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Viewer(geometry=None, value=None, data_type='FLOAT', domain='AUTO', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- value : None
- data_type : 'FLOAT'
- domain : 'AUTO'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [viewer](/docs/GeoNodes/Geometry.md#viewer) [viewer_boolean](/docs/GeoNodes/Geometry.md#viewer_boolean) [viewer_color](/docs/GeoNodes/Geometry.md#viewer_color) [viewer_float](/docs/GeoNodes/Geometry.md#viewer_float) [viewer_int](/docs/GeoNodes/Geometry.md#viewer_int) [viewer_quaternion](/docs/GeoNodes/Geometry.md#viewer_quaternion) [viewer_vector](/docs/GeoNodes/Geometry.md#viewer_vector)
- Functions : [viewer](/docs/GeoNodes/GeoNodes.md#viewer)

## Init

``` python
def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='AUTO', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeViewer', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.value           = value
```
