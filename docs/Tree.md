
# Class  Tree

> Wrap a Blender NodeTree
  
A tree class encapsulates a Blender NodeTree:
        
```python
blender_tree = tree.btree # The Blender NodeTree
```

Nodes are created by data sockets methods. In case of an error, the user cas see the state of
the tree when the script stops.

## Creation / closure

Once the tree is completed, the `arrange` method tries to place the nodes in the most readable way.
Hence, building a tree is made between the two instructions:
  - `tree = Tree(tree_name)` : creation / opening of the Blender NodeTree
  - `tree.close()` : arrange the nodes
    
It is recommanded to use the `with` syntax:
        
```python
with Tree("Geometry Nodes") as tree:
    # ... nodes creation
```

## The TREE static property

The TREE static attribute of class Tree maintains the current active Tree, i.e. the tree into which
creating the new nodes. There is only one single _open_ tree at a time.
The method `activate` set the tree as the current one.
At creation time, a Tree instance becomes the current one.

## Layouts

For clarity, it is possible to put the newly created nodes in a layout. At creation time, one can define
both the layout label and color. The layout creation makes use of the `with` syntax:
        
```python
with Tree("Geometry Node") as tree:
        
    # Nodes created here are placed directly on the tree background
        
    with tree.layout("Some tricky computation", color="green"):
            
        # Nodes created here are placed in the current layout
            
        with tree.layout("The most difficult part", color="red"):
                
            # Layouts can be imbricated
                
    # Back to standard creation
```

## Initialization

At initialization time, the existing nodes can be deleted or kept. Use clear=True
to erase all the existing nodes.

The nodes which are kep are the ones which can not be configured by script, for instance
the "Float Curve" or "ColorRamp" nodes. These nodes are reused when instancied in the script.
This allows not to loose nodes tuning.





## \_\_init\_\_

Initialize a new tree

### Arguments

- tree_name: str
  the name of the tree. The NodeTree is created if it doesn't exist.
- clear: bool, default is False
  earase all the existing nodes
  
  
  

## get_bnode

Get or create a new Blender node in the tree.

At initialization time, some nodes (the ones which can be changed by UX) are kept
in old_bnodes list. Before creating a new node, this list is scaned to find a node
of the proper type and the proper label.

### Arguments

- bl_idname: str
  A valid node bl_idname
- label: str, optional
  The label of the node.

### Returns

A blender Node




## activate

Set this tree as the current one.




## register_node

Register the node passed in argument in the tree.

When registered, a unique id is provided to the node.
This allows the users to more clearly distinguish the nodes.

### Arguments

node: Node




## get_bnode_wrapper

Get the Node instance wrapping the Blender node passed in argument.

### Arguments

- bnode: Blender node

### Returns

Node

### Raises

Error if not found




## get_bsocket_wrapper

Get the DataSocket instance wrapping the Blender socket passed in argument.

### Arguments

bsocket: Blender socket

### Returns

DataSocket

### Raises

Error if not found




## input_geometry

The group input geometry



## new_input

Create a new input socket

Don't use it directly, better call `DataSocket.Input(...)`



## to_output

Create a new output socket linked to the data class

Don't use it directly, better call `DataSocket.to_output(...)`



## to_viewer

Connect a data socket to the viewer

Don't use it directly, better call `DataSocket.to_viewer()`

The `Tree.to_viewer` method reuses the Viewer node if already exists.




## scene

Maintain a single instance of the node "Scene Time""



## frame

The "Scene Time" output socket "frame"

Used for animation:
            
```python
with Tree("Geometry Nodes") as tree:
    height = tree.frame / 10 # a value which is a tenth of the current frame 
```



## seconds

The "Scene Time" output socket "seconds"

Used for animation:
            
```python
with Tree("Geometry Nodes") as tree:
    time = tree.seconds.sqrt() # a value which is the square root of the time
```



## layout

Create a new layout where the newly created nodes will be placed

To be used in a `with` block:
            
```python
with tree.layout("My layout"): # Create a layout
    mesh = Mesh.UVSphere() # The node is parented in the layout
            
mesh.set_shade_smooth() # "Set Shade Smooth" node is created in the tree backrgound
```





## cur_frame

Get the current layout for the newly created nodes



## check_attributes

> Check the attributes
  
Input attributes are initialized with a socket owner

When finalizing the tree, we must check that the attribute actually feeds the expectedt geometry.
If it is not the case, we must insert a "Capture Attribute" node.

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
    - Create the capture node
    - Set the proper parameters
    - Input geometry with the owning socket
    - Output geometry to the sockets the owning socket was linked to
    - Output attribute to the sockets the attribute was connected to
      
      
      
      

## arrange

Arrange the created nodes in the tree background for more lisibility



## close

Call to indicated that the tree is completed and that it can be finalized

Two actions are performed:
  - Insertion of "Capture Attribute" nodes for attributes which require it,
    see [check_attributes](#check_attributes).
  - Nodes arrangement, see [arrange](#arrange)        
    
    
