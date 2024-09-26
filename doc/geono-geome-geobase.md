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

- [id](geono-geome-geobase.md#id)
- [material_index](geono-geome-geobase.md#material_index)
- [position](geono-geome-geobase.md#position)
- [replace_material](geono-geome-geobase.md#replace_material)
- [set_id](geono-geome-geobase.md#set_id)
- [set_position](geono-geome-geobase.md#set_position)

## Properties



### id

> _type_: **Integer**
>

Node 'ID' (GeometryNodeInputID)

[!Node] ID

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Content](geono-geome-geobase.md#content) :black_small_square: [Properties](geono-geome-geobase.md#properties)</sub>

### material_index

> _type_: **Integer**
>

Node 'Material Index' (GeometryNodeInputMaterialIndex)

[!Node] Material Index

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Content](geono-geome-geobase.md#content) :black_small_square: [Properties](geono-geome-geobase.md#properties)</sub>

### position

> _type_: **Vector**
>

Node 'Position' (GeometryNodeInputPosition)

[!Node] Position

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Content](geono-geome-geobase.md#content) :black_small_square: [Properties](geono-geome-geobase.md#properties)</sub>

## Methods



----------
### replace_material()

> method

``` python
replace_material(old=None, new=None)
```

Node 'Replace Material' (GeometryNodeReplaceMaterial)

[!Node] Replace Material

#### Arguments:
- **old** (_Material_ = None) : socket 'Old' (Old)
- **new** (_Material_ = None) : socket 'New' (New)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Content](geono-geome-geobase.md#content) :black_small_square: [Methods](geono-geome-geobase.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

Node 'Set ID' (GeometryNodeSetID)

[!Node] Set ID

#### Arguments:
- **id** (_Integer_ = None) : socket 'ID' (ID)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Content](geono-geome-geobase.md#content) :black_small_square: [Methods](geono-geome-geobase.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

Node 'Set Position' (GeometryNodeSetPosition)

[!Node] Set Position

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Content](geono-geome-geobase.md#content) :black_small_square: [Methods](geono-geome-geobase.md#methods)</sub>