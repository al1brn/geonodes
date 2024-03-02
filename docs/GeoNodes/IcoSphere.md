# Node IcoSphere

- Node name : 'Ico Sphere'
- bl_idname : [GeometryNodeMeshIcoSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)


``` python
IcoSphere(radius=None, subdivisions=None, node_label=None, node_color=None)
```
##### Arguments

- radius : None
- subdivisions : None

## Implementation

- Functions : [ico_sphere](/docs/GeoNodes/GeoNodesTree.md#ico_sphere) [ico_sphere](/docs/GeoNodes/GeoNodesTree.md#ico_sphere)

## Init

``` python
def __init__(self, radius=None, subdivisions=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeMeshIcoSphere', node_label=node_label, node_color=node_color)

    self.radius          = radius
    self.subdivisions    = subdivisions
```
