# class Col (Socket)

    <sub>go to [index](/docs/index.md)</sub>
    
    Socket
    ------
     - Type : RGBA
     - bl_idname : NodeSocketColor
    
    Methods
    -------
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

    BrickTexture, color1=self
    
    Node
    ----
     - class_name : [BrickTexture](/docs/classes/BrickTexture.md)
     - bl_idname : ShaderNodeTexBrick
    
### brighter

    Compare, a=self, data_type='RGBA', operation='BRIGHTER'
    
    Node
    ----
     - class_name : [Compare](/docs/classes/Compare.md)
     - bl_idname : FunctionNodeCompare
    
### checker_texture

    CheckerTexture, color1=self
    
    Node
    ----
     - class_name : [CheckerTexture](/docs/classes/CheckerTexture.md)
     - bl_idname : ShaderNodeTexChecker
    
### darker

    Compare, a=self, data_type='RGBA', operation='DARKER'
    
    Node
    ----
     - class_name : [Compare](/docs/classes/Compare.md)
     - bl_idname : FunctionNodeCompare
    
### equal

    Compare, a=self, data_type='RGBA', operation='EQUAL'
    
    Node
    ----
     - class_name : [Compare](/docs/classes/Compare.md)
     - bl_idname : FunctionNodeCompare
    
### mix

    Mix, a=self, data_type='RGBA'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_add

    Mix, a=self, blend_type='ADD'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_burn

    Mix, a=self, blend_type='BURN'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_color

    Mix, a=self, blend_type='COLOR'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_darken

    Mix, a=self, blend_type='DARKEN'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_difference

    Mix, a=self, blend_type='DIFFERENCE'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_divide

    Mix, a=self, blend_type='DIVIDE'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_dodge

    Mix, a=self, blend_type='DODGE'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_exclusion

    Mix, a=self, blend_type='EXCLUSION'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_hue

    Mix, a=self, blend_type='HUE'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_lighten

    Mix, a=self, blend_type='LIGHTEN'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_linear_light

    Mix, a=self, blend_type='LINEAR_LIGHT'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_mix

    Mix, a=self, blend_type='MIX'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_multiply

    Mix, a=self, blend_type='MULTIPLY'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_overlay

    Mix, a=self, blend_type='OVERLAY'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_saturation

    Mix, a=self, blend_type='SATURATION'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_screen

    Mix, a=self, blend_type='SCREEN'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_soft_light

    Mix, a=self, blend_type='SOFT_LIGHT'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_subtract

    Mix, a=self, blend_type='SUBTRACT'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### mix_value

    Mix, a=self, blend_type='VALUE'
    
    Node
    ----
     - class_name : [Mix](/docs/classes/Mix.md)
     - bl_idname : ShaderNodeMix
    
### not_equal

    Compare, a=self, data_type='RGBA', operation='NOT_EQUAL'
    
    Node
    ----
     - class_name : [Compare](/docs/classes/Compare.md)
     - bl_idname : FunctionNodeCompare
    
### reroute

    Reroute, input=self
    
    Node
    ----
     - class_name : [Reroute](/docs/classes/Reroute.md)
     - bl_idname : NodeReroute
    
### rgb_curves

    RGBCurves, color=self
    
    Node
    ----
     - class_name : [RGBCurves](/docs/classes/RGBCurves.md)
     - bl_idname : ShaderNodeRGBCurve
    
### separate_color

    SeparateColor, color=self, return node
    
    Node
    ----
     - class_name : [SeparateColor](/docs/classes/SeparateColor.md)
     - bl_idname : FunctionNodeSeparateColor
    
### switch

    Switch, false=self, input_type='RGBA'
    
    Node
    ----
     - class_name : [Switch](/docs/classes/Switch.md)
     - bl_idname : GeometryNodeSwitch
    