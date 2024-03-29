# Node SetSplineCyclic

- Node name : 'Set Spline Cyclic'
- bl_idname : [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)


``` python
SetSplineCyclic(geometry=None, selection=None, cyclic=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- cyclic : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [cyclic](/docs/GeoNodes/socket_GEOMETRY.md#cyclic) [set_spline_cyclic](/docs/GeoNodes/socket_GEOMETRY.md#set_spline_cyclic)

## Init

``` python
def __init__(self, geometry=None, selection=None, cyclic=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetSplineCyclic', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.selection       = selection
    self.cyclic          = cyclic
```
