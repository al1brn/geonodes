# GreasePencil

> Bases classes: [Geometry](geometry.md#geometry)

``` python
GreasePencil(value=None, name=None, tip=None)
```

> Grease Pencil Geometry

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geometry.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [blur](socket.md#blur) :black_small_square: [bounding_box](geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](geometry.md#convex_hull) :black_small_square: [curve](geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geo](geometry.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [grease_pencil](geometry.md#grease_pencil) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [id](geobase.md#id) :black_small_square: [index_of_nearest](geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](geometry.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instances](geometry.md#instances) :black_small_square: [Join](geometry.md#join) :black_small_square: [join](geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge_by_distance](geometry.md#merge_by_distance) :black_small_square: [mesh](geometry.md#mesh) :black_small_square: [name](geometry.md#name) :black_small_square: [\_node](geometry.md#_node) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](geobase.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [point_cloud](geometry.md#point_cloud) :black_small_square: [position](geobase.md#position) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](geometry.md#raycast) :black_small_square: [remove_named_attribute](geometry.md#remove_named_attribute) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](geometry.md#separate_components) :black_small_square: [set_id](geometry.md#set_id) :black_small_square: [set_material](geometry.md#set_material) :black_small_square: [set_name](geometry.md#set_name) :black_small_square: [set_position](geometry.md#set_position) :black_small_square: [set_shade_smooth](geometry.md#set_shade_smooth) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](geometry.md#to_instance) :black_small_square: [transform](geometry.md#transform) :black_small_square: [viewer](geometry.md#viewer) :black_small_square: [volume](geometry.md#volume) :black_small_square:

## Content

- [domain_size](greasepencil.md#domain_size)
- [FromCurve](greasepencil.md#fromcurve)
- [layers](greasepencil.md#layers)
- [merge_layers](greasepencil.md#merge_layers)
- [merge_layers_by_group_id](greasepencil.md#merge_layers_by_group_id)
- [merge_layers_by_name](greasepencil.md#merge_layers_by_name)
- [to_curves](greasepencil.md#to_curves)

## Properties



### domain_size

> _type_: **Node**
>

> Node ERROR: Node 'Size' not found, component = 'GREASEPENCIL'

:warning: returns the **node**, not a socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Properties](greasepencil.md#properties)</sub>

### layers

> _type_: **Layer**
>

LAYER domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Properties](greasepencil.md#properties)</sub>

## Methods



----------
### FromCurve()

> classmethod

``` python
FromCurve(curves=None, selection=None, instances_as_layers=True)
```

> Constructor node [Curves to Grease Pencil](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curves_to_grease_pencil.html)

#### Arguments:
- **curves** (_Geometry_ = None) : socket 'Curves' (Curves)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **instances_as_layers** (_Boolean_ = True) : socket 'Instances as Layers' (Instances as Layers)



#### Returns:
- **GreasePencil** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Methods](greasepencil.md#methods)</sub>

----------
### merge_layers()

> method

``` python
merge_layers(mode='MERGE_BY_NAME')
```

> Node [Merge Layers](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/merge_layers.html)



#### Arguments:
- **mode** (_str_ = MERGE_BY_NAME) : Node.mode in ('MERGE_BY_NAME', 'MERGE_BY_ID')



#### Returns:
- **Grease** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Methods](greasepencil.md#methods)</sub>

----------
### merge_layers_by_group_id()

> method

``` python
merge_layers_by_group_id()
```

> Node [Merge Layers](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/merge_layers.html)



#### Returns:
- **Grease** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Methods](greasepencil.md#methods)</sub>

----------
### merge_layers_by_name()

> method

``` python
merge_layers_by_name()
```

> Node [Merge Layers](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/merge_layers.html)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Methods](greasepencil.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(layers_as_instances=None)
```

Node 'Grease Pencil to Curves' (GeometryNodeGreasePencilToCurves)

[Grease Pencil to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/grease_pencil_to_curves.html)

#### Arguments:
- **layers_as_instances** (_Boolean_ = None) : socket 'Layers as Instances' (Layers as Instances)



#### Returns:
- **curves** (_Curve_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GreasePencil](greasepencil.md#greasepencil) :black_small_square: [Content](greasepencil.md#content) :black_small_square: [Methods](greasepencil.md#methods)</sub>