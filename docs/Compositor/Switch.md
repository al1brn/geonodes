# Node Switch

- Node name : 'Switch'
- bl_idname : [CompositorNodeSwitch](https://docs.blender.org/api/current/bpy.types.CompositorNodeSwitch.html)


``` python
Switch(off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- off : None
- on : None
- check : False
- tag_need_exec : None

## Implementation

- [RGBA](/docs/Compositor/RGBA.md) : [switch](/docs/Compositor/RGBA.md#switch)
- [VALUE](/docs/Compositor/VALUE.md) : [switch](/docs/Compositor/VALUE.md#switch)
- [VECTOR](/docs/Compositor/VECTOR.md) : [switch](/docs/Compositor/VECTOR.md#switch)

## Init

``` python
def __init__(self, off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeSwitch', node_label=node_label, node_color=node_color)

    self.check           = check
    self.tag_need_exec   = tag_need_exec
    self.off             = off
    self.on              = on
```
