# Menu

``` python
Menu(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Menu Socket.

There are two main ways to create a Menu:
- In a single instruction using the constructor : `geo = Geometry.MenuSwitch(...)`
- Item per item using the `with` context : `with Geometry.MenuSwitch() as geo:`

One can prefer the second method when the items need a lot of instructions to be built.
Each context management creates a Layout.

``` python
# First way
item1 = Mesh.Cube()
item2 = Mesh.UVSphere()
item2 = Mesh.Cone()
geo = Geometry.MenuSwitch({'Cube': item1, 'Sphere': item2, 'Cone': item3})

# Second way
with Geometry.MenuSwitch() as geo:
    Mesh.Cube().out("Cube")
    Mesh.UVSphere().out("Sphere")
    Mesh.Cone().out("Cone")

# Or, to make the code clearer
# Cube construction
with Geometry.MenuSwitch() as geo:
    Mesh.Cube().out("Cube")

# Sphere construction
with geo:
    Mesh.UVSphere().out("Sphere")

# Cone construction
with geo:
    Mesh.Cone().out("Cone")

# Tree output socket

geo.out("Selected Geometry")
```

In general, the selection socket is linked to the group input. Use the `Input` virtual socket
to connect the Menu selector.


``` python
from geonodes import GeoNodes, Geometry, Mesh, Menu, Input, Curve

with GeoNodes("Menu Demo") as tree:
    
    # ----------------------------------------------------------------------------------------------------
    # First Menu
    # ----------------------------------------------------------------------------------------------------
    
    simple = Geometry().menu_switch("Input", {
        "Cube": Mesh.Cube(),
        "Ico": Mesh.IcoSphere(),
        "Cone": Mesh.Cone(), 
        },
        menu=Input("Simple Mesh", default="Ico"), 
        )

    # ----------------------------------------------------------------------------------------------------
    # Second Menu
    # ----------------------------------------------------------------------------------------------------
        
    profile = Curve.Circle(radius=.1)
        
    with Geometry.MenuSwitch() as from_curve:
        simple.out("Simple Mesh")
        
    with from_curve:
        Curve.Spiral().to_mesh(profile_curve=profile).out("Spiral")
        
    with from_curve:
        Curve.Circle().to_mesh(profile_curve=profile).out("Circle")
        
    from_curve.node.menu = Input("From Curve", default="Simple Mesh")
    
    # ----------------------------------------------------------------------------------------------------
    # Index Switch
    # ----------------------------------------------------------------------------------------------------
    
    curve = Curve.IndexSwitch(index=Input("Curve Index"))
    with curve:
        Curve.Spiral().out()
        
    with curve:
        Curve.Circle().out()
        
    with curve:
        Curve.Quadrilateral().out()
        
    # ----------------------------------------------------------------------------------------------------
    # Switch
    # ----------------------------------------------------------------------------------------------------
    
    curve.switch(Input("Mesh/Curve"), from_curve).out()
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](core-socke-socket.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [\_create_input_socket](menu.md#_create_input_socket)
- [enable_output](menu.md#enable_output)
- [menu_switch](menu.md#menu_switch)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = None, name: 'str' = 'Menu', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, expanded: 'bool' = False, shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Menu Input

New [Menu](menu.md#menu) input with subtype 'NONE'.

Aguments
--------
- value  (object = None) : Default value
- name  (str = 'Menu') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- expanded  (bool = False) : Property menu_expanded
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = None)
- **name** (_str_ = Menu)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **expanded** (_bool_ = False)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Menu** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Menu](menu.md#menu) :black_small_square: [Content](menu.md#content) :black_small_square: [Methods](menu.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MENU'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Menu** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Menu](menu.md#menu) :black_small_square: [Content](menu.md#content) :black_small_square: [Methods](menu.md#methods)</sub>

----------
### menu_switch()

> method

``` python
menu_switch(named_sockets: 'dict' = {}, **sockets)
```

> Node [Menu Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/menu_switch.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'a' type



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **Geometry** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Menu](menu.md#menu) :black_small_square: [Content](menu.md#content) :black_small_square: [Methods](menu.md#methods)</sub>