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

- **C** : [Collection](geono-socke-collection.md) :black_small_square: [constants](geono-socke-const---constants.md)
- **I** : [Image](geono-socke-image.md)
- **M** : [Material](geono-socke-material.md)
- **N** : [NodeCache](geono-socke-nodecache.md)
- **O** : [Object](geono-socke-object.md)
- **S** : [Socket](geono-socke-socket.md) :black_small_square: [String](geono-socke-string.md)
- **T** : [TextureRoot](geono-socke-textureroot.md)
- **U** : [utils](geono-socke-utils---utils.md)
- **V** : [ValueSocket](geono-socke-valuesocket.md)

## Modules



- [constants](geono-socke-const---constants.md)
- [utils](geono-socke-utils---utils.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#socketclass) :black_small_square: [Content](#content) :black_small_square: [socketclass](geono-socke---socketclass.md)</sub>

## Classes



- [Collection](geono-socke-collection.md)
- [Image](geono-socke-image.md)
- [Material](geono-socke-material.md)
- [Menu](geono-socke-menu.md)
- [NodeCache](geono-socke-nodecache.md)
- [Object](geono-socke-object.md)
- [Socket](geono-socke-socket.md)
- [String](geono-socke-string.md)
- [TextureRoot](geono-socke-textureroot.md)
- [ValueSocket](geono-socke-valuesocket.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#socketclass) :black_small_square: [Content](#content) :black_small_square: [socketclass](geono-socke---socketclass.md)</sub>