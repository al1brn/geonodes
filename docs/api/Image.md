# class {class_name}

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## texture {#texture}

> def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

Node [Image Texture](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector
- frame: Integer
- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
- interpolation (str): 'Linear' in [Linear, Closest, Cubic]

### Returns:

- tuple ('color', 'alpha')

