# class Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


## Class methods

- [Input](#Input-classmethod)

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

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.
The initial value can be either a valid Blender Texture or the name of an existing Blender Texture.

#### Args:
- value: Blender Texture or name of an existing Blender Texture
- name: Input socket name. Avoid homonyms!
- description: user help

#### Returns:
- Texture

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## brick <sub>*staticmethod*</sub>

```python
def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):

```
> Node: [Brick Texture](ShaderNodeTexBrick.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)

#### Args:
- vector: Vector
- color1: Color
- color2: Color
- mortar: Color
- scale: Float
- mortar_size: Float
- mortar_smooth: Float
- bias: Float
- brick_width: Float
- row_height: Float
- offset (float): 0.5
- offset_frequency (int): 2
- squash (float): 1.0
- squash_frequency (int): 2

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## checker <sub>*staticmethod*</sub>

```python
def checker(vector=None, color1=None, color2=None, scale=None):

```
> Node: [Checker Texture](ShaderNodeTexChecker.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)

#### Args:
- vector: Vector
- color1: Color
- color2: Color
- scale: Float

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient <sub>*staticmethod*</sub>

```python
def gradient(vector=None, gradient_type='LINEAR'):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector
- gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_diagonal <sub>*staticmethod*</sub>

```python
def gradient_diagonal(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_easing <sub>*staticmethod*</sub>

```python
def gradient_easing(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_linear <sub>*staticmethod*</sub>

```python
def gradient_linear(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_quadratic <sub>*staticmethod*</sub>

```python
def gradient_quadratic(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_quadratic_sphere <sub>*staticmethod*</sub>

```python
def gradient_quadratic_sphere(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_radial <sub>*staticmethod*</sub>

```python
def gradient_radial(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## gradient_spherical <sub>*staticmethod*</sub>

```python
def gradient_spherical(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## image <sub>*staticmethod*</sub>

```python
def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

```
> Node: [Image Texture](GeometryNodeImageTexture.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)

#### Args:
- image: Image
- vector: Vector
- frame: Integer
- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
- interpolation (str): 'Linear' in [Linear, Closest, Cubic]

#### Returns:
- tuple ('`color`', '`alpha`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## magic <sub>*staticmethod*</sub>

```python
def magic(vector=None, scale=None, distortion=None, turbulence_depth=2):

```
> Node: [Magic Texture](ShaderNodeTexMagic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- turbulence_depth (int): 2

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## musgrave <sub>*staticmethod*</sub>

```python
def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):

```
> Node: [Musgrave Texture](ShaderNodeTexMusgrave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- detail: Float
- dimension: Float
- lacunarity: Float
- offset: Float
- gain: Float
- musgrave_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
- musgrave_type (str): 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]

#### Returns:
- socket `fac`

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## noise <sub>*staticmethod*</sub>

```python
def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float
- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## noise_1D <sub>*staticmethod*</sub>

```python
def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## noise_2D <sub>*staticmethod*</sub>

```python
def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## noise_3D <sub>*staticmethod*</sub>

```python
def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## noise_4D <sub>*staticmethod*</sub>

```python
def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Texture

#### Returns:
- socket `output`

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## voronoi <sub>*staticmethod*</sub>

```python
def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`distance`', '`color`', '`position`', '`w`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## voronoi_1D <sub>*staticmethod*</sub>

```python
def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- w: Float
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`distance`', '`color`', '`w`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## voronoi_2D <sub>*staticmethod*</sub>

```python
def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- vector: Vector
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`distance`', '`color`', '`position`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## voronoi_3D <sub>*staticmethod*</sub>

```python
def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- vector: Vector
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`distance`', '`color`', '`position`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## voronoi_4D <sub>*staticmethod*</sub>

```python
def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`distance`', '`color`', '`position`', '`w`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave <sub>*staticmethod*</sub>

```python
def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- bands_direction (str): 'X' in [X, Y, Z, DIAGONAL]
- rings_direction (str): 'X' in [X, Y, Z, SPHERICAL]
- wave_profile (str): 'SIN' in [SIN, SAW, TRI]
- wave_type (str): 'BANDS' in [BANDS, RINGS]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_bands <sub>*staticmethod*</sub>

```python
def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]
- wave_profile (str): 'SIN' in [SIN, SAW, TRI]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_bands_saw <sub>*staticmethod*</sub>

```python
def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_bands_sine <sub>*staticmethod*</sub>

```python
def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_bands_triangle <sub>*staticmethod*</sub>

```python
def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_rings <sub>*staticmethod*</sub>

```python
def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]
- wave_profile (str): 'SIN' in [SIN, SAW, TRI]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_rings_saw <sub>*staticmethod*</sub>

```python
def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_rings_sine <sub>*staticmethod*</sub>

```python
def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wave_rings_triangle <sub>*staticmethod*</sub>

```python
def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]

#### Returns:
- tuple ('`color`', '`fac`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## white_noise <sub>*staticmethod*</sub>

```python
def white_noise(vector=None, w=None, noise_dimensions='3D'):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector
- w: Float
- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

#### Returns:
- tuple ('`value`', '`color`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## white_noise_1D <sub>*staticmethod*</sub>

```python
def white_noise_1D(w=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- w: Float

#### Returns:
- tuple ('`value`', '`color`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## white_noise_2D <sub>*staticmethod*</sub>

```python
def white_noise_2D(vector=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`value`', '`color`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## white_noise_3D <sub>*staticmethod*</sub>

```python
def white_noise_3D(vector=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector

#### Returns:
- tuple ('`value`', '`color`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## white_noise_4D <sub>*staticmethod*</sub>

```python
def white_noise_4D(vector=None, w=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector
- w: Float

#### Returns:
- tuple ('`value`', '`color`')

<sub>Go to [top](#class-Texture) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

