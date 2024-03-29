# Node IsSplineCyclic

- Node name : 'Is Spline Cyclic'
- bl_idname : [GeometryNodeInputSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)


``` python
IsSplineCyclic(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [spline_cyclic](/docs/GeoNodes/socket_GEOMETRY.md#spline_cyclic)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputSplineCyclic', node_label=node_label, node_color=node_color, **kwargs)
```
