
# Class Geometry

> Inherits from: ***dsock.Geometry***

## Static methods



- [is_viewport](#is_viewport) : is_viewport (Boolean)



## Properties



- [bound_box](#bound_box) : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
- [components](#components) : Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]



## Attribute capture



- [capture_ID](#capture_id) : ID (Integer)
- [capture_index](#capture_index) : index (Integer)
- [capture_normal](#capture_normal) : normal (Vector)
- [capture_position](#capture_position) : position (Vector)
- [capture_radius](#capture_radius) : radius (Float)



## Attributes



- [ID](#id) : Integer = capture_ID(domain='POINT')
- [index](#index) : Integer = capture_index(domain='POINT')
- [normal](#normal) : Vector = capture_normal(domain='FACE')
- [position](#position) : Vector = capture_position(domain='POINT')
- [radius](#radius) : Float = capture_radius(domain='POINT')



## Methods



- [attribute_domain_size](#attribute_domain_size) : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
- [attribute_remove](#attribute_remove) : geometry (Geometry)
- [components](#components) : Sockets      [selection (Geometry), inverted (Geometry)]
- [convex_hull](#convex_hull) : convex_hull (Geometry)
- [join](#join) : geometry (Geometry)
- [proximity](#proximity) : Sockets      [position (Vector), distance (Float)]
- [switch](#switch) : output (Geometry)
- [to_instance](#to_instance) : instances (Instances)
- [transfer_boolean](#transfer_boolean) : attribute (Boolean)
- [transfer_color](#transfer_color) : attribute (Color)
- [transfer_float](#transfer_float) : attribute (Float)
- [transfer_integer](#transfer_integer) : attribute (Integer)
- [transfer_vector](#transfer_vector) : attribute (Vector)



## Stacked methods



- [delete_geometry](#delete_geometry) : Geometry
- [merge_by_distance](#merge_by_distance) : Geometry
- [realize_instances](#realize_instances) : Geometry
- [replace_material](#replace_material) : Geometry
- [scale_elements](#scale_elements) : Geometry
- [set_ID](#set_id) : Geometry
- [set_material](#set_material) : Geometry
- [set_material_index](#set_material_index) : Geometry
- [set_position](#set_position) : Geometry
- [set_shade_smooth](#set_shade_smooth) : Geometry
- [transform](#transform) : Geometry



## Methods


### ID

> Node: [ID](../nodes/{self.node_name}.md)

```python
v = geometry.ID(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### attribute_domain_size

> Node: [DomainSize](../nodes/{self.node_name}.md)

```python
v = geometry.attribute_domain_size(component)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Parameters arguments



- component : 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]



#### Returns

    Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]

### attribute_remove

> Node: [AttributeRemove](../nodes/{self.node_name}.md)

```python
v = geometry.attribute_remove(attribute_1, attribute_2, attribute_3)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- attribute : *String



#### Returns

    Geometry

### bound_box

> Node: [BoundingBox](../nodes/{self.node_name}.md)

```python
v = geometry.bound_box
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.bound_box"



#### Returns

    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]

### capture_ID

> Node: [ID](../nodes/{self.node_name}.md)

```python
v = geometry.capture_ID(self, domain='POINT')
```


#### Arguments


##### Parameters arguments



- self
- domain:'POINT'



#### Returns

    Integer

### capture_index

> Node: [Index](../nodes/{self.node_name}.md)

```python
v = geometry.capture_index(self, domain='POINT')
```


#### Arguments


##### Parameters arguments



- self
- domain:'POINT'



#### Returns

    Integer

### capture_normal

> Node: [Normal](../nodes/{self.node_name}.md)

```python
v = geometry.capture_normal(self, domain='FACE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'FACE'



#### Returns

    Vector

### capture_position

> Node: [Position](../nodes/{self.node_name}.md)

```python
v = geometry.capture_position(self, domain='POINT')
```


#### Arguments


##### Parameters arguments



- self
- domain:'POINT'



#### Returns

    Vector

### capture_radius

> Node: [Radius](../nodes/{self.node_name}.md)

```python
v = geometry.capture_radius(self, domain='POINT')
```


#### Arguments


##### Parameters arguments



- self
- domain:'POINT'



#### Returns

    Float

### components

> Node: [SeparateGeometry](../nodes/{self.node_name}.md)

```python
v = geometry.components(selection, domain)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]



#### Returns

    Sockets [selection (Geometry), inverted (Geometry)]

### convex_hull

> Node: [ConvexHull](../nodes/{self.node_name}.md)

```python
v = geometry.convex_hull()
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



#### Returns

    Geometry

### delete_geometry

> Node: [DeleteGeometry](../nodes/{self.node_name}.md)

```python
geometry.delete_geometry(selection, domain, mode)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode : 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]



#### Returns

    self

### index

> Node: [Index](../nodes/{self.node_name}.md)

```python
v = geometry.index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### is_viewport

> Node: [IsViewport](../nodes/{self.node_name}.md)

```python
v = Geometry.is_viewport()
```


#### Arguments


#### Returns

    Boolean

### join

> Node: [JoinGeometry](../nodes/{self.node_name}.md)

```python
v = geometry.join(geometry_1, geometry_2, geometry_3)
```


#### Arguments


##### Sockets arguments



- geometry : *Geometry (self)



#### Returns

    Geometry

### merge_by_distance

> Node: [MergeByDistance](../nodes/{self.node_name}.md)

```python
geometry.merge_by_distance(selection, distance)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- distance : Float



#### Returns

    self

### normal

> Node: [Normal](../nodes/{self.node_name}.md)

```python
v = geometry.normal(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Vector

### position

> Node: [Position](../nodes/{self.node_name}.md)

```python
v = geometry.position(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Vector

### proximity

> Node: [GeometryProximity](../nodes/{self.node_name}.md)

```python
v = geometry.proximity(source_position, target_element)
```


#### Arguments


##### Sockets arguments



- target : Geometry (self)
- source_position : Vector



##### Parameters arguments



- target_element : 'FACES' in [POINTS, EDGES, FACES]



#### Returns

    Sockets [position (Vector), distance (Float)]

### radius

> Node: [Radius](../nodes/{self.node_name}.md)

```python
v = geometry.radius(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Float

### realize_instances

> Node: [RealizeInstances](../nodes/{self.node_name}.md)

```python
geometry.realize_instances(legacy_behavior)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Parameters arguments



- legacy_behavior : False



#### Returns

    self

### replace_material

> Node: [ReplaceMaterial](../nodes/{self.node_name}.md)

```python
geometry.replace_material(old, new)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- old : Material
- new : Material



#### Returns

    self

### scale_elements

> Node: [ScaleElements](../nodes/{self.node_name}.md)

```python
geometry.scale_elements(selection, scale, center, axis, domain, scale_mode)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- scale : Float
- center : Vector
- axis : Vector



##### Parameters arguments



- domain : 'FACE' in [FACE, EDGE]
- scale_mode : 'UNIFORM' in [UNIFORM, SINGLE_AXIS]



#### Returns

    self

### set_ID

> Node: [SetID](../nodes/{self.node_name}.md)

```python
geometry.set_ID(selection, ID)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- ID : Integer



#### Returns

    self

### set_material

> Node: [SetMaterial](../nodes/{self.node_name}.md)

```python
geometry.set_material(selection, material)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- material : Material



#### Returns

    self

### set_material_index

> Node: [SetMaterialIndex](../nodes/{self.node_name}.md)

```python
geometry.set_material_index(selection, material_index)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- material_index : Integer



#### Returns

    self

### set_position

> Node: [SetPosition](../nodes/{self.node_name}.md)

```python
geometry.set_position(selection, position, offset)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- position : Vector
- offset : Vector



#### Returns

    self

### set_shade_smooth

> Node: [SetShadeSmooth](../nodes/{self.node_name}.md)

```python
geometry.set_shade_smooth(selection, shade_smooth)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- selection : Boolean
- shade_smooth : Boolean



#### Returns

    self

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = geometry.switch(switch1, true)
```


#### Arguments


##### Sockets arguments



- false : Geometry (self)
- switch1 : Boolean
- true : Geometry



##### Fixed parameters



- input_type : 'GEOMETRY'



#### Returns

    Geometry

### to_instance

> Node: [GeometryToInstance](../nodes/{self.node_name}.md)

```python
v = geometry.to_instance(geometry_1, geometry_2, geometry_3)
```


#### Arguments


##### Sockets arguments



- geometry : *Geometry (self)



#### Returns

    Instances

### transfer_boolean

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = geometry.transfer_boolean(attribute, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- source : Geometry (self)
- attribute : Boolean
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'BOOLEAN'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Boolean

### transfer_color

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = geometry.transfer_color(attribute, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- source : Geometry (self)
- attribute : Color
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT_COLOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Color

### transfer_float

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = geometry.transfer_float(attribute, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- source : Geometry (self)
- attribute : Float
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Float

### transfer_integer

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = geometry.transfer_integer(attribute, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- source : Geometry (self)
- attribute : Integer
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'INT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Integer

### transfer_vector

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = geometry.transfer_vector(attribute, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- source : Geometry (self)
- attribute : Vector
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Vector

### transform

> Node: [Transform](../nodes/{self.node_name}.md)

```python
geometry.transform(translation, rotation, scale)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)
- translation : Vector
- rotation : Vector
- scale : Vector



#### Returns

    self
