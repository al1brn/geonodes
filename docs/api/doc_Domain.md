# Class Domain

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[as_cloud_points](#as_cloud_points) | [as_control_points](#as_control_points) | [as_corners](#as_corners) | [as_edges](#as_edges) | [as_faces](#as_faces) | [as_insts](#as_insts) | [as_splines](#as_splines) | [as_verts](#as_verts) | [data_socket](#data_socket) | [domain](#domain) | [selection](#selection) | [selection_index](#selection_index)



**Methods**

[attribute_node](#attribute_node) | [select](#select) | [socket_stack](#socket_stack) | [view](#view)

## Properties

### as_cloud_points

 Type cast to CloudPoint.


### as_control_points

 Type cast to ControlPoint.


### as_corners

 Type cast to Corner.


### as_edges

 Type cast to Edge.


### as_faces

 Type cast to Face.


### as_insts

 Type cast to Instance.


### as_splines

 Type cast to Spline.


### as_verts

 Type cast to Vertex.


### data_socket

 Returns the data socket it belongs to.       

Returns:
    DataSocket



### domain

 Gives the **Geometry Nodes** domain string to use in the generated nodes.

- Vertex        : 'POINT',
- Edge          : 'EDGE',
- Face          : 'FACE',
- Corner        : 'CORNER',
- ControlPoint  : 'POINT',
- Spline        : 'CURVE',
- CloudPoint    : 'POINT',
- Instance      : 'INSTANCE',

Returns:
    domain string (str)



### selection

 Returns the selection value to use in nodes with a **Selection** socket.  

Returns:
    Boolean



### selection_index

 Returns the selection index.

> CAUTION: raise an error if the selection is not a integer.

Returns:
    Integer



## Methods

### attribute_node

```python
def attribute_node(self, node)
```

 Define an input node as attribute

Called when creating an input node in a property getter. Performs two actions:
    
    - Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
      This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
      a *Capture Attribute* for this field.
    - Set the nde property :attr:`field_of` to self in order to implement the transfer attribute
      mechanism.

#### Args:
- node (Node): The node created by the domain
    
Returns:
    The node argument        




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### select

```python
def select(self, selection)
```

 Select the domain

If the method is called on a **Domain** which already has a selection, the two selections are combined:
    
```python
verts = mesh.verts[10:20] # Selection of vertices from 10 to 20
v = verts.select((verts.index % 2).equal(0)) # Even indices in the previous selection
```

#### Args:
- selection (Boolean or Integer): The selection condition
    
Returns:
    Domain with the given selection (Domain)

If a selection is existing, the resulting selection is a logical and betwenn the two




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### socket_stack

```python
def socket_stack(self, node, socket_name=None)
```

 Make the owning socket jump to the output socket of the node passed in argumment.

#### Args:
- node (Node): The node to jump to
- socket_name: The name of the output socket (first one if None)



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, socket=None, label=None, node_color=None)
```

 To viewer.

Create a **Viewer** node with the domain geometry as input and the provided socket.

#### Args:
- socket (DataSocket): The value to view



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

