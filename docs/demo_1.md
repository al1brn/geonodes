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

In this example, the variables are initialized in the script. They are pure Python variables. To change them, one need to modify the script and to rerun it.

We creating a tree, we often need to change settings to see the effect on the geometry. This can be achieved by initializing a **geonodes** type rather that a python type.

In the following script, we slightly modify our script by initializing `size` as a **geonodes** type. It is not anymore a Python `float` but `gn.Float` i.e. the output socket of a Geometry Node (in that case, the output socket of the input node 'Value'):

```python
    count  = 100
    size   = gn.Float(20.)
    
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
````

The resulting tree is the following. The two `Vertices` input sockets are initialized with the same value. The two `Size` sockets are linked to the output socket of a 'Value' node. One can change the value of the node to see the result on the output geometry.

<img src="/docs/images/demo_1_grid_1.png" height = "200">

> Note: remember that the nodes are deleted a each run of the script. Hence, if you change the value in a node, the change will be lost next time you will run the script. To avoid that, either your put the value you want in the script or your read the next section.

### Group inputs

Rather that creating an input Node to initialize your data, you can use a group socket, i.e. a **Group input socket**. All data classes expose the constructor method `Input`.

Let's modify our script. This time, we initialize count as being a Group input socket.

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

Geometry creation is done through the nodes located in the menus **Mesh Primitives** and **Curve Primitives**.

In **geonodes**, these nodes are implemented as **constructors** (class or static method) of [Mesh](/docs/sockets/Mesh.md) of [Curve](/docs/sockets/Curve.md) classes.

### Layouts

Layouts are ways to make the trees clearer. Creating a layout makes use of the `with` syntax: any new node created in the scope of a `with` is included in the layout:

```python
    with tree.layout("Computing the wave", color="dark_rose"):
        # From now on, the nodes will be created in the layout
        distance = gn.sqrt(grid.position.x**2 + grid.position.y**2)
        
   # New nodes are created out of the previous layout
```


Note that the layout can be nested.


  
- **Layouts**

  Layouts can be created to make the result more readable and to help debug. Layout are initialized with a label and a color.
  All nodes created in the `with tree.layout():` scope are placed in this layout.
  
- **Operators**

  Python operators can be used on geonodes types. Operations between geonodes types and standard python types are valid in some cases:
  
  ```python
  a = gn.Float(10)         # The node "Value"
  a += 3                   # Node "Math" between previous node and default value 3
  v = gn.Vector((1, 2, 3)) # Node "Combine XYZ"
  w = v - (2, 3, a)        # Vector math between the previous vector and a "Combine XYZ" node
  ```
  
- **Methods**

  Nodes such as "Set position" are implemented as methods.
  
- **Input and output geometries**

  The output geometry is set with `tree.output_geometry`. Similaly, the input geometry can be read with `tree.input_geometry`
  
  ```python
  import geonodes as gn
  
  with gn.Tree("Geometry nodes") as tree:
  
      # The "do nothing" modifier !
      
      tree.output_geometry = tree.input_geometry
  ```
 
# Installation

Simply copy the geonodes folder in the modules folder `...blender/scripts/modules/`. Note that **geonodes** is not an addon, simply a python module.
The modules classes and functions are then accessible through a standard import statement:

```python
import geonodes as gn
```

# Overview

## Nodes, sockets and classes

geonodes manages **nodes** and **sockets**. Node sockets are data when the nodes are operators working on data.
For each socket type, there is a corresponding geonodes class:

- Geometry classes:
  - Geometry
  - Spline
  - Curve
  - Mesh
  - Instances
  - Points
  - Volume
- Values
  - Boolean
  - Integer
  - Float
  - Vector
  - Color
  - String
- Other
  - Collection
  - Object
  - Texture
  - Image
  - Material
 
A data class makes necessarily reference to a node socket. Operations on data classes are made by creating nodes. The node owning the socket is a property of the data class.<br>
The following example shows how to change the label and the color of the node owning the a Geometry class:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    # Get the input geometry
    
    geo = tree.input_geometry
    
    # Shade smooth
    
    geo.set_shade_smooth()

    # Change the node "shade smooth" name and color
    
    geo.node.node_color = "red"
    geo.node.label = "Smoothing"
    
    # Output geometry
    
    tree.output_geometry = geo 
```

The resuling tree is the following:

<img src="docs/images/node_labeling.png" width="600">


## Initializing classes

Data classes can be created in three ways:
1. From constant values
2. From group input
3. Mesh and Curve constructors

### 1. Constant initialization

