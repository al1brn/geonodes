# Node RandomValue

- Node name : 'Random Value'
- bl_idname : [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)


``` python
RandomValue(min=None, max=None, ID=None, seed=None, probability=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- min : None
- max : None
- ID : None
- seed : None
- probability : None
- data_type : 'FLOAT'

## Implementation

- Functions : [random_boolean](/docs/GeoNodes/GeoNodesTree.md#random_boolean) [random_float](/docs/GeoNodes/GeoNodesTree.md#random_float) [random_int](/docs/GeoNodes/GeoNodesTree.md#random_int) [random_value](/docs/GeoNodes/GeoNodesTree.md#random_value) [random_vector](/docs/GeoNodes/GeoNodesTree.md#random_vector)

## Init

``` python
def __init__(self, min=None, max=None, ID=None, seed=None, probability=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeRandomValue', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.min             = min
    self.max             = max
    self.ID              = ID
    self.seed            = seed
    self.probability     = probability
```
