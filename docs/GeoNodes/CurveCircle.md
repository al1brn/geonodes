# Node CurveCircle

- Node name : 'Curve Circle'
- bl_idname : [GeometryNodeCurvePrimitiveCircle](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)


``` python
CurveCircle(resolution=None, radius=None, point_1=None, point_2=None, point_3=None, mode='RADIUS', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- resolution : None
- radius : None
- point_1 : None
- point_2 : None
- point_3 : None
- mode : 'RADIUS'

## Implementation

- Functions : [curve_circle](/docs/GeoNodes/GeoNodesTree.md#curve_circle)

## Init

``` python
def __init__(self, resolution=None, radius=None, point_1=None, point_2=None, point_3=None, mode='RADIUS', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurvePrimitiveCircle', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.resolution      = resolution
    self.radius          = radius
    self.point_1         = point_1
    self.point_2         = point_2
    self.point_3         = point_3
```
