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

- **C** : [Collection](geono-socke-collection.md#collection) :black_small_square: [constants](geono-socke-const---constants.md#constants)
- **I** : [Image](geono-socke-image.md#image)
- **M** : [Material](geono-socke-material.md#material)
- **N** : [NodeCache](geono-socke-nodecache.md#nodecache)
- **O** : [Object](geono-socke-object.md#object)
- **S** : [Socket](geono-socke-socket.md#socket) :black_small_square: [String](geono-socke-string.md#string)
- **T** : [TextureRoot](geono-socke-textureroot.md#textureroot)
- **U** : [utils](geono-socke-utils---utils.md#utils)
- **V** : [ValueSocket](geono-socke-valuesocket.md#valuesocket)

## Modules



- [constants](geono-socke-const---constants.md#constants)
- [utils](geono-socke-utils---utils.md#utils)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass) :black_small_square: [Content](geono-socke---socketclass.md#content) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass)</sub>

## Classes



- [Collection](geono-socke-collection.md#collection)
- [Image](geono-socke-image.md#image)
- [Material](geono-socke-material.md#material)
- [Menu](geono-socke-menu.md#menu)
- [NodeCache](geono-socke-nodecache.md#nodecache)
- [Object](geono-socke-object.md#object)
- [Socket](geono-socke-socket.md#socket)
- [String](geono-socke-string.md#string)
- [TextureRoot](geono-socke-textureroot.md#textureroot)
- [ValueSocket](geono-socke-valuesocket.md#valuesocket)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass) :black_small_square: [Content](geono-socke---socketclass.md#content) :black_small_square: [socketclass](geono-socke---socketclass.md#socketclass)</sub>