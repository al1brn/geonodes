# GeoBase

``` python
GeoBase(/, *args, **kwargs)
```

Base class for Geometry and Domain.

Implement auto selection mechanism.

#### Arguments:
- **args**
- **kwargs**

## Content

- [id](geono-geobase.md#id)
- [material](geono-geobase.md#material)
- [material_index](geono-geobase.md#material_index)
- [offset](geono-geobase.md#offset)
- [position](geono-geobase.md#position)
- [replace_material](geono-geobase.md#replace_material)
- [set_id](geono-geobase.md#set_id)
- [set_position](geono-geobase.md#set_position)

## Properties



### id

> _type_: **Integer**
>

> Id property

- getter : [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/id.html)
- setter : [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Properties](geono-geobase.md#properties)</sub>

### material

> _type_: **Error**
>

> Material write only property

- getter : None
- setter : [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Properties](geono-geobase.md#properties)</sub>

### material_index

> _type_: **Integer**
>

> Material index property

- getter : [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
- setter : [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Properties](geono-geobase.md#properties)</sub>

### offset

> _type_: **Error**
>

> Offset write only property

- getter : None
- setter : [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Properties](geono-geobase.md#properties)</sub>

### position

> _type_: **Vector**
>

> Position property

- getter : node [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/position.html)
- setter : node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Properties](geono-geobase.md#properties)</sub>

## Methods



----------
### replace_material()

> method

``` python
replace_material(old=None, new=None)
```

> Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)



#### Arguments:
- **old** (_Material_ = None) : socket 'Old' (Old)
- **new** (_Material_ = None) : socket 'New' (New)



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Methods](geono-geobase.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

> Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)



#### Arguments:
- **id** (_Integer_ = None) : socket 'ID' (ID)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Methods](geono-geobase.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

> Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geobase.md#geobase) :black_small_square: [Content](geono-geobase.md#content) :black_small_square: [Methods](geono-geobase.md#methods)</sub>