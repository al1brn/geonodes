# Texture

``` python
Texture(value: bpy_types.Texture | geonodes.core.socket_class.Socket | None = None, name: str | None = None, tip: str | None = None)
```

Socket of type Texture

#### Arguments:
- **value** (_bpy_types.Texture | geonodes.core.socket_class.Socket | None_ = None) : image or image name in bpy.data.images
- **name** (_str | None_ = None) : create a group input socket of type Image if not None
- **tip** (_str | None_ = None) : user tip for group input socket

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- [Brick](texture.md#brick)
- [Checked](texture.md#checked)
- [Gabor](texture.md#gabor)
- [Gradient](texture.md#gradient)
- [\_\_init__](texture.md#__init__)
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
Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```

> Class Method [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)

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
### Checked()

> classmethod

``` python
Checked(vector=None, color1=None, color2=None, scale=None)
```

> Class Method [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)

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
Gabor(vector=None, scale=None, frequency=None, anisotropy=None, orientation=None, gabor_type='2D')
```

> Class Method [Gabor Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gabor.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **frequency** (_Float_ = None) : socket 'Frequency' (id: Frequency)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **orientation** (_Float_ = None) : socket 'Orientation' (id: Orientation 2D)
- **gabor_type** (_str_ = 2D) : parameter 'gabor_type' in ('2D', '3D')



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Gradient()

> classmethod

``` python
Gradient(vector=None, gradient_type='LINEAR')
```

> Class Method [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **gradient_type** (_str_ = LINEAR) : parameter 'gradient_type' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value: bpy_types.Texture | geonodes.core.socket_class.Socket | None = None, name: str | None = None, tip: str | None = None)
```

Socket of type Texture

#### Arguments:
- **value** (_bpy_types.Texture | geonodes.core.socket_class.Socket | None_ = None) : image or image name in bpy.data.images
- **name** (_str | None_ = None) : create a group input socket of type Image if not None
- **tip** (_str | None_ = None) : user tip for group input socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Magic()

> classmethod

``` python
Magic(vector=None, scale=None, distortion=None, turbulence_depth=2)
```

> Class Method [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)

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
Noise(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, noise_dimensions='3D', noise_type='FBM', normalize=True)
```

> Class Method [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **noise_dimensions** (_str_ = 3D) : parameter 'noise_dimensions' in ('1D', '2D', '3D', '4D')
- **noise_type** (_str_ = FBM) : parameter 'noise_type' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
- **normalize** (_bool_ = True) : parameter 'normalize'



#### Returns:
- **Float** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Voronoi()

> classmethod

``` python
Voronoi(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, distance='EUCLIDEAN', feature='F1', normalize=False, voronoi_dimensions='3D')
```

> Class Method [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **randomness** (_Float_ = None) : socket 'Randomness' (id: Randomness)
- **distance** (_str_ = EUCLIDEAN) : parameter 'distance' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- **feature** (_str_ = F1) : parameter 'feature' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **normalize** (_bool_ = False) : parameter 'normalize'
- **voronoi_dimensions** (_str_ = 3D) : parameter 'voronoi_dimensions' in ('1D', '2D', '3D', '4D')



#### Returns:
- **Float** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### Wave()

> classmethod

``` python
Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```

> Class Method [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **detail_scale** (_Float_ = None) : socket 'Detail Scale' (id: Detail Scale)
- **detail_roughness** (_Float_ = None) : socket 'Detail Roughness' (id: Detail Roughness)
- **phase_offset** (_Float_ = None) : socket 'Phase Offset' (id: Phase Offset)
- **bands_direction** (_str_ = X) : parameter 'bands_direction' in ('X', 'Y', 'Z', 'DIAGONAL')
- **rings_direction** (_str_ = X) : parameter 'rings_direction' in ('X', 'Y', 'Z', 'SPHERICAL')
- **wave_profile** (_str_ = SIN) : parameter 'wave_profile' in ('SIN', 'SAW', 'TRI')
- **wave_type** (_str_ = BANDS) : parameter 'wave_type' in ('BANDS', 'RINGS')



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>

----------
### WhiteNoise()

> classmethod

``` python
WhiteNoise(vector=None, noise_dimensions='3D')
```

> Class Method [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **noise_dimensions** (_str_ = 3D) : parameter 'noise_dimensions' in ('1D', '2D', '3D', '4D')



#### Returns:
- **Float** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Texture](texture.md#texture) :black_small_square: [Content](texture.md#content) :black_small_square: [Methods](texture.md#methods)</sub>