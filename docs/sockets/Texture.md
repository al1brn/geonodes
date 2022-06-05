
# Class Texture

> Inherits from: ***dsock.Texture***

## Static methods



- [**Brick**](#brick) : [BrickTexture](../nodes/BrickTexture.md) Sockets      [color (Color), fac (Float)]
- [**Checker**](#checker) : [CheckerTexture](../nodes/CheckerTexture.md) Sockets      [color (Color), fac (Float)]
- [**Gradient**](#gradient) : [GradientTexture](../nodes/GradientTexture.md) Sockets      [color (Color), fac (Float)]
- [**Image**](#image) : [ImageTexture](../nodes/ImageTexture.md) Sockets      [color (Color), alpha (Float)]
- [**Magic**](#magic) : [MagicTexture](../nodes/MagicTexture.md) Sockets      [color (Color), fac (Float)]
- [**Musgrave**](#musgrave) : [MusgraveTexture](../nodes/MusgraveTexture.md) fac (Float)
- [**Noise**](#noise) : [NoiseTexture](../nodes/NoiseTexture.md) Sockets      [fac (Float), color (Color)]
- [**Voronoi**](#voronoi) : [VoronoiTexture](../nodes/VoronoiTexture.md) Sockets      [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
- [**Wave**](#wave) : [WaveTexture](../nodes/WaveTexture.md) Sockets      [color (Color), fac (Float)]
- [**WhiteNoise**](#whitenoise) : [WhiteNoiseTexture](../nodes/WhiteNoiseTexture.md) Sockets      [value (Float), color (Color)]



## Methods



- [**switch**](#switch) : [Switch](../nodes/Switch.md) output (Texture)



## Methods reference


### Brick

> Node: [BrickTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Brick(vector, color1, color2, mortar, scale, mortar_size, mortar_smooth, bias, brick_width, row_height, offset, offset_frequency, squash, squash_frequency)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- color1 : Color
- color2 : Color
- mortar : Color
- scale : Float
- mortar_size : Float
- mortar_smooth : Float
- bias : Float
- brick_width : Float
- row_height : Float



##### Parameters arguments



- offset : 0.5
- offset_frequency : 2
- squash : 1.0
- squash_frequency : 2



#### Node creation


```python
node = nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
```


#### Returns

    Sockets [color (Color), fac (Float)]

### Checker

> Node: [CheckerTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Checker(vector, color1, color2, scale)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- color1 : Color
- color2 : Color
- scale : Float



#### Node creation


```python
node = nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)
```


#### Returns

    Sockets [color (Color), fac (Float)]

### Gradient

> Node: [GradientTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Gradient(vector, gradient_type)
```


#### Arguments


##### Sockets arguments



- vector : Vector



##### Parameters arguments



- gradient_type : 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]



#### Node creation


```python
node = nodes.GradientTexture(vector=vector, gradient_type=gradient_type)
```


#### Returns

    Sockets [color (Color), fac (Float)]

### Image

> Node: [ImageTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Image(image, vector, frame, extension, interpolation)
```


#### Arguments


##### Sockets arguments



- image : Image
- vector : Vector
- frame : Integer



##### Parameters arguments



- extension : 'REPEAT' in [REPEAT, EXTEND, CLIP]
- interpolation : 'Linear' in [Linear, Closest, Cubic]



#### Node creation


```python
node = nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
```


#### Returns

    Sockets [color (Color), alpha (Float)]

### Magic

> Node: [MagicTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Magic(vector, scale, distortion, turbulence_depth)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- scale : Float
- distortion : Float



##### Parameters arguments



- turbulence_depth : 2



#### Node creation


```python
node = nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
```


#### Returns

    Sockets [color (Color), fac (Float)]

### Musgrave

> Node: [MusgraveTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Musgrave(vector, w, scale, detail, dimension, lacunarity, offset, gain, musgrave_dimensions, musgrave_type)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- w : Float
- scale : Float
- detail : Float
- dimension : Float
- lacunarity : Float
- offset : Float
- gain : Float



##### Parameters arguments



- musgrave_dimensions : '3D' in [1D, 2D, 3D, 4D]
- musgrave_type : 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]



#### Node creation


```python
node = nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type)
```


#### Returns

    Float

### Noise

> Node: [NoiseTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Noise(vector, w, scale, detail, roughness, distortion, noise_dimensions)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- w : Float
- scale : Float
- detail : Float
- roughness : Float
- distortion : Float



##### Parameters arguments



- noise_dimensions : '3D' in [1D, 2D, 3D, 4D]



#### Node creation


```python
node = nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)
```


#### Returns

    Sockets [fac (Float), color (Color)]

### Voronoi

> Node: [VoronoiTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Voronoi(vector, w, scale, smoothness, exponent, randomness, distance, feature, voronoi_dimensions)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- w : Float
- scale : Float
- smoothness : Float
- exponent : Float
- randomness : Float



##### Parameters arguments



- distance : 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
- feature : 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
- voronoi_dimensions : '3D' in [1D, 2D, 3D, 4D]



#### Node creation


```python
node = nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
```


#### Returns

    Sockets [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]

### Wave

> Node: [WaveTexture](../nodes/{self.node_name}.md)

```python
v = Texture.Wave(vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset, bands_direction, rings_direction, wave_profile, wave_type)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- scale : Float
- distortion : Float
- detail : Float
- detail_scale : Float
- detail_roughness : Float
- phase_offset : Float



##### Parameters arguments



- bands_direction : 'X' in [X, Y, Z, DIAGONAL]
- rings_direction : 'X' in [X, Y, Z, SPHERICAL]
- wave_profile : 'SIN' in [SIN, SAW, TRI]
- wave_type : 'BANDS' in [BANDS, RINGS]



#### Node creation


```python
node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
```


#### Returns

    Sockets [color (Color), fac (Float)]

### WhiteNoise

> Node: [WhiteNoiseTexture](../nodes/{self.node_name}.md)

```python
v = Texture.WhiteNoise(vector, w, noise_dimensions)
```


#### Arguments


##### Sockets arguments



- vector : Vector
- w : Float



##### Parameters arguments



- noise_dimensions : '3D' in [1D, 2D, 3D, 4D]



#### Node creation


```python
node = nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)
```


#### Returns

    Sockets [value (Float), color (Color)]

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = texture.switch(switch1, true)
```


#### Arguments


##### Sockets arguments



- false : Texture (self)
- switch1 : Boolean
- true : Texture



##### Fixed parameters



- input_type : 'TEXTURE'



#### Node creation


```python
node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='TEXTURE')
```


#### Returns

    Texture
