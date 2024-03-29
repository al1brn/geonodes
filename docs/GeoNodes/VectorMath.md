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

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [abs](/docs/GeoNodes/socket_ROTATION.md#abs) [add](/docs/GeoNodes/socket_ROTATION.md#add) [ceil](/docs/GeoNodes/socket_ROTATION.md#ceil) [cos](/docs/GeoNodes/socket_ROTATION.md#cos) [cross](/docs/GeoNodes/socket_ROTATION.md#cross) [distance](/docs/GeoNodes/socket_ROTATION.md#distance) [divide](/docs/GeoNodes/socket_ROTATION.md#divide) [dot](/docs/GeoNodes/socket_ROTATION.md#dot) [faceforward](/docs/GeoNodes/socket_ROTATION.md#faceforward) [floor](/docs/GeoNodes/socket_ROTATION.md#floor) [frac](/docs/GeoNodes/socket_ROTATION.md#frac) [length](/docs/GeoNodes/socket_ROTATION.md#length) [max](/docs/GeoNodes/socket_ROTATION.md#max) [min](/docs/GeoNodes/socket_ROTATION.md#min) [mod](/docs/GeoNodes/socket_ROTATION.md#mod) [multiply](/docs/GeoNodes/socket_ROTATION.md#multiply) [multiply_add](/docs/GeoNodes/socket_ROTATION.md#multiply_add) [normalize](/docs/GeoNodes/socket_ROTATION.md#normalize) [project](/docs/GeoNodes/socket_ROTATION.md#project) [reflect](/docs/GeoNodes/socket_ROTATION.md#reflect) [refract](/docs/GeoNodes/socket_ROTATION.md#refract) [scale](/docs/GeoNodes/socket_ROTATION.md#scale) [sin](/docs/GeoNodes/socket_ROTATION.md#sin) [snap](/docs/GeoNodes/socket_ROTATION.md#snap) [subtract](/docs/GeoNodes/socket_ROTATION.md#subtract) [tan](/docs/GeoNodes/socket_ROTATION.md#tan) [wrap](/docs/GeoNodes/socket_ROTATION.md#wrap)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [abs](/docs/GeoNodes/socket_VECTOR.md#abs) [add](/docs/GeoNodes/socket_VECTOR.md#add) [ceil](/docs/GeoNodes/socket_VECTOR.md#ceil) [cos](/docs/GeoNodes/socket_VECTOR.md#cos) [cross](/docs/GeoNodes/socket_VECTOR.md#cross) [distance](/docs/GeoNodes/socket_VECTOR.md#distance) [divide](/docs/GeoNodes/socket_VECTOR.md#divide) [dot](/docs/GeoNodes/socket_VECTOR.md#dot) [faceforward](/docs/GeoNodes/socket_VECTOR.md#faceforward) [floor](/docs/GeoNodes/socket_VECTOR.md#floor) [frac](/docs/GeoNodes/socket_VECTOR.md#frac) [length](/docs/GeoNodes/socket_VECTOR.md#length) [max](/docs/GeoNodes/socket_VECTOR.md#max) [min](/docs/GeoNodes/socket_VECTOR.md#min) [mod](/docs/GeoNodes/socket_VECTOR.md#mod) [multiply](/docs/GeoNodes/socket_VECTOR.md#multiply) [multiply_add](/docs/GeoNodes/socket_VECTOR.md#multiply_add) [normalize](/docs/GeoNodes/socket_VECTOR.md#normalize) [project](/docs/GeoNodes/socket_VECTOR.md#project) [reflect](/docs/GeoNodes/socket_VECTOR.md#reflect) [refract](/docs/GeoNodes/socket_VECTOR.md#refract) [scale](/docs/GeoNodes/socket_VECTOR.md#scale) [sin](/docs/GeoNodes/socket_VECTOR.md#sin) [snap](/docs/GeoNodes/socket_VECTOR.md#snap) [subtract](/docs/GeoNodes/socket_VECTOR.md#subtract) [tan](/docs/GeoNodes/socket_VECTOR.md#tan) [wrap](/docs/GeoNodes/socket_VECTOR.md#wrap)
- Functions : [vabs](/docs/GeoNodes/GeoNodesTree.md#vabs) [vadd](/docs/GeoNodes/GeoNodesTree.md#vadd) [vceil](/docs/GeoNodes/GeoNodesTree.md#vceil) [vcos](/docs/GeoNodes/GeoNodesTree.md#vcos) [vcross](/docs/GeoNodes/GeoNodesTree.md#vcross) [vdistance](/docs/GeoNodes/GeoNodesTree.md#vdistance) [vdivide](/docs/GeoNodes/GeoNodesTree.md#vdivide) [vdot](/docs/GeoNodes/GeoNodesTree.md#vdot) [vfaceforward](/docs/GeoNodes/GeoNodesTree.md#vfaceforward) [vfloor](/docs/GeoNodes/GeoNodesTree.md#vfloor) [vfrac](/docs/GeoNodes/GeoNodesTree.md#vfrac) [vlength](/docs/GeoNodes/GeoNodesTree.md#vlength) [vmax](/docs/GeoNodes/GeoNodesTree.md#vmax) [vmin](/docs/GeoNodes/GeoNodesTree.md#vmin) [vmod](/docs/GeoNodes/GeoNodesTree.md#vmod) [vmultiply](/docs/GeoNodes/GeoNodesTree.md#vmultiply) [vmultiply_add](/docs/GeoNodes/GeoNodesTree.md#vmultiply_add) [vnormalize](/docs/GeoNodes/GeoNodesTree.md#vnormalize) [vproject](/docs/GeoNodes/GeoNodesTree.md#vproject) [vreflect](/docs/GeoNodes/GeoNodesTree.md#vreflect) [vrefract](/docs/GeoNodes/GeoNodesTree.md#vrefract) [vscale](/docs/GeoNodes/GeoNodesTree.md#vscale) [vsin](/docs/GeoNodes/GeoNodesTree.md#vsin) [vsnap](/docs/GeoNodes/GeoNodesTree.md#vsnap) [vsubtract](/docs/GeoNodes/GeoNodesTree.md#vsubtract) [vtan](/docs/GeoNodes/GeoNodesTree.md#vtan) [vwrap](/docs/GeoNodes/GeoNodesTree.md#vwrap)

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
