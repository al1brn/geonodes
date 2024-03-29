# Socket IMAGE


### Methods

- [image_info](#image_info)
- [image_texture](#image_texture)
- [index_switch](#index_switch)
- [switch](#switch)

## Methods

### image_info


- node : [ImageInfo](/docs/GeoNodes/ImageInfo.md)
- self : image
- jump : No
- return : node

##### Arguments

- frame : None
- node_label : None
- node_color : None

#### Source code

``` python
def image_info(self, frame=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ImageInfo(image=self, frame=frame, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### image_texture


- node : [ImageTexture](/docs/GeoNodes/ImageTexture.md)
- self : image
- jump : No
- return : node

##### Arguments

- vector : None
- frame : None
- extension : 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
- interpolation : Linear in ('Linear', 'Closest', 'Cubic')
- node_label : None
- node_color : None

#### Source code

``` python
def image_texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear', node_label=None, node_color=None, **kwargs):
    node = self.tree.ImageTexture(image=self, vector=vector, frame=frame, extension=extension, interpolation=interpolation, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### index_switch


- node : [IndexSwitch](/docs/GeoNodes/IndexSwitch.md)
- self : ARG0
- jump : No
- return : output

##### Arguments

- *args : 'ARG_NO_VALUE'
- index : None
- node_label : None
- node_color : None

#### Source code

``` python
def index_switch(self, *args, index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='IMAGE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### switch


- node : [Switch](/docs/GeoNodes/Switch.md)
- self : false
- jump : No
- return : output

##### Arguments

- switch : None
- true : None
- node_label : None
- node_color : None

#### Source code

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='IMAGE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
