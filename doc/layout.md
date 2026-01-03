# Layout

``` python
Layout(title: str = '', color: str = None, node=None)
```

Node Frame

All nodes created when a Layout is open are placed in this layout.
If the 'color' argument is None, a random color is used

If the node argument is None, the layout parent is the current layout, otherwise,
the layout becomes the parent of the node and the previous parent of the node
becomes the layout parent.

``` python
with GeoNodes("Layout Demo"):

    with Layout("Some maths"):
        a = Integer(1) + 1

    geo = Mesh()
    geo.points.offset = (0, 0, a)

    geo.out()
```

#### Arguments:
- **title** (_str_ = ) : Layout title
- **color** (_str_ = None) : Layout color (randomly generated if None)
- **node** (_Node_ = None) : the layout is inserted as direct parent of the node

## Content

- [\_\_init__](layout.md#__init__)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(title: str = '', color: str = None, node=None)
```

Node Frame

All nodes created when a Layout is open are placed in this layout.
If the 'color' argument is None, a random color is used

If the node argument is None, the layout parent is the current layout, otherwise,
the layout becomes the parent of the node and the previous parent of the node
becomes the layout parent.

``` python
with GeoNodes("Layout Demo"):

    with Layout("Some maths"):
        a = Integer(1) + 1

    geo = Mesh()
    geo.points.offset = (0, 0, a)

    geo.out()
```

#### Arguments:
- **title** (_str_ = ) : Layout title
- **color** (_str_ = None) : Layout color (randomly generated if None)
- **node** (_Node_ = None) : the layout is inserted as direct parent of the node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Layout](layout.md#layout) :black_small_square: [Content](layout.md#content) :black_small_square: [Methods](layout.md#methods)</sub>