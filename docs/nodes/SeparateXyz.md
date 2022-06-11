
# Node SeparateXyz

> Geometry node name: [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_xyz.html)<br>
  Blender type: [Separate XYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateXyz(vector=None, label=None)
```



## Arguments


### Input sockets

vector : Vector

### Node label

- label : Geometry node display label (default=None)

## Output sockets

x : Float
- y : Float
- z : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Vector) [separate](section:Data socket Vector/separate) : Property
- [class_name](section:Data socket Vector) [x](section:Data socket Vector/x) : Property
- [class_name](section:Data socket Vector) [y](section:Data socket Vector/y) : Property
- [class_name](section:Data socket Vector) [z](section:Data socket Vector/z) : Property
  
