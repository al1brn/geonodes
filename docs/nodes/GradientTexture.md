
# Node GradientTexture

> Geometry node name: [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/gradient_texture.html)<br>
  Blender type: [Gradient Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.GradientTexture(vector=None, gradient_type='LINEAR', label=None)
```



## Arguments


### Input sockets

vector : Vector

### Parameters

gradient_type : str (default = 'LINEAR') in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

color : Color
- fac : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Texture) [Gradient](section:Data socket Texture/Gradient) : Static method

