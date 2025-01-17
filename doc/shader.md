# Shader

``` python
Shader(socket)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](float.md#float), [Image](image.md#image) or [Geometry](geometry.md#geometry).

It refers to an **output** socket of a [Node](node.md#node). A socket can be set to the **input** socket
of another [Node](node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

> [!IMPORTANT]
> You can access to the other output sockets of the node in two different ways:
> - using [node](socket.md#node) attribute
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
- **socket** (_NodeSocket_) : the output socket to wrap

### Inherited

[\_\_add__](shaderroot.md#__add__) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](socket.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_\_mul__](shaderroot.md#__mul__) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [surface_out](shaderroot.md#surface_out) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [volume_out](shaderroot.md#volume_out) :black_small_square:

## Content

- **A** : [add](shader.md#add)
- **D** : [Diffuse](shader.md#diffuse)
- **E** : [Emission](shader.md#emission)
- **G** : [Glass](shader.md#glass) :black_small_square: [Glossy](shader.md#glossy)
- **H** : [Hair](shader.md#hair) :black_small_square: [Holdout](shader.md#holdout)
- **L** : [light_output](shader.md#light_output)
- **M** : [material_output](shader.md#material_output) :black_small_square: [Metallic](shader.md#metallic) :black_small_square: [mix](shader.md#mix)
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
add(shader=None)
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
### Diffuse()

> classmethod

``` python
Diffuse(color=None, roughness=None, normal=None)
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
Emission(color=None, strength=None)
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
Glass(color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX')
```

> Node ERROR: Node 'Glass BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **distribution** (_str_ = MULTI_GGX) : parameter 'distribution' in ('BECKMANN', 'GGX', 'MULTI_GGX')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Glossy()

> classmethod

``` python
Glossy(color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX')
```

> Node ERROR: Node 'Glossy BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **rotation** (_Float_ = None) : socket 'Rotation' (id: Rotation)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **tangent** (_Vector_ = None) : socket 'Tangent' (id: Tangent)
- **distribution** (_str_ = MULTI_GGX) : parameter 'distribution' in ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Hair()

> classmethod

``` python
Hair(color=None, offset=None, roughnessu=None, roughnessv=None, tangent=None, component='Reflection')
```

> Node ERROR: Node 'Hair BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **offset** (_Float_ = None) : socket 'Offset' (id: Offset)
- **roughnessu** (_Float_ = None) : socket 'RoughnessU' (id: RoughnessU)
- **roughnessv** (_Float_ = None) : socket 'RoughnessV' (id: RoughnessV)
- **tangent** (_Vector_ = None) : socket 'Tangent' (id: Tangent)
- **component** (_str_ = Reflection) : parameter 'component' in ('Reflection', 'Transmission')



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
### light_output()

> method

``` python
light_output(is_active_output=True, target='ALL')
```

> Node [Light Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/light.html)

#### Information:
- **Socket** : self



#### Arguments:
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_str_ = ALL) : parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### material_output()

> method

``` python
material_output(volume=None, displacement=None, thickness=None, is_active_output=True, target='ALL')
```

> Node [Material Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/material.html)

#### Information:
- **Socket** : self



#### Arguments:
- **volume** (_Shader_ = None) : socket 'Volume' (id: Volume)
- **displacement** (_Vector_ = None) : socket 'Displacement' (id: Displacement)
- **thickness** (_Float_ = None) : socket 'Thickness' (id: Thickness)
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_str_ = ALL) : parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Metallic()

> classmethod

``` python
Metallic(base_color=None, edge_tint=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX', fresnel_type='F82')
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
- **distribution** (_str_ = MULTI_GGX) : parameter 'distribution' in ('BECKMANN', 'GGX', 'MULTI_GGX')
- **fresnel_type** (_str_ = F82) : parameter 'fresnel_type' in ('PHYSICAL_CONDUCTOR', 'F82')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### mix()

> method

``` python
mix(shader=None, fac=None)
```

> Node ERROR: Node 'Mix Shader' not found

#### Information:
- **Socket** : self



#### Arguments:
- **shader** (_Shader_ = None) : socket 'Shader' (id: Shader_001)
- **fac** (_Float_ = None) : socket 'Fac' (id: Fac)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, diffuse_roughness=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, thin_film_thickness=None, thin_film_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK')
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
- **distribution** (_str_ = MULTI_GGX) : parameter 'distribution' in ('GGX', 'MULTI_GGX')
- **subsurface_method** (_str_ = RANDOM_WALK) : parameter 'subsurface_method' in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### PrincipledHair()

> classmethod

``` python
PrincipledHair(color=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_roughness=None, random=None, model='CHIANG', parametrization='COLOR')
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
- **model** (_str_ = CHIANG) : parameter 'model' in ('CHIANG', 'HUANG')
- **parametrization** (_str_ = COLOR) : parameter 'parametrization' in ('ABSORPTION', 'MELANIN', 'COLOR')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### RayPortal()

> classmethod

``` python
RayPortal(color=None, position=None, direction=None)
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
Refraction(color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN')
```

> Node ERROR: Node 'Refraction BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **ior** (_Float_ = None) : socket 'IOR' (id: IOR)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **distribution** (_str_ = BECKMANN) : parameter 'distribution' in ('BECKMANN', 'GGX')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Sheen()

> classmethod

``` python
Sheen(color=None, roughness=None, normal=None, distribution='MICROFIBER')
```

> Node ERROR: Node 'Sheen BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **distribution** (_str_ = MICROFIBER) : parameter 'distribution' in ('ASHIKHMIN', 'MICROFIBER')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Specular()

> classmethod

``` python
Specular(base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None)
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
SubsurfaceScattering(color=None, scale=None, radius=None, ior=None, roughness=None, anisotropy=None, normal=None, falloff='RANDOM_WALK')
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
- **falloff** (_str_ = RANDOM_WALK) : parameter 'falloff' in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Toon()

> classmethod

``` python
Toon(color=None, size=None, smooth=None, normal=None, component='DIFFUSE')
```

> Node ERROR: Node 'Toon BSDF' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **size** (_Float_ = None) : socket 'Size' (id: Size)
- **smooth** (_Float_ = None) : socket 'Smooth' (id: Smooth)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **component** (_str_ = DIFFUSE) : parameter 'component' in ('DIFFUSE', 'GLOSSY')



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### to_rgb()

> method

``` python
to_rgb()
```

> Node ERROR: Node 'Shader to RGB' not found

#### Information:
- **Socket** : self



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Translucent()

> classmethod

``` python
Translucent(color=None, normal=None)
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
Transparent(color=None)
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
world_output(volume=None, is_active_output=True, target='ALL')
```

> Node [World Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/world.html)

#### Information:
- **Socket** : self



#### Arguments:
- **volume** (_Shader_ = None) : socket 'Volume' (id: Volume)
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_str_ = ALL) : parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>