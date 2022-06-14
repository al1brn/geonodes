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
  - 'Bezier Segment' -> **BezierSegment**
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
- ...

### Operation methods

> Operations are implemented both as global functions ans as method of their _Data Socket_ class

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
  - 'Math'
  - 'Vector Math'
  - 'Boolean Math'
  - 'Mix RGB'

The mehod name is the **lower case** version of the operation value:
- 'Math':
  - 'ADD' -> **add** (gn.add or value.add)
  - 'MULTIPLY' -> **multiply**
  - 'SUBTRACT' -> **subtract**

Some values are the same for several nodes, in that case, the **global** functions are prefixed with the lower case version of the class name:

- 'Vector Math':
  - 'ADD' -> **gn.ector_add** and **Vector.add**
  - 'MULTIPLY' -> **gn.vector_multiply** and **Vector.multiply**
  - 'SUBTRACT' -> **gn_vector_subtract** and **Vector.subtract**
  - 'DOT' -> **gn.dot** and **Vector.dot** (their is not ambiguity with 'Math' node)
  
For 'Boolean math', since `and`, `or` and `not`are python reserved keywords, the methods are names **b_and**, **b_or** and **b_not**.

Note that the node 'Mesh Boolean' gives birth to 3 methods:
- intersect
- union
- difference

```python
    my_mesh.insersect(mesh1, mesh2)
    my_mesh.union(mesh1, mesh2, mesh3)
    my_mesh.difference(mesh1, mesh2)
```








