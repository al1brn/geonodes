# zones

Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : zones
--------------
- Implements couples of nodes forming a zone : Simulation or Repeat

Zone arguments are set / get from one of the two nodes depending on the 'closed' status:
    - closed :
        - arguments are set to the input sockets of the INPUT node
        - arguments are get from the output sockets of the OUTPUT node
    - not closed
        - arguments are set to the input sockets of the OUTPUT node
        - arguments are get from the output sockets of the INPUT node

The closed parameter is managed through context management:

``` python
with Repeat(geometry=None, offset=(1, 2, 3), index=0, iteration=10) as repeat_block:

    repeat_block.geometry.offset = repeat_block.offset # Set Position Offset
    repeat_block.geometry = repeat_block.geometry.join(other_geometry)

    repeat_block.index += 1

repeat_block.geometry.to_output()
```

classes
-------
- IntFloat      : Base class for Integer and Float
- Integer       : Socket of type 'INT'
- Float         : Socket of type 'FLOAT'

functions
---------

updates
-------
- creation : 2024/07/23

## Content

- [Simulation](geono-zones-simulation.md#simulation)
- [utils](geono-zones-utils---utils.md#utils)
  - [constants](geono-zones-utils-const---constants.md#constants)
  - [del_tree](geono-zones-utils---utils.md#del_tree)
  - [get_tree](geono-zones-utils---utils.md#get_tree)

## Modules



- [utils](geono-zones-utils---utils.md#utils)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [zones](geono-zones---zones.md#zones) :black_small_square: [Content](geono-zones---zones.md#content) :black_small_square: [zones](geono-zones---zones.md#zones)</sub>

## Classes



- [Repeat](geono-zones-repeat.md#repeat)
- [Simulation](geono-zones-simulation.md#simulation)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [zones](geono-zones---zones.md#zones) :black_small_square: [Content](geono-zones---zones.md#content) :black_small_square: [zones](geono-zones---zones.md#zones)</sub>