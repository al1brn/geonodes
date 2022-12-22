# Trees

**Trees** is a utility class to organize **Tree nodes** in consistent groups with a common prefix.
It offers an interface to call a **Tree nodes** group as a python function.

## Initialization

A **Trees** instance is simply initialized with a prefix string which can be None.
The example below initialize an instance of **Trees**.

```python
import geonodes as gn

my_group = gn.Trees("SUB")
```

## Tree nodes creation

A **Trees** instance can be used as `prefix` argument when initializing a [Tree](Tree.md).
The final name of the **Tree node** will be ***'SUB Add two values'***.


```python
import geonodes as gn

my_group = gn.Trees("SUB")

with gn.Tree("Add two values", group=True, prefix = my_group) as tree:
    
    a = gn.Float.Input(0, "A")
    b = gn.Float.Input(0, "B")
    
    (a + b).to_output("Sum")
    
with gn.Tree("Multiply two values", group=True, prefix = my_group) as tree:
    
    a = gn.Float.Input(0, "A")
    b = gn.Float.Input(0, "B")
    
    (a * b).to_output("Product")
```

## Calling a nodes group

A **Tree** can be called in another Tree node to perform a sub function. In the example above, two utilities have beend created *'SUB Add two values'* and
*'SUB Multiply two values'*. 

These **Tree** groups can be called using the snake case of their name, ignoring the prefix:
- `my_group.add_two_values`
- `my_group.multiply_two_values`

The arguments are key words argument of their input sockets.
The function return the group node. To get the actual result, simply use the snake version version of the desired output socket as shown in the full
example below:

```python
import geonodes as gn

my_group = gn.Trees("SUB")

with gn.Tree("Add two values", group=True, prefix = my_group) as tree:
    
    # Two input sockets
    # The snake case version of their name with be used as keys of kwargs
    
    a = gn.Float.Input(0, "A")
    b = gn.Float.Input(0, "B")
    
    # One output socket
    # The snake case version will be used to get the result from the node
    
    (a + b).to_output("Sum")
    
with gn.Tree("Multiply two values", group=True, prefix = my_group) as tree:
    
    # Two input sockets
    # The snake case version of their name with be used as keys of kwargs

    a = gn.Float.Input(0, "A")
    b = gn.Float.Input(0, "B")
    
    (a * b).to_output("Product")
    
with gn.Tree("A Tree for modifier") as tree:
    
    cube = gn.Mesh.Cube()
    
    # Some stupid computations !
    
    pos = cube.verts.position
    
    # Call the tree Node "SUB Add two values" with values for both sockets
    # Get the result form the Sum socket
    a = my_group.add_two_values(a=pos.x, b=pos.y).sum

    # Call the tree Node "SUB Multiply two values" with values for both sockets
    # Get the result form the Sum socket
    b = my_group.multiply_two_values(a=pos.x, b=pos.y).product
    
    pos.x = a + b
    
    cube.verts[0].position = pos
    
    tree.og = cube
```

