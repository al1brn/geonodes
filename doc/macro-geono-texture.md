# Texture

> Bases classes: [TextureRoot](geono-textureroot.md#textureroot)

``` python
Texture(value=None, name=None, tip=None)
```

Socket of type Texture

#### Arguments:
- **value** (_bpy.types.Image or str_ = None) : image or image name in bpy.data.images
- **name** (_str_ = None) : create a group input socket of type Image if not None
- **tip** (_str_ = None) : user tip for group input socket

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square:

## Content

- [Brick](macro-geono-texture.md#brick)
- [Checker](macro-geono-texture.md#checker)
- [Gradient](macro-geono-texture.md#gradient)
- [Image](macro-geono-texture.md#image)
- [Magic](macro-geono-texture.md#magic)
- [Noise](macro-geono-texture.md#noise)
- [Voronoi](macro-geono-texture.md#voronoi)
- [Wave](macro-geono-texture.md#wave)
- [WhiteNoise](macro-geono-texture.md#whitenoise)

## Methods



----------
### Brick()

> staticmethod

``` python
Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None)
```

> Node [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **color1** (_Color_ = None) : socket 'Color1' (Color1)
- **color2** (_Color_ = None) : socket 'Color2' (Color2)
- **mortar** (_Color_ = None) : socket 'Mortar' (Mortar)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **mortar_size** (_Float_ = None) : socket 'Mortar Size' (Mortar Size)
- **mortar_smooth** (_Float_ = None) : socket 'Mortar Smooth' (Mortar Smooth)
- **bias** (_Float_ = None) : socket 'Bias' (Bias)
- **brick_width** (_Float_ = None) : socket 'Brick Width' (Brick Width)
- **row_height** (_Float_ = None) : socket 'Row Height' (Row Height)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Checker()

> staticmethod

``` python
Checker(vector=None, color1=None, color2=None, scale=None)
```

> Node [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **color1** (_Color_ = None) : socket 'Color1' (Color1)
- **color2** (_Color_ = None) : socket 'Color2' (Color2)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Gradient()

> staticmethod

``` python
Gradient(vector=None)
```

> Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Image()

> staticmethod

``` python
Image(image=None, vector=None, frame=None, interpolation='Linear', extension='REPEAT')
```

> Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)

#### Arguments:
- **image** (_Image_ = None) : socket 'Image' (Image)
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **frame** (_Integer_ = None) : socket 'Frame' (Frame)
- **interpolation** (_str_ = Linear) : Node.interpolation in ('Linear', 'Closest', 'Cubic')
- **extension** (_str_ = REPEAT) : Node.extension in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Magic()

> staticmethod

``` python
Magic(vector=None, scale=None, distortion=None)
```

> Node [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (Distortion)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Noise()

> staticmethod

``` python
Noise(vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, offset=None, gain=None, distortion=None, dim='3D', noise_type='FBM')
```

> Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **w** (_Float_ = None) : socket 'W' (W)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **detail** (_Float_ = None) : socket 'Detail' (Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (Lacunarity)
- **offset** (_Float_ = None) : socket 'Offset' (Offset)
- **gain** (_Float_ = None) : socket 'Gain' (Gain)
- **distortion** (_Float_ = None) : socket 'Distortion' (Distortion)
- **dim** (_str_ = 3D) : Node.noise_dimensions in ('1D', '2D', '3D', '4D')
- **noise_type** (_str_ = FBM) : Node.noise_type in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Voronoi()

> staticmethod

``` python
Voronoi(vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, smoothness=None, exponent=None, randomness=None, dim='3D', feature='F1', distance='EUCLIDEAN')
```

> Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **w** (_Float_ = None) : socket 'W' (W)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **detail** (_Float_ = None) : socket 'Detail' (Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (Lacunarity)
- **smoothness** (_Float_ = None) : socket 'Smoothness' (Smoothness)
- **exponent** (_Float_ = None) : socket 'Exponent' (Exponent)
- **randomness** (_Float_ = None) : socket 'Randomness' (Randomness)
- **dim** (_str_ = 3D) : Node.voronoi_dimensions in ('1D', '2D', '3D', '4D')
- **feature** (_str_ = F1) : Node.feature in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **distance** (_str_ = EUCLIDEAN) : Node.distance in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### Wave()

> staticmethod

``` python
Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, wave_type='BANDS', bands_direction='X', rings_direction='X', wave_profile='SIN')
```

> Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (Distortion)
- **detail** (_Float_ = None) : socket 'Detail' (Detail)
- **detail_scale** (_Float_ = None) : socket 'Detail Scale' (Detail Scale)
- **detail_roughness** (_Float_ = None) : socket 'Detail Roughness' (Detail Roughness)
- **phase_offset** (_Float_ = None) : socket 'Phase Offset' (Phase Offset)
- **wave_type** (_str_ = BANDS) : Node.wave_type in ('BANDS', 'RINGS')
- **bands_direction** (_str_ = X) : Node.bands_direction in ('X', 'Y', 'Z', 'DIAGONAL')
- **rings_direction** (_str_ = X) : Node.rings_direction in ('X', 'Y', 'Z', 'SPHERICAL')
- **wave_profile** (_str_ = SIN) : Node.wave_profile in ('SIN', 'SAW', 'TRI')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>

----------
### WhiteNoise()

> staticmethod

``` python
WhiteNoise(vector=None, w=None, dim='3D')
```

> Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **w** (_Float_ = None) : socket 'W' (W)
- **dim** (_str_ = 3D) : Node.noise_dimensions in ('1D', '2D', '3D', '4D')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](macro-geono-texture.md#texture) :black_small_square: [Content](macro-geono-texture.md#content) :black_small_square: [Methods](macro-geono-texture.md#methods)</sub>