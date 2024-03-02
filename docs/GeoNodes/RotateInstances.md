# Node RotateInstances

- Node name : 'Rotate Instances'
- bl_idname : [GeometryNodeRotateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)


``` python
RotateInstances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, node_label=None, node_color=None)
```
##### Arguments

- instances : None
- selection : None
- rotation : None
- pivot_point : None
- local_space : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [rotate_instances](/docs/GeoNodes/socket_GEOMETRY.md#rotate_instances) [rotate_instances](/docs/GeoNodes/socket_GEOMETRY.md#rotate_instances)

## Init

``` python
def __init__(self, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeRotateInstances', node_label=node_label, node_color=node_color)

    self.instances       = instances
    self.selection       = selection
    self.rotation        = rotation
    self.pivot_point     = pivot_point
    self.local_space     = local_space
```
