# class Image




## Methods

- [switch](#switch)
- [texture](#texture)

## switch

<sub>Go to [top](#class-Image)</sub>```python
<sub>Go to [top](#class-Image)</sub>def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Image)</sub>```
<sub>Go to [top](#class-Image)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Image)</sub>### Args:
<sub>Go to [top](#class-Image)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Image)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Image)</sub>
<sub>Go to [top](#class-Image)</sub>### Returns:

<sub>Go to [top](#class-Image)</sub>  socket 'output'<sub>Go to [top](#class-Image)</sub>
<sub>Go to [top](#class-Image)</sub>
<sub>Go to [top](#class-Image)</sub>## texture

<sub>Go to [top](#class-Image)</sub>```python
<sub>Go to [top](#class-Image)</sub>def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

<sub>Go to [top](#class-Image)</sub>```
<sub>Go to [top](#class-Image)</sub>Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html) )

<sub>Go to [top](#class-Image)</sub>### Args:
<sub>Go to [top](#class-Image)</sub>- vector: Vector
<sub>Go to [top](#class-Image)</sub>- frame: Integer
<sub>Go to [top](#class-Image)</sub>- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
<sub>Go to [top](#class-Image)</sub>- interpolation (str): 'Linear' in [Linear, Closest, Cubic]
<sub>Go to [top](#class-Image)</sub>
<sub>Go to [top](#class-Image)</sub>### Returns:

<sub>Go to [top](#class-Image)</sub>- tuple ('color', 'alpha')
<sub>Go to [top](#class-Image)</sub>
<sub>Go to [top](#class-Image)</sub>