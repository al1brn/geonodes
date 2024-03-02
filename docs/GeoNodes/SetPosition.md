# Node SetPosition

- Node name : 'Set Position'
- bl_idname : [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)


``` python
SetPosition(geometry=None, selection=None, position=None, offset=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- position : None
- offset : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [offset](/docs/GeoNodes/GEOMETRY.md#offset) [offset](/docs/GeoNodes/GEOMETRY.md#offset) [position](/docs/GeoNodes/GEOMETRY.md#position) [position](/docs/GeoNodes/GEOMETRY.md#position) [set_position](/docs/GeoNodes/GEOMETRY.md#set_position) [set_position](/docs/GeoNodes/GEOMETRY.md#set_position)

## Init

``` python
def __init__(self, geometry=None, selection=None, position=None, offset=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetPosition', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
    self.selection       = selection
    self.position        = position
    self.offset          = offset
```
