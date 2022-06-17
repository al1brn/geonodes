
# Class Node

The root class for Blender node wrappers.

This class is basically intended to expose its constructor as a way to create
the associated Geometry Node. In the following example, we create a Node
supposingly have one single input socket named "geometry"
        
```python
my_node = Node(geometry=value, parameter='PARAM')
```

## Nodes naming convention

The Node sub classes are named accoridng their Blender label with a **Camel case** conversion,
for instance:

- _Set Shade Smooth_ --> SetShadeSmoth
- _Split Edges_ --> SplitEdges
_ _Normal_ --> Normal

## Sockets naming convention

The node socket are named after the Blender sockets names with a **snake case** conversion,
for instance:

- _Geometry_ --> geometry
- _Mesh 1_ --> mesh_1
  
For some nodes, (Math node for instance), several sockets can share the same name. In that case, the
sockets are numbered, starting from 0:

- Value --> value0
- Value --> value1

## Properties

- tree : Tree
  The tree the node bleongs to
- name : str
  Standard Geometry node name
- label : str
  User defined label. Can be None
- bnode : bpy.types.Node
  The actual Blender Geometry node
- inputs : list
  List of innput sockets
- outputs : list
  List of output sockets
- is_attribute : bool
  Indicates that the node is an field attribute
- bl_idname : str
  The node type name
  
  
  

## \_\_init\_\_

The root class for Blender node wrappers.

The creation tree is read in the static property Tree.TREE.

The blender Node is created by calling the method `tree.get_bnode` method.

### Arguments

- bl_idname: str
  A valid node bl_idname
- name: str
  The node name
- label: str, optional
  The node label
- node_color: color, optional
  The node color
  
  
  

## \_\_getattr\_\_

Access to the output sockets
We are idiot proof and accept capitalized versions :-)
Output sockets are "write only"


## \_\_setattr\_\_

Access to the input sockets
We are idiot proof and accept capitalized versions :-)
Input sockets are "write only"


## bl_idname

bl idname


## unitize

Class method to unitize a list of names


## get_label

Build the node label

If the label provided at initialization time is None, the node is labeled by concatening
its unique id with its standard name.



## chain_label

Chain label used when labeling chained nodes
eg: separate property of Vector is labeled: {chain_label}.separate


## input_geometry_bsocket

The input geometry socket when exists


## fed_nodes

All the fed nodes (nodes connected to one output socket)


## switch_input_sockets

Utility method switch the links fo two sockets/

Used when implementing operators




## plugged

Sockets plugged to an input socket


## plug

Plug the values to the input socket whose index is provided.

Since an input socket can be multi input, the values argument is a list.

If the socket is multi input, the plug method is called once per provide value.
If a value is None, nothing happens.

A not None value can be:
- either a valid valud for the socket (eg: 123 for Integer socket)
- or an output socket of another Node
  
When it is a socket, it can be a Blender socker or a DataSocket

### Arguments

- index: int
  The index of the input sockets (a valid index for Node.inputs)
- *values: list of values
  Each value can be an acceptable default value for the socket
  or an output socket 
  
  
  
----- Index can be a string

## plug_node

Plug all sockets with matching name


## as_attribute

Indicates that the node is an attribute

An attribute is intended to provide information from a particular geometry.

In Blender, one has to check if he has to use a Capture Node or not.

With geonodes scripting, attributes are considered as properties of geometry.
At creation time, the Node maintains a reference to the geometry it is an attribute of.
When closing the tree, all the attributes are check to see if a "Capture Node" must be
created instead of keeping the single attribute node.

See `Tree.check_attributes` method.




## connected_geometries

List of the nodes which are connected through a GEOMETRY socket


## attribute_is_solved

The attribute is "solved" when it feeds capture or transfer attribute


## Boolean

Node socket classes will be created in generated modules



  @staticmethod
  def DataSocket(socket):
    if socket.bl_idname == 'NodeSocketBool':
      return Node.Boolean(socket)
      
    elif socket.bl_idname == 'NodeSocketInt':
      return Node.Integer(socket)
      
    elif socket.bl_idname == 'NodeSocketIntUnsigned':
      return Node.Integer(socket)
      
    elif socket.bl_idname == 'NodeSocketFloat':
      return Node.Float(socket)
      
    elif socket.bl_idname == 'NodeSocketFloatFactor':
      return Node.Float(socket)
      
    elif socket.bl_idname == 'NodeSocketFloatAngle':
      return Node.Float(socket)
      
    elif socket.bl_idname == 'NodeSocketFloatDistance':
      return Node.Float(socket)
      
    elif socket.bl_idname == 'NodeSocketVector':
      return Node.Vector(socket)
      
    elif socket.bl_idname == 'NodeSocketVectorEuler':
      return Node.Vector(socket)
      
    elif socket.bl_idname == 'NodeSocketVectorXYZ':
      return Node.Vector(socket)
      
    elif socket.bl_idname == 'NodeSocketVectorTranslation':
      return Node.Vector(socket)
      
    elif socket.bl_idname == 'NodeSocketColor':
      return Node.Color(socket)
      
    elif socket.bl_idname == 'NodeSocketString':
      return Node.String(socket)
      
    elif socket.bl_idname == 'NodeSocketGeometry':
      return Node.Geometry(socket)
      
    elif socket.bl_idname == 'NodeSocketCollection':
      return Node.Collection(socket)
      
    elif socket.bl_idname == 'NodeSocketImage':
      return Node.Image(socket)
      
    elif socket.bl_idname == 'NodeSocketMaterial':
      return Node.Material(socket)
      
    elif socket.bl_idname == 'NodeSocketObject':
      return Node.Object(socket)
      
    elif socket.bl_idname == 'NodeSocketTexture':
      return Node.Texture(socket)
      
    raise RuntimeError(f"Unknown bl_idname for socket '{socket.name}': '{socket.bl_idname}'")
    
    
    