# Node IcoSphere

- Node name : 'Ico Sphere'
- bl_idname : [GeometryNodeMeshIcoSphere](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
IcoSphere(radius=None, subdivisions=None, node_label=None, node_color=None)
```
##### Arguments

- radius : None
- subdivisions : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, radius=None, subdivisions=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshIcoSphere', node_label=node_label, node_color=node_color)

    self.radius          = radius
    self.subdivisions    = subdivisions
```
