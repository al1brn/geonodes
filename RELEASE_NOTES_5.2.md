# GeoNodes 5.2.0

This release adds support for Blender 5.2 Geometry Nodes and introduces a new
helper for working with named geometry attributes.

## New Blender 5.2 nodes

| Blender node | GeoNodes API |
| --- | --- |
| Menu | `Menu(value)`, `nd.menu(menu)` |
| Reverse String | `String.reverse()`, `nd.reverse_string(...)` |
| Set String Case | `String.set_case(...)`, `String.lower()`, `String.upper()`, `nd.set_string_case(...)` |
| Split String | `String.split(...)`, `nd.split_string(...)` |
| Trim String | `String.trim(...)`, `nd.trim_string(...)` |
| Closure to List | `Closure.to_list(...)`, `nd.closure_to_list(...)` |
| Cluster by Connected | `Geometry.cluster_by_connected(...)`, `nd.cluster_by_connected(...)` |
| Cluster by Distance | `Geometry.cluster_by_distance(...)`, `nd.cluster_by_distance(...)` |
| Collection Children | `Collection.children(...)`, `nd.collection_children(...)` |
| Filter List | `socket.filter_list(...)`, `nd.filter_list(...)` |
| Get Attribute Names | `Geometry.get_attribute_names(...)`, `Domain.get_attribute_names(...)`, `nd.get_attribute_names(...)` |
| Get Geometry Component | `Geometry.get_component(...)`, `Geometry.get_mesh()`, `get_cloud()`, `get_point_cloud()`, `get_curve()`, `get_instances()`, `get_grease_pencil()`, `get_volume()`, and `nd.get_geometry_component(...)` |
| Font | `Font(...)`, `nd.font(...)` |
| Instance Reference | `Instances.reference`, `Instances.insts.reference`, `nd.instance_reference()` |
| Merge Points | `Geometry.merge_points(...)`, `Mesh.points.merge(...)`, `nd.merge_points(...)` |
| Mesh Bevel | `Mesh.bevel(...)`, `nd.mesh_bevel(...)` |
| Rename Attribute | `Geometry.rename_attribute(...)`, `Attribute.rename(...)`, `nd.rename_attribute(...)` |
| Set NURBS Order | `Curve.set_nurbs_order(...)`, `nd.set_nurbs_order(...)` |
| Set NURBS Weight | `Curve.set_nurbs_weight(...)`, `nd.set_nurbs_weight(...)` |
| Sort List | `socket.sort_list(...)`, `nd.sort_list(...)` |
| Tag Filter | `String.tag_filter(...)`, `nd.tag_filter(...)` |
| Transfer Attributes | `Geometry.transfer_attributes(...)`, `nd.transfer_attributes(...)` |
| XPBD Solver | `Bundle.xpbd_solver(...)`, `nd.xpbd_solver(...)` |
| Get Nested Bundle Paths | `Bundle.get_nested_paths(...)`, `nd.get_nested_bundle_paths(...)` |
| Implicit Conversion | `socket.implicit_conversion(...)`, `nd.implicit_conversion(...)` |

The list API introduced during Blender 5.2 development is also supported:

| Blender node | GeoNodes API |
| --- | --- |
| Field to List | `Socket.field_to_list(...)`, with `Socket.to_list(...)` as a shortcut, and `nd.field_to_list(...)` |
| Get List Item | `socket.get_list_item(...)`, `nd.get_list_item(...)` |
| List Length | `socket.list_length()`, `nd.list_length(...)` |

`Filter List`, `Sort List`, `Get List Item`, `List Length` and `Implicit
Conversion` are available on all compatible socket classes. The concrete
return type is inferred from the source socket.

### Not implemented

The following Blender 5.2 nodes are not currently exposed:

- Integer Vector
- Sample Sound Frequencies

## Named attributes with `Attribute`

GeoNodes 5.2 introduces the `Attribute` helper as a complement to the standard
named-attribute methods. It keeps the geometry, domain, name and data type
together, so a stored attribute can be manipulated much like a socket.

An attribute helper is normally created from a geometry domain:

```python
mesh = Mesh()

# Face attribute of type Vector
direction = mesh.faces.get("Direction", Vector)
direction.set((0, 0, 1))
```

It can also be created directly from a geometry by specifying its domain:

```python
weight = mesh.get("Weight", Float, domain="Point")
weight.set(0.5)
```

### Reading and writing values

The `value` property exposes the underlying Geometry Nodes operations:

- reading `attribute.value` creates a **Named Attribute** node;
- assigning `attribute.value` creates a **Store Named Attribute** node.

```python
weight = mesh.points.get("Weight", Float)

field = weight.value
weight.value = field * 2
```

The explicit `get()` and `set()` methods provide the same operations. A value
can be supplied directly to `set()`:

```python
weight.set(1.0)
```

### Attributes in expressions

An `Attribute` can be used with sockets, constants and other attributes. Normal
operators cache the resulting field in the helper. Calling `set()` without an
argument stores this cached result on the geometry:

```python
counter = mesh.faces.get("Counter", Integer)
counter = counter ** 2
counter = counter + 1
counter.set()
```

In-place operators store their result immediately:

```python
counter += 1
counter *= 2
```

### Attribute management

Named attributes can be renamed or removed through the same helper:

```python
attribute.rename("New Name")
attribute.remove()
```

Attribute names can be queried from a geometry or a domain, with optional data
type and domain filters:

```python
all_names = mesh.get_attribute_names()
face_vectors = mesh.faces.get_attribute_names(Vector)
```

`Attribute` builds Geometry Nodes fields and nodes. It does not directly read
or modify Blender mesh data from Python.
