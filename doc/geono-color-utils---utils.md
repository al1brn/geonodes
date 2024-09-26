# utils

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : utils
--------------
- utilities

classes
-------


functions
---------
- remove_accents    : remove accents from a string
- clean             : clean a string
- prefix_figure     : prefix a string by '_' if it is a number, e.g. : '3D Cursor' -> _3d_cursor
- socket_name       : transform a user name in snake case python name, e.g. : "Color Ramp" -> 'color_ramp'
- get_bsocket       : get a blender socket from a value which can be a Socket or a blender.types.NodeSocket
- get_socket_type   : get a socket type in SOCKET_TYPES.keys() from either a socket or a value
- get_data_type     : get a data type in DATA_TYPES from either a socket or a value
- get_input_type    : get an input type in INPUT_TYPES from either a socket or a value
- value_to_array    : convert a value into an array of the given shape. Raises an error if not possible
- is_vector_like    : socket type is a vector
- is_color_like     : socket type is a color
- is_matrix_like    : socket type is a matrix
- is_value_like     : socket type is a value
- has_bsocket       : value is a socket or a tuple with sockets
- get_blender_resource : get a Blender ressource its name, e.g. = get_blender_resource('MATERIAL', "Material") -> bpy.materials.get("Material")
- python_value_for_socket : build a python value acceptable as socket default value

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- [constants](geono-color-utils-const---constants.md#constants)
- [del_tree](geono-color-utils---utils.md#del_tree)
- [get_tree](geono-color-utils---utils.md#get_tree)

## Modules



- [constants](geono-color-utils-const---constants.md#constants)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [utils](geono-color-utils---utils.md#utils) :black_small_square: [Content](geono-color-utils---utils.md#content) :black_small_square: [utils](geono-color-utils---utils.md#utils)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [utils](geono-color-utils---utils.md#utils) :black_small_square: [Content](geono-color-utils---utils.md#content) :black_small_square: [Functions](geono-color-utils---utils.md#functions)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [utils](geono-color-utils---utils.md#utils) :black_small_square: [Content](geono-color-utils---utils.md#content) :black_small_square: [Functions](geono-color-utils---utils.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [utils](geono-color-utils---utils.md#utils) :black_small_square: [Content](geono-color-utils---utils.md#content) :black_small_square: [utils](geono-color-utils---utils.md#utils)</sub>