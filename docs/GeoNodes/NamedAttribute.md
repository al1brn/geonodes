# Node NamedAttribute

- Node name : 'Named Attribute'
- bl_idname : GeometryNodeInputNamedAttribute


``` python
NamedAttribute(name=None, data_type='FLOAT', node_label=None, node_color=None)
```
##### Arguments

- name : None
- data_type : 'FLOAT'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [named_attribute](/docs/GeoNodes/Geometry.md#named_attribute) [named_boolean](/docs/GeoNodes/Geometry.md#named_boolean) [named_color](/docs/GeoNodes/Geometry.md#named_color) [named_float](/docs/GeoNodes/Geometry.md#named_float) [named_int](/docs/GeoNodes/Geometry.md#named_int) [named_quaternion](/docs/GeoNodes/Geometry.md#named_quaternion) [named_vector](/docs/GeoNodes/Geometry.md#named_vector)
- Functions : [named_boolean](/docs/GeoNodes/index.md#named_boolean) [named_color](/docs/GeoNodes/index.md#named_color) [named_float](/docs/GeoNodes/index.md#named_float) [named_int](/docs/GeoNodes/index.md#named_int) [named_quaternion](/docs/GeoNodes/index.md#named_quaternion) [named_vector](/docs/GeoNodes/index.md#named_vector)

## Init

``` python
def __init__(self, name=None, data_type='FLOAT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputNamedAttribute', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.name            = name
```
