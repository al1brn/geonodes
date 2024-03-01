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
- Functions : [vabs](/docs/Shader/Shader.md#vabs) [vadd](/docs/Shader/Shader.md#vadd) [vceil](/docs/Shader/Shader.md#vceil) [vcos](/docs/Shader/Shader.md#vcos) [vcross](/docs/Shader/Shader.md#vcross) [vdistance](/docs/Shader/Shader.md#vdistance) [vdivide](/docs/Shader/Shader.md#vdivide) [vdot](/docs/Shader/Shader.md#vdot) [vfaceforward](/docs/Shader/Shader.md#vfaceforward) [vfloor](/docs/Shader/Shader.md#vfloor) [vfrac](/docs/Shader/Shader.md#vfrac) [vlength](/docs/Shader/Shader.md#vlength) [vmax](/docs/Shader/Shader.md#vmax) [vmin](/docs/Shader/Shader.md#vmin) [vmod](/docs/Shader/Shader.md#vmod) [vmultiply](/docs/Shader/Shader.md#vmultiply) [vmultiply_add](/docs/Shader/Shader.md#vmultiply_add) [vnormalize](/docs/Shader/Shader.md#vnormalize) [vproject](/docs/Shader/Shader.md#vproject) [vreflect](/docs/Shader/Shader.md#vreflect) [vrefract](/docs/Shader/Shader.md#vrefract) [vscale](/docs/Shader/Shader.md#vscale) [vsin](/docs/Shader/Shader.md#vsin) [vsnap](/docs/Shader/Shader.md#vsnap) [vsubtract](/docs/Shader/Shader.md#vsubtract) [vtan](/docs/Shader/Shader.md#vtan) [vwrap](/docs/Shader/Shader.md#vwrap)

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
