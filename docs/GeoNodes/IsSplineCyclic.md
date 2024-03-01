# Node IsSplineCyclic

- Node name : 'Is Spline Cyclic'
- bl_idname : [Is Spline Cyclic](https://docs.blender.org/api/current/bpy.types.Is Spline Cyclic.html)


``` python
IsSplineCyclic(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [spline_cyclic](/docs/GeoNodes/Geometry.md#spline_cyclic)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputSplineCyclic', node_label=node_label, node_color=node_color)
```
