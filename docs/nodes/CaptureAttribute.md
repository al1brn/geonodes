
# Node CaptureAttribute

> Geometry node name: [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)<br>
  Blender type: [Capture Attribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None)
        ```



## Arguments


### Input sockets

- geometry : Geometry
- value : data_type dependant

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['attribute']   
  
  

## Output sockets

- geometry : Geometry
- attribute : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
  
- [Boolean](/docs/sockets/Boolean.md).[capture_attribute](/docs/sockets/Boolean.md#capture_attribute) : Method
- [Color](/docs/sockets/Color.md).[capture_attribute](/docs/sockets/Color.md#capture_attribute) : Method
- [Float](/docs/sockets/Float.md).[capture_attribute](/docs/sockets/Float.md#capture_attribute) : Method
- [Geometry](/docs/sockets/Geometry.md).[capture_attribute](/docs/sockets/Geometry.md#capture_attribute) : Method
- [Integer](/docs/sockets/Integer.md).[capture_attribute](/docs/sockets/Integer.md#capture_attribute) : Method
- [Vector](/docs/sockets/Vector.md).[capture_attribute](/docs/sockets/Vector.md#capture_attribute) : Method
  
