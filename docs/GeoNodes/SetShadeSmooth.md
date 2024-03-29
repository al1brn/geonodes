# Node SetShadeSmooth

- Node name : 'Set Shade Smooth'
- bl_idname : [GeometryNodeSetShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)


``` python
SetShadeSmooth(geometry=None, selection=None, shade_smooth=None, domain='FACE', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- shade_smooth : None
- domain : 'FACE'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [set_shade_smooth](/docs/GeoNodes/socket_GEOMETRY.md#set_shade_smooth) [shade_smooth](/docs/GeoNodes/socket_GEOMETRY.md#shade_smooth)

## Init

``` python
def __init__(self, geometry=None, selection=None, shade_smooth=None, domain='FACE', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetShadeSmooth', node_label=node_label, node_color=node_color, **kwargs)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
    self.shade_smooth    = shade_smooth
```
