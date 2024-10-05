# Layout

``` python
Layout(label=None, color=None)
```

Node Frame

All nodes created when a Layout is open are placed in this layout.
If the 'color' argument is None, a random color is used

``` python
with GeoNodes("Layout Demo"):

    with Layout("Some maths"):
        z = gnmath.atan2(nd.position.z, Vector((nd.position.x, nd.position.y, 0)).length)

    geo = Mesh()
    geo.points.offset = (0, 0, z)

    geo.out()
```

#### Arguments:
- **label** (_str_ = None) : Layout title
- **color** (_blender color_ = None) : Layout color (randomly generated if None)

## Content

- [\_\_init__](layout.md#__init__)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(label=None, color=None)
```

Node Frame

All nodes created when a Layout is open are placed in this layout.
If the 'color' argument is None, a random color is used

``` python
with GeoNodes("Layout Demo"):

    with Layout("Some maths"):
        z = gnmath.atan2(nd.position.z, Vector((nd.position.x, nd.position.y, 0)).length)

    geo = Mesh()
    geo.points.offset = (0, 0, z)

    geo.out()
```

#### Arguments:
- **label** (_str_ = None) : Layout title
- **color** (_blender color_ = None) : Layout color (randomly generated if None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Layout](layout.md#layout) :black_small_square: [Content](layout.md#content) :black_small_square: [Methods](layout.md#methods)</sub>