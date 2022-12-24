# Class Texture

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content



**Class and static methods**

[Input](#Input) | [brick](#brick) | [checker](#checker) | [gradient](#gradient) | [gradient_diagonal](#gradient_diagonal) | [gradient_easing](#gradient_easing) | [gradient_linear](#gradient_linear) | [gradient_quadratic](#gradient_quadratic) | [gradient_quadratic_sphere](#gradient_quadratic_sphere) | [gradient_radial](#gradient_radial) | [gradient_spherical](#gradient_spherical) | [image](#image) | [magic](#magic) | [musgrave](#musgrave) | [noise](#noise) | [noise_1D](#noise_1D) | [noise_2D](#noise_2D) | [noise_3D](#noise_3D) | [noise_4D](#noise_4D) | [voronoi](#voronoi) | [voronoi_1D](#voronoi_1D) | [voronoi_2D](#voronoi_2D) | [voronoi_3D](#voronoi_3D) | [voronoi_4D](#voronoi_4D) | [wave](#wave) | [wave_bands](#wave_bands) | [wave_bands_saw](#wave_bands_saw) | [wave_bands_sine](#wave_bands_sine) | [wave_bands_triangle](#wave_bands_triangle) | [wave_rings](#wave_rings) | [wave_rings_saw](#wave_rings_saw) | [wave_rings_sine](#wave_rings_sine) | [wave_rings_triangle](#wave_rings_triangle) | [white_noise](#white_noise) | [white_noise_1D](#white_noise_1D) | [white_noise_2D](#white_noise_2D) | [white_noise_3D](#white_noise_3D) | [white_noise_4D](#white_noise_4D)

**Methods**

[switch](#switch)

## Class and static methods

### Input

```python
@classmethod
def Input(cls, value=None, name="Texture", description="")
```

 Create a Texture input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
Returns:
    Texture: The Texture data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### brick

```python
@staticmethod
def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```



## brick <sub>*staticmethod*</sub>

```python
def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):

```
> Node: [Brick Texture](ShaderNodeTexBrick.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexBrick.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### checker

```python
@staticmethod
def checker(vector=None, color1=None, color2=None, scale=None)
```



## checker <sub>*staticmethod*</sub>

```python
def checker(vector=None, color1=None, color2=None, scale=None):

```
> Node: [Checker Texture](ShaderNodeTexChecker.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)

#### Args:
- vector: Vector
- color1: Color
- color2: Color
- scale: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexChecker.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient

```python
@staticmethod
def gradient(vector=None, gradient_type='LINEAR')
```



## gradient <sub>*staticmethod*</sub>

```python
def gradient(vector=None, gradient_type='LINEAR'):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector
- gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_diagonal

```python
@staticmethod
def gradient_diagonal(vector=None)
```



## gradient_diagonal <sub>*staticmethod*</sub>

```python
def gradient_diagonal(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_easing

```python
@staticmethod
def gradient_easing(vector=None)
```



## gradient_easing <sub>*staticmethod*</sub>

```python
def gradient_easing(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_linear

```python
@staticmethod
def gradient_linear(vector=None)
```



## gradient_linear <sub>*staticmethod*</sub>

```python
def gradient_linear(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_quadratic

```python
@staticmethod
def gradient_quadratic(vector=None)
```



## gradient_quadratic <sub>*staticmethod*</sub>

```python
def gradient_quadratic(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_quadratic_sphere

```python
@staticmethod
def gradient_quadratic_sphere(vector=None)
```



## gradient_quadratic_sphere <sub>*staticmethod*</sub>

```python
def gradient_quadratic_sphere(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_radial

```python
@staticmethod
def gradient_radial(vector=None)
```



## gradient_radial <sub>*staticmethod*</sub>

```python
def gradient_radial(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gradient_spherical

```python
@staticmethod
def gradient_spherical(vector=None)
```



## gradient_spherical <sub>*staticmethod*</sub>

```python
def gradient_spherical(vector=None):

```
> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### image

```python
@staticmethod
def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```



## image <sub>*staticmethod*</sub>

```python
def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

```
> Node: [Image Texture](GeometryNodeImageTexture.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)

#### Args:
- image: Image
- vector: Vector
- frame: Integer
- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
- interpolation (str): 'Linear' in [Linear, Closest, Cubic]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

#### Returns:
- tuple ('`color`', '`alpha`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### magic

```python
@staticmethod
def magic(vector=None, scale=None, distortion=None, turbulence_depth=2)
```



## magic <sub>*staticmethod*</sub>

```python
def magic(vector=None, scale=None, distortion=None, turbulence_depth=2):

```
> Node: [Magic Texture](ShaderNodeTexMagic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- turbulence_depth (int): 2

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMagic.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### musgrave

```python
@staticmethod
def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM')
```



## musgrave <sub>*staticmethod*</sub>

```python
def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):

```
> Node: [Musgrave Texture](ShaderNodeTexMusgrave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### noise

```python
@staticmethod
def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D')
```



## noise <sub>*staticmethod*</sub>

```python
def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float
- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### noise_1D

```python
@staticmethod
def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None)
```



## noise_1D <sub>*staticmethod*</sub>

```python
def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### noise_2D

```python
@staticmethod
def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None)
```



## noise_2D <sub>*staticmethod*</sub>

```python
def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### noise_3D

```python
@staticmethod
def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None)
```



## noise_3D <sub>*staticmethod*</sub>

```python
def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### noise_4D

```python
@staticmethod
def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None)
```



## noise_4D <sub>*staticmethod*</sub>

```python
def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None):

```
> Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

#### Args:
- vector: Vector
- w: Float
- scale: Float
- detail: Float
- roughness: Float
- distortion: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### voronoi

```python
@staticmethod
def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```



## voronoi <sub>*staticmethod*</sub>

```python
def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

#### Returns:
- tuple ('`distance`', '`color`', '`position`', '`w`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### voronoi_1D

```python
@staticmethod
def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```



## voronoi_1D <sub>*staticmethod*</sub>

```python
def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- w: Float
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

#### Returns:
- tuple ('`distance`', '`color`', '`w`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### voronoi_2D

```python
@staticmethod
def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```



## voronoi_2D <sub>*staticmethod*</sub>

```python
def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- vector: Vector
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

#### Returns:
- tuple ('`distance`', '`color`', '`position`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### voronoi_3D

```python
@staticmethod
def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```



## voronoi_3D <sub>*staticmethod*</sub>

```python
def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

#### Args:
- vector: Vector
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float
- distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

#### Returns:
- tuple ('`distance`', '`color`', '`position`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### voronoi_4D

```python
@staticmethod
def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```



## voronoi_4D <sub>*staticmethod*</sub>

```python
def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):

```
> Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

#### Returns:
- tuple ('`distance`', '`color`', '`position`', '`w`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave

```python
@staticmethod
def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```



## wave <sub>*staticmethod*</sub>

```python
def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_bands

```python
@staticmethod
def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN')
```



## wave_bands <sub>*staticmethod*</sub>

```python
def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_bands_saw

```python
@staticmethod
def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```



## wave_bands_saw <sub>*staticmethod*</sub>

```python
def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_bands_sine

```python
@staticmethod
def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```



## wave_bands_sine <sub>*staticmethod*</sub>

```python
def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_bands_triangle

```python
@staticmethod
def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```



## wave_bands_triangle <sub>*staticmethod*</sub>

```python
def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, DIAGONAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_rings

```python
@staticmethod
def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN')
```



## wave_rings <sub>*staticmethod*</sub>

```python
def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_rings_saw

```python
@staticmethod
def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```



## wave_rings_saw <sub>*staticmethod*</sub>

```python
def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_rings_sine

```python
@staticmethod
def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```



## wave_rings_sine <sub>*staticmethod*</sub>

```python
def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wave_rings_triangle

```python
@staticmethod
def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
```



## wave_rings_triangle <sub>*staticmethod*</sub>

```python
def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):

```
> Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float
- direction (str): 'X' in [X, Y, Z, SPHERICAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

#### Returns:
- tuple ('`color`', '`fac`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### white_noise

```python
@staticmethod
def white_noise(vector=None, w=None, noise_dimensions='3D')
```



## white_noise <sub>*staticmethod*</sub>

```python
def white_noise(vector=None, w=None, noise_dimensions='3D'):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector
- w: Float
- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- tuple ('`value`', '`color`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### white_noise_1D

```python
@staticmethod
def white_noise_1D(w=None)
```



## white_noise_1D <sub>*staticmethod*</sub>

```python
def white_noise_1D(w=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- w: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- tuple ('`value`', '`color`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### white_noise_2D

```python
@staticmethod
def white_noise_2D(vector=None)
```



## white_noise_2D <sub>*staticmethod*</sub>

```python
def white_noise_2D(vector=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- tuple ('`value`', '`color`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### white_noise_3D

```python
@staticmethod
def white_noise_3D(vector=None)
```



## white_noise_3D <sub>*staticmethod*</sub>

```python
def white_noise_3D(vector=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- tuple ('`value`', '`color`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### white_noise_4D

```python
@staticmethod
def white_noise_4D(vector=None, w=None)
```



## white_noise_4D <sub>*staticmethod*</sub>

```python
def white_noise_4D(vector=None, w=None):

```
> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector
- w: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- tuple ('`value`', '`color`')






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### switch

```python
def switch(self, switch=None, true=None)
```



## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Texture

#### Returns:
- socket `output`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

