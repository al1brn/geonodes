# Node SetSelection

- Node name : 'Set Selection'
- bl_idname : [Set Selection](https://docs.blender.org/api/current/bpy.types.Set Selection.html)


``` python
SetSelection(geometry=None, selection=None, domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- domain : 'POINT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, geometry=None, selection=None, domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeToolSetSelection', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.geometry        = geometry
    self.selection       = selection
```
