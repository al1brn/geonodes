# Node Points

- Node name : 'Points'
- bl_idname : [GeometryNodePoints](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)


``` python
Points(count=None, position=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- count : None
- position : None
- radius : None

## Implementation

- Functions : [points](/docs/GeoNodes/GeoNodesTree.md#points)

## Init

``` python
def __init__(self, count=None, position=None, radius=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodePoints', node_label=node_label, node_color=node_color)

    self.count           = count
    self.position        = position
    self.radius          = radius
```
