# Simulation

``` python
Simulation(sockets={}, **snake_case_sockets)
```

> Simulation zone

> See [Zone](zone.md#zone)

``` python
from geonodes import *

with GeoNodes("Demo Simulation"):

    cloud = Cloud.Points(count=100, position=Vector.Random(-5, 5))

    with Simulation(cloud=cloud, index=0) as sim_zone:

        # Current points
        cloud = sim_zone.cloud

        # Get the nearest index
        index = nd.index_of_nearest(position=nd.position).index

        # Nearest position
        nearest_pos = cloud.points.sample_index(nd.position, index=index)

        # Direction
        v = (nearest_pos - nd.position).normalize()

        #cloud.points.offset = v.normalize()*(dist-.5)/2 + Vector.Random(-.2, .2, seed=nd.scene_time.frame)
        cloud.points.offset = v*.1 + Vector.Random(-.2, .2, seed=nd.scene_time.frame)

        sim_zone.cloud = cloud

    # Result to output
    sim_zone.cloud.out()
```

#### Arguments:
- **sockets** (_dict_ = {}) : sockets to create
- **snake_case_sockets** : sockets to create

### Inherited

[\_\_enter__](zone.md#__enter__) :black_small_square: [\_\_exit__](zone.md#__exit__) :black_small_square: [\_\_getattr__](zone.md#__getattr__) :black_small_square: [init_layout](zone.md#init_layout) :black_small_square: [init_zone](zone.md#init_zone) :black_small_square: [\_\_setattr__](zone.md#__setattr__) :black_small_square: [\_\_str__](zone.md#__str__) :black_small_square:

## Content

- [\_\_init__](simulation.md#__init__)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(sockets={}, **snake_case_sockets)
```

> Simulation zone

> See [Zone](zone.md#zone)

``` python
from geonodes import *

with GeoNodes("Demo Simulation"):

    cloud = Cloud.Points(count=100, position=Vector.Random(-5, 5))

    with Simulation(cloud=cloud, index=0) as sim_zone:

        # Current points
        cloud = sim_zone.cloud

        # Get the nearest index
        index = nd.index_of_nearest(position=nd.position).index

        # Nearest position
        nearest_pos = cloud.points.sample_index(nd.position, index=index)

        # Direction
        v = (nearest_pos - nd.position).normalize()

        #cloud.points.offset = v.normalize()*(dist-.5)/2 + Vector.Random(-.2, .2, seed=nd.scene_time.frame)
        cloud.points.offset = v*.1 + Vector.Random(-.2, .2, seed=nd.scene_time.frame)

        sim_zone.cloud = cloud

    # Result to output
    sim_zone.cloud.out()
```

#### Arguments:
- **sockets** (_dict_ = {}) : sockets to create
- **snake_case_sockets** : sockets to create

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Simulation](simulation.md#simulation) :black_small_square: [Content](simulation.md#content) :black_small_square: [Methods](simulation.md#methods)</sub>