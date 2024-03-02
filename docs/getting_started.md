# Getting started

- [Prerequisites](#prerequisites)
  - [3 Types of Nodes Trees](#3-types-of-nodes-trees)
  - [Importing the Module](#importing-the-module)
- [Creating a new Tree](#creating-a-new_tree)
  - [Creating a Group](#creating-a-group)
- [Creating a Node](#creating-a-node)
  - [Node Sockets](#node-sockets)
  - [Links](#links)
  - [Sockets sharing the same Name](#sockets-sharing-the-same-name)
  - [Node parameters](#node-parameters)
  - [Node init arguments order](#node-init-arguments-order)
  - [Multi Input Sockets](#multi-input-sockets)
  - [Input and Output Nodes](#input-and-output-nodes)
- [Socket Classes](#socket-classes)

## Prerequisites

To use the **geonodes** python module, you are supposed to be familiar with:
- Blender Geometry and Shader nodes
- Python language
- Running python scripts in Blender

Install the version of **geonodes** compatible with the Blender version you use.

### 3 types of Nodes Trees

**geonodes** support 3 types of nodes trees:

- Geometry nodes (class `geonodes.GeoNodes`)
- Shader nodes (class `geonodes.Shader`)
- Compositor nodes (class `geonodes.Compositor`)

Once initialized as described below, there is no major differences in the behavior.
Differences exists in the inputs and outputs of the trees and on the set of possible nodes.

### Importing the Module

We suppose that all scripts start with the following import instruction:

``` python
from geonodes import GeoNodes, Shader, Compositor
```

## Creating a new Tree

A tree is created using the with statement:

``` python
# Creating a new Geometry nodes modifier
with GeoNodes("Geometry Nodes") as tree:
    pass

# Creating a new material
with Shader("Material") as tree:
    pass
    
# Accessing the scene compositor nodes:
with Compositor() as tree:
    pass
```

The first parameter is the name of the tree to create. For `Compositor`, the nodes are the one of the current scene.
If your file hase several scenes, you can specify the name of the scene you want to edit the compositor of:

``` python
# Edit the compositor nodes of the scene named "Scene.001"
with Compositor("Scene.001") as tree:
    pass
```

> [!WARNING]
> When opening a tree, the existing nodes are deleted!

### Creating a Group

A **Node Group** can be created by using the `is_group` argument:

```python
with GeoNodes("My Group", is_group=True):
    pass
```

## Creating a Node

Create a node by using its **CamelCase** name. For instance:
- Node *Set Shade Smooth* : `tree.SetShadeSmooth``
- Node *Set Position* : `tree.SetPosition`
- Node *Curve Circle* : `tree.CurveCircle` 

The following piece of code creates an *Ico Sphere* node with default parameters:

``` python
with GeoNodes("Geometry Nodes") as tree:
    # Create an ico sphere
    node = tree.IcoSphere()
``` 

Nodes generally have input sockets and can have parameters.
These can be set as initialization arguments of the node:

``` python
with GeoNodes("Geometry Nodes") as tree:

    # Create a Math node adding 2 and 2 and get the result in the value variable
    value = tree.Math(2, 2, operation='ADD').value
    
    # Use this result as resolution of the ico sphere
    ico = tree.IcoSphere(resolution=value).mesh
```

The way sockets and parameters are named is described below.

### Node Sockets

The node sockets are named with the **snake_case** version of their actual name. For instance:
- Input sockets of `IcoSphere` node: `radius` and `subdivisions`
- Output sockets of `IcoSphere` node : `mesh` and `uv_map`

Input sockets are **write only** node attributes when output sockets are **read only** node attributes:

``` python
with GeoNodes("Geometry Nodes") as tree:
    # Create an ico sphere
    node = tree.IcoSphere()
    
    # Set the input sockets (write only attributes)
    node.radius = 2.
    node.subdivisions = 5
    
    # Get the output sockets (read only attributes)
    mesh = node.mesh
    uv = node.uv_map
```

### Links

Links between nodes are simply created by setting an input socket with an output sockets.
In the following examplen the ico sphere is smoothed:

``` python
with GeoNodes("Geometry Nodes") as tree:
    # Create an ico sphere
    node = tree.IcoSphere()
    
    # Create a Set Shade Smooth node
    smooth = tree.SetShadeSmooth()
    
    # Link the two nodes
    smooth.geometry = node.mesh
```

### Sockets sharing the same Name

When a node uses the same name for an input and an output socket, the same **snake_case** name is used for both sockets with no ambiguity.

``` python
with GeoNodes("Geometry Nodes") as tree:

    # Create a Set Shade Smooth node
    smooth = tree.SetShadeSmooth()

    # set : Input geometry of the SetShadeSmooth node
    smooth.geometry = node.mesh
    
    # get : Output geometry of the SetShadeSmooth node
    smoothed = smooth.geometry
```

The same name can be used several times for input and output sockets. In that case, the sockets are numerbered
in their order in the node from the seconde one (the first one keeps its raw snake_case name) as shown
in the example below:

``` python
with GeoNodes("Geometry Nodes") as tree:

    # A math node
    node = tree.Math()
    
    node.value    = 1 # Set the first 'Value' socket
    node.value_1  = 2 # Set the second 'Value' socket
    node.value_2  = 3 # Set the third 'Value' socket
    
    # Get the result
    result = node.value # Output 'Value' socket
```

### Node parameters

Node parameters can be accessed with their Blender attribute name. For instance de Blender node *Math* has
a parameter named `operation` which can set as an attribute of the `Math` node:

``` python

    # A math node
    node = tree.Math()
    
    # Setting the operation
    node.operation = 'MULTIPLY'
```

### Node Init Arguments Order

Sockets and parameters can be set as arguments of the node creation `__init__` instruction.
The first arguments are the sockets, then the parameters.

``` python
# Math node __init__ header
def __init__(self, value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False):
```

> [!CAUTION]
> Some sockets are hidden in the default configuration but they are present in the initialization.
> Hence, it is recommended to use keyword arguments for paramters

``` python
with GeoNodes("Geometry Nodes") as tree:

    # Add two values
    value = tree.Math(2, 2, operation='ADD').value
    
    # The following line uses 'ADD' string as input for the third socket named 'Value'
    value = tree.math(2, 2, 'ADD').value
```

> [!CAUTION]
> By exception when a selection socket exists, it is placed as the last socket

``` python
# SetPosition __init__ header: selection is the last socket even if it is the second one in the actual Node
def __init__(self, geometry=None, position=None, offset=None, selection=None)
```

### Multi Input Sockets

Some nodes have multi input sockets. Multiple output sockets can be set simultaneously through `*args`:

``` python
with GeoNodes("Geometry Nodes") as tree:

    # Creating geometries geo1, geo2 and geo3
    
    ...
    
    # Joining the geometries    
    joined_geo = tree.JoinGeometry(geo1, geo2, geo3).geometry
```

### Input and Output Nodes

Tree classes have optional input and output nodes named `tree.input_node` and `tree.output_node`.
The type of these nodes depends upon the type of tree:

- `GeoNodes` : Geometry Nodes **Group Input** and **Group Output**
- `Shader` : only **Material Output** node
- `Compositor` : **Render Layers** and **Composite**
- `Group` (`is_group = True`) : **Group Input** and **Group Output**

In the following example we connect the tree input geometry to the tree output geometry:

``` python
with GeoNodes("Do Nothing") as tree:
    tree.output_node.geometry = tree.input_node.geometry
``` 


## Socket Classes

One could implement any tree by simply creating nodes and setting sockets input sockets from output sockets.
But this wouldn't be very interesting compared to using directly the nodes editor in Blender.

A better way to create nodes is to think them as **methods** or **properties** of sockets. For instance creating a `SetShadeSmooth` node
can be thought as setting the `shade_smooth` property of a geometry:

``` python
with GeoNodes("Geometry Nodes") as tree:

    # Create an ico sphere
    ico = tree.IcoSphere(radius=2., subdivisions=4).mesh
    
    # Shading smooth
    ico.shade_smooth = True
    
    # This is equivalent to
    ico = tree.SetShadeSmooth(geometry=ico, shade_smooth=True).geometry
```

Some nodes are also implemented as **operators** between sockets and other sockets or values:

``` python
with GeoNodes("Geometry Nodes") as tree:

    # Add two values, set the result in a
    a = tree.Math(2, 2, operation='ADD').value
    
    # variable a is a socket or type VALUE
    # Standard operations are possible
    
    # Between a socket and a python value
    b = 2*a
    
    # Between two sockets
    c = b/a
    
    # In place operators are possible
    c *= 5
    b /= a
    
    # Unary operator
    e = -b
```

### Socket types

The methods available depend upon the socket types:

- VALUE
- INT
- BOOLEAN
- VECTOR
- ROTATION
- STRING
- RGBA
- SHADER
- OBJECT
- IMAGE
- GEOMETRY 
- COLLECTION
- TEXTURE
- MATERIAL

Normally, the socket classes are never directly instantied but are read from nodes.

> [!CAUTION]
> Not all types exist in the different trees : **GeoNodes**, **Shader** and **Compositor**.

### Tree input and output Sockets

As mentioned in the section [Input and Output Nodes](#input-and-output-nodes), the input and output nodes
can be read from a tree through its attributes `tree.input_node` and `tree.output_node`.

The default sockets can be directly read with dedicated attributes:

- GeoNodes
  - `tree.input_geometry` (shortcut `tree.ig`) : input ***Geometry*** socket
  - `tree.output_geometry` (shortcut `tree.og`) : output ***Geometry*** socket
- Shader
  - `tree.output_surface` : output ***Surface*** socket
  - `tree.output_volume` : output ***Volume*** socket
  - `tree.output_displacement` : output ***Displacement*** socket
- Compositor
  - `tree.use_alpha` : parameter ***Use Alpha*** of the output node
  - `tree.output_image` : output ***Image*** socket
  - `tree.output_alpha` : output ***Alpha*** socket
  
In the example below, a "Do Nothing" geometry nodes tree is created:

``` python
with GeoNodes("Do Nothing") as tree:
    tree.og = tree.ig
```

### Creating group input sockets

Tree groups and geometry nodes tree accept user created sockets.
To create custom sockets, use the methods `tree.xxx_input()` methods where `xxx` is the type
of socket input you want.

Sockets of type `FLOAT` and `VECTOR` accept sub types. The example below show all the possible inputs:

``` python
with GeoNodes("All inputs") as tree:
    
    val = 123
    min_value = 0
    max_value = 1000
    
    # Integers
    
    tree.int_input(           "Int",            value=val, min_value=min_value, max_value=max_value, description="Int")
    tree.integer_input(       "Integer",        value=val, min_value=min_value, max_value=max_value, description="Integer")
    tree.int_factor_input(    "Int Factor",     value=val, min_value=min_value, max_value=max_value, description="Int Factor")
    tree.int_percentage_input("Int Percentage", value=val, min_value=min_value, max_value=max_value, description="Int Percentage")
    
    # Floats

    tree.float_input(        "Float",       value=val, min_value=min_value, max_value=max_value, description="Float")
    tree.value_input(        "Value",       value=val, min_value=min_value, max_value=max_value, description="Value")
    tree.angle_input(        "Angle",       value=val, min_value=min_value, max_value=max_value, description="Angle")
    tree.distance_input(     "Distance",    value=val, min_value=min_value, max_value=max_value, description="Factor")
    tree.factor_input(       "Factor",      value=val, description="")
    tree.percentage_input(   "Percentage",  value=val, min_value=min_value, max_value=max_value, description="Percentage")
    tree.time_input(         "Time",        value=val, min_value=min_value, max_value=max_value, description="Time")
    tree.time_absolute_input("Time abs",    value=1., min_value=min_value, max_value=max_value, description="Time Absolute")
    
    # Rotation and vectors
    
    tree.rotation_input("Rotation", value=None, min_value=None, max_value=None, description="")

    tree.vector_input(      "Vector",       value=val, min_value=min_value, max_value=max_value, description="Vector")
    tree.translation_input( "Translation",  value=val, min_value=min_value, max_value=max_value, description="Translation")
    tree.direction_input(   "Direction",    value=val, min_value=min_value, max_value=max_value, description="Direction")
    tree.velocity_input(    "Velocity",     value=val, min_value=min_value, max_value=max_value, description="Velocity")
    tree.acceleration_input("Acceleration", value=val, min_value=min_value, max_value=max_value, description="Acceleration")
    tree.euler_input(       "Euler",        value=val, min_value=min_value, max_value=max_value, description="Euler")
    tree.xyz_input(         "xyz",          value=val, min_value=min_value, max_value=max_value, description="xyz")
    
    # Geometry
    
    tree.geometry_input(    "Geometry",     value=None, description="Geometry")
    
    # Other
    
    tree.bool_input(        "Bool",         value=True,         description="Bool")
    tree.color_input(       "Color",        value=(.2, .3, 5),  description="Color")
    tree.string_input(      "String",       value="Def string", description="String")
    
    # Blender data

    tree.collection_input(  "Collection",   value=None,         description="Collection")
    tree.image_input(       "Image",        value=None,         description="Image")
    tree.material_input(    "Material",     value=None,         description="Material")
    tree.object_input(      "Object",       value=None,         description="Object")
    tree.texture_input(     "Texture",      value=None,         description="Texture")
```

### Input sockets

Sockets can be created with input nodes such as `Boolean` or `Value`.

``` python
with GeoNodes("Demo") as tree:
    # Input boolean
    b = tree.Boolean(True).boolean
```

A better way is to use the equivalent Tree function returning directly the desired socket:

``` python
with GeoNodes("Demo") as tree:
    bool = tree.boolean(True)
    col  = tree.color(mathutils.Color((.1, .2, .3)))
    img  = tree.image(bpy.data.images.get("Image"))
    i    = tree.integer(123)
    mat  = tree.material(bpy.data.materials.get("Material"))
    s    = tree.string("Hello")
    v    = tree.value(3.14)
    vect = tree.vector((1, 2, 3))
``` 

### Operations on Values

Value sockets are basic types such as VALUE (float), INT, STRING, BOOLEAN, VECTOR, RGBA (color), ROTATION.

Nodes operating on basic types are implemented as functions, methods and operations to allow a
"pythonistic" syntax. The operations can mix sockets and true python values.

For instance, the `Math` nodes is iemplemented in the following way:
- single argument operations
  - as Tree function, e.g. `a = tree.cos(socket)`
  - as socket method, e.g. `a = socket.cos()`
  - as unary operator, e.g. `a = -b`
- several arguments operations
  - as Tree function, e.g. `a = tree.atan2(y, x)`
  - as socket method, e.g. `a = y.atan2(x)`
  - as operator, e.g. `a = b + c`

The following example generates the nodes illustrated below:

``` python
from geonodes import GeoNodes

with GeoNodes("Some computation") as tree:
    
    x = tree.value(10)
    y = tree.value(20)
    
    distance = tree.sqrt(x**2 + y**2)

    z = 3*tree.sin(distance*10)/distance
```

<img src="images/gs_img_01.png" width="600" class="center">

### Boolean operations

The python boolean operators `and`, `or` and `not` are reserved keywords.
They are implemented with nameds `band`, `bor` and `bnot`.
The operator `*`, `+` and `-`can also be used.

``` python
with GeoNodes("Demo") as tree:
    a = tree.boolean(False)
    b = tree.bool_input("User input", True)
    
    # Operations on booleans
    c = a.band(b)      # a and b
    d = tree.bor(a, b) # a or b, function 
    e = a.bnot()       # not a

    # The folllowing lines are equivalent
    c = a * b
    d = a + b
    e = -a
```

### Vectors, Rotations and Colors automatic Separation

`VECTOR`, `ROTATION` and `RGBA` sockets have components. The nodes `SeparateXYZ` and `SeparateColor`
are use to have access to their components:

``` Python
with GeoNodes("Demo") as tree:

    vect = tree.vector_input("User vector")
    col  = tree.color_input("User color")
    
    # Separate to have acces to the components
    xyz = tree.SeparateXYZ(vect)
    rgb = tree.SeparateColor(col)
    
    # Access to the components
    n = tree.sqrt(xyz.x**2 + xyz.y**2)
    a = rgb.red
```     

The separation nodes can be automatically generated by accessing the components directly from
the sockets. The code below is equialent to the previous one:

``` Python
with GeoNodes("Demo") as tree:

    vect = tree.vector_input("User vector")
    col  = tree.color_input("User color")
    
    # Separate nodes are automatically generated by refering to the components
    
    # SeparateXYZ is automatically generated
    n = tree.sqrt(vect.x**2 + vect.y**2)
    
    # SeparateColor is automatically generated
    a = col.red # mode = 'RGB'
    b = col.hue # mode = 'HSV'
```

### Geometry primitives

Geometry can be created by using the **snake_case** version of the node name rather than the **CamelCase** version.
The **snake_case** version directly returns the geometry socket rather than the node.
If other output sockets are required, theu can be read from the `IcoSphere` node which is a property
of the socket as shown below:


``` Python
with GeoNodes("Demo") as tree:

    ico_node = tree.IcoSphere()
    ico = ico_node.mesh
    uv  = ico_node.uv_map
    
    # The lines below are equivalent
    ico = tree.ico_sphere()
    
    # If we need the uv map, the node is an attribute of the socket:
    uv = ico.node.uv_map
```

### Geometry attributes

Nodes giving geometry attributes are implemented as methods or read properties of the GEOMETRY socket.
They are properties when no parameter is required (for instance `position` or `index`).
If a parameter is required, the node is implemented as a method (for instance `named_attribute` or `handle_type_selection`).
In both case, if there is only one output socket, this single socket is returned, otherwise the node is returned.

``` python
with GeoNodes("Demo") as tree:
    
    # Get the input geometry
    geo = tree.ig
    
    # Position has not input and returns only one socket
    # property returning a vector socket
    
    vector_socket = geo.position
    
    # EndpointSelection has two input sockets and returns only one socket
    # mehod returning a boolean socket
    
    boolean_socket = geo.endpoint_selection(start_size=0, end_size=1)
    
    # SplineParameter has no input socket and returns several sockets
    # property returning a node
    
    node = geo.spline_parameter()
    
    # NamedAttribute has input sockets and returns several sockets
    # method returning a node
    
    node = geo.named_attribute()
```

<img src="images/gs_img_02.png" width="600" class="center">

### Operations on Geometry

Nodes operating on geometry accept one input GEOMETRY socket and return one output GEOMETRY socket.
These nodes are implemented as methods or write properties of the GEOMETRY socket.
The nodes is impplemenetd as a write properties when it has only one input parameter, otherwise the node
is implemented as a method.

`SetPosition` is implemented twice :
- as `position` property
- as `offset` property

> [!NOTE]
> Since `position` is also a read property, the GEOMETRY socket has a read/write property named `position`.

> [!IMPORTANT]
> Operations on geometry changes the actual socket pointed by the class GEOMETRY.
>
> For instance with `geo.position = v` :
> - before setting the position, `geo` points to the output socket of node A
> - after the operation, `geo` points to the output socket of node `SetPosition` 

``` python
with GeoNodes("Demo") as tree:
    
    # Get the input geometry
    geo = tree.ig
    
    # position is a read/write property
    geo.position = geo.position + (0, 0, 1)
    
    # One can also use the write only property offset
    # The following line is equivalent
    geo.offset = (0, 0, 1)
    
    # Transform the geometru
    geo.transform_geometry(translation=(0, 0, 1), rotation=(1, 2, 3), scale=2)
    
    # Getting the result
    tree.og = geo
```

<img src="images/gs_img_03.png" width="600" class="center">















    











  
  








































The module handles two types of classes:
- **Node** classes : by instanciating such a class, a node is created in the current tree
- **Socket** classes : the **sockets** of a node are exposed as attributes of a node class

In the example below, a node "Ico Sphere" is created and the two output sockets are used to set two python variables:

``` python
with GeoNodes("Demo") as tree:
    # Node class instanciation
    node = tree.IcoSphere(radius=2, subdivisions=3)

    # Getting the two output sockets of the node
    sphere = node.mesh
    uvmap = node.uv_map
```

**Sockets** instances are then used as input sockets of for other nodes:

``` python
with GeoNodes("Demo") as tree:
    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    node = tree.SetMaterial(geometry=sphere, material="Material")
```

**Sockets** also expose methods to create nodes in a more 'pythonist' style:

``` python
with GeoNodes("Demo") as tree:
    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    # The two following statements are equivalent

    sphere = tree.SetMaterial(geometry=sphere, material="Material").geometry

    sphere.set_material("Material")
```

### Naming conventions

The name of the classes, sockets and methods are built with the following coventions: 
- Nodes classes are **CamelCase** versions of the node name:
  - Node _'Set Shade Smooth'_ --> `SetShadeSmooth`
- Methods calling a node are **snake_case** of the Blender name:
  - `mesh.set_shade_smooth()`
- Node sockets are **snake_case** of their Blender name:
  - Socket _'Mesh'_ --> `mesh`
- When several sockets of a node share the same name, their python name is suffixed with **_i** starting from the second one:
  - `Math` has up to 3 input sockets named "Value", their python names are `value`, `value_1` and ` value_2`.
  - ***Note*** : the numbering is done for the "enabled" sockets. A node such as "Store Named Attribute" has several sockets sharing the name "Attribute" but only one at a time is enabled (the one the type of which corresponds to the data type). In that case, the node class `StoreNamedAttribute` has only one socket named `value` which points to the enabled one.
 
### Links, input and output sockets

A link is created between two nodes by **setting an input socket** with an **output socket**.

**Input sockets** are write-only attributes of the node when **Output sockets** are read-only. Hence, when a node uses the same name for an input socket and an output socket, the same name is use in the corresponding class without ambiguity.

The node "Set Shade Smooth" has an input socket and an output socket named "Geometry". The `SetShadeSmooth` class owns a single attribute named `geometry` which refers to these two sockets depending on if it is set or read:

``` python
with GeoNodes("Demo") as tree:

    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    node = tree.SetShadeSmooth()

    # Link output geometry of "Ico Sphere" Node into "Set Shade Smooth" input geometry
    node.geometry = sphere

    # Get the output socket of the node "Set Shade Smooth" for further use
    shaded_sphere = node.geometry
```

### Node parameters

Some nodes have parameters. The parameters are exposed as properties of the class. In the example below, the "Set Shade Smooth" node is created with "domain" parameter set to `'EDGE'` :

``` python
with GeoNodes("Demo") as tree:
    node = tree.SetShadeSmooth(domain='EDGE')
``` 
***Important*** : the behavior of some nodes can change with parameter settings. For instance, changing a parameter can disable and/or enable sockets. Hence, it is adviced to initialize the node parameters at creation time. The example illustrates why it is important :

``` python
with GeoNodes("Demo") as tree:
    
    # ----- WRONG
    
    # By default, "Store Named Attribute" data_type is 'FLOAT'
    # The following statement will plug to the FLOAT value
    node = tree.StoreNamedAttribute(name="V", value=tree.position())
    # Setting the parameter afterwards don't change the link previously created
    node.data_type = 'FLOAT_VECTOR'
    
    # ---- CORRECT
    
    node = tree.StoreNamedAttribute(name="V", value=tree.position(), data_type='FLOAT_VECTOR')
    
    # ----- BEST
    
    sphere = tree.IcoSphere().mesh
    sphere.store_named_vector("V", tree.position())
```

### Group inputs and outputs, constants

Group inputs and outputs sockets can be access as properties of the `tree`:
- **GeoNodes**:
  - `tree.input_geometry` or `tree.ig` : get the modfier input geometry socket
  - `tree.output_geometry` or `tree.og` : set the modifier output geometry socket
- **Shader**:
  - `tree.output_surface` : set the output surface BSDF socket
  - `tree.output_volume` : set the output volume BSDF socket
  - `tree.output_displacement` : set the output displacement socket

Geometry nodes tree allows custom input and output sockets. Use `xxx_input` to create custom sockets.

``` python
with GeoNodes("Demo") as tree:
    # Let's expose two parameters
    radius = tree.float_input("Radius", 1.)
    subs   = tree.int_input("Subdivisions", 3, min_value=1, max_value=6, description="Ico sphere subdivisions. Don't be too ambitious!")

    # An ico sphere
    tree.output_geometry = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
```

With a **GeoNodes** tree, any socket can be plugged to the output with the method `to_output(name)`.

Constant values, if required, can be created by calling snake case version of the input nodes:

``` python
with GeoNodes("Demo") as tree:
    pi = tree.value(3.1415926)
    count = tree.integer(50)
```

### Maths

Python operators can be used with sockets and between sockets and standard python value.

``` python
with GeoNodes("Demo") as tree:
    pi = tree.value(3.1415926)
    # Use input
    count = tree.integer_input("Count", 50)

    # Some strange but certainly smart computations
    angle = 2*pi/count
    a = tree.sin(angle/17)
    b = tree.cos((angle**2 + 67) % 5)

    # To node output
    (a + b).to_output("At last")
```

***Note*** : boolean operator such as `and` or `not` can't be used to generate nodes. One can use `+` and `*` between boolean sockets:

``` python
with GeoNodes("Demo") as tree:
    
    a = tree.bool_input("A", False)
    b = tree.bool_input("B", False)
    
    # a OR b
    c = a + b
    
    # a AND b
    d = a*b
    
    # NOT a
    e = -a
```
### wrap up

``` python
from geonodes import GeoNodes, Shader

# Let's build a shader specific to our amazing Geometry Nodes modifier

with Shader("Ico Shader") as tree:
    node = tree.PrincipledBSDF(base_color=(.1, .2, .3), roughness=.1)
    tree.output_surface = node.bsdf

# A variable Ico Sphere using our shader

with GeoNodes("Demo") as tree:
    # Let's expose two parameters
    radius = tree.float_input("Radius", 1.)
    subs   = tree.int_input("Subdivisions", 3, min_value=1, max_value=6, description="Ico sphere subdivisions. Don't be too ambitious!")

    # An ico sphere with our material
    sphere = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
    sphere.set_material("Ico Shader")

    # Let move it upwards
    sphere.set_position(offset=(0, 0, 2))

    # We join it with the input geometry
    geo = tree.ig + sphere

    # Let's plug it into the modifier output
    tree.output_geometry = geo
```




## Playing with an icosphere

![Result](images/ico_tuto.png)

In this example:
- Two simple materials are created to be used in the geometry node modifier
- Two modifier parameters are exposed
- The array indexing syntax is used as an alternative to the `selection` socket
- Faces are extruded based on their material index

``` python
from geonodes import GeoNodes, Shader

# Let's create the base material of the Ico Sphre

with Shader("Base Material") as tree:
    tree.output_surface = tree.PrincipledBSDF(
        base_color = (0, 0, 1),
        roughness = .9,
        ).bsdf
        
# Material for selected faces

with Shader("Sel Material") as tree:
    tree.output_surface = tree.PrincipledBSDF(
        base_color = (1, 0, 0),
        roughness = .1,
        ).bsdf
        
# The Ico Sphere modifier

with GeoNodes("Icosphere tuto") as tree:

   # Good practice: let's start with the tree inputs

   radius = tree.float_input("Radius", 1., min_value=0.01, max_value=10, description="A reasonable radius for the sphere")
   subs   = tree.integer_input("Subdivisions", 3, min_value=1, max_value=6, description="Ico Sphere d-subdivisions. Don't be too ambitious")
   
   # The icosphere
   ico = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
   
   # Base material
   ico.set_material("Base Material")

   # Faces selection
   sel = tree.random_boolean(probability=.5)

   # A geometry socket can use [sel] as an alternative to selection=sel
   # The two following statements are equivalent
   if True:
      ico[sel].set_material("Sel Material")
   else:
      ico.set_material("Sel Material", selection=sel)

   
   # Extrude the select faces
   
   ico = ico[tree.material_index().equal(2)].extrude_mesh(offset_scale=0.3)
   
   tree.og = ico
    
```

![Result](images/ico_tuto.png)





















