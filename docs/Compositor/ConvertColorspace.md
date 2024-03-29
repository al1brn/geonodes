# Node ConvertColorspace

- Node name : 'Convert Colorspace'
- bl_idname : [CompositorNodeConvertColorSpace](https://docs.blender.org/api/current/bpy.types.CompositorNodeConvertColorSpace.html)


``` python
ConvertColorspace(image=None, from_color_space='Linear Rec.709', tag_need_exec=None, to_color_space='Linear Rec.709', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- from_color_space : Linear Rec.709
- tag_need_exec : None
- to_color_space : Linear Rec.709

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, from_color_space='Linear Rec.709', tag_need_exec=None, to_color_space='Linear Rec.709', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeConvertColorSpace', node_label=node_label, node_color=node_color, **kwargs)

    self.from_color_space = from_color_space
    self.tag_need_exec   = tag_need_exec
    self.to_color_space  = to_color_space
    self.image           = image
```
