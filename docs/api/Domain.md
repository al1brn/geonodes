# class Domain

## title

- [(gen.fname(wnode)](ID-property)
- [(gen.fname(wnode)](domain_index-property)
- [(gen.fname(wnode)](index-property)
- [(gen.fname(wnode)](material_index-property)
- [(gen.fname(wnode)](normal-property)
- [(gen.fname(wnode)](position-property)

## title


## title


## title

- [(gen.fname(wnode)](accumulate_field)
- [(gen.fname(wnode)](attribute_max)
- [(gen.fname(wnode)](attribute_mean)
- [(gen.fname(wnode)](attribute_median)
- [(gen.fname(wnode)](attribute_min)
- [(gen.fname(wnode)](attribute_range)
- [(gen.fname(wnode)](attribute_statistic)
- [(gen.fname(wnode)](attribute_std)
- [(gen.fname(wnode)](attribute_sum)
- [(gen.fname(wnode)](attribute_var)
- [(gen.fname(wnode)](capture_attribute)
- [(gen.fname(wnode)](delete)
- [(gen.fname(wnode)](duplicate)
- [(gen.fname(wnode)](field_at_index)
- [(gen.fname(wnode)](get_named_boolean)
- [(gen.fname(wnode)](get_named_color)
- [(gen.fname(wnode)](get_named_float)
- [(gen.fname(wnode)](get_named_integer)
- [(gen.fname(wnode)](get_named_vector)
- [(gen.fname(wnode)](material_selection)
- [(gen.fname(wnode)](named_attribute)
- [(gen.fname(wnode)](random_boolean)
- [(gen.fname(wnode)](random_float)
- [(gen.fname(wnode)](random_integer)
- [(gen.fname(wnode)](random_vector)
- [(gen.fname(wnode)](remove_named_attribute)
- [(gen.fname(wnode)](sample_index)
- [(gen.fname(wnode)](sample_nearest)
- [(gen.fname(wnode)](separate)
- [(gen.fname(wnode)](set_ID)
- [(gen.fname(wnode)](set_material_index)
- [(gen.fname(wnode)](set_named_boolean)
- [(gen.fname(wnode)](set_named_color)
- [(gen.fname(wnode)](set_named_float)
- [(gen.fname(wnode)](set_named_integer)
- [(gen.fname(wnode)](set_named_vector)
- [(gen.fname(wnode)](set_position)
- [(gen.fname(wnode)](store_named_attribute)

## ID *property*

{#ID}

> def ID(self):

Node [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html) )

### Returns:

  socket 'ID'

## ID *etter*

{#ID}

> def ID(self, attr_value):

Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html) )

Node implemented as property setter.

        ###Args:- attr_value: ID


## accumulate_field

{#accumulate_field}

> def accumulate_field(self, value=None, group_index=None):

Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html) )

        ### Args:
- value: ['Vector', 'Float', 'Integer']
- group_index: Integer

### Returns:

- tuple ('leading', 'trailing', 'total')

## attribute_max

{#attribute_max}

> def attribute_max(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'max'

## attribute_mean

{#attribute_mean}

> def attribute_mean(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'mean'

## attribute_median

{#attribute_median}

> def attribute_median(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'median'

## attribute_min

{#attribute_min}

> def attribute_min(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'min'

## attribute_range

{#attribute_range}

> def attribute_range(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'range'

## attribute_statistic

{#attribute_statistic}

> def attribute_statistic(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

## attribute_std

{#attribute_std}

> def attribute_std(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'standard_deviation'

## attribute_sum

{#attribute_sum}

> def attribute_sum(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'sum'

## attribute_var

{#attribute_var}

> def attribute_var(self, attribute=None):

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

        ### Args:
- attribute: ['Float', 'Vector']

### Returns:

  socket 'variance'

## capture_attribute

{#capture_attribute}

> def capture_attribute(self, value=None):

Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html) )

        ### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

  socket 'attribute'

## delete

{#delete}

> def delete(self, mode='ALL'):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

        ### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

### Returns:

- node with sockets ['geometry']

## domain_index *property*

{#domain_index}

> def domain_index(self):

Node [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html) )

### Returns:

  socket 'index'

## duplicate

{#duplicate}

> def duplicate(self, amount=None):

Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html) )

        ### Args:
- amount: Integer

### Returns:

  socket 'duplicate_index'

## field_at_index

{#field_at_index}

> def field_at_index(self, index=None, value=None):

Node [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html) )

        ### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

### Returns:

  socket 'value'

## get_named_boolean

{#get_named_boolean}

> def get_named_boolean(self, name=None):

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_color

{#get_named_color}

> def get_named_color(self, name=None):

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_float

{#get_named_float}

> def get_named_float(self, name=None):

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_integer

{#get_named_integer}

> def get_named_integer(self, name=None):

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## get_named_vector

{#get_named_vector}

> def get_named_vector(self, name=None):

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

        ### Args:
- name: String

### Returns:

  socket 'attribute'

## index *property*

{#index}

> def index(self):

Node [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html) )

### Returns:

  socket 'index'

## material_index *property*

{#material_index}

> def material_index(self):

Node [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html) )

### Returns:

  socket 'material_index'

## material_selection

{#material_selection}

> def material_selection(self, material=None):

Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html) )

        ### Args:
- material: Material

### Returns:

  socket 'selection'

## named_attribute

{#named_attribute}

> def named_attribute(self, name=None, data_type='FLOAT'):

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

        ### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

### Returns:

  socket 'attribute'

## normal *property*

{#normal}

> def normal(self):

Node [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html) )

### Returns:

  socket 'normal'

## position *property*

{#position}

> def position(self):

Node [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html) )

### Returns:

  socket 'position'

## position *etter*

{#position}

> def position(self, attr_value):

Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html) )

Node implemented as property setter.

        ###Args:- attr_value: position


## random_boolean

{#random_boolean}

> def random_boolean(self, probability=None, ID=None, seed=None):

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

        ### Args:
- probability: Float
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_float

{#random_float}

> def random_float(self, min=None, max=None, ID=None, seed=None):

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

        ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_integer

{#random_integer}

> def random_integer(self, min=None, max=None, ID=None, seed=None):

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

        ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_vector

{#random_vector}

> def random_vector(self, min=None, max=None, ID=None, seed=None):

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

        ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## remove_named_attribute

{#remove_named_attribute}

> def remove_named_attribute(self, name=None):

Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html) )

        ### Args:
- name: String

### Returns:

- node with sockets ['geometry']

## sample_index

{#sample_index}

> def sample_index(self, value=None, index=None, clamp=False):

Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False

### Returns:

  socket 'value'

## sample_nearest

{#sample_nearest}

> def sample_nearest(self, sample_position=None):

Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html) )

        ### Args:
- sample_position: Vector

### Returns:

  socket 'index'

## separate

{#separate}

> def separate(self, geometry=None):

Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html) )

        ### Args:
- geometry: Geometry

### Returns:

- tuple ('selection', 'inverted')

## set_ID

{#set_ID}

> def set_ID(self, ID=None):

Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html) )

        ### Args:
- ID: Integer

### Returns:

- node with sockets ['geometry']

## set_material_index

{#set_material_index}

> def set_material_index(self, material_index=None):

Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html) )

        ### Args:
- material_index: Integer

### Returns:

- node with sockets ['geometry']

## set_named_boolean

{#set_named_boolean}

> def set_named_boolean(self, name=None, value=None):

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_color

{#set_named_color}

> def set_named_color(self, name=None, value=None):

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_float

{#set_named_float}

> def set_named_float(self, name=None, value=None):

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_integer

{#set_named_integer}

> def set_named_integer(self, name=None, value=None):

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_named_vector

{#set_named_vector}

> def set_named_vector(self, name=None, value=None):

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

## set_position

{#set_position}

> def set_position(self, position=None, offset=None):

Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html) )

        ### Args:
- position: Vector
- offset: Vector

### Returns:

- node with sockets ['geometry']

## store_named_attribute

{#store_named_attribute}

> def store_named_attribute(self, name=None, value=None):

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

        ### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

### Returns:

- node with sockets ['geometry']

