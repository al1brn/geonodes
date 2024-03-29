# Node Switch

- Node name : 'Switch'
- bl_idname : [CompositorNodeSwitch](https://docs.blender.org/api/current/bpy.types.CompositorNodeSwitch.html)


``` python
Switch(off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- off : None
- on : None
- check : False
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, off=None, on=None, check=False, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeSwitch', node_label=node_label, node_color=node_color, **kwargs)

    self.check           = check
    self.tag_need_exec   = tag_need_exec
    self.off             = off
    self.on              = on
```
