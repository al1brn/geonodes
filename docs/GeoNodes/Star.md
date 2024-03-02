# Node Star

- Node name : 'Star'
- bl_idname : [GeometryNodeCurveStar](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)


``` python
Star(points=None, inner_radius=None, outer_radius=None, twist=None, node_label=None, node_color=None)
```
##### Arguments

- points : None
- inner_radius : None
- outer_radius : None
- twist : None

## Implementation

- Functions : [star](/docs/GeoNodes/GeoNodesTree.md#star) [star](/docs/GeoNodes/GeoNodesTree.md#star)

## Init

``` python
def __init__(self, points=None, inner_radius=None, outer_radius=None, twist=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveStar', node_label=node_label, node_color=node_color)

    self.points          = points
    self.inner_radius    = inner_radius
    self.outer_radius    = outer_radius
    self.twist           = twist
```
