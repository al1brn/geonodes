# Node GeometryProximity

- Node name : 'Geometry Proximity'
- bl_idname : [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)


``` python
GeometryProximity(geometry=None, sample_position=None, target_element='FACES', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- sample_position : None
- target_element : 'FACES'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [geometry_proximity](/docs/GeoNodes/socket_GEOMETRY.md#geometry_proximity)

## Init

``` python
def __init__(self, geometry=None, sample_position=None, target_element='FACES', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeProximity', node_label=node_label, node_color=node_color, **kwargs)

    self.target_element  = target_element
    self.geometry        = geometry
    self.sample_position = sample_position
```
