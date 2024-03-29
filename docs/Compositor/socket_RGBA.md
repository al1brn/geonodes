# Socket RGBA


### Methods

- [mix](#mix)
- [mix_add](#mix_add)
- [mix_burn](#mix_burn)
- [mix_color](#mix_color)
- [mix_darken](#mix_darken)
- [mix_difference](#mix_difference)
- [mix_divide](#mix_divide)
- [mix_dodge](#mix_dodge)
- [mix_exclusion](#mix_exclusion)
- [mix_hue](#mix_hue)
- [mix_lighten](#mix_lighten)
- [mix_linear_light](#mix_linear_light)
- [mix_mix](#mix_mix)
- [mix_multiply](#mix_multiply)
- [mix_overlay](#mix_overlay)
- [mix_saturation](#mix_saturation)
- [mix_screen](#mix_screen)
- [mix_soft_light](#mix_soft_light)
- [mix_subtract](#mix_subtract)
- [mix_value](#mix_value)
- [rgb_curves](#rgb_curves)
- [separate_color](#separate_color)

## Methods

### mix


- node : [Mix](/docs/Compositor/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- fac : None
- image : None
- image_1 : None
- blend_type : 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- tag_need_exec : None
- use_alpha : False
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, fac=None, image=None, image_1=None, blend_type='MIX', tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type=blend_type, tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_add


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
def mix_add(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='ADD', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_burn


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
def mix_burn(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='BURN', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_color


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
def mix_color(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='COLOR', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_darken


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
def mix_darken(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='DARKEN', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_difference


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
def mix_difference(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='DIFFERENCE', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_divide


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
def mix_divide(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='DIVIDE', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_dodge


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
def mix_dodge(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='DODGE', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_exclusion


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
def mix_exclusion(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='EXCLUSION', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_hue


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
def mix_hue(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='HUE', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_lighten


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
def mix_lighten(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='LIGHTEN', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_linear_light


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
def mix_linear_light(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='LINEAR_LIGHT', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_mix


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
def mix_mix(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='MIX', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_multiply


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
def mix_multiply(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='MULTIPLY', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_overlay


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
def mix_overlay(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='OVERLAY', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_saturation


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
def mix_saturation(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='SATURATION', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_screen


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
def mix_screen(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='SCREEN', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_soft_light


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
def mix_soft_light(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='SOFT_LIGHT', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_subtract


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
def mix_subtract(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='SUBTRACT', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_value


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
def mix_value(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='VALUE', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### rgb_curves


- node : [RGBCurves](/docs/Compositor/RGBCurves.md)
- self : color
- jump : color
- return : self

##### Arguments

- fac : None
- image : None
- black_level : None
- white_level : None
- mapping : None
- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def rgb_curves(self, fac=None, image=None, black_level=None, white_level=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.RGBCurves(fac=fac, image=image, black_level=black_level, white_level=white_level, mapping=mapping, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.color)
    return self
```
### separate_color


- node : [SeparateColor](/docs/Compositor/SeparateColor.md)
- self : color
- jump : No
- return : node

##### Arguments

- image : None
- mode : 'RGB' in ('RGB', 'HSV', 'HSL', 'YCC', 'YUV')
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def separate_color(self, image=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.tree.SeparateColor(image=image, mode=mode, tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
