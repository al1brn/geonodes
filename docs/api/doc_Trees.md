# Class Trees

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


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

The arguments are key word, the keys beinng the snake case version their input socket names.
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
    
    # Call the group node  "SUB Add two values" with values for both sockets
    # Get the result from the Sum socket
    a = my_group.add_two_values(a=pos.x, b=pos.y).sum

    # Call the group node "SUB Multiply two values" with values for both sockets
    # Get the result from the Sum socket
    b = my_group.multiply_two_values(a=pos.x, b=pos.y).product
    
    pos.x = a + b
    
    cube.verts[0].position = pos
    
    tree.og = cube
```




### Constructor

```python
Trees(self, prefix=None)
```


#### Args:
- prefix (str): The prefix to use



## Content

**Properties**

[trees](#trees)

**Class and static methods**

[get_prefix](#get_prefix) | [prefixed_name](#prefixed_name) | [prefixed_snake](#prefixed_snake) | [snake_prefix](#snake_prefix)

**Methods**

[call](#call) | [clear](#clear)

## Properties

### trees

 Gives the list of the [Tree](Tree.md) sharing the same prefix.

#### Returns:
- Trees sharing the same prefix (list)



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### get_prefix

```python
@staticmethod
def get_prefix(prefix)
```

 Utility to get the actual string prefix from a Trees or str.

#### Args:
- prefix (str or Trees): Spec

#### Returns:
- prefix (str)



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### prefixed_name

```python
@staticmethod
def prefixed_name(prefix, name)
```

 Compute the prefixed name.

#### Args:
- prefix (str or Trees): the prefix
- name (str): the tree name
    
#### Returns:
- prefixed name (str)



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### prefixed_snake

```python
@staticmethod
def prefixed_snake(prefix, name)
```

 The snake version of the prefixed name.

The prefixed version is used as a function name to instantiate the custom group.

#### Args:
- prefix (str or Trees): the prefix
- name (str): the tree name
    
#### Returns:
- snake_case version of the prefixed name (str)



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snake_prefix

```python
@staticmethod
def snake_prefix(prefix)
```

 The snake version of the prefix.

#### Args:
- prefix (str or Trees): the prefix
    
#### Returns:
- snake_case version of the prefix



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### call

```python
def call(self, name, **kwargs)
```

 Create an instance for a **Custom Group**.

The keywords arguments must be the snake_case version of the input socket names of the group.

#### Args:
- name (str): The name of the Group (without the prefix)
- **kwargs: value of the input sockets
    
#### Returns:
- An instance of the custom group (Group)



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clear

```python
def clear(self)
```

 Delete all the **Geometry Nodes** whose name has a given prefix.

For instance, to delete all the **Geometry Nodes** whose name starts with 'Utils':

```python
Trees("Utils").clear()
```

> CAUTION: `Trees().clear()` delete all the **Geometry Nodes** of your file, including those which are not
generated with **geonodes**.



<sub>Go to [top](#class-Trees) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

