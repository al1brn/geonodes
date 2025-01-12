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

> [!IMPORTANT]
> Domains are never instantiated directly but created by geometries.

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

Properties:
- _geo (Geometry) : the geometry the domain belongs to

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- [capture](domain.md#capture)
- [capture_attribute](domain.md#capture_attribute)
- [for_each](domain.md#for_each)
- [\_\_init__](domain.md#__init__)

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
### for_each()

> method

``` python
for_each(sockets={}, **kwargs)
```

> Create a [ForEachElement](foreachelement.md#foreachelement) zone on this domain

The [ForEachElement](foreachelement.md#foreachelement) zone is initialized with the domain, its geometry and
the selection:

``` python
ico = Mesh.IcoSphere(subdivisions=2)
with ico.faces[(nd.index % 2).equal(0)].for_each(position=nd.position) as feel:
    face = Mesh(feel.element)
    face.points.offset = feel.position*1.1
    feel.generated.geometry = face

feel.generated.geometry.out()
```

#### Arguments:
- **sockets** (_dict_ = {}) : input sockets
- **kwargs** : input sockets



#### Returns:
- **ForEachElement** :

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

> [!IMPORTANT]
> Domains are never instantiated directly but created by geometries.

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

Properties:
- _geo (Geometry) : the geometry the domain belongs to

#### Arguments:
- **geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>