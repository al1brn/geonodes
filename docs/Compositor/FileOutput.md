# Node FileOutput

- Node name : 'File Output'
- bl_idname : [CompositorNodeOutputFile](https://docs.blender.org/api/current/bpy.types.CompositorNodeOutputFile.html)


``` python
FileOutput(image=None, active_input_index=0, base_path='/tmp/', file_slots=None, format=None, layer_slots=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- active_input_index : 0
- base_path : /tmp/
- file_slots : None
- format : None
- layer_slots : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, active_input_index=0, base_path='/tmp/', file_slots=None, format=None, layer_slots=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeOutputFile', node_label=node_label, node_color=node_color, **kwargs)

    self.active_input_index = active_input_index
    self.base_path       = base_path
    self.file_slots      = file_slots
    self.format          = format
    self.layer_slots     = layer_slots
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
