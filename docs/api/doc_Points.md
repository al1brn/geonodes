# Class Points

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[ID](#ID) | [bl_idname](#bl_idname) | [bnode](#bnode) | [bounding_box](#bounding_box) | [bounding_box_min](#bounding_box_min) | [convex_hull](#convex_hull) | [curve_component](#curve_component) | [domain_size](#domain_size) | [index](#index) | [instances_component](#instances_component) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [is_plugged](#is_plugged) | [is_viewport](#is_viewport) | [links](#links) | [material_index](#material_index) | [mesh_component](#mesh_component) | [name](#name) | [node_chain_label](#node_chain_label) | [normal](#normal) | [points_component](#points_component) | [position](#position) | [radius](#radius) | [separate_components](#separate_components) | [socket_index](#socket_index) | [volume_component](#volume_component)

**Class and static methods**

[Collection](#Collection) | [FromCollection](#FromCollection) | [Input](#Input) | [Points](#Points) | [get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [value_data_type](#value_data_type)

**Methods**

[attribute_statistic](#attribute_statistic) | [capture_attribute](#capture_attribute) | [capture_attribute_node](#capture_attribute_node) | [connected_sockets](#connected_sockets) | [convert_python_type](#convert_python_type) | [delete](#delete) | [duplicate](#duplicate) | [field_at_index](#field_at_index) | [get_blender_socket](#get_blender_socket) | [get_named_boolean](#get_named_boolean) | [get_named_color](#get_named_color) | [get_named_float](#get_named_float) | [get_named_integer](#get_named_integer) | [get_named_vector](#get_named_vector) | [init_domains](#init_domains) | [init_socket](#init_socket) | [instance_on_points](#instance_on_points) | [instantiate](#instantiate) | [interpolate_domain](#interpolate_domain) | [join](#join) | [material_selection](#material_selection) | [merge_by_distance](#merge_by_distance) | [named_attribute](#named_attribute) | [plug](#plug) | [proximity](#proximity) | [proximity_edges](#proximity_edges) | [proximity_faces](#proximity_faces) | [proximity_points](#proximity_points) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector) | [raycast](#raycast) | [raycast_interpolated](#raycast_interpolated) | [raycast_nearest](#raycast_nearest) | [remove_named_attribute](#remove_named_attribute) | [replace_material](#replace_material) | [reroute](#reroute) | [reset_properties](#reset_properties) | [sample_index](#sample_index) | [sample_nearest](#sample_nearest) | [separate](#separate) | [set_ID](#set_ID) | [set_material](#set_material) | [set_material_index](#set_material_index) | [set_named_boolean](#set_named_boolean) | [set_named_color](#set_named_color) | [set_named_float](#set_named_float) | [set_named_integer](#set_named_integer) | [set_named_vector](#set_named_vector) | [set_point_radius](#set_point_radius) | [set_position](#set_position) | [show_handles](#show_handles) | [stack](#stack) | [store_named_attribute](#store_named_attribute) | [switch](#switch) | [to_instance](#to_instance) | [to_output](#to_output) | [to_vertices](#to_vertices) | [to_volume](#to_volume) | [to_volume_amount](#to_volume_amount) | [to_volume_size](#to_volume_size) | [transform](#transform)

## Properties

### ID



## ID <sub>*property*</sub>

```python
def ID(self):

```
> Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`






### bl_idname

 Shortcut for `self.bsocket.bl_idname`

Returns:
    socket bl_idname (str)



### bnode

 Shortcut for `self.bsocket.node`

Returns:
    Blender node (bpy.types.Node)



### bounding_box



## bounding_box <sub>*property*</sub>

```python
def bounding_box(self):

```
> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `bounding_box` of class Mesh






### bounding_box_min



## bounding_box_min <sub>*property*</sub>

```python
def bounding_box_min(self):

```
> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `max`






### convex_hull



## convex_hull <sub>*property*</sub>

```python
def convex_hull(self):

```
> Node: [Convex Hull](GeometryNodeConvexHull.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

#### Returns:
- socket `convex_hull` of class Mesh






### curve_component



## curve_component <sub>*property*</sub>

```python
def curve_component(self):

```
> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `curve` of class Curve






### domain_size



## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`






### index



## index <sub>*property*</sub>

```python
def index(self):

```
> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






### instances_component



## instances_component <sub>*property*</sub>

```python
def instances_component(self):

```
> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `instances` of class Instances






### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`

Returns:
    is multi input socket (bool)



### is_output

 Shortcut for `self.bsocket.is_output`

Returns:
    is an aoutput socket (bool)



### is_plugged

 Indicates if the socket is connected or not.

Raise an exception if called on an output socket.

Returns:
    is plugged (bool)



### is_viewport



## is_viewport <sub>*property*</sub>

```python
def is_viewport(self):

```
> Node: [Is Viewport](GeometryNodeIsViewport.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)

#### Returns:
- socket `is_viewport`






### links

 Shortcut for `self.bsocket.links`      

Returns:
    list of links (list)



### material_index



## material_index <sub>*property*</sub>

```python
def material_index(self):

```
> Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`






### mesh_component



## mesh_component <sub>*property*</sub>

```python
def mesh_component(self):

```
> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `mesh` of class Mesh






### name

 Shortcut for `self.bsocket.name`

Returns:
    socket name (str)



### node_chain_label

 Shortcut for *self.node.chain_label*



### normal



## normal <sub>*property*</sub>

```python
def normal(self):

```
> Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`






### points_component



## points_component <sub>*property*</sub>

```python
def points_component(self):

```
> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `point_cloud` of class Points






### position



## position <sub>*property*</sub>

```python
def position(self):

```
> Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`






### radius



## radius <sub>*property*</sub>

```python
def radius(self):

```
> Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`






### separate_components



## separate_components <sub>*property*</sub>

```python
def separate_components(self):

```
> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']






### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.

Returns:
    socket index (int)




### volume_component



## volume_component <sub>*property*</sub>

```python
def volume_component(self):

```
> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `volume` of class Volume






## Class and static methods

### Collection

```python
@classmethod
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```



## Collection <sub>*classmethod*</sub>

```python
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):

```
> Node: [Collection Info](GeometryNodeCollectionInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

#### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection

.. blid:: GeometryNodeCollectionInfo



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, name = None, description = "")
```

 Create a Geometry input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
Returns:
    Geometry: The Geometry data socket
    
Note
----
    This method create a new input socket in the Group Input node. To get the **default** input geometry,
    use :attr:`Tree.input_geometry`.
    



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Points

```python
@classmethod
def Points(cls, count=None, position=None, radius=None)
```



## Points <sub>*classmethod*</sub>

```python
def Points(cls, count=None, position=None, radius=None):

```
> Node: [Points](GeometryNodePoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)

#### Args:
- count: Integer
- position: Vector
- radius: Float

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to **sub classes**:
    
| Sub class                 | bl_idname                     |
|---------------------------|-------------------------------|
| Unsigned                  | NodeSocketIntUnsigned         |
| Factor                    | NodeSocketFloatFactor         |
| Angle                     | NodeSocketFloatAngle          |
| Distance                  | NodeSocketFloatDistance       |
| Rotation                  | NodeSocketVectorEuler         |
| xyz                       | NodeSocketVectorXYZ           |
| Translation               | NodeSocketVectorTranslation   |
  
These additional values allow to enter angle, distance, factor... as group input values.

#### Args:
- class_name (str): the name of the class
    
Returns:
    bl_idname (str)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

| Socket bl_idname              | Geondes class name    | Sub class             |
l-------------------------------|-----------------------|-----------------------|
| NodeSocketBool                | Boolean               | None                  |
| NodeSocketInt                 | Integer               | None                  |
| NodeSocketIntUnsigned         | Integer               | NoUnsigned            |
| NodeSocketFloat               | Float                 | None                  |
| NodeSocketFloatFactor         | Float                 | Factor                |
| NodeSocketFloatAngle          | Float                 | Angle                 |
| NodeSocketFloatDistance       | Float                 | Distance              |
| NodeSocketVector              | Vector                | None                  |
| NodeSocketVectorEuler         | Vector                | Rotation              |
| NodeSocketVectorXYZ           | Vector                | xyz                   |
| NodeSocketVectorTranslation   | Vector                | Translation           |
| NodeSocketColor               | Color                 | None                  |
| NodeSocketString              | String                | None                  |
| NodeSocketCollection          | Collection            | None                  |
| NodeSocketImage               | Image                 | None                  |
| NodeSocketMaterial            | Material              | None                  |
| NodeSocketObject              | Object                | None                  |
| NodeSocketTexture             | Texture               | None                  |
| NodeSocketGeometry            | Geometry              | None                  |

If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.

#### Args:
- socket (bpy.type.NodeSocket): the socket to use
- with_sub_class (bool): return as as second value the sub type of the socket
        



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

#### Args:
- value (any): The value to test
    
Returns:
    value is bpy.types.NodeSocket or Socket (bool)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

#### Args:
- value (any): The value to test
    
Returns:
    is a socket (bool)



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

#### Args:
- value (any): The value to test
    
Returns:
    is a socket (bool)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color='FLOAT_COLOR')
```

 Returns the data type to which the socket belongs.

This methods is used to compute the **data_type** value in nodes accepting multitype values.

|    Socket                     |    data_type    |
|-------------------------------|-----------------|
| NodeSocketBool                | 'BOOLEAN'       |
| NodeSocketInt                 | 'INT'           |
| NodeSocketIntUnsigned         | 'INT'           |
| NodeSocketFloat               | 'FLOAT'         |
| NodeSocketFloatFactor         | 'FLOAT'         |
| NodeSocketFloatAngle          | 'FLOAT'         |
| NodeSocketFloatDistance       | 'FLOAT'         |
| NodeSocketVector              | 'FLOAT_VECTOR'  |
| NodeSocketVectorEuler         | 'FLOAT_VECTOR'  |
| NodeSocketVectorXYZ           | 'FLOAT_VECTOR'  |
| NodeSocketVectorTranslation   | 'FLOAT_VECTOR'  |
| NodeSocketColor               | color           |                

#### Args:
- value (any): the value to analyze
- default (str): default data_type
- color (str): code for color data_type
    
Returns:
    the data type of the value





<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT')
```



## attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT')
```



## capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT'):

```
> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute_node

```python
def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT')
```



## capture_attribute_node

```python
def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT'):

```
> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry', 'attribute']






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### connected_sockets

```python
def connected_sockets(self)
```

 Returns the list of Socket instances linked to this socket.

Returns:
    list of connected sockets (list of Sockets)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### convert_python_type

```python
def convert_python_type(self, value, raise_exception=True)
```

 Convert a python value to a value which can be plug in the socket.

The following table gives the conversion rules:
    
| Socket type       | Conversion                                                    |
l-------------------|---------------------------------------------------------------|
| Boolean           | bool(value)                                                   |
| Integer           | int(value)                                                    |
| Float             | float(value)                                                  |
| Vector            | A triplet or the value if compatible (mathutils.Vector,...)   |
| Color             | A quadruplet or the value if compatible (mathutils.Color,...) |
| String            | str(value)                                                    |
| Collection        | value is value is a collection, bpy.data.collections[value] otherwise |
| Object            | value is value is an object, bpy.data.objects[value] otherwise        |
| Image             | value is value is an image, bpy.data.images[value] otherwise          |
| Texture           | value is value is a texture, bpy.data.textures[value] otherwise       |
| Material          | value is value is a material, bpy.data.materials[value] otherwise     |

This method allows in particular to refer to Blender resources by their name:
    
```python
# Set a material to a mesh
mesh.faces.material = "Material"

# Is equivalent to
mesh.faces.material = bpy.data.materials["Material"]
```

#### Args:
- value (any): the value to convert
- raise_exeption (bool): False to avod raising an exception in case of error.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL')
```



## delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT')
```



## duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT'):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

#### Returns:
- socket `duplicate_index`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT')
```



## field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT'):

```
> Node: [Field at Index](GeometryNodeFieldAtIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Returns the property bsocket.

Returns:
    bsocket (bpy.types.NodeSocket)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_boolean

```python
def get_named_boolean(self, name=None)
```



## get_named_boolean

```python
def get_named_boolean(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_color

```python
def get_named_color(self, name=None)
```



## get_named_color

```python
def get_named_color(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_float

```python
def get_named_float(self, name=None)
```



## get_named_float

```python
def get_named_float(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_integer

```python
def get_named_integer(self, name=None)
```



## get_named_integer

```python
def get_named_integer(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_vector

```python
def get_named_vector(self, name=None)
```



## get_named_vector

```python
def get_named_vector(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```



## instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instantiate

```python
def instantiate(self, count = 1, realize = False)
```

 Instantiate the geometry

#### Args:
- count: Number of instances to create
- realize: True to realize the instances
    
Returns:
    Instances or Geometry
    
The duplication is performed by instantiating the geometry along the vertices
of a Mesh Line initialized with `count` points.

The operator ``*`` can be used to operate this method with `realize = False`:
    
.. code-block::
    
    curves = curve * 10
    
    # is equivalent to
    
    curves = curve.duplicate(10, realize=False)
    




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### interpolate_domain

```python
def interpolate_domain(self, value=None, domain='POINT')
```



## interpolate_domain

```python
def interpolate_domain(self, value=None, domain='POINT'):

```
> Node: [Interpolate Domain](GeometryNodeFieldOnDomain.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join

```python
def join(*geometry)
```



## join

```python
def join(*geometry):

```
> Node: [Join Geometry](GeometryNodeJoinGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_selection

```python
def material_selection(self, material=None)
```



## material_selection

```python
def material_selection(self, material=None):

```
> Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL')
```



## merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL'):

```
> Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

#### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```



## named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT'):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

#### Args:
- values (any): The output sockets. More than one values can be passed if the input socket is multi input.
    
Returns:
    None



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES')
```



## proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES'):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_edges

```python
def proximity_edges(self, target=None, source_position=None)
```



## proximity_edges

```python
def proximity_edges(self, target=None, source_position=None):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_faces

```python
def proximity_faces(self, target=None, source_position=None)
```



## proximity_faces

```python
def proximity_faces(self, target=None, source_position=None):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_points

```python
def proximity_points(self, target=None, source_position=None)
```



## proximity_points

```python
def proximity_points(self, target=None, source_position=None):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None)
```



## random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None)
```



## random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None)
```



## random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None)
```



## random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```



## raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):

```
> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



## raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

```
> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



## raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

```
> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```



## remove_named_attribute

```python
def remove_named_attribute(self, name=None):

```
> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### replace_material

```python
def replace_material(self, old=None, new=None)
```



## replace_material

```python
def replace_material(self, old=None, new=None):

```
> Node: [Replace Material](GeometryNodeReplaceMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

#### Args:
- old: Material
- new: Material

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reroute

```python
def reroute(self)
```

 Reroute all output links



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT')
```



## sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):

```
> Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT')
```



## sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT'):

```
> Node: [Sample Nearest](GeometryNodeSampleNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

#### Returns:
- socket `index`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self, geometry=None, selection=None, domain='POINT')
```



## separate

```python
def separate(self, geometry=None, selection=None, domain='POINT'):

```
> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, selection=None, ID=None)
```



## set_ID

```python
def set_ID(self, selection=None, ID=None):

```
> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- selection: Boolean
- ID: Integer

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material

```python
def set_material(self, selection=None, material=None)
```



## set_material

```python
def set_material(self, selection=None, material=None):

```
> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- selection: Boolean
- material: Material

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material_index

```python
def set_material_index(self, selection=None, material_index=None)
```



## set_material_index

```python
def set_material_index(self, selection=None, material_index=None):

```
> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- selection: Boolean
- material_index: Integer

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_boolean

```python
def set_named_boolean(self, name=None, value=None, domain='POINT')
```



## set_named_boolean

```python
def set_named_boolean(self, name=None, value=None, domain='POINT'):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_color

```python
def set_named_color(self, name=None, value=None, domain='POINT')
```



## set_named_color

```python
def set_named_color(self, name=None, value=None, domain='POINT'):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_float

```python
def set_named_float(self, name=None, value=None, domain='POINT')
```



## set_named_float

```python
def set_named_float(self, name=None, value=None, domain='POINT'):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_integer

```python
def set_named_integer(self, name=None, value=None, domain='POINT')
```



## set_named_integer

```python
def set_named_integer(self, name=None, value=None, domain='POINT'):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_vector

```python
def set_named_vector(self, name=None, value=None, domain='POINT')
```



## set_named_vector

```python
def set_named_vector(self, name=None, value=None, domain='POINT'):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_point_radius

```python
def set_point_radius(self, selection=None, radius=None)
```



## set_point_radius

```python
def set_point_radius(self, selection=None, radius=None):

```
> Node: [Set Point Radius](GeometryNodeSetPointRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

#### Args:
- selection: Boolean
- radius: Float

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, selection=None, position=None, offset=None)
```



## set_position

```python
def set_position(self, selection=None, position=None, offset=None):

```
> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- selection: Boolean
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### show_handles

```python
def show_handles(self)
```

 Generate a mesh and cloud points to visualize the control points and handles

Returns:
    Geometry: The geometry can be joined to the output
    
Example:
    
    .. code-block:: python
    
        curve = ... # Curve initialization
        
        visu = curve.show_handles()
        
        tree.output_geometry = curve + visu
    




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

After the call, **the DataSocket** instance wraps a different socket, typically in a newly created node.
This is an internally used by the **geonodes** engine.

In the following example, the `mesh`

```python

# After the following instruction, mesh wraps the output socket of the Cube node
mesh = Mesh.Cube()

# After the following instruction, mesh wraps the output socket of the Set Shade Smooth node
mesh.set_shade_smooth(True)
```

    
#### Args:
- node (Node): the new node
- socket_name (str): name of the outpout socket in the node. If None, takes the first output socket of the node.
    
Returns:
    self        




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT')
```



## store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT'):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Geometry

#### Returns:
- socket `output`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_instance

```python
def to_instance(*geometry)
```



## to_instance

```python
def to_instance(*geometry):

```
> Node: [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_output

```python
def to_output(self, name=None)
```

 Create a new output socket in the Tree and plug the **DataSocket** to it.

The socket is added to the outputs of the geometry nodes tree.

> Note: To define a data socket as the result geometry of the tree, use the property `output_geometry` of 
  the current [Tree](Tree.md#output_geometry).

The created socket can be read from within another [Tree](Tree.md) by:
    - creating a [Group](Group.md): `node = Group(tree_name, **kwargs)`
    - using the snake_case version of the socket: `ver = node.socket_name`

#### Args:
- name (str): User name of the socket
    
Returns:
    None



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_vertices

```python
def to_vertices(self, points=None, selection=None)
```



## to_vertices

```python
def to_vertices(self, points=None, selection=None):

```
> Node: [Points to Vertices](GeometryNodePointsToVertices.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

#### Args:
- points: Points
- selection: Boolean

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```



## to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- radius: Float
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_volume_amount

```python
def to_volume_amount(self, density=None, voxel_amount=None, radius=None)
```



## to_volume_amount

```python
def to_volume_amount(self, density=None, voxel_amount=None, radius=None):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_amount: Float
- radius: Float

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_volume_size

```python
def to_volume_size(self, density=None, voxel_size=None, radius=None)
```



## to_volume_size

```python
def to_volume_size(self, density=None, voxel_size=None, radius=None):

```
> Node: [Points to Volume](GeometryNodePointsToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- radius: Float

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### transform

```python
def transform(self, translation=None, rotation=None, scale=None)
```



## transform

```python
def transform(self, translation=None, rotation=None, scale=None):

```
> Node: [Transform](GeometryNodeTransform.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

#### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

