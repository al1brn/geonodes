# Node DomainSize

- Node name : 'Domain Size'
- bl_idname : [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
DomainSize(geometry=None, component='MESH', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- component : 'MESH'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [domain_size](/docs/GeoNodes/Geometry.md#domain_size)

## Init

``` python
def __init__(self, geometry=None, component='MESH', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeAttributeDomainSize', node_label=node_label, node_color=node_color)

    self.component       = component
    self.geometry        = geometry
```
