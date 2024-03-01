# Node BlurAttribute

- Node name : 'Blur Attribute'
- bl_idname : GeometryNodeBlurAttribute


``` python
BlurAttribute(value=None, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None)
```
##### Arguments

- value : None
- iterations : None
- weight : None
- data_type : 'FLOAT'

## Implementation

- [Col](/docs/GeoNodes/Col.md) : [blur_attribute](/docs/GeoNodes/Col.md#blur_attribute)
- [Float](/docs/GeoNodes/Float.md) : [blur_attribute](/docs/GeoNodes/Float.md#blur_attribute)
- [Geometry](/docs/GeoNodes/Geometry.md) : [blur_attribute](/docs/GeoNodes/Geometry.md#blur_attribute)
- [Int](/docs/GeoNodes/Int.md) : [blur_attribute](/docs/GeoNodes/Int.md#blur_attribute)
- [Vect](/docs/GeoNodes/Vect.md) : [blur_attribute](/docs/GeoNodes/Vect.md#blur_attribute)

## Init

``` python
def __init__(self, value=None, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeBlurAttribute', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.value           = value
    self.iterations      = iterations
    self.weight          = weight
```
