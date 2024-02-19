# class CaptureAttribute (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : CaptureAttribute
 - bl_idname : GeometryNodeCaptureAttribute

Node parameters
 - data_type : 'FLOAT'
 - domain : 'POINT'

Input sockets
 - geometry : Geometry
 - value : Vect
 - value_1 : Float
 - value_2 : Col
 - value_3 : Bool
 - value_4 : Int
 - value_5 : Rot

Output sockets
 - geometry : Geometry
 - attribute : Vect
 - attribute_1 : Float
 - attribute_2 : Col
 - attribute_3 : Bool
 - attribute_4 : Int
 - attribute_5 : Rot

### Header

``` python
def CaptureAttribute(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```

## Implementations

o Geometry : [capture_attribute](/docs/GeoNodes_classes/Geometry.md#capture_attribute) [capture_float](/docs/GeoNodes_classes/Geometry.md#capture_float) [capture_int](/docs/GeoNodes_classes/Geometry.md#capture_int) [capture_vector](/docs/GeoNodes_classes/Geometry.md#capture_vector) [capture_color](/docs/GeoNodes_classes/Geometry.md#capture_color) [capture_boolean](/docs/GeoNodes_classes/Geometry.md#capture_boolean) [capture_quaternion](/docs/GeoNodes_classes/Geometry.md#capture_quaternion)
o Domain : [capture_attribute](/docs/GeoNodes_classes/Domain.md#capture_attribute) [capture_float](/docs/GeoNodes_classes/Domain.md#capture_float) [capture_int](/docs/GeoNodes_classes/Domain.md#capture_int) [capture_vector](/docs/GeoNodes_classes/Domain.md#capture_vector) [capture_color](/docs/GeoNodes_classes/Domain.md#capture_color) [capture_boolean](/docs/GeoNodes_classes/Domain.md#capture_boolean) [capture_quaternion](/docs/GeoNodes_classes/Domain.md#capture_quaternion)

