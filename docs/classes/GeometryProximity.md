# class GeometryProximity (Node)

    <sub>go to [index](/docs/index.md)</sub>
    
## Node reference

    Node
    ----
     - Class name : GeometryProximity
     - bl_idname : GeometryNodeProximity
    
    Node parameters
    ---------------
     - target_element : 'FACES'
    
    Input sockets
    -------------
     - target : Geometry
     - source_position : Vect
    
    Output sockets
    --------------
     - position : Vect
     - distance : Float
    
    ### Header

    ``` python
    def GeometryProximity(self, target=None, source_position=None, target_element='FACES', node_label=None, node_color=None):
    ```
    
## Implementations

    o Vect : [geometry_proximity](#geometry_proximity) 
    
    