Value classes can be initialized by passing a value in the class init:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    ok     = gn.Boolean(False)
    count  = gn.Integer(100)
    factor = gn.Float(5.5)
    vector = gn.Vector((1, 2, 3))
    color  = gn.Color((.1, .2, .3))
    title  = gn.String("My label")
 ```
 
 The variable correspond to output sockets of the initialization nodes:
 
 ![Value classes initialization](docs/images/value_init.png)
 
 ### 2. Group inputs
 
 Each class implements the class method **Input** which get the socket from the tree group input.<br>
 In the example below we initialized the same variables from group inputs:
 
 ```python
 import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    ok     = gn.Boolean.Input(False, "Option")
    count  = gn.Integer.Input(100, "Count")
    factor = gn.Float.Input(5.5, "Factor")
    vector = gn.Vector.Input((1, 2, 3), "Location")
    color  = gn.Color.Input((.1, .2, .3), "Color")
    title  = gn.String.Input("My label", "Title")
 ```
 The variables represent now the sockets of group input node:
 
 
 <img src="docs/images/group_input_values.png" width="200">

 
 Geometry classes can also be initialized from a group input socket.<br>
 In the following example, we use the optional argument `description` to provide a tool tip to the user.
 
 ```python
 import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    curve   = gn.Curve.Input("Profile", "The curve profile for converting to mesh")
    models  = gn.Collection.Input("Instances", "Collection of instances")
    control = gn.Object.Input("Control", "Object to use as control")
    image   = gn.Image.Input("Image", "The input image for the modifier")
    texture = gn.Texture.Input("Noise", "Noise texture to use to deform the surface")
 ```
 
 The group input is now:
 
 <img src="docs/images/group_input_other.png" width="200">

 ### 3. Mesh and Curve constructors
 
 **Mesh** and **Curve** classes provide constructors (class methods) to initialize geometry. Basically, the constructors create the nodes in the Geometry Nodes menu **Mesh Primitives** and **Curve Primitives**.
 
```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    sphere = gn.Mesh.UVSphere(segments=10, rings=5)
    
    tree.output_geometry = sphere
```    

<img src="docs/images/uv_sphere.png" width="300">

## Value classes : single value or array of values

It is important to understand that value classes such as **Float** or **Vector** can represent either a single value or an attribute,
i.e. an array of values (one value per **Mesh** vertex for instance).<br>
In the example below we create a modifier on a cube having several materials, each face with its own material.
The tree shifts the material index of the faces. The shift is an addition between an array of values `mat_indices` and a single value `offset`.
both variables share the same class: **Integer**.

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    # Get the geometry from the modifier object
    # Since it is a mesh, we must cast to Mesh to benefit from
    # Mesh class methods
    
    cube = gn.Mesh(tree.input_geometry)
    
    # mat_indices represents the 6 material indices of the 6 faces of the cube
    
    mat_indices = cube.material_index

    # offset is a single value Integer
    
    offset = gn.Integer(1)
    
    # We can combine the two integers to set the new indices of the cube
    
    cube.set_material_index(material_index=(mat_indices + offset) % 3)
    
    # Let's represent the result
    
    tree.output_geometry = cube
 ```  
 
<img src="docs/images/material_shift_nodes.png" height="250"> <img src="docs/images/colored_cubes.png" height="250">

Note that in real life, this example would certainly have been written in a more concentrated style, while keeping the same readibility.
The following two lines generate the above 6-nodes, 5-links tree:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    cube = gn.Mesh(tree.input_geometry)
    tree.output_geometry = cube.set_material_index(material_index=(cube.material_index + 1) % 3)
```

## Geometry nodes implementation

The Geometry nodes provide methods and properties for geonodes classes.
The nodes are implemented into several ways:

- **constructor**, for instance the node "_Curve Circle"_ is implemented as a static method of the **Curve** class
- **method**, for instance the node _"Curve to Mesh"_ is implemented as the method **to_mesh** of the class **Curve**
- **property**, for instance the node _"Bounding Box"_ is implemented as a property of **Geometry** class.<br>
  Since the _"Bounding Box"_ outputs 3 sockets, each socket is itself a property of the **Geometry** class
- **operator**, for instance the _"Math"_ node gives birth to the standard operators: +, -, * ... 

The attributes are managed in a specific way which is described in the next section.

In the script below, we see the four ways of how nodes are implemented:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    # Building a torus from two circle: major and minor circle
    
    # Both circle are created by the Circle static method or Curve
    # which implement the node "Curve Circle"
    # Note that this node outputs two sockets:
    # - curve  (Curve)
    # - center (Vector)
    # Hence the method Circle returns the node and not the socket
    # One must explicitly get the curve socket
    
    major_radius = 1
    minor_radius = .2
    
    torus   = gn.Curve.Circle(radius=major_radius).curve   # The major circle
    profile = gn.Curve.Circle(radius=minor_radius).curve   # The minor circle
    torus = torus.to_mesh(profile_curve=profile)           # "Curve to Mesh" node
    
    # Let's get the bound box of the resulting mesh
    # And use it the create a socle below the torus
    
    box = torus.box
    box.set_position(offset=(0, 0, -2*minor_radius))
    
    # The + operator between two geometries implements the "Join Geometry" node
    
    tree.output_geometry = torus + box
```

