
# Node GroupOutput

Node *Group Output*

Args:
  check_output_geometry: True for modifier

## Note

The **input** sockets of this node are the **output** sockets of the group.

This node is created by the Tree at initialization time. 

.. blid:: NodeGroupOutput





## \_\_init\_\_

Node *Group Output*

Args:
  check_output_geometry: True for modifier

### Note

The **input** sockets of this node are the **output** sockets of the group.

This node is created by the Tree at initialization time. 

.. blid:: NodeGroupOutput





## output_geometry

The output geometry socket of the tree.

Returns:
  Geometry: The output geometry
  
For a tree modifier, the first output socket of the group must be a geometry.




## to_output

Plug the socket as an output of the tree.

Args:
  socket: The socket to plug
  name: The name to display
  
  
  
  
