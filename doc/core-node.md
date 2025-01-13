# Node

``` python
Node(tree, bnode)
```

> Node wrapper

#### Arguments:
- **tree** (_Tree_) : the tree to arrange
- **bnode** (_bpy.types.Node_) : the wrapped node

## Content

- **B** : [backwards](core-node.md#backwards) :black_small_square: [bnode](core-node.md#bnode)
- **D** : [dimensions](core-node.md#dimensions)
- **F** : [forwards](core-node.md#forwards)
- **H** : [height](core-node.md#height)
- **I** : [\_\_init__](core-node.md#__init__) :black_small_square: [in_nodes](core-node.md#in_nodes) :black_small_square: [in_zone](core-node.md#in_zone) :black_small_square: [is_child_of](core-node.md#is_child_of)
- **O** : [out_nodes](core-node.md#out_nodes)
- **P** : [parent](core-node.md#parent)
- **S** : [split_peers](core-node.md#split_peers)
- **T** : [tree](core-node.md#tree)
- **W** : [width](core-node.md#width)

## Properties



### bnode

> _type_: **bpy.types.Node**
>

wrapped node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### dimensions

> _type_: **couple**
>

Node dimensions

Node dimensions are read from bnode if it is available in 'NODE_EDITOR' area.
Otherwise, dimensions are approximated

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### height

> _type_: **float**
>

Node height

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### in_nodes

> _type_: **list**
>

List of input nodes

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### out_nodes

> _type_: **list**
>

List of output nodes

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### parent

> _type_: **Node**
>

parent node if any

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### tree

> _type_: **Tree**
>

tree wrapper

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

### width

> _type_: **float**
>

Node width

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Properties](core-node.md#properties)</sub>

## Methods



----------
### backwards()

> method

``` python
backwards()
```

Iterate backwards

Iterates on the left nodes

#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Methods](core-node.md#methods)</sub>

----------
### forwards()

> method

``` python
forwards()
```

Iterate forwards

Iterates on the right nodes

#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Methods](core-node.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(tree, bnode)
```

> Node wrapper

#### Arguments:
- **tree** (_Tree_) : the tree to arrange
- **bnode** (_bpy.types.Node_) : the wrapped node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Methods](core-node.md#methods)</sub>

----------
### in_zone()

> method

``` python
in_zone(input_node, output_node)
```

The node belongs to a zone

A node belongs to the zone if the zone input is linked to the node inputs
and if the zone output is linked to the node outputs.

#### Arguments:
- **input_node**
- **output_node**



#### Returns:
- **bool** : True if the node is in the zone

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Methods](core-node.md#methods)</sub>

----------
### is_child_of()

> method

``` python
is_child_of(frame)
```

Belongs to the frame

#### Arguments:
- **frame**



#### Returns:
- **bool** : True if the frame belongs to the parents hierarchy

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Methods](core-node.md#methods)</sub>

----------
### split_peers()

> method

``` python
split_peers(nodes)
```

Separate peer nodes from the other

Nodes are peer when they share the same parent.

This method splits the list of nodes in two list:
- nodes inside the parent of self
- nodes outside the parent of self

The first list returns the ancestor of the node sharing the parent of self, not
the node passed in the list.

#### Arguments:
- **nodes** (_list of Nodes_) : the list to split



#### Returns:
- **tuple** : peer nodes and not peer nodes

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](core-node.md#node) :black_small_square: [Content](core-node.md#content) :black_small_square: [Methods](core-node.md#methods)</sub>