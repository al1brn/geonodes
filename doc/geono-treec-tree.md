# Tree

``` python
Tree(tree_name, tree_type='GeometryNodeTree', clear=True, fake_user=False, is_group=False, prefix=None)
```

Root class for GeoNodes and ShaderNodes trees.

The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
and becomes the current tree.
The Tree is poped from the stack with the method Tree.pop.

Better use the context management syntax:

``` python
with GeoNodes("My Tree"):

    # Get the current tree
    tree = Tree.current_tree

    pass

# Raises an error
tree = Tree.current_tree
```

> [!IMPORTANT]
> If you create a tree with an existing name, the existing Tree won't be overriden if it was not
> a tree created by **GeoNodes**. The string 'GEONODES' is added in the description attribute of
> node groups created by **GeoNodes** in order to differentiate generated Trees from yours.

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
- **clear** (_bool_ = True) : clear the current tree
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str_ = None) : str prefix to add at the beging of the tree name

## Content

- [arrange](geono-treec-tree.md#arrange)
- [clear](geono-treec-tree.md#clear)
- [input_node](geono-treec-tree.md#input_node)
- [link](geono-treec-tree.md#link)
- [new_input](geono-treec-tree.md#new_input)
- [new_input_from_input_socket](geono-treec-tree.md#new_input_from_input_socket)
- [new_output](geono-treec-tree.md#new_output)
- [output_node](geono-treec-tree.md#output_node)
- [remove_groups](geono-treec-tree.md#remove_groups)

## Properties



### input_node

> _type_: **Node**
>

Returns a Group Input Node.

If the node doesn't already exist, it is created.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Properties](geono-treec-tree.md#properties)</sub>

### output_node

> _type_: **Node**
>

Returns a Group Output Node.

If the node doesn't already exist, it is created.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Properties](geono-treec-tree.md#properties)</sub>

## Methods



----------
### arrange()

> method

``` python
arrange()
```

Arrange the nodes in the editor.

Tries to arrange properly the nodes from left to right.

This method is called when the Tree is poped from the stack.

#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>

----------
### clear()

> method

``` python
clear()
```

Clear the content of the Tree.

Remove all the nodes in the Tree.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>

----------
### link()

> method

``` python
link(out_socket, in_socket)
```

Create a link between two sockets.

#### Arguments:
- **out_socket** (_socket_) : a node output socket
- **in_socket** (_socket_) : input socket from another node



#### Returns:
- **Link** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>

----------
### new_input()

> classmethod

``` python
new_input(bl_idname, name, subtype='NONE', value=None, min_value=None, max_value=None, description='')
```

Create a new input socket.

This is an input socket of the tree, then an output socket of the input node.

#### Arguments:
- **bl_idname** (_str_) : socket bl_idname - name (str) : Socket name - value (any = None) : Default value - min_value (any = None) : Minimum value - max_value (any = None) : Maxium value - description (str = None) : user tip
- **name**
- **subtype** ( = NONE)
- **value** ( = None)
- **min_value** ( = None)
- **max_value** ( = None)
- **description** ( = )



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>

----------
### new_input_from_input_socket()

> classmethod

``` python
new_input_from_input_socket(input_socket, name=None)
```

Create a new group input socket from an existing input socket.

#### Arguments:
- **input_socket** (_socket_) : a node input socket
- **name** (_str_ = None) : name of the group input socket to create



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>

----------
### new_output()

> method

``` python
new_output(bl_idname, name)
```

Create a new output socket.

This is an output socket of the tree, then an input socket of the input node.

#### Arguments:
- **bl_idname** (_str_) : socket bl_idname - name (str) : Socket name
- **name**



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>

----------
### remove_groups()

> staticmethod

``` python
remove_groups(names=None, prefix=None, geonodes=True, shadernodes=True)
```

Remove Groups created by GeoNodes.

> [!IMPORTANT]
> This method can only remove groups created by **GeoNodes**.

#### Arguments:
- **names** (_str or list of strs_ = None) : name of the node groups to remove (all if None)
- **prefix** (_str_ = None) : name prefix for the groups to delete
- **geonodes** (_bool_ = True) : remove geometry nodes groups
- **shadernodes** ( = True)



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](geono-treec-tree.md#tree) :black_small_square: [Content](geono-treec-tree.md#content) :black_small_square: [Methods](geono-treec-tree.md#methods)</sub>