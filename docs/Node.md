
# Class Node

The root class for Blender node wrappers.

:param bl_idname: The node bl_idname
:param name: The node name
:param label: The node label
:param node_color: The node color
:type bl_idname: str
:type name: str
:type label: str
:type node_color: triplet, str or mathutils.Color


This class is basically intended to expose its constructor as a way to create
the associated Geometry Node. In the following example, we create a Node
supposingly have one single input socket named "geometry"


.. code-block:: python

  my_node = Node(geometry=value, parameter='PARAM')
  
**Nodes naming convention**    

The Node sub classes are named according their Blender label with a **CamelCase** conversion,
for instance:

-  *Set Shade Smooth* --> ``SetShadeSmooth``
-  *Split Edges* --> ``SplitEdges``
-  *Normal* --> ``Normal``
  
**Sockets naming convention**

The node sockets are named after the Blender sockets names with a **snake_case** conversion,
for instance:

-  *Geometry* --> ``geometry``
-  *Mesh 1* --> ``mesh_1``
-  *Curve instances* --> ``curve_instances``
  
For some nodes, (Math node for instance), several sockets can share the same name. In that case, the
sockets are numbered, starting from 0:

-  *Value* --> ``value0``
-  *Value* --> ``value1``
  
  
  
  

## \_\_init\_\_

The root class for Blender node wrappers.

:param bl_idname: The node bl_idname
:param name: The node name
:param label: The node label
:param node_color: The node color
:type bl_idname: str
:type name: str
:type label: str
:type node_color: triplet, str or mathutils.Color


This class is basically intended to expose its constructor as a way to create
the associated Geometry Node. In the following example, we create a Node
supposingly have one single input socket named "geometry"


.. code-block:: python

  my_node = Node(geometry=value, parameter='PARAM')
  
**Nodes naming convention**    

The Node sub classes are named according their Blender label with a **CamelCase** conversion,
for instance:

-  *Set Shade Smooth* --> ``SetShadeSmooth``
-  *Split Edges* --> ``SplitEdges``
-  *Normal* --> ``Normal``
  
**Sockets naming convention**

The node sockets are named after the Blender sockets names with a **snake_case** conversion,
for instance:

-  *Geometry* --> ``geometry``
-  *Mesh 1* --> ``mesh_1``
-  *Curve instances* --> ``curve_instances``
  
For some nodes, (Math node for instance), several sockets can share the same name. In that case, the
sockets are numbered, starting from 0:

-  *Value* --> ``value0``
-  *Value* --> ``value1``
  
  
  
  

## \_\_getattr\_\_

Access to the output sockets
We are idiot proof and accept capitalized versions :-)
Output sockets are "write only"


## \_\_setattr\_\_

Access to the input sockets
We are idiot proof and accept capitalized versions :-)
Input sockets are "write only"


## get_output_socket

Output socket by name
We are idiot proof and accept capitalized versions :-)


## set_input_socket

Set an input socket
We are idiot proof and accept capitalized versions :-)
Input sockets are "write only"


## get_datasocket

Get the data socket by its index.

:param index: Index of the output socket to get
:type index: int
:return: The data socket at the given socket
:rtype: DataSocket

.. Note:: The index is the **user index**. It can differ from the **geometry node index** of the socket when
  several sockets share the same name. For instance the node *Random value* has several output sockets
  named *Value*. Only one is enabled at the same time. All these sockets share the same index, which is 0.
  The socket returned by ``get_datasocket`` is the one which is enabled.
  
.. code-block:: python

  import geonodes as gn
  
  with gn.Tree("Geometry Nodes") as tree:
  

### Node 'Random Value' initialized for FLOAT

v = gn.Float.Random()


### Let's explore the node

random_node = v.node


### The actual output sockets of the geometry node


### Note that we loop on bnode which is the wrapped node

print("Actual sockets:")
for i, bsocket in enumerate(random_node.bnode.outputs):
  print(i, bsocket.name, bsocket.enabled)
