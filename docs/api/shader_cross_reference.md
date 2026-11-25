# Shader Nodes cross reference

This lookup reflects the checked-in `generation2` output. Use public socket
classes and `nd` inside the corresponding active tree. Inherited methods may
also be available on specialized socket classes.

## AOV Output

Blender identifier: `ShaderNodeOutputAOV`

### nd

- `nd.aov_output(cls, color: Color=None, value: Float=None, aov_name: str='')` — class method; returns `NODE`.

### Color

- `Color.aov_output(self, value: Float=None, aov_name: str='')` — method; returns `NODE`.

## Add Shader

Blender identifier: `ShaderNodeAddShader`

### nd

- `nd.add_shader(cls, shader: Shader=None, shader_1: Shader=None)` — class method; returns `OUT`.

### Shader

- `Shader.add(self, shader: Shader=None)` — method; returns `OUT`.

## Ambient Occlusion

Blender identifier: `ShaderNodeAmbientOcclusion`

### nd

- `nd.ambient_occlusion(cls, color: Color=None, distance: Float=None, normal: Vector=None, samples: int=16, inside: bool=False, only_local: bool=False)` — class method; returns `OUT`.

## Attribute

Blender identifier: `ShaderNodeAttribute`

### nd

- `nd.attribute(cls, attribute_name: str='', attribute_type: T_ATTRIBUTE_TYPE_1='GEOMETRY')` — class method; returns `OUT`.

## Background

Blender identifier: `ShaderNodeBackground`

### nd

- `nd.background(cls, color: Color=None, strength: Float=None)` — class method; returns `OUT`.

### Shader

- `Shader.Background(cls, color: Color=None, strength: Float=None)` — class method; returns `OUT`.

## Bevel

Blender identifier: `ShaderNodeBevel`

### nd

- `nd.bevel(cls, radius: Float=None, normal: Vector=None, samples: int=4)` — class method; returns `OUT`.

## Blackbody

Blender identifier: `ShaderNodeBlackbody`

### nd

- `nd.blackbody(cls, temperature: Float=None)` — class method; returns `OUT`.

### Color

- `Color.Blackbody(cls, temperature: Float=None)` — class method; returns `OUT`.

## Boolean

Blender identifier: `FunctionNodeInputBool`

### nd

- `nd.boolean(cls, boolean: bool=False)` — class method; returns `OUT`.

## Boolean Math

Blender identifier: `FunctionNodeBooleanMath`

### nd

- `nd.boolean_math(cls, boolean: Boolean=None, boolean_1: Boolean=None, operation: T_OPERATION_1='AND')` — class method; returns `OUT`.

### gnmath

- `gnmath.band(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.bor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.xor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.bnot(boolean: Boolean=None)` — method; returns `OUT`.
- `gnmath.not_and(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.nor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.xnor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.imply(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.nimply(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.band(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.__and__(self, other)` — method; returns `OUT`.
- `Boolean.__rand__(self, other)` — method; returns `OUT`.
- `Boolean.__iand__(self, other)` — method; returns `OUT`.
- `Boolean.__mul__(self, other)` — method; returns `OUT`.
- `Boolean.__rmul__(self, other)` — method; returns `OUT`.
- `Boolean.__imul__(self, other)` — method; returns `OUT`.
- `Boolean.bor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.__or__(self, other)` — method; returns `OUT`.
- `Boolean.__ror__(self, other)` — method; returns `OUT`.
- `Boolean.__ior__(self, other)` — method; returns `OUT`.
- `Boolean.__add__(self, other)` — method; returns `OUT`.
- `Boolean.__radd__(self, other)` — method; returns `OUT`.
- `Boolean.__iadd__(self, other)` — method; returns `OUT`.
- `Boolean.xor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.__xor__(self, other)` — method; returns `OUT`.
- `Boolean.__rxor__(self, other)` — method; returns `OUT`.
- `Boolean.__ixor__(self, other)` — method; returns `OUT`.
- `Boolean.__sub__(self, other)` — method; returns `OUT`.
- `Boolean.__rsub__(self, other)` — method; returns `OUT`.
- `Boolean.__isub__(self, other)` — method; returns `OUT`.
- `Boolean.bnot(self)` — method; returns `OUT`.
- `Boolean.__neg__(self)` — method; returns `OUT`.
- `Boolean.__invert__(self)` — method; returns `OUT`.
- `Boolean.not_and(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.nor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.xnor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.imply(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.nimply(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.boolean_math(self, boolean: Boolean=None, operation: T_OPERATION_1='AND')` — method; returns `OUT`.

## Brick Texture

Blender identifier: `ShaderNodeTexBrick`

### nd

- `nd.brick_texture(cls, vector: Vector=None, color1: Color=None, color2: Color=None, mortar: Color=None, scale: Float=None, mortar_size: Float=None, mortar_smooth: Float=None, bias: Float=None, brick_width: Float=None, row_height: Float=None, offset_frequency: int=2, squash_frequency: int=2, offset: float=0.5, squash: float=1.0)` — class method; returns `OUT`.

### Texture

- `Texture.Brick(cls, vector: Vector=None, color1: Color=None, color2: Color=None, mortar: Color=None, scale: Float=None, mortar_size: Float=None, mortar_smooth: Float=None, bias: Float=None, brick_width: Float=None, row_height: Float=None, offset_frequency: int=2, squash_frequency: int=2, offset: float=0.5, squash: float=1.0)` — class method; returns `OUT`.

## Brightness/Contrast

Blender identifier: `ShaderNodeBrightContrast`

### nd

- `nd.brightness_contrast(cls, color: Color=None, brightness: Float=None, contrast: Float=None)` — class method; returns `OUT`.

### Color

- `Color.brightness_contrast(self, brightness: Float=None, contrast: Float=None)` — method; returns `OUT`.

## Bump

Blender identifier: `ShaderNodeBump`

### nd

- `nd.bump(cls, strength: Float=None, distance: Float=None, filter_width: Float=None, height: Float=None, normal: Vector=None, invert: bool=False)` — class method; returns `OUT`.

### Float

- `Float.bump(self, distance: Float=None, filter_width: Float=None, height: Float=None, normal: Vector=None, invert: bool=False)` — method; returns `OUT`.

## Camera Data

Blender identifier: `ShaderNodeCameraData`

### nd

- `nd.camera_data(cls)` — class method; returns `OUT`.

## Checker Texture

Blender identifier: `ShaderNodeTexChecker`

### nd

- `nd.checker_texture(cls, vector: Vector=None, color1: Color=None, color2: Color=None, scale: Float=None)` — class method; returns `OUT`.

### Texture

- `Texture.Checker(cls, vector: Vector=None, color1: Color=None, color2: Color=None, scale: Float=None)` — class method; returns `OUT`.

## Clamp

Blender identifier: `ShaderNodeClamp`

### nd

- `nd.clamp(cls, value: Float=None, min: Float=None, max: Float=None, clamp_type: T_CLAMP_TYPE_1='MINMAX')` — class method; returns `OUT`.

### Float

- `Float.clamp(self, min: Float=None, max: Float=None, clamp_type: T_CLAMP_TYPE_1='MINMAX')` — method; returns `OUT`.

## Closure Input

Blender identifier: `NodeClosureInput`

### nd

- `nd.closure_input(cls)` — class method; returns `OUT`.

## Closure Output

Blender identifier: `NodeClosureOutput`

### nd

