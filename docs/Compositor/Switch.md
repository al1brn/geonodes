# Node Switch

- Node name : 'Switch'
- bl_idname : CompositorNodeSwitch


``` python
Switch(off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- off : None
- on : None
- check : False
- tag_need_exec : None

## Implementation

- [Col](/docs/Compositor/Col.md) : [switch](/docs/Compositor/Col.md#switch)
- [Float](/docs/Compositor/Float.md) : [switch](/docs/Compositor/Float.md#switch)
- [Vect](/docs/Compositor/Vect.md) : [switch](/docs/Compositor/Vect.md#switch)

## Init

``` python
def __init__(self, off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeSwitch', node_label=node_label, node_color=node_color)

    self.check           = check
    self.tag_need_exec   = tag_need_exec
    self.off             = off
    self.on              = on
```
