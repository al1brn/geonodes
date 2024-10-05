# geonodes

> Scripting nodes


### Initialize a tree

- [GeoNodes](geono-geono-geonodes.md#geonodes) and [ShaderNodes](shade1-shade1-shadernodes.md#shadernodes) : scripting nodes starts by instantianting a [Tree](tree.md#tree)
- [Break](break.md#break) : exiting from a tree context can be done by raising this exception

### Create nodes

- [Node](node.md#node) : base class to create any node in a tree
- [Group](group.md#group) : create a <*Node Group> node
- [GroupF](groupf.md#groupf) : a different way to create a <*Node Group> node
- [Layout](layout.md#layout) : to place nodes in a frame
- [Repeat](repeat.md#repeat) and [Simulation](simulation.md#simulation) : create a [Zone](zone.md#zone)

### Libraries

- [gnmath](gnmath.md#gnmath) : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- [nd](nd.md#nd) (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- [snd](snd.md#snd) (for _shader nodes_) : same as [nd](nd.md#nd) for shader node

### Sockets

Rather than using [Node](node.md#node) class, scripting nodes is done by using [Socket](socket.md#socket) classes:

- Data sockets:
  - [Attributes](attribute.md#attribute):
    - [Boolean](boolean.md#boolean)
    - [Integer](integer.md#integer)
    - [Float](float.md#float)
    - [Color](color.md#color)
    - [Vector](vector.md#vector)
    - [Rotation](rotation.md#rotation)
    - [Matrix](matrix.md#matrix)
  - [String](string.md#string)
  - [Menu](menu.md#menu)
- Blender resources:
  - [Collection](collection.md#collection)
  - [Object](object.md#object)
  - [Image](image.md#image)
  - [Material](material.md#material)
  - [Texture](texture.md#texture)
- [Geometry](geometry.md#geometry) socket:
  - [Mesh](mesh.md#mesh)
  - [Curve](curve.md#curve)
  - [Cloud](cloud.md#cloud)
  - [Instances](instances.md#instances)
  - [Volume](volume.md#volume)
- Shaders specific:
  - [Shader](shader.md#shader)
  - [VolumeShader](volumeshader.md#volumeshader)

#### Domains

Geometries have specific [Domain](domain.md#domain):
- [Mesh](mesh.md#mesh) :
  - [Vertex](vertex.md#vertex) : property [points](mesh.md#points)
  - [Edge](edge.md#edge) : property [edges](mesh.md#edges)
  - [Face](face.md#face) : property [faces](mesh.md#faces)
  - [Corner](corner.md#corner) : property [corners](mesh.md#corners)
- [Curve](curve.md#curve) :
  - [SplinePoint](splinepoint.md#splinepoint) : property [points](curve.md#points)
  - [Spline](spline.md#spline) : property [splines](curve.md#splines)
- [Cloud](cloud.md#cloud) :
  - [CloudPoint](cloudpoint.md#cloudpoint) : property [points](cloud.md#points)
- [Instances](instances.md#instances) :
  - [Instance](instance.md#instance) : property [insts](instances.md#insts)

#### Cross reference

- [Cross Reference](cross_reference.md#cross-reference) : to see how each Geometry Node can be scripted
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference) : to see how each Shader Node can be scripted

## Content

- [Cross Reference](cross_reference.md#cross-reference)
- [demos](demos.md#demos)
  - [arrows](arrows.md#arrows)
  - [counters](counters.md#counters)
  - [curly](curly.md#curly)
  - [explosion](explosion.md#explosion)
  - [fields](fields.md#fields)
  - [fourd](fourd.md#fourd)
  - [gravity](gravity.md#gravity)
  - [helloworld](helloworld.md#helloworld)
  - [rain](rain.md#rain)
  - [relativity](relativity.md#relativity)
  - [shaders](shaders.md#shaders)
- [generation](generation.md#generation)
  - [gendoc](gendoc.md#gendoc)
- [geonodes](geono---geonodes.md#geonodes)
  - [geonodes](geono-geono---geonodes.md#geonodes)
  - [gnmath](gnmath.md#gnmath)
  - [Attribute](attribute.md#attribute)
  - [Boolean](boolean.md#boolean)
  - [Break](break.md#break)
  - [Cloud](cloud.md#cloud)
  - [CloudPoint](cloudpoint.md#cloudpoint)
  - [Collection](collection.md#collection)
  - [Color](color.md#color)
  - [Corner](corner.md#corner)
  - [Curve](curve.md#curve)
  - [Domain](domain.md#domain)
  - [Edge](edge.md#edge)
  - [Face](face.md#face)
  - [Float](float.md#float)
  - [Geometry](geometry.md#geometry)
  - [Group](group.md#group)
  - [GroupF](groupf.md#groupf)
  - [Image](image.md#image)
  - [Instance](instance.md#instance)
  - [Instances](instances.md#instances)
  - [Integer](integer.md#integer)
  - [Layout](layout.md#layout)
  - [Material](material.md#material)
  - [Matrix](matrix.md#matrix)
  - [Menu](menu.md#menu)
  - [Mesh](mesh.md#mesh)
  - [nd](nd.md#nd)
  - [Node](node.md#node)
  - [Object](object.md#object)
  - [Repeat](repeat.md#repeat)
  - [Rotation](rotation.md#rotation)
  - [Simulation](simulation.md#simulation)
  - [Socket](socket.md#socket)
  - [Spline](spline.md#spline)
  - [SplinePoint](splinepoint.md#splinepoint)
  - [String](string.md#string)
  - [Texture](texture.md#texture)
  - [Tree](tree.md#tree)
  - [Vector](vector.md#vector)
  - [Vertex](vertex.md#vertex)
  - [Volume](volume.md#volume)
  - [Zone](zone.md#zone)
- [macros](macros.md#macros)
  - [double_integrals](macros.md#double_integrals)
  - [impulsion](macros.md#impulsion)
  - [integrals](macros.md#integrals)
  - [solidify](macros.md#solidify)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)
- [shadernodes](shade1---shadernodes.md#shadernodes)
  - [shaderclass](shaderclass.md#shaderclass)
  - [shadernodes](shade1-shade1---shadernodes.md#shadernodes)
  - [staticclass](staticclass.md#staticclass)

## Modules



- [demos](demos.md#demos)
- [generation](generation.md#generation)
- [geonodes](geono---geonodes.md#geonodes)
- [macros](macros.md#macros)
- [shadernodes](shade1---shadernodes.md#shadernodes)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>

## Miscellaneous



- [Cross Reference](cross_reference.md#cross-reference)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>