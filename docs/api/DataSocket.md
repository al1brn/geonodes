# Class DataSocket

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Wrapper of a node socket.

**DataSocket** represents the data (Geometry, Value, String, Material...) associated to a node socket.

**DataSocket** is the base class for actual data sockets:
- [Geometry](Geometry.md)
- [Boolean](Boolean.md)
- [Integer](Integer.md)
- [Float](Float.md)
- [Vector](Vector.md)
- [Color](Color.md)
- [String](String.md)
- [Collection](Collection.md)
- [Object](Object.md)
- [Material](Material.md)
- [Texture](Texture.md)
- [Image](IMage.md)
    
**DataSockets** are created by input nodes, for instance, in the following example, `cube` is a **Mesh** **DataSocket**
wrapping the output socket of the Blender Node *'Cube'*:    
    
```python
cube = Mesh.Cube()
```

Some methods change the node socket wrapped by the **DataSocket** instance. For instance, in the following example
the `cube` **DataSocket**:
- before the call, wraps the output socket of the Blender Node *'Cube'*
- after the call, wraps the output socket of the Blender Node *'Set Shade Smooth'*
    
```python
cube.set_shade_smooth(True)
```

Some methods return a new **DataSocket** instance:
    
```python
volume = cube.to_volume()
```

### Attributes

Attribute **DataSockets** keep a reference to the geometry they are an attribute of. By analyzing, the use
of attribute sockets, it is possible to automatically generate a *'Capture Attribute'* node when necessary.

In the example below, the `index` variable of type [Integer](Integer.md) (a sub class of **DataSocket**) keeps
a reference of the `cube` geometry as being the geometry it is the index of (also see [Domain](Domain.md) for
the `verts` property):
    
```python
index = cube.verts.index
```

Depending on how `index` will be used, a 'Capture Attribute' node will be generated on the `cube` wrapped
socket if necessary.




### Constructor

```python
DataSocket(self, socket, node=None, label=None)
```


#### Args:
- socket (bpy.types.NodeSocket or DataSocket): the socket to wrap
- node (Node): the node owning the socket
- label (str): the label to use for the node




## Content

**Properties**

