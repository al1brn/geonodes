
# Data socket Texture

> Inherits from dsock.Texture
  
<sub>go to [index](/docs/index.md)</sub>



## Static methods

- [Brick](#brick) : Sockets      [color (Color), fac (Float)]
- [Checker](#checker) : Sockets      [color (Color), fac (Float)]
- [Gradient](#gradient) : Sockets      [color (Color), fac (Float)]
- [Image](#image) : Sockets      [color (Color), alpha (Float)]
- [Magic](#magic) : Sockets      [color (Color), fac (Float)]
- [Musgrave](#musgrave) : fac (Float)
- [Noise](#noise) : Sockets      [fac (Float), color (Color)]
- [Voronoi](#voronoi) : Sockets      [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
- [Wave](#wave) : Sockets      [color (Color), fac (Float)]
- [WhiteNoise](#whitenoise) : Sockets      [value (Float), color (Color)]

## Methods

- [switch](#switch) : output (Texture)

## Brick

> Node: [BrickTexture](/docs/nodes/BrickTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexBrick](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
node ref [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) </sub>
```python
v = Texture.Brick(vector, color1, color2, mortar, scale, mortar_size, mortar_smooth, bias, brick_width, row_height, offset, offset_frequency, squash, squash_frequency)
```

### Arguments


#### Sockets

- vector : Vector
  - color1 : Color
  - color2 : Color
  - mortar : Color
  - scale : Float
  - mortar_size : Float
  - mortar_smooth : Float
  - bias : Float
  - brick_width : Float
  - row_height : Float## Parameters
  - offset : 0.5
  - offset_frequency : 2
  - squash : 1.0
  - squash_frequency : 2
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
    ```

### Returns

Sockets [color (Color), fac (Float)]


## Checker

> Node: [CheckerTexture](/docs/nodes/CheckerTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexChecker](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
node ref [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) </sub>
```python
v = Texture.Checker(vector, color1, color2, scale)
```

### Arguments


#### Sockets

- vector : Vector
  - color1 : Color
  - color2 : Color
  - scale : Float
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)
    ```

### Returns

Sockets [color (Color), fac (Float)]


## Gradient

> Node: [GradientTexture](/docs/nodes/GradientTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
node ref [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) </sub>
```python
v = Texture.Gradient(vector, gradient_type)
```

### Arguments


#### Sockets

- vector : Vector## Parameters
  - gradient_type : 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.GradientTexture(vector=vector, gradient_type=gradient_type)
    ```

### Returns

Sockets [color (Color), fac (Float)]


## Magic

> Node: [MagicTexture](/docs/nodes/MagicTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexMagic](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
node ref [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) </sub>
```python
v = Texture.Magic(vector, scale, distortion, turbulence_depth)
```

### Arguments


#### Sockets

- vector : Vector
  - scale : Float
  - distortion : Float## Parameters
  - turbulence_depth : 2
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
    ```

### Returns

Sockets [color (Color), fac (Float)]


## Musgrave

> Node: [MusgraveTexture](/docs/nodes/MusgraveTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexMusgrave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
node ref [Musgrave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) </sub>
```python
v = Texture.Musgrave(vector, w, scale, detail, dimension, lacunarity, offset, gain, musgrave_dimensions, musgrave_type)
```

### Arguments


#### Sockets

- vector : Vector
  - w : Float
  - scale : Float
  - detail : Float
  - dimension : Float
  - lacunarity : Float
  - offset : Float
  - gain : Float## Parameters
  - musgrave_dimensions : '3D' in [1D, 2D, 3D, 4D]
  - musgrave_type : 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type)
    ```

### Returns

Float


## Noise

> Node: [NoiseTexture](/docs/nodes/NoiseTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
node ref [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) </sub>
```python
v = Texture.Noise(vector, w, scale, detail, roughness, distortion, noise_dimensions)
```

### Arguments


#### Sockets

- vector : Vector
  - w : Float
  - scale : Float
  - detail : Float
  - roughness : Float
  - distortion : Float## Parameters
  - noise_dimensions : '3D' in [1D, 2D, 3D, 4D]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)
    ```

### Returns

Sockets [fac (Float), color (Color)]


## Voronoi

> Node: [VoronoiTexture](/docs/nodes/VoronoiTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexVoronoi](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
node ref [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) </sub>
```python
v = Texture.Voronoi(vector, w, scale, smoothness, exponent, randomness, distance, feature, voronoi_dimensions)
```

### Arguments


#### Sockets

- vector : Vector
  - w : Float
  - scale : Float
  - smoothness : Float
  - exponent : Float
  - randomness : Float## Parameters
  - distance : 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
  - feature : 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
  - voronoi_dimensions : '3D' in [1D, 2D, 3D, 4D]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
    ```

### Returns

Sockets [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]


## Wave

> Node: [WaveTexture](/docs/nodes/WaveTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
node ref [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) </sub>
```python
v = Texture.Wave(vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset, bands_direction, rings_direction, wave_profile, wave_type)
```

### Arguments


#### Sockets

- vector : Vector
  - scale : Float
  - distortion : Float
  - detail : Float
  - detail_scale : Float
  - detail_roughness : Float
  - phase_offset : Float## Parameters
  - bands_direction : 'X' in [X, Y, Z, DIAGONAL]
  - rings_direction : 'X' in [X, Y, Z, SPHERICAL]
  - wave_profile : 'SIN' in [SIN, SAW, TRI]
  - wave_type : 'BANDS' in [BANDS, RINGS]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
    ```

### Returns

Sockets [color (Color), fac (Float)]


## WhiteNoise

> Node: [WhiteNoiseTexture](/docs/nodes/WhiteNoiseTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
node ref [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) </sub>
```python
v = Texture.WhiteNoise(vector, w, noise_dimensions)
```

### Arguments


#### Sockets

- vector : Vector
  - w : Float## Parameters
  - noise_dimensions : '3D' in [1D, 2D, 3D, 4D]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)
    ```

### Returns

Sockets [value (Float), color (Color)]


## Image

> Node: [ImageTexture](/docs/nodes/ImageTexture.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [GeometryNodeImageTexture](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
node ref [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) </sub>
```python
v = Texture.Image(image, vector, frame, extension, interpolation)
```

### Arguments


#### Sockets

- image : Image
  - vector : Vector
  - frame : Integer## Parameters
  - extension : 'REPEAT' in [REPEAT, EXTEND, CLIP]
  - interpolation : 'Linear' in [Linear, Closest, Cubic]
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
    ```

### Returns

Sockets [color (Color), alpha (Float)]


## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-texture) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
```python
v = texture.switch(switch1, true)
```

### Arguments


#### Sockets

- false : Texture (self)
  - switch1 : Boolean
  - true : Texture## Fixed parameters
  - input_type : 'TEXTURE'
    
    Node creation
    -------------
    ```python
    from geondes import nodes
    nodes.Switch(false=self, switch1=switch1, true=true, input_type='TEXTURE')
    ```

### Returns

Texture

