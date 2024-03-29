# Node SortElements

- Node name : 'Sort Elements'
- bl_idname : [GeometryNodeSortElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeSortElements.html)


``` python
SortElements(geometry=None, selection=None, group_id=None, sort_weight=None, domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- group_id : None
- sort_weight : None
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [sort_elements](/docs/GeoNodes/socket_GEOMETRY.md#sort_elements)

## Init

``` python
def __init__(self, geometry=None, selection=None, group_id=None, sort_weight=None, domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSortElements', node_label=node_label, node_color=node_color, **kwargs)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.group_id        = group_id
    self.sort_weight     = sort_weight
```
