# class VoronoiTexture (Node)

    <sub>go to [index](/docs/index.md)</sub>
    
## Node reference

    Node
    ----
     - Class name : VoronoiTexture
     - bl_idname : ShaderNodeTexVoronoi
    
    Node parameters
    ---------------
     - color_mapping
     - distance : 'EUCLIDEAN'
     - feature : 'F1'
     - normalize : False
     - texture_mapping
     - voronoi_dimensions : '3D'
    
    Input sockets
    -------------
     - vector : Vect
     - w : Float
     - scale : Float
     - detail : Float
     - roughness : Float
     - lacunarity : Float
     - smoothness : Float
     - exponent : Float
     - randomness : Float
    
    Output sockets
    --------------
     - distance : Float
     - color : Col
     - position : Vect
     - w : Float
     - radius : Float
    
    ### Header

    ``` python
    def VoronoiTexture(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, exponent=None, smoothness=None, w=None, color_mapping=None, distance='EUCLIDEAN', feature='F1', normalize=False, texture_mapping=None,
    voronoi_dimensions='3D', node_label=None, node_color=None):
    ```
    
## Implementations

    
    