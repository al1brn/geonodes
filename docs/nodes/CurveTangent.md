
# Node CurveTangent

> Geometry node name: [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html)<br>
  Blender type: [Curve Tangent](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.CurveTangent(label=None)
        ```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- tangent : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_tangent](/docs/sockets/Spline.md#capture_tangent) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[tangent](/docs/sockets/Spline.md#tangent) : Attribute
  
