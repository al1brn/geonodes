# Node Bake

- Node name : 'Bake'
- bl_idname : [GeometryNodeBake](https://docs.blender.org/api/current/bpy.types.GeometryNodeBake.html)


``` python
Bake(geometry=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [bake](/docs/GeoNodes/socket_GEOMETRY.md#bake)
- Functions : [bake](/docs/GeoNodes/GeoNodesTree.md#bake)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeBake', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
```
