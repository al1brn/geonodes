
# Class WaveTexture

> Geometry node name: _'Wave Texture'_<br>Blender type:  **ShaderNodeTexWave**

## Initialization


```python
from geonodes import nodes
node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **scale** : _Float_
- **distortion** : _Float_
- **detail** : _Float_
- **detail_scale** : _Float_
- **detail_roughness** : _Float_
- **phase_offset** : _Float_



#### Parameters



- **bands_direction** : _'X'_ in ('X', 'Y', 'Z', 'DIAGONAL')
- **rings_direction** : _'X'_ in ('X', 'Y', 'Z', 'SPHERICAL')
- **wave_profile** : _'SIN'_ in ('SIN', 'SAW', 'TRI')
- **wave_type** : _'BANDS'_ in ('BANDS', 'RINGS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **color** : _Color_
- **fac** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Texture](./sockets/Texture.md) [Wave](./sockets/Texture.md#wave) : Static method


