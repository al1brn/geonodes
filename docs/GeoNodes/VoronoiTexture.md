# Node VoronoiTexture

- Node name : 'Voronoi Texture'
- bl_idname : [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)


``` python
VoronoiTexture(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, exponent=None, smoothness=None, w=None, color_mapping=None, distance='EUCLIDEAN', feature='F1', normalize=False, texture_mapping=None, voronoi_dimensions='3D', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- scale : None
- detail : None
- roughness : None
- lacunarity : None
- randomness : None
- exponent : None
- smoothness : None
- w : None
- color_mapping : None
- distance : 'EUCLIDEAN'
- feature : 'F1'
- normalize : False
- texture_mapping : None
- voronoi_dimensions : '3D'

## Implementation

- Functions : [voronoi_texture](/docs/GeoNodes/GeoNodesTree.md#voronoi_texture)

## Init

``` python
def __init__(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, exponent=None, smoothness=None, w=None, color_mapping=None, distance='EUCLIDEAN', feature='F1', normalize=False, texture_mapping=None, voronoi_dimensions='3D', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexVoronoi', node_label=node_label, node_color=node_color, **kwargs)

    self.color_mapping   = color_mapping
    self.distance        = distance
    self.feature         = feature
    self.normalize       = normalize
    self.texture_mapping = texture_mapping
    self.voronoi_dimensions = voronoi_dimensions
    self.vector          = vector
    self.scale           = scale
    self.detail          = detail
    self.roughness       = roughness
    self.lacunarity      = lacunarity
    self.randomness      = randomness
    self.exponent        = exponent
    self.smoothness      = smoothness
    self.w               = w
```
