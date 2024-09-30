# rain

Created on 2024/08/02

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/rain
-------------------
Simulates rain falling on a terrain.
The input geometry is a terrain with holes containing water
The dips falling in the holes produce waves.
The dips falling outside of the holes, generate smaller dips bouncing on the terrain

updates
-------
- creation : 2024/08/02
- update   : 2024/08/03

## Content

- [dip_wave](demos-rain---rain.md#dip_wave)

## Functions



----------
### dip_wave()

> function

``` python
dip_wave(center, t, length=3.0, c=5, falloff=30, omega=4, height=1, amp_only=False)
```

Wave produced by a dip

Note that location and center are supposed to be in plane (x, y)

#### Arguments:
- **center** (_Vector_) : dip impact location
- **t** (_Float_) : time
- **length** (_Float_ = 3.0) : length non null amplitude
- **c** (_Float_ = 5) : wave celerity
- **falloff** (_Float_ = 30) : falloff factor
- **omega** (_Float_ = 4) : wave omega
- **height** (_Float_ = 1) : wave height
- **amp_only** (_Boolean_ = False) : show only the amplitude



#### Returns:
- **Float** : wave heigth at position

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [rain](demos-rain---rain.md#rain) :black_small_square: [Content](demos-rain---rain.md#content) :black_small_square: [Functions](demos-rain---rain.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [rain](demos-rain---rain.md#rain) :black_small_square: [Content](demos-rain---rain.md#content) :black_small_square: [rain](demos-rain---rain.md#rain)</sub>