# Node InvertRotation

- Node name : 'Invert Rotation'
- bl_idname : FunctionNodeInvertRotation


``` python
InvertRotation(rotation=None, node_label=None, node_color=None)
```
##### Arguments

- rotation : None

## Implementation

- [Rot](/docs/GeoNodes/Rot.md) : [invert_rotation](/docs/GeoNodes/Rot.md#invert_rotation)
- [Vect](/docs/GeoNodes/Vect.md) : [invert_rotation](/docs/GeoNodes/Vect.md#invert_rotation)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeInvertRotation', node_label=node_label, node_color=node_color)

    self.rotation        = rotation
```
