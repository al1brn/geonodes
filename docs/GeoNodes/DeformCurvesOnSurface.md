# Node DeformCurvesOnSurface

- Node name : 'Deform Curves on Surface'
- bl_idname : [GeometryNodeDeformCurvesOnSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)


``` python
DeformCurvesOnSurface(curves=None, node_label=None, node_color=None)
```
##### Arguments

- curves : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [deform_curves_on_surface](/docs/GeoNodes/Geometry.md#deform_curves_on_surface)

## Init

``` python
def __init__(self, curves=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeDeformCurvesOnSurface', node_label=node_label, node_color=node_color)

    self.curves          = curves
```