### Returned values

The principe is the following:
-  When a node as only one output socket, it returns an instance of the corresponding class.
   In the following example, since the node _"Curve to Mesh"_ has only one output socket,
   the method **to_mesh** returns a class **Mesh**:
   
   ```python
   torus = torus.to_mesh(profile_curve=profile)
   ```
   
 - When a node has several output sockets, it returns the node itself.
   The user must select his output as a property of the returned node:

   ```python
    import geonodes as gn

    with gn.Tree("Geometry Nodes") as tree:
    
        # The node "Noise texture" returns two sockets
        # The constructor Noise returns the node, not a socket

        noise = gn.Texture.Noise()

        # We cas use the factor socket

        fac = noise.fac

        # Or the color socket

        color = noise.color
    ```
    
 - _"Capture Attribute"_ node is a particular case. Even if the node has two output sockets (**geometry** and **attribute**),
   the method returns the **attribute** socket. The geometry instance calling the method points on the **geometry** socket after the call.
   See the attributes section for more details.

### Creating vs transforming nodes

A node such as _"Curve to Mesh"_ takes a **Curve** as input socket et gives a **Mesh** as output socket.
The output socket must be considered as data which is different from the input socket.
The method **creates new data**, it follows the sheme: `Mesh = Curve.method(...)`.

On the other hand, a node such as "Set Shade Smooth" is a modifier applied on a geometry.
The output geometry is the same as the input geometry. It has just been transformed by the node.
The method **transforms data**, it follows the scheme: `Geometry.method()`.

The following piece of code illustrates the creation vs transformation calls:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:
    
    # Let's build a torus
    
    # The torus major circle 
    
    circle = gn.Curve.Circle(radius=1).curve
    circle.node.node_color = "green"

    # ---------------------------------------------------------------------------
    # circle : points on the output socket of the node "Curve Circle"
    # ---------------------------------------------------------------------------
    
    torus = circle.to_mesh(profile_curve=gn.Curve.Circle(radius=.2).curve)
    torus.node.label = "Torus first node"
    torus.node.node_color = "red"
    
    # ---------------------------------------------------------------------------
    # torus  : points on the output socket of the node "Curve to Mesh", renamed "Torus first node"
    # circle : didn't change
    # ---------------------------------------------------------------------------
    
    torus.set_shade_smooth()
    torus.node.label = "Torus second node"
    torus.node.node_color = "blue"

    # ---------------------------------------------------------------------------
    # torus : now points on the output socket of the node "Set Shade Smooth", renamed "Torus second node"
    # ---------------------------------------------------------------------------
    
    tree.output_geometry = torus
```

In the generated tree, we can see that the node property of the torus has changed after the call of `set_shade_smooth`:


<img src="docs/images/transformation_creation.png" width="600">







   
 
 
 
 
 
 







 
## Module presentation

The geonodes implements two layers:
- **Nodes layer**
  One class per geometry nodes, for instance AlignEulerToVector wraps the node FunctionNodeAlignEulerToVector
  The Node class initialization creates the geometry nodes
- **Sockets layer**
  One class per data type:
  - Basis data: Boolean, Integer, Float, Vector, Color, String
  - Geometry  : Geometry, Spline, Curve, Mesh, Point, Instance, Volume
  - Special   : Collection, Object, Material, Texture, Image
  The methods and properties of the sockets are implemented by creating nodes:
  ```python
  import geonodes as gn
  
  circle = gn.Mesh.Circle(radius=2.) # creates the node GeometryNodeMeshCircle
  ```
At creation time, a node takes two types or arguments:
- the input sockets
- the node parameters

```python
import geonodes as gn
from geonodes import nodes

# rotation   : first node socket
# factor     : second socket
# vector     : third socket
# axis       : first parameter
# pivot_axis : second parameter

node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```
# Source code generation

In a Blender project, create a Geometry nodes modifier and run the following script
```python
from generator.generator import gen_geonodes

# fpath is the location to where the geonodes folder is located
# within the Blender modules folder

