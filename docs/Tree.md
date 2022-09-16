
# Class Tree

Wrap a Blender NodeTree

:param tree_name: Name of the tree (index in ``bpy.data.node_groups``)
:param clear: delete the existing nodes
:param group: the tree node is not for a Geometry Node modifier but for a Group
:type tree_name: str
:type clear: bool
:type group: bool


A tree class encapsulates a Blender NodeTree:

.. code-block:: python

  blender_tree = tree.btree # The Blender NodeTree
  
  
Nodes are created by data sockets methods. In case of an error, the user can see the state of
the tree when the script stops.

**Creation / closure**

Once the tree is completed, the :func:`arrange` method tries to place the nodes in a readable shape.
Hence, building a tree is made between the two instructions:

- ``tree = Tree(tree_name)`` : creation / opening of the Blender NodeTree
- ``tree.close()`` : arrange the nodes
  
It is recommended to use the ``with`` context:

.. code-block:: python

  with Tree("Geometry Nodes") as tree:
  

## ... nodes creation

**The TREE static property**

The TREE static attribute of class Tree maintains the current active Tree, i.e. the tree into which
creating the new nodes. There is only one single *open* tree at a time.
The method :func:`activate` set the tree as the current one.
At creation time, a Tree instance becomes the current one.

**Layouts**

For a better clarity of the resulting tree, it is possible to put the newly created nodes in a layout.
At creation time, one can define both the layout label and color.
The layout creation makes use of the ``with`` context (see :func:`layout`):

.. code-block:: python

  with Tree("Geometry Node") as tree:
  

## Nodes created here are placed directly on the tree background

with tree.layout("Some tricky computation", color="green"):


## Nodes created here are placed in the current layout

with tree.layout("The most difficult part", color="red"):


## Layouts can be imbricated


## Back to standard creation

**Initialization**

At initialization time, the existing nodes can be deleted or kept. Use ``clear=True``
to erase all the existing nodes.

The nodes which are kept are the ones which can not be configured by script, for instance
the  *Float Curve* or  *ColorRamp* nodes. These nodes are reused when instancied in the script.
This allows not to loose nodes tuning.





## get_bnode

Get an existing, or create a new, Blender node in the tree.

:param bl_idname: The node bl_idname
:param label: Node label
:type bl_idname: str
:type name: str
:return: A geometry node
:rtype: bpy.types.GeometryNode


At initialization time, some nodes (the ones which can be changed by UX) are kept
in ``old_bnodes`` list. Before creating a new node, this list is scaned to find a node
of the proper type and the proper label.




## activate

Set this tree as the current one.

The Tree class property ``TREE`` is set to ``self``




## register_node

Register the node passed in parameter in the current tree.

:param node: The node to register
:type node: Node
:return: The node
:rtype: Node

When registered, a unique id is provided to the node.
This allows the users to more clearly distinguish the nodes.





## get_bnode_wrapper

Get the Node instance wrapping the Blender node passed in argument.

:param bnode: The geometry node to look the warpper of
:type bnode: bpy.types.NodeSocket
:return: The wrapping node
:rtype: Node
:raise: Exception if the wrapper is not found




## get_bsocket_wrapper

Get the DataSocket instance wrapping the Blender socket passed in argument.

:param bsocket: The blender socket to search the werapper of
:type bsocket: bpy.types.NodeSocket
:return: The node wrapping the socket
:rtype: Node
:raise: Exception if not found





## input_geometry

The group input geometry.

.. code-block:: python

  my_geometry = tree.input_geometry
  
  
  

## ig

Shortcut for :attr:`input_geometry`



## new_input

Create a new input socket.

:param class_name: Class name of the value to get
:param value: Initial value
:param min_value: Minimum value
:param max_value: Maximum value
:param description: User type
:type class_name: str
:type value: Depending on the class
:type min_value: Depending on the class
:type max_value: Depending on the class
:type description: str
:return: A data socket
:rtype: As defined by class_name

.. code-block:: python

  res = tree.new_input('Integer', 10, "Resolution", min_value=2, max_value=100, descriptioo="Grid resolution")
  
