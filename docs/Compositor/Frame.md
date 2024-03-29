# Node Frame

- Node name : 'Frame'
- bl_idname : [NodeFrame](https://docs.blender.org/api/current/bpy.types.NodeFrame.html)


``` python
Frame(label_size=20, shrink=True, text=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- label_size : 20
- shrink : True
- text : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, label_size=20, shrink=True, text=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'NodeFrame', node_label=node_label, node_color=node_color, **kwargs)

    self.label_size      = label_size
    self.shrink          = shrink
    self.text            = text
```
