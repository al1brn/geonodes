# class {class_name}

## AxisAngle *classmethod* {#AxisAngle}

> def AxisAngle(cls, rotation=None, axis=None, angle=None, space='OBJECT'):

Node [Rotate Euler](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- rotation: Vector
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## Euler *classmethod* {#Euler}

> def Euler(cls, rotation=None, rotate_by=None, space='OBJECT'):

Node [Rotate Euler](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- rotation: Vector
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## align_to_vector {#align_to_vector}

> def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

Node [Align Euler to Vector](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

### Returns:

- node with sockets ['rotation']

## rotate_axis_angle {#rotate_axis_angle}

> def rotate_axis_angle(self, axis=None, angle=None, space='OBJECT'):

Node [Rotate Euler](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## rotate_euler {#rotate_euler}

> def rotate_euler(self, rotate_by=None, space='OBJECT'):

Node [Rotate Euler](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

