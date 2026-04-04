# Shader

``` python
Shader(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](core-gener-float-float.md#float), [Image](core-gener-image-image.md#image) or [Geometry](core-gener-geome-geometry.md#geometry).

It refers to an **output** socket of a [Node](node.md#node). A socket can be set to the **input** socket
of another [Node](node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

!!! important
> You can access to the other output sockets of the node in two different ways:
> - using [node](core-socket.md#node) attribute
> - using ***peer socket** naming convention where the **snake_case** name of
>.  the other sockets is suffixed by '_'

The example below shows how to access the to 'UV Map' socket of node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html):

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Mesh.Cube()

# Getting 'UV Map' through the node
uv_map = cube.node.uv_map

# Or using the 'peer socket' naming convention
uv_map = cuve.uv_map_
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None) : input name if not None
- **tip** (_str_ = ) : description
- **panel** (_str_ = ) : panel name
- **user_label** (_str_ = None) : user label
- **props**

### Inherited

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](core-gener-boole-boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- **A** : [add](core-gener-shade-shader.md#add)
- **C** : [\_create_input_socket](core-gener-shade-shader.md#_create_input_socket)
- **D** : [Diffuse](core-gener-shade-shader.md#diffuse)
- **E** : [Emission](core-gener-shade-shader.md#emission)
- **G** : [Glass](core-gener-shade-shader.md#glass) :black_small_square: [Glossy](core-gener-shade-shader.md#glossy)
- **H** : [Hair](core-gener-shade-shader.md#hair) :black_small_square: [Holdout](core-gener-shade-shader.md#holdout)
- **L** : [light_output](core-gener-shade-shader.md#light_output)
- **M** : [material_output](core-gener-shade-shader.md#material_output) :black_small_square: [Metallic](core-gener-shade-shader.md#metallic) :black_small_square: [mix](core-gener-shade-shader.md#mix)
- **P** : [Principled](core-gener-shade-shader.md#principled) :black_small_square: [PrincipledHair](core-gener-shade-shader.md#principledhair)
- **R** : [RayPortal](core-gener-shade-shader.md#rayportal) :black_small_square: [Refraction](core-gener-shade-shader.md#refraction)
- **S** : [Sheen](core-gener-shade-shader.md#sheen) :black_small_square: [Specular](core-gener-shade-shader.md#specular) :black_small_square: [SubsurfaceScattering](core-gener-shade-shader.md#subsurfacescattering)
- **T** : [Toon](core-gener-shade-shader.md#toon) :black_small_square: [to_rgb](core-gener-shade-shader.md#to_rgb) :black_small_square: [Translucent](core-gener-shade-shader.md#translucent) :black_small_square: [Transparent](core-gener-shade-shader.md#transparent)
- **W** : [world_output](core-gener-shade-shader.md#world_output)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Shader', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Shader Input

New [Shader](core-gener-shade-shader.md#shader) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Shader') : Input socket name
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **distribution** (_Literal['BECKMANN', 'GGX', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ('Beckmann', 'GGX', 'Multiscatter GGX')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **distribution** (_Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ('Beckmann', 'GGX', 'Ashikhmin-Shirley', 'Multiscatter GGX')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **component** (_Literal['Reflection', 'Transmission']_ = Reflection) : parameter 'component' in ('Reflection', 'Transmission')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

----------
### Holdout()

> classmethod

``` python
Holdout()
```

> Node ERROR: Node 'Holdout' not found

#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **target** (_Literal['ALL', 'EEVEE', 'CYCLES']_ = ALL) : parameter 'target' in ('All', 'EEVEE', 'Cycles')



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **target** (_Literal['ALL', 'EEVEE', 'CYCLES']_ = ALL) : parameter 'target' in ('All', 'EEVEE', 'Cycles')



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **distribution** (_Literal['BECKMANN', 'GGX', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ('Beckmann', 'GGX', 'Multiscatter GGX')
- **fresnel_type** (_Literal['PHYSICAL_CONDUCTOR', 'F82']_ = F82) : parameter 'fresnel_type' in ('Physical Conductor', 'F82 Tint')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **distribution** (_Literal['GGX', 'MULTI_GGX']_ = MULTI_GGX) : parameter 'distribution' in ('GGX', 'Multiscatter GGX')
- **subsurface_method** (_Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']_ = RANDOM_WALK) : parameter 'subsurface_method' in ('Christensen-Burley', 'Random Walk', 'Random Walk (Skin)')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **model** (_Literal['CHIANG', 'HUANG']_ = CHIANG) : parameter 'model' in ('Chiang', 'Huang')
- **parametrization** (_Literal['ABSORPTION', 'MELANIN', 'COLOR']_ = COLOR) : parameter 'parametrization' in ('Absorption Coefficient', 'Melanin Concentration', 'Direct Coloring')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **distribution** (_Literal['BECKMANN', 'GGX']_ = BECKMANN) : parameter 'distribution' in ('Beckmann', 'GGX')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **distribution** (_Literal['ASHIKHMIN', 'MICROFIBER']_ = MICROFIBER) : parameter 'distribution' in ('Ashikhmin', 'Microfiber')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **falloff** (_Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']_ = RANDOM_WALK) : parameter 'falloff' in ('Christensen-Burley', 'Random Walk', 'Random Walk (Skin)')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **component** (_Literal['DIFFUSE', 'GLOSSY']_ = DIFFUSE) : parameter 'component' in ('Diffuse', 'Glossy')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>

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
- **target** (_Literal['ALL', 'EEVEE', 'CYCLES']_ = ALL) : parameter 'target' in ('All', 'EEVEE', 'Cycles')



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](core-gener-shade-shader.md#shader) :black_small_square: [Content](core-gener-shade-shader.md#content) :black_small_square: [Methods](core-gener-shade-shader.md#methods)</sub>