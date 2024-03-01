# Node GeometryToInstance

- Node name : 'Geometry to Instance'
- bl_idname : GeometryNodeGeometryToInstance


``` python
GeometryToInstance(*args, geometry=None, node_label=None, node_color=None)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- geometry : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [geometry_to_instance](/docs/GeoNodes/Geometry.md#geometry_to_instance)

## Init

``` python
def __init__(self, *args, geometry=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeGeometryToInstance', node_label=node_label, node_color=node_color)

    self._set_multi_input(*args)
    self.geometry        = geometry
```
