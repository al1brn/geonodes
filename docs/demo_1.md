# Demo script

> Let's review this demo script in detail. Afterwards, you should be able to script your own tree.

> [!NOTE]
> To start using this module, it is recommanded to read first [Getting Started](getting_started.md).

The script creates a surface from a grid by computing
`z = sin(d)/d` where `d=sqrt(x^2 + y^2)` is the distance of the vertex to the center.

## Module import

Import the tree classes `GeoNodes`,  `Shader` and/or `Compositor` from the module

```python
# Compositor class is not required in this demo
from geonodes import GeoNodes, Shader
```

## Creating the tree nodes

The tree nodes are created using the `with` context management. The material is created first because it is then used in the Geometry Nodes modifier.

> [!CAUTION]
> All nodes are erased.

```
# A Shader to be used by the Geometry Nodes modifier
with Shader("Hello Material") as tree:
    pass
        
# The Geometry Nodes modifier
with GeoNodes("Hello World") as tree:
    pass
```

## Modifier input

User input can be created using `tree.<DATA_TYPE>_input()` methods as shown below:

``` python
with GeoNodes("Hello World") as tree:
    
    # Let's get the parameters from the user
    count  = tree.integer_input("Resolution", 100, min_value=10, max_value=300)
    size   = 20   # Size
    omega  = tree.integer_input("Omega", 2.)
    height = tree.integer_input("Height", 2.)
    target = tree.object_input("Direction")
```

## Geometry primitive

Use the **CamelCase** name of the node to create the node in the current tree. The code below create a grid:

``` python
    # Create the grid and get the output socket mesh in the variable grid
    grid = tree.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
```

Alternatively, use the **snake_case** version of the name to directly get the output socket:

``` python
    # Create the grid and get the output socket mesh in the variable grid
    grid = tree.grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
```

## Computations

Do maths on vectors, floats, booleans, integers using operators and maths functions available in the tree:

``` python
    # Separate XYZ the position vector 
    pos = grid.position
    
    # Compute the distance
    distance = tree.sqrt(pos.x**2 + pos.y**2)
    
    # Height in z
    z = height * tree.sin(distance*omega)/distance
```











With the default option `is_group=False`, first sockets (input and output) are `Geometry`.

Within the scope of a Tree creation / closure, use `tree` as the variable owning node and socket classes.

In the following example, the `grid` mesh is created in `tree`: 

```python
with GeoNodes("Geometry Nodes') as tree:
    grid = tree.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
```

Fore more details, see [class Tree reference](Tree.md)

### Variables

You can use standard Python variables:

```python
    count  = 100  # Grid resolution
    size   = 20   # Size
    omega  = 2.   # Period
    height = 2.   # Height of the surface
```

The variables can be used for standard python computing:

```python
# We need an angle of 30 degrees
angle = math.pi / 6
```

The variables can also be used as default values of node sockets:

```python
# Let's create an UV sphere of radius 0.5
r = 0.5
sphere = tree.UVSphere(radius=r).mesh
```

In the created node, the input socket `radius` is initialized with `0.5`:

<img src="/docs/images/demo_1_uvsphere.png" width="200">

### Geonodes types

In this example, the variables are initialized in the script. They are pure Python variables. To change them, one needs to modify the script and to rerun it.

When creating a tree, we often need to change settings to see the effect on the geometry. This can be achieved by initializing a **geonodes** type rather than a python type.

In the following script, we slightly modify our code by initializing `size` as a **geonodes** type. It is not anymore a Python `float` but a **geonodes** `Float` i.e. the output socket of a Geometry Node (in that case, the output socket of the input node 'Value'):

```python
    count  = 100
    size   = tree.Float(20.)
    
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
````

The resulting tree is the following. The two `Vertices` input sockets are initialized with the same value. The two `Size` sockets are linked to the output socket of a 'Value' node. One can change the value of the node to see the result on the output geometry.

<img src="/docs/images/demo_1_grid_1.png" height = "200">

> Note: remember that the nodes are deleted a each run of the script.
> Hence, if you change the value in a node, the change will be lost next time you will run the script.
> To avoid that, either your put the value you want in the script or your read the next section.

### Group inputs

Rather that creating an input Node to initialize your data, you can use a group socket, i.e. a **Group input socket**. All data socket classes expose the constructor method `Input`.

Let's modify our script. This time, we initialize `count` as being a Group input socket.

> Note: an **input** socket of the modifier is an **output socket** of the node 'Group Input'.

```python
    count  = tree.integer_nput("Grid resolution", 100)
    size   = tree.Float(20.)
    
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
````
In the resulting tree, the node 'Grid' is now fed by one node and a user parameter named 'Grid resolution':

