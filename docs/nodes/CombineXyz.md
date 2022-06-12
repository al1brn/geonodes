
# Node CombineXyz

> Geometry node name: [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html)<br>
  Blender type: [Combine XYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
        from geonodes import nodes
        node = nodes.CombineXyz(x=None, y=None, z=None, label=None)
        ```



## Arguments


### Input sockets

- x : Float
- y : Float
- z : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- vector : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Vector](/docs/sockets/Vector.md).[Combine](/docs/sockets/Vector.md#combine) : Constructor
  
