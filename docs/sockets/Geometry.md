
# Class Geometry

> Inherits from: ***dsock.Geometry***

## Static methods



- [**self.meth_name**](#is_viewport) : [IsViewport](../nodes/IsViewport.md) is_viewport (Boolean)



## Properties



- [**self.meth_name**](#bound_box) : [BoundingBox](../nodes/BoundingBox.md) Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
- [**self.meth_name**](#box) : [BoundingBox](../nodes/BoundingBox.md) bounding_box (Geometry) = bound_box.bounding_box
- [**self.meth_name**](#box_max) : [BoundingBox](../nodes/BoundingBox.md) max (Vector) = bound_box.max
- [**self.meth_name**](#box_min) : [BoundingBox](../nodes/BoundingBox.md) min (Vector) = bound_box.min
- [**self.meth_name**](#components) : [SeparateComponents](../nodes/SeparateComponents.md) Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
- [**self.meth_name**](#curve_component) : [SeparateComponents](../nodes/SeparateComponents.md) curve (Curve) = components.curve
- [**self.meth_name**](#instances_component) : [SeparateComponents](../nodes/SeparateComponents.md) instances (Instances) = components.instances
- [**self.meth_name**](#mesh_component) : [SeparateComponents](../nodes/SeparateComponents.md) mesh (Mesh) = components.mesh
- [**self.meth_name**](#points_component) : [SeparateComponents](../nodes/SeparateComponents.md) point_cloud (Geometry) = components.point_cloud
- [**self.meth_name**](#volume_component) : [SeparateComponents](../nodes/SeparateComponents.md) volume (Volume) = components.volume



## Attribute capture



- [**self.meth_name**](#capture_id) : [ID](../nodes/ID.md) ID (Integer)
- [**self.meth_name**](#capture_index) : [Index](../nodes/Index.md) index (Integer)
- [**self.meth_name**](#capture_normal) : [Normal](../nodes/Normal.md) normal (Vector)
- [**self.meth_name**](#capture_position) : [Position](../nodes/Position.md) position (Vector)
- [**self.meth_name**](#capture_radius) : [Radius](../nodes/Radius.md) radius (Float)



## Attributes



- [**self.meth_name**](#id) : [ID](../nodes/ID.md) Integer = capture_ID(domain='POINT')
- [**self.meth_name**](#index) : [Index](../nodes/Index.md) Integer = capture_index(domain='POINT')
- [**self.meth_name**](#normal) : [Normal](../nodes/Normal.md) Vector = capture_normal(domain='FACE')
- [**self.meth_name**](#position) : [Position](../nodes/Position.md) Vector = capture_position(domain='POINT')
- [**self.meth_name**](#radius) : [Radius](../nodes/Radius.md) Float = capture_radius(domain='POINT')



## Methods



- [**self.meth_name**](#attribute_domain_size) : [DomainSize](../nodes/DomainSize.md) Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
- [**self.meth_name**](#attribute_remove) : [AttributeRemove](../nodes/AttributeRemove.md) geometry (Geometry)
- [**self.meth_name**](#components) : [SeparateGeometry](../nodes/SeparateGeometry.md) Sockets      [selection (Geometry), inverted (Geometry)]
- [**self.meth_name**](#convex_hull) : [ConvexHull](../nodes/ConvexHull.md) convex_hull (Geometry)
- [**self.meth_name**](#join) : [JoinGeometry](../nodes/JoinGeometry.md) geometry (Geometry)
- [**self.meth_name**](#proximity) : [GeometryProximity](../nodes/GeometryProximity.md) Sockets      [position (Vector), distance (Float)]
- [**self.meth_name**](#switch) : [Switch](../nodes/Switch.md) output (Geometry)
- [**self.meth_name**](#to_instance) : [GeometryToInstance](../nodes/GeometryToInstance.md) instances (Instances)
- [**self.meth_name**](#transfer_boolean) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Boolean)
- [**self.meth_name**](#transfer_color) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Color)
- [**self.meth_name**](#transfer_float) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Float)
- [**self.meth_name**](#transfer_integer) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Integer)
- [**self.meth_name**](#transfer_vector) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Vector)



## Stacked methods



- [**self.meth_name**](#delete_geometry) : [DeleteGeometry](../nodes/DeleteGeometry.md) Geometry
- [**self.meth_name**](#merge_by_distance) : [MergeByDistance](../nodes/MergeByDistance.md) Geometry
- [**self.meth_name**](#realize_instances) : [RealizeInstances](../nodes/RealizeInstances.md) Geometry
- [**self.meth_name**](#replace_material) : [ReplaceMaterial](../nodes/ReplaceMaterial.md) Geometry
- [**self.meth_name**](#scale_elements) : [ScaleElements](../nodes/ScaleElements.md) Geometry
- [**self.meth_name**](#set_id) : [SetID](../nodes/SetID.md) Geometry
- [**self.meth_name**](#set_material) : [SetMaterial](../nodes/SetMaterial.md) Geometry
- [**self.meth_name**](#set_material_index) : [SetMaterialIndex](../nodes/SetMaterialIndex.md) Geometry
- [**self.meth_name**](#set_position) : [SetPosition](../nodes/SetPosition.md) Geometry
- [**self.meth_name**](#set_shade_smooth) : [SetShadeSmooth](../nodes/SetShadeSmooth.md) Geometry
- [**self.meth_name**](#transform) : [Transform](../nodes/Transform.md) Geometry



## Methods reference


### ID

> Node: [ID](../nodes/{self.node_name}.md)

```python
v = geometry.ID(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.ID()
```


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



#### Node creation


```python
node = nodes.DomainSize(geometry=self, component=component)
```


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



#### Node creation


```python
node = nodes.AttributeRemove(*attribute, geometry=self)
```


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



#### Node creation


```python
node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
```


#### Returns

    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]

### box

> Node: [BoundingBox](../nodes/{self.node_name}.md)

```python
v = geometry.box
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.box"



#### Node creation


```python
node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box")
```


#### Returns

    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]

### box_max

> Node: [BoundingBox](../nodes/{self.node_name}.md)

```python
v = geometry.box_max
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.box_max"



#### Node creation


```python
node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_max")
```


#### Returns

    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]

### box_min

> Node: [BoundingBox](../nodes/{self.node_name}.md)

```python
v = geometry.box_min
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.box_min"



#### Node creation


```python
node = nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_min")
```


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



#### Node creation


```python
node = nodes.ID()
```


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



#### Node creation


```python
node = nodes.Index()
```


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



#### Node creation


```python
node = nodes.Normal()
```


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



#### Node creation


```python
node = nodes.Position()
```


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



#### Node creation


```python
node = nodes.Radius()
```


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



#### Node creation


```python
node = nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain)
```


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



#### Node creation


```python
node = nodes.ConvexHull(geometry=self)
```


#### Returns

    Geometry

### curve_component

> Node: [SeparateComponents](../nodes/{self.node_name}.md)

```python
v = geometry.curve_component
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.curve_component"



#### Node creation


```python
node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.curve_component")
```


#### Returns

    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]

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



#### Node creation


```python
node = nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode)
```


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



#### Node creation


```python
node = nodes.Index()
```


#### Returns

    Integer

### instances_component

> Node: [SeparateComponents](../nodes/{self.node_name}.md)

```python
v = geometry.instances_component
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.instances_component"



#### Node creation


```python
node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.instances_component")
```


#### Returns

    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]

### is_viewport

> Node: [IsViewport](../nodes/{self.node_name}.md)

```python
v = Geometry.is_viewport()
```


#### Arguments


#### Node creation


```python
node = nodes.IsViewport()
```


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



#### Node creation


```python
node = nodes.JoinGeometry(self, *geometry)
```


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



#### Node creation


```python
node = nodes.MergeByDistance(geometry=self, selection=selection, distance=distance)
```


#### Returns

    self

### mesh_component

> Node: [SeparateComponents](../nodes/{self.node_name}.md)

```python
v = geometry.mesh_component
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.mesh_component"



#### Node creation


```python
node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.mesh_component")
```


#### Returns

    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]

### normal

> Node: [Normal](../nodes/{self.node_name}.md)

```python
v = geometry.normal(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.Normal()
```


#### Returns

    Vector

### points_component

> Node: [SeparateComponents](../nodes/{self.node_name}.md)

```python
v = geometry.points_component
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.points_component"



#### Node creation


```python
node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.points_component")
```


#### Returns

    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]

### position

> Node: [Position](../nodes/{self.node_name}.md)

```python
v = geometry.position(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.Position()
```


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



#### Node creation


```python
node = nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element)
```


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



#### Node creation


```python
node = nodes.Radius()
```


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



#### Node creation


```python
node = nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior)
```


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



#### Node creation


```python
node = nodes.ReplaceMaterial(geometry=self, old=old, new=new)
```


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



#### Node creation


```python
node = nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode)
```


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



#### Node creation


```python
node = nodes.SetID(geometry=self, selection=selection, ID=ID)
```


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



#### Node creation


```python
node = nodes.SetMaterial(geometry=self, selection=selection, material=material)
```


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



#### Node creation


```python
node = nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index)
```


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



#### Node creation


```python
node = nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset)
```


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



#### Node creation


```python
node = nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth)
```


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



#### Node creation


```python
node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY')
```


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



#### Node creation


```python
node = nodes.GeometryToInstance(self, *geometry)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale)
```


#### Returns

    self

### volume_component

> Node: [SeparateComponents](../nodes/{self.node_name}.md)

```python
v = geometry.volume_component
```


#### Arguments


##### Sockets arguments



- geometry : Geometry (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.volume_component"



#### Node creation


```python
node = nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.volume_component")
```


#### Returns

    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
