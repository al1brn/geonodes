# Naming conventions

> Blender has names for nodes, nodes sockets, nodes parameters and nodes parameters values.
> This section explains the conventions used to name python classes, methods and properties after these names

## Nodes

The nodes class names are **CamelCase** versions of their Blender name:
- 'Replace Material' -> **ReplaceMaterial**
- 'Checker Texture' -> **CheckerTexture**

Note that the Blender node 'ColorRamp' is strangely named in one word. This CamelCase named is kept:
- 'ColorRamp' -> **ColorRamp**

## Output sockets

Output sockets are implemented as properties of node classes.
Their python name is the **snake_case** of their name.
Since, the most often, the socket names are single words, their python name is the lower case version of their name:
- Geometry -> **geometry**
- Attribute -> **attribute**
- Value -> **value**

## Data sockets

_Data socket_ classes are named as basic names: **Boolean**, **Integer**, **Geometry**... (see [Data socket classes](/README.md#data-socket-classes) for the full list)

## Methods and properties

_Data sockets_ classes have methods and properties which can be named in two ways:
1. After the node they implement ('Set Shade Smooth' -> **set_shade_smooth**)
2. After the parameter value used when creating the node they implement ('Math', operation = 'ADD' -> **add**)

### Node methods

To follow python typo conventions, the naming depends upon if it is a constructor or not.

#### Constructors (class or static methods)

This concerns the nodes accessible in the Blender Add menus: **Mesh Primitives**, **Curve Primitives** and **Texture**.

Nodes methods are **CamelCase** versions of their Blender name, but **removing the class name** when it exists:

- Mesh constructors:
  - 'Mesh Line' -> **Mesh.Line**
  - 'Mesh Circle' -> **Mesh.Circle**
  - 'Cone' -> **Mesh.Cone**
  - 'Grid' -> **Mesh.Grid**
  - ...
- Curve constructors
  - 'Curve Line' -> **Curve.Line**
  - 'Curve Circle' -> **Curve.Circle**
  - 'Bezier Segment' -> **Curve.BezierSegment**
  - ...
- Texture constructors:
  - 'Brick Texture' -> **Texture.Brick**
  - 'Noise Texture' -> **Texture.Noise**
  - 'Gradient Texture' -> **Texture.Gradient**
  - ...

#### Methods

Instances methods are named with the **snake_version** of the node name, but **removing the class name** when it exists:

- 'Replace Material' -> **geometry.replace_material**
- 'Set Position' -> **geometry.set_position**
- 'Curve to Mesh' -> **curve.to_mesh**
- 'Realize Instances' -> **instances.realize**
- 'Rotate Instances' -> **instances.insts.rotate**
- ...

### Operation methods

> Operations are implemented both as global functions and as method of their _Data Socket_ class

```python
    a = gn.Float(5.)
    b = gn.Float(6.)
    
    c = gn.add(a, b)
    # or
    c = a.add(b)
    
    d = gn.sin(a)
    # or
    d = a.sin()
```

The following nodes are implemented as many times as their are possible value for their parameter:
  - [Math](/docs/nodes/Math.md)
  - [Vector Math](/docs/nodes/VectorMath.md)
  - [Boolean Math](/docs/nodes/BooleanMath.md)
  - [Mix RGB](/docs/nodes/Mix.md)

The mehod name is the **lower case** version of the operation value:
- 'Math':
  - 'ADD' -> **add** (gn.add or value.add)
  - 'MULTIPLY' -> **multiply**
  - 'SUBTRACT' -> **subtract**

Some values are the same for several nodes, in that case, the **global** functions are prefixed with the lower case version of the class name:

- 'Vector Math':
  - 'ADD' -> **gn.vector_add** and **Vector.add**
  - 'MULTIPLY' -> **gn.vector_multiply** and **Vector.multiply**
  - 'SUBTRACT' -> **gn_vector_subtract** and **Vector.subtract**
  - 'DOT' -> **gn.dot** and **Vector.dot** (their is not ambiguity with 'Math' node)
  
For 'Boolean math', since `and`, `or` and `not`are python reserved keywords, the methods are names **b_and**, **b_or** and **b_not**.

Note that the node [Mesh Boolean](/docs/nodes/MeshBoolean.md) gives birth to 3 methods:
- [intersect](/docs/sockets/Mesh.md#intersect)
- [union](/docs/sockets/Mesh.md#union)
- [difference](/docs/sockets/Mesh.md#difference)

```python
    my_mesh.insersect(mesh1, mesh2)
    my_mesh.union(mesh1, mesh2, mesh3)
    my_mesh.difference(mesh1, mesh2)
```
## Node parameters names

The node parameter names is equal to the python Blender class representing the object.

## Node input socket names

The node input socket names are used as arguments when creating a node or calling a method based on a node.
As for the output sockets, their names is the **snake_case** version of their Blender name.

**Note:** Input sockets are _write only_ when output sockets are _read only_.
Hence, input and output sockets can share the same name without ambiguity:

``` python

node = nodes.SubdivideMesh()

node.mesh = my_geometry         # node input socket
subdivided_geometry = node.mesh # node output socket

```

When several sockets share the same name, their are suffixed by their rank, starting from 0 as illustrated in the class Math constructor

```python

class Math(Node):
    def __init__(self, value0=None, value1=None, value2=None, operation='ADD', label=None):

```

The Math has between 1 and 3 visible nodes depending upon its operation.











