# class Object


## Class methods

- [(Self](Self-classmethod)


## Methods

- [(geometry](geometry)
- [(info](info)
- [(location](location)
- [(rotation](rotation)
- [(scale](scale)
- [(switch](switch)

## Self *classmethod*

{#Self}

> def Self(cls):

Node [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html) )

### Returns:

  socket 'self_object'

## geometry

{#geometry}

> def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'geometry'

## info

{#info}

> def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

- node with sockets ['location', 'rotation', 'scale', 'geometry']

## location

{#location}

> def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'location'

## rotation

{#rotation}

> def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'rotation'

## scale

{#scale}

> def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

        ### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'scale'

## switch

{#switch}

> def switch(self, switch=None, true=None):

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

