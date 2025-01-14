# Object

``` python
Object(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
```

Class Object data socket

#### Arguments:
- **value** (_bpy.types.Object or str_ = None) : object or object name in bpy.data.objects
- **name** (_str_ = None) : create a group input socket of type Object if not None
- **tip** (_str_ = None) : user tip for group input socket
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- [ActiveCamera](object.md#activecamera)
- [info](object.md#info)
- [\_\_init__](object.md#__init__)
- [Self](object.md#self)

## Methods



----------
### ActiveCamera()

> classmethod

``` python
ActiveCamera()
```

> Node [Active Camera](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/active_camera.html)

#### Returns:
- **Object** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### info()

> method

``` python
info(as_instance=None, transform_space='ORIGINAL')
```

> Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/object_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **as_instance** (_Boolean_ = None) : socket 'As Instance' (id: As Instance)
- **transform_space** (_str_ = ORIGINAL) : parameter 'transform_space' in ('ORIGINAL', 'RELATIVE')



#### Returns:
- **node** (_Matrix_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
```

Class Object data socket

#### Arguments:
- **value** (_bpy.types.Object or str_ = None) : object or object name in bpy.data.objects
- **name** (_str_ = None) : create a group input socket of type Object if not None
- **tip** (_str_ = None) : user tip for group input socket
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### Self()

> classmethod

``` python
Self()
```

> Node [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/self_object.html)

#### Returns:
- **Object** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>