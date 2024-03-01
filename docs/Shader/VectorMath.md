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

- [Rot](/docs/Shader/Rot.md) : [abs](/docs/Shader/Rot.md#abs) [add](/docs/Shader/Rot.md#add) [ceil](/docs/Shader/Rot.md#ceil) [cos](/docs/Shader/Rot.md#cos) [cross](/docs/Shader/Rot.md#cross) [distance](/docs/Shader/Rot.md#distance) [divide](/docs/Shader/Rot.md#divide) [dot](/docs/Shader/Rot.md#dot) [faceforward](/docs/Shader/Rot.md#faceforward) [floor](/docs/Shader/Rot.md#floor) [frac](/docs/Shader/Rot.md#frac) [length](/docs/Shader/Rot.md#length) [max](/docs/Shader/Rot.md#max) [min](/docs/Shader/Rot.md#min) [mod](/docs/Shader/Rot.md#mod) [multiply](/docs/Shader/Rot.md#multiply) [multiply_add](/docs/Shader/Rot.md#multiply_add) [normalize](/docs/Shader/Rot.md#normalize) [project](/docs/Shader/Rot.md#project) [reflect](/docs/Shader/Rot.md#reflect) [refract](/docs/Shader/Rot.md#refract) [scale](/docs/Shader/Rot.md#scale) [sin](/docs/Shader/Rot.md#sin) [snap](/docs/Shader/Rot.md#snap) [subtract](/docs/Shader/Rot.md#subtract) [tan](/docs/Shader/Rot.md#tan) [wrap](/docs/Shader/Rot.md#wrap)
- [Vect](/docs/Shader/Vect.md) : [abs](/docs/Shader/Vect.md#abs) [add](/docs/Shader/Vect.md#add) [ceil](/docs/Shader/Vect.md#ceil) [cos](/docs/Shader/Vect.md#cos) [cross](/docs/Shader/Vect.md#cross) [distance](/docs/Shader/Vect.md#distance) [divide](/docs/Shader/Vect.md#divide) [dot](/docs/Shader/Vect.md#dot) [faceforward](/docs/Shader/Vect.md#faceforward) [floor](/docs/Shader/Vect.md#floor) [frac](/docs/Shader/Vect.md#frac) [length](/docs/Shader/Vect.md#length) [max](/docs/Shader/Vect.md#max) [min](/docs/Shader/Vect.md#min) [mod](/docs/Shader/Vect.md#mod) [multiply](/docs/Shader/Vect.md#multiply) [multiply_add](/docs/Shader/Vect.md#multiply_add) [normalize](/docs/Shader/Vect.md#normalize) [project](/docs/Shader/Vect.md#project) [reflect](/docs/Shader/Vect.md#reflect) [refract](/docs/Shader/Vect.md#refract) [scale](/docs/Shader/Vect.md#scale) [sin](/docs/Shader/Vect.md#sin) [snap](/docs/Shader/Vect.md#snap) [subtract](/docs/Shader/Vect.md#subtract) [tan](/docs/Shader/Vect.md#tan) [wrap](/docs/Shader/Vect.md#wrap)
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
