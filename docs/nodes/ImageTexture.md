
# Node ImageTexture

> Geometry node name: [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)<br>
  Blender type: [Image Texture](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None)
```



## Arguments


### Input sockets

- image : Image
- vector : Vector
- frame : Integer

### Parameters

- extension : str (default = 'REPEAT') in ('REPEAT', 'EXTEND', 'CLIP')
- interpolation : str (default = 'Linear') in ('Linear', 'Closest', 'Cubic')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- color : Color
- alpha : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Texture](/docs/sockets/Texture.md).[Image](/docs/sockets/Texture.md#image) : Static method
  
