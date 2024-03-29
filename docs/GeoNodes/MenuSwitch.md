# Node MenuSwitch

- Node name : 'Menu Switch'
- bl_idname : [GeometryNodeMenuSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeMenuSwitch.html)

> 
``` python
MenuSwitch(menu=None, data_type=None, node_label=None, node_color=None, **kwargs)
```

## Arguments
- menu (Socket=None) : Socket Menu
- data_type (str=None) : type of value sockets. If None, data_type is deduced from kwargs data types
- kwargs : socket name -> socket to select from menu

## Default sockets

In the editor, this node is created with predefined sockets name A and B.
Here, there is no predefined sockets. The names can be freely chosen.

## Menu socket

Generally, the menu socket is read from group input. There is two manners to create a group input dedicated
to the menu socket.

The first way is to explicitly create a menu socket with `tree.menu_input`. Since this method needs an
existing socket, it must be created afterwards.

As a reminder, input sockets are write only attributes. To get an input socket, it is necessary to use
the `inputs` list.

``` python
with GeoNodes("Test") as tree:
    switch_node = tree.MenuSwitch(sphere=tree.ico_sphere(), cube=tree.cube(), cone=tree.cone())
    # Input sockets are write only
    tree.menu_input("Shape", switch_node.inputs["Menu"])
    tree.og = switch_node.output
```

Since there is only one input menu, it is possible to pass directly the node rather than its menu socket:
    
``` python
with GeoNodes("Test") as tree:
    switch_node = tree.MenuSwitch(sphere=tree.ico_sphere(), cube=tree.cube(), cone=tree.cone())
    # menu_input method will take the first input menu socket
    tree.menu_input("Shape", switch_node)
    tree.og = switch_node.output
```

## Dynamic creation

The other way to create the group menu socket is to use the method `input_for_socket` as value
for the `menu` socket. This method accepts the name of the socket to create as an argument.
The following code is equivalent as the two previous pieces:
    
``` python
switch_node = tree.MenuSwitch(
    menu   = tree.input_for_socket("Shape"),
    sphere = tree.ico_sphere(),
    cube   = tree.cube(),
    cone   = tree.cone())

tree.og = switch_node.output
```


## Implementation

- Functions : [menu_switch](/docs/GeoNodes/GeoNodesTree.md#menu_switch)

