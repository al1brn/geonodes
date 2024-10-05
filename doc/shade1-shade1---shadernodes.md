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

- [snd](snd.md#snd)
- [add_shader](snd.md#add_shader)
- [ambient_occlusion](snd.md#ambient_occlusion)
- [aov_output](snd.md#aov_output)
- [attribute](snd.md#attribute)
- [background](snd.md#background)
- [bevel](snd.md#bevel)
- [blackbody](snd.md#blackbody)
- [brick_texture](snd.md#brick_texture)
- [brightness_contrast](snd.md#brightness_contrast)
- [bump](snd.md#bump)
- [checker_texture](snd.md#checker_texture)
- [clamp](snd.md#clamp)
- [color_attribute](snd.md#color_attribute)
- [color_ramp](snd.md#color_ramp)
- [combine_color](snd.md#combine_color)
- [combine_xyz](snd.md#combine_xyz)
- [diffuse_bsdf](snd.md#diffuse_bsdf)
- [displacement](snd.md#displacement)
- [emission](snd.md#emission)
- [environment_texture](snd.md#environment_texture)
- [float_curve](snd.md#float_curve)
- [frame](snd.md#frame)
- [fresnel](snd.md#fresnel)
- [gamma](snd.md#gamma)
- [glass_bsdf](snd.md#glass_bsdf)
- [glossy_bsdf](snd.md#glossy_bsdf)
- [gradient_texture](snd.md#gradient_texture)
- [group](snd.md#group)
- [group_output](snd.md#group_output)
- [hair_bsdf](snd.md#hair_bsdf)
- [holdout](snd.md#holdout)
- [hue_saturation_value](snd.md#hue_saturation_value)
- [ies_texture](snd.md#ies_texture)
- [image_texture](snd.md#image_texture)
- [invert_color](snd.md#invert_color)
- [layer_weight](snd.md#layer_weight)
- [light_falloff](snd.md#light_falloff)
- [light_output](snd.md#light_output)
- [line_style_output](snd.md#line_style_output)
- [magic_texture](snd.md#magic_texture)
- [mapping](snd.md#mapping)
- [map_range](snd.md#map_range)
- [material_output](snd.md#material_output)
- [math](snd.md#math)
- [mix](snd.md#mix)
- [mix_shader](snd.md#mix_shader)
- [noise_texture](snd.md#noise_texture)
- [normal](snd.md#normal)
- [normal_map](snd.md#normal_map)
- [point_density](snd.md#point_density)
- [position](snd.md#position)
- [principled_bsdf](snd.md#principled_bsdf)
- [principled_hair_bsdf](snd.md#principled_hair_bsdf)
- [principled_volume](snd.md#principled_volume)
- [ray_portal_bsdf](snd.md#ray_portal_bsdf)
- [refraction_bsdf](snd.md#refraction_bsdf)
- [reroute](snd.md#reroute)
- [rgb_curves](snd.md#rgb_curves)
- [rgb_to_bw](snd.md#rgb_to_bw)
- [script](snd.md#script)
- [separate_color](snd.md#separate_color)
- [separate_xyz](snd.md#separate_xyz)
- [shader_to_rgb](snd.md#shader_to_rgb)
- [sharp_face](snd.md#sharp_face)
- [sheen_bsdf](snd.md#sheen_bsdf)
- [sky_texture](snd.md#sky_texture)
- [specular_bsdf](snd.md#specular_bsdf)
- [subsurface_scattering](snd.md#subsurface_scattering)
- [tangent](snd.md#tangent)
- [texture_coordinate](snd.md#texture_coordinate)
- [toon_bsdf](snd.md#toon_bsdf)
- [translucent_bsdf](snd.md#translucent_bsdf)
- [transparent_bsdf](snd.md#transparent_bsdf)
- [uv_along_stroke](snd.md#uv_along_stroke)
- [uvmap](snd.md#uvmap)
- [uv_map](snd.md#uv_map)
- [vector_curves](snd.md#vector_curves)
- [vector_displacement](snd.md#vector_displacement)
- [vector_math](snd.md#vector_math)
- [vector_rotate](snd.md#vector_rotate)
- [vector_transform](snd.md#vector_transform)
- [volume_absorption](snd.md#volume_absorption)
- [volume_scatter](snd.md#volume_scatter)
- [voronoi_texture](snd.md#voronoi_texture)
- [wavelength](snd.md#wavelength)
- [wave_texture](snd.md#wave_texture)
- [white_noise_texture](snd.md#white_noise_texture)
- [wireframe](snd.md#wireframe)
- [world_output](snd.md#world_output)

## Classes



- [ShaderNodes](shade1-shade1-shadernodes.md#shadernodes)
- [snd](snd.md#snd)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [shadernodes](shade1-shade1---shadernodes.md#shadernodes) :black_small_square: [Content](shade1-shade1---shadernodes.md#content) :black_small_square: [shadernodes](shade1-shade1---shadernodes.md#shadernodes)</sub>