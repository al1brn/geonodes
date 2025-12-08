# Shader

``` python
Shader(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False)
```

Socket of type Shader

A group input socket of type Shader.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier

### Inherited

[\_\_add__](shaderroot.md#__add__) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_classes_test](core-socke-socket.md#_classes_test) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_from](core-socke-socket.md#link_from) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_\_mul__](shaderroot.md#__mul__) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: ['_socket_type' not found]() :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [surface_out](shaderroot.md#surface_out) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [volume_out](shaderroot.md#volume_out) :black_small_square:

## Content

- **A** : [add](shader.md#add)
- **C** : [\_create_input_socket](shader.md#_create_input_socket)
- **D** : [Diffuse](shader.md#diffuse)
- **E** : [Emission](shader.md#emission)
- **G** : [Glass](shader.md#glass) :black_small_square: [Glossy](shader.md#glossy)
- **H** : [Hair](shader.md#hair) :black_small_square: [Holdout](shader.md#holdout)
- **I** : [\_\_init__](shader.md#__init__)
- **L** : [light_output](shader.md#light_output)
- **M** : [material_output](shader.md#material_output) :black_small_square: [Metallic](shader.md#metallic) :black_small_square: [mix](shader.md#mix)
- **O** : [out](shader.md#out)
- **P** : [Principled](shader.md#principled) :black_small_square: [PrincipledHair](shader.md#principledhair)
- **R** : [RayPortal](shader.md#rayportal) :black_small_square: [Refraction](shader.md#refraction)
- **S** : [Sheen](shader.md#sheen) :black_small_square: [Specular](shader.md#specular) :black_small_square: [SubsurfaceScattering](shader.md#subsurfacescattering)
- **T** : [Toon](shader.md#toon) :black_small_square: [to_rgb](shader.md#to_rgb) :black_small_square: [Translucent](shader.md#translucent) :black_small_square: [Transparent](shader.md#transparent)
- **W** : [world_output](shader.md#world_output)

## Methods



----------
### add()

> method

``` python
add(shader: 'Shader' = None)
```

> Node ERROR: Node 'Add Shader' not found

#### Information:
- **Socket** : self



#### Arguments:
- **shader** (_Shader_ = None) : socket 'Shader' (id: Shader_001)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Shader', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Shader Input

New [Shader](shader.md#shader) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Shader') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **name** (_str_ = Shader)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Diffuse()

> classmethod

``` python
Diffuse(color: 'Color' = None, roughness: 'Float' = None, normal: 'Vector' = None)
```

> Node ERROR: Node 'Diffuse BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Emission()

> classmethod

``` python
Emission(color: 'Color' = None, strength: 'Float' = None)
```

> Node ERROR: Node 'Emission' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Glass()

> classmethod

``` python
Glass(color: 'Color' = None, roughness: 'Float' = None, ior: 'Float' = None, normal: 'Vector' = None, thin_film_thickness: 'Float' = None, thin_film_ior: 'Float' = None, distribution: "Literal['BECKMANN', 'GGX', 'MULTI_GGX']" = 'MULTI_GGX')
```

> Node ERROR: Node 'Glass BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **thin_film_thickness** (_Float_ = None) : socket 'Thin Film Thickness' (id: Thin Film Thickness)
- **thin_film_ior** (_Float_ = None) : socket 'Thin Film IOR' (id: Thin Film IOR)
- **distribution** (_Literal['BECKMANN', 'GGX', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ['BECKMANN', 'GGX', 'MULTI_GGX']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Glossy()

> classmethod

``` python
Glossy(color: 'Color' = None, roughness: 'Float' = None, anisotropy: 'Float' = None, rotation: 'Float' = None, normal: 'Vector' = None, tangent: 'Vector' = None, distribution: "Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX']" = 'MULTI_GGX')
```

> Node ERROR: Node 'Glossy BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **rotation** (_Float_ = None) : socket 'Rotation' (id: Rotation)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **tangent** (_Vector_ = None) : socket 'Tangent' (id: Tangent)
- **distribution** (_Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Hair()

> classmethod

``` python
Hair(color: 'Color' = None, offset: 'Float' = None, roughnessu: 'Float' = None, roughnessv: 'Float' = None, tangent: 'Vector' = None, component: "Literal['Reflection', 'Transmission']" = 'Reflection')
```

> Node ERROR: Node 'Hair BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **offset** (_Float_ = None) : socket 'Offset' (id: Offset)
- **roughnessu** (_Float_ = None) : socket 'RoughnessU' (id: RoughnessU)
- **roughnessv** (_Float_ = None) : socket 'RoughnessV' (id: RoughnessV)
- **tangent** (_Vector_ = None) : socket 'Tangent' (id: Tangent)
- **component** (_Literal['Reflection', 'Transmission']_ = Reflection) : parameter 'component' in ['Reflection', 'Transmission']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Holdout()

> classmethod

``` python
Holdout()
```

> Node ERROR: Node 'Holdout' not found

#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False)
```

Socket of type Shader

A group input socket of type Shader.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### light_output()

> method

``` python
light_output(is_active_output=True, target: "Literal['ALL', 'EEVEE', 'CYCLES']" = 'ALL')
```

> Node [Light Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/light.html)

#### Information:
- **Socket** : self



#### Arguments:
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_Literal['ALL', 'EEVEE', 'CYCLES']_ = ALL) : parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### material_output()

> method

``` python
material_output(volume: 'VolumeShader' = None, displacement: 'Vector' = None, thickness: 'Float' = None, is_active_output=True, target: "Literal['ALL', 'EEVEE', 'CYCLES']" = 'ALL')
```

> Node [Material Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/material.html)

#### Information:
- **Socket** : self



#### Arguments:
- **volume** (_VolumeShader_ = None) : socket 'Volume' (id: Volume)
- **displacement** (_Vector_ = None) : socket 'Displacement' (id: Displacement)
- **thickness** (_Float_ = None) : socket 'Thickness' (id: Thickness)
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_Literal['ALL', 'EEVEE', 'CYCLES']_ = ALL) : parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Metallic()

> classmethod

``` python
Metallic(base_color: 'Color' = None, edge_tint: 'Color' = None, roughness: 'Float' = None, anisotropy: 'Float' = None, rotation: 'Float' = None, normal: 'Vector' = None, tangent: 'Vector' = None, thin_film_thickness: 'Float' = None, thin_film_ior: 'Float' = None, distribution: "Literal['BECKMANN', 'GGX', 'MULTI_GGX']" = 'MULTI_GGX', fresnel_type: "Literal['PHYSICAL_CONDUCTOR', 'F82']" = 'F82')
```

> Node ERROR: Node 'Metallic BSDF' not found

#### Arguments:
- **base_color** (_Color_ = None) : socket 'Base Color' (id: Base Color)
- **edge_tint** (_Color_ = None) : socket 'Edge Tint' (id: Edge Tint)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **rotation** (_Float_ = None) : socket 'Rotation' (id: Rotation)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **tangent** (_Vector_ = None) : socket 'Tangent' (id: Tangent)
- **thin_film_thickness** (_Float_ = None) : socket 'Thin Film Thickness' (id: Thin Film Thickness)
- **thin_film_ior** (_Float_ = None) : socket 'Thin Film IOR' (id: Thin Film IOR)
- **distribution** (_Literal['BECKMANN', 'GGX', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ['BECKMANN', 'GGX', 'MULTI_GGX']
- **fresnel_type** (_Literal['PHYSICAL_CONDUCTOR', 'F82']_ = F82) : parameter 'fresnel_type' in ['PHYSICAL_CONDUCTOR', 'F82']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### mix()

> method

``` python
mix(shader: 'Shader' = None, factor: 'Float' = None)
```

> Node ERROR: Node 'Mix Shader' not found

#### Information:
- **Socket** : self



#### Arguments:
- **shader** (_Shader_ = None) : socket 'Shader' (id: Shader_001)
- **factor** (_Float_ = None) : socket 'Factor' (id: Fac)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### out()

> method

``` python
out(name=None, panel='')
```

Shader output

#### Arguments:
- **name** ( = None)
- **panel** ( = )

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(base_color: 'Color' = None, metallic: 'Float' = None, roughness: 'Float' = None, ior: 'Float' = None, alpha: 'Float' = None, normal: 'Vector' = None, diffuse_roughness: 'Float' = None, subsurface_weight: 'Float' = None, subsurface_radius: 'Vector' = None, subsurface_scale: 'Float' = None, subsurface_anisotropy: 'Float' = None, specular_ior_level: 'Float' = None, specular_tint: 'Color' = None, anisotropic: 'Float' = None, anisotropic_rotation: 'Float' = None, tangent: 'Vector' = None, transmission_weight: 'Float' = None, coat_weight: 'Float' = None, coat_roughness: 'Float' = None, coat_ior: 'Float' = None, coat_tint: 'Color' = None, coat_normal: 'Vector' = None, sheen_weight: 'Float' = None, sheen_roughness: 'Float' = None, sheen_tint: 'Color' = None, emission_color: 'Color' = None, emission_strength: 'Float' = None, thin_film_thickness: 'Float' = None, thin_film_ior: 'Float' = None, distribution: "Literal['GGX', 'MULTI_GGX']" = 'MULTI_GGX', subsurface_method: "Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']" = 'RANDOM_WALK')
```

> Node ERROR: Node 'Principled BSDF' not found

#### Arguments:
- **base_color** (_Color_ = None) : socket 'Base Color' (id: Base Color)
- **metallic** (_Float_ = None) : socket 'Metallic' (id: Metallic)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **alpha** (_Float_ = None) : socket 'Alpha' (id: Alpha)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **diffuse_roughness** (_Float_ = None) : socket 'Diffuse Roughness' (id: Diffuse Roughness)
- **subsurface_weight** (_Float_ = None) : socket 'Subsurface Weight' (id: Subsurface Weight)
- **subsurface_radius** (_Vector_ = None) : socket 'Subsurface Radius' (id: Subsurface Radius)
- **subsurface_scale** (_Float_ = None) : socket 'Subsurface Scale' (id: Subsurface Scale)
- **subsurface_anisotropy** (_Float_ = None) : socket 'Subsurface Anisotropy' (id: Subsurface Anisotropy)
- **specular_ior_level** (_Float_ = None) : socket 'Specular IOR Level' (id: Specular IOR Level)
- **specular_tint** (_Color_ = None) : socket 'Specular Tint' (id: Specular Tint)
- **anisotropic** (_Float_ = None) : socket 'Anisotropic' (id: Anisotropic)
- **anisotropic_rotation** (_Float_ = None) : socket 'Anisotropic Rotation' (id: Anisotropic Rotation)
- **tangent** (_Vector_ = None) : socket 'Tangent' (id: Tangent)
- **transmission_weight** (_Float_ = None) : socket 'Transmission Weight' (id: Transmission Weight)
- **coat_weight** (_Float_ = None) : socket 'Coat Weight' (id: Coat Weight)
- **coat_roughness** (_Float_ = None) : socket 'Coat Roughness' (id: Coat Roughness)
- **coat_ior** (_Float_ = None) : socket 'Coat IOR' (id: Coat IOR)
- **coat_tint** (_Color_ = None) : socket 'Coat Tint' (id: Coat Tint)
- **coat_normal** (_Vector_ = None) : socket 'Coat Normal' (id: Coat Normal)
- **sheen_weight** (_Float_ = None) : socket 'Sheen Weight' (id: Sheen Weight)
- **sheen_roughness** (_Float_ = None) : socket 'Sheen Roughness' (id: Sheen Roughness)
- **sheen_tint** (_Color_ = None) : socket 'Sheen Tint' (id: Sheen Tint)
- **emission_color** (_Color_ = None) : socket 'Emission Color' (id: Emission Color)
- **emission_strength** (_Float_ = None) : socket 'Emission Strength' (id: Emission Strength)
- **thin_film_thickness** (_Float_ = None) : socket 'Thin Film Thickness' (id: Thin Film Thickness)
- **thin_film_ior** (_Float_ = None) : socket 'Thin Film IOR' (id: Thin Film IOR)
- **distribution** (_Literal['GGX', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ['GGX', 'MULTI_GGX']
- **subsurface_method** (_Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']_ = RANDOM_WALK) : parameter 'subsurface_method' in ['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### PrincipledHair()

> classmethod

``` python
PrincipledHair(color: 'Color' = None, roughness: 'Float' = None, radial_roughness: 'Float' = None, coat: 'Float' = None, ior: 'Float' = None, offset: 'Float' = None, random_roughness: 'Float' = None, random: 'Float' = None, model: "Literal['CHIANG', 'HUANG']" = 'CHIANG', parametrization: "Literal['ABSORPTION', 'MELANIN', 'COLOR']" = 'COLOR')
```

> Node ERROR: Node 'Principled Hair BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **radial_roughness** (_Float_ = None) : socket 'Radial Roughness' (id: Radial Roughness)
- **coat** (_Float_ = None) : socket 'Coat' (id: Coat)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **offset** (_Float_ = None) : socket 'Offset' (id: Offset)
- **random_roughness** (_Float_ = None) : socket 'Random Roughness' (id: Random Roughness)
- **random** (_Float_ = None) : socket 'Random' (id: Random)
- **model** (_Literal['CHIANG', 'HUANG']_ = CHIANG) : parameter 'model' in ['CHIANG', 'HUANG']
- **parametrization** (_Literal['ABSORPTION', 'MELANIN', 'COLOR']_ = COLOR) : parameter 'parametrization' in ['ABSORPTION', 'MELANIN', 'COLOR']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### RayPortal()

> classmethod

``` python
RayPortal(color: 'Color' = None, position: 'Vector' = None, direction: 'Vector' = None)
```

> Node ERROR: Node 'Ray Portal BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Refraction()

> classmethod

``` python
Refraction(color: 'Color' = None, roughness: 'Float' = None, ior: 'Float' = None, normal: 'Vector' = None, distribution: "Literal['BECKMANN', 'GGX']" = 'BECKMANN')
```

> Node ERROR: Node 'Refraction BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **distribution** (_Literal['BECKMANN', 'GGX']_ = BECKMANN) : parameter 'distribution' in ['BECKMANN', 'GGX']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Sheen()

> classmethod

``` python
Sheen(color: 'Color' = None, roughness: 'Float' = None, normal: 'Vector' = None, distribution: "Literal['ASHIKHMIN', 'MICROFIBER']" = 'MICROFIBER')
```

> Node ERROR: Node 'Sheen BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **distribution** (_Literal['ASHIKHMIN', 'MICROFIBER']_ = MICROFIBER) : parameter 'distribution' in ['ASHIKHMIN', 'MICROFIBER']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Specular()

> classmethod

``` python
Specular(base_color: 'Color' = None, specular: 'Color' = None, roughness: 'Float' = None, emissive_color: 'Color' = None, transparency: 'Float' = None, normal: 'Vector' = None, clear_coat: 'Float' = None, clear_coat_roughness: 'Float' = None, clear_coat_normal: 'Vector' = None)
```

> Node ERROR: Node 'Specular BSDF' not found

#### Arguments:
- **base_color** (_Color_ = None) : socket 'Base Color' (id: Base Color)
- **specular** (_Color_ = None) : socket 'Specular' (id: Specular)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **emissive_color** (_Color_ = None) : socket 'Emissive Color' (id: Emissive Color)
- **transparency** (_Float_ = None) : socket 'Transparency' (id: Transparency)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **clear_coat** (_Float_ = None) : socket 'Clear Coat' (id: Clear Coat)
- **clear_coat_roughness** (_Float_ = None) : socket 'Clear Coat Roughness' (id: Clear Coat Roughness)
- **clear_coat_normal** (_Vector_ = None) : socket 'Clear Coat Normal' (id: Clear Coat Normal)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### SubsurfaceScattering()

> classmethod

``` python
SubsurfaceScattering(color: 'Color' = None, scale: 'Float' = None, radius: 'Vector' = None, ior: 'Float' = None, roughness: 'Float' = None, anisotropy: 'Float' = None, normal: 'Vector' = None, falloff: "Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']" = 'RANDOM_WALK')
```

> Node ERROR: Node 'Subsurface Scattering' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **radius** (_Vector_ = None) : socket 'Radius' (id: Radius)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **falloff** (_Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']_ = RANDOM_WALK) : parameter 'falloff' in ['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Toon()

> classmethod

``` python
Toon(color: 'Color' = None, size: 'Float' = None, smooth: 'Float' = None, normal: 'Vector' = None, component: "Literal['DIFFUSE', 'GLOSSY']" = 'DIFFUSE')
```

> Node ERROR: Node 'Toon BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **size** (_Float_ = None) : socket 'Size' (id: Size)
- **smooth** (_Float_ = None) : socket 'Smooth' (id: Smooth)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **component** (_Literal['DIFFUSE', 'GLOSSY']_ = DIFFUSE) : parameter 'component' in ['DIFFUSE', 'GLOSSY']



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### to_rgb()

> method

``` python
to_rgb()
```

> Node [Shader to RGB](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/shader_to_rgb.html)

#### Information:
- **Socket** : self



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Translucent()

> classmethod

``` python
Translucent(color: 'Color' = None, normal: 'Vector' = None)
```

> Node ERROR: Node 'Translucent BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Transparent()

> classmethod

``` python
Transparent(color: 'Color' = None)
```

> Node ERROR: Node 'Transparent BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### world_output()

> method

``` python
world_output(volume: 'VolumeShader' = None, is_active_output=True, target: "Literal['ALL', 'EEVEE', 'CYCLES']" = 'ALL')
```

> Node [World Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/world.html)

#### Information:
- **Socket** : self



#### Arguments:
- **volume** (_VolumeShader_ = None) : socket 'Volume' (id: Volume)
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_Literal['ALL', 'EEVEE', 'CYCLES']_ = ALL) : parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>