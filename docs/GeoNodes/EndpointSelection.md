# Node EndpointSelection

- Node name : 'Endpoint Selection'
- bl_idname : GeometryNodeCurveEndpointSelection


``` python
EndpointSelection(start_size=None, end_size=None, node_label=None, node_color=None)
```
##### Arguments

- start_size : None
- end_size : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [endpoint_selection](/docs/GeoNodes/Geometry.md#endpoint_selection)

## Init

``` python
def __init__(self, start_size=None, end_size=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveEndpointSelection', node_label=node_label, node_color=node_color)

    self.start_size      = start_size
    self.end_size        = end_size
```
