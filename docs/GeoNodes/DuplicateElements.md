# Node DuplicateElements

- Node name : 'Duplicate Elements'
- bl_idname : [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)


``` python
DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- amount : None
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [duplicate_elements](/docs/GeoNodes/socket_GEOMETRY.md#duplicate_elements)

## Init

``` python
def __init__(self, geometry=None, selection=None, amount=None, domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeDuplicateElements', node_label=node_label, node_color=node_color, **kwargs)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.amount          = amount
```
