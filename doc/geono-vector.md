# Vector

> Bases classes: [ValueSocket](geono-socke-valuesocket.md#valuesocket)

``` python
Vector(value=(0, 0, 0), name=None, tip=None, subtype='NONE')
```



#### Arguments:
- **value** ( = (0, 0, 0))
- **name** ( = None)
- **tip** ( = None)
- **subtype** ( = NONE)

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- [normal](geono-vector.md#normal)
- [Tangent](geono-vector.md#tangent)
- [UVMap](geono-vector.md#uvmap)

## Methods



----------
### normal()

> method

``` python
normal(normal=None)
```

Node 'Normal'

Tree: Shader

#### Arguments:
- **normal** (_Vector_ = None) : 



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](geono-vector.md#vector) :black_small_square: [Content](geono-vector.md#content) :black_small_square: [Methods](geono-vector.md#methods)</sub>

----------
### Tangent()

> classmethod

``` python
Tangent(axis='Z', direction_type='RADIAL', uv_map='')
```

Node 'Tangent' (ShaderNodeTangent)
- axis in ('X', 'Y', 'Z')
- direction_type in ('RADIAL', 'UV_MAP')

#### Arguments:
- **axis** ( = Z)
- **direction_type** ( = RADIAL)
- **uv_map** ( = )

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](geono-vector.md#vector) :black_small_square: [Content](geono-vector.md#content) :black_small_square: [Methods](geono-vector.md#methods)</sub>

----------
### UVMap()

> classmethod

``` python
UVMap(uv_map='', from_instancer=False)
```

Node 'UV Map' (ShaderNodeUVMap)

#### Arguments:
- **uv_map** ( = )
- **from_instancer** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](geono-vector.md#vector) :black_small_square: [Content](geono-vector.md#content) :black_small_square: [Methods](geono-vector.md#methods)</sub>