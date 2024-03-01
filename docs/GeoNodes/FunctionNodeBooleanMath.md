# Node BooleanMath

- Node name : 'Boolean Math'
- bl_idname : FunctionNodeBooleanMath


``` python
BooleanMath(boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None)
```
##### Arguments

- boolean : None
- boolean_1 : None
- operation : AND

## Implementation

- [Bool](/docs/GeoNodes/Bool.md) : [band](/docs/GeoNodes/Bool.md#band) [bnot](/docs/GeoNodes/Bool.md#bnot) [bor](/docs/GeoNodes/Bool.md#bor) [imply](/docs/GeoNodes/Bool.md#imply) [nand](/docs/GeoNodes/Bool.md#nand) [nimply](/docs/GeoNodes/Bool.md#nimply) [nor](/docs/GeoNodes/Bool.md#nor) [xnor](/docs/GeoNodes/Bool.md#xnor) [xor](/docs/GeoNodes/Bool.md#xor)
- Functions : [band](/docs/GeoNodes/Bool.md#band) [bnot](/docs/GeoNodes/Bool.md#bnot) [bor](/docs/GeoNodes/Bool.md#bor) [imply](/docs/GeoNodes/Bool.md#imply) [nand](/docs/GeoNodes/Bool.md#nand) [nimply](/docs/GeoNodes/Bool.md#nimply) [nor](/docs/GeoNodes/Bool.md#nor) [xnor](/docs/GeoNodes/Bool.md#xnor) [xor](/docs/GeoNodes/Bool.md#xor)

## Init

``` python
def __init__(self, boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeBooleanMath', node_label=node_label, node_color=node_color)

    self.operation       = operation
    self.boolean         = boolean
    self.boolean_1       = boolean_1
```
