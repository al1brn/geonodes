
# Class Texture

> Inherits from: ***dsock.Texture***

## Static methods



- Brick : Sockets      [color (Color), fac (Float)]
- Checker : Sockets      [color (Color), fac (Float)]
- Gradient : Sockets      [color (Color), fac (Float)]
- Image : Sockets      [color (Color), alpha (Float)]
- Magic : Sockets      [color (Color), fac (Float)]
- Musgrave : fac (Float)
- Noise : Sockets      [fac (Float), color (Color)]
- Voronoi : Sockets      [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
- Wave : Sockets      [color (Color), fac (Float)]
- WhiteNoise : Sockets      [value (Float), color (Color)]



## Methods



- switch : output (Texture)



## Methods


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



#### Returns

    Texture
