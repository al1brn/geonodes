# blendertree

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : blendertree
--------------------
- Create and delete trees
- Loops on nodes

classes
-------


functions
---------
- get_tree          : get or create a tree of the given type
- del_tree          : delete the tree
- loop_on_nodes     : loop on all the possible nodes and run a function for each
- gen_SOCKET_TYPES  : create the dict SOCKET_TYPES
- gen_NODE_NAMES    : create the dict NODE_NAMES
- gen_maths         : legacy - used once
- gen_boolean_math  : legacy - used once
- gen_vector_math   : legacy - used once
- gen_int_compare   : legacy - used once

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- [del_tree](blendertree.md#del_tree)
- [get_tree](blendertree.md#get_tree)

## Functions



----------
### del_tree()

> function

``` python
del_tree(btree)
```

Delete a tree

#### Arguments:
- **btree** : (blender Tree or str : Tree or tree name

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [blendertree](blendertree.md#blendertree) :black_small_square: [Content](blendertree.md#content) :black_small_square: [Functions](blendertree.md#functions)</sub>

----------
### get_tree()

> function

``` python
get_tree(name, tree_type='GeometryNodeTree', create=True)
```

Get or create a new nodes tree

#### Arguments:
- **name** (_str_) : Tree name - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree') - create (bool = False) : Create the tree if it doesn't exist
- **tree_type** ( = GeometryNodeTree)
- **create** ( = True)



#### Returns:
- **Tree** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [blendertree](blendertree.md#blendertree) :black_small_square: [Content](blendertree.md#content) :black_small_square: [Functions](blendertree.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [blendertree](blendertree.md#blendertree) :black_small_square: [Content](blendertree.md#content) :black_small_square: [blendertree](blendertree.md#blendertree)</sub>