# SplinePoint

> Bases classes: [Point](geono-point.md#point)

``` python
SplinePoint(geometry)
```

> Point domain of a [Curve](geono-curve.md#curve)

Methods of **SplinePoint** class are nodes which accept 'POINT' domain.

In addition, the nodes [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html) and ERROR: Node 'Point in Curve' not found are implemented
in methods [curve_index](macro-geono-splinepoint.md#curve_index), [index_in_curve](macro-geono-splinepoint.md#index_in_curve) and [offset_in_curve](macro-geono-splinepoint.md#offset_in_curve).

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [capture](geono-domain.md#capture) :black_small_square: [capture_attribute](geono-domain.md#capture_attribute) :black_small_square: [captures](geono-domain.md#captures) :black_small_square: [count](geono-point.md#count) :black_small_square: [delete](geono-domain.md#delete) :black_small_square: [delete_all](geono-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-domain.md#delete_geometry) :black_small_square: [domain_name](geono-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-domain.md#exclude_corner) :black_small_square: [extrude](geono-domain.md#extrude) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [instance_on](geono-point.md#instance_on) :black_small_square: [\_jump](geono-domain.md#_jump) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [\_node](geono-domain.md#_node) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [plural_domain](geono-domain.md#plural_domain) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [proximity](geono-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-domain.md#restrict_domain) :black_small_square: [sample_index](geono-domain.md#sample_index) :black_small_square: [sample_nearest](geono-domain.md#sample_nearest) :black_small_square: [\_sel](geono-domain.md#_sel) :black_small_square: [separate](geono-domain.md#separate) :black_small_square: [set_id](geono-geobase.md#set_id) :black_small_square: [set_position](geono-geobase.md#set_position) :black_small_square: [sort_elements](geono-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-domain.md#split_to_instances) :black_small_square: [store](geono-domain.md#store) :black_small_square: [store_named_attribute](geono-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-domain.md#__str__) :black_small_square: [to_points](geono-domain.md#to_points) :black_small_square: [viewer](geono-domain.md#viewer) :black_small_square:

## Content

- **C** : [curve_index](macro-geono-splinepoint.md#curve_index)
- **H** : [handle_align](macro-geono-splinepoint.md#handle_align) :black_small_square: [handle_auto](macro-geono-splinepoint.md#handle_auto) :black_small_square: [handle_free](macro-geono-splinepoint.md#handle_free) :black_small_square: [handle_positions](macro-geono-splinepoint.md#handle_positions) :black_small_square: [handle_type](macro-geono-splinepoint.md#handle_type) :black_small_square: [handle_type_selection](macro-geono-splinepoint.md#handle_type_selection) :black_small_square: [handle_vector](macro-geono-splinepoint.md#handle_vector)
- **I** : [index_in_curve](macro-geono-splinepoint.md#index_in_curve)
- **L** : [left_handle_align](macro-geono-splinepoint.md#left_handle_align) :black_small_square: [left_handle_auto](macro-geono-splinepoint.md#left_handle_auto) :black_small_square: [left_handle_free](macro-geono-splinepoint.md#left_handle_free) :black_small_square: [left_handle_offset](macro-geono-splinepoint.md#left_handle_offset) :black_small_square: [left_handle_position](macro-geono-splinepoint.md#left_handle_position) :black_small_square: [left_handle_type](macro-geono-splinepoint.md#left_handle_type) :black_small_square: [left_handle_vector](macro-geono-splinepoint.md#left_handle_vector)
- **O** : [offset_in_curve](macro-geono-splinepoint.md#offset_in_curve)
- **R** : [right_handle_align](macro-geono-splinepoint.md#right_handle_align) :black_small_square: [right_handle_auto](macro-geono-splinepoint.md#right_handle_auto) :black_small_square: [right_handle_free](macro-geono-splinepoint.md#right_handle_free) :black_small_square: [right_handle_offset](macro-geono-splinepoint.md#right_handle_offset) :black_small_square: [right_handle_position](macro-geono-splinepoint.md#right_handle_position) :black_small_square: [right_handle_type](macro-geono-splinepoint.md#right_handle_type) :black_small_square: [right_handle_vector](macro-geono-splinepoint.md#right_handle_vector)
- **S** : [set_handle_positions](macro-geono-splinepoint.md#set_handle_positions) :black_small_square: [set_handle_type](macro-geono-splinepoint.md#set_handle_type)

## Properties



### handle_align

> _type_: **Boolean**
>

> Handle align property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'ALIGN'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### handle_auto

> _type_: **Boolean**
>

> Handle auto property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'AUTO'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### handle_free

> _type_: **Boolean**
>

> Handle free property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'FREE'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### handle_type

> _type_: **Error**
>

> Handle type write only property

Set the curve handle type

``` python
curve.handle_type = 'FREE'
```

- getter : None, write only Property
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### handle_vector

> _type_: **Boolean**
>

> Handle vector property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'VECTOR'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_align

> _type_: **Boolean**
>

> Left handle auto property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'ALIGN'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_auto

> _type_: **Boolean**
>

> Left handle auto property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'AUTO'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_free

> _type_: **Boolean**
>

> Left handle free property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'FREE'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_offset

> _type_: **Vector**
>

> Left handle offset property

- getter : socket 'Left' of node ERROR: Node 'Handle Positions' not found, relative
- setter : node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_position

> _type_: **Vector**
>

> Left handle property

- getter : socket 'Left' of node ERROR: Node 'Handle Positions' not found
- setter : node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_type

> _type_: **Error**
>

> Left handle type write only property

Set the curve handle type

- getter : None, write only Property
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### left_handle_vector

> _type_: **Boolean**
>

> Left handle vector property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'VECTOR'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_align

> _type_: **Boolean**
>

> Right handle align property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'ALIGN'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_auto

> _type_: **Boolean**
>

> Right handle auto property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'AUTO'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_free

> _type_: **Boolean**
>

> Right handle free property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'FREE'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_offset

> _type_: **Vector**
>

> Right handle offset property

- getter : socket 'Right' of node ERROR: Node 'Handle Positions' not found, relative
- setter : node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_position

> _type_: **Vector**
>

> Right handle position property

- getter : socket 'Right' of node ERROR: Node 'Handle Positions' not found
- setter : node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_type

> _type_: **Error**
>

> Right handle type write only property

Set the curve handle type

- getter : None, write only Property
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

### right_handle_vector

> _type_: **Boolean**
>

> Right handle vector property

- getter : node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)
- setter : node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html), **handle_type** = 'VECTOR'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Properties](macro-geono-splinepoint.md#properties)</sub>

## Methods



----------
### curve_index()

> method

``` python
curve_index(point_index=None)
```

> Socket 'Curve Index' of node ERROR: Node 'of Point' not found

#### Arguments:
- **point_index** (_Integer_ = None) : point index



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>

----------
### handle_positions()

> classmethod

``` python
handle_positions(relative=None)
```

> Node ERROR: Node 'Curve Handle Positions' not found

#### Arguments:
- **relative** (_Boolean_ = None) : socket 'Relative' (Relative)



#### Returns:
- **Node** : 'Curve Handle Positions' node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>

----------
### handle_type_selection()

> classmethod

``` python
handle_type_selection(left=True, right=True, handle_type='AUTO')
```

> Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)

#### Arguments:
- **left** (_bool_ = True) : left handle
- **right** (_bool_ = True) : right handle
- **handle_type** (_str_ = AUTO) : Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>

----------
### index_in_curve()

> method

``` python
index_in_curve(point_index=None)
```

> Socket 'Index in Curve' of node ERROR: Node 'of Point' not found

#### Arguments:
- **point_index** (_Integer_ = None) : point index



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>

----------
### offset_in_curve()

> method

``` python
offset_in_curve(point_index=None, offset=None)
```

> Socket 'Point Index' of node ERROR: Node 'Point in Curve' not found

#### Arguments:
- **point_index** ( = None)
- **offset** ( = None)



#### Returns:
- **Integer** : spline index

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>

----------
### set_handle_positions()

> method

``` python
set_handle_positions(position=None, offset=None, mode=None)
```

> Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)



``` python
with GeoNodes("Curve handles"):
    curve = Curve.Line(0, (20, 0, 0)).resample(20)

    curve.splines.type = 'BEZIER'

    with Layout("Set by str"):
        curve.points.left_handle_type = 'AUTO'
        curve.points.right_handle_type = 'AUTO'
        curve.points[(nd.index % 2).equal(0)].handle_type = 'ALIGN'

        curve.points[curve.points.handle_align].offset = (0, 0, 2)

    with Layout("Both set boolean"):
        curve.points[1].handle_auto = True
        curve.points[3].handle_free = True
        curve.points[5].handle_vector = True
        curve.points[7].handle_align = True

    with Layout("Left / right set boolean"):
        curve.points[9].left_handle_auto = True
        curve.points[9].right_handle_free = True
        curve.points[11].left_handle_free = True
        curve.points[11].right_handle_vector = True
        curve.points[13].left_handle_vector = True
        curve.points[13].right_handle_align = True
        curve.points[15].left_handle_align = True
        curve.points[15].right_handle_auto = True

    with Layout("Left selection"):
        curve.points[curve.points.left_handle_auto].offset = (0, 0.5, 0)
        curve.points[curve.points.left_handle_free].offset = (0, 1.0, 0)
        curve.points[curve.points.left_handle_vector].offset = (0, 1.5, 0)
        curve.points[curve.points.left_handle_align].offset = (0, 2.0, 0)

    with Layout("Right selection"):
        curve.points[curve.points.right_handle_auto].offset = (0, 0, 0.5)
        curve.points[curve.points.right_handle_free].offset = (0, 0, 1.0)
        curve.points[curve.points.right_handle_vector].offset = (0, 0, 1.5)
        curve.points[curve.points.right_handle_align].offset = (0, 0, 2.0)

    with Layout("Moving handles"):
        curve.points[curve.points.left_handle_free].left_handle_position = (5, 0, 0)
        curve.points[curve.points.right_handle_free].right_handle_position = (-5, 0, 0)

        curve.points[curve.points.left_handle_vector].left_handle_offset = (0, 5, 0)
        curve.points[curve.points.right_handle_vector].right_handle_offset = (0, -5, 0)

    curve.out()
```

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **mode** (_str_ = None) : Node.mode in ('LEFT', 'RIGHT')



#### Returns:
- **Curve** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>

----------
### set_handle_type()

> method

``` python
set_handle_type(left=True, right=True, handle_type='AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)



``` python
with GeoNodes("Curve handles"):
    curve = Curve.Line(0, (20, 0, 0)).resample(20)

    curve.splines.type = 'BEZIER'

    with Layout("Set by str"):
        curve.points.left_handle_type = 'AUTO'
        curve.points.right_handle_type = 'AUTO'
        curve.points[(nd.index % 2).equal(0)].handle_type = 'ALIGN'

        curve.points[curve.points.handle_align].offset = (0, 0, 2)

    with Layout("Both set boolean"):
        curve.points[1].handle_auto = True
        curve.points[3].handle_free = True
        curve.points[5].handle_vector = True
        curve.points[7].handle_align = True

    with Layout("Left / right set boolean"):
        curve.points[9].left_handle_auto = True
        curve.points[9].right_handle_free = True
        curve.points[11].left_handle_free = True
        curve.points[11].right_handle_vector = True
        curve.points[13].left_handle_vector = True
        curve.points[13].right_handle_align = True
        curve.points[15].left_handle_align = True
        curve.points[15].right_handle_auto = True

    with Layout("Left selection"):
        curve.points[curve.points.left_handle_auto].offset = (0, 0.5, 0)
        curve.points[curve.points.left_handle_free].offset = (0, 1.0, 0)
        curve.points[curve.points.left_handle_vector].offset = (0, 1.5, 0)
        curve.points[curve.points.left_handle_align].offset = (0, 2.0, 0)

    with Layout("Right selection"):
        curve.points[curve.points.right_handle_auto].offset = (0, 0, 0.5)
        curve.points[curve.points.right_handle_free].offset = (0, 0, 1.0)
        curve.points[curve.points.right_handle_vector].offset = (0, 0, 1.5)
        curve.points[curve.points.right_handle_align].offset = (0, 0, 2.0)

    with Layout("Moving handles"):
        curve.points[curve.points.left_handle_free].left_handle_position = (5, 0, 0)
        curve.points[curve.points.right_handle_free].right_handle_position = (-5, 0, 0)

        curve.points[curve.points.left_handle_vector].left_handle_offset = (0, 5, 0)
        curve.points[curve.points.right_handle_vector].right_handle_offset = (0, -5, 0)

    curve.out()
```

#### Arguments:
- **left** (_bool_ = True) : left handle
- **right** (_bool_ = True) : right handle
- **handle_type** (_str_ = AUTO) : Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')



#### Returns:
- **Curve** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](macro-geono-splinepoint.md#splinepoint) :black_small_square: [Content](macro-geono-splinepoint.md#content) :black_small_square: [Methods](macro-geono-splinepoint.md#methods)</sub>