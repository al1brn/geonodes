# Shader Cross Reference

You will find here how nodes are implemented

## Content

- **&** : [&Material Output](shader_cross_reference.md#&material-output)
- **A** : [Add Shader](shader_cross_reference.md#add-shader) :black_small_square: [Ambient Occlusion](shader_cross_reference.md#ambient-occlusion) :black_small_square: [AOV Output](shader_cross_reference.md#aov-output) :black_small_square: [Attribute](shader_cross_reference.md#attribute)
- **B** : [Background](shader_cross_reference.md#background) :black_small_square: [Bevel](shader_cross_reference.md#bevel) :black_small_square: [Blackbody](shader_cross_reference.md#blackbody) :black_small_square: [Brick Texture](shader_cross_reference.md#brick-texture) :black_small_square: [Brightness Contrast](shader_cross_reference.md#brightness-contrast) :black_small_square: [Bump](shader_cross_reference.md#bump)
- **C** : [Checker Texture](shader_cross_reference.md#checker-texture) :black_small_square: [Clamp](shader_cross_reference.md#clamp) :black_small_square: [Color Attribute](shader_cross_reference.md#color-attribute) :black_small_square: [Color Ramp](shader_cross_reference.md#color-ramp) :black_small_square: [Combine Color](shader_cross_reference.md#combine-color) :black_small_square: [Combine XYZ](shader_cross_reference.md#combine-xyz)
- **D** : [Diffuse BSDF](shader_cross_reference.md#diffuse-bsdf) :black_small_square: [Displacement](shader_cross_reference.md#displacement)
- **E** : [Emission](shader_cross_reference.md#emission) :black_small_square: [Environment Texture](shader_cross_reference.md#environment-texture)
- **F** : [Float Curve](shader_cross_reference.md#float-curve) :black_small_square: [Frame](shader_cross_reference.md#frame) :black_small_square: [Fresnel](shader_cross_reference.md#fresnel)
- **G** : [Gabor Texture](shader_cross_reference.md#gabor-texture) :black_small_square: [Gamma](shader_cross_reference.md#gamma) :black_small_square: [Glass BSDF](shader_cross_reference.md#glass-bsdf) :black_small_square: [Glossy BSDF](shader_cross_reference.md#glossy-bsdf) :black_small_square: [Gradient Texture](shader_cross_reference.md#gradient-texture) :black_small_square: [Group](shader_cross_reference.md#group) :black_small_square: [Group Output](shader_cross_reference.md#group-output)
- **H** : [Hair BSDF](shader_cross_reference.md#hair-bsdf) :black_small_square: [Holdout](shader_cross_reference.md#holdout) :black_small_square: [Hue Saturation Value](shader_cross_reference.md#hue-saturation-value)
- **I** : [IES Texture](shader_cross_reference.md#ies-texture) :black_small_square: [Image Texture](shader_cross_reference.md#image-texture) :black_small_square: [Input](shader_cross_reference.md#input) :black_small_square: [Invert Color](shader_cross_reference.md#invert-color)
- **L** : [Layer Weight](shader_cross_reference.md#layer-weight) :black_small_square: [Light Falloff](shader_cross_reference.md#light-falloff) :black_small_square: [Light Output](shader_cross_reference.md#light-output) :black_small_square: [Line Style Output](shader_cross_reference.md#line-style-output)
- **M** : [Magic Texture](shader_cross_reference.md#magic-texture) :black_small_square: [Map Range](shader_cross_reference.md#map-range) :black_small_square: [Mapping](shader_cross_reference.md#mapping) :black_small_square: [Material Output](shader_cross_reference.md#material-output) :black_small_square: [Math](shader_cross_reference.md#math) :black_small_square: [Metallic BSDF](shader_cross_reference.md#metallic-bsdf) :black_small_square: [Mix](shader_cross_reference.md#mix) :black_small_square: [Mix Shader](shader_cross_reference.md#mix-shader)
- **N** : [Noise Texture](shader_cross_reference.md#noise-texture) :black_small_square: [Normal](shader_cross_reference.md#normal) :black_small_square: [Normal Map](shader_cross_reference.md#normal-map)
- **O** : [of curve](shader_cross_reference.md#of-curve) :black_small_square: [of Point](shader_cross_reference.md#of-point) :black_small_square: [Output](shader_cross_reference.md#output)
- **P** : [Point Density](shader_cross_reference.md#point-density) :black_small_square: [Point in Curve](shader_cross_reference.md#point-in-curve) :black_small_square: [Principled BSDF](shader_cross_reference.md#principled-bsdf) :black_small_square: [Principled Hair BSDF](shader_cross_reference.md#principled-hair-bsdf) :black_small_square: [Principled Volume](shader_cross_reference.md#principled-volume)
- **R** : [Ray Portal BSDF](shader_cross_reference.md#ray-portal-bsdf) :black_small_square: [Refraction BSDF](shader_cross_reference.md#refraction-bsdf) :black_small_square: [Reroute](shader_cross_reference.md#reroute) :black_small_square: [RGB Curves](shader_cross_reference.md#rgb-curves) :black_small_square: [RGB to BW](shader_cross_reference.md#rgb-to-bw)
- **S** : [Script](shader_cross_reference.md#script) :black_small_square: [Separate Color](shader_cross_reference.md#separate-color) :black_small_square: [Separate XYZ](shader_cross_reference.md#separate-xyz) :black_small_square: [Shader to RGB](shader_cross_reference.md#shader-to-rgb) :black_small_square: [Sheen BSDF](shader_cross_reference.md#sheen-bsdf) :black_small_square: [Size](shader_cross_reference.md#size) :black_small_square: [Sky Texture](shader_cross_reference.md#sky-texture) :black_small_square: [Specular BSDF](shader_cross_reference.md#specular-bsdf) :black_small_square: [Subsurface Scattering](shader_cross_reference.md#subsurface-scattering)
- **T** : [Tangent](shader_cross_reference.md#tangent) :black_small_square: [Texture Coordinate](shader_cross_reference.md#texture-coordinate) :black_small_square: [to Euler](shader_cross_reference.md#to-euler) :black_small_square: [to Rotation](shader_cross_reference.md#to-rotation) :black_small_square: [Toon BSDF](shader_cross_reference.md#toon-bsdf) :black_small_square: [Translucent BSDF](shader_cross_reference.md#translucent-bsdf) :black_small_square: [Transparent BSDF](shader_cross_reference.md#transparent-bsdf)
- **U** : [UV Along Stroke](shader_cross_reference.md#uv-along-stroke) :black_small_square: [UV Map](shader_cross_reference.md#uv-map)
- **V** : [Value](shader_cross_reference.md#value) :black_small_square: [Vector Curves](shader_cross_reference.md#vector-curves) :black_small_square: [Vector Displacement](shader_cross_reference.md#vector-displacement) :black_small_square: [Vector Math](shader_cross_reference.md#vector-math) :black_small_square: [Vector Rotate](shader_cross_reference.md#vector-rotate) :black_small_square: [Vector Transform](shader_cross_reference.md#vector-transform) :black_small_square: [Volume Absorption](shader_cross_reference.md#volume-absorption) :black_small_square: [Volume Scatter](shader_cross_reference.md#volume-scatter) :black_small_square: [Voronoi Texture](shader_cross_reference.md#voronoi-texture)
- **W** : [Wave Texture](shader_cross_reference.md#wave-texture) :black_small_square: [Wavelength](shader_cross_reference.md#wavelength) :black_small_square: [White Noise Texture](shader_cross_reference.md#white-noise-texture) :black_small_square: [Wireframe](shader_cross_reference.md#wireframe) :black_small_square: [World Output](shader_cross_reference.md#world-output)
- **X** : [XYZ](shader_cross_reference.md#xyz)

#### &Material Output

- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Add Shader

- [snd](core-allno-snd.md#snd) :white_small_square: [add_shader](core-allno-snd.md#add_shader)

#### Ambient Occlusion

- [snd](core-allno-snd.md#snd) :white_small_square: [ambient_occlusion](core-allno-snd.md#ambient_occlusion)

#### AOV Output

- [snd](core-allno-snd.md#snd) :white_small_square: [aov_output](core-allno-snd.md#aov_output)
- [Color](color.md#color) :white_small_square: [out](color.md#out)
- [Float](float.md#float) :white_small_square: [out](float.md#out)
- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Attribute

- [snd](core-allno-snd.md#snd) :white_small_square: [attribute](core-allno-snd.md#attribute)

#### Background

- [snd](core-allno-snd.md#snd) :white_small_square: [background](core-allno-snd.md#background)

#### Bevel

- [snd](core-allno-snd.md#snd) :white_small_square: [bevel](core-allno-snd.md#bevel)

#### Blackbody

- [nd](nd.md#nd) :white_small_square: [blackbody](nd.md#blackbody)
- [snd](core-allno-snd.md#snd) :white_small_square: [blackbody](core-allno-snd.md#blackbody)
- [Color](color.md#color) :white_small_square: [Blackbody](color.md#blackbody)

#### Brick Texture

- [nd](nd.md#nd) :white_small_square: [brick_texture](nd.md#brick_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [brick_texture](core-allno-snd.md#brick_texture)

#### Brightness Contrast

- [snd](core-allno-snd.md#snd) :white_small_square: [brightness_contrast](core-allno-snd.md#brightness_contrast)
- [Color](color.md#color) :white_small_square: [brightness_contrast](color.md#brightness_contrast)

#### Bump

- [snd](core-allno-snd.md#snd) :white_small_square: [bump](core-allno-snd.md#bump)
- [Vector](vector.md#vector) :white_small_square: [bump](vector.md#bump)

#### Checker Texture

- [nd](nd.md#nd) :white_small_square: [checker_texture](nd.md#checker_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [checker_texture](core-allno-snd.md#checker_texture)

#### Clamp

- [nd](nd.md#nd) :white_small_square: [clamp](nd.md#clamp)
- [snd](core-allno-snd.md#snd) :white_small_square: [clamp](core-allno-snd.md#clamp)

#### Color Attribute

- [snd](core-allno-snd.md#snd) :white_small_square: [color_attribute](core-allno-snd.md#color_attribute)
- [Color](color.md#color) :white_small_square: [Attribute](color.md#attribute)
- [Color](color.md#color) :white_small_square: [ambient_occlusion](color.md#ambient_occlusion)

#### Color Ramp

- [nd](nd.md#nd) :white_small_square: [color_ramp](nd.md#color_ramp)
- [snd](core-allno-snd.md#snd) :white_small_square: [color_ramp](core-allno-snd.md#color_ramp)

#### Combine Color

- [snd](core-allno-snd.md#snd) :white_small_square: [combine_color](core-allno-snd.md#combine_color)

#### Combine XYZ

- [nd](nd.md#nd) :white_small_square: [combine_xyz](nd.md#combine_xyz)
- [snd](core-allno-snd.md#snd) :white_small_square: [combine_xyz](core-allno-snd.md#combine_xyz)

#### Diffuse BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [diffuse_bsdf](core-allno-snd.md#diffuse_bsdf)

#### Displacement

- [snd](core-allno-snd.md#snd) :white_small_square: [displacement](core-allno-snd.md#displacement)
- [Vector](vector.md#vector) :white_small_square: [displacement](vector.md#displacement)

#### Emission

- [snd](core-allno-snd.md#snd) :white_small_square: [emission](core-allno-snd.md#emission)

#### Environment Texture

- [snd](core-allno-snd.md#snd) :white_small_square: [environment_texture](core-allno-snd.md#environment_texture)

#### Float Curve

- [nd](nd.md#nd) :white_small_square: [float_curve](nd.md#float_curve)
- [snd](core-allno-snd.md#snd) :white_small_square: [float_curve](core-allno-snd.md#float_curve)

#### Frame

- [nd](nd.md#nd) :white_small_square: [frame](nd.md#frame)
- [snd](core-allno-snd.md#snd) :white_small_square: [frame](core-allno-snd.md#frame)

#### Fresnel

- [snd](core-allno-snd.md#snd) :white_small_square: [fresnel](core-allno-snd.md#fresnel)

#### Gabor Texture

- [nd](nd.md#nd) :white_small_square: [gabor_texture](nd.md#gabor_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [gabor_texture](core-allno-snd.md#gabor_texture)

#### Gamma

- [snd](core-allno-snd.md#snd) :white_small_square: [gamma](core-allno-snd.md#gamma)
- [Color](color.md#color) :white_small_square: [gamma](color.md#gamma)

#### Glass BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [glass_bsdf](core-allno-snd.md#glass_bsdf)

#### Glossy BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [glossy_bsdf](core-allno-snd.md#glossy_bsdf)

#### Gradient Texture

- [nd](nd.md#nd) :white_small_square: [gradient_texture](nd.md#gradient_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [gradient_texture](core-allno-snd.md#gradient_texture)

#### Group

- [snd](core-allno-snd.md#snd) :white_small_square: [group](core-allno-snd.md#group)

#### Group Output

- [nd](nd.md#nd) :white_small_square: [group_output](nd.md#group_output)
- [snd](core-allno-snd.md#snd) :white_small_square: [group_output](core-allno-snd.md#group_output)

#### Hair BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [hair_bsdf](core-allno-snd.md#hair_bsdf)

#### Holdout

- [snd](core-allno-snd.md#snd) :white_small_square: [holdout](core-allno-snd.md#holdout)

#### Hue Saturation Value

- [snd](core-allno-snd.md#snd) :white_small_square: [hue_saturation_value](core-allno-snd.md#hue_saturation_value)
- [Color](color.md#color) :white_small_square: [hue_saturation_value](color.md#hue_saturation_value)

#### IES Texture

- [snd](core-allno-snd.md#snd) :white_small_square: [ies_texture](core-allno-snd.md#ies_texture)

#### Image Texture

- [snd](core-allno-snd.md#snd) :white_small_square: [image_texture](core-allno-snd.md#image_texture)

#### Input

- [Tree](tree.md#tree) :white_small_square: [new_input](tree.md#new_input)

#### Invert Color

- [snd](core-allno-snd.md#snd) :white_small_square: [invert_color](core-allno-snd.md#invert_color)
- [Color](color.md#color) :white_small_square: [invert](color.md#invert)

#### Layer Weight

- [snd](core-allno-snd.md#snd) :white_small_square: [layer_weight](core-allno-snd.md#layer_weight)

#### Light Falloff

- [snd](core-allno-snd.md#snd) :white_small_square: [light_falloff](core-allno-snd.md#light_falloff)

#### Light Output

- [snd](core-allno-snd.md#snd) :white_small_square: [light_output](core-allno-snd.md#light_output)

#### Line Style Output

- [snd](core-allno-snd.md#snd) :white_small_square: [line_style_output](core-allno-snd.md#line_style_output)

#### Magic Texture

- [nd](nd.md#nd) :white_small_square: [magic_texture](nd.md#magic_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [magic_texture](core-allno-snd.md#magic_texture)

#### Map Range

- [nd](nd.md#nd) :white_small_square: [map_range](nd.md#map_range)
- [snd](core-allno-snd.md#snd) :white_small_square: [map_range](core-allno-snd.md#map_range)

#### Mapping

- [snd](core-allno-snd.md#snd) :white_small_square: [mapping](core-allno-snd.md#mapping)
- [Vector](vector.md#vector) :white_small_square: [mapping](vector.md#mapping)

#### Material Output

- [snd](core-allno-snd.md#snd) :white_small_square: [material_output](core-allno-snd.md#material_output)
- [Vector](vector.md#vector) :white_small_square: [displacement_out](vector.md#displacement_out)

#### Math

- [nd](nd.md#nd) :white_small_square: [math](nd.md#math)
- [snd](core-allno-snd.md#snd) :white_small_square: [math](core-allno-snd.md#math)

#### Metallic BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [metallic_bsdf](core-allno-snd.md#metallic_bsdf)

#### Mix

- [nd](nd.md#nd) :white_small_square: [mix](nd.md#mix)
- [snd](core-allno-snd.md#snd) :white_small_square: [mix](core-allno-snd.md#mix)

#### Mix Shader

- [snd](core-allno-snd.md#snd) :white_small_square: [mix_shader](core-allno-snd.md#mix_shader)

#### Noise Texture

- [nd](nd.md#nd) :white_small_square: [noise_texture](nd.md#noise_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [noise_texture](core-allno-snd.md#noise_texture)

#### Normal

- [snd](core-allno-snd.md#snd) :white_small_square: [normal](core-allno-snd.md#normal)
- [Vector](vector.md#vector) :white_small_square: [normal](vector.md#normal)

#### Normal Map

- [snd](core-allno-snd.md#snd) :white_small_square: [normal_map](core-allno-snd.md#normal_map)
- [Color](color.md#color) :white_small_square: [normal_map](color.md#normal_map)
- [Vector](vector.md#vector) :white_small_square: [NormalMap](vector.md#normalmap)

#### of curve

- [Spline](spline.md#spline) :white_small_square: [points](spline.md#points)

#### of Point

- [SplinePoint](splinepoint.md#splinepoint) :white_small_square: [curve_index](splinepoint.md#curve_index)
- [SplinePoint](splinepoint.md#splinepoint) :white_small_square: [index_in_curve](splinepoint.md#index_in_curve)

#### Output

- [Tree](tree.md#tree) :white_small_square: [new_output](tree.md#new_output)

#### Point Density

- [snd](core-allno-snd.md#snd) :white_small_square: [point_density](core-allno-snd.md#point_density)

#### Point in Curve

- [SplinePoint](splinepoint.md#splinepoint) :white_small_square: [offset_in_curve](splinepoint.md#offset_in_curve)

#### Principled BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [principled_bsdf](core-allno-snd.md#principled_bsdf)

#### Principled Hair BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [principled_hair_bsdf](core-allno-snd.md#principled_hair_bsdf)

#### Principled Volume

- [snd](core-allno-snd.md#snd) :white_small_square: [principled_volume](core-allno-snd.md#principled_volume)

#### Ray Portal BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [ray_portal_bsdf](core-allno-snd.md#ray_portal_bsdf)

#### Refraction BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [refraction_bsdf](core-allno-snd.md#refraction_bsdf)

#### Reroute

- [nd](nd.md#nd) :white_small_square: [reroute](nd.md#reroute)
- [snd](core-allno-snd.md#snd) :white_small_square: [reroute](core-allno-snd.md#reroute)

#### RGB Curves

- [nd](nd.md#nd) :white_small_square: [rgb_curves](nd.md#rgb_curves)
- [snd](core-allno-snd.md#snd) :white_small_square: [rgb_curves](core-allno-snd.md#rgb_curves)

#### RGB to BW

- [snd](core-allno-snd.md#snd) :white_small_square: [rgb_to_bw](core-allno-snd.md#rgb_to_bw)
- [Color](color.md#color) :white_small_square: [to_bw](color.md#to_bw)

#### Script

- [snd](core-allno-snd.md#snd) :white_small_square: [script](core-allno-snd.md#script)

#### Separate Color

- [snd](core-allno-snd.md#snd) :white_small_square: [separate_color](core-allno-snd.md#separate_color)

#### Separate XYZ

- [nd](nd.md#nd) :white_small_square: [separate_xyz](nd.md#separate_xyz)
- [snd](core-allno-snd.md#snd) :white_small_square: [separate_xyz](core-allno-snd.md#separate_xyz)

#### Shader to RGB

- [snd](core-allno-snd.md#snd) :white_small_square: [shader_to_rgb](core-allno-snd.md#shader_to_rgb)
- [Color](color.md#color) :white_small_square: [FromShader](color.md#fromshader)

#### Sheen BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [sheen_bsdf](core-allno-snd.md#sheen_bsdf)

#### Size

- [Cloud](cloud.md#cloud) :white_small_square: [domain_size](cloud.md#domain_size)
- [Curve](curve.md#curve) :white_small_square: [domain_size](curve.md#domain_size)
- [GreasePencil](greasepencil.md#greasepencil) :white_small_square: [domain_size](greasepencil.md#domain_size)
- [Instances](instances.md#instances) :white_small_square: [domain_size](instances.md#domain_size)
- [Mesh](mesh.md#mesh) :white_small_square: [domain_size](mesh.md#domain_size)

#### Sky Texture

- [snd](core-allno-snd.md#snd) :white_small_square: [sky_texture](core-allno-snd.md#sky_texture)

#### Specular BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [specular_bsdf](core-allno-snd.md#specular_bsdf)

#### Subsurface Scattering

- [snd](core-allno-snd.md#snd) :white_small_square: [subsurface_scattering](core-allno-snd.md#subsurface_scattering)

#### Tangent

- [snd](core-allno-snd.md#snd) :white_small_square: [tangent](core-allno-snd.md#tangent)
- [Vector](vector.md#vector) :white_small_square: [Tangent](vector.md#tangent)

#### Texture Coordinate

- [snd](core-allno-snd.md#snd) :white_small_square: [texture_coordinate](core-allno-snd.md#texture_coordinate)

#### to Euler

- [Vector](vector.md#vector) :white_small_square: [FromRotation](vector.md#fromrotation)

#### to Rotation

- [Vector](vector.md#vector) :white_small_square: [to_rotation](vector.md#to_rotation)

#### Toon BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [toon_bsdf](core-allno-snd.md#toon_bsdf)

#### Translucent BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [translucent_bsdf](core-allno-snd.md#translucent_bsdf)

#### Transparent BSDF

- [snd](core-allno-snd.md#snd) :white_small_square: [transparent_bsdf](core-allno-snd.md#transparent_bsdf)

#### UV Along Stroke

- [snd](core-allno-snd.md#snd) :white_small_square: [uv_along_stroke](core-allno-snd.md#uv_along_stroke)

#### UV Map

- [snd](core-allno-snd.md#snd) :white_small_square: [uv_map](core-allno-snd.md#uv_map)
- [Vector](vector.md#vector) :white_small_square: [UVMap](vector.md#uvmap)

#### Value

- [Rotation](rotation.md#rotation) :white_small_square: [Random](rotation.md#random)
- [Vector](vector.md#vector) :white_small_square: [Random](vector.md#random)

#### Vector Curves

- [nd](nd.md#nd) :white_small_square: [vector_curves](nd.md#vector_curves)
- [snd](core-allno-snd.md#snd) :white_small_square: [vector_curves](core-allno-snd.md#vector_curves)

#### Vector Displacement

- [snd](core-allno-snd.md#snd) :white_small_square: [vector_displacement](core-allno-snd.md#vector_displacement)
- [Color](color.md#color) :white_small_square: [vector_displacement](color.md#vector_displacement)
- [Vector](vector.md#vector) :white_small_square: [vector_displacement](vector.md#vector_displacement)

#### Vector Math

- [nd](nd.md#nd) :white_small_square: [vector_math](nd.md#vector_math)
- [snd](core-allno-snd.md#snd) :white_small_square: [vector_math](core-allno-snd.md#vector_math)

#### Vector Rotate

- [nd](nd.md#nd) :white_small_square: [vector_rotate](nd.md#vector_rotate)
- [snd](core-allno-snd.md#snd) :white_small_square: [vector_rotate](core-allno-snd.md#vector_rotate)

#### Vector Transform

- [snd](core-allno-snd.md#snd) :white_small_square: [vector_transform](core-allno-snd.md#vector_transform)
- [Vector](vector.md#vector) :white_small_square: [transform](vector.md#transform)

#### Volume Absorption

- [snd](core-allno-snd.md#snd) :white_small_square: [volume_absorption](core-allno-snd.md#volume_absorption)

#### Volume Scatter

- [snd](core-allno-snd.md#snd) :white_small_square: [volume_scatter](core-allno-snd.md#volume_scatter)

#### Voronoi Texture

- [nd](nd.md#nd) :white_small_square: [voronoi_texture](nd.md#voronoi_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [voronoi_texture](core-allno-snd.md#voronoi_texture)

#### Wave Texture

- [nd](nd.md#nd) :white_small_square: [wave_texture](nd.md#wave_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [wave_texture](core-allno-snd.md#wave_texture)

#### Wavelength

- [snd](core-allno-snd.md#snd) :white_small_square: [wavelength](core-allno-snd.md#wavelength)
- [Color](color.md#color) :white_small_square: [Wavelength](color.md#wavelength)

#### White Noise Texture

- [nd](nd.md#nd) :white_small_square: [white_noise_texture](nd.md#white_noise_texture)
- [snd](core-allno-snd.md#snd) :white_small_square: [white_noise_texture](core-allno-snd.md#white_noise_texture)

#### Wireframe

- [snd](core-allno-snd.md#snd) :white_small_square: [wireframe](core-allno-snd.md#wireframe)

#### World Output

- [snd](core-allno-snd.md#snd) :white_small_square: [world_output](core-allno-snd.md#world_output)

#### XYZ

- [Rotation](rotation.md#rotation) :white_small_square: [Combine](rotation.md#combine)
- [Rotation](rotation.md#rotation) :white_small_square: [x](rotation.md#x)
- [Rotation](rotation.md#rotation) :white_small_square: [y](rotation.md#y)
- [Rotation](rotation.md#rotation) :white_small_square: [z](rotation.md#z)
- [Vector](vector.md#vector) :white_small_square: [Combine](vector.md#combine)
- [Vector](vector.md#vector) :white_small_square: [x](vector.md#x)
- [Vector](vector.md#vector) :white_small_square: [y](vector.md#y)
- [Vector](vector.md#vector) :white_small_square: [z](vector.md#z)