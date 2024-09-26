# Shader

> Bases classes: [ValueSocket](geono-socke-valuesocket.md#valuesocket)

``` python
Shader(socket)
```



#### Arguments:
- **socket**

### Inherited

[blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square:

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

Node 'Diffuse BSDF' (ShaderNodeBsdfDiffuse)

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

Node 'Emission' (ShaderNodeEmission)

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

Node 'Glass BSDF' (ShaderNodeBsdfGlass)
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

Node 'Glossy BSDF' (ShaderNodeBsdfAnisotropic)
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

Node 'Holdout' (ShaderNodeHoldout)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, thin_film_thickness=None, thin_film_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK')
```

Node 'Principled BSDF' (ShaderNodeBsdfPrincipled)
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

Node 'Refraction BSDF' (ShaderNodeBsdfRefraction)
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

Node 'Specular BSDF' (ShaderNodeEeveeSpecular)

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

Node 'Subsurface Scattering' (ShaderNodeSubsurfaceScattering)
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

Node 'Translucent BSDF' (ShaderNodeBsdfTranslucent)

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

Node 'Transparent BSDF' (ShaderNodeBsdfTransparent)

#### Arguments:
- **color** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shade-shade-shader.md#shader) :black_small_square: [Content](shade-shade-shader.md#content) :black_small_square: [Methods](shade-shade-shader.md#methods)</sub>