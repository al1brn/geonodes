# Node Quadrilateral

- Node name : 'Quadrilateral'
- bl_idname : [GeometryNodeCurvePrimitiveQuadrilateral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)


``` python
Quadrilateral(width=None, height=None, offset=None, bottom_width=None, top_width=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- width : None
- height : None
- offset : None
- bottom_width : None
- top_width : None
- bottom_height : None
- top_height : None
- point_1 : None
- point_2 : None
- point_3 : None
- point_4 : None
- mode : 'RECTANGLE'

## Implementation

- Functions : [quadrilateral](/docs/GeoNodes/GeoNodesTree.md#quadrilateral)

## Init

``` python
def __init__(self, width=None, height=None, offset=None, bottom_width=None, top_width=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurvePrimitiveQuadrilateral', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.width           = width
    self.height          = height
    self.offset          = offset
    self.bottom_width    = bottom_width
    self.top_width       = top_width
    self.bottom_height   = bottom_height
    self.top_height      = top_height
    self.point_1         = point_1
    self.point_2         = point_2
    self.point_3         = point_3
    self.point_4         = point_4
```
