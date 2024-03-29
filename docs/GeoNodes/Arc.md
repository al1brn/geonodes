# Node Arc

- Node name : 'Arc'
- bl_idname : [GeometryNodeCurveArc](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)


``` python
Arc(resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, start=None, middle=None, end=None, offset_angle=None, mode='RADIUS', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- resolution : None
- radius : None
- start_angle : None
- sweep_angle : None
- connect_center : None
- invert_arc : None
- start : None
- middle : None
- end : None
- offset_angle : None
- mode : 'RADIUS'

## Implementation

- Functions : [arc](/docs/GeoNodes/GeoNodesTree.md#arc)

## Init

``` python
def __init__(self, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, start=None, middle=None, end=None, offset_angle=None, mode='RADIUS', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveArc', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.resolution      = resolution
    self.radius          = radius
    self.start_angle     = start_angle
    self.sweep_angle     = sweep_angle
    self.connect_center  = connect_center
    self.invert_arc      = invert_arc
    self.start           = start
    self.middle          = middle
    self.end             = end
    self.offset_angle    = offset_angle
```
