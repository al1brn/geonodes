# class Texture



## Static methods

- [brick](#brick-staticmethod)
- [checker](#checker-staticmethod)
- [gradient](#gradient-staticmethod)
- [gradient_diagonal](#gradient_diagonal-staticmethod)
- [gradient_easing](#gradient_easing-staticmethod)
- [gradient_linear](#gradient_linear-staticmethod)
- [gradient_quadratic](#gradient_quadratic-staticmethod)
- [gradient_quadratic_sphere](#gradient_quadratic_sphere-staticmethod)
- [gradient_radial](#gradient_radial-staticmethod)
- [gradient_spherical](#gradient_spherical-staticmethod)
- [image](#image-staticmethod)
- [magic](#magic-staticmethod)
- [musgrave](#musgrave-staticmethod)
- [noise](#noise-staticmethod)
- [noise_1D](#noise_1D-staticmethod)
- [noise_2D](#noise_2D-staticmethod)
- [noise_3D](#noise_3D-staticmethod)
- [noise_4D](#noise_4D-staticmethod)
- [voronoi](#voronoi-staticmethod)
- [voronoi_1D](#voronoi_1D-staticmethod)
- [voronoi_2D](#voronoi_2D-staticmethod)
- [voronoi_3D](#voronoi_3D-staticmethod)
- [voronoi_4D](#voronoi_4D-staticmethod)
- [wave](#wave-staticmethod)
- [wave_bands](#wave_bands-staticmethod)
- [wave_bands_saw](#wave_bands_saw-staticmethod)
- [wave_bands_sine](#wave_bands_sine-staticmethod)
- [wave_bands_triangle](#wave_bands_triangle-staticmethod)
- [wave_rings](#wave_rings-staticmethod)
- [wave_rings_saw](#wave_rings_saw-staticmethod)
- [wave_rings_sine](#wave_rings_sine-staticmethod)
- [wave_rings_triangle](#wave_rings_triangle-staticmethod)
- [white_noise](#white_noise-staticmethod)
- [white_noise_1D](#white_noise_1D-staticmethod)
- [white_noise_2D](#white_noise_2D-staticmethod)
- [white_noise_3D](#white_noise_3D-staticmethod)
- [white_noise_4D](#white_noise_4D-staticmethod)

## Methods

- [switch](#switch)

## brick <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- color1: Color
<sub>Go to [top](#class-Texture)</sub>- color2: Color
<sub>Go to [top](#class-Texture)</sub>- mortar: Color
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- mortar_size: Float
<sub>Go to [top](#class-Texture)</sub>- mortar_smooth: Float
<sub>Go to [top](#class-Texture)</sub>- bias: Float
<sub>Go to [top](#class-Texture)</sub>- brick_width: Float
<sub>Go to [top](#class-Texture)</sub>- row_height: Float
<sub>Go to [top](#class-Texture)</sub>- offset (float): 0.5
<sub>Go to [top](#class-Texture)</sub>- offset_frequency (int): 2
<sub>Go to [top](#class-Texture)</sub>- squash (float): 1.0
<sub>Go to [top](#class-Texture)</sub>- squash_frequency (int): 2
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## checker <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def checker(vector=None, color1=None, color2=None, scale=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- color1: Color
<sub>Go to [top](#class-Texture)</sub>- color2: Color
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient(vector=None, gradient_type='LINEAR'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_diagonal <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_diagonal(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_easing <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_easing(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_linear <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_linear(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_quadratic <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_quadratic(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_quadratic_sphere <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_quadratic_sphere(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_radial <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_radial(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## gradient_spherical <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def gradient_spherical(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## image <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- image: Image
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- frame: Integer
<sub>Go to [top](#class-Texture)</sub>- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
<sub>Go to [top](#class-Texture)</sub>- interpolation (str): 'Linear' in [Linear, Closest, Cubic]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'alpha')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## magic <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def magic(vector=None, scale=None, distortion=None, turbulence_depth=2):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- turbulence_depth (int): 2
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## musgrave <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Musgrave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- dimension: Float
<sub>Go to [top](#class-Texture)</sub>- lacunarity: Float
<sub>Go to [top](#class-Texture)</sub>- offset: Float
<sub>Go to [top](#class-Texture)</sub>- gain: Float
<sub>Go to [top](#class-Texture)</sub>- musgrave_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>- musgrave_type (str): 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>  socket 'fac'<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## noise <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- roughness: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## noise_1D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- roughness: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## noise_2D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- roughness: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## noise_3D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- roughness: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## noise_4D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- roughness: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## switch

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Texture)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>  socket 'output'<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## voronoi <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- smoothness: Float
<sub>Go to [top](#class-Texture)</sub>- exponent: Float
<sub>Go to [top](#class-Texture)</sub>- randomness: Float
<sub>Go to [top](#class-Texture)</sub>- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
<sub>Go to [top](#class-Texture)</sub>- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
<sub>Go to [top](#class-Texture)</sub>- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('distance', 'color', 'position', 'w')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## voronoi_1D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- smoothness: Float
<sub>Go to [top](#class-Texture)</sub>- exponent: Float
<sub>Go to [top](#class-Texture)</sub>- randomness: Float
<sub>Go to [top](#class-Texture)</sub>- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
<sub>Go to [top](#class-Texture)</sub>- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
<sub>Go to [top](#class-Texture)</sub>- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('distance', 'color', 'w')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## voronoi_2D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- smoothness: Float
<sub>Go to [top](#class-Texture)</sub>- exponent: Float
<sub>Go to [top](#class-Texture)</sub>- randomness: Float
<sub>Go to [top](#class-Texture)</sub>- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
<sub>Go to [top](#class-Texture)</sub>- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
<sub>Go to [top](#class-Texture)</sub>- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('distance', 'color', 'position')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## voronoi_3D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- smoothness: Float
<sub>Go to [top](#class-Texture)</sub>- exponent: Float
<sub>Go to [top](#class-Texture)</sub>- randomness: Float
<sub>Go to [top](#class-Texture)</sub>- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
<sub>Go to [top](#class-Texture)</sub>- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
<sub>Go to [top](#class-Texture)</sub>- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('distance', 'color', 'position')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## voronoi_4D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- smoothness: Float
<sub>Go to [top](#class-Texture)</sub>- exponent: Float
<sub>Go to [top](#class-Texture)</sub>- randomness: Float
<sub>Go to [top](#class-Texture)</sub>- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
<sub>Go to [top](#class-Texture)</sub>- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
<sub>Go to [top](#class-Texture)</sub>- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('distance', 'color', 'position', 'w')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- bands_direction (str): 'X' in [X, Y, Z, DIAGONAL]
<sub>Go to [top](#class-Texture)</sub>- rings_direction (str): 'X' in [X, Y, Z, SPHERICAL]
<sub>Go to [top](#class-Texture)</sub>- wave_profile (str): 'SIN' in [SIN, SAW, TRI]
<sub>Go to [top](#class-Texture)</sub>- wave_type (str): 'BANDS' in [BANDS, RINGS]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_bands <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, DIAGONAL]
<sub>Go to [top](#class-Texture)</sub>- wave_profile (str): 'SIN' in [SIN, SAW, TRI]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_bands_saw <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, DIAGONAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_bands_sine <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, DIAGONAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_bands_triangle <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, DIAGONAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_rings <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, SPHERICAL]
<sub>Go to [top](#class-Texture)</sub>- wave_profile (str): 'SIN' in [SIN, SAW, TRI]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_rings_saw <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, SPHERICAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_rings_sine <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, SPHERICAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## wave_rings_triangle <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- scale: Float
<sub>Go to [top](#class-Texture)</sub>- distortion: Float
<sub>Go to [top](#class-Texture)</sub>- detail: Float
<sub>Go to [top](#class-Texture)</sub>- detail_scale: Float
<sub>Go to [top](#class-Texture)</sub>- detail_roughness: Float
<sub>Go to [top](#class-Texture)</sub>- phase_offset: Float
<sub>Go to [top](#class-Texture)</sub>- direction (str): 'X' in [X, Y, Z, SPHERICAL]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('color', 'fac')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## white_noise <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def white_noise(vector=None, w=None, noise_dimensions='3D'):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('value', 'color')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## white_noise_1D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def white_noise_1D(w=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('value', 'color')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## white_noise_2D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def white_noise_2D(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('value', 'color')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## white_noise_3D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def white_noise_3D(vector=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('value', 'color')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>## white_noise_4D <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Texture)</sub>```python
<sub>Go to [top](#class-Texture)</sub>def white_noise_4D(vector=None, w=None):

<sub>Go to [top](#class-Texture)</sub>```
<sub>Go to [top](#class-Texture)</sub>Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html) )

<sub>Go to [top](#class-Texture)</sub>### Args:
<sub>Go to [top](#class-Texture)</sub>- vector: Vector
<sub>Go to [top](#class-Texture)</sub>- w: Float
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>### Returns:

<sub>Go to [top](#class-Texture)</sub>- tuple ('value', 'color')
<sub>Go to [top](#class-Texture)</sub>
<sub>Go to [top](#class-Texture)</sub>