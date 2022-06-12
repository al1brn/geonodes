
# Data socket DataSocket

DataSocket class, sub class and domain data type from socket bl_idname


## __init__

----- Ensure the properties are create


## is_data_socket

> An alternative to isinstance(value, DataSocket)
  
  

## gives_bsocket

Test if the argument provides a valid output socket. It can be:
- A Blender Geometry Node Socket
- An instance of DataSocket

### Arguments

- value: the argument to test

### Returns

bool



## bl_idname

> Shortcut for `self.bsocket.bl_idname`
  
  

## name

> Shortcut for `self.bsocket.name`
  
  

## is_output

> Shortcut for `self.bsocket.is_output`
  
  

## is_multi_input

> Shortcut for `self.bsocket.is_multi_output`
  
  

## links

> Shortcut for `self.bsocket.links`
  
  

## bnode

> Shortcut for `self.bsocket.node`
  
  

## node_chain_label

> Shortcut for `self.node.chain_label`
  
_chain_label_ property is the name to be used when automatically naming nodes.



## socket_index

> Return the index of the socket within the list of node sockets.
  
Depending on the _is_output_ property, the socket belongs either to _node.inputs_ or
_node.outputs_.



## connected_sockets

> Returns the list of DataSocket instances linked to this socket.
  
  

## domain_data_type

> Returns the domain to which the socket belongs
  
The correspondance table is the following:

- NodeSocketBool : 'BOOLEAN' 
- NodeSocketInt : 'INT'
- NodeSocketIntUnsigned : 'INT
- NodeSocketFloat :'FLOAT'
- NodeSocketFloatFactor : 'FLOAT'
- NodeSocketFloatAngle : 'FLOAT' 
- NodeSocketFloatDistance :'FLOAT' 
- NodeSocketVector : 'FLOAT_VECTOR'
- NodeSocketVectorEuler : 'FLOAT_VECTOR'
- NodeSocketVectorXYZ : 'FLOAT_VECTOR'
- NodeSocketVectorTranslation : 'FLOAT_VECTOR'
- NodeSocketColor : 'FLOAT_COLOR' 
- NodeSocketString : 'FLOAT_COLOR'
  
  

## get_class_name

> Get the DataSocket class name corresponding to the socket type and name.
  
The correspondance table is the following:

- NodeSocketBool : 'Boolean'
- NodeSocketInt : 'Integer' 
- NodeSocketIntUnsigned : Integer'
- NodeSocketFloat : 'Float' 
- NodeSocketFloatFactor : 'Float'
- NodeSocketFloatAngle : 'Float'
- NodeSocketFloatDistance : 'Float' 
- NodeSocketVector : 'Vector'
- NodeSocketVectorEuler : 'Vector'
- NodeSocketVectorXYZ : 'Vector' 
- NodeSocketVectorTranslation : 'Vector'
- NodeSocketColor : 'Color'
- NodeSocketString' : 'String'
- NodeSocketCollection : 'Collection'
- NodeSocketImage : 'Image'
- NodeSocketMaterial : 'Material'
- NodeSocketObject : 'Object'
- NodeSocketTexture : 'Texture'
- NodeSocketGeometry : 'Geometry'
  If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve'],
  the name is chosen as the class name.
  
  

## get_bl_idname

> Get the node socket bl_idname name from the DataSocket class
  
Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to _sub classes_:

- Unsigned: Integer sub class (NodeSocketIntUnsigned)
- Factor : Float sub class (NodeSocketFloatFactor)
- Angle : Float sub class  (NodeSocketFloatAngle)
- Distance : Float sub class (NodeSocketFloatDistance)
- Rotation : Vector sub class (NodeSocketVectorEuler)
- Xyz : Vector sub class (NodeSocketVectorXYZ)
- Translation : Vector sub class (NodeSocketVectorTranslation)
  
These additional values allow to enter angle, distance, factor... as group input values.

### Arguments

- class_name: str in
- Boolean
- Integer, Unsigned
- Float, Factor, Angle, Distance
- Vector, Rotation, Xyz, Translation
- Color
- String
- Geometry, Mesh, Points, Instances, Volume, Spline, Curve
- Image
- Material
- Texture
- Collection
- Object

### Returns

str: the name of the socket type




## get_blender_socket

The Blender socket is used to link nodes
Rather than accessing it directly, one must use the method get_blender_socket
This method can be used to implement specific code before connection


## reset_properties

The DataSocket can have properties
Reset the properties to None
It is called at initialization time to create the properties

class Vector(...):
def __init__(self, ...):
...
self.reset_properties()
...

def reset_properties(self):
super().reset_properties()
self.separate_ = None      # Created by property self.seperate() with node SeparateXyz


## stack

> Utility changing the output sockets refered by the DataSocket instance
  
Methods are implemented in two modes:
- Creation
- Transformation
  
In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.
In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
After the method return, the calling DataSocket instance refers to a new Blender output socket.

```python


### 1. Creation mode


### # to_mesh method creates a new mesh from a curve.


### The curve instance refers to the same output node socket


### We need to get the result of the method in a new variable

new_mesh = curve.to_mesh(profile_curve=circle)


### 2. Transformation mode


### # set_shade_smooth method transformes the mesh.


### After the call, the mesh instance refers to the output socket of the


### newly created node "Set Shade Smooth". There is no need to get the result


### of the method.

mesh.set_shade_smooth()


### Note that a transformation method returns self and so, the following line


### is equivallent:

mesh = mesh.set_shade_smooth()
```

The stack method changes the socket the instance refers to and reinitialize the
properties



## plug_bsocket

> Plug the values to the input Blender socket.
  
This static method is called by the DataClass method `plug(*values)`.

This method is the one which links an output socket of a node to the input
socket of another one.

Several values or DataSocket instances can be passed in the case the socket is
multi input.

If the socket is multi input, the plug method is called once per provided value.
If a value is None, nothing happens.

A not None value can be:
- either a valid value for the socket (eg: 123 for Integer socket)
- or an output socket of another Node
  
When it is a socket, it can be a Blender socker or a DataSocket

### Arguments

- bsocket: Geometry Node input socket
- *values: list of values
  Each value can be an acceptable default value for the socket
  or an output socket 
  
  
  

## plug

> Plug values in the socket (input sockets only)
  
see [plug_bsocket](#plug_bsocket)



## to_output

> Plug the data socket to the group output
  
The socket is added to the outputs of the geometry nodes tree.

**Note**: to define a data socket as the result geometry of the node, use `tree.output_geometry = my_geomety`.



## to_viewer

To viewer (for output sockets only)

