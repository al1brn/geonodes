# class Corner




## Methods

- [domain_size](#domain_size)

## domain_size

<sub>Go to [top](#class-Corner)</sub>```python
<sub>Go to [top](#class-Corner)</sub>def __len__(self):

<sub>Go to [top](#class-Corner)</sub>```
<sub>Go to [top](#class-Corner)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Corner)</sub>### Args:
<sub>Go to [top](#class-Corner)</sub>- geometry: Geometry
<sub>Go to [top](#class-Corner)</sub>- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-Corner)</sub>
<sub>Go to [top](#class-Corner)</sub>### Returns:

<sub>Go to [top](#class-Corner)</sub>- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Corner)</sub>
<sub>Go to [top](#class-Corner)</sub>