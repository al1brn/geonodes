# Node Clamp

- Node name : 'Clamp'
- bl_idname : [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)


``` python
Clamp(value=None, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None)
```
##### Arguments

- value : None
- min : None
- max : None
- clamp_type : 'MINMAX'

## Implementation

- [INT](/docs/GeoNodes/INT.md) : [clamp](/docs/GeoNodes/INT.md#clamp) [clamp](/docs/GeoNodes/INT.md#clamp)
- [VALUE](/docs/GeoNodes/VALUE.md) : [clamp](/docs/GeoNodes/VALUE.md#clamp) [clamp](/docs/GeoNodes/VALUE.md#clamp)

## Init

``` python
def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeClamp', node_label=node_label, node_color=node_color)

    self.clamp_type      = clamp_type
    self.value           = value
    self.min             = min
    self.max             = max
```
