# Tree

``` python
Tree(tree_name: str, tree_type: str = 'GeometryNodeTree', *, fake_user: bool = False, is_group: bool = False, prefix: str = '', replace_material: bool = False)
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

!!! important
> Trees scripted with **geonodes** are kept distinct from manually created trees by putting the
> marker string _'GEONODES'_ in the description attribute. If you initialize a Tree with the
> name of an existing tree:
> - it will be replaced if it is a tree scripted with **geonodes**
> - it will be renamed if it is not the case
> This avoids to accidentally delete a manually created tree.

> [!CAUTION]
> This doesn't work with shaders embedded in a Material. It is why the argument `replace_material` is set to False
> by default when creating a Shader. Hence, an existing material is not replaced by a geonodes scripts
> except if you change the default value of `replace_material` argument to True.

``` python
# Create the material if it doesn't exist
# Do nothing if it already exists
with ShaderNodes("My Material"):
    pass
    
# Replace the existing material
with ShaderNodes("My Material", replace_material=True):
    pass
```

!!! note
> `prefix` argument is added at the begining of the name.

``` python
# The two following modifiers have the same name

with GeoNodes("My Modifier", prefix="Utils"):
    pass
    
with GeoNodes("Utils My Modifier"):
    pass
````

The `prefix` is usefull for big projects with numerous Groups and when you want the Groups to be sorted by their name.
You can then use the special class `G` to call the groups as python functions:

``` python
# Prefix
util = "Util"
math = "Math"

# Util Change Shape
with GeoNodes("Change Shape", prefix=util):
    pass
    
# Util Rotate
with GeoNodes("Rotate", prefix=util):
    pass
    
# Math Multiply
with GeoNodes("Multiply", prefix=math)
    pass
    
# Math Divide
with GeoNodes("Divide", prefix=math)
    pass
    
# Call the groups
with GeoNodes("My Modifier"):
    # Call a math group with the special class G
    a = G(math).divide(...)
```

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str_ = ) : prefix to add at the begining of the tree name
- **replace_material** (_bool_ = False) : replace the existing matertial if True

## Content

- **A** : [add_method](tree.md#add_method) :black_small_square: [arrange](tree.md#arrange)
- **C** : [clear](tree.md#clear) :black_small_square: [create_input_socket](tree.md#create_input_socket) :black_small_square: [current_tree](tree.md#current_tree)
- **G** : [get_signature](tree.md#get_signature)
- **I** : [\_\_init__](tree.md#__init__) :black_small_square: [input_node](tree.md#input_node) :black_small_square: [is_geonodes](tree.md#is_geonodes) :black_small_square: [is_shader](tree.md#is_shader)
- **L** : [link](tree.md#link)
- **O** : [output_node](tree.md#output_node)
- **P** : [pop](tree.md#pop) :black_small_square: [push](tree.md#push)
- **R** : [register_node](tree.md#register_node) :black_small_square: [remove_groups](tree.md#remove_groups)

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
### add_method()

> method

``` python
add_method(target_class: type, func_name: str = None, self_attr: str = None, ret_class: type = None, **fixed)
```

Add a method calling the Group.

#### Arguments:
- **target_class** (_type_) : class to add the method to
- **func_name** (_str_ = None) : name of the method to create (snae case version of group name if None)
- **self_attr** (_str_ = None) : self name attribute name
- **ret_class** (_type_ = None) : class to use to transtype the output socket
- **fixed** (_dict_) : fixed values for sockets

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

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
clear(keep_nodes: bool = True)
```

Clear the content of the Tree.

Remove all the nodes in the Tree.

#### Arguments:
- **keep_nodes** (_bool_ = True)

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
__init__(tree_name: str, tree_type: str = 'GeometryNodeTree', *, fake_user: bool = False, is_group: bool = False, prefix: str = '', replace_material: bool = False)
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

!!! important
> Trees scripted with **geonodes** are kept distinct from manually created trees by putting the
> marker string _'GEONODES'_ in the description attribute. If you initialize a Tree with the
> name of an existing tree:
> - it will be replaced if it is a tree scripted with **geonodes**
> - it will be renamed if it is not the case
> This avoids to accidentally delete a manually created tree.

> [!CAUTION]
> This doesn't work with shaders embedded in a Material. It is why the argument `replace_material` is set to False
> by default when creating a Shader. Hence, an existing material is not replaced by a geonodes scripts
> except if you change the default value of `replace_material` argument to True.

``` python
# Create the material if it doesn't exist
# Do nothing if it already exists
with ShaderNodes("My Material"):
    pass
    
# Replace the existing material
with ShaderNodes("My Material", replace_material=True):
    pass
```

!!! note
> `prefix` argument is added at the begining of the name.

``` python
# The two following modifiers have the same name

with GeoNodes("My Modifier", prefix="Utils"):
    pass
    
with GeoNodes("Utils My Modifier"):
    pass
````

The `prefix` is usefull for big projects with numerous Groups and when you want the Groups to be sorted by their name.
You can then use the special class `G` to call the groups as python functions:

``` python
# Prefix
util = "Util"
math = "Math"

# Util Change Shape
with GeoNodes("Change Shape", prefix=util):
    pass
    
# Util Rotate
with GeoNodes("Rotate", prefix=util):
    pass
    
# Math Multiply
with GeoNodes("Multiply", prefix=math)
    pass
    
# Math Divide
with GeoNodes("Divide", prefix=math)
    pass
    
# Call the groups
with GeoNodes("My Modifier"):
    # Call a math group with the special class G
    a = G(math).divide(...)
```

#### Arguments:
- **tree_name** (_str_) : tree name
- **tree_type** (_str_ = GeometryNodeTree) : tree type
- **fake_user** (_bool_ = False) : fake user flag
- **is_group** (_bool_ = False) : Group or not
- **prefix** (_str_ = ) : prefix to add at the begining of the tree name
- **replace_material** (_bool_ = False) : replace the existing matertial if True

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
### pop()

> method

``` python
pop(error=False)
```

> Remove this tree from the stack

!!! important
> This methods shouldn't be called directly, better use a **with** context block.


``` python
with Tree("My Name"):
    pass
```

#### Raises:
- **NodeError** : if this tree is not the current one



#### Arguments:
- **error** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### push()

> method

``` python
push()
```

> Make this tree zone the current one

!!! important
> This methods shouldn't be called directly, better use a **with** context block.

``` python
with Tree("My Name"):
    pass
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### register_node()

> method

``` python
register_node(node)
```

Register a new Node.

This method is called by the Node class constructor. Never call directly.

Registered Nodes are stored in the dictionary : _nodes = bpy.types.Node.name -> Node

#### Arguments:
- **node** (_Node_) : the newly created Node to register



#### Returns:
- **Node** : the passed argument

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>

----------
### remove_groups()

> staticmethod

``` python
remove_groups(names=None, prefix=None, geonodes=True, shadernodes=True)
```

> Remove Groups created by GeoNodes.

!!! important
> This method can only remove groups created by **GeoNodes**.

#### Arguments:
- **names** (_str or list of strs_ = None) : name of the node groups to remove (all if None)
- **prefix** (_str_ = None) : name prefix for the groups to delete
- **geonodes** (_bool_ = True) : remove geometry nodes groups
- **shadernodes** ( = True)



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Tree](tree.md#tree) :black_small_square: [Content](tree.md#content) :black_small_square: [Methods](tree.md#methods)</sub>