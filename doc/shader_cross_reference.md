# Shader Cross Reference

You will find here how nodes are implemented

## Content

- **&** : [&Material Output](shader_cross_reference.md#&material-output)
- **A** : [Add Shader](shader_cross_reference.md#add-shader) :black_small_square: [AOV Output](shader_cross_reference.md#aov-output)
- **B** : [Background](shader_cross_reference.md#background) :black_small_square: [Bevel](shader_cross_reference.md#bevel) :black_small_square: [Blackbody](shader_cross_reference.md#blackbody) :black_small_square: [Brightness Contrast](shader_cross_reference.md#brightness-contrast) :black_small_square: [Bump](shader_cross_reference.md#bump)
- **C** : [Color Attribute](shader_cross_reference.md#color-attribute) :black_small_square: [Combine Color](shader_cross_reference.md#combine-color)
- **D** : [Diffuse BSDF](shader_cross_reference.md#diffuse-bsdf) :black_small_square: [Displacement](shader_cross_reference.md#displacement)
- **E** : [Emission](shader_cross_reference.md#emission) :black_small_square: [Environment Texture](shader_cross_reference.md#environment-texture)
- **F** : [Fresnel](shader_cross_reference.md#fresnel)
- **G** : [Gamma](shader_cross_reference.md#gamma) :black_small_square: [Glass BSDF](shader_cross_reference.md#glass-bsdf) :black_small_square: [Glossy BSDF](shader_cross_reference.md#glossy-bsdf)
- **H** : [Hair BSDF](shader_cross_reference.md#hair-bsdf) :black_small_square: [Holdout](shader_cross_reference.md#holdout) :black_small_square: [Hue Saturation Value](shader_cross_reference.md#hue-saturation-value)
- **I** : [IES Texture](shader_cross_reference.md#ies-texture) :black_small_square: [Image Texture](shader_cross_reference.md#image-texture) :black_small_square: [Invert Color](shader_cross_reference.md#invert-color)
- **L** : [Layer Weight](shader_cross_reference.md#layer-weight) :black_small_square: [Light Falloff](shader_cross_reference.md#light-falloff) :black_small_square: [Light Output](shader_cross_reference.md#light-output) :black_small_square: [Line Style Output](shader_cross_reference.md#line-style-output)
- **M** : [Mapping](shader_cross_reference.md#mapping) :black_small_square: [Material Output](shader_cross_reference.md#material-output) :black_small_square: [Metallic BSDF](shader_cross_reference.md#metallic-bsdf) :black_small_square: [Mix Shader](shader_cross_reference.md#mix-shader)
- **N** : [Normal](shader_cross_reference.md#normal) :black_small_square: [Normal Map](shader_cross_reference.md#normal-map)
- **P** : [Principled BSDF](shader_cross_reference.md#principled-bsdf) :black_small_square: [Principled Hair BSDF](shader_cross_reference.md#principled-hair-bsdf) :black_small_square: [Principled Volume](shader_cross_reference.md#principled-volume)
- **R** : [Ray Portal BSDF](shader_cross_reference.md#ray-portal-bsdf) :black_small_square: [Refraction BSDF](shader_cross_reference.md#refraction-bsdf) :black_small_square: [RGB to BW](shader_cross_reference.md#rgb-to-bw)
- **S** : [Separate Color](shader_cross_reference.md#separate-color) :black_small_square: [Shader to RGB](shader_cross_reference.md#shader-to-rgb) :black_small_square: [Sheen BSDF](shader_cross_reference.md#sheen-bsdf) :black_small_square: [Sky Texture](shader_cross_reference.md#sky-texture) :black_small_square: [Specular BSDF](shader_cross_reference.md#specular-bsdf) :black_small_square: [Subsurface Scattering](shader_cross_reference.md#subsurface-scattering)
- **T** : [Tangent](shader_cross_reference.md#tangent) :black_small_square: [to Euler](shader_cross_reference.md#to-euler) :black_small_square: [Toon BSDF](shader_cross_reference.md#toon-bsdf) :black_small_square: [Translucent BSDF](shader_cross_reference.md#translucent-bsdf) :black_small_square: [Transparent BSDF](shader_cross_reference.md#transparent-bsdf)
- **U** : [UV Map](shader_cross_reference.md#uv-map)
- **V** : [Vector Displacement](shader_cross_reference.md#vector-displacement) :black_small_square: [Vector Transform](shader_cross_reference.md#vector-transform) :black_small_square: [Volume Absorption](shader_cross_reference.md#volume-absorption) :black_small_square: [Volume Scatter](shader_cross_reference.md#volume-scatter)
- **W** : [Wavelength](shader_cross_reference.md#wavelength) :black_small_square: [Wireframe](shader_cross_reference.md#wireframe) :black_small_square: [World Output](shader_cross_reference.md#world-output)

#### &Material Output

- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Add Shader

- [Shader](shader.md#shader) :white_small_square: [add](shader.md#add)

#### AOV Output

- [Color](color.md#color) :white_small_square: [aov_output](color.md#aov_output)
- [Color](color.md#color) :white_small_square: [out](color.md#out)
- [Float](float.md#float) :white_small_square: [out](float.md#out)
- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Background

- [Color](color.md#color) :white_small_square: [background](color.md#background)

#### Bevel

- [Float](float.md#float) :white_small_square: [bevel](float.md#bevel)

#### Blackbody

- [Color](color.md#color) :white_small_square: [Blackbody](color.md#blackbody)

#### Brightness Contrast

- [Color](color.md#color) :white_small_square: [brightness_contrast](color.md#brightness_contrast)

#### Bump

- [Float](float.md#float) :white_small_square: [bump](float.md#bump)
- [Vector](vector.md#vector) :white_small_square: [bump](vector.md#bump)

#### Color Attribute

- [Color](color.md#color) :white_small_square: [Attribute](color.md#attribute)
- [Color](color.md#color) :white_small_square: [ColorAttribute](color.md#colorattribute)
- [Color](color.md#color) :white_small_square: [ambient_occlusion](color.md#ambient_occlusion)

#### Combine Color

- [Float](float.md#float) :white_small_square: [combine_color](float.md#combine_color)
- [Float](float.md#float) :white_small_square: [combine_color_HSL](float.md#combine_color_hsl)
- [Float](float.md#float) :white_small_square: [combine_color_HSV](float.md#combine_color_hsv)
- [Float](float.md#float) :white_small_square: [combine_color_RGB](float.md#combine_color_rgb)

#### Diffuse BSDF

- [Shader](shader.md#shader) :white_small_square: [Diffuse](shader.md#diffuse)

#### Displacement

- [Float](float.md#float) :white_small_square: [displacement](float.md#displacement)
- [Vector](vector.md#vector) :white_small_square: [displacement](vector.md#displacement)

#### Emission

- [Shader](shader.md#shader) :white_small_square: [Emission](shader.md#emission)

#### Environment Texture

- [Vector](vector.md#vector) :white_small_square: [environment_texture](vector.md#environment_texture)

#### Fresnel

- [Float](float.md#float) :white_small_square: [fresnel](float.md#fresnel)

#### Gamma

- [Color](color.md#color) :white_small_square: [gamma](color.md#gamma)

#### Glass BSDF

- [Shader](shader.md#shader) :white_small_square: [Glass](shader.md#glass)

#### Glossy BSDF

- [Shader](shader.md#shader) :white_small_square: [Glossy](shader.md#glossy)

#### Hair BSDF

- [Shader](shader.md#shader) :white_small_square: [Hair](shader.md#hair)

#### Holdout

- [Shader](shader.md#shader) :white_small_square: [Holdout](shader.md#holdout)

#### Hue Saturation Value

- [Color](color.md#color) :white_small_square: [hue_saturation_value](color.md#hue_saturation_value)
- [Float](float.md#float) :white_small_square: [hue_saturation_value](float.md#hue_saturation_value)

#### IES Texture

- [Vector](vector.md#vector) :white_small_square: [ies_texture](vector.md#ies_texture)
- [Vector](vector.md#vector) :white_small_square: [ies_texture_external](vector.md#ies_texture_external)
- [Vector](vector.md#vector) :white_small_square: [ies_texture_internal](vector.md#ies_texture_internal)

#### Image Texture

- [Vector](vector.md#vector) :white_small_square: [image_texture](vector.md#image_texture)

#### Invert Color

- [Color](color.md#color) :white_small_square: [invert](color.md#invert)
- [Color](color.md#color) :white_small_square: [invert_color](color.md#invert_color)

#### Layer Weight

- [Float](float.md#float) :white_small_square: [layer_weight](float.md#layer_weight)

#### Light Falloff

- [Float](float.md#float) :white_small_square: [light_falloff](float.md#light_falloff)

#### Light Output

- [Shader](shader.md#shader) :white_small_square: [light_output](shader.md#light_output)

#### Line Style Output

- [Color](color.md#color) :white_small_square: [line_style_output](color.md#line_style_output)

#### Mapping

- [Vector](vector.md#vector) :white_small_square: [mapping](vector.md#mapping)

#### Material Output

- [Shader](shader.md#shader) :white_small_square: [material_output](shader.md#material_output)
- [Vector](vector.md#vector) :white_small_square: [displacement_out](vector.md#displacement_out)

#### Metallic BSDF

- [Shader](shader.md#shader) :white_small_square: [Metallic](shader.md#metallic)

#### Mix Shader

- [Shader](shader.md#shader) :white_small_square: [mix](shader.md#mix)

#### Normal

- [Vector](vector.md#vector) :white_small_square: [normal](vector.md#normal)

#### Normal Map

- [Color](color.md#color) :white_small_square: [normal_map](color.md#normal_map)
- [Float](float.md#float) :white_small_square: [normal_map](float.md#normal_map)
- [Vector](vector.md#vector) :white_small_square: [NormalMap](vector.md#normalmap)

#### Principled BSDF

- [Shader](shader.md#shader) :white_small_square: [Principled](shader.md#principled)

#### Principled Hair BSDF

- [Shader](shader.md#shader) :white_small_square: [PrincipledHair](shader.md#principledhair)

#### Principled Volume

- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [Principled](volumeshader.md#principled)

#### Ray Portal BSDF

- [Shader](shader.md#shader) :white_small_square: [RayPortal](shader.md#rayportal)

#### Refraction BSDF

- [Shader](shader.md#shader) :white_small_square: [Refraction](shader.md#refraction)

#### RGB to BW

- [Color](color.md#color) :white_small_square: [rgb_to_bw](color.md#rgb_to_bw)
- [Color](color.md#color) :white_small_square: [to_bw](color.md#to_bw)

#### Separate Color

- [Color](color.md#color) :white_small_square: [separate_col](color.md#separate_col)
- [Color](color.md#color) :white_small_square: [separate_col_HSL](color.md#separate_col_hsl)
- [Color](color.md#color) :white_small_square: [separate_col_HSV](color.md#separate_col_hsv)
- [Color](color.md#color) :white_small_square: [separate_col_RGB](color.md#separate_col_rgb)

#### Shader to RGB

- [Color](color.md#color) :white_small_square: [FromShader](color.md#fromshader)
- [Shader](shader.md#shader) :white_small_square: [to_rgb](shader.md#to_rgb)

#### Sheen BSDF

- [Shader](shader.md#shader) :white_small_square: [Sheen](shader.md#sheen)

#### Sky Texture

- [Color](color.md#color) :white_small_square: [SkyTexture](color.md#skytexture)

#### Specular BSDF

- [Shader](shader.md#shader) :white_small_square: [Specular](shader.md#specular)

#### Subsurface Scattering

- [Shader](shader.md#shader) :white_small_square: [SubsurfaceScattering](shader.md#subsurfacescattering)

#### Tangent

- [Vector](vector.md#vector) :white_small_square: [Tangent](vector.md#tangent)

#### to Euler

- [Vector](vector.md#vector) :white_small_square: [FromRotation](vector.md#fromrotation)

#### Toon BSDF

- [Shader](shader.md#shader) :white_small_square: [Toon](shader.md#toon)

#### Translucent BSDF

- [Shader](shader.md#shader) :white_small_square: [Translucent](shader.md#translucent)

#### Transparent BSDF

- [Shader](shader.md#shader) :white_small_square: [Transparent](shader.md#transparent)

#### UV Map

- [Vector](vector.md#vector) :white_small_square: [UVMap](vector.md#uvmap)
- [Vector](vector.md#vector) :white_small_square: [UvMap](vector.md#uvmap)

#### Vector Displacement

- [Color](color.md#color) :white_small_square: [vector_displacement](color.md#vector_displacement)
- [Vector](vector.md#vector) :white_small_square: [vector_displacement](vector.md#vector_displacement)

#### Vector Transform

- [Vector](vector.md#vector) :white_small_square: [transform](vector.md#transform)
- [Vector](vector.md#vector) :white_small_square: [vector_transform](vector.md#vector_transform)

#### Volume Absorption

- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [Absorption](volumeshader.md#absorption)

#### Volume Scatter

- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [Scatter](volumeshader.md#scatter)

#### Wavelength

- [Color](color.md#color) :white_small_square: [Wavelength](color.md#wavelength)
- [Float](float.md#float) :white_small_square: [wavelength](float.md#wavelength)

#### Wireframe

- [Float](float.md#float) :white_small_square: [wireframe](float.md#wireframe)

#### World Output

- [Shader](shader.md#shader) :white_small_square: [world_output](shader.md#world_output)