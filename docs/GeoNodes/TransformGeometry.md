# Node TransformGeometry

- Node name : 'Transform Geometry'
- bl_idname : [Transform Geometry](https://docs.blender.org/api/current/bpy.types.Transform Geometry.html)


``` python
TransformGeometry(geometry=None, translation=None, rotation=None, scale=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- translation : None
- rotation : None
- scale : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [transform_geometry](/docs/GeoNodes/Geometry.md#transform_geometry)

## Init

``` python
def __init__(self, geometry=None, translation=None, rotation=None, scale=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeTransform', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
    self.translation     = translation
    self.rotation        = rotation
    self.scale           = scale
```
