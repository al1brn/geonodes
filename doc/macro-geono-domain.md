# Domain

> Bases classes: [GeoBase](geono-geobase.md#geobase) :black_small_square: [NodeCache](geono-nodecache.md#nodecache)

``` python
Domain(geometry)
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

Properties:
- _geo (Geometry) : the geometry the domain belongs to

#### Arguments:
- **geometry**

### Inherited

[\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [set_id](geono-geobase.md#set_id) :black_small_square: [set_position](geono-geobase.md#set_position) :black_small_square:

## Content

- **A** : [accumulate_field](macro-geono-domain.md#accumulate_field) :black_small_square: [attribute_statistic](macro-geono-domain.md#attribute_statistic)
- **C** : [capture](macro-geono-domain.md#capture) :black_small_square: [capture_attribute](macro-geono-domain.md#capture_attribute)
- **D** : [delete](macro-geono-domain.md#delete) :black_small_square: [delete_all](macro-geono-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](macro-geono-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](macro-geono-domain.md#delete_faces) :black_small_square: [delete_geometry](macro-geono-domain.md#delete_geometry) :black_small_square: [duplicate_elements](macro-geono-domain.md#duplicate_elements)
- **E** : [evaluate_at_index](macro-geono-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](macro-geono-domain.md#evaluate_on_domain) :black_small_square: [extrude](macro-geono-domain.md#extrude)
- **P** : [proximity](macro-geono-domain.md#proximity)
- **S** : [sample_index](macro-geono-domain.md#sample_index) :black_small_square: [sample_nearest](macro-geono-domain.md#sample_nearest) :black_small_square: [separate](macro-geono-domain.md#separate) :black_small_square: [sort_elements](macro-geono-domain.md#sort_elements) :black_small_square: [split_to_instances](macro-geono-domain.md#split_to_instances) :black_small_square: [store](macro-geono-domain.md#store) :black_small_square: [store_named_attribute](macro-geono-domain.md#store_named_attribute)
- **T** : [to_points](macro-geono-domain.md#to_points)
- **V** : [viewer](macro-geono-domain.md#viewer)

## Methods



----------
### accumulate_field()

> method

``` python
accumulate_field(value=None, group_id=None)
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group Index)



#### Returns:
- **Node** : 'Accumulate Field'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### attribute_statistic()

> method

``` python
attribute_statistic(attribute=None)
```

> Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

#### Arguments:
- **attribute** (_Socket_ = None) : attribute to compute statistic



#### Returns:
- **Node** : 'Attribute Statistic Node'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### capture()

> method

``` python
capture(attribute=None, **others)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)

> see [capture_attribute](macro-geono-domain.md#capture_attribute)

#### Arguments:
- **attribute** ( = None)
- **others**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### capture_attribute()

> method

``` python
capture_attribute(attribute=None, **others)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)

:warning: returns the **node**, not a socket

This method return the capture of 'attribute' argument if no keyword arguments are provided,
otherwise returns the node.

``` python
with GeoNodes("Capture Attribute"):
    mesh = Mesh()

    # A single anonymous attribute
    p = mesh.points.capture_attribute(nd.position)
    assert(isinstance(p, Vector))

    # Only named attributes
    node = mesh.faces.capture_attribute(pos=nd.position, idx=nd.material_index)
    assert(isinstance(node, Node))
    assert(isinstance(node.pos, Vector))
    assert(isinstance(node.idx, Integer))

    # Anonymous attribute plus named attributes
    node = mesh.faces.capture_attribute(nd.position, idx=nd.material_index)
    assert(isinstance(node, Node))
    assert(isinstance(node.attribute, Vector))
    assert(isinstance(node.idx, Integer))
```

#### Arguments:
- **attribute** (_Socket_ = None) : attribute to capture
- **others** (_Sockets_) : named attributes to capture



#### Returns:
- **Socket** (_no keyword arguments_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> See [delete_geometry](macro-geono-domain.md#delete_geometry)

#### Arguments:
- **mode** ( = ALL)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### delete_all()

> method

``` python
delete_all()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Shortcut for :
``` python
domain.delete_geometry(mode='ALL')
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### delete_edges_and_faces()

> method

``` python
delete_edges_and_faces()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Shortcut for :
``` python
domain.delete_geometry(mode='EDGE_FACE')
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### delete_faces()

> method

``` python
delete_faces()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Shortcut for :
``` python
domain.delete_geometry(mode='ONLY_FACE')
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **mode** (_str_ = ALL) : Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### duplicate_elements()

> method

``` python
duplicate_elements(amount=1)
```

> Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

#### Arguments:
- **amount** (_Integer_ = 1) : socket 'Amount' (Amount)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### evaluate_at_index()

> method

``` python
evaluate_at_index(index=None, value=None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### evaluate_on_domain()

> method

``` python
evaluate_on_domain(value=None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### extrude()

> method

``` python
extrude(offset=None, offset_scale=None, individual=None)
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

- mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES')

``` python
with GeoNodes("Extrusion"):
    cube = Mesh.Cube()

    cube = cube.faces.extrude(nd.normal, .5)
    cube = cube.faces[cube.top_].extrude(offset_scale=0)
    top = cube.top_
    cube = cube.faces[top].scale(scale=.8, uniform=False)
    cube = cube.faces[top].scale(scale=.6, uniform=True)
    cube = cube.faces[top].extrude(offset_scale=.5)
    cube = cube.faces[cube.top_].flip()

    cube.out()
```

#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (Offset Scale)
- **individual** (_Boolean_ = None) : socket 'Individual' (Individual)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### proximity()

> method

``` python
proximity(group_id=None, sample_position=None, sample_group_id=None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (Sample Group ID)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### sample_index()

> method

``` python
sample_index(value=None, index=0, clamp=False)
```

> Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **index** (_Integer_ = 0) : socket 'Index' (Index)
- **clamp** (_bool_ = False) : Node.clamp



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position=None)
```

> Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER')

#### Arguments:
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Sample Position)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

> Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

:warning: returns the **node**, not a socket

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### sort_elements()

> method

``` python
sort_elements(group_id=None, sort_weight=None)
```

> Node [Sort Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/sort_elements.html)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (Sort Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### split_to_instances()

> method

``` python
split_to_instances(group_id=None)
```

> Node [Split to Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/split_to_instances.html)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### store()

> method

``` python
store(name, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

> See [store_named_attribute](macro-geono-domain.md#store_named_attribute)

#### Arguments:
- **name**
- **value** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

- mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Arguments:
- **value** (_Socket_ = None) : value to view

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](macro-geono-domain.md#domain) :black_small_square: [Content](macro-geono-domain.md#content) :black_small_square: [Methods](macro-geono-domain.md#methods)</sub>