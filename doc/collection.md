# Collection

``` python
Collection(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Collection Socket.

The Collection can be read from bpy.data.collections or passed with its name.

``` python
import bpy
from geonodes import GeoNodes, Collection, nd

for c in "ABC":
    test_name = f"Test Coll {c}"
    coll = bpy.data.collections.get(test_name)
    if coll is None:
        coll = bpy.data.collections.new(test_name)
        bpy.context.collection.children.link(coll)

with GeoNodes("Collection Test"):

    g = Collection("Test Coll A").info(transform_space='RELATIVE')
    g += Collection(name="From Input'").info(separate_children=True, reset_children=True)
    g += nd.collection_info("Test Coll B")
    g += nd.collection_info(bpy.data.collections["Test Coll C"])

    g.out()
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](closure.md#_pop) :black_small_square: [\_push](closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [\_create_input_socket](collection.md#_create_input_socket)
- [enable_output](collection.md#enable_output)
- [info](collection.md#info)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = None, name: 'str' = 'Collection', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Collection Input

New [Collection](collection.md#collection) input with subtype 'NONE'.

Aguments
--------
- value  (object = None) : Default value
- name  (str = 'Collection') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **value** (_object_ = None)
- **name** (_str_ = Collection)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Collection** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Content](collection.md#content) :black_small_square: [Methods](collection.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COLLECTION'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Collection** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Content](collection.md#content) :black_small_square: [Methods](collection.md#methods)</sub>

----------
### info()

> method

``` python
info(separate_children: 'Boolean' = None, reset_children: 'Boolean' = None, transform_space: "Literal['ORIGINAL', 'RELATIVE']" = 'ORIGINAL')
```

> Node [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/collection_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **separate_children** (_Boolean_ = None) : socket 'Separate Children' (id: Separate Children)
- **reset_children** (_Boolean_ = None) : socket 'Reset Children' (id: Reset Children)
- **transform_space** (_Literal['ORIGINAL', 'RELATIVE']_ = ORIGINAL) : parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Content](collection.md#content) :black_small_square: [Methods](collection.md#methods)</sub>