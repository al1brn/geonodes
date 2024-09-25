# VolumeShader

> Bases classes: [ShaderRoot](shade-shade-shaderroot.md)

``` python
VolumeShader(socket)
```



#### Arguments:
- **socket**

### Inherited

[\_\_add__](shade-shade-shaderroot.md#__add__) :black_small_square: [add](shade-shade-shaderroot.md#add) :black_small_square: [blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [mix](shade-shade-shaderroot.md#mix) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [\_\_radd__](shade-shade-shaderroot.md#__radd__) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [surface_out](shade-shade-shaderroot.md#surface_out) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_rgb](shade-shade-shaderroot.md#to_rgb) :black_small_square: [volume_out](shade-shade-shaderroot.md#volume_out) :black_small_square:

## Content

- [Absorption](shade-shade-volumeshader.md#absorption)
- [Principled](shade-shade-volumeshader.md#principled)
- [Scatter](shade-shade-volumeshader.md#scatter)

## Methods



----------
### Absorption()

> classmethod

``` python
Absorption(color=None, density=None)
```

Node 'Volume Absorption' (ShaderNodeVolumeAbsorption)

#### Arguments:
- **color** ( = None)
- **density** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#volumeshader) :black_small_square: [Content](#content) :black_small_square: [Methods](shade-shade-volumeshader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None)
```

Node 'Principled Volume' (ShaderNodeVolumePrincipled)

#### Arguments:
- **color** ( = None)
- **color_attribute** ( = None)
- **density** ( = None)
- **density_attribute** ( = None)
- **anisotropy** ( = None)
- **absorption_color** ( = None)
- **emission_strength** ( = None)
- **emission_color** ( = None)
- **blackbody_intensity** ( = None)
- **blackbody_tint** ( = None)
- **temperature** ( = None)
- **temperature_attribute** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#volumeshader) :black_small_square: [Content](#content) :black_small_square: [Methods](shade-shade-volumeshader.md#methods)</sub>

----------
### Scatter()

> classmethod

``` python
Scatter(color=None, density=None, anisotropy=None)
```

Node 'Volume Scatter' (ShaderNodeVolumeScatter)

#### Arguments:
- **color** ( = None)
- **density** ( = None)
- **anisotropy** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#volumeshader) :black_small_square: [Content](#content) :black_small_square: [Methods](shade-shade-volumeshader.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#volumeshader) :black_small_square: [Content](#content) :black_small_square: [VolumeShader](shade-shade-volumeshader.md)</sub>