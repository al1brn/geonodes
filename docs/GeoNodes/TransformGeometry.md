# Node TransformGeometry

- Node name : 'Transform Geometry'
- bl_idname : [GeometryNodeTransform](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)


``` python
TransformGeometry(geometry=None, translation=None, rotation=None, scale=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- translation : None
- rotation : None
- scale : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [transform_geometry](/docs/GeoNodes/socket_GEOMETRY.md#transform_geometry)

## Init

``` python
def __init__(self, geometry=None, translation=None, rotation=None, scale=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeTransform', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.translation     = translation
    self.rotation        = rotation
    self.scale           = scale
```
