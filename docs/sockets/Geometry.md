
# Data socket Geometry

> Inherits from dsock.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Static methods

- [is_viewport](#is_viewport) : is_viewport (Boolean)

## Properties

- [bound_box](#bound_box) : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
- [box](#box) : bounding_box (Geometry) = bound_box.bounding_box
- [box_max](#box_max) : max (Vector) = bound_box.max
- [box_min](#box_min) : min (Vector) = bound_box.min
- [components](#components) : Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
- [curve_component](#curve_component) : curve (Curve) = components.curve
- [instances_component](#instances_component) : instances (Instances) = components.instances
- [mesh_component](#mesh_component) : mesh (Mesh) = components.mesh
- [points_component](#points_component) : point_cloud (Geometry) = components.point_cloud
- [volume_component](#volume_component) : volume (Volume) = components.volume

## Methods

- [capture_attribute](#capture_attribute) : attribute (data_type dependant)
- [convex_hull](#convex_hull) : convex_hull (Geometry)
- [delete_geometry](#delete_geometry) : geometry (Geometry)
- [duplicate_elements](#duplicate_elements) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [join](#join) : geometry (Geometry)
- [merge_by_distance](#merge_by_distance) : geometry (Geometry)
- [proximity](#proximity) : Sockets      [position (Vector), distance (Float)]
- [remove_named_attribute](#remove_named_attribute) : geometry (Geometry)
- [replace_material](#replace_material) : geometry (Geometry)
- [scale_elements](#scale_elements) : geometry (Geometry)
- [separate_geometry](#separate_geometry) : Sockets      [selection (Geometry), inverted (Geometry)]
- [set_ID](#set_id) : geometry (Geometry)
- [set_material](#set_material) : geometry (Geometry)
- [set_material_index](#set_material_index) : geometry (Geometry)
- [set_position](#set_position) : geometry (Geometry)
- [set_shade_smooth](#set_shade_smooth) : geometry (Geometry)
- [store_named_attribute](#store_named_attribute) : geometry (Geometry)
- [store_named_boolean](#store_named_boolean) : geometry (Geometry)
- [store_named_byte_color](#store_named_byte_color) : geometry (Geometry)
- [store_named_color](#store_named_color) : geometry (Geometry)
- [store_named_float](#store_named_float) : geometry (Geometry)
- [store_named_integer](#store_named_integer) : geometry (Geometry)
- [store_named_vector](#store_named_vector) : geometry (Geometry)
- [switch](#switch) : output (Geometry)
- [to_instance](#to_instance) : instances (Instances)
- [transform](#transform) : geometry (Geometry)

## is_viewport

Geometry node [*Is Viewport*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Boolean
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.IsViewport`
  
  
  .. blid:: GeometryNodeIsViewport
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.IsViewport(label=node_label, node_color=node_color)
    

## bound_box

Geometry node [*Bounding Box*].



  Returns:
    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.BoundingBox`
  
  
  .. blid:: GeometryNodeBoundBox
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
    

## box

Geometry node [*Bounding Box*].



  Returns:
    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.BoundingBox`
  
  
  .. blid:: GeometryNodeBoundBox
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box")
    

## box_min

Geometry node [*Bounding Box*].



  Returns:
    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.BoundingBox`
  
  
  .. blid:: GeometryNodeBoundBox
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_min")
    

## box_max

Geometry node [*Bounding Box*].



  Returns:
    Sockets [bounding_box (Geometry), min (Vector), max (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.BoundingBox`
  
  
  .. blid:: GeometryNodeBoundBox
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_max")
    

## components

Geometry node [*Separate Components*].



  Returns:
    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateComponents`
  
  
  .. blid:: GeometryNodeSeparateComponents
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
    

## mesh_component

Geometry node [*Separate Components*].



  Returns:
    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateComponents`
  
  
  .. blid:: GeometryNodeSeparateComponents
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.mesh_component")
    

## points_component

Geometry node [*Separate Components*].



  Returns:
    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateComponents`
  
  
  .. blid:: GeometryNodeSeparateComponents
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.points_component")
    

## curve_component

Geometry node [*Separate Components*].



  Returns:
    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateComponents`
  
  
  .. blid:: GeometryNodeSeparateComponents
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.curve_component")
    

## volume_component

Geometry node [*Separate Components*].



  Returns:
    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateComponents`
  
  
  .. blid:: GeometryNodeSeparateComponents
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.volume_component")
    

## instances_component

Geometry node [*Separate Components*].



  Returns:
    Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateComponents`
  
  
  .. blid:: GeometryNodeSeparateComponents
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.instances_component")
    

## switch

Geometry node [*Switch*].


  Args:
    switch: Boolean
    true: Geometry
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Switch`
  
  - input_type = 'GEOMETRY'
    
  .. blid:: GeometryNodeSwitch
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Switch(false=self, switch=switch, true=true, input_type='GEOMETRY', label=node_label, node_color=node_color)
    

## capture_attribute

Geometry node [*Capture Attribute*].


  Args:
    value: Float
    data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), attribute (data_type dependant)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
  
  
  .. blid:: GeometryNodeCaptureAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
    

## duplicate_elements

Geometry node [*Duplicate Elements*].


  Args:
    selection: Boolean
    amount: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), duplicate_index (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DuplicateElements`
  
  
  .. blid:: GeometryNodeDuplicateElements
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain=domain, label=node_label, node_color=node_color)
    

## delete_geometry

Geometry node [*Delete Geometry*].


  Args:
    selection: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
    mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DeleteGeometry`
  
  
  .. blid:: GeometryNodeDeleteGeometry
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode, label=node_label, node_color=node_color)
    

## merge_by_distance

Geometry node [*Merge by Distance*].


  Args:
    selection: Boolean
    distance: Float
    mode (str): 'ALL' in [ALL, CONNECTED]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MergeByDistance`
  
  
  .. blid:: GeometryNodeMergeByDistance
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode, label=node_label, node_color=node_color)
    

## replace_material

Geometry node [*Replace Material*].


  Args:
    old: Material
    new: Material
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ReplaceMaterial`
  
  
  .. blid:: GeometryNodeReplaceMaterial
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ReplaceMaterial(geometry=self, old=old, new=new, label=node_label, node_color=node_color)
    

## scale_elements

Geometry node [*Scale Elements*].


  Args:
    selection: Boolean
    scale: Float
    center: Vector
    axis: Vector
    domain (str): 'FACE' in [FACE, EDGE]
    scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ScaleElements`
  
  
  .. blid:: GeometryNodeScaleElements
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode, label=node_label, node_color=node_color)
    

## set_ID

Geometry node [*Set ID*].


  Args:
    selection: Boolean
    ID: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetID`
  
  
  .. blid:: GeometryNodeSetID
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetID(geometry=self, selection=selection, ID=ID, label=node_label, node_color=node_color)
    

## set_material

Geometry node [*Set Material*].


  Args:
    selection: Boolean
    material: Material
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetMaterial`
  
  
  .. blid:: GeometryNodeSetMaterial
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetMaterial(geometry=self, selection=selection, material=material, label=node_label, node_color=node_color)
    

## set_material_index

Geometry node [*Set Material Index*].


  Args:
    selection: Boolean
    material_index: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetMaterialIndex`
  
  
  .. blid:: GeometryNodeSetMaterialIndex
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index, label=node_label, node_color=node_color)
    

## set_position

Geometry node [*Set Position*].


  Args:
    selection: Boolean
    position: Vector
    offset: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetPosition`
  
  
  .. blid:: GeometryNodeSetPosition
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset, label=node_label, node_color=node_color)
    

## set_shade_smooth

Geometry node [*Set Shade Smooth*].


  Args:
    selection: Boolean
    shade_smooth: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetShadeSmooth`
  
  
  .. blid:: GeometryNodeSetShadeSmooth
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth, label=node_label, node_color=node_color)
    

## transform

Geometry node [*Transform*].


  Args:
    translation: Vector
    rotation: Vector
    scale: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Transform`
  
  
  .. blid:: GeometryNodeTransform
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
    

## store_named_attribute

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Float
    data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BYTE_COLOR, BOOLEAN]
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
    

## store_named_float

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Float
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  - data_type = 'FLOAT'
    
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
    

## store_named_integer

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Integer
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  - data_type = 'INT'
    
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
    

## store_named_vector

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Vector
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  - data_type = 'FLOAT_VECTOR'
    
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
    

## store_named_color

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Color
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  - data_type = 'FLOAT_COLOR'
    
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
    

## store_named_byte_color

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Color
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  - data_type = 'BYTE_COLOR'
    
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BYTE_COLOR', domain=domain, label=node_label, node_color=node_color)
    

## store_named_boolean

Geometry node [*Store Named Attribute*].


  Args:
    name: String
    value: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.StoreNamedAttribute`
  
  - data_type = 'BOOLEAN'
    
  .. blid:: GeometryNodeStoreNamedAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
    

## remove_named_attribute

Geometry node [*Remove Named Attribute*].


  Args:
    name: String
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.RemoveNamedAttribute`
  
  
  .. blid:: GeometryNodeRemoveAttribute
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.RemoveNamedAttribute(geometry=self, name=name, label=node_label, node_color=node_color)
    

## separate_geometry

Geometry node [*Separate Geometry*].


  Args:
    selection: Boolean
    domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [selection (Geometry), inverted (Geometry)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SeparateGeometry`
  
  
  .. blid:: GeometryNodeSeparateGeometry
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain, label=node_label, node_color=node_color)
    

## convex_hull

Geometry node [*Convex Hull*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ConvexHull`
  
  
  .. blid:: GeometryNodeConvexHull
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ConvexHull(geometry=self, label=node_label, node_color=node_color)
    

## to_instance

Geometry node [*Geometry to Instance*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Instances
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.GeometryToInstance`
  
  
  .. blid:: GeometryNodeGeometryToInstance
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.GeometryToInstance(self, *geometry, label=node_label, node_color=node_color)
    

## join

Geometry node [*Join Geometry*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.JoinGeometry`
  
  
  .. blid:: GeometryNodeJoinGeometry
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.JoinGeometry(self, *geometry, label=node_label, node_color=node_color)
    

## proximity

Geometry node [*Geometry Proximity*].


  Args:
    source_position: Vector
    target_element (str): 'FACES' in [POINTS, EDGES, FACES]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [position (Vector), distance (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.GeometryProximity`
  
  
  .. blid:: GeometryNodeProximity
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element, label=node_label, node_color=node_color)
    
