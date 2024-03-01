# Node VectorMath

- Node name : 'Vector Math'
- bl_idname : ShaderNodeVectorMath


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

- [Rot](/docs/GeoNodes/Rot.md) : [abs](/docs/GeoNodes/Rot.md#abs) [add](/docs/GeoNodes/Rot.md#add) [ceil](/docs/GeoNodes/Rot.md#ceil) [cos](/docs/GeoNodes/Rot.md#cos) [cross](/docs/GeoNodes/Rot.md#cross) [distance](/docs/GeoNodes/Rot.md#distance) [divide](/docs/GeoNodes/Rot.md#divide) [dot](/docs/GeoNodes/Rot.md#dot) [faceforward](/docs/GeoNodes/Rot.md#faceforward) [floor](/docs/GeoNodes/Rot.md#floor) [frac](/docs/GeoNodes/Rot.md#frac) [length](/docs/GeoNodes/Rot.md#length) [max](/docs/GeoNodes/Rot.md#max) [min](/docs/GeoNodes/Rot.md#min) [mod](/docs/GeoNodes/Rot.md#mod) [multiply](/docs/GeoNodes/Rot.md#multiply) [multiply_add](/docs/GeoNodes/Rot.md#multiply_add) [normalize](/docs/GeoNodes/Rot.md#normalize) [project](/docs/GeoNodes/Rot.md#project) [reflect](/docs/GeoNodes/Rot.md#reflect) [refract](/docs/GeoNodes/Rot.md#refract) [scale](/docs/GeoNodes/Rot.md#scale) [sin](/docs/GeoNodes/Rot.md#sin) [snap](/docs/GeoNodes/Rot.md#snap) [subtract](/docs/GeoNodes/Rot.md#subtract) [tan](/docs/GeoNodes/Rot.md#tan) [wrap](/docs/GeoNodes/Rot.md#wrap)
- [Vect](/docs/GeoNodes/Vect.md) : [abs](/docs/GeoNodes/Vect.md#abs) [add](/docs/GeoNodes/Vect.md#add) [ceil](/docs/GeoNodes/Vect.md#ceil) [cos](/docs/GeoNodes/Vect.md#cos) [cross](/docs/GeoNodes/Vect.md#cross) [distance](/docs/GeoNodes/Vect.md#distance) [divide](/docs/GeoNodes/Vect.md#divide) [dot](/docs/GeoNodes/Vect.md#dot) [faceforward](/docs/GeoNodes/Vect.md#faceforward) [floor](/docs/GeoNodes/Vect.md#floor) [frac](/docs/GeoNodes/Vect.md#frac) [length](/docs/GeoNodes/Vect.md#length) [max](/docs/GeoNodes/Vect.md#max) [min](/docs/GeoNodes/Vect.md#min) [mod](/docs/GeoNodes/Vect.md#mod) [multiply](/docs/GeoNodes/Vect.md#multiply) [multiply_add](/docs/GeoNodes/Vect.md#multiply_add) [normalize](/docs/GeoNodes/Vect.md#normalize) [project](/docs/GeoNodes/Vect.md#project) [reflect](/docs/GeoNodes/Vect.md#reflect) [refract](/docs/GeoNodes/Vect.md#refract) [scale](/docs/GeoNodes/Vect.md#scale) [sin](/docs/GeoNodes/Vect.md#sin) [snap](/docs/GeoNodes/Vect.md#snap) [subtract](/docs/GeoNodes/Vect.md#subtract) [tan](/docs/GeoNodes/Vect.md#tan) [wrap](/docs/GeoNodes/Vect.md#wrap)
- Functions : [vabs](/docs/GeoNodes/GeoNodes.md#vabs) [vadd](/docs/GeoNodes/GeoNodes.md#vadd) [vceil](/docs/GeoNodes/GeoNodes.md#vceil) [vcos](/docs/GeoNodes/GeoNodes.md#vcos) [vcross](/docs/GeoNodes/GeoNodes.md#vcross) [vdistance](/docs/GeoNodes/GeoNodes.md#vdistance) [vdivide](/docs/GeoNodes/GeoNodes.md#vdivide) [vdot](/docs/GeoNodes/GeoNodes.md#vdot) [vfaceforward](/docs/GeoNodes/GeoNodes.md#vfaceforward) [vfloor](/docs/GeoNodes/GeoNodes.md#vfloor) [vfrac](/docs/GeoNodes/GeoNodes.md#vfrac) [vlength](/docs/GeoNodes/GeoNodes.md#vlength) [vmax](/docs/GeoNodes/GeoNodes.md#vmax) [vmin](/docs/GeoNodes/GeoNodes.md#vmin) [vmod](/docs/GeoNodes/GeoNodes.md#vmod) [vmultiply](/docs/GeoNodes/GeoNodes.md#vmultiply) [vmultiply_add](/docs/GeoNodes/GeoNodes.md#vmultiply_add) [vnormalize](/docs/GeoNodes/GeoNodes.md#vnormalize) [vproject](/docs/GeoNodes/GeoNodes.md#vproject) [vreflect](/docs/GeoNodes/GeoNodes.md#vreflect) [vrefract](/docs/GeoNodes/GeoNodes.md#vrefract) [vscale](/docs/GeoNodes/GeoNodes.md#vscale) [vsin](/docs/GeoNodes/GeoNodes.md#vsin) [vsnap](/docs/GeoNodes/GeoNodes.md#vsnap) [vsubtract](/docs/GeoNodes/GeoNodes.md#vsubtract) [vtan](/docs/GeoNodes/GeoNodes.md#vtan) [vwrap](/docs/GeoNodes/GeoNodes.md#vwrap)

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
