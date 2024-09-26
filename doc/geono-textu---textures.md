# textures

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : textures
-----------------
- Create the textures

This module implementes texture creation as class meythod of Texture class.
Texture class inherits from TextureRoot which can be created as a Group Input.

```  python
# Create a noise texture
noise_node = Texture.Noise()
```

classes
-------
- Texture       : Implements the texture nodes creation
    - Brick
    - Checker
    - Gradient
    - Image
    - Magic
    - Noise
    - Voronoi
    - Wave
    - WhiteNoise

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- [Texture](geono-textu-texture.md#texture)
- [Brick](geono-textu-texture.md#brick)
- [Checker](geono-textu-texture.md#checker)
- [Gradient](geono-textu-texture.md#gradient)
- [Image](geono-textu-texture.md#image)
- [Magic](geono-textu-texture.md#magic)
- [Noise](geono-textu-texture.md#noise)
- [Voronoi](geono-textu-texture.md#voronoi)
- [Wave](geono-textu-texture.md#wave)
- [WhiteNoise](geono-textu-texture.md#whitenoise)

## Classes



- [Texture](geono-textu-texture.md#texture)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [textures](geono-textu---textures.md#textures) :black_small_square: [Content](geono-textu---textures.md#content) :black_small_square: [textures](geono-textu---textures.md#textures)</sub>