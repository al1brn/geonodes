# Node SetShadeSmooth

- Node name : 'Set Shade Smooth'
- bl_idname : GeometryNodeSetShadeSmooth


``` python
SetShadeSmooth(geometry=None, selection=None, shade_smooth=None, domain='FACE', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- shade_smooth : None
- domain : 'FACE'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [set_shade_smooth](/docs/GeoNodes/Geometry.md#set_shade_smooth) [shade_smooth](/docs/GeoNodes/Geometry.md#shade_smooth)

## Init

``` python
def __init__(self, geometry=None, selection=None, shade_smooth=None, domain='FACE', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetShadeSmooth', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.shade_smooth    = shade_smooth
```
