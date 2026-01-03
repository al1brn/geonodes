# Texture

``` python
Texture(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Texture class

The Texture class only exposed texture creation class methods.

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_class_test](core-socke-socket.md#_class_test) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](core-socke-socket.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [Brick](texture.md#brick)
- [Checker](texture.md#checker)
- [Gabor](texture.md#gabor)
- [Gradient](texture.md#gradient)
- [Magic](texture.md#magic)
- [Noise](texture.md#noise)
- [Voronoi](texture.md#voronoi)
- [Wave](texture.md#wave)
- [WhiteNoise](texture.md#whitenoise)

## Methods



----------
### Brick()

> classmethod

``` python
Brick(vector: 'Vector' = None, color1: 'Color' = None, color2: 'Color' = None, mortar: 'Color' = None, scale: 'Float' = None, mortar_size: 'Float' = None, mortar_smooth: 'Float' = None, bias: 'Float' = None, brick_width: 'Float' = None, row_height: 'Float' = None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```

> Node [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **color1** (_Color_ = None) : socket 'Color1' (id: Color1)
- **color2** (_Color_ = None) : socket 'Color2' (id: Color2)
- **mortar** (_Color_ = None) : socket 'Mortar' (id: Mortar)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **mortar_size** (_Float_ = None) : socket 'Mortar Size' (id: Mortar Size)
- **mortar_smooth** (_Float_ = None) : socket 'Mortar Smooth' (id: Mortar Smooth)
- **bias** (_Float_ = None) : socket 'Bias' (id: Bias)
- **brick_width** (_Float_ = None) : socket 'Brick Width' (id: Brick Width)
- **row_height** (_Float_ = None) : socket 'Row Height' (id: Row Height)
- **offset** (_float_ = 0.5) : parameter 'offset'
- **offset_frequency** (_int_ = 2) : parameter 'offset_frequency'
- **squash** (_float_ = 1.0) : parameter 'squash'
- **squash_frequency** (_int_ = 2) : parameter 'squash_frequency'



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Checker()

> classmethod

``` python
Checker(vector: 'Vector' = None, color1: 'Color' = None, color2: 'Color' = None, scale: 'Float' = None)
```

> Node [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **color1** (_Color_ = None) : socket 'Color1' (id: Color1)
- **color2** (_Color_ = None) : socket 'Color2' (id: Color2)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Gabor()

> classmethod

``` python
Gabor(vector: 'Vector' = None, scale: 'Float' = None, frequency: 'Float' = None, anisotropy: 'Float' = None, orientation: 'Float' = None, gabor_type: "Literal['2D', '3D']" = '2D')
```

> Node [Gabor Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gabor.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **frequency** (_Float_ = None) : socket 'Frequency' (id: Frequency)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **orientation** (_Float_ = None) : socket 'Orientation' (id: Orientation 2D)
- **gabor_type** (_Literal['2D', '3D']_ = 2D) : parameter 'gabor_type' in ['2D', '3D']



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Gradient()

> classmethod

``` python
Gradient(vector: 'Vector' = None, gradient_type: "Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']" = 'LINEAR')
```

> Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **gradient_type** (_Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']_ = LINEAR) : parameter 'gradient_type' in ['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Magic()

> classmethod

``` python
Magic(vector: 'Vector' = None, scale: 'Float' = None, distortion: 'Float' = None, turbulence_depth=2)
```

> Node [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **turbulence_depth** (_int_ = 2) : parameter 'turbulence_depth'



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Noise()

> classmethod

``` python
Noise(vector: 'Vector' = None, scale: 'Float' = None, detail: 'Float' = None, roughness: 'Float' = None, lacunarity: 'Float' = None, distortion: 'Float' = None, noise_dimensions: "Literal['1D', '2D', '3D', '4D']" = '3D', noise_type: "Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']" = 'FBM', normalize=True)
```

> Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **noise_dimensions** (_Literal['1D', '2D', '3D', '4D']_ = 3D) : parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']
- **noise_type** (_Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']_ = FBM) : parameter 'noise_type' in ['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']
- **normalize** (_bool_ = True) : parameter 'normalize'



#### Returns:
- **Float** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Voronoi()

> classmethod

``` python
Voronoi(vector: 'Vector' = None, scale: 'Float' = None, detail: 'Float' = None, roughness: 'Float' = None, lacunarity: 'Float' = None, randomness: 'Float' = None, distance: "Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']" = 'EUCLIDEAN', feature: "Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']" = 'F1', normalize=False, voronoi_dimensions: "Literal['1D', '2D', '3D', '4D']" = '3D')
```

> Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **randomness** (_Float_ = None) : socket 'Randomness' (id: Randomness)
- **distance** (_Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']_ = EUCLIDEAN) : parameter 'distance' in ['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']
- **feature** (_Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']_ = F1) : parameter 'feature' in ['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']
- **normalize** (_bool_ = False) : parameter 'normalize'
- **voronoi_dimensions** (_Literal['1D', '2D', '3D', '4D']_ = 3D) : parameter 'voronoi_dimensions' in ['1D', '2D', '3D', '4D']



#### Returns:
- **Float** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Wave()

> classmethod

``` python
Wave(vector: 'Vector' = None, scale: 'Float' = None, distortion: 'Float' = None, detail: 'Float' = None, detail_scale: 'Float' = None, detail_roughness: 'Float' = None, phase_offset: 'Float' = None, bands_direction: "Literal['X', 'Y', 'Z', 'DIAGONAL']" = 'X', rings_direction: "Literal['X', 'Y', 'Z', 'SPHERICAL']" = 'X', wave_profile: "Literal['SIN', 'SAW', 'TRI']" = 'SIN', wave_type: "Literal['BANDS', 'RINGS']" = 'BANDS')
```

> Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **detail_scale** (_Float_ = None) : socket 'Detail Scale' (id: Detail Scale)
- **detail_roughness** (_Float_ = None) : socket 'Detail Roughness' (id: Detail Roughness)
- **phase_offset** (_Float_ = None) : socket 'Phase Offset' (id: Phase Offset)
- **bands_direction** (_Literal['X', 'Y', 'Z', 'DIAGONAL']_ = X) : parameter 'bands_direction' in ['X', 'Y', 'Z', 'DIAGONAL']
- **rings_direction** (_Literal['X', 'Y', 'Z', 'SPHERICAL']_ = X) : parameter 'rings_direction' in ['X', 'Y', 'Z', 'SPHERICAL']
- **wave_profile** (_Literal['SIN', 'SAW', 'TRI']_ = SIN) : parameter 'wave_profile' in ['SIN', 'SAW', 'TRI']
- **wave_type** (_Literal['BANDS', 'RINGS']_ = BANDS) : parameter 'wave_type' in ['BANDS', 'RINGS']



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### WhiteNoise()

> classmethod

``` python
WhiteNoise(vector: 'Vector' = None, noise_dimensions: "Literal['1D', '2D', '3D', '4D']" = '3D')
```

> Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **noise_dimensions** (_Literal['1D', '2D', '3D', '4D']_ = 3D) : parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']



#### Returns:
- **Float** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>