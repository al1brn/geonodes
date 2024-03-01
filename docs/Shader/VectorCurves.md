# Node VectorCurves

- Node name : 'Vector Curves'
- bl_idname : [ShaderNodeVectorCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)


``` python
VectorCurves(fac=None, vector=None, mapping=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- vector : None
- mapping : None

## Implementation

- [Rot](/docs/Shader/Rot.md) : [vector_curves](/docs/Shader/Rot.md#vector_curves)
- [Vect](/docs/Shader/Vect.md) : [vector_curves](/docs/Shader/Vect.md#vector_curves)

## Init

``` python
def __init__(self, fac=None, vector=None, mapping=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeVectorCurve', node_label=node_label, node_color=node_color)

    self.mapping         = mapping
    self.fac             = fac
    self.vector          = vector
```
