# Socket Img


### Methods

- [image_info](#image_info)
- [image_texture](#image_texture)
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
def image_info(self, frame=None, node_label=None, node_color=None):
    node = self.tree.ImageInfo(image=self, frame=frame, node_label=node_label, node_color=node_color)
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
def image_texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear', node_label=None, node_color=None):
    node = self.tree.ImageTexture(image=self, vector=vector, frame=frame, extension=extension, interpolation=interpolation, node_label=node_label, node_color=node_color)
    return node
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
def switch(self, switch=None, true=None, node_label=None, node_color=None):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='IMAGE', node_label=node_label, node_color=node_color)
    return node.output
```
