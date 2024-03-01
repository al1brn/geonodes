# Node ScaleElements

- Node name : 'Scale Elements'
- bl_idname : GeometryNodeScaleElements


``` python
ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- scale : None
- center : None
- axis : None
- domain : 'FACE'
- scale_mode : 'UNIFORM'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [scale_elements](/docs/GeoNodes/Geometry.md#scale_elements)

## Init

``` python
def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeScaleElements', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.scale_mode      = scale_mode
    self.geometry        = geometry
    self.selection       = selection
    self.scale           = scale
    self.center          = center
    self.axis            = axis
```
