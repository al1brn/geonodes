# Node ScaleInstances

- Node name : 'Scale Instances'
- bl_idname : [GeometryNodeScaleInstances](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
ScaleInstances(instances=None, selection=None, scale=None, center=None, local_space=None, node_label=None, node_color=None)
```
##### Arguments

- instances : None
- selection : None
- scale : None
- center : None
- local_space : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [scale_instances](/docs/GeoNodes/Geometry.md#scale_instances)

## Init

``` python
def __init__(self, instances=None, selection=None, scale=None, center=None, local_space=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeScaleInstances', node_label=node_label, node_color=node_color)

    self.instances       = instances
    self.selection       = selection
    self.scale           = scale
    self.center          = center
    self.local_space     = local_space
```
