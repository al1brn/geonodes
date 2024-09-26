# staticclass

Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : staticclass
--------------------
- Functional nodes

Functional nodes are nodes which can't be considered as methods or properties of a data class.
Functional nodes also include input nodes such as 'Position' or 'Index'. Theses nodes should be considered
as properties of geometry but to ease the scripting, there are also implemented as functions.

Functional nodes are implemented as static functions and properties or a class named nd which is short.

```  python
# Some functional nodes
pos = nd.position
i = nd.index
attr = named_attribute(name, 'FLOAT')
```

classes
-------
- Texture       : Implements the texture nodes creation
    - Brick
    - Checker
    - Gradient
    - Image
    - Magic
    - Noise
    - Voronoi
    - Wave
    - WhiteNoise


functions
---------

updates
-------
- creation : 2024/07/23