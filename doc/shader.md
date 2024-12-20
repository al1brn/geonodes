# Shader

> Bases classes: [Attribute](attribute.md#attribute)

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

#### Arguments:
- **socket** (_NodeSocket_) : the output socket to wrap

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](socket.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [Named](attribute.md#named) :black_small_square: [NamedAttribute](attribute.md#namedattribute) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- **D** : [Diffuse](shader.md#diffuse)
- **E** : [Emission](shader.md#emission)
- **G** : [Glass](shader.md#glass) :black_small_square: [Glossy](shader.md#glossy)
- **H** : [Holdout](shader.md#holdout)
- **P** : [Principled](shader.md#principled)
- **R** : [Refraction](shader.md#refraction)
- **S** : [Specular](shader.md#specular) :black_small_square: [SubsurfaceScattering](shader.md#subsurfacescattering)
- **T** : [Translucent](shader.md#translucent) :black_small_square: [Transparent](shader.md#transparent)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Holdout()

> classmethod

``` python
Holdout()
```

Node 'Holdout' (ShaderNodeHoldout)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>

----------
### Transparent()

> classmethod

``` python
Transparent(color=None)
```

Node 'Transparent BSDF' (ShaderNodeBsdfTransparent)

#### Arguments:
- **color** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Shader](shader.md#shader) :black_small_square: [Content](shader.md#content) :black_small_square: [Methods](shader.md#methods)</sub>