fpath = ".../blender/modules/scripts/modules/geonodes/"
gen_geonodes(fpath)
```
# geonodes folder structure

## geonodes.core
### geonodes.core.node

- **Tree**        : Blender NodeTree wrapper
- **DataSocket**  : Root class for socket wrappers
- **Node**        : Root class for blender geometry nodes wrappers

  Some specific nodes are implemented in this module. They are used by **Tree**:
    
  - **GroupInput** : Wrapper for node NodeGroupInput.
    ```python
    # The group input is initialized in the Tree
    Tree.group_input = GroupInput()
    ```
  - **GroupOutput** : Wrapper for node NodeGroupOutput
    ```python
    # The group output is initialized in the Tree
    Tree.group_output = GroupOutput()
    ```       
  - **Viewer**      : Wrapper for node GeometryNodeViewer
    ```python
    # The viewer is initialized by the Tree when required
    Tree.viewer = None
    ...
    if self.viewer is None:
        self.viewer = Viewer()
    ```
    One viewer per tree. Data sockets can use the method to_viewer()
              
  - **Frame**       : Wrapper for node NodeFrame
    ```python
    def new_layout(self, label, color):
       self.layouts.append(Frame(label, color))
    ```
  - **SceneTime**   : Wrapper for GeometryNodeInputSceneTime
    ```python
    Tree.scene_ = None
    
    @property
    def scene(self):
        if self.scene_ is None:
            self.scene_ = SceneTime()
        return self.scene_
    ```
    
### geonodes.core.datasockets

Implements the base class for DataSockets
All the classes are base on geonode.node.DataSocket
For geometry data, only the class Geometry is implemented in this module
The final classes will be created in geonodes.sockets with the following inheritance
Geometry
    - Spline
        - Curve
    - Mesh
        - Points
        - Instance
        - Volume
        
----- geonodes.core.colors
Some colors constants
----- geonodes.core.arrange
arrange function locates the nodes to make the whole tree somehow readable
It works independantly of the geonodes structure and just take the name
of the NodeTree as an argument.
----------------------------------------------------------------------------------------------------
----- geonodes.nodes.nodes
All he nodes generated by the generator
----------------------------------------------------------------------------------------------------
----- geonodes.nodes.sockets
One file per data socket class plus functions.py which contains the global functions
----------------------------------------------------------------------------------------------------
----- geonodes.__init__.py
The pack initi file contains
====================================================================================================
Generation principle
The generation module is designed to ease the updates with the new versions of geometry nodes
Step 1
------
    try to create all the possible nodes by listing all the types in bpy.types:
    
    for type_name in dir(bpy.types):
        try:
            node = nodes.new(type_name)
        except:
            continue
        
        # We have a valid type
        
    The legacy nodes are excluded from the scane
    
Step 2
------
    Each node is analyzed by:
        - Identifying the parameters (non standard attributes)
            Three types of parameters are possible:
                - Non settable parameters, for instance the color selector of an input color node
                - Enum parameters: str param with a list of valid values
                - Non enum settable parameters, the resolution of a circle for instance
            The settable parameters will be part of the node creation argument
        
        - Identifying if the node has "shared sockets"
            Shared sockets are sockets of different types but sharing the same name.
            Only one socket is enabled at a time, depending upon a "driving parameter"
            Example: node FunctionNodeCompare:
                    - Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
                    - Input sockets     : ['a', 'b']
                    a and b are names shared by sockets of type Float, Integer, Vector, String and Color
                    
        - Renaming sockets homonyms when exist
            For instance node ShaderNodeMath has three input sockets named Value. They are renamed
            value0, value1 and value2
                    
Step 3
------
    file nodes.py generation in folder geonodes.nodes
    
    The __init__ method of the node class is the concatenation of the input sockets and the settable parameters
    
    for instance, the __init__ method of ShaderNodeMath is:
        
        def __init__(self, value0=None, value1=None, value2=None, operation='ADD'):
            
            The node has 3 sockets and one parameter named operation.
            The default value 'ADD' is the one of the parameter at creation time.
            When a socket has the value None, it is left unplugged.
            A socket can be either a value or data socket class. If it is a value, it
            must be an acceptable default value for the input socket.
            
    An additional argument label is used to allow the user to change the node label:
        def __init__(self, value0=None, value1=None, value2=None, operation='ADD', label=None):
            
Step 4
------
    Generation of the data sockets classes.
    
    A data socket basically wraps an output node socket.
    The methods of a data class consist in creating a node and to plug the socket to one
    input socket of this node.
    
    Example:
        Let use x as a Float which is the output socket of a node.
        We can write:
            
            y = x ** 3
            
        This will create the node ShaderNodeMath with the following parameters:
            
            node = Math(value0=self, value1=3, operation='POWER')
            return node.value
        
    Implementation types
    ---------------------
    
    Depending on their behaviors, the nodes can be implented in the following ways:
        
        Constructor
        -----------
            For nodes which don't transform a socket but create new data
            
            Example: GeometryNodeMeshCircle is implemented as a Mesh constructor
            
            @classmethod
            def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
                return cls(nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)
            
        Property
        --------
            For node which return info on data sockets. The properties are kept in local attributes:
                
                self.prop_ = ... node creation
                return self.prop_
            
            Example: GeometryNodeBoundBox returns 3 infos on the geometry : bounding_box, min and max
"""
