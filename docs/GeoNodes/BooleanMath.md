# Node BooleanMath

- Node name : 'Boolean Math'
- bl_idname : [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)


``` python
BooleanMath(boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- boolean : None
- boolean_1 : None
- operation : 'AND'

## Implementation

- [BOOLEAN](/docs/GeoNodes/socket_BOOLEAN.md) : [band](/docs/GeoNodes/socket_BOOLEAN.md#band) [bnot](/docs/GeoNodes/socket_BOOLEAN.md#bnot) [bor](/docs/GeoNodes/socket_BOOLEAN.md#bor) [imply](/docs/GeoNodes/socket_BOOLEAN.md#imply) [nand](/docs/GeoNodes/socket_BOOLEAN.md#nand) [nimply](/docs/GeoNodes/socket_BOOLEAN.md#nimply) [nor](/docs/GeoNodes/socket_BOOLEAN.md#nor) [xnor](/docs/GeoNodes/socket_BOOLEAN.md#xnor) [xor](/docs/GeoNodes/socket_BOOLEAN.md#xor)
- Functions : [band](/docs/GeoNodes/GeoNodesTree.md#band) [bnot](/docs/GeoNodes/GeoNodesTree.md#bnot) [bor](/docs/GeoNodes/GeoNodesTree.md#bor) [imply](/docs/GeoNodes/GeoNodesTree.md#imply) [nand](/docs/GeoNodes/GeoNodesTree.md#nand) [nimply](/docs/GeoNodes/GeoNodesTree.md#nimply) [nor](/docs/GeoNodes/GeoNodesTree.md#nor) [xnor](/docs/GeoNodes/GeoNodesTree.md#xnor) [xor](/docs/GeoNodes/GeoNodesTree.md#xor)

## Init

``` python
def __init__(self, boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeBooleanMath', node_label=node_label, node_color=node_color, **kwargs)

    self.operation       = operation
    self.boolean         = boolean
    self.boolean_1       = boolean_1
```
