# class Mat (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : MATERIAL
 - bl_idname : NodeSocketMaterial

Methods
 - [material_selection](#material_selection) : MaterialSelection, material=self, return socket
 - [switch](#switch) : Switch, false=self, input_type='MATERIAL'

## Methods

### material_selection

> MaterialSelection, material=self, return socket

``` python
def material_selection(self, node_label=None, node_color=None):
```
Node
 - class_name : [MaterialSelection](/docs/classes/MaterialSelection.md)
 - bl_idname : GeometryNodeMaterialSelection

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - material : self
 - node_label : node_label
 - node_color : node_color

### switch

> Switch, false=self, input_type='MATERIAL'

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
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
 - input_type : 'MATERIAL'
 - node_label : node_label
 - node_color : node_color
