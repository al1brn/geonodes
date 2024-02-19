# class StoreNamedAttribute (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : StoreNamedAttribute
 - bl_idname : GeometryNodeStoreNamedAttribute

Node parameters
 - data_type : 'FLOAT'
 - domain : 'POINT'

Input sockets
 - geometry : Geometry
 - selection : Bool
 - name : Str
 - value : Vect
 - value_1 : Float
 - value_2 : Col
 - value_3 : Bool
 - value_4 : Int
 - value_5 : Rot

Output sockets
 - geometry : Geometry

### Header

``` python
def StoreNamedAttribute(self, geometry=None, name=None, value=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```

## Implementations

o functions : [store_named_attribute](#store_named_attribute)
o Geometry : [store_named_attribute](#store_named_attribute) [store_named_float](#store_named_float) [store_named_int](#store_named_int) [store_named_vector](#store_named_vector) [store_named_float_color](#store_named_float_color) [store_named_byte_color](#store_named_byte_color) [store_named_boolean](#store_named_boolean) [store_named_float2](#store_named_float2) [store_named_quaternion](#store_named_quaternion) 
o Domain : [store_named_attribute](#store_named_attribute) [store_named_float](#store_named_float) [store_named_int](#store_named_int) [store_named_vector](#store_named_vector) [store_named_float_color](#store_named_float_color) [store_named_byte_color](#store_named_byte_color) [store_named_boolean](#store_named_boolean) [store_named_float2](#store_named_float2) [store_named_quaternion](#store_named_quaternion) 
