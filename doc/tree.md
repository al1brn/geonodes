# Tree

``` python
Tree(tree_name: str, tree_type: str = 'GeometryNodeTree', clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: str = '')
```

Root class for [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) trees.

The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
and becomes the current tree.
The Tree is poped from the stack with the method [pop](tree.md#pop).

Better use the context management syntax:

``` python
with GeoNodes("My Tree") as tree:

    pass

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

The 'panel' argument is the default name to use when the tree is called from another tree using method ['#link_from' not found]().

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
- **clear** (_bool_ = True) : clear the current tree
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str_ = ) : str prefix to add at the beging of the tree name

## Content

- **A** : [arrange](tree.md#arrange)
- **C** : [clear](tree.md#clear) :black_small_square: [create_input_from_socket_OLD](tree.md#create_input_from_socket_old) :black_small_square: [create_input_socket](tree.md#create_input_socket) :black_small_square: [create_output_socket_OLD](tree.md#create_output_socket_old) :black_small_square: [current_tree](tree.md#current_tree)
- **G** : [get_in_socket](tree.md#get_in_socket) :black_small_square: [get_signature](tree.md#get_signature)
- **I** : [\_\_init__](tree.md#__init__) :black_small_square: [input_node](tree.md#input_node) :black_small_square: [is_geonodes](tree.md#is_geonodes) :black_small_square: [is_shader](tree.md#is_shader)
- **L** : [link](tree.md#link) :black_small_square: [link_nodes](tree.md#link_nodes)
- **O** : [output_node](tree.md#output_node)
- **P** : [pop](tree.md#pop) :black_small_square: [push](tree.md#push)
- **R** : [remove_groups](tree.md#remove_groups)

## Properties



### input_node

> _type_: **Node**
>

> Return a [Group Input](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../compositing/types/input/group_input.html) node

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
### create_input_from_socket_OLD()

> method

``` python
create_input_from_socket_OLD(input_socket, name=None, panel='', **props)
```

Create a new group input socket from an existing input socket.

#### Arguments:
- **input_socket** (_socket_) : a node input _insocket
- **name** (_str_ = None) : name of the group input socket to create
- **panel** (_str_ = ) : name of the panel
- **props** (_dict_) : input socket properties



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### create_input_socket()

> method

``` python
create_input_socket(bl_idname, name, panel='', **props)
```

Create a new input socket.

This is an **input socket** of the zone, hence an **output socket** of the input node.

#### Arguments:
- **bl_idname** (_str_) : socket bl_idname - name (str): Socket name - panel (str = "") : Panel to place the socket in - props : properties specific to interface socket
- **name**
- **panel** ( = )
- **props**



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### create_output_socket_OLD()

> method

``` python
create_output_socket_OLD(socket, name=None, panel='', **props)
```

Create a new output socket.

This is an **output socket** of the Tree, hence an input socket of the [Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/output/output.html) node.

#### Arguments:
- **socket** (_socket_) : socket
- **name** (_str_ = None) : Socket name
- **panel** (_str_ = ) : Panel name
- **props**



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### current_tree()

> staticmethod

``` python
current_tree()
```

> Get the Current Tree.

Returns None if no tree is currently open

#### Returns:
- **Tree** : current tree or None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### get_in_socket()

> method

``` python
get_in_socket(name: str, panel: str = '')
```

Get an existing socket within a panel

#### Arguments:
- **name** (_str_) : name of the socket
- **panel** (_str_ = ) : panel name



#### Returns:
- **Socket** : None if not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### get_signature()

> method

``` python
get_signature(include: list = None, exclude: list = [], enabled_only=True, with_sockets: bool = False)
```

Build the closure signature of the tree.

The closure signature is the tuple made of the outpout signature of the input node
and the input signature of the output node

#### Arguments:
- **include** (_list_ = None)
- **exclude** (_list_ = [])
- **enabled_only** ( = True)
- **with_sockets** (_bool_ = False)



#### Returns:
- **Signature** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(tree_name: str, tree_type: str = 'GeometryNodeTree', clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: str = '')
```

Root class for [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) trees.

The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
and becomes the current tree.
The Tree is poped from the stack with the method [pop](tree.md#pop).

Better use the context management syntax:

``` python
with GeoNodes("My Tree") as tree:

    pass

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

The 'panel' argument is the default name to use when the tree is called from another tree using method ['#link_from' not found]().

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
- **clear** (_bool_ = True) : clear the current tree
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str_ = ) : str prefix to add at the beging of the tree name

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### is_geonodes()

> classmethod

``` python
is_geonodes()
```

> Current Tree is Geometry Nodes.

#### Returns:
- **True** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### is_shader()

> classmethod

``` python
is_shader()
```

> Current Tree is Shader Nodes.

#### Returns:
- **True** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### link()

> method

``` python
link(out_socket, in_socket, handle_dynamic_sockets=False)
```

> Create a link between two sockets.

#### Arguments:
- **out_socket** (_socket_) : a node output socket
- **in_socket** (_socket_) : input socket from another node
- **handle_dynamic_sockets** ( = False)



#### Returns:
- **Link** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### link_nodes()

> method

``` python
link_nodes(from_node, to_node, include=None, exclude=[], create=True, panel='')
```

Link two nodes

If from_node is a Group Input node, the necessary sockets can be created if 'create' argument is True.

#### Arguments:
- **from_node** : the node to get the outputs from (i.e. tree Input Node)
- **to_node** : the node to plug into
- **include** (_list_ = None) : connect only the sockets in the list (or panels)
- **exclude** (_list_ = []) : exclude sockets in this list (or panels)
- **create** ( = True) : create tree input sockets  (i.e. node output sockets) in from_node if it is a 'Group Input Node'
- **panel** (_str_ = ) : panel name to create, use tree default name if None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### pop()

> method

``` python
pop()
```

> Remove this tree from the stack

> [!IMPORTANT]
> This methods shouldn't be called directly, better use a **with** context block.


``` python
with Tree("My Name"):
    pass
```

#### Raises:
- **NodeError** : if this tree is not the current one

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### push()

> method

``` python
push()
```

> Make this tree zone the current one

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