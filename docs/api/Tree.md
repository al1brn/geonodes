# Class Tree

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 A geometry nodes tree.

A **Tree** class encapsulates a Blender **NodeTree**:
    
```python
    blender_tree = tree.btree # The Blender NodeTree
```

### Modifier and custom group

A Tree can be used for two purposes:
- to be used in a **Geometry Nodes** modifier (default)
- to be used as a custom [Group](Group.md) called in another Tree (`group = True`)
    
To include a custom group into a Tree, simply initialize a [Group](Group.md) class with its name as first parameter.

```python
# Call of the custom group named "Reusable Computation"
# After the name, use keyword arguments to feed the input sockets of the custom group

node = Group("Resusable Computation", ...)

# The node is supposed to return two sockets "Total value", "Average value"

total = node.total_value
avg   = node.average_value
```

### Tree creation

Once the tree is completed, the [arrange](#arrange) method makes the whole tree of nodes quite readable.
Building a tree is made between the two instructions:
    
- `tree = Tree(tree_name)` : creation / opening of the Blender NodeTree
- `tree.close()` : arrange the nodes

It is recommended to use the `with` context:
    
```python
with Tree("Geometry Nodes") as tree:
    # ... nodes creation
    
# Tree is created and arranged
```

### Layout

For a better clarity of the resulting tree, it is possible to put the newly created nodes in a layout.
The layout creation makes use of the `with` context (see [layout](#layout)):
    
```python
with Tree("Geometry Nodes") as tree:
    
    # Nodes created here are placed directly on the tree background
    
    with tree.layout("Some tricky computation"):
        
        # Nodes created here are placed in the current layout
        
        with tree.layout("The most difficult part"):
            
            # Layouts can be imbricated
            
    # Back to standard creation
```

### Input and output geometries

The input geometry is read with the **Tree** property [input_geometry](#input_geometry) or its short version [ig](#ig).

The output geometry is defined by setting the **Tree** property [output_geometry](#output_geometry) or its short version [og](#og).

The *do nothing* modifier can be written:

```python
import geonodes as gn

with gn.Tree("Do nothing") as tree:
    tree.og = tree.ig
```

### Input sockets

The **Tree** input sockets are defined with the **Input** class method of data classes.

For instance, to create an input socket of type [Float](Float.md):
    
```python
import geonodes as gn

with gn.Tree("Test") as tree:
    user_param = gn.Float.Input(.5, "Volume density", val_min=0.1, val_max=20., description="Which density do you want ?")
```

### Output sockets

To create output sockets, call the **to_output** method of data classes.

For instance, to create an output socket of type [Vector](Vector.md):
    
```python
import geonodes as gn

with gn.Tree("Test") as tree:
    vect = gn.Vector((1, 2, 3))
    vect.to_output("Some vector")
```




### Constructor

```python
Tree(self, tree_name, clear=False, group=False, fake_user=False, prefix=None)
```


#### Args:
- tree_name (str): name of the tree
- clear (bool): delete existing nodes if True
- group (bool): the tree is a custom [Group](Group.md) (no default input and output geometries)
- fake_user (bool): the fake user flag
- prefix (str or [Trees](Trees.md)): Prefix to add at the begining of the tree name




## Content

**Properties**

[cur_frame](#cur_frame) | [frame](#frame) | [ig](#ig) | [input_geometry](#input_geometry) | [og](#og) | [output_geometry](#output_geometry) | [scene](#scene) | [seconds](#seconds)

**Methods**

[activate](#activate) | [arrange](#arrange) | [check_attributes](#check_attributes) | [close](#close) | [get_bnode](#get_bnode) | [get_bnode_wrapper](#get_bnode_wrapper) | [get_bsocket_wrapper](#get_bsocket_wrapper) | [layout](#layout) | [new_group_input](#new_group_input) | [new_group_output](#new_group_output) | [new_input](#new_input) | [prev_node](#prev_node) | [register_node](#register_node) | [to_output](#to_output)

## Properties

### cur_frame

 Get the current layout for the newly created nodes.



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### frame

 The "Scene Time" output socket "frame".



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ig

 Shortcut for [input_geometry](#input_geometry).



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### input_geometry

 The group input geometry.

```python
    my_geometry = tree.input_geometry
```      



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### og

 Shortcut for [output_geometry](#output_geometry).



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### output_geometry

 The group output geometry.

```python
tree.output_geometry = my_geometry 
```



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scene

 Maintain a single instance of the node :class:`SceneTime`.



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### seconds

 The "Scene Time" output socket "seconds".



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### activate

```python
def activate(self)
```

 Set this tree as the current one.

The Tree class property ``TREE`` is set to ``self``




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arrange

```python
def arrange(self)
```

 Arrange the created nodes in the tree background for more lisibility



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### check_attributes

```python
def check_attributes(self)
```

 Check the attributes

This utility function is called when closing the tree to "solve" the attribute input nodes,
i.e. to determine if a 'Capture Attribute' node is required.

In **geonodes**, attributes are initialized as properties of a geometry.
For instance, in the following piece of code, the node 'Position' is to be the *position*
of the vertices of my_mesh:
    
```python
v = my_mesh.verts.position  # Create the node 'Position'
```
    
To actually get these vertices, a 'Capture Attribute' can be necessary. This is determined
by `check_attribute` method.

The insertion is made with the following algorithm

1. Check if capture is needed

   for each fed node:
       
   - if the node has an input geometry:
       
     - if the input geometry is the expected one:
         
       - ok
       
     - else
     
       - insertion is needed
       
   - else:
       
     - continue exploration with the nodes fed by this node

2. If insertion is needed

   - Create the 'Capture Attribute' node
   - Set the proper parameters
   - Input geometry with the owning socket
   - Output geometry to the sockets the owning socket was linked to
   - Output attribute to the sockets the attribute was connected to
   
 
Note that by initializing an attribute with geometry and domain, we have what we need to insert
a 'Capture Attribute' node:
    
```python
# Get the position of the vertices of my_mesh

v = my_mesh.verts.position

# Create the capture node

capture_node = nodes.CaptureNode(
    geometry  = my_mesh,
    value     = (output socket of Position node),
    data_type = 'VECTOR',  # We deal with position which is a Vector
    domain    = 'POINT',   # my_mesh.verts.position  --> 'POINT'
                           # my_mesh.edges.position  --> 'EDGE'
                           # my_mesh.faces.position  --> 'FACE'
    )
```           



Flag to colorize the dependancies

<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### close

```python
def close(self)
```

 Call to indicate that the tree is completed and that it can be finalized

Three actions are performed:
    
- Insertion of "Capture Attribute" nodes for attributes which require it,
  see :func:`check_attributes`.
- Insert group input nodes in frame when ok_capture_inputs is set to True
- Nodes arrangement, see :func:`arrange`.   
                                   



----- Capture attributes


<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bnode

```python
def get_bnode(self, bl_idname, label=None)
```

 Get an existing, or create a new, Blender node in the tree.

#### Args:
- bl_idname (str): the node bl_idname
- label (str): Node label
    
#### Returns:
- the blender node (bpy.types.GeometryNode)

At initialization time, some nodes (the ones which can be changed by UX) are kept
in `old_bnodes` list. Before creating a new node, this list is scaned to find a node
of the proper type and the proper label.




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bnode_wrapper

```python
def get_bnode_wrapper(self, bnode)
```

 Get the Node instance wrapping the Blender node passed in argument.

#### Args:
- bnode (bpy.types.NodeSocket): a blender node
    
#### Returns:
- The wrapping node (Node)




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bsocket_wrapper

```python
def get_bsocket_wrapper(self, bsocket)
```

 Get the DataSocket instance wrapping the Blender socket passed in argument.

#### Args:
- bsocket (bpy.types.NodeSocket): a blender socket
    
#### Returns:
- The node wrapping the socket (Node)




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### layout

```python
def layout(self, label="Layout", color=None, capture_inputs=None)
```

 Create a new layout where the newly created nodes will be placed.

#### Args:
- label (str): the layout label
- color (str or color): the layout background color
- capture_inputs (bool): if True, create a new instance fo group inputs in the frame

To be used in a `with` block:
    
```python
with tree.layout("My layout"): # Create a layout
    mesh = Mesh.UVSphere() # The node is parented in the layout
        
mesh.set_shade_smooth() # "Set Shade Smooth" node is created in the tree background
```




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### new_group_input

```python
def new_group_input(self)
```

 Create a new instance in group input.


<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### new_group_output

```python
def new_group_output(self)
```

 Create a new instance in group output.


<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### new_input

```python
def new_input(self, class_name, value=None, name=None, min_value=None, max_value=None, description="")
```

 Create a new input socket.

#### Args:
- class_name (str): class name of the value to get
- value (any): initial value
- name (str): name of the socket to create
- min_value (any): minimum value
- max_value (any): maximum value
- description (str): user tip

#### Returns:
- DataSocket

```python
res = tree.new_input('Integer', 10, "Resolution", min_value=2, max_value=100, description="Grid resolution")
```

> Don't use it directly, better call the constructor ``Input`` of data classes.

```python
res = Integer.Input(10, "Resolution", min_value=2, max_value=100, description="Grid resolution")
```




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### prev_node

```python
def prev_node(self, index)
```

 Utility which prints the configuration of a node in the console.

#### Args:
- index (int) : the unique id of the node to print
    
#### Returns:
- None

When a node is tweaked to obtain the expected result, the changes will be lost
next time the script will be run. By calling `prev_node` the parameters are printed
in the console and can be copied/pasted.




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### register_node

```python
def register_node(self, node)
```

 Register the node passed in parameter in the current tree.

#### Args:
- node (Node): The node to register
    
#### Returns:
- node

When registered, a unique id is provided to the node.
This allows the users to more clearly distinguish the nodes.




<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_output

```python
def to_output(self, socket)
```

 Create a new output socket linked to the data class.

#### Args:
- socket (DataSocket): the socket to connect to an output of the tree
Returns:
- None
    
```
tree.to_output(value)
```

Don't use it directly, better call method `to_output` of data classes.

```python
value.to_output()
```



<sub>Go to [top](#class-Tree) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

