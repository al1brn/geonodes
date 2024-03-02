# Node InstancesToPoints

- Node name : 'Instances to Points'
- bl_idname : [GeometryNodeInstancesToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)


``` python
InstancesToPoints(instances=None, selection=None, position=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- instances : None
- selection : None
- position : None
- radius : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [instances_to_points](/docs/GeoNodes/socket_GEOMETRY.md#instances_to_points) [instances_to_points](/docs/GeoNodes/socket_GEOMETRY.md#instances_to_points)

## Init

``` python
def __init__(self, instances=None, selection=None, position=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInstancesToPoints', node_label=node_label, node_color=node_color)

    self.instances       = instances
    self.selection       = selection
    self.position        = position
    self.radius          = radius
```
