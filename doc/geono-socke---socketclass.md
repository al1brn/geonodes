# socketclass

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : socketclass
--------------------
- Provides the base class for data socket Socket which wraps an output socket of a Node
- Implement simple Data Sockets:

classes
-------
- NodeCache     : Interface for Socket and Domain which can cache created nodes
- Socket    : Wraps the output socket of node and exposes nodes creation as methods or properties
- ValueSocket   : Socket subtype for sockets representing a value (i.e. attributes)
- String        : Socket of type 'STRING'
- Material      : Socket of type 'MATERIAL'
- Image         : Socket of type 'IMAGE'
- Object        : Socket of type 'OBJECT'
- Collection    : Socket of type 'COLLECTION'
- Menu          : Socket of type 'MENU'
- TextureRoot   : Socket of type 'TEXTURE'

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- [Collection](geono-socke-collection.md#collection)
  - [Info](geono-socke-collection.md#info)
  - [info](geono-socke-collection.md#info)
- [constants](geono-socke-const---constants.md#constants)
- [Image](geono-socke-image.md#image)
  - [Info](geono-socke-image.md#info)
  - [info](geono-socke-image.md#info)
- [Material](geono-socke-material.md#material)
- [Object](geono-socke-object.md#object)
  - [Info](geono-socke-object.md#info)
  - [info](geono-socke-object.md#info)
- [Socket](geono-socke-socket.md#socket)
  - [node](geono-socke-socket.md#node)
  - [blur](geono-socke-socket.md#blur)
  - [IndexSwitch](geono-socke-socket.md#indexswitch)
  - [index_switch](geono-socke-socket.md#index_switch)
  - [\_lc](geono-socke-socket.md#_lc)
  - [MenuSwitch](geono-socke-socket.md#menuswitch)
  - [menu_switch](geono-socke-socket.md#menu_switch)
  - [out](geono-socke-socket.md#out)
  - [Switch](geono-socke-socket.md#switch)
  - [switch](geono-socke-socket.md#switch)
  - [to_output](geono-socke-socket.md#to_output)
- [String](geono-socke-string.md#string)
  - [length](geono-socke-string.md#length)
  - [equal](geono-socke-string.md#equal)
  - [FromValue](geono-socke-string.md#fromvalue)
  - [Join](geono-socke-string.md#join)
  - [join](geono-socke-string.md#join)
  - [not_equal](geono-socke-string.md#not_equal)
  - [replace](geono-socke-string.md#replace)
  - [slice](geono-socke-string.md#slice)
  - [to_curves](geono-socke-string.md#to_curves)
- [utils](geono-socke-utils---utils.md#utils)
  - [constants](geono-socke-utils-const---constants.md#constants)
  - [del_tree](geono-socke-utils---utils.md#del_tree)
  - [get_tree](geono-socke-utils---utils.md#get_tree)

## Modules



- [constants](geono-socke-const---constants.md#constants)
- [utils](geono-socke-utils---utils.md#utils)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass) :black_small_square: [Content](geono-socke---socketclass.md#content) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass)</sub>

## Classes



- [Collection](geono-socke-collection.md#collection)
- [Image](geono-socke-image.md#image)
- [Material](geono-socke-material.md#material)
- [Menu](geono-socke-menu.md#menu)
- [Object](geono-socke-object.md#object)
- [Socket](geono-socke-socket.md#socket)
- [String](geono-socke-string.md#string)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass) :black_small_square: [Content](geono-socke---socketclass.md#content) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass)</sub>