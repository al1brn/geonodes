# Node Normal

- Node name : 'Normal'
- bl_idname : [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Normal(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [normal](/docs/GeoNodes/Geometry.md#normal)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputNormal', node_label=node_label, node_color=node_color)
```
