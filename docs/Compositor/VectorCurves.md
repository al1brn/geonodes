# Node VectorCurves

- Node name : 'Vector Curves'
- bl_idname : [CompositorNodeCurveVec](https://docs.blender.org/api/current/bpy.types.CompositorNodeCurveVec.html)


``` python
VectorCurves(vector=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- mapping : None
- tag_need_exec : None

## Implementation

- [VECTOR](/docs/Compositor/socket_VECTOR.md) : [vector_curves](/docs/Compositor/socket_VECTOR.md#vector_curves)

## Init

``` python
def __init__(self, vector=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeCurveVec', node_label=node_label, node_color=node_color, **kwargs)

    self.mapping         = mapping
    self.tag_need_exec   = tag_need_exec
    self.vector          = vector
```
