# class Geometry

## Properties

- [ID](#ID-property)
- [bounding_box](#bounding_box-property)
- [bounding_box_min](#bounding_box_min-property)
- [bounding_box_min](#bounding_box_min-property)
- [convex_hull](#convex_hull-property)
- [curve_component](#curve_component-property)
- [domain_size](#domain_size-property)
- [index](#index-property)
- [instances_component](#instances_component-property)
- [is_viewport](#is_viewport-property)
- [material_index](#material_index-property)
- [mesh_component](#mesh_component-property)
- [normal](#normal-property)
- [points_component](#points_component-property)
- [position](#position-property)
- [radius](#radius-property)
- [separate_components](#separate_components-property)
- [volume_component](#volume_component-property)

## Class methods

- [Collection](#Collection-classmethod)


## Methods

- [attribute_statistic](#attribute_statistic)
- [capture_attribute](#capture_attribute)
- [capture_attribute_node](#capture_attribute_node)
- [delete](#delete)
- [duplicate](#duplicate)
- [field_at_index](#field_at_index)
- [get_named_boolean](#get_named_boolean)
- [get_named_color](#get_named_color)
- [get_named_float](#get_named_float)
- [get_named_integer](#get_named_integer)
- [get_named_vector](#get_named_vector)
- [join](#join)
- [material_selection](#material_selection)
- [merge_by_distance](#merge_by_distance)
- [named_attribute](#named_attribute)
- [proximity](#proximity)
- [proximity_edges](#proximity_edges)
- [proximity_facess](#proximity_facess)
- [proximity_points](#proximity_points)
- [random_boolean](#random_boolean)
- [random_float](#random_float)
- [random_integer](#random_integer)
- [random_vector](#random_vector)
- [raycast](#raycast)
- [raycast_interpolated](#raycast_interpolated)
- [raycast_nearest](#raycast_nearest)
- [remove_named_attribute](#remove_named_attribute)
- [replace_material](#replace_material)
- [sample_index](#sample_index)
- [sample_nearest](#sample_nearest)
- [separate](#separate)
- [set_ID](#set_ID)
- [set_material](#set_material)
- [set_material_index](#set_material_index)
- [set_named_boolean](#set_named_boolean)
- [set_named_color](#set_named_color)
- [set_named_float](#set_named_float)
- [set_named_integer](#set_named_integer)
- [set_named_vector](#set_named_vector)
- [set_position](#set_position)
- [store_named_attribute](#store_named_attribute)
- [switch](#switch)
- [to_instance](#to_instance)
- [transform](#transform)

## Collection <sub>*classmethod*</sub>

```python
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):

```
Node [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html) )

### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:
- socket `geometry`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## ID <sub>*property*</sub>

```python
def ID(self):

```
Node [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html) )

### Returns:
- socket `ID`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):

```
Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## bounding_box <sub>*property*</sub>

```python
def bounding_box(self):

```
Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html) )

### Returns:
- socket `bounding_box` of class Mesh

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## bounding_box_min <sub>*property*</sub>

```python
def bounding_box_min(self):

```
Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html) )

### Returns:
- socket `min`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## bounding_box_min <sub>*property*</sub>

```python
def bounding_box_min(self):

```
Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html) )

### Returns:
- socket `max`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT'):

```
Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html) )

### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## capture_attribute_node

```python
def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT'):

```
Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html) )

### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- node with sockets ['geometry', 'attribute']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## convex_hull <sub>*property*</sub>

```python
def convex_hull(self):

```
Node [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html) )

### Returns:
- socket `convex_hull` of class Mesh

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## curve_component <sub>*property*</sub>

```python
def curve_component(self):

```
Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

### Returns:
- socket `curve` of class Curve

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL'):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self, component='MESH'):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT'):

```
Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html) )

### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT'):

```
Node [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html) )

### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- socket `value`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## get_named_boolean

```python
def get_named_boolean(self, name=None):

```
Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

### Args:
- name: String

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## get_named_color

```python
def get_named_color(self, name=None):

```
Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

### Args:
- name: String

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## get_named_float

```python
def get_named_float(self, name=None):

```
Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

### Args:
- name: String

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## get_named_integer

```python
def get_named_integer(self, name=None):

```
Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

### Args:
- name: String

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## get_named_vector

```python
def get_named_vector(self, name=None):

```
Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

### Args:
- name: String

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## index <sub>*property*</sub>

```python
def index(self):

```
Node [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html) )

### Returns:
- socket `index`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## instances_component <sub>*property*</sub>

```python
def instances_component(self):

```
Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## is_viewport <sub>*property*</sub>

```python
def is_viewport(self):

```
Node [Is Viewport](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html) )

### Returns:
- socket `is_viewport`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## join

```python
def join(*geometry):

```
Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html) )

### Args:
- geometry: <m>Geometry

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## material_index <sub>*property*</sub>

```python
def material_index(self):

```
Node [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html) )

### Returns:
- socket `material_index`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## material_selection

```python
def material_selection(self, material=None):

```
Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html) )

### Args:
- material: Material

### Returns:
- socket `selection`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL'):

```
Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html) )

### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## mesh_component <sub>*property*</sub>

```python
def mesh_component(self):

```
Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT'):

```
Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

### Returns:
- socket `attribute`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## normal <sub>*property*</sub>

```python
def normal(self):

```
Node [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html) )

### Returns:
- socket `normal`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## points_component <sub>*property*</sub>

```python
def points_component(self):

```
Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

### Returns:
- socket `point_cloud` of class Points

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## position <sub>*property*</sub>

```python
def position(self):

```
Node [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html) )

### Returns:
- socket `position`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES'):

```
Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

### Returns:
- socket `distance`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## proximity_edges

```python
def proximity_edges(self, target=None, source_position=None):

```
Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

### Args:
- target: Geometry
- source_position: Vector

### Returns:
- socket `distance`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## proximity_facess

```python
def proximity_facess(self, target=None, source_position=None):

```
Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

### Args:
- target: Geometry
- source_position: Vector

### Returns:
- socket `distance`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## proximity_points

```python
def proximity_points(self, target=None, source_position=None):

```
Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

### Args:
- target: Geometry
- source_position: Vector

### Returns:
- socket `distance`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## radius <sub>*property*</sub>

```python
def radius(self):

```
Node [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html) )

### Returns:
- socket `radius`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None):

```
Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

### Args:
- probability: Float
- ID: Integer
- seed: Integer

### Returns:
- socket `value`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None):

```
Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:
- socket `value`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None):

```
Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:
- socket `value`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None):

```
Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:
- socket `value`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):

```
Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html) )

### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

```
Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html) )

### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

```
Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html) )

### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## remove_named_attribute

```python
def remove_named_attribute(self, name=None):

```
Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html) )

### Args:
- name: String

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## replace_material

```python
def replace_material(self, old=None, new=None):

```
Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html) )

### Args:
- old: Material
- new: Material

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):

```
Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html) )

### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- socket `value`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT'):

```
Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html) )

### Args:
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

### Returns:
- socket `index`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## separate

```python
def separate(self, geometry=None, selection=None, domain='POINT'):

```
Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html) )

### Args:
- geometry: Geometry
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:
- tuple ('`selection`', '`inverted`')

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## separate_components <sub>*property*</sub>

```python
def separate_components(self):

```
Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

### Returns:
- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_ID

```python
def set_ID(self, selection=None, ID=None):

```
Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html) )

### Args:
- selection: Boolean
- ID: Integer

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_material

```python
def set_material(self, selection=None, material=None):

```
Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

### Args:
- selection: Boolean
- material: Material

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_material_index

```python
def set_material_index(self, selection=None, material_index=None):

```
Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html) )

### Args:
- selection: Boolean
- material_index: Integer

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_named_boolean

```python
def set_named_boolean(self, name=None, value=None, domain='POINT'):

```
Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_named_color

```python
def set_named_color(self, name=None, value=None, domain='POINT'):

```
Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_named_float

```python
def set_named_float(self, name=None, value=None, domain='POINT'):

```
Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_named_integer

```python
def set_named_integer(self, name=None, value=None, domain='POINT'):

```
Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_named_vector

```python
def set_named_vector(self, name=None, value=None, domain='POINT'):

```
Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## set_position

```python
def set_position(self, selection=None, position=None, offset=None):

```
Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html) )

### Args:
- selection: Boolean
- position: Vector
- offset: Vector

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT'):

```
Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: Boolean
- false: Geometry

### Returns:
- socket `output`

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## to_instance

```python
def to_instance(*geometry):

```
Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html) )

### Args:
- geometry: <m>Geometry

### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## transform

```python
def transform(self, translation=None, rotation=None, scale=None):

```
Node [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html) )

### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

### Returns:
- self

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

## volume_component <sub>*property*</sub>

```python
def volume_component(self):

```
Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Geometry) [data structure](../structure.md)</sub>

