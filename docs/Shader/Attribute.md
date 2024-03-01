# Node Attribute

- Node name : 'Attribute'
- bl_idname : [Attribute](https://docs.blender.org/api/current/bpy.types.Attribute.html)


``` python
Attribute(attribute_name='', attribute_type='GEOMETRY', node_label=None, node_color=None)
```
##### Arguments

- attribute_name : ''
- attribute_type : 'GEOMETRY'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, attribute_name='', attribute_type='GEOMETRY', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeAttribute', node_label=node_label, node_color=node_color)

    self.attribute_name  = attribute_name
    self.attribute_type  = attribute_type
```
