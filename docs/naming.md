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

- 'Replace Material' -> **replace_material**
- 'Set Position' -> **set_position**
- 





