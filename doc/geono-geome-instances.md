# Instances

> Bases classes: [Geometry](geono-geome-geometry.md#geometry)

``` python
Instances(value=None, name=None, tip=None)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geono-geome-geometry.md#__add__) :black_small_square: [bake](geono-geome-geometry.md#bake) :black_small_square: [blur](geono-socke-socket.md#blur) :black_small_square: [bounding_box](geono-geome-geometry.md#bounding_box) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [convex_hull](geono-geome-geometry.md#convex_hull) :black_small_square: [curve](geono-geome-geometry.md#curve) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geo](geono-geome-geometry.md#_geo) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [index_of_nearest](geono-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [instances](geono-geome-geometry.md#instances) :black_small_square: [join](geono-geome-geometry.md#join) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [merge_by_distance](geono-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geome-geometry.md#mesh) :black_small_square: [\_node](geono-geome-geometry.md#_node) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [point_cloud](geono-geome-geometry.md#point_cloud) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [raycast](geono-geome-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geome-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [\_sel](geono-geome-geobase.md#_sel) :black_small_square: [separate_components](geono-geome-geometry.md#separate_components) :black_small_square: [set_id](geono-geome-geometry.md#set_id) :black_small_square: [set_material](geono-geome-geometry.md#set_material) :black_small_square: [set_position](geono-geome-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geome-geometry.md#set_shade_smooth) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_instance](geono-geome-geometry.md#to_instance) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square: [transform](geono-geome-geometry.md#transform) :black_small_square: [viewer](geono-geome-geometry.md#viewer) :black_small_square: [volume](geono-geome-geometry.md#volume) :black_small_square:

## Content

- [FromGeometry](geono-geome-instances.md#fromgeometry)
- [FromString](geono-geome-instances.md#fromstring)
- [on_points](geono-geome-instances.md#on_points)
- [realize](geono-geome-instances.md#realize)
- [rotate](geono-geome-instances.md#rotate)
- [scale](geono-geome-instances.md#scale)
- [to_points](geono-geome-instances.md#to_points)
- [translate](geono-geome-instances.md#translate)

## Methods



----------
### FromGeometry()

> classmethod

``` python
FromGeometry(*geometries)
```

Node 'Geometry to Instance' (GeometryNodeGeometryToInstance)

[!Node] Geometry to Instance

#### Arguments:
- **geometries** (_Geometry_) : socket 'Geometry' (Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### FromString()

> classmethod

``` python
FromString(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT')
```

Node 'String to Curves' (GeometryNodeStringToCurves)

[!Node] String to Curves

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### on_points()

> method

``` python
on_points(points, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

Node 'Instance on Points' (GeometryNodeInstanceOnPoints)

[!Node] Instance on Points

#### Arguments:
- **points**
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### realize()

> method

``` python
realize(realize_all=None, depth=None)
```

Node 'Realize Instances' (GeometryNodeRealizeInstances)

[!Node] Realize Instances

#### Arguments:
- **realize_all** (_Boolean_ = None) : socket 'Realize All' (Realize All)
- **depth** (_Integer_ = None) : socket 'Depth' (Depth)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotation=None, pivot_point=None, local_space=None)
```

Node 'Rotate Instances' (GeometryNodeRotateInstances)

[!Node] Rotate Instances

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **pivot_point** (_Vector_ = None) : socket 'Pivot Point' (Pivot Point)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None, center=None, local_space=None)
```

Node 'Scale Instances' (GeometryNodeScaleInstances)

[!Node] Scale Instances

#### Arguments:
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
```

Node 'Instances to Points' (GeometryNodeInstancesToPoints)

[!Node] Instances to Points

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Points** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>

----------
### translate()

> method

``` python
translate(translation=None, local_space=None)
```

Node 'Translate Instances' (GeometryNodeTranslateInstances)

[!Node] Translate Instances

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](geono-geome-instances.md#instances) :black_small_square: [Content](geono-geome-instances.md#content) :black_small_square: [Methods](geono-geome-instances.md#methods)</sub>