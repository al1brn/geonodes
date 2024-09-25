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

- [StaticClass](shade-stati-staticclass.md)
- [add_shader](shade-stati-staticclass.md#add_shader)
- [ambient_occlusion](shade-stati-staticclass.md#ambient_occlusion)
- [aov_output](shade-stati-staticclass.md#aov_output)
- [attribute](shade-stati-staticclass.md#attribute)
- [background](shade-stati-staticclass.md#background)
- [bevel](shade-stati-staticclass.md#bevel)
- [blackbody](shade-stati-staticclass.md#blackbody)
- [brick_texture](shade-stati-staticclass.md#brick_texture)
- [brightness_contrast](shade-stati-staticclass.md#brightness_contrast)
- [bump](shade-stati-staticclass.md#bump)
- [checker_texture](shade-stati-staticclass.md#checker_texture)
- [clamp](shade-stati-staticclass.md#clamp)
- [color_attribute](shade-stati-staticclass.md#color_attribute)
- [color_ramp](shade-stati-staticclass.md#color_ramp)
- [combine_color](shade-stati-staticclass.md#combine_color)
- [combine_xyz](shade-stati-staticclass.md#combine_xyz)
- [diffuse_bsdf](shade-stati-staticclass.md#diffuse_bsdf)
- [displacement](shade-stati-staticclass.md#displacement)
- [emission](shade-stati-staticclass.md#emission)
- [environment_texture](shade-stati-staticclass.md#environment_texture)
- [float_curve](shade-stati-staticclass.md#float_curve)
- [frame](shade-stati-staticclass.md#frame)
- [fresnel](shade-stati-staticclass.md#fresnel)
- [gamma](shade-stati-staticclass.md#gamma)
- [glass_bsdf](shade-stati-staticclass.md#glass_bsdf)
- [glossy_bsdf](shade-stati-staticclass.md#glossy_bsdf)
- [gradient_texture](shade-stati-staticclass.md#gradient_texture)
- [group](shade-stati-staticclass.md#group)
- [group_output](shade-stati-staticclass.md#group_output)
- [hair_bsdf](shade-stati-staticclass.md#hair_bsdf)
- [holdout](shade-stati-staticclass.md#holdout)
- [hue_saturation_value](shade-stati-staticclass.md#hue_saturation_value)
- [ies_texture](shade-stati-staticclass.md#ies_texture)
- [image_texture](shade-stati-staticclass.md#image_texture)
- [invert_color](shade-stati-staticclass.md#invert_color)
- [layer_weight](shade-stati-staticclass.md#layer_weight)
- [light_falloff](shade-stati-staticclass.md#light_falloff)
- [light_output](shade-stati-staticclass.md#light_output)
- [line_style_output](shade-stati-staticclass.md#line_style_output)
- [magic_texture](shade-stati-staticclass.md#magic_texture)
- [mapping](shade-stati-staticclass.md#mapping)
- [map_range](shade-stati-staticclass.md#map_range)
- [material_output](shade-stati-staticclass.md#material_output)
- [math](shade-stati-staticclass.md#math)
- [mix](shade-stati-staticclass.md#mix)
- [mix_shader](shade-stati-staticclass.md#mix_shader)
- [noise_texture](shade-stati-staticclass.md#noise_texture)
- [normal](shade-stati-staticclass.md#normal)
- [normal_map](shade-stati-staticclass.md#normal_map)
- [point_density](shade-stati-staticclass.md#point_density)
- [principled_bsdf](shade-stati-staticclass.md#principled_bsdf)
- [principled_hair_bsdf](shade-stati-staticclass.md#principled_hair_bsdf)
- [principled_volume](shade-stati-staticclass.md#principled_volume)
- [ray_portal_bsdf](shade-stati-staticclass.md#ray_portal_bsdf)
- [refraction_bsdf](shade-stati-staticclass.md#refraction_bsdf)
- [reroute](shade-stati-staticclass.md#reroute)
- [rgb_curves](shade-stati-staticclass.md#rgb_curves)
- [rgb_to_bw](shade-stati-staticclass.md#rgb_to_bw)
- [script](shade-stati-staticclass.md#script)
- [separate_color](shade-stati-staticclass.md#separate_color)
- [separate_xyz](shade-stati-staticclass.md#separate_xyz)
- [shader_to_rgb](shade-stati-staticclass.md#shader_to_rgb)
- [sheen_bsdf](shade-stati-staticclass.md#sheen_bsdf)
- [sky_texture](shade-stati-staticclass.md#sky_texture)
- [specular_bsdf](shade-stati-staticclass.md#specular_bsdf)
- [subsurface_scattering](shade-stati-staticclass.md#subsurface_scattering)
- [tangent](shade-stati-staticclass.md#tangent)
- [texture_coordinate](shade-stati-staticclass.md#texture_coordinate)
- [toon_bsdf](shade-stati-staticclass.md#toon_bsdf)
- [translucent_bsdf](shade-stati-staticclass.md#translucent_bsdf)
- [transparent_bsdf](shade-stati-staticclass.md#transparent_bsdf)
- [uv_along_stroke](shade-stati-staticclass.md#uv_along_stroke)
- [uv_map](shade-stati-staticclass.md#uv_map)
- [vector_curves](shade-stati-staticclass.md#vector_curves)
- [vector_displacement](shade-stati-staticclass.md#vector_displacement)
- [vector_math](shade-stati-staticclass.md#vector_math)
- [vector_rotate](shade-stati-staticclass.md#vector_rotate)
- [vector_transform](shade-stati-staticclass.md#vector_transform)
- [volume_absorption](shade-stati-staticclass.md#volume_absorption)
- [volume_scatter](shade-stati-staticclass.md#volume_scatter)
- [voronoi_texture](shade-stati-staticclass.md#voronoi_texture)
- [wavelength](shade-stati-staticclass.md#wavelength)
- [wave_texture](shade-stati-staticclass.md#wave_texture)
- [white_noise_texture](shade-stati-staticclass.md#white_noise_texture)
- [wireframe](shade-stati-staticclass.md#wireframe)
- [world_output](shade-stati-staticclass.md#world_output)

## Classes



- [StaticClass](shade-stati-staticclass.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#staticclass) :black_small_square: [Content](#content) :black_small_square: [staticclass](shade-stati---staticclass.md)</sub>