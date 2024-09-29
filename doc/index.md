# geonodes

> Scripting nodes


### Tree

Scripting nodes starts by instantianting a [Tree](geono-tree.md#tree), either a [Geometry nodes tree](geono-geono-geonodes.md#geonodes) or
a [Shader nodes tree](shade-shade1-shadernodes.md#shadernodes):

Exiting from a tree context can be done by raising the [Break](geono-break.md#break) exception.

### Node class

Once the current tree instantiated, nodes can be created by instancianting a [Node](geono-node.md#node) class, for instance:

[Group](geono-group.md#group) is used to call a group. [GroupF](geono-groupf.md#groupf) does the same by exposing the **snake_name** name of
the called group.

Use [Layout](geono-layout.md#layout) class to group nodes in a Layout:

Zones are create using [Repeat](geono-repeat.md#repeat) and [Simulation](geono-simulation.md#simulation).

The special class [nd](geono-nd.md#nd) (for _nodes_) exposes all nodes by the **snake_case** name.

Use [snd](shade-shade1-snd.md#snd) (for _shader nodes_) when scripting [ShaderNodes](shade-shade1-shadernodes.md#shadernodes).

### Sockets

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
- [Geometry](geono-geometry.md#geometry) socket:
  - [Mesh](geono-mesh.md#mesh)
  - [Curve](geono-curve.md#curve)
  - [Cloud](geono-cloud.md#cloud)
  - [Instances](geono-instances.md#instances)
  - [Volume](geono-volume.md#volume)
- Shaders specific:
  - [Shader](shade-shade-shader.md#shader)
  - [VolumeShader](shade-shade-volumeshader.md#volumeshader)

#### Domains

Geometries have specific [Domain](geono-domain.md#domain):
- [Vertex](geono-vertex.md#vertex) ([Mesh](geono-mesh.md#mesh) [points](geono-mesh.md#points) property)
- [Edge](geono-edge.md#edge)  ([Mesh](geono-mesh.md#mesh) [edges](geono-mesh.md#edges) property)
- [Face](geono-face.md#face)  ([Mesh](geono-mesh.md#mesh) [faces](geono-mesh.md#faces) property)
- [Corner](geono-corner.md#corner)  ([Mesh](geono-mesh.md#mesh) [corners](geono-mesh.md#corners) property)
- [SplinePoint](geono-splinepoint.md#splinepoint) ([Curve](geono-curve.md#curve) [points](geono-curve.md#points) property)
- [Spline](geono-spline.md#spline) ([Curve](geono-curve.md#curve) [splines](geono-curve.md#splines) property)
- [CloudPoint](geono-cloudpoint.md#cloudpoint) ([Cloud](geono-cloud.md#cloud) [points](geono-cloud.md#points) property)
- [Instance](geono-instance.md#instance) ([Instances](geono-instances.md#instances) [insts](geono-instances.md#insts) property)

#### maths

The module [gnmath](geono-gnmat---gnmath.md#gnmath) provides math functions and be uses as standard python **math** library.

## Content

- [Cross Reference](cross_reference.md#cross-reference)
- [geonodes](geono---geonodes.md#geonodes)
  - [geonodes](geono-geono---geonodes.md#geonodes)
  - [gnmath](geono-gnmat---gnmath.md#gnmath)
  - [Boolean](geono-boolean.md#boolean)
  - [Break](geono-break.md#break)
  - [Cloud](geono-cloud.md#cloud)
  - [CloudPoint](geono-cloudpoint.md#cloudpoint)
  - [Collection](geono-collection.md#collection)
  - [Color](geono-color.md#color)
  - [Corner](geono-corner.md#corner)
  - [Curve](geono-curve.md#curve)
  - [Domain](geono-domain.md#domain)
  - [Edge](geono-edge.md#edge)
  - [Face](geono-face.md#face)
  - [Float](geono-float.md#float)
  - [Geometry](geono-geometry.md#geometry)
  - [Group](geono-group.md#group)
  - [GroupF](geono-groupf.md#groupf)
  - [Image](geono-image.md#image)
  - [Instance](geono-instance.md#instance)
  - [Instances](geono-instances.md#instances)
  - [Integer](geono-integer.md#integer)
  - [Layout](geono-layout.md#layout)
  - [Material](geono-material.md#material)
  - [Matrix](geono-matrix.md#matrix)
  - [Menu](geono-menu.md#menu)
  - [Mesh](geono-mesh.md#mesh)
  - [nd](geono-nd.md#nd)
  - [Node](geono-node.md#node)
  - [Object](geono-object.md#object)
  - [Repeat](geono-repeat.md#repeat)
  - [Rotation](geono-rotation.md#rotation)
  - [Simulation](geono-simulation.md#simulation)
  - [Socket](geono-socket.md#socket)
  - [Spline](geono-spline.md#spline)
  - [SplinePoint](geono-splinepoint.md#splinepoint)
  - [String](geono-string.md#string)
  - [Texture](geono-texture.md#texture)
  - [Tree](geono-tree.md#tree)
  - [Vector](geono-vector.md#vector)
  - [Vertex](geono-vertex.md#vertex)
  - [Volume](geono-volume.md#volume)
- [shadernodes](shade---shadernodes.md#shadernodes)
  - [shaderclass](shade-shade---shaderclass.md#shaderclass)
  - [shadernodes](shade-shade1---shadernodes.md#shadernodes)
  - [staticclass](shade-stati---staticclass.md#staticclass)

## Modules



- [geonodes](geono---geonodes.md#geonodes)
- [shadernodes](shade---shadernodes.md#shadernodes)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>

## Miscellaneous



- [Cross Reference](cross_reference.md#cross-reference)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>