<img src="/docs/images/demo_1_grid_2.png" height = "200">

### Geometry creation

In our demo, the initial grid is created with the following line:

```python
    grid = tree.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
```

### Layouts

Layouts are ways to make the trees clearer. Creating a layout is done in the context of `with` syntax: any new node created in the scope of a `with` is included in the layout:

```python
    with tree.layout("Computing the wave"):
    
        # From now on, nodes will be created in a dark pink layout
        
        distance = tree.sqrt(grid.position.x**2 + grid.position.y**2)
        z = height * tree.sin(distance*omega)/distance
        
   # New nodes are created out of the previous layout
```

<img src="/docs/images/demo_1_layout.png" width=600>

Note that layouts can be imbricated.

### Math

`GeoNodes` class provides math functions such as `sin`, `arccos` or `color_subtract` based on the nodes 'Math', 'Vector Math' and 'Boolean Math'... Here after are examples of valid operations:

```python
a = tree.Float(1           # The node "Value"
a += 3                     # Node "Math" between previous node and default value 3
b = tree.sin(a)            # Math operations are implemented as functions
v = tree.Vector((1, 2, 3)) # Node "Combine XYZ"
w = v - (2, 3, a)          # Vector math between the previous vector and a "Combine XYZ" node
```

#### Boolean math

Python bool operators `and`, `or` and `not` are reserved keywords. **geonodes** functions are respectively named `band`, `bor` and `bnot`:

```python
yes = tree.Boolean(True)
no = yes.bnot()              # Don't use no = not yes
perhaps = tree.bor(yes, no)  # don't use perhaps = yes or no
```

The basic logical operations are implemented with math operator `+`, `*` and `-`:

```python
yes = tree.Boolean(True)
no = -yes          # Unary operator can be used as logical not
perhaps = yes + no # Operator + can be used as logical or
sure = yes * no    # Operator * can be used as logical and 
```

See [Nodes parameters and method names](/docs/nodes_and_sockets.md#nodes-parameters-and-method-names)

### Sockets methods

The call of a data socket method creates a Geometry node which performs the expected operation.

```python
    grid.set_position(offset=(0, 0, a))    
```

The node 'Set Position' has 4 input sockets (Geometry, Selection, Position, Offset). In this example, the node is created with the following links:
- Geometry : linked with the output socket **Mesh** of the 'Grid' node
- Selection : no link
- Position : no link
- Offset : linked to the output socket **Vector** of a 'Combine XYZ' node

This is illustrated here below:

<img src="/docs/images/demo_1_set_position.png" height="200">

### Domains

Some nodes accept a **domain** parameter. For instance the node **StoreNamedAttribute** must specify a domain where to store the attribute.
An alternative syntax is proposed to simplify the code:

``` python
geo.store_named_attribute("name", attribute=value, domain='FACE')

# is equivalent to:

geo.FACE.store_named_attribute("name", attribute=value)
```

### Selection

The selection socket can be replaced by item selector syntax:

``` python
# Selection of vertices by their index
selection = geo.index.greater_then(10)

# Change the position of these vertices
geo.set_position(position=some_vector, selection=selection)

# Is equivalent to
geo[selection].set_position(position=some_vector)
```

Rather than a bool selection, the selector can be an integer. In that case, **geonodes** generates the nodes to compare the index with the passes argument:

``` python

# ----- index equal a value
geo.set_position(position=v, selection=geo.index.equal(some_index))

# is equivalent to
geo[some_index].set_position(position=v)

# ----- index in a range (python int only)
geo.set_position(position=v, selection=geo.index.greather_than(10) * geo.index.greather_than(20))

# is equivalent to
geo[10:20].set_position(position=v)
```

Selection and domain shortcut can be comabined

``` python
# Store the value 15 on the faces indexed between 10 and 20
geo.FACE[10:20].store_named_attribute("name", attribute=15)
``` 


### Output geometry

To define a geometry as the result of the modifier, simply set the `output_geometry` property of the tree.

```python
    tree.output_geometry = grid.set_shade_smooth()

    # Or you can use the 'shortcut' og
    tree.og = grid.set_shade_smooth()
    
```

## Further reading

TBD

