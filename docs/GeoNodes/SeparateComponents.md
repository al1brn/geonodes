# Node SeparateComponents

- Node name : 'Separate Components'
- bl_idname : GeometryNodeSeparateComponents


``` python
SeparateComponents(geometry=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [separate_components](/docs/GeoNodes/Geometry.md#separate_components)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSeparateComponents', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
```
