Class Points

## Properties

### ID

 Node ID.

Node reference [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)
Developer reference [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

Returns:
    socket `ID`



### bl_idname

 Shortcut for `self.bsocket.bl_idname`



### bnode

 Shortcut for `self.bsocket.node`



### bounding_box

 Node BoundingBox.

Node reference [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html)
Developer reference [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

Returns:
    socket `bounding_box` [Mesh](Mesh.md)



### bounding_box_min

 Node BoundingBox.

Node reference [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html)
Developer reference [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

Returns:
    socket `max`



### convex_hull

 Node ConvexHull.

Node reference [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html)
Developer reference [GeometryNodeConvexHull](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

Returns:
    socket `convex_hull` [Mesh](Mesh.md)



### curve_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

Returns:
    socket `curve` [Curve](Curve.md)



### domain_size

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

Returns:
    socket `point_count`



### index

 Node Index.

Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

Returns:
    socket `index`



### instances_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

Returns:
    socket `instances` [Instances](Instances.md)



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`



### is_output

 Shortcut for `self.bsocket.is_output`



### is_viewport

 Node IsViewport.

Node reference [Is Viewport](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html)
Developer reference [GeometryNodeIsViewport](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)

Returns:
    socket `is_viewport`



### links

 Shortcut for `self.bsocket.links`



### material_index

 Node MaterialIndex.

Node reference [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
Developer reference [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

Returns:
    socket `material_index`



### mesh_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

Returns:
    socket `mesh` [Mesh](Mesh.md)



### name

 Shortcut for `self.bsocket.name`



### node_chain_label

 Shortcut for *self.node.chain_label*



### normal

 Node Normal.

Node reference [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
Developer reference [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

Returns:
    socket `normal`



### points_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

Returns:
    socket `point_cloud` [Points](Points.md)



### position

 Node Position.

Node reference [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
Developer reference [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

Returns:
    socket `position`



### radius

 Node Radius.

Node reference [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
Developer reference [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

Returns:
    socket `radius`



### separate_components

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

Returns:
    node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']



### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.




### volume_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

Returns:
    socket `volume` [Volume](Volume.md)



## Class and static methods

### Collection

```python
@classmethod
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```

 Node CollectionInfo.

Node reference [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html)
Developer reference [GeometryNodeCollectionInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

Args:
    collection: Collection
    separate_children: Boolean
    reset_children: Boolean
    transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

Returns:
    socket `geometry`



### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection

.. blid:: GeometryNodeCollectionInfo



### Input

```python
@classmethod
def Input(cls, name = None, description = "")
```

 Create a Geometry input socket in the Group Input Node

Args:
    name: The socket name
    description: User tip
    
Returns:
    Geometry: The Geometry data socket
    
Note
----
    This method create a new input socket in the Group Input node. To get the **default** input geometry,
    use :attr:`Tree.input_geometry`.
    



### Points

```python
@classmethod
def Points(cls, count=None, position=None, radius=None)
```

 Node Points.

Node reference [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)
Developer reference [GeometryNodePoints](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)

Args:
    count: Integer
    position: Vector
    radius: Float

Returns:
    socket `geometry`



### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

:param class_name: The class name
:type class_name: str
:return: The bl_idname associated to this class name
:rtype: str

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to *sub classes*:
    
.. list-table:: 
   :widths: 20 40
   :header-rows: 0

   * - Unsigned
     - Integer sub class (NodeSocketIntUnsigned)
   * - Factor
     - Float sub class (NodeSocketFloatFactor)
   * - Angle
     - Float sub class  (NodeSocketFloatAngle)
   * - Distance
     - Float sub class (NodeSocketFloatDistance)
   * - Rotation
     - Vector sub class (NodeSocketVectorEuler)
   * - xyz
     - Vector sub class (NodeSocketVectorXYZ)
   * - Translation
     - Vector sub class (NodeSocketVectorTranslation)
  
These additional values allow to enter angle, distance, factor... as group input values.




### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

:param socket: The socket to determine the class of
:param with_sub_class: Return the sub class if True
:typ socket: bpy.types.NodeSocket, Socket
:type with_sub_class: bool
:return: The name of the class associated to the bl_idname of the socket
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20 20
   :header-rows: 1
   
   * - NodeSocket
     - class name
     - sub class name
   * - NodeSocketBool 
     - 'Boolean'
     - 
   * - NodeSocketInt 
     - 'Integer'
     - 
   * - NodeSocketIntUnsigned 
     - 'Integer'
     - 'Unsigned'
   * - NodeSocketFloat 
     - 'Float' 
     - 
   * - NodeSocketFloatFactor 
     - 'Float'
     - 'Factor'
   * - NodeSocketFloatAngle  
     - 'Float'
     - 'Angle'
   * - NodeSocketFloatDistance 
     - 'Float'
     - 'Distance'
   * - NodeSocketVector 
     - 'Vector'
     - 
   * - NodeSocketVectorEuler 
     - 'Vector'
     - 'Rotation'
   * - NodeSocketVectorXYZ 
     - 'Vector'
     - 'xyz'
   * - NodeSocketVectorTranslation 
     - 'Vector'
     - 'Translation'
   * - NodeSocketColor 
     - 'Color'
     - 
   * - NodeSocketString' 
     - 'String'
     - 
   * - NodeSocketCollection 
     - 'Collection'
     - 
   * - NodeSocketImage 
     - 'Image'
     - 
   * - NodeSocketMaterial 
     - 'Material'
     - 
   * - NodeSocketObject 
     - 'Object'
     - 
   * - NodeSocketTexture 
     - 'Texture'
     - 
   * - NodeSocketGeometry
     - 'Geometry'
     - 
  
  
If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.



### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

:param value: The value to test
:type value: any
:return: True if *value* is or wraps a socket
:rtype: bool

Returns True if value is:
    
- A Blender Geometry Node Socket
- An instance of Socket        




### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool



### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool




### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

 Returns the domain to which the socket belongs

:param value: The socket
:type value: any
:return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20
   :header-rows: 1

   * - Socket bl_idname
     - Domain code
   * - NodeSocketBool
     - 'BOOLEAN'
   * - NodeSocketInt               
     - 'INT'
   * - NodeSocketIntUnsigned       
     - 'INT'
   * - NodeSocketFloat            
     - 'FLOAT'
   * - NodeSocketFloatFactor       
     - 'FLOAT'
   * - NodeSocketFloatAngle        
     - 'FLOAT'
   * - NodeSocketFloatDistance     
     - 'FLOAT'         
   * - NodeSocketVector            
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorEuler       
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorXYZ         
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorTranslation
     - 'FLOAT_VECTOR'
   * - NodeSocketColor      
     - 'FLOAT_COLOR'
   * - NodeSocketString           
     - 'FLOAT_COLOR'





## Methods

### attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT')
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

Args:
    selection: Boolean
    attribute: ['Float', 'Vector']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']



### capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT')
```

 Node CaptureAttribute.

Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

Args:
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    socket `attribute`



### capture_attribute_node

```python
def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT')
```

 Node CaptureAttribute.

Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

Args:
    geometry: Geometry
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry', 'attribute']



### connected_sockets

```python
def connected_sockets(self)
```

 Returns the list of Socket instances linked to this socket.




### delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

Args:
    selection: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
    mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

Returns:
    node with sockets ['geometry']



### duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT')
```

 Node DuplicateElements.

Node reference [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
Developer reference [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

Args:
    selection: Boolean
    amount: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

Returns:
    socket `duplicate_index`



### field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT')
```

 Node FieldAtIndex.

Node reference [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
Developer reference [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

Args:
    index: Integer
    value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    socket `value`



### get_blender_socket

```python
def get_blender_socket(self)
```

 Returns the property bsocket.

:return: self.bsocket
:rtype: bpy.types.NodeSocket




### get_named_boolean

```python
def get_named_boolean(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

Args:
    name: String

Returns:
    socket `attribute`



### get_named_color

```python
def get_named_color(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

Args:
    name: String

Returns:
    socket `attribute`



### get_named_float

```python
def get_named_float(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

Args:
    name: String

Returns:
    socket `attribute`



### get_named_integer

```python
def get_named_integer(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

Args:
    name: String

Returns:
    socket `attribute`



### get_named_vector

```python
def get_named_vector(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

Args:
    name: String

Returns:
    socket `attribute`



### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



### instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

 Node InstanceOnPoints.

Node reference [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
Developer reference [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

Args:
    selection: Boolean
    instance: Geometry
    pick_instance: Boolean
    instance_index: Integer
    rotation: Vector
    scale: Vector

Returns:
    socket `instances`



### instantiate

```python
def instantiate(self, count = 1, realize = False)
```

 Instantiate the geometry

Args:
    count: Number of instances to create
    realize: True to realize the instances
    
Returns:
    Instances or Geometry
    
The duplication is performed by instantiating the geometry along the vertices
of a Mesh Line initialized with `count` points.

The operator ``*`` can be used to operate this method with `realize = False`:
    
.. code-block::
    
    curves = curve * 10
    
    # is equivalent to
    
    curves = curve.duplicate(10, realize=False)
    




### interpolate_domain

```python
def interpolate_domain(self, value=None, domain='POINT')
```

 Node InterpolateDomain.

Node reference [Interpolate Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html)
Developer reference [GeometryNodeFieldOnDomain](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

Args:
    value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    socket `value`



### join

```python
def join(*geometry)
```

 Node JoinGeometry.

Node reference [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)
Developer reference [GeometryNodeJoinGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

Args:
    geometry: <m>Geometry

Returns:
    node with sockets ['geometry']



### material_selection

```python
def material_selection(self, material=None)
```

 Node MaterialSelection.

Node reference [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
Developer reference [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

Args:
    material: Material

Returns:
    socket `selection`



### merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL')
```

 Node MergeByDistance.

Node reference [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)
Developer reference [GeometryNodeMergeByDistance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

Args:
    selection: Boolean
    distance: Float
    mode (str): 'ALL' in [ALL, CONNECTED]

Returns:
    node with sockets ['geometry']



### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

Args:
    name: String
    data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

Returns:
    socket `attribute`



### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

:param values: The output sockets. More than one values can be passed
    if the input socket is multi input.
:type values: array of bpy.types.NodeSocket, Socket, values

see :func:`plug_bsocket`



### proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES')
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

Args:
    target: Geometry
    source_position: Vector
    target_element (str): 'FACES' in [POINTS, EDGES, FACES]

Returns:
    socket `distance`



### proximity_edges

```python
def proximity_edges(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

Args:
    target: Geometry
    source_position: Vector

Returns:
    socket `distance`



### proximity_faces

```python
def proximity_faces(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

Args:
    target: Geometry
    source_position: Vector

Returns:
    socket `distance`



### proximity_points

```python
def proximity_points(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

Args:
    target: Geometry
    source_position: Vector

Returns:
    socket `distance`



### random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

Args:
    probability: Float
    ID: Integer
    seed: Integer

Returns:
    socket `value`



### random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

Args:
    min: ['Vector', 'Float', 'Integer']
    max: ['Vector', 'Float', 'Integer']
    ID: Integer
    seed: Integer

Returns:
    socket `value`



### random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

Args:
    min: ['Vector', 'Float', 'Integer']
    max: ['Vector', 'Float', 'Integer']
    ID: Integer
    seed: Integer

Returns:
    socket `value`



### random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

Args:
    min: ['Vector', 'Float', 'Integer']
    max: ['Vector', 'Float', 'Integer']
    ID: Integer
    seed: Integer

Returns:
    socket `value`



### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```

 Node Raycast.

Node reference [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
Developer reference [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

Args:
    target_geometry: Geometry
    attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    source_position: Vector
    ray_direction: Vector
    ray_length: Float
    mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

Returns:
    node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']



### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```

 Node Raycast.

Node reference [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
Developer reference [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

Args:
    target_geometry: Geometry
    attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    source_position: Vector
    ray_direction: Vector
    ray_length: Float

Returns:
    node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']



### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```

 Node Raycast.

Node reference [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
Developer reference [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

Args:
    target_geometry: Geometry
    attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    source_position: Vector
    ray_direction: Vector
    ray_length: Float

Returns:
    node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']



### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```

 Node RemoveNamedAttribute.

Node reference [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
Developer reference [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

Args:
    name: String

Returns:
    node with sockets ['geometry']



### replace_material

```python
def replace_material(self, old=None, new=None)
```

 Node ReplaceMaterial.

Node reference [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)
Developer reference [GeometryNodeReplaceMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

Args:
    old: Material
    new: Material

Returns:
    node with sockets ['geometry']



### reroute

```python
def reroute(self)
```

 Reroute all output links



### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.

:example:

.. code-block:: python

    class Vector(...):
        def __init__(self, ...):
             ...
             self.reset_properties()
             ...
    
         def reset_properties(self):
             super().reset_properties()
             self.separate_ = None      # Created by property self.seperate() with node SeparateXyz






### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT')
```

 Node SampleIndex.

Node reference [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
Developer reference [GeometryNodeSampleIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

Args:
    value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
    index: Integer
    clamp (bool): False
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    socket `value`



### sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT')
```

 Node SampleNearest.

Node reference [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)
Developer reference [GeometryNodeSampleNearest](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

Args:
    sample_position: Vector
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

Returns:
    socket `index`



### separate

```python
def separate(self, geometry=None, selection=None, domain='POINT')
```

 Node SeparateGeometry.

Node reference [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
Developer reference [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

Args:
    geometry: Geometry
    selection: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

Returns:
    tuple ('selection', 'inverted')



### set_ID

```python
def set_ID(self, selection=None, ID=None)
```

 Node SetID.

Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

Args:
    selection: Boolean
    ID: Integer

Returns:
    node with sockets ['geometry']



### set_material

```python
def set_material(self, selection=None, material=None)
```

 Node SetMaterial.

Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

Args:
    selection: Boolean
    material: Material

Returns:
    node with sockets ['geometry']



### set_material_index

```python
def set_material_index(self, selection=None, material_index=None)
```

 Node SetMaterialIndex.

Node reference [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
Developer reference [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

Args:
    selection: Boolean
    material_index: Integer

Returns:
    node with sockets ['geometry']



### set_named_boolean

```python
def set_named_boolean(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

Args:
    name: String
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry']



### set_named_color

```python
def set_named_color(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

Args:
    name: String
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry']



### set_named_float

```python
def set_named_float(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

Args:
    name: String
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry']



### set_named_integer

```python
def set_named_integer(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

Args:
    name: String
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry']



### set_named_vector

```python
def set_named_vector(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

Args:
    name: String
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry']



### set_point_radius

```python
def set_point_radius(self, selection=None, radius=None)
```

 Node SetPointRadius.

Node reference [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)
Developer reference [GeometryNodeSetPointRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

Args:
    selection: Boolean
    radius: Float

Returns:
    node with sockets ['points']



### set_position

```python
def set_position(self, selection=None, position=None, offset=None)
```

 Node SetPosition.

Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Args:
    selection: Boolean
    position: Vector
    offset: Vector

Returns:
    node with sockets ['geometry']



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
    




### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

:param node: The new node owning the output socket to wrap
:type node: Node
:return: self

Methods are implemented in two modes:

- Creation
- Transformation

In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.

In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
After the method returns, the calling DataSocket instance refers to a new Blender output socket.
The stack method changes the socket the instance refers to and reinitialize properties

.. code-block:: python

    # 1. Creation mode
    # 
    # to_mesh method creates a new mesh from a curve.
    # The curve instance refers to the same output node socket
    # We need to get the result of the method in a new variable
    
    new_mesh = curve.to_mesh(profile_curve=circle)
    
    # 2. Transformation mode
    #
    # set_shade_smooth method transforms the mesh.
    # After the call, the mesh instance refers to the output socket of the
    # newly created node "Set Shade Smooth". There is no need to get the result
    # of the method.
    
    mesh.set_shade_smooth()
    
    # Note that a transformation method returns self and so, the following line
    # is equivallent:
    
    mesh = mesh.set_shade_smooth()





### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

Args:
    name: String
    value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

Returns:
    node with sockets ['geometry']



### switch

```python
def switch(self, switch=None, true=None)
```

 Node Switch.

Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

Args:
    switch: Boolean
    true: Geometry

Returns:
    socket `output`



### to_instance

```python
def to_instance(*geometry)
```

 Node GeometryToInstance.

Node reference [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
Developer reference [GeometryNodeGeometryToInstance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

Args:
    geometry: <m>Geometry

Returns:
    socket `instances` [Instances](Instances.md)



### to_output

```python
def to_output(self, name=None)
```

 Plug the data socket to the group output

:param name: The name to give to the modifier output
:type name: str

The socket is added to the outputs of the geometry nodes tree.

.. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.




### to_vertices

```python
def to_vertices(self, points=None, selection=None)
```

 Node PointsToVertices.

Node reference [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)
Developer reference [GeometryNodePointsToVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

Args:
    points: Points
    selection: Boolean

Returns:
    socket `mesh` [Mesh](Mesh.md)



### to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

 Node PointsToVolume.

Node reference [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)
Developer reference [GeometryNodePointsToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

Args:
    density: Float
    voxel_size: Float
    voxel_amount: Float
    radius: Float
    resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

Returns:
    socket `volume` [Volume](Volume.md)



### to_volume_amount

```python
def to_volume_amount(self, density=None, voxel_amount=None, radius=None)
```

 Node PointsToVolume.

Node reference [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)
Developer reference [GeometryNodePointsToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

Args:
    density: Float
    voxel_amount: Float
    radius: Float

Returns:
    socket `volume` [Volume](Volume.md)



### to_volume_size

```python
def to_volume_size(self, density=None, voxel_size=None, radius=None)
```

 Node PointsToVolume.

Node reference [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)
Developer reference [GeometryNodePointsToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

Args:
    density: Float
    voxel_size: Float
    radius: Float

Returns:
    socket `volume` [Volume](Volume.md)



### transform

```python
def transform(self, translation=None, rotation=None, scale=None)
```

 Node Transform.

Node reference [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html)
Developer reference [GeometryNodeTransform](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

Args:
    translation: Vector
    rotation: Vector
    scale: Vector

Returns:
    node with sockets ['geometry']



### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

 Link the data socket to the viewer

If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.

If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
accordingly.



