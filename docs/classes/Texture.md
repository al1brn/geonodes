# class Texture (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : TEXTURE
 - bl_idname : NodeSocketTexture

Methods
 - [switch](#switch) : Switch, false=self, input_type='TEXTURE'

## Methods

### switch

Switch, false=self, input_type='TEXTURE'

Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - true : None
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : self
 - true : true
 - input_type : 'TEXTURE'
 - node_label : node_label
 - node_color : node_color

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```