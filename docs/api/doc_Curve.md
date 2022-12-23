# Class Curve

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[bl_idname](#bl_idname) | [bnode](#bnode) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [links](#links) | [name](#name) | [node_chain_label](#node_chain_label) | [socket_index](#socket_index)

**Class and static methods**

[FromCollection](#FromCollection) | [Input](#Input) | [get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [value_data_type](#value_data_type)

**Methods**

[connected_sockets](#connected_sockets) | [get_blender_socket](#get_blender_socket) | [init_domains](#init_domains) | [init_socket](#init_socket) | [instantiate](#instantiate) | [plug](#plug) | [reroute](#reroute) | [reset_properties](#reset_properties) | [show_handles](#show_handles) | [stack](#stack) | [to_output](#to_output) | [view](#view)

## Properties

### bl_idname

 Shortcut for `self.bsocket.bl_idname`



### bnode

 Shortcut for `self.bsocket.node`



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`



### is_output

 Shortcut for `self.bsocket.is_output`



### links

 Shortcut for `self.bsocket.links`



### name

 Shortcut for `self.bsocket.name`



### node_chain_label

 Shortcut for *self.node.chain_label*



### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.




## Class and static methods

### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection

.. blid:: GeometryNodeCollectionInfo



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, name = None, description = "")
```

 Create a Geometry input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
Returns:
    Geometry: The Geometry data socket
    
Note
----
    This method create a new input socket in the Group Input node. To get the **default** input geometry,
    use :attr:`Tree.input_geometry`.
    



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

:param class_name: The class name
:type class_name: str
:return: The bl_idname associated to this class name
:rtype: str

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to *sub classes*:
    
.. list-table:: 
   :widths: 20 40
   :header-rows: 0

   * - Unsigned
     - Integer sub class (NodeSocketIntUnsigned)
   * - Factor
     - Float sub class (NodeSocketFloatFactor)
   * - Angle
     - Float sub class  (NodeSocketFloatAngle)
   * - Distance
     - Float sub class (NodeSocketFloatDistance)
   * - Rotation
     - Vector sub class (NodeSocketVectorEuler)
   * - xyz
     - Vector sub class (NodeSocketVectorXYZ)
   * - Translation
     - Vector sub class (NodeSocketVectorTranslation)
  
These additional values allow to enter angle, distance, factor... as group input values.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

:param socket: The socket to determine the class of
:param with_sub_class: Return the sub class if True
:typ socket: bpy.types.NodeSocket, Socket
:type with_sub_class: bool
:return: The name of the class associated to the bl_idname of the socket
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20 20
   :header-rows: 1
   
   * - NodeSocket
     - class name
     - sub class name
   * - NodeSocketBool 
     - 'Boolean'
     - 
   * - NodeSocketInt 
     - 'Integer'
     - 
   * - NodeSocketIntUnsigned 
     - 'Integer'
     - 'Unsigned'
   * - NodeSocketFloat 
     - 'Float' 
     - 
   * - NodeSocketFloatFactor 
     - 'Float'
     - 'Factor'
   * - NodeSocketFloatAngle  
     - 'Float'
     - 'Angle'
   * - NodeSocketFloatDistance 
     - 'Float'
     - 'Distance'
   * - NodeSocketVector 
     - 'Vector'
     - 
   * - NodeSocketVectorEuler 
     - 'Vector'
     - 'Rotation'
   * - NodeSocketVectorXYZ 
     - 'Vector'
     - 'xyz'
   * - NodeSocketVectorTranslation 
     - 'Vector'
     - 'Translation'
   * - NodeSocketColor 
     - 'Color'
     - 
   * - NodeSocketString' 
     - 'String'
     - 
   * - NodeSocketCollection 
     - 'Collection'
     - 
   * - NodeSocketImage 
     - 'Image'
     - 
   * - NodeSocketMaterial 
     - 'Material'
     - 
   * - NodeSocketObject 
     - 'Object'
     - 
   * - NodeSocketTexture 
     - 'Texture'
     - 
   * - NodeSocketGeometry
     - 'Geometry'
     - 
  
  
If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

:param value: The value to test
:type value: any
:return: True if *value* is or wraps a socket
:rtype: bool

Returns True if value is:
    
- A Blender Geometry Node Socket
- An instance of Socket        




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

 Returns the domain to which the socket belongs

:param value: The socket
:type value: any
:return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20
   :header-rows: 1

   * - Socket bl_idname
     - Domain code
   * - NodeSocketBool
     - 'BOOLEAN'
   * - NodeSocketInt               
     - 'INT'
   * - NodeSocketIntUnsigned       
     - 'INT'
   * - NodeSocketFloat            
     - 'FLOAT'
   * - NodeSocketFloatFactor       
     - 'FLOAT'
   * - NodeSocketFloatAngle        
     - 'FLOAT'
   * - NodeSocketFloatDistance     
     - 'FLOAT'         
   * - NodeSocketVector            
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorEuler       
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorXYZ         
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorTranslation
     - 'FLOAT_VECTOR'
   * - NodeSocketColor      
     - 'FLOAT_COLOR'
   * - NodeSocketString           
     - 'FLOAT_COLOR'





<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### connected_sockets

```python
def connected_sockets(self)
```

 Returns the list of Socket instances linked to this socket.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Returns the property bsocket.

:return: self.bsocket
:rtype: bpy.types.NodeSocket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instantiate

```python
def instantiate(self, count = 1, realize = False)
```

 Instantiate the geometry

#### Args:
- count: Number of instances to create
- realize: True to realize the instances
    
Returns:
    Instances or Geometry
    
The duplication is performed by instantiating the geometry along the vertices
of a Mesh Line initialized with `count` points.

The operator ``*`` can be used to operate this method with `realize = False`:
    
.. code-block::
    
    curves = curve * 10
    
    # is equivalent to
    
    curves = curve.duplicate(10, realize=False)
    




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

:param values: The output sockets. More than one values can be passed
    if the input socket is multi input.
:type values: array of bpy.types.NodeSocket, Socket, values

see :func:`plug_bsocket`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reroute

```python
def reroute(self)
```

 Reroute all output links



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.

:example:

.. code-block:: python

    class Vector(...):
        def __init__(self, ...):
             ...
             self.reset_properties()
             ...
    
         def reset_properties(self):
             super().reset_properties()
             self.separate_ = None      # Created by property self.seperate() with node SeparateXyz






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### show_handles

```python
def show_handles(self)
```

 Generate a mesh and cloud points to visualize the control points and handles

Returns:
    Geometry: The geometry can be joined to the output
    
Example:
    
    .. code-block:: python
    
        curve = ... # Curve initialization
        
        visu = curve.show_handles()
        
        tree.output_geometry = curve + visu
    




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

:param node: The new node owning the output socket to wrap
:type node: Node
:return: self

Methods are implemented in two modes:

- Creation
- Transformation

In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.

In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
After the method returns, the calling DataSocket instance refers to a new Blender output socket.
The stack method changes the socket the instance refers to and reinitialize properties

.. code-block:: python

    # 1. Creation mode
    # 
    # to_mesh method creates a new mesh from a curve.
    # The curve instance refers to the same output node socket
    # We need to get the result of the method in a new variable
    
    new_mesh = curve.to_mesh(profile_curve=circle)
    
    # 2. Transformation mode
    #
    # set_shade_smooth method transforms the mesh.
    # After the call, the mesh instance refers to the output socket of the
    # newly created node "Set Shade Smooth". There is no need to get the result
    # of the method.
    
    mesh.set_shade_smooth()
    
    # Note that a transformation method returns self and so, the following line
    # is equivallent:
    
    mesh = mesh.set_shade_smooth()





<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_output

```python
def to_output(self, name=None)
```

 Plug the data socket to the group output

:param name: The name to give to the modifier output
:type name: str

The socket is added to the outputs of the geometry nodes tree.

.. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

 Link the data socket to the viewer

If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.

If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
accordingly.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

