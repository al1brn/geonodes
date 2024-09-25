# Domain

> Bases classes: [GeoBase](geono-geome-geobase.md) :black_small_square: [NodeCache](geono-socke-nodecache.md)

``` python
Domain(geometry)
```



#### Arguments:
- **geometry**

### Inherited

[\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [set_id](geono-geome-geobase.md#set_id) :black_small_square: [set_position](geono-geome-geobase.md#set_position) :black_small_square:

## Content

- **A** : [accumulate_field](geono-geome-domain.md#accumulate_field)
- **C** : [capture](geono-geome-domain.md#capture) :black_small_square: [capture_attribute](geono-geome-domain.md#capture_attribute)
- **D** : [delete](geono-geome-domain.md#delete) :black_small_square: [delete_all](geono-geome-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-geome-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-geome-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-geome-domain.md#delete_geometry) :black_small_square: [duplicate_elements](geono-geome-domain.md#duplicate_elements)
- **E** : [evaluate_at_index](geono-geome-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-geome-domain.md#evaluate_on_domain) :black_small_square: [extrude](geono-geome-domain.md#extrude)
- **P** : [proximity](geono-geome-domain.md#proximity)
- **S** : [sample_index](geono-geome-domain.md#sample_index) :black_small_square: [sample_nearest](geono-geome-domain.md#sample_nearest) :black_small_square: [separate](geono-geome-domain.md#separate) :black_small_square: [sort_elements](geono-geome-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-geome-domain.md#split_to_instances) :black_small_square: [store](geono-geome-domain.md#store) :black_small_square: [store_named_attribute](geono-geome-domain.md#store_named_attribute)
- **T** : [to_points](geono-geome-domain.md#to_points)

## Methods



----------
### accumulate_field()

> method

``` python
accumulate_field(value=None, group_id=None)
```

Node 'Accumulate Field' (GeometryNodeAccumulateField)

[!Node] Accumulate Field

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group Index)



#### Returns:
- **Node** : [leading (Float), trailing (Float), total (Float)]

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### capture()

> method

``` python
capture(attribute=None, **others)
```

Node 'Capture Attribute' (GeometryNodeCaptureAttribute)

[!Node] Capture Attribute

synonym of 'capture_named_attribute'

#### Arguments:
- **attribute** ( = None)
- **others**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### capture_attribute()

> method

``` python
capture_attribute(attribute=None, **others)
```

Node 'Capture Attribute' (GeometryNodeCaptureAttribute)

[!Node] Capture Attribute

This method return the capture of 'attribute' argument if not keyword arguments are provided,
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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode='ALL')
```

Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

[!Node] Delete Geometry

Synonym of 'delete_geometry'

#### Arguments:
- **mode** ( = ALL)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### delete_all()

> method

``` python
delete_all()
```

Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

[!Node] Delete Geometry

Shortcut for : ``` domain.delete_geometry(mode='ALL') ```

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### delete_edges_and_faces()

> method

``` python
delete_edges_and_faces()
```

Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

[!Node] Delete Geometry

Shortcut for : ``` domain.delete_geometry(mode='EDGE_FACE') ```

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### delete_faces()

> method

``` python
delete_faces()
```

Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

[!Node] Delete Geometry

Shortcut for : ``` domain.delete_geometry(mode='ONLY_FACE') ```

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode='ALL')
```

Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

[!Node] Delete Geometry

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **mode** (_str_ = ALL) : Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **geometry** (_Geometry_)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### duplicate_elements()

> method

``` python
duplicate_elements(amount=1)
```

Node 'Duplicate Elements' (GeometryNodeDuplicateElements)

[!Node] Duplicate Elements

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

#### Arguments:
- **amount** (_Integer_ = 1) : socket 'Amount' (Amount)



#### Returns:
- **Geometry** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### evaluate_at_index()

> method

``` python
evaluate_at_index(index=None, value=None)
```

Node 'Evaluate at Index' (GeometryNodeFieldAtIndex)

[!Node] Evaluate at Index

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Socket** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### evaluate_on_domain()

> method

``` python
evaluate_on_domain(value=None)
```

Node 'Evaluate on Domain' (GeometryNodeFieldOnDomain)

[!Node] Evaluate on Domain

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Socket** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### extrude()

> method

``` python
extrude(offset=None, offset_scale=None, individual=None)
```

Node 'Extrude Mesh' (GeometryNodeExtrudeMesh)

[!Node] Extrude Mesh

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### proximity()

> method

``` python
proximity(group_id=None, sample_position=None, sample_group_id=None)
```

Node 'Geometry Proximity' (GeometryNodeProximity)

[!Node] Geometry Proximity

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (Sample Group ID)



#### Returns:
- **Vector** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### sample_index()

> method

``` python
sample_index(value=None, index=0, clamp=False)
```

Node 'Sample Index' (GeometryNodeSampleIndex)

[!Node] Sample Index

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **index** (_Integer_ = 0) : socket 'Index' (Index)
- **clamp** (_bool_ = False) : Node.clamp



#### Returns:
- **Socket** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position=None)
```

Node 'Sample Nearest' (GeometryNodeSampleNearest)

[!Node] Sample Nearest

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER')

#### Arguments:
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Sample Position)



#### Returns:
- **Integer** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

Node 'Separate Geometry' (GeometryNodeSeparateGeometry)

[!Node] Separate Geometry

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Returns:
- **Geometry** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### sort_elements()

> method

``` python
sort_elements(group_id=None, sort_weight=None)
```

Node 'Sort Elements' (GeometryNodeSortElements)

[!Node] Sort Elements

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (Sort Weight)



#### Returns:
- **Geometry** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### split_to_instances()

> method

``` python
split_to_instances(group_id=None)
```

Node 'Split to Instances' (GeometryNodeSplitToInstances)

[!Node] Split to Instances

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **instances** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### store()

> method

``` python
store(name, value=None)
```

Node 'Store Named Attribute' (GeometryNodeStoreNamedAttribute)

[!Node] Store Named Attribute

Synonym of 'store_named_attribute'

#### Arguments:
- **name**
- **value** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name, value=None)
```

Node 'Store Named Attribute' (GeometryNodeStoreNamedAttribute)

[!Node] Store Named Attribute

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Geometry** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
```

Node 'Mesh to Points' (GeometryNodeMeshToPoints)

[!Node] Mesh to Points

- mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Geometry** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-domain.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#domain) :black_small_square: [Content](#content) :black_small_square: [Domain](geono-geome-domain.md)</sub>