# Demo script

> Let's review this demo script in detail. Afterwards, you should be able to script your own tree.

The script creates a surface from a grid by computing
`z = sin(d)/d` where `d=sqrt(x^2 + y^2)` is the distance of the vertex to the center.

```python
# Import the geonodes modules
# gn is the suggested alias
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:

    # Let's document our parameters
    count  = 100  # Grid resolution
    size   = 20.  # Size
    omega  = 2.   # Period
    height = 2.   # Height of the surface
    
    # The base (x, y) grid
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
    
    # We compute z
    with tree.layout("Computing the wave", color="dark_rose"):
        distance = gn.sqrt(grid.position.x**2 + grid.position.y**2)
        z = height * gn.sin(distance*omega)/distance
        
    # Let's change the z coordinate of our vertices
    grid.set_position(offset=(0, 0, z))
    
    # We are done: plugging the deformed grid as the modified geometry
    tree.output_geometry = grid.set_shade_smooth()     
```

The generated nodes and the result of the Geometry nodes modifier is given below:

<img src="images/demo_intro.png" width="600" class="center">

## Description

### Import

```python
import geonodes as gn
```

Be sure to have properly installed the **geonodes** module as described in the [Installation section](/README.md#installation).

`gn` is the proposed alias to use as **geonodes** naming space.

### Tree creation

A Tree instance can be created with
  
```python
tree = Tree(tree_name)
...
tree.close()
```

But it is recommanded to use `with` syntax to ensure that the tree will be properly closed. The closing performs final mandatory treatments.

```python
with gn.Tree("Geometry Nodes") as tree:
    ...
```

The `tree_name` is the name of a geometry nodes modifier. If it doesn't exist, it will be created. However, it is recommended to create the geometry nodes first.

> CAUTION: when calling `tree(tree_name)`, ***all the nodes and links are erased***. Be sure not to open a tree with an existing valuable tree you don't want to loose.

<hr>

> Important notice: within the scope of a Tree creation / closure, all the nodes are created within this tree. There is no need to make reference to this tree.

In the following example, the `grid` mesh is created in `tree` without making any explicit reference to it. 

```python
with gn.Tree("Geometry Nodes') as tree:
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
```
<hr>

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
angle = pi / 6
```

The variables can also be used as default values of node sockets:

```python
# Let's create an UV sphere of radius 0.5
r = 0.5
sphere = gn.Mesh.UVSphere(radius=r)
```

In the created node, the input socket `radius` is initialized with `0.5`:

<img src="/docs/images/demo_1_uvsphere.png" width="200">

### Geonodes types

In this example, the variables are initialized in the script. They are pure Python variables. To change them, one needs to modify the script and to rerun it.

When creating a tree, we often need to change settings to see the effect on the geometry. This can be achieved by initializing a **geonodes** type rather that a python type.

In the following script, we slightly modify our script by initializing `size` as a **geonodes** type. It is not anymore a Python `float` but a **geonodes** `Float` i.e. the output socket of a Geometry Node (in that case, the output socket of the input node 'Value'):

```python
    count  = 100
    size   = gn.Float(20.)
    
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
````

The resulting tree is the following. The two `Vertices` input sockets are initialized with the same value. The two `Size` sockets are linked to the output socket of a 'Value' node. One can change the value of the node to see the result on the output geometry.

<img src="/docs/images/demo_1_grid_1.png" height = "200">

> Note: remember that the nodes are deleted a each run of the script. Hence, if you change the value in a node, the change will be lost next time you will run the script. To avoid that, either your put the value you want in the script or your read the next section.

### Group inputs

Rather that creating an input Node to initialize your data, you can use a group socket, i.e. a **Group input socket**. All data socket classes expose the constructor method `Input`.

Let's modify our script. This time, we initialize `count` as being a Group input socket.

> Note: an **input** socket of the modifier is an **output socket** of the node 'Group Input'.

```python
    count  = gn.Integer.Input(100, "Grid resolution")
    size   = gn.Float(20.)
    
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
````
In the resulting tree, the node 'Grid' is now fed by one node and a user parameter named 'Resolution':

<img src="/docs/images/demo_1_grid_2.png" height = "200">

### Geometry creation

In our demo, the initial grid is created with the following line:

```python
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
```

Geometry creation is done through the nodes located in the Blender add menus **Mesh Primitives** and **Curve Primitives**.

In **geonodes**, these nodes are implemented as **constructors** (class or static method) of [Mesh](/docs/sockets/Mesh.md) of [Curve](/docs/sockets/Curve.md) classes.

### Layouts

Layouts are ways to make the trees clearer. Creating a layout makes use of the `with` syntax: any new node created in the scope of a `with` is included in the layout:

```python
    with tree.layout("Computing the wave", color="dark_rose"):
    
        # From now on, nodes will be created in a dark pink layout
        
        distance = gn.sqrt(grid.position.x**2 + grid.position.y**2)
        z = height * gn.sin(distance*omega)/distance
        
   # New nodes are created out of the previous layout
```

<img src="/docs/images/demo_1_layout.png" width=600>

Note that the layout can be nested.

### Math

**geonodes** provides math function such as `sin`, `arccos` or `color_subtract`. Math operators can also be used on geonodes values. Are after are example of valid operations:

```python
a = gn.Float(10)         # The node "Value"
a += 3                   # Node "Math" between previous node and default value 3
b = gn.sin(a)            # Math operations are implemented as functions
v = gn.Vector((1, 2, 3)) # Node "Combine XYZ"
w = v - (2, 3, a)        # Vector math between the previous vector and a "Combine XYZ" node
```

### Boolean math

Python bool operators `and`, `or` and `not` are reserved keywords. **geonodes** functions are respectively named `b_and`, `b_or` and `b_not`:

```python
yes = gn.Boolean(True)
no = yes.b_not()            # Don't use no = not yes
perhaps = gn.b_or(yes, no)  # don't use perhaps = yes or no
```

The basic logical operations are implemented with math operator `+`, `*` and `-`:

```python
yes = gn.Boolean(True)
no = -yes          # Unary operator can be used as logical not
perhaps = yes + no # Operator + can be used as logical or
sure = yes * no    # Operator * can be used as logical and 
```

### Nodes methods

The call of a data socket method creates a Geometry node which performs the expected operation.

```python
    grid.set_position(offset=(0, 0, z))
```

The node 'Set Position' has 4 input sockets (Geometry, Selection, Position, Offset). In this example, the node is created with the following links:
- Geometry : linked with the output socket grid
- Selection : no link
- Position : no link
- Position : linked ot the output socket of a node 'Combine XYZ'

This is illustrated here below:

<img src="/docs/images/demo_1_set_position.png" height="200">

### Output geometry

To define a geometry as the result of the modifier, simply set the `output_geometry` property of the tree.

```python
    tree.output_geometry = grid.set_shade_smooth()     
```

## Further reading

TBD

