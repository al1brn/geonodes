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

## Collection <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- collection: Collection
<sub>Go to [top](#class-Geometry)</sub>- separate_children: Boolean
<sub>Go to [top](#class-Geometry)</sub>- reset_children: Boolean
<sub>Go to [top](#class-Geometry)</sub>- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'geometry'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## ID <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def ID(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'ID'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## attribute_statistic

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## bounding_box <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def bounding_box(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'bounding_box'<sub>Go to [top](#class-Geometry)</sub> of class Mesh
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## bounding_box_min <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def bounding_box_min(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'min'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## bounding_box_min <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def bounding_box_min(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'max'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## capture_attribute

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def capture_attribute(self, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## capture_attribute_node

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- geometry: Geometry
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry', 'attribute']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## convex_hull <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def convex_hull(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'convex_hull'<sub>Go to [top](#class-Geometry)</sub> of class Mesh
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## curve_component <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def curve_component(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'curve'<sub>Go to [top](#class-Geometry)</sub> of class Curve
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## delete

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def delete(self, selection=None, domain='POINT', mode='ALL'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## domain_size <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def domain_size(self, component='MESH'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## duplicate

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def duplicate(self, selection=None, amount=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- amount: Integer
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'duplicate_index'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## field_at_index

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def field_at_index(self, index=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- index: Integer
<sub>Go to [top](#class-Geometry)</sub>- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'value'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## get_named_boolean

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def get_named_boolean(self, name=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## get_named_color

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def get_named_color(self, name=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## get_named_float

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def get_named_float(self, name=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## get_named_integer

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def get_named_integer(self, name=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## get_named_vector

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def get_named_vector(self, name=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def index(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'index'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## instances_component <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def instances_component(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'instances'<sub>Go to [top](#class-Geometry)</sub> of class Instances
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## is_viewport <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def is_viewport(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Is Viewport](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'is_viewport'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## join

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def join(*geometry):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- geometry: <m>Geometry
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## material_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def material_index(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'material_index'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## material_selection

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def material_selection(self, material=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- material: Material
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'selection'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## merge_by_distance

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def merge_by_distance(self, selection=None, distance=None, mode='ALL'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- distance: Float
<sub>Go to [top](#class-Geometry)</sub>- mode (str): 'ALL' in [ALL, CONNECTED]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## mesh_component <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def mesh_component(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'mesh'<sub>Go to [top](#class-Geometry)</sub> of class Mesh
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## named_attribute

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def named_attribute(self, name=None, data_type='FLOAT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'attribute'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## normal <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def normal(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'normal'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## points_component <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def points_component(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'point_cloud'<sub>Go to [top](#class-Geometry)</sub> of class Points
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## position <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def position(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'position'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## proximity

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def proximity(self, target=None, source_position=None, target_element='FACES'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target: Geometry
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>- target_element (str): 'FACES' in [POINTS, EDGES, FACES]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'distance'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## proximity_edges

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def proximity_edges(self, target=None, source_position=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target: Geometry
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'distance'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## proximity_facess

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def proximity_facess(self, target=None, source_position=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target: Geometry
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'distance'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## proximity_points

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def proximity_points(self, target=None, source_position=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target: Geometry
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'distance'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## radius <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def radius(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html) )

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'radius'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## random_boolean

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def random_boolean(self, probability=None, ID=None, seed=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- probability: Float
<sub>Go to [top](#class-Geometry)</sub>- ID: Integer
<sub>Go to [top](#class-Geometry)</sub>- seed: Integer
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'value'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## random_float

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def random_float(self, min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- ID: Integer
<sub>Go to [top](#class-Geometry)</sub>- seed: Integer
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'value'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## random_integer

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def random_integer(self, min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- ID: Integer
<sub>Go to [top](#class-Geometry)</sub>- seed: Integer
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'value'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## random_vector

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def random_vector(self, min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- ID: Integer
<sub>Go to [top](#class-Geometry)</sub>- seed: Integer
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'value'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## raycast

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target_geometry: Geometry
<sub>Go to [top](#class-Geometry)</sub>- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>- ray_direction: Vector
<sub>Go to [top](#class-Geometry)</sub>- ray_length: Float
<sub>Go to [top](#class-Geometry)</sub>- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## raycast_interpolated

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target_geometry: Geometry
<sub>Go to [top](#class-Geometry)</sub>- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>- ray_direction: Vector
<sub>Go to [top](#class-Geometry)</sub>- ray_length: Float
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## raycast_nearest

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- target_geometry: Geometry
<sub>Go to [top](#class-Geometry)</sub>- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- source_position: Vector
<sub>Go to [top](#class-Geometry)</sub>- ray_direction: Vector
<sub>Go to [top](#class-Geometry)</sub>- ray_length: Float
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## remove_named_attribute

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def remove_named_attribute(self, name=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## replace_material

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def replace_material(self, old=None, new=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- old: Material
<sub>Go to [top](#class-Geometry)</sub>- new: Material
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## sample_index

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Geometry)</sub>- index: Integer
<sub>Go to [top](#class-Geometry)</sub>- clamp (bool): False
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'value'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## sample_nearest

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def sample_nearest(self, sample_position=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- sample_position: Vector
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'index'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## separate

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def separate(self, geometry=None, selection=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- geometry: Geometry
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- tuple ('selection', 'inverted')
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## separate_components <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def separate_components(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_ID

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_ID(self, selection=None, ID=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- ID: Integer
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_material

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_material(self, selection=None, material=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- material: Material
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_material_index

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_material_index(self, selection=None, material_index=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- material_index: Integer
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_named_boolean

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_named_boolean(self, name=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_named_color

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_named_color(self, name=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_named_float

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_named_float(self, name=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_named_integer

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_named_integer(self, name=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_named_vector

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_named_vector(self, name=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## set_position

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def set_position(self, selection=None, position=None, offset=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- selection: Boolean
<sub>Go to [top](#class-Geometry)</sub>- position: Vector
<sub>Go to [top](#class-Geometry)</sub>- offset: Vector
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## store_named_attribute

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def store_named_attribute(self, name=None, value=None, domain='POINT'):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- name: String
<sub>Go to [top](#class-Geometry)</sub>- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Geometry)</sub>- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## switch

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Geometry)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'output'<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## to_instance

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def to_instance(*geometry):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- geometry: <m>Geometry
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'instances'<sub>Go to [top](#class-Geometry)</sub> of class Instances
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## transform

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def transform(self, translation=None, rotation=None, scale=None):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html) )

<sub>Go to [top](#class-Geometry)</sub>### Args:
<sub>Go to [top](#class-Geometry)</sub>- translation: Vector
<sub>Go to [top](#class-Geometry)</sub>- rotation: Vector
<sub>Go to [top](#class-Geometry)</sub>- scale: Vector
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>## volume_component <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Geometry)</sub>```python
<sub>Go to [top](#class-Geometry)</sub>def volume_component(self):

<sub>Go to [top](#class-Geometry)</sub>```
<sub>Go to [top](#class-Geometry)</sub>Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html) )

<sub>Go to [top](#class-Geometry)</sub>Node implemented as property.

<sub>Go to [top](#class-Geometry)</sub>### Returns:

<sub>Go to [top](#class-Geometry)</sub>  socket 'volume'<sub>Go to [top](#class-Geometry)</sub> of class Volume
<sub>Go to [top](#class-Geometry)</sub>
<sub>Go to [top](#class-Geometry)</sub>