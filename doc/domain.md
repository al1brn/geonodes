# Domain

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

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

Properties:
- _geo (Geometry) : the geometry the domain belongs to

#### Arguments:
- **geometry**

## Content

- **A** : [accumulate_field](domain.md#accumulate_field) :black_small_square: [attribute_statistic](domain.md#attribute_statistic)
- **C** : [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [captures](domain.md#captures)
- **D** : [delete](domain.md#delete) :black_small_square: [delete_all](domain.md#delete_all) :black_small_square: [delete_edges_and_faces](domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](domain.md#delete_faces) :black_small_square: [delete_geometry](domain.md#delete_geometry) :black_small_square: [duplicate_elements](domain.md#duplicate_elements)
- **E** : [evaluate_at_index](domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](domain.md#evaluate_on_domain) :black_small_square: [extrude](domain.md#extrude)
- **F** : [for_each](domain.md#for_each)
- **I** : [id](domain.md#id) :black_small_square: [\_\_init__](domain.md#__init__)
- **M** : [material](domain.md#material) :black_small_square: [material_index](domain.md#material_index)
- **O** : [offset](domain.md#offset)
- **P** : [position](domain.md#position) :black_small_square: [proximity](domain.md#proximity)
- **R** : [replace_material](domain.md#replace_material)
- **S** : [sample_index](domain.md#sample_index) :black_small_square: [sample_nearest](domain.md#sample_nearest) :black_small_square: [separate](domain.md#separate) :black_small_square: [set_id](domain.md#set_id) :black_small_square: [set_position](domain.md#set_position) :black_small_square: [sort_elements](domain.md#sort_elements) :black_small_square: [split_to_instances](domain.md#split_to_instances) :black_small_square: [store](domain.md#store) :black_small_square: [store_named_attribute](domain.md#store_named_attribute)
- **T** : [to_points](domain.md#to_points)
- **V** : [viewer](domain.md#viewer)

## Properties



### id

> _type_: **Integer**
>

> Id property

- getter : [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/id.html)
- setter : [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Properties](domain.md#properties)</sub>

### material

> _type_: **Error**
>

> Material write only property

- getter : None
- setter : [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Properties](domain.md#properties)</sub>

### material_index

> _type_: **Integer**
>

> Material index property

- getter : [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
- setter : [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Properties](domain.md#properties)</sub>

### offset

> _type_: **Error**
>

> Offset write only property

- getter : None
- setter : [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Properties](domain.md#properties)</sub>

### position

> _type_: **Vector**
>

> Position property

- getter : node [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/position.html)
- setter : node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Properties](domain.md#properties)</sub>

## Methods



----------
### accumulate_field()

> method

``` python
accumulate_field(value=None, group_id=None)
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

:warning: returns the **node**, not a socket

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group Index)



#### Returns:
- **Node** : 'Accumulate Field'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### attribute_statistic()

> method

``` python
attribute_statistic(attribute=None)
```

> Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

:warning: returns the **node**, not a socket

#### Arguments:
- **attribute** (_Socket_ = None) : attribute to compute statistic



#### Returns:
- **Node** : 'Attribute Statistic Node'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### capture()

> method

``` python
capture(attribute)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)



> Short name for [capture_attribute](domain.md#capture_attribute)

``` python
with GeoNodes("Capture Attribute"):
    captured_attr = mesh.points.capture(attr)

    # If more than one attribute is to be captured
    node = mesh.points.captures(attr1 = attr1, attr2=attr2)
    captured_attr1 = node.attr1
    captured_attr2 = node.attr2
```

#### Arguments:
- **attribute** (_Socket_) : the single attribute to capture



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### capture_attribute()

> method

``` python
capture_attribute(**attributes)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)


:warning: returns the **node**, not a socket

> You can use two short names:
> [capture](domain.md#capture) : to capture only one attribute
> [capture](domain.md#capture) : same as **capture_attribute** to capture several named attributes

``` python
with GeoNodes("Capture Attribute"):
    # Capture attributes
    node = mesh.points.capture_attribute(attr1 = attr1, attr2=attr2)
    captured_attr1 = node.attr1
    captured_attr2 = node.attr2

    # Capture one attribute
    captured_attr3 = mesh.points.capture(attr3)
```

#### Arguments:
- **attributes** (_Sockets_) : named attributes to capture



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### captures()

> method

``` python
captures(**attributes)
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)


:warning: returns the **node**, not a socket

> Short name for [capture_attribute](domain.md#capture_attribute)

``` python
with GeoNodes("Capture Attribute"):
    # Capture attributes
    node = mesh.points.captures(attr1 = attr1, attr2=attr2)
    captured_attr1 = node.attr1
    captured_attr2 = node.attr2

    # Capture one attribute
    captured_attr3 = mesh.points.capture(attr3)
```

#### Arguments:
- **attributes** (_Sockets_) : named attributes to capture



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)



> Short name for [delete_geometry](domain.md#delete_geometry)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **mode** (_str_ = ALL) : Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### delete_all()

> method

``` python
delete_all()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html), mode = 'ALL'



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### delete_edges_and_faces()

> method

``` python
delete_edges_and_faces()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html), mode = 'EDGE_FACE'



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### delete_faces()

> method

``` python
delete_faces()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html), mode = 'ONLY_FACE'



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)



> You can use short name [delete](domain.md#delete)

- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Arguments:
- **mode** (_str_ = ALL) : Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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

    cube.faces.extrude(nd.normal, .5)
    cube.faces[cube.top_].extrude(offset_scale=0)

    # Next cube extrusion will change top_
    top = cube.top_

    cube.faces[top].scale(scale=.8, uniform=False)
    cube.faces[top].scale(scale=.6, uniform=True)
    cube.faces[top].extrude(offset_scale=.5)
    cube.faces[cube.top_].flip()

    cube.out()
```

#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (Offset Scale)
- **individual** (_Boolean_ = None) : socket 'Individual' (Individual)



#### Returns:
- **Geometry** : self

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
__init__(geometry)
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
- **geometry**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### replace_material()

> method

``` python
replace_material(old=None, new=None)
```

> Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)



#### Arguments:
- **old** (_Material_ = None) : socket 'Old' (Old)
- **new** (_Material_ = None) : socket 'New' (New)



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

> Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html)



> [!NOTE]
> Use **peer socket** convention to get the inverted socket

``` python
mesh = Mesh.Cube()
selected = mesh.points.separate()
inverted = selected.inverted_
```

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

> Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)



#### Arguments:
- **id** (_Integer_ = None) : socket 'ID' (ID)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

> Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### store()

> method

``` python
store(name, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)



> Short name of [store_named_attribute](domain.md#store_named_attribute)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

> [!NOTE]
> Use constructor method [Named](attribute.md#named) to read stored attributes

``` python
mesh = Mesh.Cube()
mesh.points.store("An Integer", 123)
i = Integer.Named("An Integer")
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)



> You can use short name [store](domain.md#store)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
- domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

> [!NOTE]
> Use constructor method [NamedAttribute](attribute.md#namedattribute) to read stored attributes

``` python
mesh = Mesh.Cube()
mesh.points.store_named_attribute("An Integer", 123)
i = Integer.NamedAttribute("An Integer")
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)
- **value** (_Float_ = None) : socket 'Value' (Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

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
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Arguments:
- **value** (_Socket_ = None) : value to view

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Domain](domain.md#domain) :black_small_square: [Content](domain.md#content) :black_small_square: [Methods](domain.md#methods)</sub>