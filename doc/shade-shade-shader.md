# Shader

> Bases classes: [ValueSocket](geono-socke-valuesocket.md#valuesocket)

``` python
Shader(socket)
```



#### Arguments:
- **socket**

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- **D** : [Diffuse](shade-shade-shader.md#diffuse)
- **E** : [Emission](shade-shade-shader.md#emission)
- **G** : [Glass](shade-shade-shader.md#glass) :black_small_square: [Glossy](shade-shade-shader.md#glossy)
- **H** : [Holdout](shade-shade-shader.md#holdout)
- **P** : [Principled](shade-shade-shader.md#principled)
- **R** : [Refraction](shade-shade-shader.md#refraction)
- **S** : [Specular](shade-shade-shader.md#specular) :black_small_square: [SubsurfaceScattering](shade-shade-shader.md#subsurfacescattering)
- **T** : [Translucent](shade-shade-shader.md#translucent) :black_small_square: [Transparent](shade-shade-shader.md#transparent)

## Methods



----------
### Diffuse()

> classmethod

``` python
Diffuse(color=None, roughness=None, normal=None)
```

> **node** : ERROR: Node 'Diffuse BSDF' not found

#### Arguments:
- **color** ( = None)
- **roughness** ( = None)
- **normal** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Emission()

> classmethod

``` python
Emission(color=None, strength=None)
```

> **node** : ERROR: Node 'Emission' not found

#### Arguments:
- **color** ( = None)
- **strength** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Glass()

> classmethod

``` python
Glass(color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX')
```

> **node** : ERROR: Node 'Glass BSDF' not found
- distribution in ('BECKMANN', 'GGX', 'MULTI_GGX')

#### Arguments:
- **color** ( = None)
- **roughness** ( = None)
- **ior** ( = None)
- **normal** ( = None)
- **distribution** ( = MULTI_GGX)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Glossy()

> classmethod

``` python
Glossy(color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX')
```

> **node** : ERROR: Node 'Glossy BSDF' not found
- distribution in ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX')

#### Arguments:
- **color** ( = None)
- **roughness** ( = None)
- **anisotropy** ( = None)
- **rotation** ( = None)
- **normal** ( = None)
- **tangent** ( = None)
- **distribution** ( = MULTI_GGX)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Holdout()

> classmethod

``` python
Holdout()
```

> **node** : ERROR: Node 'Holdout' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, thin_film_thickness=None, thin_film_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK')
```

> **node** : ERROR: Node 'Principled BSDF' not found
- distribution in ('GGX', 'MULTI_GGX')
- subsurface_method in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')

#### Arguments:
- **base_color** ( = None)
- **metallic** ( = None)
- **roughness** ( = None)
- **ior** ( = None)
- **alpha** ( = None)
- **normal** ( = None)
- **subsurface_weight** ( = None)
- **subsurface_radius** ( = None)
- **subsurface_scale** ( = None)
- **subsurface_anisotropy** ( = None)
- **specular_ior_level** ( = None)
- **specular_tint** ( = None)
- **anisotropic** ( = None)
- **anisotropic_rotation** ( = None)
- **tangent** ( = None)
- **transmission_weight** ( = None)
- **coat_weight** ( = None)
- **coat_roughness** ( = None)
- **coat_ior** ( = None)
- **coat_tint** ( = None)
- **coat_normal** ( = None)
- **sheen_weight** ( = None)
- **sheen_roughness** ( = None)
- **sheen_tint** ( = None)
- **emission_color** ( = None)
- **emission_strength** ( = None)
- **thin_film_thickness** ( = None)
- **thin_film_ior** ( = None)
- **distribution** ( = MULTI_GGX)
- **subsurface_method** ( = RANDOM_WALK)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Refraction()

> classmethod

``` python
Refraction(color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN')
```

> **node** : ERROR: Node 'Refraction BSDF' not found
- distribution in ('BECKMANN', 'GGX')

#### Arguments:
- **color** ( = None)
- **roughness** ( = None)
- **ior** ( = None)
- **normal** ( = None)
- **distribution** ( = BECKMANN)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Specular()

> classmethod

``` python
Specular(base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None)
```

> **node** : ERROR: Node 'Specular BSDF' not found

#### Arguments:
- **base_color** ( = None)
- **specular** ( = None)
- **roughness** ( = None)
- **emissive_color** ( = None)
- **transparency** ( = None)
- **normal** ( = None)
- **clear_coat** ( = None)
- **clear_coat_roughness** ( = None)
- **clear_coat_normal** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### SubsurfaceScattering()

> classmethod

``` python
SubsurfaceScattering(color=None, scale=None, radius=None, ior=None, roughness=None, anisotropy=None, normal=None, falloff='RANDOM_WALK')
```

> **node** : ERROR: Node 'Subsurface Scattering' not found
- falloff in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')

#### Arguments:
- **color** ( = None)
- **scale** ( = None)
- **radius** ( = None)
- **ior** ( = None)
- **roughness** ( = None)
- **anisotropy** ( = None)
- **normal** ( = None)
- **falloff** ( = RANDOM_WALK)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Translucent()

> classmethod

``` python
Translucent(color=None, normal=None)
```

> **node** : ERROR: Node 'Translucent BSDF' not found

#### Arguments:
- **color** ( = None)
- **normal** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Transparent()

> classmethod

``` python
Transparent(color=None)
```

> **node** : ERROR: Node 'Transparent BSDF' not found

#### Arguments:
- **color** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>