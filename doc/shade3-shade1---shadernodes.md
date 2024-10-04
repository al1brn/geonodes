# shadernodes

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Shader Nodes
-----------------------------------------------------

module : shadernodes
--------------------
- Implement Shader Nodes tree

classes
-------
- ShaderNodes      : Geometry Nodes tree
- nd               : Overrides static class with addition methods

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- [snd](shade3-shade1-snd.md#snd)
- [add_shader](shade3-shade1-snd.md#add_shader)
- [ambient_occlusion](shade3-shade1-snd.md#ambient_occlusion)
- [aov_output](shade3-shade1-snd.md#aov_output)
- [attribute](shade3-shade1-snd.md#attribute)
- [background](shade3-shade1-snd.md#background)
- [bevel](shade3-shade1-snd.md#bevel)
- [blackbody](shade3-shade1-snd.md#blackbody)
- [brick_texture](shade3-shade1-snd.md#brick_texture)
- [brightness_contrast](shade3-shade1-snd.md#brightness_contrast)
- [bump](shade3-shade1-snd.md#bump)
- [checker_texture](shade3-shade1-snd.md#checker_texture)
- [clamp](shade3-shade1-snd.md#clamp)
- [color_attribute](shade3-shade1-snd.md#color_attribute)
- [color_ramp](shade3-shade1-snd.md#color_ramp)
- [combine_color](shade3-shade1-snd.md#combine_color)
- [combine_xyz](shade3-shade1-snd.md#combine_xyz)
- [diffuse_bsdf](shade3-shade1-snd.md#diffuse_bsdf)
- [displacement](shade3-shade1-snd.md#displacement)
- [emission](shade3-shade1-snd.md#emission)
- [environment_texture](shade3-shade1-snd.md#environment_texture)
- [float_curve](shade3-shade1-snd.md#float_curve)
- [frame](shade3-shade1-snd.md#frame)
- [fresnel](shade3-shade1-snd.md#fresnel)
- [gamma](shade3-shade1-snd.md#gamma)
- [glass_bsdf](shade3-shade1-snd.md#glass_bsdf)
- [glossy_bsdf](shade3-shade1-snd.md#glossy_bsdf)
- [gradient_texture](shade3-shade1-snd.md#gradient_texture)
- [group](shade3-shade1-snd.md#group)
- [group_output](shade3-shade1-snd.md#group_output)
- [hair_bsdf](shade3-shade1-snd.md#hair_bsdf)
- [holdout](shade3-shade1-snd.md#holdout)
- [hue_saturation_value](shade3-shade1-snd.md#hue_saturation_value)
- [ies_texture](shade3-shade1-snd.md#ies_texture)
- [image_texture](shade3-shade1-snd.md#image_texture)
- [invert_color](shade3-shade1-snd.md#invert_color)
- [layer_weight](shade3-shade1-snd.md#layer_weight)
- [light_falloff](shade3-shade1-snd.md#light_falloff)
- [light_output](shade3-shade1-snd.md#light_output)
- [line_style_output](shade3-shade1-snd.md#line_style_output)
- [magic_texture](shade3-shade1-snd.md#magic_texture)
- [mapping](shade3-shade1-snd.md#mapping)
- [map_range](shade3-shade1-snd.md#map_range)
- [material_output](shade3-shade1-snd.md#material_output)
- [math](shade3-shade1-snd.md#math)
- [mix](shade3-shade1-snd.md#mix)
- [mix_shader](shade3-shade1-snd.md#mix_shader)
- [noise_texture](shade3-shade1-snd.md#noise_texture)
- [normal](shade3-shade1-snd.md#normal)
- [normal_map](shade3-shade1-snd.md#normal_map)
- [point_density](shade3-shade1-snd.md#point_density)
- [position](shade3-shade1-snd.md#position)
- [principled_bsdf](shade3-shade1-snd.md#principled_bsdf)
- [principled_hair_bsdf](shade3-shade1-snd.md#principled_hair_bsdf)
- [principled_volume](shade3-shade1-snd.md#principled_volume)
- [ray_portal_bsdf](shade3-shade1-snd.md#ray_portal_bsdf)
- [refraction_bsdf](shade3-shade1-snd.md#refraction_bsdf)
- [reroute](shade3-shade1-snd.md#reroute)
- [rgb_curves](shade3-shade1-snd.md#rgb_curves)
- [rgb_to_bw](shade3-shade1-snd.md#rgb_to_bw)
- [script](shade3-shade1-snd.md#script)
- [separate_color](shade3-shade1-snd.md#separate_color)
- [separate_xyz](shade3-shade1-snd.md#separate_xyz)
- [shader_to_rgb](shade3-shade1-snd.md#shader_to_rgb)
- [sharp_face](shade3-shade1-snd.md#sharp_face)
- [sheen_bsdf](shade3-shade1-snd.md#sheen_bsdf)
- [sky_texture](shade3-shade1-snd.md#sky_texture)
- [specular_bsdf](shade3-shade1-snd.md#specular_bsdf)
- [subsurface_scattering](shade3-shade1-snd.md#subsurface_scattering)
- [tangent](shade3-shade1-snd.md#tangent)
- [texture_coordinate](shade3-shade1-snd.md#texture_coordinate)
- [toon_bsdf](shade3-shade1-snd.md#toon_bsdf)
- [translucent_bsdf](shade3-shade1-snd.md#translucent_bsdf)
- [transparent_bsdf](shade3-shade1-snd.md#transparent_bsdf)
- [uv_along_stroke](shade3-shade1-snd.md#uv_along_stroke)
- [uvmap](shade3-shade1-snd.md#uvmap)
- [uv_map](shade3-shade1-snd.md#uv_map)
- [vector_curves](shade3-shade1-snd.md#vector_curves)
- [vector_displacement](shade3-shade1-snd.md#vector_displacement)
- [vector_math](shade3-shade1-snd.md#vector_math)
- [vector_rotate](shade3-shade1-snd.md#vector_rotate)
- [vector_transform](shade3-shade1-snd.md#vector_transform)
- [volume_absorption](shade3-shade1-snd.md#volume_absorption)
- [volume_scatter](shade3-shade1-snd.md#volume_scatter)
- [voronoi_texture](shade3-shade1-snd.md#voronoi_texture)
- [wavelength](shade3-shade1-snd.md#wavelength)
- [wave_texture](shade3-shade1-snd.md#wave_texture)
- [white_noise_texture](shade3-shade1-snd.md#white_noise_texture)
- [wireframe](shade3-shade1-snd.md#wireframe)
- [world_output](shade3-shade1-snd.md#world_output)

## Classes



- [ShaderNodes](shade3-shade1-shadernodes.md#shadernodes)
- [snd](shade3-shade1-snd.md#snd)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [shadernodes](shade3-shade1---shadernodes.md#shadernodes) :black_small_square: [Content](shade3-shade1---shadernodes.md#content) :black_small_square: [shadernodes](shade3-shade1---shadernodes.md#shadernodes)</sub>