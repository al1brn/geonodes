# class Object


## Class methods

- [Self](#Self-classmethod)


## Methods

- [geometry](#geometry)
- [info](#info)
- [location](#location)
- [rotation](#rotation)
- [scale](#scale)
- [switch](#switch)

## Self <span style="color:blue">*classmethod*</span>

```python
def Self(cls):

```
Node [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html) )

### Returns:

  socket 'self_object'

<sub>Go to [top](#class-Object)</sub>

## geometry

```python
def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'geometry'

<sub>Go to [top](#class-Object)</sub>

## info

```python
def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

- node with sockets ['location', 'rotation', 'scale', 'geometry']

<sub>Go to [top](#class-Object)</sub>

## location

```python
def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'location'

<sub>Go to [top](#class-Object)</sub>

## rotation

```python
def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'rotation'

<sub>Go to [top](#class-Object)</sub>

## scale

```python
def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Returns:

  socket 'scale'

<sub>Go to [top](#class-Object)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

<sub>Go to [top](#class-Object)</sub>

