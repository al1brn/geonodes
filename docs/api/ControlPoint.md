# class {class_name}

## curve {#curve}

> def curve(self):

Node [Curve of Point](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- tuple ('curve_index', 'index_in_curve')

## domain_size {#domain_size}

> def __len__(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## endpoint_selection {#endpoint_selection}

> def endpoint_selection(self, start_size=None, end_size=None):

Node [Endpoint Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start_size: Integer
- end_size: Integer

### Returns:

  socket 'selection'

## handle_positions {#handle_positions}

> def handle_positions(self, relative=None):

Node [Curve Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- relative: Boolean

### Returns:

- node with sockets ['left', 'right']

## handle_type_selection {#handle_type_selection}

> def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):

Node [Handle Type Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['selection']

## handle_type_selection {#handle_type_selection}

> def handle_type_selection_free(self, left=True, right=True):

Node [Handle Type Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['selection']

## handle_type_selection {#handle_type_selection}

> def handle_type_selection_auto(self, left=True, right=True):

Node [Handle Type Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['selection']

## handle_type_selection {#handle_type_selection}

> def handle_type_selection_vector(self, left=True, right=True):

Node [Handle Type Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['selection']

## handle_type_selection {#handle_type_selection}

> def handle_type_selection_align(self, left=True, right=True):

Node [Handle Type Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['selection']

## handle_type_selection_node {#handle_type_selection_node}

> def handle_type_selection_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

Node [Handle Type Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

  socket 'selection'

## instance_on_points {#instance_on_points}

> def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances' of class Instances

## left_handle_positions *property* {#left_handle_positions}

> def left_handle_positions(self):

Node [Curve Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'left'

## left_handle_positions *etter* {#left_handle_positions}

> def left_handle_positions(self, attr_value):

Node [Set Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: position


## offset {#offset}

> def offset(self, offset=None):

Node [Offset Point in Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- offset: Integer

### Returns:

- tuple ('is_valid_offset', 'point_index')

## parameter *property* {#parameter}

> def parameter(self):

Node [Spline Parameter](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- tuple ('factor', 'length', 'index')

## parameter_factor *property* {#parameter_factor}

> def parameter_factor(self):

Node [Spline Parameter](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'factor'

## parameter_index *property* {#parameter_index}

> def parameter_index(self):

Node [Spline Parameter](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'index'

## parameter_length *property* {#parameter_length}

> def parameter_length(self):

Node [Spline Parameter](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'length'

## radius *property* {#radius}

> def radius(self):

Node [Radius](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'radius'

## radius *etter* {#radius}

> def radius(self, attr_value):

Node [Set Curve Radius](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: radius


## right_handle_positions *property* {#right_handle_positions}

> def right_handle_positions(self):

Node [Curve Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'right'

## right_handle_positions *etter* {#right_handle_positions}

> def right_handle_positions(self, attr_value):

Node [Set Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: position


## set_handle_positions {#set_handle_positions}

> def set_handle_positions(self, position=None, offset=None, mode='LEFT'):

Node [Set Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- position: Vector
- offset: Vector
- mode (str): 'LEFT' in [LEFT, RIGHT]

### Returns:

- node with sockets ['curve']

## set_handle_positions_left {#set_handle_positions_left}

> def set_handle_positions_left(self, curve=None, position=None, offset=None):

Node [Set Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve: Curve
- position: Vector
- offset: Vector

### Returns:

- node with sockets ['curve']

## set_handle_positions_right {#set_handle_positions_right}

> def set_handle_positions_right(self, curve=None, position=None, offset=None):

Node [Set Handle Positions](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve: Curve
- position: Vector
- offset: Vector

### Returns:

- node with sockets ['curve']

## set_handle_type {#set_handle_type}

> def set_handle_type(self, left=True, right=True, handle_type='AUTO'):

Node [Set Handle Type](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve: Curve
- selection: Boolean
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['curve']

## set_handle_type_node {#set_handle_type_node}

> def set_handle_type_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

Node [Set Handle Type](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:

- node with sockets ['curve']

## set_radius {#set_radius}

> def set_radius(self, radius=None):

Node [Set Curve Radius](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- radius: Float

### Returns:

- node with sockets ['curve']

## set_tilt {#set_tilt}

> def set_tilt(self, tilt=None):

Node [Set Curve Tilt](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- tilt: Float

### Returns:

- node with sockets ['curve']

## tangent *property* {#tangent}

> def tangent(self):

Node [Curve Tangent](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'tangent'

## tilt *property* {#tilt}

> def tilt(self):

Node [Curve Tilt](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'tilt'

## tilt *etter* {#tilt}

> def tilt(self, attr_value):

Node [Set Curve Tilt](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: tilt


