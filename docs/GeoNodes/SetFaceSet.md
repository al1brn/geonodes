# Node SetFaceSet

- Node name : 'Set Face Set'
- bl_idname : [GeometryNodeToolSetFaceSet](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
SetFaceSet(mesh=None, selection=None, face_set=None, node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- selection : None
- face_set : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, mesh=None, selection=None, face_set=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeToolSetFaceSet', node_label=node_label, node_color=node_color)

    self.mesh            = mesh
    self.selection       = selection
    self.face_set        = face_set
```
