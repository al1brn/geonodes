
# Class DataSocket

> DataSocket initialization
  
Arguments

- socket: a node socket or a DataSocket
Passing a DataSocket instance as argument allows type casting

```python
value = Float(10.) # Float data class pointing on the output socket of node "Value"
v = Vector(value)  # Cast the previous socket to Vector
```

- node: the node owning the socket. If node is None, the initializer searchs for it in the list
of existing nodes.

- label: optional node label. Used to name the created Geometry Nodes.
  
  

## \_\_init\_\_

> DataSocket initialization
  
Arguments

- socket: a node socket or a DataSocket
Passing a DataSocket instance as argument allows type casting

```python
value = Float(10.) # Float data class pointing on the output socket of node "Value"
v = Vector(value)  # Cast the previous socket to Vector
```

- node: the node owning the socket. If node is None, the initializer searchs for it in the list
of existing nodes.

- label: optional node label. Used to name the created Geometry Nodes.
  
  

## node_chain_label

> Shortcut for `self.node.chain_label`
  
_chain_label_ property is the name to be used when automatically naming nodes.



## init_domains

Initialize the geometry domains:
- Mesh
- Vertex
- Edge
- Face
- Face corner
- Curve
- Point
- Spline
- Point cloud
- Point
- Instances
  
  

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
# 1. Creation mode
#
# to_mesh method creates a new mesh from a curve.
# The curve instance refers to the same output node socket
# We need to get the result of the method in a new variable

new_mesh = curve.to_mesh(profile_curve=circle)

# 2. Transformation mode
#
# set_shade_smooth method transformes the mesh.
# After the call, the mesh instance refers to the output socket of the
# newly created node "Set Shade Smooth". There is no need to get the result
# of the method.

mesh.set_shade_smooth()

# Note that a transformation method returns self and so, the following line
# is equivallent:

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
