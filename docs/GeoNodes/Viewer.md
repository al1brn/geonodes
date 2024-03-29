# Node Viewer

- Node name : 'Viewer'
- bl_idname : [GeometryNodeViewer](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)


``` python
Viewer(geometry=None, value=None, data_type='FLOAT', domain='AUTO', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- value : None
- data_type : 'FLOAT'
- domain : 'AUTO'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [viewer](/docs/GeoNodes/socket_GEOMETRY.md#viewer) [viewer_boolean](/docs/GeoNodes/socket_GEOMETRY.md#viewer_boolean) [viewer_color](/docs/GeoNodes/socket_GEOMETRY.md#viewer_color) [viewer_float](/docs/GeoNodes/socket_GEOMETRY.md#viewer_float) [viewer_int](/docs/GeoNodes/socket_GEOMETRY.md#viewer_int) [viewer_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#viewer_quaternion) [viewer_vector](/docs/GeoNodes/socket_GEOMETRY.md#viewer_vector)
- Functions : [viewer](/docs/GeoNodes/GeoNodesTree.md#viewer)

## Init

``` python
def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='AUTO', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeViewer', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.value           = value
```
