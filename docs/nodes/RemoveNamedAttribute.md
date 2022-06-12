
# Node RemoveNamedAttribute

> Geometry node name: [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)<br>
  Blender type: [Remove Named Attribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.RemoveNamedAttribute(geometry=None, name=None, label=None)
        ```



## Arguments


### Input sockets

- geometry : Geometry
- name : String

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[remove_attribute](/docs/sockets/Geometry.md#remove_attribute) : Method
  
