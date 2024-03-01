# Node Script

- Node name : 'Script'
- bl_idname : ShaderNodeScript


``` python
Script(bytecode='', bytecode_hash='', filepath='', mode='INTERNAL', script=None, use_auto_update=False, node_label=None, node_color=None)
```
##### Arguments

- bytecode : ''
- bytecode_hash : ''
- filepath : ''
- mode : 'INTERNAL'
- script : None
- use_auto_update : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, bytecode='', bytecode_hash='', filepath='', mode='INTERNAL', script=None, use_auto_update=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeScript', node_label=node_label, node_color=node_color)

    self.bytecode        = bytecode
    self.bytecode_hash   = bytecode_hash
    self.filepath        = filepath
    self.mode            = mode
    self.script          = script
    self.use_auto_update = use_auto_update
```
