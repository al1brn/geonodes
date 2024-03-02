# Node DuplicateElements

- Node name : 'Duplicate Elements'
- bl_idname : [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)


``` python
DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- amount : None
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [duplicate_elements](/docs/GeoNodes/GEOMETRY.md#duplicate_elements) [duplicate_elements](/docs/GeoNodes/GEOMETRY.md#duplicate_elements)

## Init

``` python
def __init__(self, geometry=None, selection=None, amount=None, domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeDuplicateElements', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.amount          = amount
```
