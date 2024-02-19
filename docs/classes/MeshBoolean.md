# class MeshBoolean (Node)

    <sub>go to [index](/docs/index.md)</sub>
    
## Node reference

    Node
    ----
     - Class name : MeshBoolean
     - bl_idname : GeometryNodeMeshBoolean
    
    Node parameters
    ---------------
     - operation : 'DIFFERENCE'
    
    Input sockets
    -------------
     - mesh_1 : Geometry
     - mesh_2 : Geometry
     - self_intersection : Bool
     - hole_tolerant : Bool
    
    Output sockets
    --------------
     - mesh : Geometry
     - intersecting_edges : Bool
    
    ### Header

    ``` python
    def MeshBoolean(self, *args, mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', node_label=None, node_color=None):
    ```
    
## Implementations

    o Geometry : [mesh_boolean](#mesh_boolean) [difference](#difference) [intersect](#intersect) [union](#union) 
    
    