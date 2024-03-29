# Node AttributeStatistic

- Node name : 'Attribute Statistic'
- bl_idname : [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)


``` python
AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- attribute : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [attribute_statistic](/docs/GeoNodes/socket_GEOMETRY.md#attribute_statistic) [attribute_statistic_float](/docs/GeoNodes/socket_GEOMETRY.md#attribute_statistic_float) [attribute_statistic_vector](/docs/GeoNodes/socket_GEOMETRY.md#attribute_statistic_vector)

## Init

``` python
def __init__(self, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeAttributeStatistic', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.attribute       = attribute
```
