# Repeat

> Bases classes: [Zone](geono-zone.md#zone)

``` python
Repeat(sockets={}, iterations=1, **snake_case_sockets)
```

> Reapeat zone

> See [Zone](geono-zone.md#zone)

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

### Inherited

[\_\_enter__](geono-zone.md#__enter__) :black_small_square: [\_\_exit__](geono-zone.md#__exit__) :black_small_square: [\_\_getattr__](geono-zone.md#__getattr__) :black_small_square: [init_zone](geono-zone.md#init_zone) :black_small_square: [\_\_setattr__](geono-zone.md#__setattr__) :black_small_square: [\_\_str__](geono-zone.md#__str__) :black_small_square: