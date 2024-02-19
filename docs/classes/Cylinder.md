# class Cylinder (Node)

    <sub>go to [index](/docs/index.md)</sub>
    
## Node reference

    Node
    ----
     - Class name : Cylinder
     - bl_idname : GeometryNodeMeshCylinder
    
    Node parameters
    ---------------
     - fill_type : 'NGON'
    
    Input sockets
    -------------
     - vertices : Int
     - side_segments : Int
     - fill_segments : Int
     - radius : Float
     - depth : Float
    
    Output sockets
    --------------
     - mesh : Geometry
     - top : Bool
     - side : Bool
     - bottom : Bool
     - uv_map : Vect
    
    ### Header

    ``` python
    def Cylinder(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', node_label=None, node_color=None):
    ```
    
## Implementations

    
    