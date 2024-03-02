# Socket VECTOR


### Methods

- [map_range](#map_range)
- [mix](#mix)
- [separate_xyz](#separate_xyz)
- [switch](#switch)
- [vector_curves](#vector_curves)

## Methods

### map_range


- node : [MapRange](/docs/Compositor/MapRange.md)
- self : value
- jump : No
- return : result

##### Arguments

- from_min : None
- from_max : None
- to_min : None
- to_max : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None):
    node = self.tree.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color)
    return node.result
```
### mix


- node : [Mix](/docs/Compositor/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- fac : None
- image : None
- image_1 : None
- tag_need_exec : None
- use_alpha : False
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='MIX', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color)
    self.jump(node.result)
    return self
```
### separate_xyz


- node : [SeparateXYZ](/docs/Compositor/SeparateXYZ.md)
- self : vector
- jump : No
- return : node

##### Arguments

- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def separate_xyz(self, tag_need_exec=None, node_label=None, node_color=None):
    node = self.tree.SeparateXYZ(vector=self, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color)
    return node
```
### switch


- node : [Switch](/docs/Compositor/Switch.md)
- self : false
- jump : No
- return : output

##### Arguments

- off : None
- on : None
- check : False
- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def switch(self, off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None):
    node = self.tree.Switch(off=off, on=on, check=check, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color)
    return node.output
```
### vector_curves


- node : [VectorCurves](/docs/Compositor/VectorCurves.md)
- self : vector
- jump : vector
- return : self

##### Arguments

- mapping : None
- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def vector_curves(self, mapping=None, tag_need_exec=None, node_label=None, node_color=None):
    node = self.tree.VectorCurves(vector=self, mapping=mapping, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color)
    self.jump(node.vector)
    return self
```
