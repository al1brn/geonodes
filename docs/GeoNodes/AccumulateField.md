# Node AccumulateField

- Node name : 'Accumulate Field'
- bl_idname : [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
AccumulateField(value=None, group_id=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- value : None
- group_id : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, value=None, group_id=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeAccumulateField', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.domain          = domain
    self.value           = value
    self.group_id        = group_id
```
