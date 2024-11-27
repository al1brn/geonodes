# Instances

> Bases classes: [Geometry](geometry.md#geometry)

``` python
Instances(value=None, name=None, tip=None)
```

> Instances Geometry

> [!NOTE]
> The name of geometry class is plural : **Instances** when the name of the
> domain is singular : [Instance](instance.md#instance). The named of the domain property is [insts](instances.md#insts).

The **Instances** class exposes all methods specific to instances.
Since there is no ambiguity, the word **instances** is omitted in the name of
the methods:

``` python
realized = instances.realize() # Node 'Realize Instances'
```
Nodes requiring a domain parameter, are implemented in the domain [insts](instances.md#insts).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geometry.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [blur](socket.md#blur) :black_small_square: [bounding_box](geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](geometry.md#convex_hull) :black_small_square: [curve](geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geo](geometry.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [grease_pencil](geometry.md#grease_pencil) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [id](geobase.md#id) :black_small_square: [index_of_nearest](geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](geometry.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instances](geometry.md#instances) :black_small_square: [Join](geometry.md#join) :black_small_square: [join](geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge_by_distance](geometry.md#merge_by_distance) :black_small_square: [mesh](geometry.md#mesh) :black_small_square: [name](geometry.md#name) :black_small_square: [\_node](geometry.md#_node) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](geobase.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [point_cloud](geometry.md#point_cloud) :black_small_square: [position](geobase.md#position) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](geometry.md#raycast) :black_small_square: [remove_named_attribute](geometry.md#remove_named_attribute) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](geometry.md#separate_components) :black_small_square: [set_id](geometry.md#set_id) :black_small_square: [set_material](geometry.md#set_material) :black_small_square: [set_name](geometry.md#set_name) :black_small_square: [set_position](geometry.md#set_position) :black_small_square: [set_shade_smooth](geometry.md#set_shade_smooth) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](geometry.md#to_instance) :black_small_square: [transform](geometry.md#transform) :black_small_square: [viewer](geometry.md#viewer) :black_small_square: [volume](geometry.md#volume) :black_small_square:

## Content

- **D** : [domain_size](instances.md#domain_size)
- **F** : [FromGeometry](instances.md#fromgeometry) :black_small_square: [FromString](instances.md#fromstring)
- **I** : [ImportPLY](instances.md#importply) :black_small_square: [insts](instances.md#insts)
- **O** : [on_points](instances.md#on_points)
- **R** : [realize](instances.md#realize) :black_small_square: [rotate](instances.md#rotate)
- **S** : [scale](instances.md#scale)
- **T** : [to_grease_pencil](instances.md#to_grease_pencil) :black_small_square: [to_points](instances.md#to_points) :black_small_square: [translate](instances.md#translate)

## Properties



### domain_size

> _type_: **Node**
>

> Node ERROR: Node 'Size' not found, component = 'INSTANCES'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Properties](instances.md#properties)</sub>

### insts

> _type_: **Instance**
>

INSTANCES domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Properties](instances.md#properties)</sub>

## Methods



----------
### FromGeometry()

> classmethod

``` python
FromGeometry(*geometries)
```

> Constructor node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)

#### Arguments:
- **geometries** (_Geometry_) : socket 'Geometry' (Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### FromString()

> classmethod

``` python
FromString(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT')
```

> Constructor node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html)

#### Arguments:
- **string** (_String_ = None) : socket 'String' (String)
- **size** (_Float_ = None) : socket 'Size' (Size)
- **character_spacing** (_Float_ = None) : socket 'Character Spacing' (Character Spacing)
- **word_spacing** (_Float_ = None) : socket 'Word Spacing' (Word Spacing)
- **line_spacing** (_Float_ = None) : socket 'Line Spacing' (Line Spacing)
- **text_box_width** (_Float_ = None) : socket 'Text Box Width' (Text Box Width)
- **text_box_height** (_Float_ = None) : socket 'Text Box Height' (Text Box Height)
- **overflow** (_str_ = OVERFLOW) : Node.overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- **align_x** (_str_ = LEFT) : Node.align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- **align_y** (_str_ = TOP_BASELINE) : Node.align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- **pivot_mode** (_str_ = BOTTOM_LEFT) : Node.pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### ImportPLY()

> classmethod

``` python
ImportPLY(path=None)
```

> Node ERROR: Node 'Import PLY' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (Path)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### on_points()

> method

``` python
on_points(points, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

> Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)



#### Arguments:
- **points** (_Geometry_) : socket 'Points' (Instance)
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Instances** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### realize()

> method

``` python
realize(realize_all=None, depth=None)
```

> Node [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)



#### Arguments:
- **realize_all** (_Boolean_ = None) : socket 'Realize All' (Realize All)
- **depth** (_Integer_ = None) : socket 'Depth' (Depth)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotation=None, pivot_point=None, local_space=None)
```

> Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)



#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **pivot_point** (_Vector_ = None) : socket 'Pivot Point' (Pivot Point)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None, center=None, local_space=None)
```

> Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)



#### Arguments:
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### to_grease_pencil()

> method

``` python
to_grease_pencil(instances_as_layers=None)
```

Node 'Curves to Grease Pencil' (GeometryNodeCurvesToGreasePencil)

[Curves to Grease Pencil](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curves_to_grease_pencil.html)

#### Arguments:
- **instances_as_layers** (_Boolean_ = None) : socket 'Instances as Layers' (Instances as Layers)



#### Returns:
- **grease_pencil** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
```

> Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Points** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### translate()

> method

``` python
translate(translation=None, local_space=None)
```

> Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>