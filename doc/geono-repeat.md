# Repeat

``` python
Repeat(sockets={}, iterations=1, **snake_case_sockets)
```

> Reapeat zone

> See ['Zone' not found]()

``` python
from geonodes import *

with GeoNodes("Demo Repeat"):

    with Repeat(Geometry=Geometry(), z=3, iterations=5) as repeat_zone:

        # Lopp geomety
        geo = repeat_zone.geometry

        # Offset upwards
        geo = geo.set_position(offset=(0, 0, repeat_zone.z))

        # Join to loop geometry (CAUTION: exponential growth)
        repeat_zone.geometry += geo

        # Net vertical offset
        repeat_zone.z *= 2

    # Result to output
    repeat_zone.geometry.out()
```

#### Arguments:
- **sockets** (_dict_ = {}) : sockets to create
- **iterations** (_int_ = 1) : Iterations socket
- **snake_case_sockets** : sockets to create

## Content

- [init_zone](geono-repeat.md#init_zone)

## Methods



----------
### init_zone()

> method

``` python
init_zone(sockets={}, create_geometry=True, **snake_case_sockets)
```

> Two nodes zone

**Zone** is the root class for [Simulation](geono-simulation.md#simulation) and [Repeat](geono-repeat.md#repeat) zones.

#### With block

A **Zone** is intended to be used in a **with** block:

``` python
with Zone(...) as zone:
    ...
```

#### Sockets definition

The zone sockets can be defined in two ways:
- using the **sockets** dict argument
- using the **snake_case_sockets** key word arguments

````python
# Create a zone with 2 sockets:
# - First Socket
# - second_ocket
with Zone(socket={"First Socket": Float(3.14)}, second_socket=Geometry()) as zone:
    ...
```

> [!NOTE]
> The sockets are created on the two nodes and, in both nodes, as input and output sockets.
> Hence, a single name correspond two 4 sockets:
> - input socket of the first node
> - output socket of the first node
> - input socket of the second node
> - output socket of the second node

#### Getting and setting zone sockets

Zone sockets are accessed through their **snake_case** name whatever the manner they have
been initialized:

``` python
with Zone(socket={"First Socket": Float(3.14)}, second_socket=Geometry()) as zone:
    a = zone.first_socket
    b = zone.second_socket
```

Inside the **with** block:
- **getting** a socket: output socket of the first node
- **setting** a socket: input socket of the second node

Outside the **with** block:
- **getting** a socket: output socket of the second node
- **setting** a socket: Error

Even if it is not easy to describe, this is in fact quite straightforward:

``` python
with Repeat(geometry=None, index=0, iterations=10) as repeat_zone:

    # Value of the current index
    index = repeat_zone.index

    # ...

    # Update the index for next loop
    repeat_zone.index = index + 1

    # Incrementing is also valid
    repeat_zone.index += 1

# Outside the block, we have accees to the result of the loop
geo = repeat_zone.geometry
```

#### Arguments:
- **sockets** (_dict_ = {}) : sockets to create
- **create_geometry** (_bool_ = True) : ensure the 'Geometry' socket is created
- **snake_case_sockets** : sockets to create

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Repeat](geono-repeat.md#repeat) :black_small_square: [Content](geono-repeat.md#content) :black_small_square: [Methods](geono-repeat.md#methods)</sub>