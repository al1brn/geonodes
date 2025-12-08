# Closure

``` python
Closure(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False)
```

Socket of type Closure

#### Arguments:
- **value** (_Socket_ = None) : Default value
- **name** (_str_ = None) : Input socket name
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_classes_test](core-socke-socket.md#_classes_test) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_from](core-socke-socket.md#link_from) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: ['_socket_type' not found]() :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [\_create_input_socket](closure.md#_create_input_socket)
- [enable_output](closure.md#enable_output)
- [evaluate](closure.md#evaluate)
- [get_signature](closure.md#get_signature)
- [\_\_init__](closure.md#__init__)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Closure', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Closure Input

New [Closure](closure.md#closure) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Closure') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **name** (_str_ = Closure)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Closure** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Closure](closure.md#closure) :black_small_square: [Content](closure.md#content) :black_small_square: [Methods](closure.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CLOSURE'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Closure** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Closure](closure.md#closure) :black_small_square: [Content](closure.md#content) :black_small_square: [Methods](closure.md#methods)</sub>

----------
### evaluate()

> method

``` python
evaluate(named_sockets: dict = {}, signature: geonodes.core.signature.Signature = None, **sockets)
```

> Node ERROR: Node 'Closure Evaluate' not found

Evaluate the closure.

The closure signature can be read directly when the closure sockets comes from a Closure
zone. Otherwise, the signature argument must be defined.

``` python
with GeoNodes("Closure Evaluation"):
    
    # ----- Evaluation from a Closure zone
    
    with Closure() as cl:
        cube = Mesh.Cube(size=cl.new_input(), vertices_x=cl.new_input("Resolution"))
        cube.node.vertices_y = cl.input_node.resolution
        cube.node.vertices_z = cl.input_node.resolution
        cube.out("Cube")
        
    # Direct evalution: no signature required
    cl.evaluate(size=(1, 2, 3), resolution=5).out("First Closure")
    
    # ----- Evaluation with a closure signature
    
    # A closure is passed as Tree input argument
    closure = Closure(None, name="Other Closure")
    
    # The closure can be switched for instance
    closure = cl.switch(Boolean(False, "Use other"), closure)
    
    # Evaluation is made using the reference signature
    closure.evaluate(signature=cl.get_signature(), size=(10, 20, 30), resolution=10).out("Second Closure")
    
    # ----- Evaluation with any signature
    
    # A closure is passed as Tree input argument
    closure = Closure(None, name="IcoSphere Closure")
    
    # The signature is supposed to be the one of an ico sphere creation
    ico = Mesh.IcoSphere()
    
    # Evaluation with this node signature
    closure.evaluate(closure_signature=ico.node.get_signature(), radius=3.14).out("Third Closure")
```

#### Arguments:
- **named_sockets** (_dict_ = {}) : named sockets values
- **signature** (_Signature_ = None) : the evaluation signature
- **sockets** : socket values



#### Returns:
- **First** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Closure](closure.md#closure) :black_small_square: [Content](closure.md#content) :black_small_square: [Methods](closure.md#methods)</sub>

----------
### get_signature()

> method

``` python
get_signature(with_sockets: bool = False)
```

Build the closure signature of the zone.

Closure signature is the tuple (input_signature, output_signature)

#### Arguments:
- **with_sockets** (_bool_ = False) : include sockets



#### Returns:
- **Signature** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Closure](closure.md#closure) :black_small_square: [Content](closure.md#content) :black_small_square: [Methods](closure.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False)
```

Socket of type Closure

#### Arguments:
- **value** (_Socket_ = None) : Default value
- **name** (_str_ = None) : Input socket name
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Closure](closure.md#closure) :black_small_square: [Content](closure.md#content) :black_small_square: [Methods](closure.md#methods)</sub>