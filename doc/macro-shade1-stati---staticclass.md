# staticclass

Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : staticclass
--------------------
- Functional nodes

Functional nodes are nodes which can't be considered as methods or properties of a data class.
Functional nodes also include input nodes such as 'Position' or 'Index'. Theses nodes should be considered
as properties of geometry but to ease the scripting, there are also implemented as functions.

Functional nodes are implemented as static functions and properties or a class named nd which is short.

```  python
# Some functional nodes
pos = nd.position
i = nd.index
attr = named_attribute(name, 'FLOAT')
```

classes
-------
- Texture       : Implements the texture nodes creation
    - Brick
    - Checker
    - Gradient
    - Image
    - Magic
    - Noise
    - Voronoi
    - Wave
    - WhiteNoise


functions
---------

updates
-------
- creation : 2024/07/23

## Content

- [StaticClass](macro-shade1-stati-staticclass.md#staticclass)
- [add_shader](macro-shade1-stati-staticclass.md#add_shader)
- [ambient_occlusion](macro-shade1-stati-staticclass.md#ambient_occlusion)
- [aov_output](macro-shade1-stati-staticclass.md#aov_output)
- [attribute](macro-shade1-stati-staticclass.md#attribute)
- [background](macro-shade1-stati-staticclass.md#background)
- [bevel](macro-shade1-stati-staticclass.md#bevel)
- [blackbody](macro-shade1-stati-staticclass.md#blackbody)
- [brick_texture](macro-shade1-stati-staticclass.md#brick_texture)
- [brightness_contrast](macro-shade1-stati-staticclass.md#brightness_contrast)
- [bump](macro-shade1-stati-staticclass.md#bump)
- [checker_texture](macro-shade1-stati-staticclass.md#checker_texture)
- [clamp](macro-shade1-stati-staticclass.md#clamp)
- [color_attribute](macro-shade1-stati-staticclass.md#color_attribute)
- [color_ramp](macro-shade1-stati-staticclass.md#color_ramp)
- [combine_color](macro-shade1-stati-staticclass.md#combine_color)
- [combine_xyz](macro-shade1-stati-staticclass.md#combine_xyz)
- [diffuse_bsdf](macro-shade1-stati-staticclass.md#diffuse_bsdf)
- [displacement](macro-shade1-stati-staticclass.md#displacement)
- [emission](macro-shade1-stati-staticclass.md#emission)
- [environment_texture](macro-shade1-stati-staticclass.md#environment_texture)
- [float_curve](macro-shade1-stati-staticclass.md#float_curve)
- [frame](macro-shade1-stati-staticclass.md#frame)
- [fresnel](macro-shade1-stati-staticclass.md#fresnel)
- [gamma](macro-shade1-stati-staticclass.md#gamma)
- [glass_bsdf](macro-shade1-stati-staticclass.md#glass_bsdf)
- [glossy_bsdf](macro-shade1-stati-staticclass.md#glossy_bsdf)
- [gradient_texture](macro-shade1-stati-staticclass.md#gradient_texture)
- [group](macro-shade1-stati-staticclass.md#group)
- [group_output](macro-shade1-stati-staticclass.md#group_output)
- [hair_bsdf](macro-shade1-stati-staticclass.md#hair_bsdf)
- [holdout](macro-shade1-stati-staticclass.md#holdout)
- [hue_saturation_value](macro-shade1-stati-staticclass.md#hue_saturation_value)
- [ies_texture](macro-shade1-stati-staticclass.md#ies_texture)
- [image_texture](macro-shade1-stati-staticclass.md#image_texture)
- [invert_color](macro-shade1-stati-staticclass.md#invert_color)
- [layer_weight](macro-shade1-stati-staticclass.md#layer_weight)
- [light_falloff](macro-shade1-stati-staticclass.md#light_falloff)
- [light_output](macro-shade1-stati-staticclass.md#light_output)
- [line_style_output](macro-shade1-stati-staticclass.md#line_style_output)
- [magic_texture](macro-shade1-stati-staticclass.md#magic_texture)
- [mapping](macro-shade1-stati-staticclass.md#mapping)
- [map_range](macro-shade1-stati-staticclass.md#map_range)
- [material_output](macro-shade1-stati-staticclass.md#material_output)
- [math](macro-shade1-stati-staticclass.md#math)
- [mix](macro-shade1-stati-staticclass.md#mix)
- [mix_shader](macro-shade1-stati-staticclass.md#mix_shader)
- [noise_texture](macro-shade1-stati-staticclass.md#noise_texture)
- [normal](macro-shade1-stati-staticclass.md#normal)
- [normal_map](macro-shade1-stati-staticclass.md#normal_map)
- [point_density](macro-shade1-stati-staticclass.md#point_density)
- [principled_bsdf](macro-shade1-stati-staticclass.md#principled_bsdf)
- [principled_hair_bsdf](macro-shade1-stati-staticclass.md#principled_hair_bsdf)
- [principled_volume](macro-shade1-stati-staticclass.md#principled_volume)
- [ray_portal_bsdf](macro-shade1-stati-staticclass.md#ray_portal_bsdf)
- [refraction_bsdf](macro-shade1-stati-staticclass.md#refraction_bsdf)
- [reroute](macro-shade1-stati-staticclass.md#reroute)
- [rgb_curves](macro-shade1-stati-staticclass.md#rgb_curves)
- [rgb_to_bw](macro-shade1-stati-staticclass.md#rgb_to_bw)
- [script](macro-shade1-stati-staticclass.md#script)
- [separate_color](macro-shade1-stati-staticclass.md#separate_color)
- [separate_xyz](macro-shade1-stati-staticclass.md#separate_xyz)
- [shader_to_rgb](macro-shade1-stati-staticclass.md#shader_to_rgb)
- [sheen_bsdf](macro-shade1-stati-staticclass.md#sheen_bsdf)
- [sky_texture](macro-shade1-stati-staticclass.md#sky_texture)
- [specular_bsdf](macro-shade1-stati-staticclass.md#specular_bsdf)
- [subsurface_scattering](macro-shade1-stati-staticclass.md#subsurface_scattering)
- [tangent](macro-shade1-stati-staticclass.md#tangent)
- [texture_coordinate](macro-shade1-stati-staticclass.md#texture_coordinate)
- [toon_bsdf](macro-shade1-stati-staticclass.md#toon_bsdf)
- [translucent_bsdf](macro-shade1-stati-staticclass.md#translucent_bsdf)
- [transparent_bsdf](macro-shade1-stati-staticclass.md#transparent_bsdf)
- [uv_along_stroke](macro-shade1-stati-staticclass.md#uv_along_stroke)
- [uv_map](macro-shade1-stati-staticclass.md#uv_map)
- [vector_curves](macro-shade1-stati-staticclass.md#vector_curves)
- [vector_displacement](macro-shade1-stati-staticclass.md#vector_displacement)
- [vector_math](macro-shade1-stati-staticclass.md#vector_math)
- [vector_rotate](macro-shade1-stati-staticclass.md#vector_rotate)
- [vector_transform](macro-shade1-stati-staticclass.md#vector_transform)
- [volume_absorption](macro-shade1-stati-staticclass.md#volume_absorption)
- [volume_scatter](macro-shade1-stati-staticclass.md#volume_scatter)
- [voronoi_texture](macro-shade1-stati-staticclass.md#voronoi_texture)
- [wavelength](macro-shade1-stati-staticclass.md#wavelength)
- [wave_texture](macro-shade1-stati-staticclass.md#wave_texture)
- [white_noise_texture](macro-shade1-stati-staticclass.md#white_noise_texture)
- [wireframe](macro-shade1-stati-staticclass.md#wireframe)
- [world_output](macro-shade1-stati-staticclass.md#world_output)

## Classes



- [StaticClass](macro-shade1-stati-staticclass.md#staticclass)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [staticclass](macro-shade1-stati---staticclass.md#staticclass) :black_small_square: [Content](macro-shade1-stati---staticclass.md#content) :black_small_square: [staticclass](macro-shade1-stati---staticclass.md#staticclass)</sub>