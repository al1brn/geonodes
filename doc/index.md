# geonodes

> Scripting nodes


### Initialize a tree

- [GeoNodes](geono-geono-geonodes.md#geonodes) and [ShaderNodes](macro-shade1-shade1-shadernodes.md#shadernodes) : scripting nodes starts by instantianting a [Tree](geono-tree.md#tree)
- [Break](geono-break.md#break) : exiting from a tree context can be done by raising this exception

### Create nodes

- [Node](geono-node.md#node) : base class to create any node in a tree
- [Group](geono-group.md#group) : create a <*Node Group> node
- [GroupF](geono-groupf.md#groupf) : a different way to create a <*Node Group> node
- [Layout](geono-layout.md#layout) : to place nodes in a frame
- [Repeat](geono-repeat.md#repeat) and [Simulation](geono-simulation.md#simulation) : create a [Zone](geono-zone.md#zone)

### Libraries

- [gnmath](geono-gnmat---gnmath.md#gnmath) : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- [nd](geono-nd.md#nd) (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- [snd](macro-shade1-shade1-snd.md#snd) (for _shader nodes_) : same as [nd](geono-nd.md#nd) for shader node

### Sockets

Rather than using [Node](geono-node.md#node) class, scripting nodes is done by using [Socket](geono-socket.md#socket) classes:

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
  - [Shader](macro-shade1-shade-shader.md#shader)
  - [VolumeShader](macro-shade1-shade-volumeshader.md#volumeshader)

#### Domains

Geometries have specific [Domain](geono-domain.md#domain):
- [Mesh](geono-mesh.md#mesh) :
  - [Vertex](geono-vertex.md#vertex) : property [points](geono-mesh.md#points)
  - [Edge](geono-edge.md#edge) : property [edges](geono-mesh.md#edges)
  - [Face](geono-face.md#face) : property [faces](geono-mesh.md#faces)
  - [Corner](geono-corner.md#corner) : property [corners](geono-mesh.md#corners)
- [Curve](geono-curve.md#curve) :
  - [SplinePoint](geono-splinepoint.md#splinepoint) : property [points](geono-curve.md#points)
  - [Spline](geono-spline.md#spline) : property [splines](geono-curve.md#splines)
- [Cloud](geono-cloud.md#cloud) :
  - [CloudPoint](geono-cloudpoint.md#cloudpoint) : property [points](geono-cloud.md#points)
- [Instances](geono-instances.md#instances) :
  - [Instance](geono-instance.md#instance) : property [insts](geono-instances.md#insts)

#### Cross reference

- [Cross Reference](cross_reference.md#cross-reference) : to see how each Geometry Node can be scripted
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference) : to see how each Shader Node can be scripted

## Content

- [Cross Reference](cross_reference.md#cross-reference)
- [demos](demos---demos.md#demos)
  - [arrows](demos-arrow---arrows.md#arrows)
  - [counters](demos-count---counters.md#counters)
  - [curly](demos-curly---curly.md#curly)
  - [explosion](demos-explo---explosion.md#explosion)
  - [fields](demos-field---fields.md#fields)
  - [fourd](demos-fourd---fourd.md#fourd)
  - [gravity](demos-gravi---gravity.md#gravity)
  - [helloworld](demos-hello---helloworld.md#helloworld)
  - [rain](demos-rain---rain.md#rain)
  - [relativity](demos-relat---relativity.md#relativity)
  - [shaders](demos-shade---shaders.md#shaders)
- [generation](gener---generation.md#generation)
  - [gendoc](gener-gendo---gendoc.md#gendoc)
- [geonodes](geono---geonodes.md#geonodes)
  - [geonodes](geono-geono---geonodes.md#geonodes)
  - [gnmath](geono-gnmat---gnmath.md#gnmath)
  - [Attribute](geono-attribute.md#attribute)
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
  - [GeoBase](geono-geobase.md#geobase)
  - [Geometry](geono-geometry.md#geometry)
  - [Group](geono-group.md#group)
  - [GroupF](geono-groupf.md#groupf)
  - [Image](geono-image.md#image)
  - [Instance](geono-instance.md#instance)
  - [Instances](geono-instances.md#instances)
  - [Integer](geono-integer.md#integer)
  - [IntFloat](geono-intfloat.md#intfloat)
  - [Layout](geono-layout.md#layout)
  - [Material](geono-material.md#material)
  - [Matrix](geono-matrix.md#matrix)
  - [Menu](geono-menu.md#menu)
  - [Mesh](geono-mesh.md#mesh)
  - [nd](geono-nd.md#nd)
  - [Node](geono-node.md#node)
  - [NodeCache](geono-nodecache.md#nodecache)
  - [Object](geono-object.md#object)
  - [Point](geono-point.md#point)
  - [Repeat](geono-repeat.md#repeat)
  - [Rotation](geono-rotation.md#rotation)
  - [Simulation](geono-simulation.md#simulation)
  - [Socket](geono-socket.md#socket)
  - [Spline](geono-spline.md#spline)
  - [SplinePoint](geono-splinepoint.md#splinepoint)
  - [String](geono-string.md#string)
  - [Texture](geono-texture.md#texture)
  - [TextureRoot](geono-textureroot.md#textureroot)
  - [Tree](geono-tree.md#tree)
  - [Vector](geono-vector.md#vector)
  - [Vertex](geono-vertex.md#vertex)
  - [Volume](geono-volume.md#volume)
  - [Zone](geono-zone.md#zone)
- [macros](macro---macros.md#macros)
  - [demos](macro-demos---demos.md#demos)
  - [generation](macro-gener---generation.md#generation)
  - [geonodes](macro-geono---geonodes.md#geonodes)
  - [shadernodes](macro-shade1---shadernodes.md#shadernodes)
  - [double_integrals](macro---macros.md#double_integrals)
  - [impulsion](macro---macros.md#impulsion)
  - [integrals](macro---macros.md#integrals)
  - [solidify](macro---macros.md#solidify)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)
- [shadernodes](shade3---shadernodes.md#shadernodes)
  - [shaderclass](shade3-shade---shaderclass.md#shaderclass)
  - [shadernodes](shade3-shade1---shadernodes.md#shadernodes)
  - [staticclass](shade3-stati---staticclass.md#staticclass)

## Modules



- [demos](demos---demos.md#demos)
- [generation](gener---generation.md#generation)
- [geonodes](geono---geonodes.md#geonodes)
- [macros](macro---macros.md#macros)
- [shadernodes](shade3---shadernodes.md#shadernodes)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>

## Miscellaneous



- [Cross Reference](cross_reference.md#cross-reference)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>