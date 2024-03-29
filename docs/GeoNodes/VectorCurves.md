# Node VectorCurves

- Node name : 'Vector Curves'
- bl_idname : [ShaderNodeVectorCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)


``` python
VectorCurves(fac=None, vector=None, mapping=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- vector : None
- mapping : None

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [vector_curves](/docs/GeoNodes/socket_ROTATION.md#vector_curves)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [vector_curves](/docs/GeoNodes/socket_VECTOR.md#vector_curves)

## Init

``` python
def __init__(self, fac=None, vector=None, mapping=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVectorCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.mapping         = mapping
    self.fac             = fac
    self.vector          = vector
```
