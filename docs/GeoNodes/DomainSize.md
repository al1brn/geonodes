# Node DomainSize

- Node name : 'Domain Size'
- bl_idname : [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)


``` python
DomainSize(geometry=None, component='MESH', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- component : 'MESH'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [domain_size](/docs/GeoNodes/socket_GEOMETRY.md#domain_size)

## Init

``` python
def __init__(self, geometry=None, component='MESH', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeAttributeDomainSize', node_label=node_label, node_color=node_color, **kwargs)

    self.component       = component
    self.geometry        = geometry
```
