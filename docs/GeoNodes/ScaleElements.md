# Node ScaleElements

- Node name : 'Scale Elements'
- bl_idname : [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)


``` python
ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None, **kwargs)
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

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [scale_elements](/docs/GeoNodes/socket_GEOMETRY.md#scale_elements)

## Init

``` python
def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeScaleElements', node_label=node_label, node_color=node_color, **kwargs)

    self.domain          = domain
    self.scale_mode      = scale_mode
    self.geometry        = geometry
    self.selection       = selection
    self.scale           = scale
    self.center          = center
    self.axis            = axis
```
