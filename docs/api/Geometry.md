# class {class_name}

## Collection *classmethod* {#Collection}

> def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):

Node [Collection Info](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'geometry'

## ID *property* {#ID}

> def ID(self):

Node [ID](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'ID'

## attribute_statistic {#attribute_statistic}

> def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

## bounding_box *property* {#bounding_box}

> def bounding_box(self):

Node [Bounding Box](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'bounding_box' of class Mesh

## bounding_box_min *property* {#bounding_box_min}

> def bounding_box_min(self):

Node [Bounding Box](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'min'

## bounding_box_min *property* {#bounding_box_min}

> def bounding_box_min(self):

Node [Bounding Box](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'max'

## capture_attribute {#capture_attribute}

> def capture_attribute(self, value=None, domain='POINT'):

Node [Capture Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

  socket 'attribute'

## capture_attribute_node {#capture_attribute_node}

> def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT'):

Node [Capture Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry', 'attribute']

## convex_hull *property* {#convex_hull}

> def convex_hull(self):

Node [Convex Hull](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'convex_hull' of class Mesh

## curve_component *property* {#curve_component}

> def curve_component(self):

Node [Separate Components](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'curve' of class Curve

## delete {#delete}

> def delete(self, selection=None, domain='POINT', mode='ALL'):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

### Returns:

- node with sockets ['geometry']

## domain_size *property* {#domain_size}

> def domain_size(self, component='MESH'):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## duplicate {#duplicate}

> def duplicate(self, selection=None, amount=None, domain='POINT'):

Node [Duplicate Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

### Returns:

  socket 'duplicate_index'

## field_at_index {#field_at_index}

> def field_at_index(self, index=None, value=None, domain='POINT'):

Node [Field at Index](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

  socket 'value'

## get_named_boolean {#get_named_boolean}

> def get_named_boolean(self, name=None):

Node [Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_color {#get_named_color}

> def get_named_color(self, name=None):

Node [Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_float {#get_named_float}

> def get_named_float(self, name=None):

Node [Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_integer {#get_named_integer}

> def get_named_integer(self, name=None):

Node [Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_vector {#get_named_vector}

> def get_named_vector(self, name=None):

Node [Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## index *property* {#index}

> def index(self):

Node [Index](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'index'

## instances_component *property* {#instances_component}

> def instances_component(self):

Node [Separate Components](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'instances' of class Instances

## is_viewport *property* {#is_viewport}

> def is_viewport(self):

Node [Is Viewport](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'is_viewport'

## join {#join}

> def join(*geometry):

Node [Join Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: <m>Geometry

### Returns:

- node with sockets ['geometry']

## material_index *property* {#material_index}

> def material_index(self):

Node [Material Index](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'material_index'

## material_selection {#material_selection}

> def material_selection(self, material=None):

Node [Material Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- material: Material

### Returns:

  socket 'selection'

## merge_by_distance {#merge_by_distance}

> def merge_by_distance(self, selection=None, distance=None, mode='ALL'):

Node [Merge by Distance](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

### Returns:

- node with sockets ['geometry']

## mesh_component *property* {#mesh_component}

> def mesh_component(self):

Node [Separate Components](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'mesh' of class Mesh

## named_attribute {#named_attribute}

> def named_attribute(self, name=None, data_type='FLOAT'):

Node [Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

### Returns:

  socket 'attribute'

## normal *property* {#normal}

> def normal(self):

Node [Normal](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'normal'

## points_component *property* {#points_component}

> def points_component(self):

Node [Separate Components](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'point_cloud' of class Points

## position *property* {#position}

> def position(self):

Node [Position](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'position'

## proximity {#proximity}

> def proximity(self, target=None, source_position=None, target_element='FACES'):

Node [Geometry Proximity](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

### Returns:

  socket 'distance'

## proximity_edges {#proximity_edges}

> def proximity_edges(self, target=None, source_position=None):

Node [Geometry Proximity](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target: Geometry
- source_position: Vector

### Returns:

  socket 'distance'

## proximity_facess {#proximity_facess}

> def proximity_facess(self, target=None, source_position=None):

Node [Geometry Proximity](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target: Geometry
- source_position: Vector

### Returns:

  socket 'distance'

## proximity_points {#proximity_points}

> def proximity_points(self, target=None, source_position=None):

Node [Geometry Proximity](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target: Geometry
- source_position: Vector

### Returns:

  socket 'distance'

## radius *property* {#radius}

> def radius(self):

Node [Radius](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'radius'

## random_boolean {#random_boolean}

> def random_boolean(self, probability=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- probability: Float
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_float {#random_float}

> def random_float(self, min=None, max=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_integer {#random_integer}

> def random_integer(self, min=None, max=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_vector {#random_vector}

> def random_vector(self, min=None, max=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## raycast {#raycast}

> def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):

Node [Raycast](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

### Returns:

- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']

## raycast_interpolated {#raycast_interpolated}

> def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

Node [Raycast](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

### Returns:

- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']

## raycast_nearest {#raycast_nearest}

> def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):

Node [Raycast](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

### Returns:

- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']

## remove_named_attribute {#remove_named_attribute}

> def remove_named_attribute(self, name=None):

Node [Remove Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

- node with sockets ['geometry']

## replace_material {#replace_material}

> def replace_material(self, old=None, new=None):

Node [Replace Material](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- old: Material
- new: Material

### Returns:

- node with sockets ['geometry']

## sample_index {#sample_index}

> def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):

Node [Sample Index](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

  socket 'value'

## sample_nearest {#sample_nearest}

> def sample_nearest(self, sample_position=None, domain='POINT'):

Node [Sample Nearest](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

### Returns:

  socket 'index'

## separate {#separate}

> def separate(self, geometry=None, selection=None, domain='POINT'):

Node [Separate Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- tuple ('selection', 'inverted')

## separate_components *property* {#separate_components}

> def separate_components(self):

Node [Separate Components](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']

## set_ID {#set_ID}

> def set_ID(self, selection=None, ID=None):

Node [Set ID](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- ID: Integer

### Returns:

- node with sockets ['geometry']

## set_material {#set_material}

> def set_material(self, selection=None, material=None):

Node [Set Material](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- material: Material

### Returns:

- node with sockets ['geometry']

## set_material_index {#set_material_index}

> def set_material_index(self, selection=None, material_index=None):

Node [Set Material Index](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- material_index: Integer

### Returns:

- node with sockets ['geometry']

## set_named_boolean {#set_named_boolean}

> def set_named_boolean(self, name=None, value=None, domain='POINT'):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## set_named_color {#set_named_color}

> def set_named_color(self, name=None, value=None, domain='POINT'):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## set_named_float {#set_named_float}

> def set_named_float(self, name=None, value=None, domain='POINT'):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## set_named_integer {#set_named_integer}

> def set_named_integer(self, name=None, value=None, domain='POINT'):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## set_named_vector {#set_named_vector}

> def set_named_vector(self, name=None, value=None, domain='POINT'):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## set_position {#set_position}

> def set_position(self, selection=None, position=None, offset=None):

Node [Set Position](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- position: Vector
- offset: Vector

### Returns:

- node with sockets ['geometry']

## store_named_attribute {#store_named_attribute}

> def store_named_attribute(self, name=None, value=None, domain='POINT'):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## to_instance {#to_instance}

> def to_instance(*geometry):

Node [Geometry to Instance](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: <m>Geometry

### Returns:

  socket 'instances' of class Instances

## transform {#transform}

> def transform(self, translation=None, rotation=None, scale=None):

Node [Transform](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

### Returns:

- node with sockets ['geometry']

## volume_component *property* {#volume_component}

> def volume_component(self):

Node [Separate Components](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'volume' of class Volume

