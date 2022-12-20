# class {class_name}

## LineBreak *staticmethod* {#LineBreak}

> def LineBreak():

Node [Special Characters](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'line_break'

## String *classmethod* {#String}

> def String(cls, string=''):

Node [String](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- string (str): ''

### Returns:

  socket 'string'

## Tab *staticmethod* {#Tab}

> def Tab():

Node [Special Characters](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'tab'

## equal {#equal}

> def equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## join {#join}

> def join(*strings, delimiter=None):

Node [Join Strings](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- strings: <m>String
- delimiter: String

### Returns:

  socket 'string'

## length *property* {#length}

> def length(self):

Node [String Length](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'length'

## not_equal {#not_equal}

> def not_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## replace {#replace}

> def replace(self, find=None, replace=None):

Node [Replace String](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- find: String
- replace: String

### Returns:

  socket 'string'

## slice {#slice}

> def slice(self, position=None, length=None):

Node [Slice String](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- position: Integer
- length: Integer

### Returns:

  socket 'string'

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## to_curves {#to_curves}

> def to_curves(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):

Node [String to Curves](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- string: String
- size: Float
- character_spacing: Float
- word_spacing: Float
- line_spacing: Float
- text_box_width: Float
- text_box_height: Float
- align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
- align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
- overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
- pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]

### Returns:

- tuple ('curve_instances', 'line', 'pivot_point')

