# Node BooleanMath

- Node name : 'Boolean Math'
- bl_idname : [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)


``` python
BooleanMath(boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None)
```
##### Arguments

- boolean : None
- boolean_1 : None
- operation : 'AND'

## Implementation

- [Bool](/docs/GeoNodes/Bool.md) : [band](/docs/GeoNodes/Bool.md#band) [bnot](/docs/GeoNodes/Bool.md#bnot) [bor](/docs/GeoNodes/Bool.md#bor) [imply](/docs/GeoNodes/Bool.md#imply) [nand](/docs/GeoNodes/Bool.md#nand) [nimply](/docs/GeoNodes/Bool.md#nimply) [nor](/docs/GeoNodes/Bool.md#nor) [xnor](/docs/GeoNodes/Bool.md#xnor) [xor](/docs/GeoNodes/Bool.md#xor)
- Functions : [band](/docs/GeoNodes/GeoNodesTree.md#band) [bnot](/docs/GeoNodes/GeoNodesTree.md#bnot) [bor](/docs/GeoNodes/GeoNodesTree.md#bor) [imply](/docs/GeoNodes/GeoNodesTree.md#imply) [nand](/docs/GeoNodes/GeoNodesTree.md#nand) [nimply](/docs/GeoNodes/GeoNodesTree.md#nimply) [nor](/docs/GeoNodes/GeoNodesTree.md#nor) [xnor](/docs/GeoNodes/GeoNodesTree.md#xnor) [xor](/docs/GeoNodes/GeoNodesTree.md#xor)

## Init

``` python
def __init__(self, boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeBooleanMath', node_label=node_label, node_color=node_color)

    self.operation       = operation
    self.boolean         = boolean
    self.boolean_1       = boolean_1
```
