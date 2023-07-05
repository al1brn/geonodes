# Class Texture

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Brick](#Brick) | [Checker](#Checker) | [Gradient](#Gradient) | [GradientDiagonal](#GradientDiagonal) | [GradientEeasing](#GradientEeasing) | [GradientLinear](#GradientLinear) | [GradientQuadratic](#GradientQuadratic) | [GradientQuadratic_sphere](#GradientQuadratic_sphere) | [GradientRadial](#GradientRadial) | [GradientSpherical](#GradientSpherical) | [Image](#Image) | [Input](#Input) | [Magic](#Magic) | [Musgrave](#Musgrave) | [Noise](#Noise) | [Noise1D](#Noise1D) | [Noise2D](#Noise2D) | [Noise3D](#Noise3D) | [Noise4D](#Noise4D) | [Voronoi](#Voronoi) | [Voronoi1D](#Voronoi1D) | [Voronoi2D](#Voronoi2D) | [Voronoi3D](#Voronoi3D) | [Voronoi4D](#Voronoi4D) | [Wave](#Wave) | [WaveBands](#WaveBands) | [WaveBands_saw](#WaveBands_saw) | [WaveBands_sine](#WaveBands_sine) | [WaveBands_triangle](#WaveBands_triangle) | [WaveRings](#WaveRings) | [WaveRings_saw](#WaveRings_saw) | [WaveRings_sine](#WaveRings_sine) | [WaveRings_triangle](#WaveRings_triangle) | [WhiteNoise](#WhiteNoise) | [WhiteNoise1D](#WhiteNoise1D) | [WhiteNoise2D](#WhiteNoise2D) | [WhiteNoise3D](#WhiteNoise3D) | [WhiteNoise4D](#WhiteNoise4D)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[switch](#switch)

***Inherited***

[capture](DataSocket.md#capture) | [connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Class and static methods

### Brick

```python
@staticmethod
def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Checker

```python
@staticmethod
def Checker(vector=None, color1=None, color2=None, scale=None)
```



> Node: [Checker Texture](ShaderNodeTexChecker.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)

#### Args:
- vector: Vector
- color1: Color
- color2: Color
- scale: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexChecker.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Gradient

```python
@staticmethod
def Gradient(vector=None, gradient_type='LINEAR')
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector
- gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientDiagonal

```python
@staticmethod
def GradientDiagonal(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientEeasing

```python
@staticmethod
def GradientEeasing(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientLinear

```python
@staticmethod
def GradientLinear(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientQuadratic

```python
@staticmethod
def GradientQuadratic(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientQuadratic_sphere

```python
@staticmethod
def GradientQuadratic_sphere(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientRadial

```python
@staticmethod
def GradientRadial(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### GradientSpherical

```python
@staticmethod
def GradientSpherical(vector=None)
```



> Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Image

```python
@staticmethod
def Image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```



> Node: [Image Texture](GeometryNodeImageTexture.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)

#### Args:
- image: Image
- vector: Vector
- frame: Integer
- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP, MIRROR]
- interpolation (str): 'Linear' in [Linear, Closest, Cubic]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

#### Returns:
- node with sockets ['color', 'alpha']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, value=None, name="Texture", description="")
```

 Create a Texture input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
#### Returns:
- Texture: The Texture data socket




<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Magic

```python
@staticmethod
def Magic(vector=None, scale=None, distortion=None, turbulence_depth=2)
```



> Node: [Magic Texture](ShaderNodeTexMagic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)

#### Args:
- vector: Vector
- scale: Float
- distortion: Float
- turbulence_depth (int): 2

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMagic.webp)

#### Returns:
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Musgrave

```python
@classmethod
def Musgrave(cls, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM')
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






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Noise

```python
@staticmethod
def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D')
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
- node with sockets ['fac', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Noise1D

```python
@staticmethod
def Noise1D(w=None, scale=None, detail=None, roughness=None, distortion=None)
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
- node with sockets ['fac', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Noise2D

```python
@staticmethod
def Noise2D(vector=None, scale=None, detail=None, roughness=None, distortion=None)
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
- node with sockets ['fac', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Noise3D

```python
@staticmethod
def Noise3D(vector=None, scale=None, detail=None, roughness=None, distortion=None)
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
- node with sockets ['fac', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Noise4D

```python
@staticmethod
def Noise4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None)
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
- node with sockets ['fac', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Voronoi

```python
@staticmethod
def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
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
- node with sockets ['distance', 'color', 'position', 'w', 'radius']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Voronoi1D

```python
@staticmethod
def Voronoi1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
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
- node with sockets ['distance', 'color', 'position', 'w', 'radius']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Voronoi2D

```python
@staticmethod
def Voronoi2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
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
- node with sockets ['distance', 'color', 'position', 'w', 'radius']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Voronoi3D

```python
@staticmethod
def Voronoi3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
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
- node with sockets ['distance', 'color', 'position', 'w', 'radius']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Voronoi4D

```python
@staticmethod
def Voronoi4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
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
- node with sockets ['distance', 'color', 'position', 'w', 'radius']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Wave

```python
@staticmethod
def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveBands

```python
@staticmethod
def WaveBands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveBands_saw

```python
@staticmethod
def WaveBands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveBands_sine

```python
@staticmethod
def WaveBands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveBands_triangle

```python
@staticmethod
def WaveBands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveRings

```python
@staticmethod
def WaveRings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveRings_saw

```python
@staticmethod
def WaveRings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveRings_sine

```python
@staticmethod
def WaveRings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WaveRings_triangle

```python
@staticmethod
def WaveRings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X')
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
- node with sockets ['color', 'fac']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WhiteNoise

```python
@staticmethod
def WhiteNoise(vector=None, w=None, noise_dimensions='3D')
```



> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector
- w: Float
- noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- node with sockets ['value', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WhiteNoise1D

```python
@staticmethod
def WhiteNoise1D(w=None)
```



> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- w: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- node with sockets ['value', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WhiteNoise2D

```python
@staticmethod
def WhiteNoise2D(vector=None)
```



> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- node with sockets ['value', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WhiteNoise3D

```python
@staticmethod
def WhiteNoise3D(vector=None)
```



> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- node with sockets ['value', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### WhiteNoise4D

```python
@staticmethod
def WhiteNoise4D(vector=None, w=None)
```



> Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

#### Args:
- vector: Vector
- w: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

#### Returns:
- node with sockets ['value', 'color']






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Texture

#### Returns:
- socket `output`






<sub>Go to [top](#class-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