print()


### All the socket share the same name and user index


### The one whih is return is the enabled one

print("User sockets:")
for key in random_node.outsockets:
  socket = getattr(v.node, key)
  print(key, socket.socket_index, socket.bl_idname)
  
.. code-block:: console

  Actual sockets:
  0 Value False
  1 Value True
  2 Value False
  3 Value False
  
  User sockets:
  value 1 NodeSocketFloat                    
  
  
  

## \_\_str\_\_

Let's make thing readable


## bl_idname

Shortcut for ``self.bnode.bl_idname``



## unitize

Utility to build unique names from a list with homonyms

:param names: The list of names to unitize
:type names: list of strs
:return: list with the same number of names where homonyms are suffixed by their rank
:rtype: list of strs




## get_label

Build the node label

If the label provided at initialization time is None, the node is labeled by concatening
its unique id with its standard name.



## chain_label

Label to use when building chain labels


## input_geometry_bsocket

The input geometry blender socket


## fed_nodes

List of the node with input sockets connected with this socket



## switch_input_sockets

Utility method which switchs the links of two sockets.

:param index0: The first index
:param index1: The second index
:type index0: int
:typ index1: int

Used when implementing operators __rxxx___




## plugged

The liste of plugged sockets

:param index: the index of the socket to consider
:type index: int
:return: The list of connected sockets
:rtype: list of DataSockets




## plug

Plug the values to the input socket whose index is provided.

:param index: The index of the input sockets (a valid index for Node.inputs)
:param values: Each value can be an acceptable default value for the socket
  or an output socket 
:type index: int
:type values: list of values

Since an input socket can be multi input, the values argument is a list.

If the socket is multi input, the plug method is called once per provide value.
If a value is None, nothing happens.

A not None value can be:

- either a valid valud for the socket (eg: 123 for Integer socket)
- or an output socket of another Node
  
When it is a socket, it can be a Blender socket or a DataSocket



----- Index can be a string

## plug_node

Plug all the sockets of a node.

:param node: The node whose output sockets will be plugged
:type node: Node

Plug the output sockets of node whose name match an input socket of self.





## as_attribute

Indicates that the node is an attribute.

:param owning_socket: The owning socket it is an atribute of
:param domain: The domain if 'Capture Attribute' is necessary
:type owning_socket: DataSocket
:type domain: str

Set the property :attr:`is_atribute` to `True` to indicate that the socket
is the attribute of a Geometry.
The domain is stored in the property `domain`

see :func:`Tree.check_attributes` 




## connected_geometries

List of the connected geometries

Explore the fowards links until finding a node with an input geometry.
The resulting list will allow to determine if a 'Capture Attribute' is necessary.




## attribute_is_solved

Check if the attribute is already solved.

No need to insert a  *Capture Attribute* Node when the socket is already
connected to nodes  *Capture Attribute* or  *Transfer Attribute*.

see :func:`Tree.check_attributes` 




## Boolean

Initialize a Boolean with a DataSocket


## Integer

Initialize a Integer with a DataSocket


## Float

Initialize a Float with a DataSocket


## Vector

Initialize a Vector with a DataSocket


## Color

Initialize a Color with a DataSocket


## String

Initialize a String with a DataSocket


## Geometry

Initialize a Geometry with a DataSocket


## Curve

Initialize a Curve with a DataSocket


## Mesh

Initialize a Mesh with a DataSocket


## Points

Initialize a Points with a DataSocket


## Instances

Initialize a Instances with a DataSocket


## Volume

Initialize a Volume with a DataSocket


## Texture

Initialize a Texture with a DataSocket


## Material

Initialize a Material with a DataSocket


## Image

Initialize a Image with a DataSocket


## Collection

Initialize a Collection with a DataSocket


## Object

Initialize a Object with a DataSocket


## DataClass

Initialize a DataClass of the propert class from from the bl_idname of the socket