- `nd.closure_output(cls, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

## Color

Blender identifier: `ShaderNodeRGB`

### nd

- `nd.color(cls)` — property; returns `OUT`.

## Color Attribute

Blender identifier: `ShaderNodeVertexColor`

### nd

- `nd.color_attribute(cls, layer_name: str='')` — class method; returns `OUT`.

## Color Ramp

Blender identifier: `ShaderNodeValToRGB`

### nd

- `nd.color_ramp(cls, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.color_ramp(self)` — method; returns `OUT`.

## Combine Bundle

Blender identifier: `NodeCombineBundle`

### nd

- `nd.combine_bundle(cls, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

### Bundle

- `Bundle.Combine(cls, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

## Combine Color

Blender identifier: `ShaderNodeCombineColor`

### nd

- `nd.combine_color(cls, red: Float=None, green: Float=None, blue: Float=None, *, hue: Float=None, saturation: Float=None, value: Float=None, lightness: Float=None, mode: T_MODE_1='RGB')` — class method; returns `OUT`.

### Color

- `Color.Combine(cls, red: Float=None, green: Float=None, blue: Float=None, *, hue: Float=None, saturation: Float=None, value: Float=None, lightness: Float=None, mode: T_MODE_1='RGB')` — class method; returns `OUT`.
- `Color.CombineRGB(cls, red: Float=None, green: Float=None, blue: Float=None)` — class method; returns `OUT`.
- `Color.CombineHSV(cls, hue: Float=None, saturation: Float=None, value: Float=None)` — class method; returns `OUT`.
- `Color.CombineHSL(cls, hue: Float=None, saturation: Float=None, lightness: Float=None)` — class method; returns `OUT`.

## Combine XYZ

Blender identifier: `ShaderNodeCombineXYZ`

### nd

- `nd.combine_xyz(cls, x: Float=None, y: Float=None, z: Float=None)` — class method; returns `OUT`.

### Vector

- `Vector.CombineXYZ(cls, x: Float=None, y: Float=None, z: Float=None)` — class method; returns `OUT`.

## Comment

Blender identifier: `NodeComment`

### nd

- `nd.comment(cls, text: str='## Comment')` — class method; returns `NODE`.

## Curves Info

Blender identifier: `ShaderNodeHairInfo`

### nd

- `nd.curves_info(cls)` — class method; returns `OUT`.

## Diffuse BSDF

Blender identifier: `ShaderNodeBsdfDiffuse`

### nd

- `nd.diffuse_bsdf(cls, color: Color=None, roughness: Float=None, normal: Vector=None)` — class method; returns `OUT`.

### Shader

- `Shader.Diffuse(cls, color: Color=None, roughness: Float=None, normal: Vector=None)` — class method; returns `OUT`.

## Displacement

Blender identifier: `ShaderNodeDisplacement`

### nd

- `nd.displacement(cls, height: Float=None, midlevel: Float=None, scale: Float=None, normal: Vector=None, space: T_SPACE_1='OBJECT')` — class method; returns `OUT`.

### Float

- `Float.displacement(self, midlevel: Float=None, scale: Float=None, normal: Vector=None, space: T_SPACE_1='OBJECT')` — method; returns `OUT`.

## Emission

Blender identifier: `ShaderNodeEmission`

### nd

- `nd.emission(cls, color: Color=None, strength: Float=None)` — class method; returns `OUT`.

### Shader

- `Shader.Emission(cls, color: Color=None, strength: Float=None)` — class method; returns `OUT`.

## Enable Output

Blender identifier: `NodeEnableOutput`

### nd

- `nd.enable_output(cls, enable: Boolean=None, value: Socket=None, data_type: T_DATA_TYPE_1='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Integer

- `Integer.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Vector

- `Vector.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Color

- `Color.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### String

- `String.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Menu

- `Menu.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Shader

- `Shader.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Bundle

- `Bundle.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Closure

- `Closure.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

## Environment Texture

Blender identifier: `ShaderNodeTexEnvironment`

### nd

- `nd.environment_texture(cls, vector: Vector=None, image=None, projection: T_PROJECTION_1='EQUIRECTANGULAR', interpolation: T_INTERPOLATION_1='Linear')` — class method; returns `OUT`.

### Texture

- `Texture.Environment(cls, vector: Vector=None, image=None, projection: T_PROJECTION_1='EQUIRECTANGULAR', interpolation: T_INTERPOLATION_1='Linear')` — class method; returns `OUT`.

## Evaluate Closure

Blender identifier: `NodeEvaluateClosure`

### nd

- `nd.evaluate_closure(cls, closure: Closure=None, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

### Closure

- `Closure.evaluate(self, named_sockets: dict={}, define_signature: bool=False, **sockets)` — method; returns `OUT`.

## Find in String

Blender identifier: `FunctionNodeFindInString`

### nd

- `nd.find_in_string(cls, string: String=None, search: String=None, mode: Menu=None)` — class method; returns `OUT`.

### String

- `String.find_in_string(self, search: String=None, mode: Menu=None)` — method; returns `OUT`.

## Float Curve

Blender identifier: `ShaderNodeFloatCurve`

### nd

- `nd.float_curve(cls, value: Float=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.float_curve(self, value: Float=None)` — method; returns `OUT`.

## Format String

Blender identifier: `FunctionNodeFormatString`

### nd

- `nd.format_string(cls, format: String=None, named_sockets: dict={}, **sockets)` — class method; returns `OUT`.

### String

- `String.format(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

## Frame

Blender identifier: `NodeFrame`

### nd

- `nd.frame(cls, text=None, shrink: bool=True, label_size: int=20)` — class method; returns `NODE`.

## Fresnel

Blender identifier: `ShaderNodeFresnel`

### nd

- `nd.fresnel(cls, ior: Float=None, normal: Vector=None)` — class method; returns `OUT`.

## Gabor Texture

Blender identifier: `ShaderNodeTexGabor`

### nd

- `nd.gabor_texture(cls, vector: Vector=None, scale: Float=None, frequency: Float=None, anisotropy: Float=None, orientation: Socket=None, gabor_type: T_GABOR_TYPE_1='2D')` — class method; returns `OUT`.

### Texture

- `Texture.Gabor(cls, vector: Vector=None, scale: Float=None, frequency: Float=None, anisotropy: Float=None, orientation: Socket=None, gabor_type: T_GABOR_TYPE_1='2D')` — class method; returns `OUT`.

## Gamma

Blender identifier: `ShaderNodeGamma`

### nd

- `nd.gamma(cls, color: Color=None, gamma: Float=None)` — class method; returns `OUT`.

### Color

- `Color.gamma(self, gamma: Float=None)` — method; returns `OUT`.

## Geometry

Blender identifier: `ShaderNodeNewGeometry`

### nd

- `nd.geometry(cls)` — class method; returns `NODE`.

## Get Vector Component

Blender identifier: `FunctionNodeGetVectorComponent`

### nd

- `nd.get_vector_component(cls, vector: Vector=None, index: Integer=None)` — class method; returns `OUT`.

### Vector

- `Vector.get_component(self, index: Integer=None)` — method; returns `OUT`.

## Glass BSDF

Blender identifier: `ShaderNodeBsdfGlass`

### nd

- `nd.glass_bsdf(cls, color: Color=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, ior: Float=None, normal: Vector=None, tangent: Vector=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_1='MULTI_GGX')` — class method; returns `OUT`.

### Shader

- `Shader.Glass(cls, color: Color=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, ior: Float=None, normal: Vector=None, tangent: Vector=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_1='MULTI_GGX')` — class method; returns `OUT`.

## Glossy BSDF

Blender identifier: `ShaderNodeBsdfAnisotropic`

### nd

- `nd.glossy_bsdf(cls, color: Color=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, normal: Vector=None, tangent: Vector=None, distribution: T_DISTRIBUTION_2='MULTI_GGX')` — class method; returns `OUT`.

### Shader

- `Shader.Glossy(cls, color: Color=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, normal: Vector=None, tangent: Vector=None, distribution: T_DISTRIBUTION_2='MULTI_GGX')` — class method; returns `OUT`.

## Gradient Texture

Blender identifier: `ShaderNodeTexGradient`

### nd

- `nd.gradient_texture(cls, vector: Vector=None, gradient_type: T_GRADIENT_TYPE_1='LINEAR')` — class method; returns `OUT`.

### Texture

- `Texture.Gradient(cls, vector: Vector=None, gradient_type: T_GRADIENT_TYPE_1='LINEAR')` — class method; returns `OUT`.

## Group

Blender identifier: `ShaderNodeGroup`

### nd

- `nd.group(cls, node_tree=None)` — class method; returns `NODE`.

## Hair BSDF

Blender identifier: `ShaderNodeBsdfHair`

### nd

- `nd.hair_bsdf(cls, color: Color=None, offset: Float=None, roughnessu: Float=None, roughnessv: Float=None, tangent: Vector=None, component: T_COMPONENT_1='Reflection')` — class method; returns `OUT`.

### Shader

- `Shader.Hair(cls, color: Color=None, offset: Float=None, roughnessu: Float=None, roughnessv: Float=None, tangent: Vector=None, component: T_COMPONENT_1='Reflection')` — class method; returns `OUT`.

## Holdout

Blender identifier: `ShaderNodeHoldout`

### nd

- `nd.holdout(cls)` — property; returns `OUT`.

### Shader

- `Shader.Holdout(cls)` — class method; returns `OUT`.

## Hue/Saturation/Value

Blender identifier: `ShaderNodeHueSaturation`

### nd

- `nd.hue_saturation_value(cls, hue: Float=None, saturation: Float=None, value: Float=None, color: Color=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.hue_saturation_value(self, saturation: Float=None, value: Float=None, color: Color=None, factor: Float=None)` — method; returns `OUT`.

## IES Texture

Blender identifier: `ShaderNodeTexIES`

### nd

- `nd.ies_texture(cls, vector: Vector=None, strength: Float=None, ies=None, filepath: str='', mode: T_MODE_2='INTERNAL')` — class method; returns `OUT`.

### Texture

- `Texture.IES(cls, vector: Vector=None, strength: Float=None, ies=None, filepath: str='', mode: T_MODE_2='INTERNAL')` — class method; returns `OUT`.

## Image Texture

Blender identifier: `ShaderNodeTexImage`

### nd

- `nd.image_texture(cls, vector: Vector=None, image=None, projection_blend: float=0.0, projection: T_PROJECTION_2='FLAT', interpolation: T_INTERPOLATION_1='Linear', extension: T_EXTENSION_1='REPEAT')` — class method; returns `OUT`.

### Texture

- `Texture.Image(cls, vector: Vector=None, image=None, projection_blend: float=0.0, projection: T_PROJECTION_2='FLAT', interpolation: T_INTERPOLATION_1='Linear', extension: T_EXTENSION_1='REPEAT')` — class method; returns `OUT`.

## Implicit Conversion

Blender identifier: `NodeImplicitConversion`

### nd

- `nd.implicit_conversion(cls, value: Socket=None, socket_idname: str='NodeSocketColor', data_type: T_DATA_TYPE_1='RGBA')` — class method; returns `OUT`.

### Float

- `Float.implicit_conversion(self, socket_idname: str='NodeSocketFloat')` — method; returns `OUT`.

### Integer

- `Integer.implicit_conversion(self, socket_idname: str='NodeSocketInt')` — method; returns `OUT`.

### Boolean

- `Boolean.implicit_conversion(self, socket_idname: str='NodeSocketBool')` — method; returns `OUT`.

### Vector

- `Vector.implicit_conversion(self, socket_idname: str='NodeSocketVector')` — method; returns `OUT`.

### Color

- `Color.implicit_conversion(self, socket_idname: str='NodeSocketColor')` — method; returns `OUT`.

### String

- `String.implicit_conversion(self, socket_idname: str='NodeSocketString')` — method; returns `OUT`.

### Menu

- `Menu.implicit_conversion(self, socket_idname: str='NodeSocketMenu')` — method; returns `OUT`.

### Shader

- `Shader.implicit_conversion(self, socket_idname: str='NodeSocketShader')` — method; returns `OUT`.

### Bundle

- `Bundle.implicit_conversion(self, socket_idname: str='NodeSocketBundle')` — method; returns `OUT`.

### Closure

- `Closure.implicit_conversion(self, socket_idname: str='NodeSocketClosure')` — method; returns `OUT`.

## Index Switch

Blender identifier: `GeometryNodeIndexSwitch`

### nd

- `nd.index_switch(cls, *items, index: Integer=None, data_type: T_DATA_TYPE_1='RGBA')` — class method; returns `OUT`.

### Float

- `Float.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Boolean

- `Boolean.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Color

- `Color.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### String

- `String.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Menu

- `Menu.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Shader

- `Shader.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Bundle

- `Bundle.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Closure

- `Closure.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

## Integer

Blender identifier: `FunctionNodeInputInt`

### nd

- `nd.integer(cls, integer: int=0)` — class method; returns `OUT`.

## Integer Math

Blender identifier: `FunctionNodeIntegerMath`

### nd

- `nd.integer_math(cls, value: Integer=None, value_1: Integer=None, addend: Integer=None, *, base: Integer=None, multiplier: Integer=None, exponent: Integer=None, operation: T_OPERATION_2='ADD')` — class method; returns `OUT`.

### gnmath

- `gnmath.iadd(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.isubtract(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.imultiply(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.idivide(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.ipower(base: Integer=None, exponent: Integer=None)` — method; returns `OUT`.
- `gnmath.imodulo(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.iabs(value: Integer=None)` — method; returns `OUT`.
- `gnmath.negate(value: Integer=None)` — method; returns `OUT`.
- `gnmath.imultiply_add(value: Integer=None, multiplier: Integer=None, addend: Integer=None)` — method; returns `OUT`.
- `gnmath.isign(value: Integer=None)` — method; returns `OUT`.
- `gnmath.imin(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.imax(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.divide_round(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.divide_floor(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.divide_ceil(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.ifloored_modulo(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.gcd(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.lcm(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.add(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__add__(self, other)` — method; returns `OUT`.
- `Integer.__radd__(self, other)` — method; returns `OUT`.
- `Integer.__iadd__(self, other)` — method; returns `OUT`.
- `Integer.subtract(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__sub__(self, other)` — method; returns `OUT`.
- `Integer.__rsub__(self, other)` — method; returns `OUT`.
- `Integer.__isub__(self, other)` — method; returns `OUT`.
- `Integer.multiply(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__mul__(self, other)` — method; returns `OUT`.
- `Integer.__rmul__(self, other)` — method; returns `OUT`.
- `Integer.__imul__(self, other)` — method; returns `OUT`.
- `Integer.divide(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__floordiv__(self, other)` — method; returns `OUT`.
- `Integer.__rfloordiv__(self, other)` — method; returns `OUT`.
- `Integer.__ifloordiv__(self, other)` — method; returns `OUT`.
- `Integer.power(self, exponent: Integer=None)` — method; returns `OUT`.
- `Integer.__pow__(self, other)` — method; returns `OUT`.
- `Integer.__rpow__(self, other)` — method; returns `OUT`.
- `Integer.__ipow__(self, other)` — method; returns `OUT`.
- `Integer.modulo(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__mod__(self, other)` — method; returns `OUT`.
- `Integer.__rmod__(self, other)` — method; returns `OUT`.
- `Integer.__imod__(self, other)` — method; returns `OUT`.
- `Integer.abs(self)` — method; returns `OUT`.
- `Integer.__abs__(self)` — method; returns `OUT`.
- `Integer.negate(self)` — method; returns `OUT`.
- `Integer.__neg__(self)` — method; returns `OUT`.
- `Integer.multiply_add(self, multiplier: Integer=None, addend: Integer=None)` — method; returns `OUT`.
- `Integer.sign(self)` — method; returns `OUT`.
- `Integer.min(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.max(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.divide_round(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.divide_floor(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.divide_ceil(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.floored_modulo(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.gcd(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.lcm(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.integer_math(self, value: Integer=None, addend: Integer=None, *, multiplier: Integer=None, exponent: Integer=None, operation: T_OPERATION_2='ADD')` — method; returns `OUT`.

## Invert Color

Blender identifier: `ShaderNodeInvert`

### nd

- `nd.invert_color(cls, color: Color=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.invert_color(self, color: Color=None)` — method; returns `OUT`.

## Join Bundle

Blender identifier: `NodeJoinBundle`

### nd

- `nd.join_bundle(cls, *bundle: Bundle)` — class method; returns `OUT`.

### Bundle

- `Bundle.join(self, *bundle: Bundle)` — method; returns `OUT`.

## Layer Weight

Blender identifier: `ShaderNodeLayerWeight`

### nd

- `nd.layer_weight(cls, blend: Float=None, normal: Vector=None)` — class method; returns `OUT`.

## Light Accumulation

Blender identifier: `ShaderNodeLightAccumulation`

### nd

- `nd.light_accumulation(cls, diffuse_light: Color=None, diffuse_color: Color=None, glossy_light: Color=None, glossy_color: Color=None, transmission_light: Color=None, transmission_color: Color=None)` — class method; returns `OUT`.

### Shader

- `Shader.LightAccumulation(cls, diffuse_light: Color=None, diffuse_color: Color=None, glossy_light: Color=None, glossy_color: Color=None, transmission_light: Color=None, transmission_color: Color=None)` — class method; returns `OUT`.

## Light Evaluation

Blender identifier: `ShaderNodeLightEvaluation`

### nd

- `nd.light_evaluation(cls, position: Vector=None, normal: Vector=None, roughness: Float=None, mode: T_MODE_3='DIFFUSE')` — class method; returns `OUT`.

## Light Falloff

Blender identifier: `ShaderNodeLightFalloff`

### nd

- `nd.light_falloff(cls, strength: Float=None, smooth: Float=None)` — class method; returns `OUT`.

### Float

- `Float.light_falloff(self, smooth: Float=None)` — method; returns `OUT`.

## Light Info

Blender identifier: `ShaderNodeLightInfo`

### nd

- `nd.light_info(cls)` — class method; returns `OUT`.

## Light Iter Internal Input

Blender identifier: `ShaderNodeLightIterInternalInput`

### nd

- `nd.light_iter_internal_input(cls)` — property; returns `OUT`.

### Integer

- `Integer.LightIterInternalInput(cls)` — class method; returns `OUT`.

## Light Iter Internal Output

Blender identifier: `ShaderNodeLightIterInternalOutput`

### nd

- `nd.light_iter_internal_output(cls)` — class method; returns `NODE`.

## Light Output

Blender identifier: `ShaderNodeOutputLight`

### nd

- `nd.light_output(cls, surface: Shader=None, is_active_output: bool=True, target: T_TARGET_1='ALL')` — class method; returns `NODE`.

### Shader

- `Shader.light_output(self, is_active_output: bool=True, target: T_TARGET_1='ALL')` — method; returns `NODE`.

## Light Path

Blender identifier: `ShaderNodeLightPath`

### nd

- `nd.light_path(cls)` — class method; returns `OUT`.

## Magic Texture

Blender identifier: `ShaderNodeTexMagic`

### nd

- `nd.magic_texture(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, turbulence_depth: int=2)` — class method; returns `OUT`.

### Texture

- `Texture.Magic(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, turbulence_depth: int=2)` — class method; returns `OUT`.

## Map Range

Blender identifier: `ShaderNodeMapRange`

### nd

- `nd.map_range(cls, value: Float=None, from_min: Socket=None, from_max: Socket=None, to_min: Socket=None, to_max: Socket=None, steps: Socket=None, vector: Vector=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR', data_type: T_DATA_TYPE_2='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.map_range(self, from_min: Float=None, from_max: Float=None, to_min: Float=None, to_max: Float=None, steps: Float=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.
- `Float.interpolate(self, to_min: Float=None, to_max: Float=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.

### Vector

- `Vector.map_range(self, from_min: Vector=None, from_max: Vector=None, to_min: Vector=None, to_max: Vector=None, steps: Vector=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.
- `Vector.interpolate(self, to_min: Vector=None, to_max: Vector=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.

## Mapping

Blender identifier: `ShaderNodeMapping`

### nd

- `nd.mapping(cls, vector: Vector=None, location: Vector=None, rotation: Vector=None, scale: Vector=None, vector_type: T_VECTOR_TYPE_1='POINT')` — class method; returns `OUT`.

### Vector

- `Vector.mapping(self, location: Vector=None, rotation: Vector=None, scale: Vector=None, vector_type: T_VECTOR_TYPE_1='POINT')` — method; returns `OUT`.

## Match String

Blender identifier: `FunctionNodeMatchString`

### nd

- `nd.match_string(cls, string: String=None, key: String=None, operation: Menu=None)` — class method; returns `OUT`.

### String

- `String.match(self, key: String=None, operation: Menu=None)` — method; returns `OUT`.

## Material Output

Blender identifier: `ShaderNodeOutputMaterial`

### nd

- `nd.material_output(cls, surface: Shader=None, volume: VolumeShader=None, displacement: Vector=None, thickness: Float=None, is_active_output: bool=True, target: T_TARGET_1='ALL')` — class method; returns `NODE`.

## Math

Blender identifier: `ShaderNodeMath`

### nd

- `nd.math(cls, value: Float=None, value_1: Float=None, addend: Float=None, *, base: Float=None, degrees: Float=None, radians: Float=None, multiplier: Float=None, exponent: Float=None, base_1: Float=None, threshold: Float=None, max: Float=None, increment: Float=None, scale: Float=None, epsilon: Float=None, distance: Float=None, min: Float=None, use_clamp: bool=False, operation: T_OPERATION_3='ADD')` — class method; returns `OUT`.

### gnmath

- `gnmath.add(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.subtract(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.multiply(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.divide(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.power(base: Float=None, exponent: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.modulo(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.abs(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.round(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.trunc(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.floor(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.ceil(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.multiply_add(value: Float=None, multiplier: Float=None, addend: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.log(value: Float=None, base: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sqrt(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.inverse_sqrt(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.exp(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.min(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.max(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sign(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.smooth_min(value: Float=None, value_1: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.smooth_max(value: Float=None, value_1: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.fract(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.floored_modulo(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.wrap(value: Float=None, max: Float=None, min: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.snap(value: Float=None, increment: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.pingpong(value: Float=None, scale: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sin(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.cos(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.tan(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.asin(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.acos(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.arctangent(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.atan2(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sinh(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.cosh(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.tanh(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.radians(degrees: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.degrees(radians: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.less_than(value: Float=None, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.greater_than(value: Float=None, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.compare(value: Float=None, value_1: Float=None, epsilon: Float=None, use_clamp: bool=False)` — method; returns `OUT`.

### Float

- `Float.add(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__add__(self, other)` — method; returns `OUT`.
- `Float.__radd__(self, other)` — method; returns `OUT`.
- `Float.__iadd__(self, other)` — method; returns `OUT`.
- `Float.subtract(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__sub__(self, other)` — method; returns `OUT`.
- `Float.__rsub__(self, other)` — method; returns `OUT`.
- `Float.__isub__(self, other)` — method; returns `OUT`.
- `Float.multiply(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__mul__(self, other)` — method; returns `OUT`.
- `Float.__rmul__(self, other)` — method; returns `OUT`.
- `Float.__imul__(self, other)` — method; returns `OUT`.
- `Float.__neg__(self)` — method; returns `OUT`.
- `Float.divide(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__truediv__(self, other)` — method; returns `OUT`.
- `Float.__rtruediv__(self, other)` — method; returns `OUT`.
- `Float.__itruediv__(self, other)` — method; returns `OUT`.
- `Float.power(self, exponent: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__pow__(self, other)` — method; returns `OUT`.
- `Float.__rpow__(self, other)` — method; returns `OUT`.
- `Float.__ipow__(self, other)` — method; returns `OUT`.
- `Float.modulo(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__mod__(self, other)` — method; returns `OUT`.
- `Float.__rmod__(self, other)` — method; returns `OUT`.
- `Float.__imod__(self, other)` — method; returns `OUT`.
- `Float.abs(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__abs__(self)` — method; returns `OUT`.
- `Float.round(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__round__(self)` — method; returns `OUT`.
- `Float.trunc(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__trunc__(self)` — method; returns `OUT`.
- `Float.floor(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__floor__(self)` — method; returns `OUT`.
- `Float.ceil(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__ceil__(self)` — method; returns `OUT`.
- `Float.multiply_add(self, multiplier: Float=None, addend: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.log(self, base: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sqrt(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.inverse_sqrt(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.exp(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.min(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.max(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sign(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.smooth_min(self, value: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.smooth_max(self, value: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.fract(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.floored_modulo(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.wrap(self, max: Float=None, min: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.snap(self, increment: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.pingpong(self, scale: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sin(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.cos(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.tan(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.asin(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.acos(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.arctangent(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.atan2(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sinh(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.cosh(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.tanh(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.radians(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.degrees(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.less_than(self, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.greater_than(self, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.compare(self, value: Float=None, epsilon: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.math(self, value: Float=None, addend: Float=None, *, multiplier: Float=None, exponent: Float=None, base: Float=None, threshold: Float=None, max: Float=None, increment: Float=None, scale: Float=None, epsilon: Float=None, distance: Float=None, min: Float=None, use_clamp: bool=False, operation: T_OPERATION_3='ADD')` — method; returns `OUT`.

## Menu

Blender identifier: `FunctionNodeInputMenu`

### nd

- `nd.menu(cls, value: str='')` — class method; returns `OUT`.

## Menu Switch

Blender identifier: `GeometryNodeMenuSwitch`

### nd

- `nd.menu_switch(cls, named_sockets: dict={}, menu: Menu=None, data_type: T_DATA_TYPE_1='RGBA', **sockets)` — class method; returns `OUT`.

### Float

- `Float.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Integer

- `Integer.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Boolean

- `Boolean.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Vector

- `Vector.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Color

- `Color.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### String

- `String.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Menu

- `Menu.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Shader

- `Shader.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Bundle

- `Bundle.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Closure

- `Closure.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

## Metallic BSDF

Blender identifier: `ShaderNodeBsdfMetallic`

### nd

- `nd.metallic_bsdf(cls, base_color: Color=None, edge_tint: Color=None, ior: Vector=None, extinction: Vector=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, normal: Vector=None, tangent: Vector=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_1='MULTI_GGX', fresnel_type: T_FRESNEL_TYPE_1='F82')` — class method; returns `OUT`.

### Shader

- `Shader.Metallic(cls, base_color: Color=None, edge_tint: Color=None, ior: Vector=None, extinction: Vector=None, roughness: Float=None, anisotropy: Float=None, rotation: Float=None, normal: Vector=None, tangent: Vector=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_1='MULTI_GGX', fresnel_type: T_FRESNEL_TYPE_1='F82')` — class method; returns `OUT`.

## Mix

Blender identifier: `ShaderNodeMix`

### nd

- `nd.mix(cls, a: Socket=None, b: Socket=None, factor: Socket=None, clamp_factor: bool=True, clamp_result: bool=False, data_type: T_DATA_TYPE_3='FLOAT', factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.

### Float

- `Float.Mix(cls, a: Float=None, b: Float=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Float.mix(self, b: Float=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

### Vector

- `Vector.Mix(cls, a: Vector=None, b: Vector=None, factor: Socket=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Vector.mix(self, b: Vector=None, factor: Socket=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

### Color

- `Color.Mix(cls, a: Color=None, b: Color=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Color.mix(self, b: Color=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

## Mix (Legacy)

Blender identifier: `ShaderNodeMixRGB`

### nd

- `nd.mix_legacy_(cls, color1: Color=None, color2: Color=None, factor: Float=None, use_alpha: bool=False, use_clamp: bool=False, blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.

### Float

- `Float.mix_legacy_(self, color1: Color=None, color2: Color=None, use_alpha: bool=False, use_clamp: bool=False, blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

## Mix Shader

Blender identifier: `ShaderNodeMixShader`

### nd

- `nd.mix_shader(cls, shader: Shader=None, shader_1: Shader=None, factor: Float=None)` — class method; returns `OUT`.

### Shader

- `Shader.MixShader(cls, shader: Shader=None, shader_1: Shader=None, factor: Float=None)` — class method; returns `OUT`.

## Noise Texture

Blender identifier: `ShaderNodeTexNoise`

### nd

- `nd.noise_texture(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, offset: Float=None, gain: Float=None, distortion: Float=None, normalize: bool=True, noise_dimensions: T_NOISE_DIMENSIONS_1='3D', noise_type: T_NOISE_TYPE_1='FBM')` — class method; returns `OUT`.

### Texture

- `Texture.Noise(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, offset: Float=None, gain: Float=None, distortion: Float=None, normalize: bool=True, noise_dimensions: T_NOISE_DIMENSIONS_1='3D', noise_type: T_NOISE_TYPE_1='FBM')` — class method; returns `OUT`.

## Normal

Blender identifier: `ShaderNodeNormal`

### nd

- `nd.normal(cls, normal: Vector=None)` — property; returns `Normal`.
- `nd.true_normal(cls, normal: Vector=None)` — property; returns `True Normal`.

### Vector

- `Vector.normal(cls, normal: Vector=None)` — property; returns `Normal`.
- `Vector.true_normal(cls, normal: Vector=None)` — property; returns `True Normal`.

## Normal Map

Blender identifier: `ShaderNodeNormalMap`

### nd

- `nd.normal_map(cls, strength: Float=None, color: Color=None, uv_map: str='', space: T_SPACE_2='TANGENT', convention: T_CONVENTION_1='OPENGL', base: T_BASE_1='DISPLACED')` — class method; returns `OUT`.

### Float

- `Float.normal_map(self, color: Color=None, uv_map: str='', space: T_SPACE_2='TANGENT', convention: T_CONVENTION_1='OPENGL', base: T_BASE_1='DISPLACED')` — method; returns `OUT`.

## Object Info

Blender identifier: `ShaderNodeObjectInfo`

### nd

- `nd.object_info(cls)` — class method; returns `OUT`.

## Particle Info

Blender identifier: `ShaderNodeParticleInfo`

### nd

- `nd.particle_info(cls)` — class method; returns `OUT`.

## Point Info

Blender identifier: `ShaderNodePointInfo`

### nd

- `nd.point_info(cls)` — class method; returns `OUT`.

## Principled BSDF

Blender identifier: `ShaderNodeBsdfPrincipled`

### nd

- `nd.principled_bsdf(cls, base_color: Color=None, metallic: Float=None, roughness: Float=None, ior: Float=None, alpha: Float=None, thin_wall: Boolean=None, normal: Vector=None, diffuse_roughness: Float=None, subsurface_weight: Float=None, subsurface_radius: Vector=None, subsurface_scale: Float=None, subsurface_ior: Float=None, subsurface_anisotropy: Float=None, specular_ior_level: Float=None, specular_tint: Color=None, anisotropic: Float=None, anisotropic_rotation: Float=None, tangent: Vector=None, transmission_weight: Float=None, transmission_dispersion_scale: Float=None, transmission_dispersion_abbe_number: Float=None, coat_weight: Float=None, coat_roughness: Float=None, coat_ior: Float=None, coat_tint: Color=None, coat_normal: Vector=None, sheen_weight: Float=None, sheen_roughness: Float=None, sheen_tint: Color=None, emission_color: Color=None, emission_strength: Float=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_3='MULTI_GGX', subsurface_method: T_SUBSURFACE_METHOD_1='RANDOM_WALK')` — class method; returns `OUT`.

### Shader

- `Shader.Principled(cls, base_color: Color=None, metallic: Float=None, roughness: Float=None, ior: Float=None, alpha: Float=None, thin_wall: Boolean=None, normal: Vector=None, diffuse_roughness: Float=None, subsurface_weight: Float=None, subsurface_radius: Vector=None, subsurface_scale: Float=None, subsurface_ior: Float=None, subsurface_anisotropy: Float=None, specular_ior_level: Float=None, specular_tint: Color=None, anisotropic: Float=None, anisotropic_rotation: Float=None, tangent: Vector=None, transmission_weight: Float=None, transmission_dispersion_scale: Float=None, transmission_dispersion_abbe_number: Float=None, coat_weight: Float=None, coat_roughness: Float=None, coat_ior: Float=None, coat_tint: Color=None, coat_normal: Vector=None, sheen_weight: Float=None, sheen_roughness: Float=None, sheen_tint: Color=None, emission_color: Color=None, emission_strength: Float=None, thin_film_thickness: Float=None, thin_film_ior: Float=None, distribution: T_DISTRIBUTION_3='MULTI_GGX', subsurface_method: T_SUBSURFACE_METHOD_1='RANDOM_WALK')` — class method; returns `OUT`.

## Principled Hair BSDF

Blender identifier: `ShaderNodeBsdfHairPrincipled`

### nd

- `nd.principled_hair_bsdf(cls, color: Color=None, melanin: Float=None, melanin_redness: Float=None, tint: Color=None, absorption_coefficient: Vector=None, aspect_ratio: Float=None, roughness: Float=None, radial_roughness: Float=None, coat: Float=None, ior: Float=None, offset: Float=None, random_color: Float=None, random_roughness: Float=None, random: Float=None, reflection: Float=None, transmission: Float=None, secondary_reflection: Float=None, model: T_MODEL_1='CHIANG', parametrization: T_PARAMETRIZATION_1='COLOR')` — class method; returns `OUT`.

### Shader

- `Shader.PrincipledHair(cls, color: Color=None, melanin: Float=None, melanin_redness: Float=None, tint: Color=None, absorption_coefficient: Vector=None, aspect_ratio: Float=None, roughness: Float=None, radial_roughness: Float=None, coat: Float=None, ior: Float=None, offset: Float=None, random_color: Float=None, random_roughness: Float=None, random: Float=None, reflection: Float=None, transmission: Float=None, secondary_reflection: Float=None, model: T_MODEL_1='CHIANG', parametrization: T_PARAMETRIZATION_1='COLOR')` — class method; returns `OUT`.

## Principled Volume

Blender identifier: `ShaderNodeVolumePrincipled`

### nd

- `nd.principled_volume(cls, color: Color=None, color_attribute: String=None, density: Float=None, density_attribute: String=None, anisotropy: Float=None, absorption_color: Color=None, emission_strength: Float=None, emission_color: Color=None, blackbody_intensity: Float=None, blackbody_tint: Color=None, temperature: Float=None, temperature_attribute: String=None)` — class method; returns `OUT`.

### VolumeShader

- `VolumeShader.Principled(cls, color: Color=None, color_attribute: String=None, density: Float=None, density_attribute: String=None, anisotropy: Float=None, absorption_color: Color=None, emission_strength: Float=None, emission_color: Color=None, blackbody_intensity: Float=None, blackbody_tint: Color=None, temperature: Float=None, temperature_attribute: String=None)` — class method; returns `OUT`.

## RGB Curves

Blender identifier: `ShaderNodeRGBCurve`

### nd

- `nd.rgb_curves(cls, color: Color=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.rgb_curves(self, color: Color=None)` — method; returns `OUT`.

## RGB to BW

Blender identifier: `ShaderNodeRGBToBW`

### nd

- `nd.rgb_to_bw(cls, color: Color=None)` — class method; returns `OUT`.

### Color

- `Color.rgb_to_bw(self)` — method; returns `OUT`.

## Radial Tiling

Blender identifier: `ShaderNodeRadialTiling`

### nd

- `nd.radial_tiling(cls, vector: Vector=None, sides: Float=None, roundness: Float=None, normalize: bool=False)` — class method; returns `OUT`.

### Vector

- `Vector.radial_tiling(self, sides: Float=None, roundness: Float=None, normalize: bool=False)` — method; returns `OUT`.

## Ray Portal BSDF

Blender identifier: `ShaderNodeBsdfRayPortal`

### nd

- `nd.ray_portal_bsdf(cls, color: Color=None, position: Vector=None, direction: Vector=None)` — class method; returns `OUT`.

### Shader

- `Shader.RayPortal(cls, color: Color=None, position: Vector=None, direction: Vector=None)` — class method; returns `OUT`.

## Raycast

Blender identifier: `ShaderNodeRaycast`

### nd

- `nd.raycast(cls, position: Vector=None, direction: Vector=None, length: Float=None, named_sockets: dict={}, only_local: bool=False, **sockets)` — class method; returns `OUT`.

## Refraction BSDF

Blender identifier: `ShaderNodeBsdfRefraction`

### nd

- `nd.refraction_bsdf(cls, color: Color=None, roughness: Float=None, ior: Float=None, normal: Vector=None, distribution: T_DISTRIBUTION_4='BECKMANN')` — class method; returns `OUT`.

### Shader

- `Shader.Refraction(cls, color: Color=None, roughness: Float=None, ior: Float=None, normal: Vector=None, distribution: T_DISTRIBUTION_4='BECKMANN')` — class method; returns `OUT`.

## Replace String

Blender identifier: `FunctionNodeReplaceString`

### nd

- `nd.replace_string(cls, string: String=None, find: String=None, replace: String=None)` — class method; returns `OUT`.

### String

- `String.replace(self, find: String=None, replace: String=None)` — method; returns `OUT`.

## Reverse String

Blender identifier: `FunctionNodeReverseString`

### nd

- `nd.reverse_string(cls, string: String=None)` — class method; returns `OUT`.

### String

- `String.reverse(self)` — method; returns `OUT`.

## Scene Time

Blender identifier: `GeometryNodeInputSceneTime`

### nd

- `nd.scene_time(cls)` — class method; returns `OUT`.

## Script

Blender identifier: `ShaderNodeScript`

### nd

- `nd.script(cls, script=None, filepath: str='', use_auto_update: bool=False, bytecode: str='', bytecode_hash: str='', mode: T_MODE_2='INTERNAL')` — class method; returns `NODE`.

## Separate Bundle

Blender identifier: `NodeSeparateBundle`

### nd

- `nd.separate_bundle(cls, bundle: Bundle=None, define_signature: bool=False)` — class method; returns `OUT`.

### Bundle

- `Bundle.separate(self, define_signature: bool=False)` — method; returns `OUT`.

## Separate Color

Blender identifier: `ShaderNodeSeparateColor`

### nd

- `nd.separate_color(cls, color: Color=None, mode: T_MODE_1='RGB')` — class method; returns `OUT`.

### Color

- `Color.separate(self, mode: T_MODE_1='RGB')` — method; returns `OUT`.

## Separate XYZ

Blender identifier: `ShaderNodeSeparateXYZ`

### nd

- `nd.separate_xyz(cls, vector: Vector=None)` — class method; returns `OUT`.

### Vector

- `Vector.separate_xyz(self)` — method; returns `OUT`.

## Set String Case

Blender identifier: `FunctionNodeSetStringCase`

### nd

- `nd.set_string_case(cls, string: String=None, case: Menu=None)` — class method; returns `OUT`.

### String

- `String.set_string_case(self, case: Menu=None)` — method; returns `OUT`.

## Shader to RGB

Blender identifier: `ShaderNodeShaderToRGB`

### nd

- `nd.shader_to_rgb(cls, shader: Shader=None)` — class method; returns `OUT`.

### Shader

- `Shader.shader_to_rgb(self)` — method; returns `OUT`.

## Shadow Raycast

Blender identifier: `ShaderNodeShadowRaycast`

### nd

- `nd.shadow_raycast(cls, position: Vector=None, softness: Float=None)` — class method; returns `OUT`.

## Sheen BSDF

Blender identifier: `ShaderNodeBsdfSheen`

### nd

- `nd.sheen_bsdf(cls, color: Color=None, roughness: Float=None, normal: Vector=None, distribution: T_DISTRIBUTION_5='MICROFIBER')` — class method; returns `OUT`.

### Shader

- `Shader.Sheen(cls, color: Color=None, roughness: Float=None, normal: Vector=None, distribution: T_DISTRIBUTION_5='MICROFIBER')` — class method; returns `OUT`.

## Sky Texture

Blender identifier: `ShaderNodeTexSky`

### nd

- `nd.sky_texture(cls, vector: Vector=None, sun_disc: bool=True, sun_size: float=0.009512044489383698, sun_intensity: float=1.0, sun_elevation: float=0.2617993950843811, sun_rotation: float=0.0, altitude: float=100.0, air_density: float=1.0, aerosol_density: float=1.0, ozone_density: float=1.0, turbidity: float=2.200000047683716, ground_albedo: float=0.30000001192092896, sky_type: T_SKY_TYPE_1='MULTIPLE_SCATTERING')` — class method; returns `OUT`.

### Texture

- `Texture.Sky(cls, vector: Vector=None, sun_disc: bool=True, sun_size: float=0.009512044489383698, sun_intensity: float=1.0, sun_elevation: float=0.2617993950843811, sun_rotation: float=0.0, altitude: float=100.0, air_density: float=1.0, aerosol_density: float=1.0, ozone_density: float=1.0, turbidity: float=2.200000047683716, ground_albedo: float=0.30000001192092896, sky_type: T_SKY_TYPE_1='MULTIPLE_SCATTERING')` — class method; returns `OUT`.

## Slice String

Blender identifier: `FunctionNodeSliceString`

### nd

- `nd.slice_string(cls, string: String=None, position: Integer=None, length: Integer=None)` — class method; returns `OUT`.

### String

- `String.slice(self, position: Integer=None, length: Integer=None)` — method; returns `OUT`.

## Special Characters

Blender identifier: `FunctionNodeInputSpecialCharacters`

### nd

- `nd.special_characters(cls)` — class method; returns `OUT`.

### String

- `String.line_break(cls)` — property; returns `Line Break`.
- `String.tab(cls)` — property; returns `Tab`.

## Specular BSDF

Blender identifier: `ShaderNodeEeveeSpecular`

### nd

- `nd.specular_bsdf(cls, base_color: Color=None, specular: Color=None, roughness: Float=None, emissive_color: Color=None, transparency: Float=None, normal: Vector=None, clear_coat: Float=None, clear_coat_roughness: Float=None, clear_coat_normal: Vector=None)` — class method; returns `OUT`.

### Shader

- `Shader.Specular(cls, base_color: Color=None, specular: Color=None, roughness: Float=None, emissive_color: Color=None, transparency: Float=None, normal: Vector=None, clear_coat: Float=None, clear_coat_roughness: Float=None, clear_coat_normal: Vector=None)` — class method; returns `OUT`.

## Squeeze Value (Legacy)

Blender identifier: `ShaderNodeSqueeze`

### nd

- `nd.squeeze_value_legacy_(cls, value: Float=None, width: Float=None, center: Float=None)` — class method; returns `OUT`.

### Float

- `Float.squeeze_value_legacy_(self, width: Float=None, center: Float=None)` — method; returns `OUT`.

## String

Blender identifier: `FunctionNodeInputString`

### nd

- `nd.string(cls, string: str='')` — class method; returns `OUT`.

## String Length

Blender identifier: `FunctionNodeStringLength`

### nd

- `nd.string_length(cls, string: String=None)` — class method; returns `OUT`.

### String

- `String.length(self)` — method; returns `OUT`.

## String to Value

Blender identifier: `FunctionNodeStringToValue`

### nd

- `nd.string_to_value(cls, string: String=None, base: Integer=None, data_type: T_DATA_TYPE_4='FLOAT')` — class method; returns `OUT`.

### String

- `String.to_value(self, base: Integer=None, data_type: T_DATA_TYPE_4='FLOAT')` — method; returns `OUT`.

### Float

- `Float.FromString(cls, string: String=None, base: Integer=None, data_type: T_DATA_TYPE_4='FLOAT')` — class method; returns `OUT`.

## Subsurface Scattering

Blender identifier: `ShaderNodeSubsurfaceScattering`

### nd

- `nd.subsurface_scattering(cls, color: Color=None, scale: Float=None, radius: Vector=None, ior: Float=None, roughness: Float=None, anisotropy: Float=None, normal: Vector=None, falloff: T_SUBSURFACE_METHOD_1='RANDOM_WALK')` — class method; returns `OUT`.

### Shader

- `Shader.SubsurfaceScattering(cls, color: Color=None, scale: Float=None, radius: Vector=None, ior: Float=None, roughness: Float=None, anisotropy: Float=None, normal: Vector=None, falloff: T_SUBSURFACE_METHOD_1='RANDOM_WALK')` — class method; returns `OUT`.

## Switch

Blender identifier: `GeometryNodeSwitch`

### nd

- `nd.switch(cls, switch: Boolean=None, false: Socket=None, true: Socket=None, input_type: T_DATA_TYPE_1='RGBA')` — class method; returns `OUT`.

### Float

- `Float.switch(self, switch: Boolean=None, true: Float=None)` — method; returns `OUT`.
- `Float.switch_false(self, switch: Boolean=None, false: Float=None)` — method; returns `OUT`.
- `Float.Switch(cls, switch: Boolean=None, false: Float=None, true: Float=None)` — class method; returns `cls`.

### Integer

- `Integer.switch(self, switch: Boolean=None, true: Integer=None)` — method; returns `OUT`.
- `Integer.switch_false(self, switch: Boolean=None, false: Integer=None)` — method; returns `OUT`.
- `Integer.Switch(cls, switch: Boolean=None, false: Integer=None, true: Integer=None)` — class method; returns `cls`.

### Boolean

- `Boolean.switch(self, switch: Boolean=None, true: Boolean=None)` — method; returns `OUT`.
- `Boolean.switch_false(self, switch: Boolean=None, false: Boolean=None)` — method; returns `OUT`.
- `Boolean.Switch(cls, switch: Boolean=None, false: Boolean=None, true: Boolean=None)` — class method; returns `cls`.

### Vector

- `Vector.switch(self, switch: Boolean=None, true: Vector=None)` — method; returns `OUT`.
- `Vector.switch_false(self, switch: Boolean=None, false: Vector=None)` — method; returns `OUT`.
- `Vector.Switch(cls, switch: Boolean=None, false: Vector=None, true: Vector=None)` — class method; returns `cls`.

### Color

- `Color.switch(self, switch: Boolean=None, true: Color=None)` — method; returns `OUT`.
- `Color.switch_false(self, switch: Boolean=None, false: Color=None)` — method; returns `OUT`.
- `Color.Switch(cls, switch: Boolean=None, false: Color=None, true: Color=None)` — class method; returns `cls`.

### String

- `String.switch(self, switch: Boolean=None, true: String=None)` — method; returns `OUT`.
- `String.switch_false(self, switch: Boolean=None, false: String=None)` — method; returns `OUT`.
- `String.Switch(cls, switch: Boolean=None, false: String=None, true: String=None)` — class method; returns `cls`.

### Menu

- `Menu.switch(self, switch: Boolean=None, true: Menu=None)` — method; returns `OUT`.
- `Menu.switch_false(self, switch: Boolean=None, false: Menu=None)` — method; returns `OUT`.
- `Menu.Switch(cls, switch: Boolean=None, false: Menu=None, true: Menu=None)` — class method; returns `cls`.

### Shader

- `Shader.switch(self, switch: Boolean=None, true: Shader=None)` — method; returns `OUT`.
- `Shader.switch_false(self, switch: Boolean=None, false: Shader=None)` — method; returns `OUT`.
- `Shader.Switch(cls, switch: Boolean=None, false: Shader=None, true: Shader=None)` — class method; returns `cls`.

### Bundle

- `Bundle.switch(self, switch: Boolean=None, true: Bundle=None)` — method; returns `OUT`.
- `Bundle.switch_false(self, switch: Boolean=None, false: Bundle=None)` — method; returns `OUT`.
- `Bundle.Switch(cls, switch: Boolean=None, false: Bundle=None, true: Bundle=None)` — class method; returns `cls`.

### Closure

- `Closure.switch(self, switch: Boolean=None, true: Closure=None)` — method; returns `OUT`.
- `Closure.switch_false(self, switch: Boolean=None, false: Closure=None)` — method; returns `OUT`.
- `Closure.Switch(cls, switch: Boolean=None, false: Closure=None, true: Closure=None)` — class method; returns `cls`.

## Tangent

Blender identifier: `ShaderNodeTangent`

### nd

- `nd.tangent(cls, uv_map: str='', direction_type: T_DIRECTION_TYPE_1='RADIAL', axis: T_AXIS_1='Z')` — class method; returns `OUT`.

## Texture Coordinate

Blender identifier: `ShaderNodeTexCoord`

### nd

- `nd.texture_coordinate(cls, object=None, from_instancer: bool=False)` — class method; returns `OUT`.

## Toon BSDF

Blender identifier: `ShaderNodeBsdfToon`

### nd

- `nd.toon_bsdf(cls, color: Color=None, size: Float=None, smooth: Float=None, normal: Vector=None, component: T_MODE_3='DIFFUSE')` — class method; returns `OUT`.

### Shader

- `Shader.Toon(cls, color: Color=None, size: Float=None, smooth: Float=None, normal: Vector=None, component: T_MODE_3='DIFFUSE')` — class method; returns `OUT`.

## Translucent BSDF

Blender identifier: `ShaderNodeBsdfTranslucent`

### nd

- `nd.translucent_bsdf(cls, color: Color=None, normal: Vector=None)` — class method; returns `OUT`.

### Shader

- `Shader.Translucent(cls, color: Color=None, normal: Vector=None)` — class method; returns `OUT`.

## Transparent BSDF

Blender identifier: `ShaderNodeBsdfTransparent`

### nd

- `nd.transparent_bsdf(cls, color: Color=None)` — class method; returns `OUT`.

### Shader

- `Shader.Transparent(cls, color: Color=None)` — class method; returns `OUT`.

## Trim String

Blender identifier: `FunctionNodeTrimString`

### nd

- `nd.trim_string(cls, string: String=None, characters: String=None, whitespace: Boolean=None, start: Boolean=None, end: Boolean=None)` — class method; returns `OUT`.

### String

- `String.trim(self, characters: String=None, whitespace: Boolean=None, start: Boolean=None, end: Boolean=None)` — method; returns `OUT`.

## UV Along Stroke

Blender identifier: `ShaderNodeUVAlongStroke`

### nd

- `nd.uv_along_stroke(cls, use_tips: bool=False)` — class method; returns `OUT`.

## UV Map

Blender identifier: `ShaderNodeUVMap`

### nd

- `nd.uv_map(cls, from_instancer: bool=False, uv_map: str='')` — class method; returns `OUT`.

## Value

Blender identifier: `ShaderNodeValue`

### nd

- `nd.value(cls)` — property; returns `OUT`.

## Value to String

Blender identifier: `FunctionNodeValueToString`

### nd

- `nd.value_to_string(cls, value: Socket=None, decimals: Integer=None, base: Integer=None, padding: Integer=None, data_type: T_DATA_TYPE_4='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.to_string(self, decimals: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.to_string(self, base: Integer=None, padding: Integer=None)` — method; returns `OUT`.

### String

- `String.FromValue(cls, value: Integer=None, base: Integer=None, padding: Integer=None)` — class method; returns `OUT`.

## Vector

Blender identifier: `FunctionNodeInputVector`

### nd

- `nd.vector(cls, vector: tuple[float, float, float]=(0.0, 0.0, 0.0), vector_dimensions: int=3)` — class method; returns `OUT`.

## Vector Curves

Blender identifier: `ShaderNodeVectorCurve`

### nd

- `nd.vector_curves(cls, vector: Vector=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.vector_curves(self, vector: Vector=None)` — method; returns `OUT`.

## Vector Displacement

Blender identifier: `ShaderNodeVectorDisplacement`

### nd

- `nd.vector_displacement(cls, vector: Color=None, midlevel: Float=None, scale: Float=None, space: T_SPACE_3='TANGENT')` — class method; returns `OUT`.

### Color

- `Color.vector_displacement(self, midlevel: Float=None, scale: Float=None, space: T_SPACE_3='TANGENT')` — method; returns `OUT`.

## Vector Math

Blender identifier: `ShaderNodeVectorMath`

### nd

- `nd.vector_math(cls, vector: Vector=None, vector_1: Vector=None, addend: Vector=None, ior: Float=None, *, base: Vector=None, multiplier: Vector=None, incident: Vector=None, exponent: Vector=None, max: Vector=None, increment: Vector=None, reference: Vector=None, min: Vector=None, scale: Float=None, operation: T_OPERATION_4='ADD')` — class method; returns `OUT`.

### gnmath

- `gnmath.vadd(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vsubtract(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vmultiply(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vdivide(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vpower(base: Vector=None, exponent: Vector=None)` — method; returns `OUT`.
- `gnmath.vmodulo(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vabs(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vround(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vfloor(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vceil(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.scale(vector: Vector=None, scale: Float=None)` — method; returns `OUT`.
- `gnmath.vmultiply_add(vector: Vector=None, multiplier: Vector=None, addend: Vector=None)` — method; returns `OUT`.
- `gnmath.cross(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.project(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.reflect(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.refract(vector: Vector=None, vector_1: Vector=None, ior: Float=None)` — method; returns `OUT`.
- `gnmath.faceforward(vector: Vector=None, incident: Vector=None, reference: Vector=None)` — method; returns `OUT`.
- `gnmath.dot(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.distance(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.length(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.normalize(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vsign(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vmin(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vmax(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vfraction(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vwrap(vector: Vector=None, max: Vector=None, min: Vector=None)` — method; returns `OUT`.
- `gnmath.vsnap(vector: Vector=None, increment: Vector=None)` — method; returns `OUT`.
- `gnmath.vsin(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vcos(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vtan(vector: Vector=None)` — method; returns `OUT`.

### Vector

- `Vector.add(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__add__(self, other)` — method; returns `OUT`.
- `Vector.__radd__(self, other)` — method; returns `OUT`.
- `Vector.__iadd__(self, other)` — method; returns `OUT`.
- `Vector.subtract(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__sub__(self, other)` — method; returns `OUT`.
- `Vector.__rsub__(self, other)` — method; returns `OUT`.
- `Vector.__isub__(self, other)` — method; returns `OUT`.
- `Vector.multiply(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__mul__(self, other)` — method; returns `OUT`.
- `Vector.__rmul__(self, other)` — method; returns `OUT`.
- `Vector.__imul__(self, other)` — method; returns `OUT`.
- `Vector.divide(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__truediv__(self, other)` — method; returns `OUT`.
- `Vector.__rtruediv__(self, other)` — method; returns `OUT`.
- `Vector.__itruediv__(self, other)` — method; returns `OUT`.
- `Vector.power(self, exponent: Vector=None)` — method; returns `OUT`.
- `Vector.__pow__(self, other)` — method; returns `OUT`.
- `Vector.__rpow__(self, other)` — method; returns `OUT`.
- `Vector.__ipow__(self, other)` — method; returns `OUT`.
- `Vector.modulo(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__mod__(self, other)` — method; returns `OUT`.
- `Vector.__rmod__(self, other)` — method; returns `OUT`.
- `Vector.__imod__(self, other)` — method; returns `OUT`.
- `Vector.abs(self)` — method; returns `OUT`.
- `Vector.__abs__(self)` — method; returns `OUT`.
- `Vector.round(self)` — method; returns `OUT`.
- `Vector.__round__(self)` — method; returns `OUT`.
- `Vector.floor(self)` — method; returns `OUT`.
- `Vector.__floor__(self)` — method; returns `OUT`.
- `Vector.ceil(self)` — method; returns `OUT`.
- `Vector.__ceil__(self)` — method; returns `OUT`.
- `Vector.scale(self, scale: Float=None)` — method; returns `OUT`.
- `Vector.__neg__(self)` — method; returns `OUT`.
- `Vector.multiply_add(self, multiplier: Vector=None, addend: Vector=None)` — method; returns `OUT`.
- `Vector.cross(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.project(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.reflect(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.refract(self, vector: Vector=None, ior: Float=None)` — method; returns `OUT`.
- `Vector.faceforward(self, incident: Vector=None, reference: Vector=None)` — method; returns `OUT`.
- `Vector.dot(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.distance(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.length(self)` — method; returns `OUT`.
- `Vector.normalize(self)` — method; returns `OUT`.
- `Vector.sign(self)` — method; returns `OUT`.
- `Vector.min(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.max(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.fraction(self)` — method; returns `OUT`.
- `Vector.wrap(self, max: Vector=None, min: Vector=None)` — method; returns `OUT`.
- `Vector.snap(self, increment: Vector=None)` — method; returns `OUT`.
- `Vector.sin(self)` — method; returns `OUT`.
- `Vector.cos(self)` — method; returns `OUT`.
- `Vector.tan(self)` — method; returns `OUT`.
- `Vector.vector_math(self, vector: Vector=None, addend: Vector=None, ior: Float=None, *, multiplier: Vector=None, incident: Vector=None, exponent: Vector=None, max: Vector=None, increment: Vector=None, reference: Vector=None, min: Vector=None, scale: Float=None, operation: T_OPERATION_4='ADD')` — method; returns `OUT`.

## Vector Rotate

Blender identifier: `ShaderNodeVectorRotate`

### nd

- `nd.vector_rotate(cls, vector: Vector=None, center: Vector=None, axis: Vector=None, angle: Float=None, rotation: Vector=None, invert: bool=False, rotation_type: T_ROTATION_TYPE_1='AXIS_ANGLE')` — class method; returns `OUT`.

### Vector

- `Vector.vector_rotate(self, center: Vector=None, axis: Vector=None, angle: Float=None, rotation: Vector=None, invert: bool=False, rotation_type: T_ROTATION_TYPE_1='AXIS_ANGLE')` — method; returns `OUT`.

## Vector Transform

Blender identifier: `ShaderNodeVectorTransform`

### nd

- `nd.vector_transform(cls, vector: Vector=None, vector_type: T_VECTOR_TYPE_2='VECTOR', convert_from: T_CONVERT_FROM_1='WORLD', convert_to: T_CONVERT_FROM_1='OBJECT')` — class method; returns `OUT`.

### Vector

- `Vector.vector_transform(self, vector_type: T_VECTOR_TYPE_2='VECTOR', convert_from: T_CONVERT_FROM_1='WORLD', convert_to: T_CONVERT_FROM_1='OBJECT')` — method; returns `OUT`.

## Volume Absorption

Blender identifier: `ShaderNodeVolumeAbsorption`

### nd

- `nd.volume_absorption(cls, color: Color=None, density: Float=None)` — class method; returns `OUT`.

### VolumeShader

- `VolumeShader.Absorption(cls, color: Color=None, density: Float=None)` — class method; returns `OUT`.

## Volume Coefficients

Blender identifier: `ShaderNodeVolumeCoefficients`

### nd

- `nd.volume_coefficients(cls, absorption_coefficients: Vector=None, scatter_coefficients: Vector=None, anisotropy: Float=None, ior: Float=None, backscatter: Float=None, alpha: Float=None, diameter: Float=None, emission_coefficients: Vector=None, phase: T_PHASE_1='HENYEY_GREENSTEIN')` — class method; returns `OUT`.

### VolumeShader

- `VolumeShader.Coefficients(cls, absorption_coefficients: Vector=None, scatter_coefficients: Vector=None, anisotropy: Float=None, ior: Float=None, backscatter: Float=None, alpha: Float=None, diameter: Float=None, emission_coefficients: Vector=None, phase: T_PHASE_1='HENYEY_GREENSTEIN')` — class method; returns `OUT`.

## Volume Info

Blender identifier: `ShaderNodeVolumeInfo`

### nd

- `nd.volume_info(cls)` — class method; returns `OUT`.

## Volume Scatter

Blender identifier: `ShaderNodeVolumeScatter`

### nd

- `nd.volume_scatter(cls, color: Color=None, density: Float=None, anisotropy: Float=None, ior: Float=None, backscatter: Float=None, alpha: Float=None, diameter: Float=None, phase: T_PHASE_1='HENYEY_GREENSTEIN')` — class method; returns `OUT`.

### VolumeShader

- `VolumeShader.Scatter(cls, color: Color=None, density: Float=None, anisotropy: Float=None, ior: Float=None, backscatter: Float=None, alpha: Float=None, diameter: Float=None, phase: T_PHASE_1='HENYEY_GREENSTEIN')` — class method; returns `OUT`.

## Voronoi Texture

Blender identifier: `ShaderNodeTexVoronoi`

### nd

- `nd.voronoi_texture(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, smoothness: Float=None, exponent: Float=None, randomness: Float=None, normalize: bool=False, voronoi_dimensions: T_NOISE_DIMENSIONS_1='3D', distance: T_DISTANCE_1='EUCLIDEAN', feature: T_FEATURE_1='F1')` — class method; returns `OUT`.

### Texture

- `Texture.Voronoi(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, smoothness: Float=None, exponent: Float=None, randomness: Float=None, normalize: bool=False, voronoi_dimensions: T_NOISE_DIMENSIONS_1='3D', distance: T_DISTANCE_1='EUCLIDEAN', feature: T_FEATURE_1='F1')` — class method; returns `OUT`.

## Warning

Blender identifier: `GeometryNodeWarning`

### nd

- `nd.warning(cls, show: Boolean=None, message: String=None, warning_type: T_WARNING_TYPE_1='ERROR')` — class method; returns `OUT`.

### Boolean

- `Boolean.error(self, message: String=None)` — method; returns `OUT`.
- `Boolean.warning(self, message: String=None)` — method; returns `OUT`.
- `Boolean.info(self, message: String=None)` — method; returns `OUT`.

## Wave Texture

Blender identifier: `ShaderNodeTexWave`

### nd

- `nd.wave_texture(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, detail: Float=None, detail_scale: Float=None, detail_roughness: Float=None, phase_offset: Float=None, wave_type: T_WAVE_TYPE_1='BANDS', bands_direction: T_BANDS_DIRECTION_1='X', rings_direction: T_RINGS_DIRECTION_1='X', wave_profile: T_WAVE_PROFILE_1='SIN')` — class method; returns `OUT`.

### Texture

- `Texture.Wave(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, detail: Float=None, detail_scale: Float=None, detail_roughness: Float=None, phase_offset: Float=None, wave_type: T_WAVE_TYPE_1='BANDS', bands_direction: T_BANDS_DIRECTION_1='X', rings_direction: T_RINGS_DIRECTION_1='X', wave_profile: T_WAVE_PROFILE_1='SIN')` — class method; returns `OUT`.

## Wavelength

Blender identifier: `ShaderNodeWavelength`

### nd

- `nd.wavelength(cls, wavelength: Float=None)` — class method; returns `OUT`.

### Float

- `Float.wavelength(self)` — method; returns `OUT`.

## White Noise Texture

Blender identifier: `ShaderNodeTexWhiteNoise`

### nd

- `nd.white_noise_texture(cls, vector: Vector=None, w: Float=None, noise_dimensions: T_NOISE_DIMENSIONS_1='3D')` — class method; returns `OUT`.

### Texture

- `Texture.WhiteNoise(cls, vector: Vector=None, w: Float=None, noise_dimensions: T_NOISE_DIMENSIONS_1='3D')` — class method; returns `OUT`.

## Wireframe

Blender identifier: `ShaderNodeWireframe`

### nd

- `nd.wireframe(cls, size: Float=None, use_pixel_size: bool=False)` — class method; returns `OUT`.

## World Output

Blender identifier: `ShaderNodeOutputWorld`

### nd

- `nd.world_output(cls, surface: Shader=None, volume: VolumeShader=None, is_active_output: bool=True, target: T_TARGET_1='ALL')` — class method; returns `NODE`.

### Shader

- `Shader.world_output(self, volume: VolumeShader=None, is_active_output: bool=True, target: T_TARGET_1='ALL')` — method; returns `NODE`.