Don't use it directly, better call the constructor ``Input`` of data classes.

.. code-block:: python

  res = Integer.Input(10, "Resolution", min_value=2, max_value=100, descriptioo="Grid resolution")
  
  
  
  

## to_output

Create a new output socket linked to the data class.

:param socket: The data socket to plug as group output
:type socket: DataSocket

.. code-block:: python

  tree.to_output(value)
  
Don't use it directly, better call method ``to_output`` of data classes.

.. code-block:: python

  value.to_output()
  
  
  
  

## new_group_input

Create a new instance in group input.


## new_group_output

Create a new instance in group output.


## view

Connect a data socket to the viewer.

:param geometry: The geometry to connect to the viewer
:param socket: The attribute to connect to the viewer
:type geometry: Geometry
:type socket: Value

You can also call ``DataSocket.view()``





## scene

Maintain a single instance of the node :class:`SceneTime`.



## frame

The "Scene Time" output socket "frame".

Used for animation:

.. code-block:: python

  with Tree("Geometry Nodes") as tree:
    height = tree.frame / 10 # a value which is a tenth of the current frame 
    
    
    

## seconds

The "Scene Time" output socket "seconds".

Used for animation:

.. code-block:: python

  with Tree("Geometry Nodes") as tree:
    time = tree.seconds.sqrt() # a value which is the square root of the time
    
    
    

## layout

Create a new layout where the newly created nodes will be placed.

:param label: The layout label
:param color: The color of the layout
:param capture_inputs: Create a new instance fo group inputs in the frame
:type label: str
:type color: triplet, str or mathutils.Color
:type capture_inputs: bool or None

To be used in a `with` block:

.. code-block:: python

  with tree.layout("My layout"): # Create a layout
    mesh = Mesh.UVSphere() # The node is parented in the layout
    
  mesh.set_shade_smooth() # "Set Shade Smooth" node is created in the tree backrgound
  
  
  
  

## cur_frame

Get the current layout for the newly created nodes.



## call

Custom group


## check_attributes

Check the attributes

This utility function is called when closing the tree to "solve" the attribute input nodes,
i.e. to determine if a 'Capture Attribute' node is required.

In **geonodes**, attributes are initialized as properties of a geometry.
For instance, in the following piece of code, the node 'Position' is to be the *position*
of the vertices of my_mesh:

.. code-block:: python

  v = my_mesh.verts.position  # Create the node 'Position'
  
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
  
1. If insertion is needed
   
- Create the 'Capture Attribute' node
- Set the proper parameters
- Input geometry with the owning socket
- Output geometry to the sockets the owning socket was linked to
- Output attribute to the sockets the attribute was connected to
  
  
Note that by initializing an attribute with geometry and domain, we have what we need to insert
a 'Capture Attribute' node:

.. code-block:: python


### Get the position of the vertices of my_mesh

v = my_mesh.verts.position


### Create the capture node

capture_node = nodes.CaptureNode(
  geometry  = my_mesh,
  value     = (output socket of Position node),
  data_type = 'VECTOR',  # We deal with position which is a Vector
  domain    = 'POINT',   # my_mesh.verts.position  --> 'POINT'
  

### my_mesh.edges.position  --> 'EDGE'


### my_mesh.faces.position  --> 'FACE'

)






## prev_node

Utility which prints the configuration of a node in the console.

:param index: The unique id of the node to print
:type index: int

When a node is tweaked to obtain the expected result, the changes will be lost
next time the script will be run. By calling `prev_node` the parameters are printed
in the console and can be copied/pasted.




## arrange

Arrange the created nodes in the tree background for more lisibility



## close

Call to indicate that the tree is completed and that it can be finalized

Three actions are performed:

- Insertion of "Capture Attribute" nodes for attributes which require it,
  see :func:`check_attributes`.
- Insert group input nodes in frame when ok_capture_inputs is set to True
- Nodes arrangement, see :func:`arrange`.   
  
  
  
  
----- Capture attributes
