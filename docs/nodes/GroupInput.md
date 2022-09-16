
# Node GroupInput

Node *Group input*

Args:
  check_input_geometry: True for modifier
  
  
Note that the **output** sockets of this node are the **input** sockets of the group.

For modifiers, the first socket must be a geometry socket: this is the gemetry of the object on which the modifier
applies. Make sure that this socket exists.

This node is created by the Tree at initialization time. 





## \_\_init\_\_

Node *Group input*

Args:
  check_input_geometry: True for modifier
  
  
Note that the **output** sockets of this node are the **input** sockets of the group.

For modifiers, the first socket must be a geometry socket: this is the gemetry of the object on which the modifier
applies. Make sure that this socket exists.

This node is created by the Tree at initialization time. 





## \_\_getitem\_\_

Input socket by their name


## input_geometry

The default input geometry sockets.

Returns:
  Geometry: The input geometry socket
  
  
  
  

## new_socket

Create a new input socket

