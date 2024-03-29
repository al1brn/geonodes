# Node VectorMath

- Node name : 'Vector Math'
- bl_idname : [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)


``` python
VectorMath(vector=None, vector_1=None, vector_2=None, scale=None, operation='ADD', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- vector_1 : None
- vector_2 : None
- scale : None
- operation : 'ADD'

## Implementation

- [ROTATION](/docs/Shader/socket_ROTATION.md) : [abs](/docs/Shader/socket_ROTATION.md#abs) [add](/docs/Shader/socket_ROTATION.md#add) [ceil](/docs/Shader/socket_ROTATION.md#ceil) [cos](/docs/Shader/socket_ROTATION.md#cos) [cross](/docs/Shader/socket_ROTATION.md#cross) [distance](/docs/Shader/socket_ROTATION.md#distance) [divide](/docs/Shader/socket_ROTATION.md#divide) [dot](/docs/Shader/socket_ROTATION.md#dot) [faceforward](/docs/Shader/socket_ROTATION.md#faceforward) [floor](/docs/Shader/socket_ROTATION.md#floor) [frac](/docs/Shader/socket_ROTATION.md#frac) [length](/docs/Shader/socket_ROTATION.md#length) [max](/docs/Shader/socket_ROTATION.md#max) [min](/docs/Shader/socket_ROTATION.md#min) [mod](/docs/Shader/socket_ROTATION.md#mod) [multiply](/docs/Shader/socket_ROTATION.md#multiply) [multiply_add](/docs/Shader/socket_ROTATION.md#multiply_add) [normalize](/docs/Shader/socket_ROTATION.md#normalize) [project](/docs/Shader/socket_ROTATION.md#project) [reflect](/docs/Shader/socket_ROTATION.md#reflect) [refract](/docs/Shader/socket_ROTATION.md#refract) [scale](/docs/Shader/socket_ROTATION.md#scale) [sin](/docs/Shader/socket_ROTATION.md#sin) [snap](/docs/Shader/socket_ROTATION.md#snap) [subtract](/docs/Shader/socket_ROTATION.md#subtract) [tan](/docs/Shader/socket_ROTATION.md#tan) [wrap](/docs/Shader/socket_ROTATION.md#wrap)
- [VECTOR](/docs/Shader/socket_VECTOR.md) : [abs](/docs/Shader/socket_VECTOR.md#abs) [add](/docs/Shader/socket_VECTOR.md#add) [ceil](/docs/Shader/socket_VECTOR.md#ceil) [cos](/docs/Shader/socket_VECTOR.md#cos) [cross](/docs/Shader/socket_VECTOR.md#cross) [distance](/docs/Shader/socket_VECTOR.md#distance) [divide](/docs/Shader/socket_VECTOR.md#divide) [dot](/docs/Shader/socket_VECTOR.md#dot) [faceforward](/docs/Shader/socket_VECTOR.md#faceforward) [floor](/docs/Shader/socket_VECTOR.md#floor) [frac](/docs/Shader/socket_VECTOR.md#frac) [length](/docs/Shader/socket_VECTOR.md#length) [max](/docs/Shader/socket_VECTOR.md#max) [min](/docs/Shader/socket_VECTOR.md#min) [mod](/docs/Shader/socket_VECTOR.md#mod) [multiply](/docs/Shader/socket_VECTOR.md#multiply) [multiply_add](/docs/Shader/socket_VECTOR.md#multiply_add) [normalize](/docs/Shader/socket_VECTOR.md#normalize) [project](/docs/Shader/socket_VECTOR.md#project) [reflect](/docs/Shader/socket_VECTOR.md#reflect) [refract](/docs/Shader/socket_VECTOR.md#refract) [scale](/docs/Shader/socket_VECTOR.md#scale) [sin](/docs/Shader/socket_VECTOR.md#sin) [snap](/docs/Shader/socket_VECTOR.md#snap) [subtract](/docs/Shader/socket_VECTOR.md#subtract) [tan](/docs/Shader/socket_VECTOR.md#tan) [wrap](/docs/Shader/socket_VECTOR.md#wrap)
- Functions : [vabs](/docs/Shader/ShaderTree.md#vabs) [vadd](/docs/Shader/ShaderTree.md#vadd) [vceil](/docs/Shader/ShaderTree.md#vceil) [vcos](/docs/Shader/ShaderTree.md#vcos) [vcross](/docs/Shader/ShaderTree.md#vcross) [vdistance](/docs/Shader/ShaderTree.md#vdistance) [vdivide](/docs/Shader/ShaderTree.md#vdivide) [vdot](/docs/Shader/ShaderTree.md#vdot) [vfaceforward](/docs/Shader/ShaderTree.md#vfaceforward) [vfloor](/docs/Shader/ShaderTree.md#vfloor) [vfrac](/docs/Shader/ShaderTree.md#vfrac) [vlength](/docs/Shader/ShaderTree.md#vlength) [vmax](/docs/Shader/ShaderTree.md#vmax) [vmin](/docs/Shader/ShaderTree.md#vmin) [vmod](/docs/Shader/ShaderTree.md#vmod) [vmultiply](/docs/Shader/ShaderTree.md#vmultiply) [vmultiply_add](/docs/Shader/ShaderTree.md#vmultiply_add) [vnormalize](/docs/Shader/ShaderTree.md#vnormalize) [vproject](/docs/Shader/ShaderTree.md#vproject) [vreflect](/docs/Shader/ShaderTree.md#vreflect) [vrefract](/docs/Shader/ShaderTree.md#vrefract) [vscale](/docs/Shader/ShaderTree.md#vscale) [vsin](/docs/Shader/ShaderTree.md#vsin) [vsnap](/docs/Shader/ShaderTree.md#vsnap) [vsubtract](/docs/Shader/ShaderTree.md#vsubtract) [vtan](/docs/Shader/ShaderTree.md#vtan) [vwrap](/docs/Shader/ShaderTree.md#vwrap)

## Init

``` python
def __init__(self, vector=None, vector_1=None, vector_2=None, scale=None, operation='ADD', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVectorMath', node_label=node_label, node_color=node_color, **kwargs)

    self.operation       = operation
    self.vector          = vector
    self.vector_1        = vector_1
    self.vector_2        = vector_2
    self.scale           = scale
```
