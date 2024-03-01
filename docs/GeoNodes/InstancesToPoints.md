# Node InstancesToPoints

- Node name : 'Instances to Points'
- bl_idname : GeometryNodeInstancesToPoints


``` python
InstancesToPoints(instances=None, selection=None, position=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- instances : None
- selection : None
- position : None
- radius : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [instances_to_points](/docs/GeoNodes/Geometry.md#instances_to_points)

## Init

``` python
def __init__(self, instances=None, selection=None, position=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInstancesToPoints', node_label=node_label, node_color=node_color)

    self.instances       = instances
    self.selection       = selection
    self.position        = position
    self.radius          = radius
```
