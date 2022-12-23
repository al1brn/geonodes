# Class Edge

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

### ID

 Node ID.

Node reference [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)
Developer reference [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`



Setter

 Node SetID.

Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

Node implemented as property setter.

#### Args:
- attr_value: ID




### angle

 Node EdgeAngle.

Node reference [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
Developer reference [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

#### Returns:
- node with sockets ['unsigned_angle', 'signed_angle']



### count

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `edge_count`



### domain_index

 Node Index.

Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`



### index

 Node Index.

Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`



### material_index

 Node MaterialIndex.

Node reference [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
Developer reference [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`



### neighbors

 Node EdgeNeighbors.

Node reference [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html)
Developer reference [GeometryNodeInputMeshEdgeNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)

#### Returns:
- socket `face_count`



### normal

 Node Normal.

Node reference [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
Developer reference [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`



### position

 Node Position.

Node reference [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
Developer reference [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`



Setter

 Node SetPosition.

Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: position




### signed_angle

 Node EdgeAngle.

Node reference [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
Developer reference [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

#### Returns:
- socket `signed_angle`



### unsigned_angle

 Node EdgeAngle.

Node reference [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
Developer reference [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

#### Returns:
- socket `unsigned_angle`



### vertices

 Node EdgeVertices.

Node reference [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
Developer reference [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

#### Returns:
- node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']



### vertices_index

 Node EdgeVertices.

Node reference [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
Developer reference [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

#### Returns:
- tuple ('vertex_index_1', 'vertex_index_2')



### vertices_position

 Node EdgeVertices.

Node reference [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
Developer reference [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

#### Returns:
- tuple ('position_1', 'position_2')



## Methods

### accumulate_field

```python
def accumulate_field(self, value=None, group_index=None)
```

 Node AccumulateField.

Node reference [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html)
Developer reference [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

#### Args:
- value: ['Vector', 'Float', 'Integer']
- group_index: Integer

#### Returns:
- tuple ('leading', 'trailing', 'total')



### attribute_max

```python
def attribute_max(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `max`



### attribute_mean

```python
def attribute_mean(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `mean`



### attribute_median

```python
def attribute_median(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `median`



### attribute_min

```python
def attribute_min(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `min`



### attribute_range

```python
def attribute_range(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `range`



### attribute_statistic

```python
def attribute_statistic(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']



### attribute_std

```python
def attribute_std(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `standard_deviation`



### attribute_sum

```python
def attribute_sum(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `sum`



### attribute_var

```python
def attribute_var(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `variance`



### capture_attribute

```python
def capture_attribute(self, value=None)
```

 Node CaptureAttribute.

Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- socket `attribute`



### delete

```python
def delete(self, mode='ALL')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- node with sockets ['geometry']



### delete_all

```python
def delete_all(self)
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- node with sockets ['geometry']



### delete_edges

```python
def delete_edges(self)
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- node with sockets ['geometry']



### delete_faces

```python
def delete_faces(self)
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- node with sockets ['geometry']



### duplicate

```python
def duplicate(self, amount=None)
```

 Node DuplicateElements.

Node reference [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
Developer reference [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`



### edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None)
```

 Node EdgePathsToCurves.

Node reference [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html)
Developer reference [GeometryNodeEdgePathsToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `curves` [Curve](Curve.md)



### extrude

```python
def extrude(self, offset=None, offset_scale=None, individual=None)
```

 Node ExtrudeMesh.

Node reference [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
Developer reference [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

#### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

#### Returns:
- tuple ('top', 'side')



### field_at_index

```python
def field_at_index(self, index=None, value=None)
```

 Node FieldAtIndex.

Node reference [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
Developer reference [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`



### get_named_boolean

```python
def get_named_boolean(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_color

```python
def get_named_color(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_float

```python
def get_named_float(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_integer

```python
def get_named_integer(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_vector

```python
def get_named_vector(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### interpolate

```python
def interpolate(self, value=None)
```

 Node InterpolateDomain.

Node reference [Interpolate Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html)
Developer reference [GeometryNodeFieldOnDomain](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`



### material_selection

```python
def material_selection(self, material=None)
```

 Node MaterialSelection.

Node reference [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
Developer reference [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`



### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`



### proximity

```python
def proximity(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`



### random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```

 Node RemoveNamedAttribute.

Node reference [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
Developer reference [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- node with sockets ['geometry']



### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False)
```

 Node SampleIndex.

Node reference [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
Developer reference [GeometryNodeSampleIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False

#### Returns:
- socket `value`



### sample_nearest

```python
def sample_nearest(self, sample_position=None)
```

 Node SampleNearest.

Node reference [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)
Developer reference [GeometryNodeSampleNearest](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector

#### Returns:
- socket `index`



### scale_single_axis

```python
def scale_single_axis(self, scale=None, center=None, axis=None)
```

 Node ScaleElements.

Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- scale: Float
- center: Vector
- axis: Vector

#### Returns:
- node with sockets ['geometry']



### scale_uniform

```python
def scale_uniform(self, scale=None, center=None)
```

 Node ScaleElements.

Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- scale: Float
- center: Vector

#### Returns:
- node with sockets ['geometry']



### separate

```python
def separate(self, geometry=None)
```

 Node SeparateGeometry.

Node reference [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
Developer reference [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry

#### Returns:
- tuple ('selection', 'inverted')



### set_ID

```python
def set_ID(self, ID=None)
```

 Node SetID.

Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- ID: Integer

#### Returns:
- node with sockets ['geometry']



### set_material_index

```python
def set_material_index(self, material_index=None)
```

 Node SetMaterialIndex.

Node reference [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
Developer reference [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- material_index: Integer

#### Returns:
- node with sockets ['geometry']



### set_named_boolean

```python
def set_named_boolean(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



### set_named_color

```python
def set_named_color(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



### set_named_float

```python
def set_named_float(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



### set_named_integer

```python
def set_named_integer(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



### set_named_vector

```python
def set_named_vector(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



### set_position

```python
def set_position(self, position=None, offset=None)
```

 Node SetPosition.

Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- node with sockets ['geometry']



### split

```python
def split(self)
```

 Node SplitEdges.

Node reference [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html)
Developer reference [GeometryNodeSplitEdges](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

#### Returns:
- node with sockets ['mesh']



### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



### to_curve

```python
def to_curve(self)
```

 Node MeshToCurve.

Node reference [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)
Developer reference [GeometryNodeMeshToCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

#### Returns:
- socket `curve` [Curve](Curve.md)



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

