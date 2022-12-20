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

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def Self(cls):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html) )

<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

  socket 'self_object'<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

## geometry

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

<sub>Go to [top](#class-Object)</sub>

### Args:
<sub>Go to [top](#class-Object)</sub>

- object: Object
<sub>Go to [top](#class-Object)</sub>

- as_instance: Boolean
<sub>Go to [top](#class-Object)</sub>

- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

  socket 'geometry'<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

## info

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

<sub>Go to [top](#class-Object)</sub>

### Args:
<sub>Go to [top](#class-Object)</sub>

- object: Object
<sub>Go to [top](#class-Object)</sub>

- as_instance: Boolean
<sub>Go to [top](#class-Object)</sub>

- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

- node with sockets ['location', 'rotation', 'scale', 'geometry']
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

## location

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

<sub>Go to [top](#class-Object)</sub>

### Args:
<sub>Go to [top](#class-Object)</sub>

- object: Object
<sub>Go to [top](#class-Object)</sub>

- as_instance: Boolean
<sub>Go to [top](#class-Object)</sub>

- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

  socket 'location'<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

## rotation

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

<sub>Go to [top](#class-Object)</sub>

### Args:
<sub>Go to [top](#class-Object)</sub>

- object: Object
<sub>Go to [top](#class-Object)</sub>

- as_instance: Boolean
<sub>Go to [top](#class-Object)</sub>

- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

  socket 'rotation'<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

## scale

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

<sub>Go to [top](#class-Object)</sub>

### Args:
<sub>Go to [top](#class-Object)</sub>

- object: Object
<sub>Go to [top](#class-Object)</sub>

- as_instance: Boolean
<sub>Go to [top](#class-Object)</sub>

- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

  socket 'scale'<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

## switch

<sub>Go to [top](#class-Object)</sub>

```python
<sub>Go to [top](#class-Object)</sub>

def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Object)</sub>

```
<sub>Go to [top](#class-Object)</sub>

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Object)</sub>

### Args:
<sub>Go to [top](#class-Object)</sub>

- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Object)</sub>

- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

### Returns:

<sub>Go to [top](#class-Object)</sub>

  socket 'output'<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>


<sub>Go to [top](#class-Object)</sub>

