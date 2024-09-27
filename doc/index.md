# geonodes

Scripting nodes


Scripting nodes starts by instantianting a [Tree](geono-tree.md#tree), either a [Geometry nodes tree](geono-geono-geonodes.md#geonodes) or
a [Shader nodes tree](shade-shade1-shadernodes.md#shadernodes):

``` python
with GeoNodes("Geometry Nodes"):
    pass
```

Once the current tree instantiated, nodes can be created by instancianting a [Node](geono-node.md#node) class, for instance:

``` python
with GeoNodes("Geometry Nodes"):
    node = Node('Set Position', {'Geometry': ..., 'Selection': ..., 'Offset': ...})
    result = node.geometry
```

A better and more pythonistic way to script nodes, is to use a [Socket](geono-socket.md#socket) subclass among:

- Data sockets:
  - [Boolean](geono-boolean.md#boolean)
  - [Integer](geono-integer.md#integer)
  - [Float](geono-float.md#float)
  - [Color](geono-color.md#color)
  - [Vector](geono-vector.md#vector)
  - [Rotation](geono-rotation.md#rotation)
  - [Matrix](geono-matrix.md#matrix)
  - [String](geono-string.md#string)
  - [Menu](geono-menu.md#menu)
- Blender resources:
  - [Collection](geono-collection.md#collection)
  - [Object](geono-object.md#object)
  - [Image](geono-image.md#image)
  - [Material](geono-material.md#material)
  - [Texture](geono-texture.md#texture)
- And of course a [Geometry](geono-geometry.md#geometry) socket:
  - [Mesh](geono-mesh.md#mesh)
  - [Curve](geono-curve.md#curve)
  - [Cloud](geono-cloud.md#cloud)
  - [Instances](geono-instances.md#instances)
  - [Volume](geono-volume.md#volume)

``` python
geometry = Geometry()
# Create a 'Set Position' node by calling the method of Geometry
moved_geometry = geometry.set_position(...)
```

## Content

- [Cross Reference](cross_reference.md#cross_reference)
- [geonodes](geono---geonodes.md#geonodes)
- [shadernodes](shade---shadernodes.md#shadernodes)

## Modules



- [geonodes](geono---geonodes.md#geonodes)
- [shadernodes](shade---shadernodes.md#shadernodes)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>

- [Cross Reference](cross_reference.md#cross_reference)