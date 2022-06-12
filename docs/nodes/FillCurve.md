
# Node FillCurve

> Geometry node name: [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html)<br>
  Blender type: [Fill Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.FillCurve(curve=None, mode='TRIANGLES', label=None)
        ```



## Arguments


### Input sockets

- curve : Curve

### Parameters

- mode : str (default = 'TRIANGLES') in ('TRIANGLES', 'NGONS')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[fill](/docs/sockets/Curve.md#fill) : Method
  
