# Node BoundingBox

- Node name : 'Bounding Box'
- bl_idname : [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)


``` python
BoundingBox(geometry=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [bounding_box](/docs/GeoNodes/socket_GEOMETRY.md#bounding_box)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeBoundBox', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
```
