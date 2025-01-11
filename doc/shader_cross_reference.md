# Shader Cross Reference

You will find here how nodes are implemented

## Content

- **&** : [&Material Output](shader_cross_reference.md#&material-output)
- **A** : [Add Shader](shader_cross_reference.md#add-shader) :black_small_square: [Ambient Occlusion](shader_cross_reference.md#ambient-occlusion) :black_small_square: [AOV Output](shader_cross_reference.md#aov-output) :black_small_square: [Attribute](shader_cross_reference.md#attribute)
- **B** : [Background](shader_cross_reference.md#background) :black_small_square: [Bevel](shader_cross_reference.md#bevel) :black_small_square: [Blackbody](shader_cross_reference.md#blackbody) :black_small_square: [Brick Texture](shader_cross_reference.md#brick-texture) :black_small_square: [Brightness Contrast](shader_cross_reference.md#brightness-contrast) :black_small_square: [Bump](shader_cross_reference.md#bump)
- **C** : [Camera Data](shader_cross_reference.md#camera-data) :black_small_square: [Checker Texture](shader_cross_reference.md#checker-texture) :black_small_square: [Clamp](shader_cross_reference.md#clamp) :black_small_square: [Color Attribute](shader_cross_reference.md#color-attribute) :black_small_square: [Color Ramp](shader_cross_reference.md#color-ramp) :black_small_square: [Combine Color](shader_cross_reference.md#combine-color) :black_small_square: [Combine XYZ](shader_cross_reference.md#combine-xyz) :black_small_square: [Curves Info](shader_cross_reference.md#curves-info)
- **D** : [Diffuse BSDF](shader_cross_reference.md#diffuse-bsdf) :black_small_square: [Displacement](shader_cross_reference.md#displacement)
- **E** : [Emission](shader_cross_reference.md#emission) :black_small_square: [Environment Texture](shader_cross_reference.md#environment-texture)
- **F** : [Float Curve](shader_cross_reference.md#float-curve) :black_small_square: [Frame](shader_cross_reference.md#frame) :black_small_square: [Fresnel](shader_cross_reference.md#fresnel)
- **G** : [Gabor Texture](shader_cross_reference.md#gabor-texture) :black_small_square: [Gamma](shader_cross_reference.md#gamma) :black_small_square: [Geometry](shader_cross_reference.md#geometry) :black_small_square: [Glass BSDF](shader_cross_reference.md#glass-bsdf) :black_small_square: [Glossy BSDF](shader_cross_reference.md#glossy-bsdf) :black_small_square: [Gradient Texture](shader_cross_reference.md#gradient-texture) :black_small_square: [Group](shader_cross_reference.md#group) :black_small_square: [Group Output](shader_cross_reference.md#group-output)
- **H** : [Hair BSDF](shader_cross_reference.md#hair-bsdf) :black_small_square: [Holdout](shader_cross_reference.md#holdout) :black_small_square: [Hue Saturation Value](shader_cross_reference.md#hue-saturation-value)
- **I** : [IES Texture](shader_cross_reference.md#ies-texture) :black_small_square: [Image Texture](shader_cross_reference.md#image-texture) :black_small_square: [Input](shader_cross_reference.md#input) :black_small_square: [Invert Color](shader_cross_reference.md#invert-color)
- **L** : [Layer Weight](shader_cross_reference.md#layer-weight) :black_small_square: [Light Falloff](shader_cross_reference.md#light-falloff) :black_small_square: [Light Output](shader_cross_reference.md#light-output) :black_small_square: [Light Path](shader_cross_reference.md#light-path) :black_small_square: [Line Style Output](shader_cross_reference.md#line-style-output)
- **M** : [Magic Texture](shader_cross_reference.md#magic-texture) :black_small_square: [Map Range](shader_cross_reference.md#map-range) :black_small_square: [Mapping](shader_cross_reference.md#mapping) :black_small_square: [Material Output](shader_cross_reference.md#material-output) :black_small_square: [Math](shader_cross_reference.md#math) :black_small_square: [Metallic BSDF](shader_cross_reference.md#metallic-bsdf) :black_small_square: [Mix](shader_cross_reference.md#mix) :black_small_square: [Mix Shader](shader_cross_reference.md#mix-shader)
- **N** : [Noise Texture](shader_cross_reference.md#noise-texture) :black_small_square: [Normal](shader_cross_reference.md#normal) :black_small_square: [Normal Map](shader_cross_reference.md#normal-map)
- **O** : [Object Info](shader_cross_reference.md#object-info) :black_small_square: [Output](shader_cross_reference.md#output)
- **P** : [Particle Info](shader_cross_reference.md#particle-info) :black_small_square: [Point Density](shader_cross_reference.md#point-density) :black_small_square: [Point Info](shader_cross_reference.md#point-info) :black_small_square: [Principled BSDF](shader_cross_reference.md#principled-bsdf) :black_small_square: [Principled Hair BSDF](shader_cross_reference.md#principled-hair-bsdf) :black_small_square: [Principled Volume](shader_cross_reference.md#principled-volume)
- **R** : [Ray Portal BSDF](shader_cross_reference.md#ray-portal-bsdf) :black_small_square: [Refraction BSDF](shader_cross_reference.md#refraction-bsdf) :black_small_square: [Reroute](shader_cross_reference.md#reroute) :black_small_square: [RGB](shader_cross_reference.md#rgb) :black_small_square: [RGB Curves](shader_cross_reference.md#rgb-curves) :black_small_square: [RGB to BW](shader_cross_reference.md#rgb-to-bw)
- **S** : [Script](shader_cross_reference.md#script) :black_small_square: [Separate Color](shader_cross_reference.md#separate-color) :black_small_square: [Separate XYZ](shader_cross_reference.md#separate-xyz) :black_small_square: [Shader to RGB](shader_cross_reference.md#shader-to-rgb) :black_small_square: [Sheen BSDF](shader_cross_reference.md#sheen-bsdf) :black_small_square: [Sky Texture](shader_cross_reference.md#sky-texture) :black_small_square: [Specular BSDF](shader_cross_reference.md#specular-bsdf) :black_small_square: [Subsurface Scattering](shader_cross_reference.md#subsurface-scattering)
- **T** : [Tangent](shader_cross_reference.md#tangent) :black_small_square: [Texture Coordinate](shader_cross_reference.md#texture-coordinate) :black_small_square: [to Euler](shader_cross_reference.md#to-euler) :black_small_square: [Toon BSDF](shader_cross_reference.md#toon-bsdf) :black_small_square: [Translucent BSDF](shader_cross_reference.md#translucent-bsdf) :black_small_square: [Transparent BSDF](shader_cross_reference.md#transparent-bsdf)
- **U** : [UV Along Stroke](shader_cross_reference.md#uv-along-stroke) :black_small_square: [UV Map](shader_cross_reference.md#uv-map)
- **V** : [Vector Curves](shader_cross_reference.md#vector-curves) :black_small_square: [Vector Displacement](shader_cross_reference.md#vector-displacement) :black_small_square: [Vector Math](shader_cross_reference.md#vector-math) :black_small_square: [Vector Rotate](shader_cross_reference.md#vector-rotate) :black_small_square: [Vector Transform](shader_cross_reference.md#vector-transform) :black_small_square: [Volume Absorption](shader_cross_reference.md#volume-absorption) :black_small_square: [Volume Info](shader_cross_reference.md#volume-info) :black_small_square: [Volume Scatter](shader_cross_reference.md#volume-scatter) :black_small_square: [Voronoi Texture](shader_cross_reference.md#voronoi-texture)
- **W** : [Wave Texture](shader_cross_reference.md#wave-texture) :black_small_square: [Wavelength](shader_cross_reference.md#wavelength) :black_small_square: [White Noise Texture](shader_cross_reference.md#white-noise-texture) :black_small_square: [Wireframe](shader_cross_reference.md#wireframe) :black_small_square: [World Output](shader_cross_reference.md#world-output)

#### &Material Output

- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Add Shader

- [snd](snd.md#snd) :white_small_square: [add_shader](snd.md#add_shader)
- [Shader](shader.md#shader) :white_small_square: [add](shader.md#add)

#### Ambient Occlusion

- [snd](snd.md#snd) :white_small_square: [ambient_occlusion](snd.md#ambient_occlusion)

#### AOV Output

- [snd](snd.md#snd) :white_small_square: [aov_output](snd.md#aov_output)
- [Color](color.md#color) :white_small_square: [aov_output](color.md#aov_output)
- [Color](color.md#color) :white_small_square: [out](color.md#out)
- [Float](float.md#float) :white_small_square: [out](float.md#out)
- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Attribute

- [snd](snd.md#snd) :white_small_square: [attribute](snd.md#attribute)

#### Background

- [snd](snd.md#snd) :white_small_square: [background](snd.md#background)
- [Color](color.md#color) :white_small_square: [background](color.md#background)

#### Bevel

- [snd](snd.md#snd) :white_small_square: [bevel](snd.md#bevel)
- [Float](float.md#float) :white_small_square: [bevel](float.md#bevel)

#### Blackbody

- [snd](snd.md#snd) :white_small_square: [blackbody](snd.md#blackbody)
- [Color](color.md#color) :white_small_square: [Blackbody](color.md#blackbody)

#### Brick Texture

- [snd](snd.md#snd) :white_small_square: [brick_texture](snd.md#brick_texture)

#### Brightness Contrast

- [snd](snd.md#snd) :white_small_square: [brightness_contrast](snd.md#brightness_contrast)
- [Color](color.md#color) :white_small_square: [brightness_contrast](color.md#brightness_contrast)

#### Bump

- [snd](snd.md#snd) :white_small_square: [bump](snd.md#bump)
- [Float](float.md#float) :white_small_square: [bump](float.md#bump)
- [Vector](vector.md#vector) :white_small_square: [bump](vector.md#bump)

#### Camera Data

- [snd](snd.md#snd) :white_small_square: [camera_data](snd.md#camera_data)

#### Checker Texture

- [snd](snd.md#snd) :white_small_square: [checker_texture](snd.md#checker_texture)

#### Clamp

- [snd](snd.md#snd) :white_small_square: [clamp](snd.md#clamp)

#### Color Attribute

- [snd](snd.md#snd) :white_small_square: [color_attribute](snd.md#color_attribute)
- [Color](color.md#color) :white_small_square: [Attribute](color.md#attribute)
- [Color](color.md#color) :white_small_square: [ColorAttribute](color.md#colorattribute)
- [Color](color.md#color) :white_small_square: [ambient_occlusion](color.md#ambient_occlusion)

#### Color Ramp

- [snd](snd.md#snd) :white_small_square: [color_ramp](snd.md#color_ramp)

#### Combine Color

- [snd](snd.md#snd) :white_small_square: [combine_color](snd.md#combine_color)
- [Float](float.md#float) :white_small_square: [combine_color](float.md#combine_color)
- [Float](float.md#float) :white_small_square: [combine_color_HSL](float.md#combine_color_hsl)
- [Float](float.md#float) :white_small_square: [combine_color_HSV](float.md#combine_color_hsv)
- [Float](float.md#float) :white_small_square: [combine_color_RGB](float.md#combine_color_rgb)

#### Combine XYZ

- [snd](snd.md#snd) :white_small_square: [combine_xyz](snd.md#combine_xyz)

#### Curves Info

- [snd](snd.md#snd) :white_small_square: [curves_info](snd.md#curves_info)

#### Diffuse BSDF

- [snd](snd.md#snd) :white_small_square: [diffuse_bsdf](snd.md#diffuse_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Diffuse](shader.md#diffuse)

#### Displacement

- [snd](snd.md#snd) :white_small_square: [displacement](snd.md#displacement)
- [Float](float.md#float) :white_small_square: [displacement](float.md#displacement)
- [Vector](vector.md#vector) :white_small_square: [displacement](vector.md#displacement)

#### Emission

- [snd](snd.md#snd) :white_small_square: [emission](snd.md#emission)
- [Shader](shader.md#shader) :white_small_square: [Emission](shader.md#emission)

#### Environment Texture

- [snd](snd.md#snd) :white_small_square: [environment_texture](snd.md#environment_texture)
- [Vector](vector.md#vector) :white_small_square: [environment_texture](vector.md#environment_texture)

#### Float Curve

- [snd](snd.md#snd) :white_small_square: [float_curve](snd.md#float_curve)

#### Frame

- [snd](snd.md#snd) :white_small_square: [frame](snd.md#frame)

#### Fresnel

- [snd](snd.md#snd) :white_small_square: [fresnel](snd.md#fresnel)
- [Float](float.md#float) :white_small_square: [fresnel](float.md#fresnel)

#### Gabor Texture

- [snd](snd.md#snd) :white_small_square: [gabor_texture](snd.md#gabor_texture)

#### Gamma

- [snd](snd.md#snd) :white_small_square: [gamma](snd.md#gamma)
- [Color](color.md#color) :white_small_square: [gamma](color.md#gamma)

#### Geometry

- [snd](snd.md#snd) :white_small_square: [geometry](snd.md#geometry)

#### Glass BSDF

- [snd](snd.md#snd) :white_small_square: [glass_bsdf](snd.md#glass_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Glass](shader.md#glass)

#### Glossy BSDF

- [snd](snd.md#snd) :white_small_square: [glossy_bsdf](snd.md#glossy_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Glossy](shader.md#glossy)

#### Gradient Texture

- [snd](snd.md#snd) :white_small_square: [gradient_texture](snd.md#gradient_texture)

#### Group

- [snd](snd.md#snd) :white_small_square: [group](snd.md#group)

#### Group Output

- [snd](snd.md#snd) :white_small_square: [group_output](snd.md#group_output)

#### Hair BSDF

- [snd](snd.md#snd) :white_small_square: [hair_bsdf](snd.md#hair_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Hair](shader.md#hair)

#### Holdout

- [snd](snd.md#snd) :white_small_square: [holdout](snd.md#holdout)
- [Shader](shader.md#shader) :white_small_square: [Holdout](shader.md#holdout)

#### Hue Saturation Value

- [snd](snd.md#snd) :white_small_square: [hue_saturation_value](snd.md#hue_saturation_value)
- [Color](color.md#color) :white_small_square: [hue_saturation_value](color.md#hue_saturation_value)
- [Float](float.md#float) :white_small_square: [hue_saturation_value](float.md#hue_saturation_value)

#### IES Texture

- [snd](snd.md#snd) :white_small_square: [ies_texture](snd.md#ies_texture)
- [Vector](vector.md#vector) :white_small_square: [ies_texture](vector.md#ies_texture)
- [Vector](vector.md#vector) :white_small_square: [ies_texture_external](vector.md#ies_texture_external)
- [Vector](vector.md#vector) :white_small_square: [ies_texture_internal](vector.md#ies_texture_internal)

#### Image Texture

- [snd](snd.md#snd) :white_small_square: [image_texture](snd.md#image_texture)
- [Vector](vector.md#vector) :white_small_square: [image_texture](vector.md#image_texture)

#### Input

- [Tree](tree.md#tree) :white_small_square: [new_input](tree.md#new_input)

#### Invert Color

- [snd](snd.md#snd) :white_small_square: [invert_color](snd.md#invert_color)
- [Color](color.md#color) :white_small_square: [invert](color.md#invert)
- [Color](color.md#color) :white_small_square: [invert_color](color.md#invert_color)

#### Layer Weight

- [snd](snd.md#snd) :white_small_square: [layer_weight](snd.md#layer_weight)
- [Float](float.md#float) :white_small_square: [layer_weight](float.md#layer_weight)

#### Light Falloff

- [snd](snd.md#snd) :white_small_square: [light_falloff](snd.md#light_falloff)
- [Float](float.md#float) :white_small_square: [light_falloff](float.md#light_falloff)

#### Light Output

- [snd](snd.md#snd) :white_small_square: [light_output](snd.md#light_output)
- [Shader](shader.md#shader) :white_small_square: [light_output](shader.md#light_output)

#### Light Path

- [snd](snd.md#snd) :white_small_square: [light_path](snd.md#light_path)

#### Line Style Output

- [snd](snd.md#snd) :white_small_square: [line_style_output](snd.md#line_style_output)
- [Color](color.md#color) :white_small_square: [line_style_output](color.md#line_style_output)

#### Magic Texture

- [snd](snd.md#snd) :white_small_square: [magic_texture](snd.md#magic_texture)

#### Map Range

- [snd](snd.md#snd) :white_small_square: [map_range](snd.md#map_range)

#### Mapping

- [snd](snd.md#snd) :white_small_square: [mapping](snd.md#mapping)
- [Vector](vector.md#vector) :white_small_square: [mapping](vector.md#mapping)

#### Material Output

- [snd](snd.md#snd) :white_small_square: [material_output](snd.md#material_output)
- [Shader](shader.md#shader) :white_small_square: [material_output](shader.md#material_output)
- [Vector](vector.md#vector) :white_small_square: [displacement_out](vector.md#displacement_out)

#### Math

- [snd](snd.md#snd) :white_small_square: [math](snd.md#math)

#### Metallic BSDF

- [snd](snd.md#snd) :white_small_square: [metallic_bsdf](snd.md#metallic_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Metallic](shader.md#metallic)

#### Mix

- [snd](snd.md#snd) :white_small_square: [mix](snd.md#mix)

#### Mix Shader

- [snd](snd.md#snd) :white_small_square: [mix_shader](snd.md#mix_shader)
- [Shader](shader.md#shader) :white_small_square: [mix](shader.md#mix)

#### Noise Texture

- [snd](snd.md#snd) :white_small_square: [noise_texture](snd.md#noise_texture)

#### Normal

- [snd](snd.md#snd) :white_small_square: [normal](snd.md#normal)
- [Vector](vector.md#vector) :white_small_square: [normal](vector.md#normal)

#### Normal Map

- [snd](snd.md#snd) :white_small_square: [normal_map](snd.md#normal_map)
- [Color](color.md#color) :white_small_square: [normal_map](color.md#normal_map)
- [Float](float.md#float) :white_small_square: [normal_map](float.md#normal_map)
- [Vector](vector.md#vector) :white_small_square: [NormalMap](vector.md#normalmap)

#### Object Info

- [snd](snd.md#snd) :white_small_square: [object_info](snd.md#object_info)

#### Output

- [Tree](tree.md#tree) :white_small_square: [new_output](tree.md#new_output)

#### Particle Info

- [snd](snd.md#snd) :white_small_square: [particle_info](snd.md#particle_info)

#### Point Density

- [snd](snd.md#snd) :white_small_square: [point_density](snd.md#point_density)
- [Vector](vector.md#vector) :white_small_square: [point_density](vector.md#point_density)

#### Point Info

- [snd](snd.md#snd) :white_small_square: [point_info](snd.md#point_info)

#### Principled BSDF

- [snd](snd.md#snd) :white_small_square: [principled_bsdf](snd.md#principled_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Principled](shader.md#principled)

#### Principled Hair BSDF

- [snd](snd.md#snd) :white_small_square: [principled_hair_bsdf](snd.md#principled_hair_bsdf)
- [Shader](shader.md#shader) :white_small_square: [PrincipledHair](shader.md#principledhair)

#### Principled Volume

- [snd](snd.md#snd) :white_small_square: [principled_volume](snd.md#principled_volume)
- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [Principled](volumeshader.md#principled)

#### Ray Portal BSDF

- [snd](snd.md#snd) :white_small_square: [ray_portal_bsdf](snd.md#ray_portal_bsdf)
- [Shader](shader.md#shader) :white_small_square: [RayPortal](shader.md#rayportal)

#### Refraction BSDF

- [snd](snd.md#snd) :white_small_square: [refraction_bsdf](snd.md#refraction_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Refraction](shader.md#refraction)

#### Reroute

- [snd](snd.md#snd) :white_small_square: [reroute](snd.md#reroute)

#### RGB

- [Color](color.md#color) :white_small_square: [RGB](color.md#rgb)

#### RGB Curves

- [snd](snd.md#snd) :white_small_square: [rgb_curves](snd.md#rgb_curves)

#### RGB to BW

- [snd](snd.md#snd) :white_small_square: [rgb_to_bw](snd.md#rgb_to_bw)
- [Color](color.md#color) :white_small_square: [rgb_to_bw](color.md#rgb_to_bw)
- [Color](color.md#color) :white_small_square: [to_bw](color.md#to_bw)

#### Script

- [snd](snd.md#snd) :white_small_square: [script](snd.md#script)

#### Separate Color

- [snd](snd.md#snd) :white_small_square: [separate_color](snd.md#separate_color)
- [Color](color.md#color) :white_small_square: [separate_col](color.md#separate_col)
- [Color](color.md#color) :white_small_square: [separate_col_HSL](color.md#separate_col_hsl)
- [Color](color.md#color) :white_small_square: [separate_col_HSV](color.md#separate_col_hsv)
- [Color](color.md#color) :white_small_square: [separate_col_RGB](color.md#separate_col_rgb)

#### Separate XYZ

- [snd](snd.md#snd) :white_small_square: [separate_xyz](snd.md#separate_xyz)

#### Shader to RGB

- [snd](snd.md#snd) :white_small_square: [shader_to_rgb](snd.md#shader_to_rgb)
- [Color](color.md#color) :white_small_square: [FromShader](color.md#fromshader)
- [Shader](shader.md#shader) :white_small_square: [to_rgb](shader.md#to_rgb)

#### Sheen BSDF

- [snd](snd.md#snd) :white_small_square: [sheen_bsdf](snd.md#sheen_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Sheen](shader.md#sheen)

#### Sky Texture

- [snd](snd.md#snd) :white_small_square: [sky_texture](snd.md#sky_texture)
- [Color](color.md#color) :white_small_square: [SkyTexture](color.md#skytexture)

#### Specular BSDF

- [snd](snd.md#snd) :white_small_square: [specular_bsdf](snd.md#specular_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Specular](shader.md#specular)

#### Subsurface Scattering

- [snd](snd.md#snd) :white_small_square: [subsurface_scattering](snd.md#subsurface_scattering)
- [Shader](shader.md#shader) :white_small_square: [SubsurfaceScattering](shader.md#subsurfacescattering)

#### Tangent

- [snd](snd.md#snd) :white_small_square: [tangent](snd.md#tangent)
- [Vector](vector.md#vector) :white_small_square: [Tangent](vector.md#tangent)

#### Texture Coordinate

- [snd](snd.md#snd) :white_small_square: [texture_coordinate](snd.md#texture_coordinate)

#### to Euler

- [Vector](vector.md#vector) :white_small_square: [FromRotation](vector.md#fromrotation)

#### Toon BSDF

- [snd](snd.md#snd) :white_small_square: [toon_bsdf](snd.md#toon_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Toon](shader.md#toon)

#### Translucent BSDF

- [snd](snd.md#snd) :white_small_square: [translucent_bsdf](snd.md#translucent_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Translucent](shader.md#translucent)

#### Transparent BSDF

- [snd](snd.md#snd) :white_small_square: [transparent_bsdf](snd.md#transparent_bsdf)
- [Shader](shader.md#shader) :white_small_square: [Transparent](shader.md#transparent)

#### UV Along Stroke

- [snd](snd.md#snd) :white_small_square: [uv_along_stroke](snd.md#uv_along_stroke)

#### UV Map

- [snd](snd.md#snd) :white_small_square: [uv_map](snd.md#uv_map)
- [Vector](vector.md#vector) :white_small_square: [UVMap](vector.md#uvmap)
- [Vector](vector.md#vector) :white_small_square: [UvMap](vector.md#uvmap)

#### Vector Curves

- [snd](snd.md#snd) :white_small_square: [vector_curves](snd.md#vector_curves)

#### Vector Displacement

- [snd](snd.md#snd) :white_small_square: [vector_displacement](snd.md#vector_displacement)
- [Color](color.md#color) :white_small_square: [vector_displacement](color.md#vector_displacement)
- [Vector](vector.md#vector) :white_small_square: [vector_displacement](vector.md#vector_displacement)

#### Vector Math

- [snd](snd.md#snd) :white_small_square: [vector_math](snd.md#vector_math)

#### Vector Rotate

- [snd](snd.md#snd) :white_small_square: [vector_rotate](snd.md#vector_rotate)

#### Vector Transform

- [snd](snd.md#snd) :white_small_square: [vector_transform](snd.md#vector_transform)
- [Vector](vector.md#vector) :white_small_square: [transform](vector.md#transform)
- [Vector](vector.md#vector) :white_small_square: [vector_transform](vector.md#vector_transform)

#### Volume Absorption

- [snd](snd.md#snd) :white_small_square: [volume_absorption](snd.md#volume_absorption)
- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [Absorption](volumeshader.md#absorption)

#### Volume Info

- [snd](snd.md#snd) :white_small_square: [volume_info](snd.md#volume_info)
- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [info](volumeshader.md#info)

#### Volume Scatter

- [snd](snd.md#snd) :white_small_square: [volume_scatter](snd.md#volume_scatter)
- [VolumeShader](volumeshader.md#volumeshader) :white_small_square: [Scatter](volumeshader.md#scatter)

#### Voronoi Texture

- [snd](snd.md#snd) :white_small_square: [voronoi_texture](snd.md#voronoi_texture)

#### Wave Texture

- [snd](snd.md#snd) :white_small_square: [wave_texture](snd.md#wave_texture)

#### Wavelength

- [snd](snd.md#snd) :white_small_square: [wavelength](snd.md#wavelength)
- [Color](color.md#color) :white_small_square: [Wavelength](color.md#wavelength)
- [Float](float.md#float) :white_small_square: [wavelength](float.md#wavelength)

#### White Noise Texture

- [snd](snd.md#snd) :white_small_square: [white_noise_texture](snd.md#white_noise_texture)

#### Wireframe

- [snd](snd.md#snd) :white_small_square: [wireframe](snd.md#wireframe)
- [Float](float.md#float) :white_small_square: [wireframe](float.md#wireframe)

#### World Output

- [snd](snd.md#snd) :white_small_square: [world_output](snd.md#world_output)
- [Shader](shader.md#shader) :white_small_square: [world_output](shader.md#world_output)