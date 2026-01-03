# ZoneIterator

``` python
ZoneIterator(socket: geonodes.core.nodeclass.Socket, node: geonodes.core.nodeclass.Node)
```

Wrap the nodes creation within a zone.

The ZoneIterator wraps a pair of nodes forming a zone : Simulation, Repeat, For Each, Closure.

The iteration contains exactly one iteration in order to generate the nodes only once.

The first call to __next__ method pushes the input and output nodes in order to capture inputs and outputs.
The second call pops the i/o capture and raises StopIteration.

The iterator returns itself as it exposes the nodes sockets:
- During the iteration, the input sockets are the ones of the output node and the output sockets are
  the ones of the input node.
- Outside the iteration, the input sockets are the ones of the input node and the output sockets are
  the ones of the output node.

``` python
geo = Geometry()
for sim in geo.simulation(A=1.0):
    
    # Output sockets come from input node
    a = sim.a

    # Sockets creation is captured
    # A new simulation socket named B is created
    b = Float(2.0, name="B")

    # Input sockets come from output node
    sim.a = a + b

    # Output is captured
    sim.b = a - b
    
    # No socket C was created
    try:
        sim.c = 0
    except AttributeError:
        print("An error is raised when accessing a non existing socket")

    # Within the loop, geo socket comes from input node
    # 
    geo.position += a

    # Default output geometry is in output node
    geo.out()

# Outside the loop, geometry is now the output node output geometry
# The zone output sockets can be accessed from simulation
geo.position += sim.a

geo.out()
```

#### Arguments:
- **socket** (_Socket_) : the socket to loop on
- **node** (_Node_) : a valid zone output node

### Inherited

['_done' not found]() :black_small_square: ['_input_node' not found]() :black_small_square: ['_in_zone' not found]() :black_small_square: [\_name](core-socket.md#_name) :black_small_square: ['_output_node' not found]() :black_small_square: ['_socket' not found]() :black_small_square:

## Content

- [\_\_init__](zoneiterator.md#__init__)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(socket: geonodes.core.nodeclass.Socket, node: geonodes.core.nodeclass.Node)
```

Wrap the nodes creation within a zone.

The ZoneIterator wraps a pair of nodes forming a zone : Simulation, Repeat, For Each, Closure.

The iteration contains exactly one iteration in order to generate the nodes only once.

The first call to __next__ method pushes the input and output nodes in order to capture inputs and outputs.
The second call pops the i/o capture and raises StopIteration.

The iterator returns itself as it exposes the nodes sockets:
- During the iteration, the input sockets are the ones of the output node and the output sockets are
  the ones of the input node.
- Outside the iteration, the input sockets are the ones of the input node and the output sockets are
  the ones of the output node.

``` python
geo = Geometry()
for sim in geo.simulation(A=1.0):
    
    # Output sockets come from input node
    a = sim.a

    # Sockets creation is captured
    # A new simulation socket named B is created
    b = Float(2.0, name="B")

    # Input sockets come from output node
    sim.a = a + b

    # Output is captured
    sim.b = a - b
    
    # No socket C was created
    try:
        sim.c = 0
    except AttributeError:
        print("An error is raised when accessing a non existing socket")

    # Within the loop, geo socket comes from input node
    # 
    geo.position += a

    # Default output geometry is in output node
    geo.out()

# Outside the loop, geometry is now the output node output geometry
# The zone output sockets can be accessed from simulation
geo.position += sim.a

geo.out()
```

#### Arguments:
- **socket** (_Socket_) : the socket to loop on
- **node** (_Node_) : a valid zone output node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ZoneIterator](zoneiterator.md#zoneiterator) :black_small_square: [Content](zoneiterator.md#content) :black_small_square: [Methods](zoneiterator.md#methods)</sub>