# class BrickTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : BrickTexture
 - bl_idname : ShaderNodeTexBrick

Node parameters
 - color_mapping
 - offset : 0.5
 - offset_frequency : 2
 - squash : 1.0
 - squash_frequency : 2
 - texture_mapping

Input sockets
 - vector : Vect
 - color1 : Col
 - color2 : Col
 - mortar : Col
 - scale : Float
 - mortar_size : Float
 - mortar_smooth : Float
 - bias : Float
 - brick_width : Float
 - row_height : Float

Output sockets
 - color : Col
 - fac : Float

### Header

``` python
def BrickTexture(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0,
squash_frequency=2, texture_mapping=None, node_label=None, node_color=None):
```

## Implementations

o Col : [brick_texture](/docs/GeoNodes_classes/Col.md#brick_texture) 

