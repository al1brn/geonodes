# Node StoreNamedAttribute

- Node name : 'Store Named Attribute'
- bl_idname : [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)


``` python
StoreNamedAttribute(geometry=None, selection=None, name=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- name : None
- value : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [store_named_attribute](/docs/GeoNodes/socket_GEOMETRY.md#store_named_attribute) [store_named_boolean](/docs/GeoNodes/socket_GEOMETRY.md#store_named_boolean) [store_named_byte_color](/docs/GeoNodes/socket_GEOMETRY.md#store_named_byte_color) [store_named_float](/docs/GeoNodes/socket_GEOMETRY.md#store_named_float) [store_named_float2](/docs/GeoNodes/socket_GEOMETRY.md#store_named_float2) [store_named_float_color](/docs/GeoNodes/socket_GEOMETRY.md#store_named_float_color) [store_named_int](/docs/GeoNodes/socket_GEOMETRY.md#store_named_int) [store_named_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#store_named_quaternion) [store_named_vector](/docs/GeoNodes/socket_GEOMETRY.md#store_named_vector)

## Init

``` python
def __init__(self, geometry=None, selection=None, name=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeStoreNamedAttribute', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.name            = name
    self.value           = value
```
