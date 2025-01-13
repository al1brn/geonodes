# Tree

``` python
Tree(tree_name: str, tree_type: str = 'GeometryNodeTree', clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: str | None = None)
```

Root class for [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) trees.

The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
and becomes the current tree.
The Tree is poped from the stack with the method [pop](tree.md#pop).

Better use the context management syntax:

``` python
with GeoNodes("My Tree"):

    # Get the current tree
    tree = Tree.current_tree

    pass

# Returns None
tree = Tree.current_tree
```

> [!IMPORTANT]
> Trees scripted with **geonodes** are kept distinct from manually created trees by putting the
> marker string _'GEONODES'_ in the description attribute. If you initialize a Tree with the
> name of an existing tree:
> - it will be cleared if it is a tree scripted with **geonodes**
> - it will be renamed if it is not the case
> This avoids to accidentally delete a manually created tree.

> [!CAUTION]
> This doesn't work with materials embedded shaders. So, make sure not to override
> a existing shader when instantiating a new [ShaderNodes](shadernodes.md#shadernodes).

The 'panel' argument is the default name to use when the tree is called from another tree using method [link_from](node.md#link_from).

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
- **clear** (_bool_ = True) : clear the current tree
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str | None_ = None) : str prefix to add at the beging of the tree name

## Content

- **A** : [arrange](tree.md#arrange)
- **C** : [clear](tree.md#clear)
- **I** : [\_\_init__](tree.md#__init__) :black_small_square: [input_node](tree.md#input_node)
- **L** : [link](tree.md#link) :black_small_square: [link_nodes](tree.md#link_nodes)
- **N** : [new_input](tree.md#new_input) :black_small_square: [new_input_from_input_socket](tree.md#new_input_from_input_socket) :black_small_square: [new_output](tree.md#new_output)
- **O** : [output_node](tree.md#output_node)
- **P** : [pop](tree.md#pop) :black_small_square: [push](tree.md#push)
- **R** : [remove_groups](tree.md#remove_groups)

## Properties



### input_node

> _type_: **Node**
>

> Return a ERROR: Node 'Group Input' not found node

If the node doesn't already exist, it is created.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Properties](tree.md#properties)</sub>

### output_node

> _type_: **Node**
>

Returns a ERROR: Node 'Group Output' not found node

If the node doesn't already exist, it is created.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Properties](tree.md#properties)</sub>

## Methods



----------
### arrange()

> method

``` python
arrange()
```

> Arrange the nodes in the editor.

Try to arrange properly the nodes from left to right.

This method is called when the Tree is poped from the stack.

#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### clear()

> method

``` python
clear()
```

Clear the content of the Tree.

Remove all the nodes in the Tree.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(tree_name: str, tree_type: str = 'GeometryNodeTree', clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: str | None = None)
```

Root class for [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) trees.

The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
and becomes the current tree.
The Tree is poped from the stack with the method [pop](tree.md#pop).

Better use the context management syntax:

``` python
with GeoNodes("My Tree"):

    # Get the current tree
    tree = Tree.current_tree

    pass

# Returns None
tree = Tree.current_tree
```

> [!IMPORTANT]
> Trees scripted with **geonodes** are kept distinct from manually created trees by putting the
> marker string _'GEONODES'_ in the description attribute. If you initialize a Tree with the
> name of an existing tree:
> - it will be cleared if it is a tree scripted with **geonodes**
> - it will be renamed if it is not the case
> This avoids to accidentally delete a manually created tree.

> [!CAUTION]
> This doesn't work with materials embedded shaders. So, make sure not to override
> a existing shader when instantiating a new [ShaderNodes](shadernodes.md#shadernodes).

The 'panel' argument is the default name to use when the tree is called from another tree using method [link_from](node.md#link_from).

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
- **clear** (_bool_ = True) : clear the current tree
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str | None_ = None) : str prefix to add at the beging of the tree name

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### link()

> method

``` python
link(out_socket, in_socket)
```

> Create a link between two sockets.

#### Arguments:
- **out_socket** (_socket_) : a node output socket
- **in_socket** (_socket_) : input socket from another node



#### Returns:
- **Link** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### link_nodes()

> method

``` python
link_nodes(from_node, to_node, include=None, exclude=[], create=True, panel=None)
```

Link two nodes

If from_node is a Group Input node, the necessary sockets can be created if 'create' argument is True.

#### Arguments:
- **from_node** : the node to get the outputs from
- **to_node** : the node to plug into
- **include** (_list_ = None) : connect only the sockets in the list
- **exclude** (_list_ = []) : exclude sockets in this list
- **create** ( = True) : create the output sockets in from_node if it is a 'Group Input Node'
- **panel** ( = None) : panel name to create, use tree default name if None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### new_input()

> classmethod

``` python
new_input(bl_idname: str, name: str, value: 'Any' = None, panel: str | None = None, **props)
```

Create a new input socket.

This is an **input socket** of the Tree, hence an **output socket** of the ERROR: Node 'Input' not found node.

#### Arguments:
- **bl_idname** (_str_) : socket bl_idname - name : Socket name - value : Default value - props : properties specific to interface socket
- **name** (_str_)
- **value** (_Any_ = None)
- **panel** (_str | None_ = None)
- **props**



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### new_input_from_input_socket()

> classmethod

``` python
new_input_from_input_socket(input_socket, name=None, panel=None)
```

Create a new group input socket from an existing input socket.

#### Arguments:
- **input_socket** (_socket_) : a node input _insocket
- **name** (_str_ = None) : name of the group input socket to create
- **panel** (_str_ = None) : name of the panel



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### new_output()

> method

``` python
new_output(bl_idname, name, panel=None, **props)
```

Create a new output socket.

This is an **output socket** of the Tree, hence an input socket of the [Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/output/output.html) node.

#### Arguments:
- **bl_idname** (_str_) : socket bl_idname - name (str) : Socket name
- **name**
- **panel** ( = None)
- **props**



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### pop()

> method

``` python
pop(clean=True)
```

> Remove this tree from the stack

> [!IMPORTANT]
> This methods shouldn't be called directly, better use a **with** context block.

Calls [arrange](tree.md#arrange) to arrange the location of the nodes.


``` python
with Tree("My Name"):
    pass
```

#### Raises:
- **NodeError** : if this tree is not the current one



#### Arguments:
- **clean** ( = True)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### push()

> method

``` python
push()
```

> Make this tree the current one

> [!IMPORTANT]
> This methods shouldn't be called directly, better use a **with** context block.

``` python
with Tree("My Name"):
    pass
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### remove_groups()

> staticmethod

``` python
remove_groups(names=None, prefix=None, geonodes=True, shadernodes=True)
```

> Remove Groups created by GeoNodes.

> [!IMPORTANT]
> This method can only remove groups created by **GeoNodes**.

#### Arguments:
- **names** (_str or list of strs_ = None) : name of the node groups to remove (all if None)
- **prefix** (_str_ = None) : name prefix for the groups to delete
- **geonodes** (_bool_ = True) : remove geometry nodes groups
- **shadernodes** ( = True)



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>