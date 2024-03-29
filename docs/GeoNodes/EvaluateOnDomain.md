# Node EvaluateOnDomain

- Node name : 'Evaluate on Domain'
- bl_idname : [GeometryNodeFieldOnDomain](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)


``` python
EvaluateOnDomain(value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [evaluate_on_domain](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain) [evaluate_on_domain_boolean](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain_boolean) [evaluate_on_domain_color](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain_color) [evaluate_on_domain_float](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain_float) [evaluate_on_domain_int](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain_int) [evaluate_on_domain_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain_quaternion) [evaluate_on_domain_vector](/docs/GeoNodes/socket_GEOMETRY.md#evaluate_on_domain_vector)

## Init

``` python
def __init__(self, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeFieldOnDomain', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.domain          = domain
    self.value           = value
```
