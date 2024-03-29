# Node EndpointSelection

- Node name : 'Endpoint Selection'
- bl_idname : [GeometryNodeCurveEndpointSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)


``` python
EndpointSelection(start_size=None, end_size=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- start_size : None
- end_size : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [endpoint_selection](/docs/GeoNodes/socket_GEOMETRY.md#endpoint_selection)

## Init

``` python
def __init__(self, start_size=None, end_size=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveEndpointSelection', node_label=node_label, node_color=node_color, **kwargs)

    self.start_size      = start_size
    self.end_size        = end_size
```
