# Node RealizeInstances

- Node name : 'Realize Instances'
- bl_idname : [Realize Instances](https://docs.blender.org/api/current/bpy.types.Realize Instances.html)


``` python
RealizeInstances(geometry=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [realize_instances](/docs/GeoNodes/Geometry.md#realize_instances)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeRealizeInstances', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
```
