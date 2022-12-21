# Node Domain Size

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
- geonodes name: `DomainSize`
- bl_idname: `GeometryNodeAttributeDomainSize`

```python
from geonodes import nodes

node = nodes.DomainSize(geometry=None, component='MESH')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **component** (str): default = 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')

### Output sockets:

- **point_count** : [Integer](Integer.md)
- **edge_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)
- **face_corner_count** : [Integer](Integer.md)
- **spline_count** : [Integer](Integer.md)
- **instance_count** : [Integer](Integer.md)

## Implementation

#### [CloudPoint](CloudPoint.md)

 - [domain_size](CloudPoint.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [ControlPoint](ControlPoint.md)

 - [domain_size](ControlPoint.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [Corner](Corner.md)

 - [domain_size](Corner.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [Curve](Curve.md)

 - [domain_size](Curve.md#domain_size-property)
  ```python
  nodes.DomainSize(geometry=self, component='CURVE'  ```

 - [point_count](Curve.md#point_count-property)
  ```python
  nodes.DomainSize(geometry=self, component='CURVE'  ```

 - [spline_count](Curve.md#spline_count-property)
  ```python
  nodes.DomainSize(geometry=self, component='CURVE'  ```

#### [Edge](Edge.md)

 - [domain_size](Edge.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [Face](Face.md)

 - [domain_size](Face.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [Geometry](Geometry.md)

 - [domain_size](Geometry.md#domain_size-property)
  ```python
  nodes.DomainSize(geometry=self, component=component  ```

#### [Instance](Instance.md)

 - [domain_size](Instance.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [Instances](Instances.md)

 - [domain_size](Instances.md#domain_size-property)
  ```python
  nodes.DomainSize(geometry=self, component='INSTANCES'  ```

#### [Mesh](Mesh.md)

 - [domain_size](Mesh.md#domain_size-property)
  ```python
  nodes.DomainSize(geometry=self, component='MESH'  ```

 - [point_count](Mesh.md#point_count-property)
  ```python
  nodes.DomainSize(geometry=self, component='MESH'  ```

 - [face_count](Mesh.md#face_count-property)
  ```python
  nodes.DomainSize(geometry=self, component='MESH'  ```

 - [edge_count](Mesh.md#edge_count-property)
  ```python
  nodes.DomainSize(geometry=self, component='MESH'  ```

 - [corner_count](Mesh.md#corner_count-property)
  ```python
  nodes.DomainSize(geometry=self, component='MESH'  ```

#### [Points](Points.md)

 - [domain_size](Points.md#domain_size-property)
  ```python
  nodes.DomainSize(geometry=self, component='POINTCLOUD'  ```

#### [Spline](Spline.md)

 - [domain_size](Spline.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

#### [Vertex](Vertex.md)

 - [domain_size](Vertex.md#domain_size)
  ```python
  nodes.DomainSize(geometry=geometry, component=component  ```

