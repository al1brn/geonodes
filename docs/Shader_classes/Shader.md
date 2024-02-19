# class Shader (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : SHADER
 - bl_idname : NodeSocketShader

Methods
 - [add_shader](#add_shader) : AddShader, shader=self
 - [light_output](#light_output) : LightOutput, surface=self, return node
 - [mix_shader](#mix_shader) : MixShader, shader=self
 - [shader_to_rgb](#shader_to_rgb) : ShaderToRGB, shader=self, return node

## Methods

### add_shader

> AddShader, shader=self

``` python
def add_shader(self, shader=None, node_label=None, node_color=None):
```
Node
 - class_name : [AddShader](/docs/Shader_classes/AddShader.md)
 - bl_idname : ShaderNodeAddShader

Arguments
 - shader : None
 - node_label : None
 - node_color : None

Node initialization
 - shader : self
 - shader_1 : shader
 - node_label : node_label
 - node_color : node_color

### light_output

> LightOutput, surface=self, return node

``` python
def light_output(self, is_active_output=True, target='ALL', node_label=None, node_color=None):
```
Node
 - class_name : [LightOutput](/docs/Shader_classes/LightOutput.md)
 - bl_idname : ShaderNodeOutputLight

Arguments
 - is_active_output : True
 - target : 'ALL'
 - node_label : None
 - node_color : None

Node initialization
 - surface : self
 - is_active_output : is_active_output
 - target : target
 - node_label : node_label
 - node_color : node_color

### mix_shader

> MixShader, shader=self

``` python
def mix_shader(self, fac=None, shader=None, node_label=None, node_color=None):
```
Node
 - class_name : [MixShader](/docs/Shader_classes/MixShader.md)
 - bl_idname : ShaderNodeMixShader

Arguments
 - fac : None
 - shader : None
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - shader : self
 - shader_1 : shader
 - node_label : node_label
 - node_color : node_color

### shader_to_rgb

> ShaderToRGB, shader=self, return node

``` python
def shader_to_rgb(self, node_label=None, node_color=None):
```
Node
 - class_name : [ShaderToRGB](/docs/Shader_classes/ShaderToRGB.md)
 - bl_idname : ShaderNodeShaderToRGB

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - shader : self
 - node_label : node_label
 - node_color : node_color
