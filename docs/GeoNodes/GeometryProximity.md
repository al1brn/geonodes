# Node GeometryProximity

- Node name : 'Geometry Proximity'
- bl_idname : [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)


``` python
GeometryProximity(target=None, source_position=None, target_element='FACES', node_label=None, node_color=None)
```
##### Arguments

- target : None
- source_position : None
- target_element : 'FACES'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [geometry_proximity](/docs/GeoNodes/socket_GEOMETRY.md#geometry_proximity) [geometry_proximity](/docs/GeoNodes/socket_GEOMETRY.md#geometry_proximity)

## Init

``` python
def __init__(self, target=None, source_position=None, target_element='FACES', node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeProximity', node_label=node_label, node_color=node_color)

    self.target_element  = target_element
    self.target          = target
    self.source_position = source_position
```
