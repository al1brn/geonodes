# treeclass

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : treeclass
------------------
Provides the two major classes:
- Tree: the tree currently edited
- Node: base class to create a node

Note that to ease the scripting, nodes are created without refering explicity to a tree,
but get the tree in a stack of trees as the 'current tree'.

This allows the syntax:

```python
my_node = Node(...)
````

rather than:
``` python
my_node = tree.Node(...)
```

Pushing and poping the stack of tree is made with context management:

``` python
with Tree("Geometry Nodes"):
    my_node = Node(...)

# The following line raises an error:
node_error = Node(...)
```

classes
-------
- Break         : Exit from with block
- Layout        : Creates a Frame where the new nodes are placed into
- Tree          : The tree to build
- Node          : Node creation in the current Tree and Layout
- Group         : Node Group creation
- GroupF        : Utility class to call a group with python syntax

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- [Break](geono-treec-break.md)
- [constants](geono-treec-const---constants.md)
- [Group](geono-treec-group.md)
  - [Prefix](geono-treec-group.md#prefix)
- [GroupF](geono-treec-groupf.md)
- [Layout](geono-treec-layout.md)
- [Node](geono-treec-node.md)
  - [\_out](geono-treec-node.md#_out)
  - [plug_node_into](geono-treec-node.md#plug_node_into)
- [Tree](geono-treec-tree.md)
  - [input_node](geono-treec-tree.md#input_node)
  - [output_node](geono-treec-tree.md#output_node)
  - [arrange](geono-treec-tree.md#arrange)
  - [clear](geono-treec-tree.md#clear)
  - [link](geono-treec-tree.md#link)
  - [new_input](geono-treec-tree.md#new_input)
  - [new_input_from_input_socket](geono-treec-tree.md#new_input_from_input_socket)
  - [new_output](geono-treec-tree.md#new_output)
  - [remove_groups](geono-treec-tree.md#remove_groups)
- [treearrange](geono-treec-treea---treearrange.md)
- [utils](geono-treec-utils---utils.md)
  - [constants](geono-treec-utils-const---constants.md)
  - [del_tree](geono-treec-utils---utils.md#del_tree)
  - [get_tree](geono-treec-utils---utils.md#get_tree)

## Modules



- [constants](geono-treec-const---constants.md)
- [treearrange](geono-treec-treea---treearrange.md)
- [utils](geono-treec-utils---utils.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treeclass) :black_small_square: [Content](#content) :black_small_square: [treeclass](geono-treec---treeclass.md)</sub>

## Classes



- [Break](geono-treec-break.md)
- [Group](geono-treec-group.md)
- [GroupF](geono-treec-groupf.md)
- [Layout](geono-treec-layout.md)
- [Node](geono-treec-node.md)
- [Tree](geono-treec-tree.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treeclass) :black_small_square: [Content](#content) :black_small_square: [treeclass](geono-treec---treeclass.md)</sub>