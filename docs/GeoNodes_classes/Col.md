# class Col (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : RGBA
 - bl_idname : NodeSocketColor

Methods
 - [brick_texture](#brick_texture) : BrickTexture, color1=self
 - [brighter](#brighter) : Compare, a=self, data_type='RGBA', operation='BRIGHTER'
 - [checker_texture](#checker_texture) : CheckerTexture, color1=self
 - [darker](#darker) : Compare, a=self, data_type='RGBA', operation='DARKER'
 - [equal](#equal) : Compare, a=self, data_type='RGBA', operation='EQUAL'
 - [mix](#mix) : Mix, a=self, data_type='RGBA'
 - [mix_add](#mix_add) : Mix, a=self, blend_type='ADD'
 - [mix_burn](#mix_burn) : Mix, a=self, blend_type='BURN'
 - [mix_color](#mix_color) : Mix, a=self, blend_type='COLOR'
 - [mix_darken](#mix_darken) : Mix, a=self, blend_type='DARKEN'
 - [mix_difference](#mix_difference) : Mix, a=self, blend_type='DIFFERENCE'
 - [mix_divide](#mix_divide) : Mix, a=self, blend_type='DIVIDE'
 - [mix_dodge](#mix_dodge) : Mix, a=self, blend_type='DODGE'
 - [mix_exclusion](#mix_exclusion) : Mix, a=self, blend_type='EXCLUSION'
 - [mix_hue](#mix_hue) : Mix, a=self, blend_type='HUE'
 - [mix_lighten](#mix_lighten) : Mix, a=self, blend_type='LIGHTEN'
 - [mix_linear_light](#mix_linear_light) : Mix, a=self, blend_type='LINEAR_LIGHT'
 - [mix_mix](#mix_mix) : Mix, a=self, blend_type='MIX'
 - [mix_multiply](#mix_multiply) : Mix, a=self, blend_type='MULTIPLY'
 - [mix_overlay](#mix_overlay) : Mix, a=self, blend_type='OVERLAY'
 - [mix_saturation](#mix_saturation) : Mix, a=self, blend_type='SATURATION'
 - [mix_screen](#mix_screen) : Mix, a=self, blend_type='SCREEN'
 - [mix_soft_light](#mix_soft_light) : Mix, a=self, blend_type='SOFT_LIGHT'
 - [mix_subtract](#mix_subtract) : Mix, a=self, blend_type='SUBTRACT'
 - [mix_value](#mix_value) : Mix, a=self, blend_type='VALUE'
 - [not_equal](#not_equal) : Compare, a=self, data_type='RGBA', operation='NOT_EQUAL'
 - [reroute](#reroute) : Reroute, input=self
 - [rgb_curves](#rgb_curves) : RGBCurves, color=self
 - [separate_color](#separate_color) : SeparateColor, color=self, return node
 - [switch](#switch) : Switch, false=self, input_type='RGBA'

## Methods

### brick_texture

> BrickTexture, color1=self

``` python
def brick_texture(self, vector=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2,
texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [BrickTexture](/docs/GeoNodes_classes/BrickTexture.md)
 - bl_idname : ShaderNodeTexBrick

Arguments
 - vector : None
 - color2 : None
 - mortar : None
 - scale : None
 - mortar_size : None
 - mortar_smooth : None
 - bias : None
 - brick_width : None
 - row_height : None
 - color_mapping
 - offset : 0.5
 - offset_frequency : 2
 - squash : 1.0
 - squash_frequency : 2
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - color1 : self
 - color2 : color2
 - mortar : mortar
 - scale : scale
 - mortar_size : mortar_size
 - mortar_smooth : mortar_smooth
 - bias : bias
 - brick_width : brick_width
 - row_height : row_height
 - color_mapping : color_mapping
 - offset : offset
 - offset_frequency : offset_frequency
 - squash : squash
 - squash_frequency : squash_frequency
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

### brighter

> Compare, a=self, data_type='RGBA', operation='BRIGHTER'

``` python
def brighter(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/GeoNodes_classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'RGBA'
 - mode : mode
 - operation : 'BRIGHTER'
 - node_label : node_label
 - node_color : node_color

### checker_texture

> CheckerTexture, color1=self

``` python
def checker_texture(self, vector=None, color2=None, scale=None, color_mapping=None, texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [CheckerTexture](/docs/GeoNodes_classes/CheckerTexture.md)
 - bl_idname : ShaderNodeTexChecker

Arguments
 - vector : None
 - color2 : None
 - scale : None
 - color_mapping
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - color1 : self
 - color2 : color2
 - scale : scale
 - color_mapping : color_mapping
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

### darker

> Compare, a=self, data_type='RGBA', operation='DARKER'

``` python
def darker(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/GeoNodes_classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'RGBA'
 - mode : mode
 - operation : 'DARKER'
 - node_label : node_label
 - node_color : node_color

### equal

> Compare, a=self, data_type='RGBA', operation='EQUAL'

``` python
def equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/GeoNodes_classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - epsilon : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - epsilon : epsilon
 - data_type : 'RGBA'
 - mode : mode
 - operation : 'EQUAL'
 - node_label : node_label
 - node_color : node_color

### mix

> Mix, a=self, data_type='RGBA'

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - blend_type : 'MIX'
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : blend_type
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_add

> Mix, a=self, blend_type='ADD'

``` python
def mix_add(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'ADD'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_burn

> Mix, a=self, blend_type='BURN'

``` python
def mix_burn(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'BURN'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_color

> Mix, a=self, blend_type='COLOR'

``` python
def mix_color(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'COLOR'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_darken

> Mix, a=self, blend_type='DARKEN'

``` python
def mix_darken(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'DARKEN'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_difference

> Mix, a=self, blend_type='DIFFERENCE'

``` python
def mix_difference(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'DIFFERENCE'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_divide

> Mix, a=self, blend_type='DIVIDE'

``` python
def mix_divide(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'DIVIDE'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_dodge

> Mix, a=self, blend_type='DODGE'

``` python
def mix_dodge(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'DODGE'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_exclusion

> Mix, a=self, blend_type='EXCLUSION'

``` python
def mix_exclusion(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'EXCLUSION'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_hue

> Mix, a=self, blend_type='HUE'

``` python
def mix_hue(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'HUE'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_lighten

> Mix, a=self, blend_type='LIGHTEN'

``` python
def mix_lighten(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'LIGHTEN'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_linear_light

> Mix, a=self, blend_type='LINEAR_LIGHT'

``` python
def mix_linear_light(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'LINEAR_LIGHT'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_mix

> Mix, a=self, blend_type='MIX'

``` python
def mix_mix(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'MIX'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_multiply

> Mix, a=self, blend_type='MULTIPLY'

``` python
def mix_multiply(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'MULTIPLY'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_overlay

> Mix, a=self, blend_type='OVERLAY'

``` python
def mix_overlay(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'OVERLAY'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_saturation

> Mix, a=self, blend_type='SATURATION'

``` python
def mix_saturation(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'SATURATION'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_screen

> Mix, a=self, blend_type='SCREEN'

``` python
def mix_screen(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'SCREEN'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_soft_light

> Mix, a=self, blend_type='SOFT_LIGHT'

``` python
def mix_soft_light(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'SOFT_LIGHT'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_subtract

> Mix, a=self, blend_type='SUBTRACT'

``` python
def mix_subtract(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'SUBTRACT'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mix_value

> Mix, a=self, blend_type='VALUE'

``` python
def mix_value(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : 'VALUE'
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'RGBA'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### not_equal

> Compare, a=self, data_type='RGBA', operation='NOT_EQUAL'

``` python
def not_equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/GeoNodes_classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - epsilon : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - epsilon : epsilon
 - data_type : 'RGBA'
 - mode : mode
 - operation : 'NOT_EQUAL'
 - node_label : node_label
 - node_color : node_color

### reroute

> Reroute, input=self

``` python
def reroute(self, node_label=None, node_color=None):
```
Node
 - class_name : [Reroute](/docs/GeoNodes_classes/Reroute.md)
 - bl_idname : NodeReroute

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - input : self
 - node_label : node_label
 - node_color : node_color

### rgb_curves

> RGBCurves, color=self

``` python
def rgb_curves(self, fac=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [RGBCurves](/docs/GeoNodes_classes/RGBCurves.md)
 - bl_idname : ShaderNodeRGBCurve

Arguments
 - fac : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - color : self
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

### separate_color

> SeparateColor, color=self, return node

``` python
def separate_color(self, mode='RGB', node_label=None, node_color=None):
```
Node
 - class_name : [SeparateColor](/docs/GeoNodes_classes/SeparateColor.md)
 - bl_idname : FunctionNodeSeparateColor

Arguments
 - mode : 'RGB'
 - node_label : None
 - node_color : None

Node initialization
 - color : self
 - mode : mode
 - node_label : node_label
 - node_color : node_color

### switch

> Switch, false=self, input_type='RGBA'

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
Node
 - class_name : [Switch](/docs/GeoNodes_classes/Switch.md)
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
 - input_type : 'RGBA'
 - node_label : node_label
 - node_color : node_color
