# Node EvaluateOnDomain

- Node name : 'Evaluate on Domain'
- bl_idname : [Evaluate on Domain](https://docs.blender.org/api/current/bpy.types.Evaluate on Domain.html)


``` python
EvaluateOnDomain(value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- value : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [evaluate_on_domain](/docs/GeoNodes/Geometry.md#evaluate_on_domain) [evaluate_on_domain_boolean](/docs/GeoNodes/Geometry.md#evaluate_on_domain_boolean) [evaluate_on_domain_color](/docs/GeoNodes/Geometry.md#evaluate_on_domain_color) [evaluate_on_domain_float](/docs/GeoNodes/Geometry.md#evaluate_on_domain_float) [evaluate_on_domain_int](/docs/GeoNodes/Geometry.md#evaluate_on_domain_int) [evaluate_on_domain_quaternion](/docs/GeoNodes/Geometry.md#evaluate_on_domain_quaternion) [evaluate_on_domain_vector](/docs/GeoNodes/Geometry.md#evaluate_on_domain_vector)

## Init

``` python
def __init__(self, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeFieldOnDomain', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.domain          = domain
    self.value           = value
```
