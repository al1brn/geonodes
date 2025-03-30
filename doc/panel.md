# Panel

``` python
Panel(name: str, tip: str = '', default_closed: bool = False)
```

Socket panel

All group input and output sockets an panels will be created within the current panel

``` python
with GeoNodes("Layout Demo"):

    # Socket outside a panel
    g = Geometry()

    with Panel("First Panel"):
        a = Float(10, "Float Socket")
        b = Float(20, "Another Float Socket")

        with Panel("Sub Panel"):
            c = Color(None, "Color")

    with Panel("Second Panel"):
        i = Integer(1, "Integer Socket")
        j = Integer(20 "Another Integer Socket")
```

#### Arguments:
- **name** (_str_) : panel title
- **tip** (_str_ = ) : panel description
- **default_closed** (_bool_ = False) : closed by default

## Content

- [\_\_init__](panel.md#__init__)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(name: str, tip: str = '', default_closed: bool = False)
```

Socket panel

All group input and output sockets an panels will be created within the current panel

``` python
with GeoNodes("Layout Demo"):

    # Socket outside a panel
    g = Geometry()

    with Panel("First Panel"):
        a = Float(10, "Float Socket")
        b = Float(20, "Another Float Socket")

        with Panel("Sub Panel"):
            c = Color(None, "Color")

    with Panel("Second Panel"):
        i = Integer(1, "Integer Socket")
        j = Integer(20 "Another Integer Socket")
```

#### Arguments:
- **name** (_str_) : panel title
- **tip** (_str_ = ) : panel description
- **default_closed** (_bool_ = False) : closed by default

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Panel](panel.md#panel) :black_small_square: [Content](panel.md#content) :black_small_square: [Methods](panel.md#methods)</sub>