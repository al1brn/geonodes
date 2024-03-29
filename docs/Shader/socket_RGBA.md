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


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- blend_type : 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_add


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_add(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_burn


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_burn(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_color


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_color(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_darken


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_darken(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_difference


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_difference(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_divide


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_divide(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_dodge


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_dodge(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_exclusion


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_exclusion(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='EXCLUSION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_hue


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_hue(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_lighten


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_lighten(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_linear_light


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_linear_light(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_mix


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_mix(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_multiply


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_multiply(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_overlay


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_overlay(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_saturation


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_saturation(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_screen


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_screen(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_soft_light


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_soft_light(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_subtract


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_subtract(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mix_value


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix_value(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### rgb_curves


- node : [RGBCurves](/docs/Shader/RGBCurves.md)
- self : color
- jump : color
- return : self

##### Arguments

- fac : None
- mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def rgb_curves(self, fac=None, mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.RGBCurves(fac=fac, color=self, mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.color)
    return self
```
### separate_color


- node : [SeparateColor](/docs/Shader/SeparateColor.md)
- self : color
- jump : No
- return : node

##### Arguments

- mode : 'RGB' in ('RGB', 'HSV', 'HSL')
- node_label : None
- node_color : None

#### Source code

``` python
def separate_color(self, mode='RGB', node_label=None, node_color=None, **kwargs):
    node = self.tree.SeparateColor(color=self, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
