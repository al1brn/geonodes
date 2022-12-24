# Class Group

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 > Node group

Node groups are dynamically built by reading the input and output sockets of the group.

Input sockets are initialized in the keyword arguments.

They can later on be initialized by the snake_case names




### Constructor

```python
Group(self, node_name, **kwargs)
```

## Content

**Properties**

[bl_idname](#bl_idname) | [chain_label](#chain_label) | [fed_nodes](#fed_nodes) | [input_geometry_bsocket](#input_geometry_bsocket) | [label](#label) | [node_color](#node_color)

**Class and static methods**

[Boolean](#Boolean) | [Collection](#Collection) | [Color](#Color) | [Curve](#Curve) | [Curves](#Curves) | [DataClass](#DataClass) | [Float](#Float) | [Geometry](#Geometry) | [Image](#Image) | [Instances](#Instances) | [Integer](#Integer) | [Material](#Material) | [Mesh](#Mesh) | [Object](#Object) | [Points](#Points) | [String](#String) | [Texture](#Texture) | [Vector](#Vector) | [Volume](#Volume) | [build_unames_dict](#build_unames_dict) | [unitize](#unitize)

**Methods**

[as_attribute](#as_attribute) | [attribute_is_solved](#attribute_is_solved) | [connected_geometries](#connected_geometries) | [get_datasocket](#get_datasocket) | [get_label](#get_label) | [get_output_socket](#get_output_socket) | [plug](#plug) | [plug_node](#plug_node) | [plugged](#plugged) | [switch_input_sockets](#switch_input_sockets)

## Properties

### bl_idname

 Shortcut for ``self.bnode.bl_idname``



<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### chain_label

 Label to use when building chain labels


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fed_nodes

 List of the node with input sockets connected with this socket



<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### input_geometry_bsocket

 The input geometry blender socket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### label

 Node label


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### node_color

 Noe color


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Boolean

```python
@staticmethod
def Boolean(socket)
```

 Initialize a Boolean with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Collection

```python
@staticmethod
def Collection(socket)
```

 Initialize a Collection with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Color

```python
@staticmethod
def Color(socket)
```

 Initialize a Color with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Curve

```python
@staticmethod
def Curve(socket)
```

 Initialize a Curve with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Curves

```python
@staticmethod
def Curves(socket)
```

 Initialize a Curves with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### DataClass

```python
@staticmethod
def DataClass(socket)
```

 Initialize a DataClass of the property class from from the bl_idname of the socket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Float

```python
@staticmethod
def Float(socket)
```

 Initialize a Float with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Geometry

```python
@staticmethod
def Geometry(socket)
```

 Initialize a Geometry with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Image

```python
@staticmethod
def Image(socket)
```

 Initialize a Image with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Instances

```python
@staticmethod
def Instances(socket)
```

 Initialize a Instances with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Integer

```python
@staticmethod
def Integer(socket)
```

 Initialize a Integer with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Material

```python
@staticmethod
def Material(socket)
```

 Initialize a Material with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Mesh

```python
@staticmethod
def Mesh(socket)
```

 Initialize a Mesh with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Object

```python
@staticmethod
def Object(socket)
```

 Initialize a Object with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Points

```python
@staticmethod
def Points(socket)
```

 Initialize a Points with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### String

```python
@staticmethod
def String(socket)
```

 Initialize a String with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Texture

```python
@staticmethod
def Texture(socket)
```

 Initialize a Texture with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Vector

```python
@staticmethod
def Vector(socket)
```

 Initialize a Vector with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Volume

```python
@staticmethod
def Volume(socket)
```

 Initialize a Volume with a DataSocket


<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### build_unames_dict

```python
@staticmethod
def build_unames_dict(bsockets)
```

snake_case version of the sockets names

<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### unitize

```python
@staticmethod
def unitize(names)
```

 Utility to build unique names from a list with homonyms

:param names: The list of names to unitize
:type names: list of strs
:return: list with the same number of names where homonyms are suffixed by their rank
:rtype: list of strs




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### as_attribute

```python
def as_attribute(self, owning_socket, domain='POINT')
```

 Indicates that the node is an attribute.

:param owning_socket: The owning socket it is an atribute of
:param domain: The domain if 'Capture Attribute' is necessary
:type owning_socket: DataSocket
:type domain: str

Set the property :attr:`is_atribute` to `True` to indicate that the socket
is the attribute of a Geometry.
The domain is stored in the property `domain`

see :func:`Tree.check_attributes` 




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_is_solved

```python
def attribute_is_solved(self)
```

 Check if the attribute is already solved.

No need to insert a  *Capture Attribute* Node when the socket is already
connected to nodes  *Capture Attribute* or  *Transfer Attribute*.

see :func:`Tree.check_attributes` 




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### connected_geometries

```python
def connected_geometries(self)
```

 List of the connected geometries

Explore the fowards links until finding a node with an input geometry.
The resulting list will allow to determine if a 'Capture Attribute' is necessary.




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_datasocket

```python
def get_datasocket(self, index)
```

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
        
        # Node 'Random Value' initialized for FLOAT
        
        v = gn.Float.Random()
        
        # Let's explore the node
         
        random_node = v.node
        
        # The actual output sockets of the geometry node
        # Note that we loop on bnode which is the wrapped node
        
        print("Actual sockets:")
        for i, bsocket in enumerate(random_node.bnode.outputs):
            print(i, bsocket.name, bsocket.enabled)
        print()
    
        # All the socket share the same name and user index
        # The one whih is return is the enabled one
            
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




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_label

```python
def get_label(self)
```

 Build the node label

If the label provided at initialization time is None, the node is labeled by concatening
its unique id with its standard name.



<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_output_socket

```python
def get_output_socket(self, name)
```

ock_ind = self.outsockets.get(name.lower())

<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug

```python
def plug(self, index, *values)
```

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

<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug_node

```python
def plug_node(self, node)
```

 Plug all the sockets of a node.

:param node: The node whose output sockets will be plugged
:type node: Node

Plug the output sockets of node whose name match an input socket of self.





<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plugged

```python
def plugged(self, index)
```

 The liste of plugged sockets

:param index: the index of the socket to consider
:type index: int
:return: The list of connected sockets
:rtype: list of DataSockets




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_input_sockets

```python
def switch_input_sockets(self, index0, index1)
```

 Utility method which switchs the links of two sockets.

:param index0: The first index
:param index1: The second index
:type index0: int
:typ index1: int

Used when implementing operators __rxxx___




<sub>Go to [top](#class-Group) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

