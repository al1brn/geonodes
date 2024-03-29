# Node SplitToInstances

- Node name : 'Split to Instances'
- bl_idname : [GeometryNodeSplitToInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitToInstances.html)


``` python
SplitToInstances(geometry=None, selection=None, group_id=None, domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- group_id : None
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [split_to_instances](/docs/GeoNodes/socket_GEOMETRY.md#split_to_instances)

## Init

``` python
def __init__(self, geometry=None, selection=None, group_id=None, domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSplitToInstances', node_label=node_label, node_color=node_color, **kwargs)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.group_id        = group_id
```
