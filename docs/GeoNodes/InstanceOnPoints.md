# Node InstanceOnPoints

- Node name : 'Instance on Points'
- bl_idname : [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)


``` python
InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- points : None
- selection : None
- instance : None
- pick_instance : None
- instance_index : None
- rotation : None
- scale : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [instance_on_points](/docs/GeoNodes/socket_GEOMETRY.md#instance_on_points)

## Init

``` python
def __init__(self, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInstanceOnPoints', node_label=node_label, node_color=node_color, **kwargs)

    self.points          = points
    self.selection       = selection
    self.instance        = instance
    self.pick_instance   = pick_instance
    self.instance_index  = instance_index
    self.rotation        = rotation
    self.scale           = scale
```
