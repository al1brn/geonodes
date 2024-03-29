# Node Attribute

- Node name : 'Attribute'
- bl_idname : [ShaderNodeAttribute](https://docs.blender.org/api/current/bpy.types.ShaderNodeAttribute.html)


``` python
Attribute(attribute_name='', attribute_type='GEOMETRY', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- attribute_name : ''
- attribute_type : 'GEOMETRY'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, attribute_name='', attribute_type='GEOMETRY', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeAttribute', node_label=node_label, node_color=node_color, **kwargs)

    self.attribute_name  = attribute_name
    self.attribute_type  = attribute_type
```
