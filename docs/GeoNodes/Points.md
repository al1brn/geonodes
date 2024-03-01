# Node Points

- Node name : 'Points'
- bl_idname : [Points](https://docs.blender.org/api/current/bpy.types.Points.html)


``` python
Points(count=None, position=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- count : None
- position : None
- radius : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, count=None, position=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodePoints', node_label=node_label, node_color=node_color)

    self.count           = count
    self.position        = position
    self.radius          = radius
```
