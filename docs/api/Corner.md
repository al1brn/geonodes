# class Corner

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)




## Methods

- [domain_size](#domain_size)

## domain_size

```python
def __len__(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Corner) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

