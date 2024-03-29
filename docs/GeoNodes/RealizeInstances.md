# Node RealizeInstances

- Node name : 'Realize Instances'
- bl_idname : [GeometryNodeRealizeInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)


``` python
RealizeInstances(geometry=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [realize_instances](/docs/GeoNodes/socket_GEOMETRY.md#realize_instances)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeRealizeInstances', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
```
