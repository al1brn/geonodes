# class {class_name}

## Self *classmethod* {#Self}

> def Self(cls):

Node [Self Object](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'self_object'

## geometry {#geometry}

> def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'geometry'

## info {#info}

> def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

- node with sockets ['location', 'rotation', 'scale', 'geometry']

## location {#location}

> def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'location'

## rotation {#rotation}

> def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'rotation'

## scale {#scale}

> def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'scale'

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

