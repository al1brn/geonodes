# Domain

``` python
Domain(geometry: geonodes.core.geometry_class.Geometry)
```

> Base class for geometry domains

A domain stores the default value to be set in node needing a **domain** parameter
such as 'Store Named Attibute.

All nodes requiring a domain parameter are implemented as domain method

``` python
cube = Mesh.Cube()
cube.faces.store_named_attribute() # doamin = 'FACE'
```

When a node as a ***Selection*** socket, the value can be set using the get item syntax:

``` python
    # Plug the value of 'my_selection` into Selection socket
    Mesh().points[my_selection].store_named_attribute("Name", value)
```

> [!IMPORTANT]
> Domains are never instantiated directly but created by geometries.

The domain specific to geometries are the followings:
    - Mesh:
        - points (class [Vertex](vertex.md#vertex))
        - faces (class [Face](face.md#face))
        - edges (class [Edge](edge.md#edge))
        - corners (clas [Corner](corner.md#corner))
    - Curve:
        - points (class [SplinePoint](splinepoint.md#splinepoint))
        - splines (class [Spline](spline.md#spline))
    - GreasePencil:
        - layers (class [Layer](layer.md#layer))
    - Instances
        - insts (class [Instance](instance.md#instance))
    - Cloud
        - points (class [CloudPoint](cloudpoint.md#cloudpoint))
    - Volume

All the domain classes are a subclass of [Domain](domain.md#domain).
[Vertex](vertex.md#vertex), [SplinePoint](splinepoint.md#splinepoint) and [SplinePoint](splinepoint.md#splinepoint) classes are subclasses of [Point](point.md#point).

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_geo](domain.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: ['_selection' not found]() :black_small_square:

## Content

- [capture](domain.md#capture)
- [capture_attribute](domain.md#capture_attribute)
- [for_each_element](domain.md#for_each_element)
- [\_geo](domain.md#_geo)
- [get_selection](domain.md#get_selection)
- [\_\_init__](domain.md#__init__)

## Properties



### \_geo

> _type_: **Geometry**
>

the geometry the domain belongs to

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Properties](domain.md#properties)</sub>

## Methods



----------
### capture()

> method

``` python
capture(attribute=None, **attributes)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)



> Short name for [capture_attribute](domain.md#capture_attribute)

#### Arguments:
- **attribute** (_Socket_ = None) : first attribute to capture
- **attributes** (_Sockets_) : named attributes to capture



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### capture_attribute()

> method

``` python
capture_attribute(attribute=None, **attributes)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)



> [!CAUTION]
> When there is only one attribute, the function returns the captured attribute,
> otherwise returns the node.

``` python
with GeoNodes("Capture Attribute"):
    # Capture several attributes
    node = mesh.points.capture_attribute(attr1 = attr1, attr2=attr2)
    captured_attr1 = node.attr1
    captured_attr2 = node.attr2

    # Capture one single attribute
    captured_attr = mesh.points.capture_attribute(my_attr=attr1)

    # Capture one attribute without key
    captured_attr3 = mesh.points.capture_attribute(attr3)
```

#### Arguments:
- **attribute** (_Socket_ = None) : first attribute to capture
- **attributes** (_Sockets_) : named attributes to capture



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### for_each_element()

> method

``` python
for_each_element(named_sockets: dict = {}, selection=None, **sockets)
```

Simulation zone

#### Arguments:
- **named_sockets** (_dict_ = {})
- **selection** (_Boolean_ = None) : selection
- **sockets** (_dict_) : other sockets



#### Returns:
- **ZoneIterator** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### get_selection()

> method

``` python
get_selection()
```

Get the selection from Gometry and/or from Domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(geometry: geonodes.core.geometry_class.Geometry)
```

> Base class for geometry domains

A domain stores the default value to be set in node needing a **domain** parameter
such as 'Store Named Attibute.

All nodes requiring a domain parameter are implemented as domain method

``` python
cube = Mesh.Cube()
cube.faces.store_named_attribute() # doamin = 'FACE'
```

When a node as a ***Selection*** socket, the value can be set using the get item syntax:

``` python
    # Plug the value of 'my_selection` into Selection socket
    Mesh().points[my_selection].store_named_attribute("Name", value)
```

> [!IMPORTANT]
> Domains are never instantiated directly but created by geometries.

The domain specific to geometries are the followings:
    - Mesh:
        - points (class [Vertex](vertex.md#vertex))
        - faces (class [Face](face.md#face))
        - edges (class [Edge](edge.md#edge))
        - corners (clas [Corner](corner.md#corner))
    - Curve:
        - points (class [SplinePoint](splinepoint.md#splinepoint))
        - splines (class [Spline](spline.md#spline))
    - GreasePencil:
        - layers (class [Layer](layer.md#layer))
    - Instances
        - insts (class [Instance](instance.md#instance))
    - Cloud
        - points (class [CloudPoint](cloudpoint.md#cloudpoint))
    - Volume

All the domain classes are a subclass of [Domain](domain.md#domain).
[Vertex](vertex.md#vertex), [SplinePoint](splinepoint.md#splinepoint) and [SplinePoint](splinepoint.md#splinepoint) classes are subclasses of [Point](point.md#point).

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

#### Arguments:
- **geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>