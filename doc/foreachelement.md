# ForEachElement

> Bases classes: [Zone](zone.md#zone)

``` python
ForEachElement(geometry=None, selection=None, domain=None, sockets={}, **snake_case_sockets)
```

> For Each Element zone

> See [Zone](zone.md#zone)

This loops has 3 items lists with their corresponding index:
- input_items, active_input_index
- main_items, active_main_index
- generation_items, active_generation_index

The zone initialization creates properties on the input_items.

The output node of the zone has two subsets of sockets:
- ***Main*** sockets
- ***Generated*** sockets

Sockets can be created in each subset by setting a property. They can be read once
the block in closed:

``` python
with ForEachElement() as feel:
    # Creating a socket in the main subset
    feel.main.vector = Vector()

    # Join the geometry
    feel.generated.geometry = Mesh.Cube()
```

> [!NOTE]
> It is recommended to use the `for_each` method of a domain rather than instantiate
> the class

``` python
cube = Mesh.Cube()
with cube.faces.for_each(position=nd.position) as feel:
    pass
```

#### Arguments:
- **geometry** (_Geometry_ = None) : geometry to loop on
- **selection** (_Boolean_ = None) : element selection
- **domain** (_str_ = None) : domain name
- **sockets** (_dict_ = {}) : sockets to create
- **snake_case_sockets** : sockets to create

### Inherited

[\_\_enter__](zone.md#__enter__) :black_small_square: [\_\_exit__](zone.md#__exit__) :black_small_square: [\_\_getattr__](zone.md#__getattr__) :black_small_square: [init_layout](zone.md#init_layout) :black_small_square: [init_zone](zone.md#init_zone) :black_small_square: [\_\_setattr__](zone.md#__setattr__) :black_small_square: [\_\_str__](zone.md#__str__) :black_small_square:

## Content

- [element](foreachelement.md#element)
- [generated](foreachelement.md#generated)
- [index](foreachelement.md#index)
- [\_\_init__](foreachelement.md#__init__)
- [main](foreachelement.md#main)

## Properties



### element

> _type_: **Geometry**
>

Element socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ForEachElement](foreachelement.md#foreachelement) :black_small_square: [Content](foreachelement.md#content) :black_small_square: [Properties](foreachelement.md#properties)</sub>

### generated

> _type_: **Node like**
>

contains the sockets in the ***Generated*** part of the output node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ForEachElement](foreachelement.md#foreachelement) :black_small_square: [Content](foreachelement.md#content) :black_small_square: [Properties](foreachelement.md#properties)</sub>

### index

> _type_: **Integer**
>

Index socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ForEachElement](foreachelement.md#foreachelement) :black_small_square: [Content](foreachelement.md#content) :black_small_square: [Properties](foreachelement.md#properties)</sub>

### main

> _type_: **Node like**
>

contains the sockets in the ***Main*** part of the output node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ForEachElement](foreachelement.md#foreachelement) :black_small_square: [Content](foreachelement.md#content) :black_small_square: [Properties](foreachelement.md#properties)</sub>

## Methods



----------
### \_\_init__()

> method

``` python
__init__(geometry=None, selection=None, domain=None, sockets={}, **snake_case_sockets)
```

> For Each Element zone

> See [Zone](zone.md#zone)

This loops has 3 items lists with their corresponding index:
- input_items, active_input_index
- main_items, active_main_index
- generation_items, active_generation_index

The zone initialization creates properties on the input_items.

The output node of the zone has two subsets of sockets:
- ***Main*** sockets
- ***Generated*** sockets

Sockets can be created in each subset by setting a property. They can be read once
the block in closed:

``` python
with ForEachElement() as feel:
    # Creating a socket in the main subset
    feel.main.vector = Vector()

    # Join the geometry
    feel.generated.geometry = Mesh.Cube()
```

> [!NOTE]
> It is recommended to use the `for_each` method of a domain rather than instantiate
> the class

``` python
cube = Mesh.Cube()
with cube.faces.for_each(position=nd.position) as feel:
    pass
```

#### Arguments:
- **geometry** (_Geometry_ = None) : geometry to loop on
- **selection** (_Boolean_ = None) : element selection
- **domain** (_str_ = None) : domain name
- **sockets** (_dict_ = {}) : sockets to create
- **snake_case_sockets** : sockets to create

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ForEachElement](foreachelement.md#foreachelement) :black_small_square: [Content](foreachelement.md#content) :black_small_square: [Methods](foreachelement.md#methods)</sub>