[bl_idname](#bl_idname) | [bnode](#bnode) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [is_plugged](#is_plugged) | [links](#links) | [name](#name) | [node_chain_label](#node_chain_label) | [socket_index](#socket_index)

**Class and static methods**

[get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [python_type_to_socket](#python_type_to_socket) | [value_data_type](#value_data_type)

**Methods**

[connected_sockets](#connected_sockets) | [get_blender_socket](#get_blender_socket) | [init_domains](#init_domains) | [init_socket](#init_socket) | [plug](#plug) | [reroute](#reroute) | [reset_properties](#reset_properties) | [stack](#stack) | [to_output](#to_output)

## Properties

### bl_idname

 Shortcut for `self.bsocket.bl_idname`

#### Returns:
- socket bl_idname (str)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### bnode

 Shortcut for `self.bsocket.node`

#### Returns:
- Blender node (bpy.types.Node)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`

#### Returns:
- is multi input socket (bool)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_output

 Shortcut for `self.bsocket.is_output`

#### Returns:
- is an aoutput socket (bool)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_plugged

 Indicates if the socket is connected or not.

Raise an exception if called on an output socket.

#### Returns:
- is plugged (bool)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### links

 Shortcut for `self.bsocket.links`      

#### Returns:
- list of links (list)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### name

 Shortcut for `self.bsocket.name`

#### Returns:
- socket name (str)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### node_chain_label

 Shortcut for *self.node.chain_label*



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.

#### Returns:
- socket index (int)




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to **sub classes**:
    
| Sub class                 | bl_idname                     |
|---------------------------|-------------------------------|
| Unsigned                  | NodeSocketIntUnsigned         |
| Factor                    | NodeSocketFloatFactor         |
| Angle                     | NodeSocketFloatAngle          |
| Distance                  | NodeSocketFloatDistance       |
| Rotation                  | NodeSocketVectorEuler         |
| xyz                       | NodeSocketVectorXYZ           |
| Translation               | NodeSocketVectorTranslation   |
  
These additional values allow to enter angle, distance, factor... as group input values.

#### Args:
- class_name (str): the name of the class
    
#### Returns:
- bl_idname (str)




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

| Socket bl_idname              | Geondes class name    | Sub class             |
|-------------------------------|-----------------------|-----------------------|
| NodeSocketBool                | Boolean               | None                  |
| NodeSocketInt                 | Integer               | None                  |
| NodeSocketIntUnsigned         | Integer               | NoUnsigned            |
| NodeSocketFloat               | Float                 | None                  |
| NodeSocketFloatFactor         | Float                 | Factor                |
| NodeSocketFloatAngle          | Float                 | Angle                 |
| NodeSocketFloatDistance       | Float                 | Distance              |
| NodeSocketVector              | Vector                | None                  |
| NodeSocketVectorEuler         | Vector                | Rotation              |
| NodeSocketVectorXYZ           | Vector                | xyz                   |
| NodeSocketVectorTranslation   | Vector                | Translation           |
| NodeSocketColor               | Color                 | None                  |
| NodeSocketString              | String                | None                  |
| NodeSocketCollection          | Collection            | None                  |
| NodeSocketImage               | Image                 | None                  |
| NodeSocketMaterial            | Material              | None                  |
| NodeSocketObject              | Object                | None                  |
| NodeSocketTexture             | Texture               | None                  |
| NodeSocketGeometry            | Geometry              | None                  |

If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.

#### Args:
- socket (bpy.type.NodeSocket): the socket to use
- with_sub_class (bool): return as as second value the sub type of the socket
        



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

#### Args:
- value (any): The value to test
    
#### Returns:
- value is bpy.types.NodeSocket or Socket (bool)




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

#### Args:
- value (any): The value to test
    
#### Returns:
- is a socket (bool)



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

#### Args:
- value (any): The value to test
    
#### Returns:
- is a socket (bool)




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### python_type_to_socket

```python
@staticmethod
def python_type_to_socket(value, bl_idname, raise_exception=True)
```

 Convert a python value to a value which can be plug in the socket.

The following table gives the conversion rules:
    
| Socket type       | Conversion                                                    |
|-------------------|---------------------------------------------------------------|
| Boolean           | bool(value)                                                   |
| Integer           | int(value)                                                    |
| Float             | float(value)                                                  |
| Vector            | A triplet or the value if compatible (mathutils.Vector,...)   |
| Color             | A quadruplet or the value if compatible (mathutils.Color,...) |
| String            | str(value)                                                    |
| Collection        | value is value is a collection, bpy.data.collections[value] otherwise |
| Object            | value is value is an object, bpy.data.objects[value] otherwise        |
| Image             | value is value is an image, bpy.data.images[value] otherwise          |
| Texture           | value is value is a texture, bpy.data.textures[value] otherwise       |
| Material          | value is value is a material, bpy.data.materials[value] otherwise     |

This method allows in particular to refer to Blender resources by their name:
    
```python
# Set a material to a mesh
mesh.faces.material = "Material"

# Is equivalent to
mesh.faces.material = bpy.data.materials["Material"]
```

#### Args:
- value (any): the value to convert
- bl_idname (str): the socket bl_idname
- raise_exception (bool): False to avod raising an exception in case of error.




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color='FLOAT_COLOR')
```

 Returns the data type to which the socket belongs.

This methods is used to compute the **data_type** value in nodes accepting multitype values.

|    Socket                     |    data_type    |
|-------------------------------|-----------------|
| NodeSocketBool                | 'BOOLEAN'       |
| NodeSocketInt                 | 'INT'           |
| NodeSocketIntUnsigned         | 'INT'           |
| NodeSocketFloat               | 'FLOAT'         |
| NodeSocketFloatFactor         | 'FLOAT'         |
| NodeSocketFloatAngle          | 'FLOAT'         |
| NodeSocketFloatDistance       | 'FLOAT'         |
| NodeSocketVector              | 'FLOAT_VECTOR'  |
| NodeSocketVectorEuler         | 'FLOAT_VECTOR'  |
| NodeSocketVectorXYZ           | 'FLOAT_VECTOR'  |
| NodeSocketVectorTranslation   | 'FLOAT_VECTOR'  |
| NodeSocketColor               | color           |                

#### Args:
- value (any): the value to analyze
- default (str): default data_type
- color (str): code for color data_type
    
#### Returns:
- the data type of the value





<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### connected_sockets

```python
def connected_sockets(self)
```

 Returns the list of Socket instances linked to this socket.

#### Returns:
- list of connected sockets (list of Sockets)




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Returns the property bsocket.

#### Returns:
- bsocket (bpy.types.NodeSocket)




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

#### Args:
- values (any): The output sockets. More than one values can be passed if the input socket is multi input.
    
#### Returns:
- None



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reroute

```python
def reroute(self)
```

 Reroute all output links



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

After the call, **the DataSocket** instance wraps a different socket, typically in a newly created node.
This is an internally used by the **geonodes** engine.

In the following example, the `mesh`

```python

# After the following instruction, mesh wraps the output socket of the Cube node
mesh = Mesh.Cube()

# After the following instruction, mesh wraps the output socket of the Set Shade Smooth node
mesh.set_shade_smooth(True)
```

    
#### Args:
- node (Node): the new node
- socket_name (str): name of the outpout socket in the node. If None, takes the first output socket of the node.
    
#### Returns:
- self




<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_output

```python
def to_output(self, name=None)
```

 Create a new output socket in the Tree and plug the **DataSocket** to it.

The socket is added to the outputs of the geometry nodes tree.

> Note: To define a data socket as the result geometry of the tree, use the property `output_geometry` of 
  the current [Tree](Tree.md#output_geometry).

The created socket can be read from within another [Tree](Tree.md) by:
    - creating a [Group](Group.md): `node = Group(tree_name, **kwargs)`
    - using the snake_case version of the socket: `ver = node.socket_name`

#### Args:
- name (str): User name of the socket
    
#### Returns:
- None



<sub>Go to [top](#class-DataSocket) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

