# class {class_name}

## ID *property* {#ID}

> def ID(self):

Node [ID](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'ID'

## ID *etter* {#ID}

> def ID(self, attr_value):

Node [Set ID](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: ID


## accumulate_field {#accumulate_field}

> def accumulate_field(self, value=None, group_index=None):

Node [Accumulate Field](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Vector', 'Float', 'Integer']
- group_index: Integer

### Returns:

- tuple ('leading', 'trailing', 'total')

## attribute_max {#attribute_max}

> def attribute_max(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'max'

## attribute_mean {#attribute_mean}

> def attribute_mean(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'mean'

## attribute_median {#attribute_median}

> def attribute_median(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'median'

## attribute_min {#attribute_min}

> def attribute_min(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'min'

## attribute_range {#attribute_range}

> def attribute_range(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'range'

## attribute_statistic {#attribute_statistic}

> def attribute_statistic(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

## attribute_std {#attribute_std}

> def attribute_std(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'standard_deviation'

## attribute_sum {#attribute_sum}

> def attribute_sum(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'sum'

## attribute_var {#attribute_var}

> def attribute_var(self, attribute=None):

Node [Attribute Statistic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'variance'

## capture_attribute {#capture_attribute}

> def capture_attribute(self, value=None):

Node [Capture Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

  socket 'attribute'

## delete {#delete}

> def delete(self, mode='ALL'):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

### Returns:

- node with sockets ['geometry']

## domain_index *property* {#domain_index}

> def domain_index(self):

Node [Index](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'index'

## duplicate {#duplicate}

> def duplicate(self, amount=None):

Node [Duplicate Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- amount: Integer

### Returns:

  socket 'duplicate_index'

## field_at_index {#field_at_index}

> def field_at_index(self, index=None, value=None):

Node [Field at Index](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

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

## position *property* {#position}

> def position(self):

Node [Position](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'position'

## position *etter* {#position}

> def position(self, attr_value):

Node [Set Position](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: position


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

## remove_named_attribute {#remove_named_attribute}

> def remove_named_attribute(self, name=None):

Node [Remove Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String

### Returns:

- node with sockets ['geometry']

## sample_index {#sample_index}

> def sample_index(self, value=None, index=None, clamp=False):

Node [Sample Index](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False

### Returns:

  socket 'value'

## sample_nearest {#sample_nearest}

> def sample_nearest(self, sample_position=None):

Node [Sample Nearest](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- sample_position: Vector

### Returns:

  socket 'index'

## separate {#separate}

> def separate(self, geometry=None):

Node [Separate Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry

### Returns:

- tuple ('selection', 'inverted')

## set_ID {#set_ID}

> def set_ID(self, ID=None):

Node [Set ID](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- ID: Integer

### Returns:

- node with sockets ['geometry']

## set_material_index {#set_material_index}

> def set_material_index(self, material_index=None):

Node [Set Material Index](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- material_index: Integer

### Returns:

- node with sockets ['geometry']

## set_named_boolean {#set_named_boolean}

> def set_named_boolean(self, name=None, value=None):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_color {#set_named_color}

> def set_named_color(self, name=None, value=None):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_float {#set_named_float}

> def set_named_float(self, name=None, value=None):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_integer {#set_named_integer}

> def set_named_integer(self, name=None, value=None):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_vector {#set_named_vector}

> def set_named_vector(self, name=None, value=None):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_position {#set_position}

> def set_position(self, position=None, offset=None):

Node [Set Position](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- position: Vector
- offset: Vector

### Returns:

- node with sockets ['geometry']

## store_named_attribute {#store_named_attribute}

> def store_named_attribute(self, name=None, value=None):

Node [Store Named Attribute](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

