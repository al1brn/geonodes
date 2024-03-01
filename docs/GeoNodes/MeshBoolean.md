# Node MeshBoolean

- Node name : 'Mesh Boolean'
- bl_idname : GeometryNodeMeshBoolean


``` python
MeshBoolean(*args, mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', node_label=None, node_color=None)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- mesh_1 : None
- mesh_2 : None
- self_intersection : None
- hole_tolerant : None
- operation : 'DIFFERENCE'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [mesh_difference](/docs/GeoNodes/Geometry.md#mesh_difference) [mesh_intersect](/docs/GeoNodes/Geometry.md#mesh_intersect) [mesh_union](/docs/GeoNodes/Geometry.md#mesh_union)

## Init

``` python
def __init__(self, *args, mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshBoolean', node_label=node_label, node_color=node_color)

    self.operation       = operation
    self._set_multi_input(*args)
    self.mesh_1          = mesh_1
    self.mesh_2          = mesh_2
    self.self_intersection = self_intersection
    self.hole_tolerant   = hole_tolerant
```
