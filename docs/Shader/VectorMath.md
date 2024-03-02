# Node VectorMath

- Node name : 'Vector Math'
- bl_idname : [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)


``` python
VectorMath(vector=None, vector_1=None, vector_2=None, scale=None, operation='ADD', node_label=None, node_color=None)
```
##### Arguments

- vector : None
- vector_1 : None
- vector_2 : None
- scale : None
- operation : 'ADD'

## Implementation

- [ROTATION](/docs/Shader/ROTATION.md) : [abs](/docs/Shader/ROTATION.md#abs) [add](/docs/Shader/ROTATION.md#add) [ceil](/docs/Shader/ROTATION.md#ceil) [cos](/docs/Shader/ROTATION.md#cos) [cross](/docs/Shader/ROTATION.md#cross) [distance](/docs/Shader/ROTATION.md#distance) [divide](/docs/Shader/ROTATION.md#divide) [dot](/docs/Shader/ROTATION.md#dot) [faceforward](/docs/Shader/ROTATION.md#faceforward) [floor](/docs/Shader/ROTATION.md#floor) [frac](/docs/Shader/ROTATION.md#frac) [length](/docs/Shader/ROTATION.md#length) [max](/docs/Shader/ROTATION.md#max) [min](/docs/Shader/ROTATION.md#min) [mod](/docs/Shader/ROTATION.md#mod) [multiply](/docs/Shader/ROTATION.md#multiply) [multiply_add](/docs/Shader/ROTATION.md#multiply_add) [normalize](/docs/Shader/ROTATION.md#normalize) [project](/docs/Shader/ROTATION.md#project) [reflect](/docs/Shader/ROTATION.md#reflect) [refract](/docs/Shader/ROTATION.md#refract) [scale](/docs/Shader/ROTATION.md#scale) [sin](/docs/Shader/ROTATION.md#sin) [snap](/docs/Shader/ROTATION.md#snap) [subtract](/docs/Shader/ROTATION.md#subtract) [tan](/docs/Shader/ROTATION.md#tan) [wrap](/docs/Shader/ROTATION.md#wrap)
- [VECTOR](/docs/Shader/VECTOR.md) : [abs](/docs/Shader/VECTOR.md#abs) [add](/docs/Shader/VECTOR.md#add) [ceil](/docs/Shader/VECTOR.md#ceil) [cos](/docs/Shader/VECTOR.md#cos) [cross](/docs/Shader/VECTOR.md#cross) [distance](/docs/Shader/VECTOR.md#distance) [divide](/docs/Shader/VECTOR.md#divide) [dot](/docs/Shader/VECTOR.md#dot) [faceforward](/docs/Shader/VECTOR.md#faceforward) [floor](/docs/Shader/VECTOR.md#floor) [frac](/docs/Shader/VECTOR.md#frac) [length](/docs/Shader/VECTOR.md#length) [max](/docs/Shader/VECTOR.md#max) [min](/docs/Shader/VECTOR.md#min) [mod](/docs/Shader/VECTOR.md#mod) [multiply](/docs/Shader/VECTOR.md#multiply) [multiply_add](/docs/Shader/VECTOR.md#multiply_add) [normalize](/docs/Shader/VECTOR.md#normalize) [project](/docs/Shader/VECTOR.md#project) [reflect](/docs/Shader/VECTOR.md#reflect) [refract](/docs/Shader/VECTOR.md#refract) [scale](/docs/Shader/VECTOR.md#scale) [sin](/docs/Shader/VECTOR.md#sin) [snap](/docs/Shader/VECTOR.md#snap) [subtract](/docs/Shader/VECTOR.md#subtract) [tan](/docs/Shader/VECTOR.md#tan) [wrap](/docs/Shader/VECTOR.md#wrap)
- Functions : [vabs](/docs/Shader/ShaderTree.md#vabs) [vadd](/docs/Shader/ShaderTree.md#vadd) [vceil](/docs/Shader/ShaderTree.md#vceil) [vcos](/docs/Shader/ShaderTree.md#vcos) [vcross](/docs/Shader/ShaderTree.md#vcross) [vdistance](/docs/Shader/ShaderTree.md#vdistance) [vdivide](/docs/Shader/ShaderTree.md#vdivide) [vdot](/docs/Shader/ShaderTree.md#vdot) [vfaceforward](/docs/Shader/ShaderTree.md#vfaceforward) [vfloor](/docs/Shader/ShaderTree.md#vfloor) [vfrac](/docs/Shader/ShaderTree.md#vfrac) [vlength](/docs/Shader/ShaderTree.md#vlength) [vmax](/docs/Shader/ShaderTree.md#vmax) [vmin](/docs/Shader/ShaderTree.md#vmin) [vmod](/docs/Shader/ShaderTree.md#vmod) [vmultiply](/docs/Shader/ShaderTree.md#vmultiply) [vmultiply_add](/docs/Shader/ShaderTree.md#vmultiply_add) [vnormalize](/docs/Shader/ShaderTree.md#vnormalize) [vproject](/docs/Shader/ShaderTree.md#vproject) [vreflect](/docs/Shader/ShaderTree.md#vreflect) [vrefract](/docs/Shader/ShaderTree.md#vrefract) [vscale](/docs/Shader/ShaderTree.md#vscale) [vsin](/docs/Shader/ShaderTree.md#vsin) [vsnap](/docs/Shader/ShaderTree.md#vsnap) [vsubtract](/docs/Shader/ShaderTree.md#vsubtract) [vtan](/docs/Shader/ShaderTree.md#vtan) [vwrap](/docs/Shader/ShaderTree.md#vwrap)

## Init

``` python
def __init__(self, vector=None, vector_1=None, vector_2=None, scale=None, operation='ADD', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeVectorMath', node_label=node_label, node_color=node_color)

    self.operation       = operation
    self.vector          = vector
    self.vector_1        = vector_1
    self.vector_2        = vector_2
    self.scale           = scale
```
