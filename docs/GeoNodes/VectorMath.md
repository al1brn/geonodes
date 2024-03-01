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

- [Rot](/docs/GeoNodes/Rot.md) : [abs](/docs/GeoNodes/Rot.md#abs) [add](/docs/GeoNodes/Rot.md#add) [ceil](/docs/GeoNodes/Rot.md#ceil) [cos](/docs/GeoNodes/Rot.md#cos) [cross](/docs/GeoNodes/Rot.md#cross) [distance](/docs/GeoNodes/Rot.md#distance) [divide](/docs/GeoNodes/Rot.md#divide) [dot](/docs/GeoNodes/Rot.md#dot) [faceforward](/docs/GeoNodes/Rot.md#faceforward) [floor](/docs/GeoNodes/Rot.md#floor) [frac](/docs/GeoNodes/Rot.md#frac) [length](/docs/GeoNodes/Rot.md#length) [max](/docs/GeoNodes/Rot.md#max) [min](/docs/GeoNodes/Rot.md#min) [mod](/docs/GeoNodes/Rot.md#mod) [multiply](/docs/GeoNodes/Rot.md#multiply) [multiply_add](/docs/GeoNodes/Rot.md#multiply_add) [normalize](/docs/GeoNodes/Rot.md#normalize) [project](/docs/GeoNodes/Rot.md#project) [reflect](/docs/GeoNodes/Rot.md#reflect) [refract](/docs/GeoNodes/Rot.md#refract) [scale](/docs/GeoNodes/Rot.md#scale) [sin](/docs/GeoNodes/Rot.md#sin) [snap](/docs/GeoNodes/Rot.md#snap) [subtract](/docs/GeoNodes/Rot.md#subtract) [tan](/docs/GeoNodes/Rot.md#tan) [wrap](/docs/GeoNodes/Rot.md#wrap)
- [Vect](/docs/GeoNodes/Vect.md) : [abs](/docs/GeoNodes/Vect.md#abs) [add](/docs/GeoNodes/Vect.md#add) [ceil](/docs/GeoNodes/Vect.md#ceil) [cos](/docs/GeoNodes/Vect.md#cos) [cross](/docs/GeoNodes/Vect.md#cross) [distance](/docs/GeoNodes/Vect.md#distance) [divide](/docs/GeoNodes/Vect.md#divide) [dot](/docs/GeoNodes/Vect.md#dot) [faceforward](/docs/GeoNodes/Vect.md#faceforward) [floor](/docs/GeoNodes/Vect.md#floor) [frac](/docs/GeoNodes/Vect.md#frac) [length](/docs/GeoNodes/Vect.md#length) [max](/docs/GeoNodes/Vect.md#max) [min](/docs/GeoNodes/Vect.md#min) [mod](/docs/GeoNodes/Vect.md#mod) [multiply](/docs/GeoNodes/Vect.md#multiply) [multiply_add](/docs/GeoNodes/Vect.md#multiply_add) [normalize](/docs/GeoNodes/Vect.md#normalize) [project](/docs/GeoNodes/Vect.md#project) [reflect](/docs/GeoNodes/Vect.md#reflect) [refract](/docs/GeoNodes/Vect.md#refract) [scale](/docs/GeoNodes/Vect.md#scale) [sin](/docs/GeoNodes/Vect.md#sin) [snap](/docs/GeoNodes/Vect.md#snap) [subtract](/docs/GeoNodes/Vect.md#subtract) [tan](/docs/GeoNodes/Vect.md#tan) [wrap](/docs/GeoNodes/Vect.md#wrap)
- Functions : [vabs](/docs/GeoNodes/GeoNodesTree.md#vabs) [vadd](/docs/GeoNodes/GeoNodesTree.md#vadd) [vceil](/docs/GeoNodes/GeoNodesTree.md#vceil) [vcos](/docs/GeoNodes/GeoNodesTree.md#vcos) [vcross](/docs/GeoNodes/GeoNodesTree.md#vcross) [vdistance](/docs/GeoNodes/GeoNodesTree.md#vdistance) [vdivide](/docs/GeoNodes/GeoNodesTree.md#vdivide) [vdot](/docs/GeoNodes/GeoNodesTree.md#vdot) [vfaceforward](/docs/GeoNodes/GeoNodesTree.md#vfaceforward) [vfloor](/docs/GeoNodes/GeoNodesTree.md#vfloor) [vfrac](/docs/GeoNodes/GeoNodesTree.md#vfrac) [vlength](/docs/GeoNodes/GeoNodesTree.md#vlength) [vmax](/docs/GeoNodes/GeoNodesTree.md#vmax) [vmin](/docs/GeoNodes/GeoNodesTree.md#vmin) [vmod](/docs/GeoNodes/GeoNodesTree.md#vmod) [vmultiply](/docs/GeoNodes/GeoNodesTree.md#vmultiply) [vmultiply_add](/docs/GeoNodes/GeoNodesTree.md#vmultiply_add) [vnormalize](/docs/GeoNodes/GeoNodesTree.md#vnormalize) [vproject](/docs/GeoNodes/GeoNodesTree.md#vproject) [vreflect](/docs/GeoNodes/GeoNodesTree.md#vreflect) [vrefract](/docs/GeoNodes/GeoNodesTree.md#vrefract) [vscale](/docs/GeoNodes/GeoNodesTree.md#vscale) [vsin](/docs/GeoNodes/GeoNodesTree.md#vsin) [vsnap](/docs/GeoNodes/GeoNodesTree.md#vsnap) [vsubtract](/docs/GeoNodes/GeoNodesTree.md#vsubtract) [vtan](/docs/GeoNodes/GeoNodesTree.md#vtan) [vwrap](/docs/GeoNodes/GeoNodesTree.md#vwrap)

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
