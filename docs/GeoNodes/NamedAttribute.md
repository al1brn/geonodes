# Node NamedAttribute

- Node name : 'Named Attribute'
- bl_idname : [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)


``` python
NamedAttribute(name=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- name : None
- data_type : 'FLOAT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [named_attribute](/docs/GeoNodes/socket_GEOMETRY.md#named_attribute) [named_boolean](/docs/GeoNodes/socket_GEOMETRY.md#named_boolean) [named_color](/docs/GeoNodes/socket_GEOMETRY.md#named_color) [named_float](/docs/GeoNodes/socket_GEOMETRY.md#named_float) [named_int](/docs/GeoNodes/socket_GEOMETRY.md#named_int) [named_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#named_quaternion) [named_vector](/docs/GeoNodes/socket_GEOMETRY.md#named_vector)
- Functions : [named_boolean](/docs/GeoNodes/GeoNodesTree.md#named_boolean) [named_color](/docs/GeoNodes/GeoNodesTree.md#named_color) [named_float](/docs/GeoNodes/GeoNodesTree.md#named_float) [named_int](/docs/GeoNodes/GeoNodesTree.md#named_int) [named_quaternion](/docs/GeoNodes/GeoNodesTree.md#named_quaternion) [named_vector](/docs/GeoNodes/GeoNodesTree.md#named_vector)

## Init

``` python
def __init__(self, name=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputNamedAttribute', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.name            = name
```
