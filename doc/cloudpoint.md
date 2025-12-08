# CloudPoint

``` python
CloudPoint(geometry: geonodes.core.geometry_class.Geometry)
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

[accumulate_field](core-gener-dom_p-point.md#accumulate_field) :black_small_square: [active_element](core-gener-dom_p-point.md#active_element) :black_small_square: [attribute_statistic](core-gener-dom_p-point.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [count](corner.md#count) :black_small_square: [delete](core-gener-dom_p-point.md#delete) :black_small_square: [delete_all](core-gener-dom_p-point.md#delete_all) :black_small_square: [delete_edge_face](core-gener-dom_p-point.md#delete_edge_face) :black_small_square: [delete_geometry](core-gener-dom_p-point.md#delete_geometry) :black_small_square: [delete_geometry_all](core-gener-dom_p-point.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](core-gener-dom_p-point.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](core-gener-dom_p-point.md#delete_geometry_only_face) :black_small_square: [delete_only_face](core-gener-dom_p-point.md#delete_only_face) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [duplicate](core-gener-dom_p-point.md#duplicate) :black_small_square: [evaluate_at_index](core-gener-dom_p-point.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](core-gener-dom_p-point.md#evaluate_on_domain) :black_small_square: [field_average](core-gener-dom_p-point.md#field_average) :black_small_square: [field_min_max](core-gener-dom_p-point.md#field_min_max) :black_small_square: [field_variance](core-gener-dom_p-point.md#field_variance) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [foreach](domain.md#foreach) :black_small_square: [for_each_element](domain.md#for_each_element) :black_small_square: [\_geo](domain.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](domain.md#get_selection) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [instance_on](core-gener-dom_p-point.md#instance_on) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [normal](core-gener-dom_p-point.md#normal) :black_small_square: [offset](core-gener-dom_p-point.md#offset) :black_small_square: [position](core-gener-dom_p-point.md#position) :black_small_square: [sample_index](core-gener-dom_p-point.md#sample_index) :black_small_square: [sample_nearest](core-gener-dom_p-point.md#sample_nearest) :black_small_square: ['_selection' not found]() :black_small_square: [separate](core-gener-dom_p-point.md#separate) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [set_radius](core-gener-dom_p-point.md#set_radius) :black_small_square: [set_selection](core-gener-dom_p-point.md#set_selection) :black_small_square: [sort](core-gener-dom_p-point.md#sort) :black_small_square: [split_to_instances](core-gener-dom_p-point.md#split_to_instances) :black_small_square: [store](core-gener-dom_p-point.md#store) :black_small_square: [store_named_attribute](core-gener-dom_p-point.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [viewer](core-gener-dom_p-point.md#viewer) :black_small_square:

## Content

- [\_geo](cloudpoint.md#_geo)
- [radius](cloudpoint.md#radius)

## Properties



### \_geo

> _type_: **Geometry**
>

the geometry the domain belongs to

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [CloudPoint](cloudpoint.md#cloudpoint) :black_small_square: [Content](cloudpoint.md#content) :black_small_square: [Properties](cloudpoint.md#properties)</sub>

### radius

> _type_: **?**
>

Property get node <Node Set Point Radius>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [CloudPoint](cloudpoint.md#cloudpoint) :black_small_square: [Content](cloudpoint.md#content) :black_small_square: [Properties](cloudpoint.md#properties)</sub>