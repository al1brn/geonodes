# Closure

``` python
Closure(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Closure Socket.

A Closure is defined as a Tree within a `with` context:

``` python
with Closure() as c:
    # Create a closure input socket
    pi = Float(3.14, "Pi")
    # Create a closure output socket
    pi.out("Pi")
````

The Closure can be then evaluated using `evaluate` method. This method requires a Signature. The
Signature can be read from an existing Closure or created manually as a couple of dicts.


``` python
with GeoNodes("Closure Test") as tree:
    
    Geometry().out()
    
    with Layout("First closure"):
    
        with Closure() as cl:
            g = Mesh()
            g.points.store(String("Pi Attr", name="Attr Name"), Float(3.14, "Float Attribute"))
            
            (Integer(2, "Two") + Integer(2, "Two")).out("Four")
            
            cloud = g.faces.distribute_points()
            cloud.node.link_inputs(None, "Cloud")
            cloud.node.link_outputs(None, "Cloud")

            g.out()
            cloud.out("Points")
            
    with Layout("Direct evaluation"):
        cl.evaluate().out(panel="First closure")
        
    cl.out("First Closure")
        
    # Get the first signature
    sig1 = cl.get_signature()
        
    with Layout("Second Closure"):
        cl = Closure()
        
        with cl:
            spiral = Curve.Spiral(resolution=Integer(name="Resolution"))
            spiral.out("Spiral")
            
        with cl:
            spiral.to_mesh(profile_curve=Curve(name="Profile")).out("Mesh")
            
    cl.out("Second Closure")
    
    # Get the second signature
    sig2 = cl.get_signature()
    
    with Layout("Evaluate with signatures"):
        
        cl1 = Closure(name="Closure 1")
        cl2 = Closure(name="Closure 2")
        
        # Using evaluate method
        cl1.evaluate(signature=sig1).node.out(panel="Closure 1 out")

        # Using calling methjod
        cl2(signature=sig2).node.out(panel="Closure 2 out")

    # Manual signature
    with Closure() as cl3:
        pi = Float(3.14, "Pi")
        fac = Integer(2, "Multiplicator")
        (fac*pi).out("Tau")

    cl3.evaluate(signature=({'Pi': Float, 'Multiplicator': Integer}, {'Tau': Float})).out("Manual Signature")
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [\_create_input_socket](closure.md#_create_input_socket)
- [enable_output](closure.md#enable_output)
- [evaluate](closure.md#evaluate)
- [get_signature](closure.md#get_signature)

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