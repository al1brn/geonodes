# geonodes

> Scripting nodes


### Initialize a tree

- [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) : scripting nodes starts by instantianting a [Tree](tree.md#tree)
- [Break](break.md#break) : exiting from a tree context can be done by raising this exception

### Create nodes

- [Node](node.md#node) : base class to create any node in a tree
- [Group](group.md#group) : create a <*Node Group> node
- [G](g.md#g) : a different way to create a <*Node Group> node
- [Layout](layout.md#layout) : to place nodes in a frame
- [Panel](panel.md#panel) : to place inputs into a panel
- [Repeat](repeat.md#repeat), [Simulation](simulation.md#simulation) and [ForEachElement](foreachelement.md#foreachelement): create a [Zone](zone.md#zone)
- Specific node : [ColorRamp](color.md#colorramp)

### Libraries

- [gnmath](gnmath.md#gnmath) : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- [nd](nd.md#nd) (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- [snd](snd.md#snd) (for _shader nodes_) : same as [nd](nd.md#nd) for shader node

### Sockets

Rather than using [Node](node.md#node) class, scripting nodes is done by using [Socket](socket.md#socket) classes:

- Data sockets:
  - [Attributes](color.md#attribute):
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
  - [GreasePencil](greasepencil.md#greasepencil)
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
- [GreasePencil](greasepencil.md#greasepencil) :
  - [Layer](layer.md#layer) : property [layers](greasepencil.md#layers)
- [Cloud](cloud.md#cloud) :
  - [CloudPoint](cloudpoint.md#cloudpoint) : property [points](cloud.md#points)
- [Instances](instances.md#instances) :
  - [Instance](instance.md#instance) : property [insts](instances.md#insts)

#### Demos
- Of course, start with [Hello World](helloworld.md#helloworld)

#### Cross reference

- [Cross Reference](cross_reference.md#cross-reference) : to see how each Geometry Node can be scripted
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference) : to see how each Shader Node can be scripted

## Content

- [core](core.md#core)
  - [generated](generated.md#generated)
  - [Boolean](boolean.md#boolean)
  - [Break](break.md#break)
  - [Cloud](cloud.md#cloud)
  - [CloudPoint](cloudpoint.md#cloudpoint)
  - [Collection](collection.md#collection)
  - [Color](color.md#color)
  - [ColorRamp](colorramp.md#colorramp)
  - [Corner](corner.md#corner)
  - [Curve](curve.md#curve)
  - [Domain](domain.md#domain)
  - [Edge](edge.md#edge)
  - [Face](face.md#face)
  - [Float](float.md#float)
  - [ForEachElement](foreachelement.md#foreachelement)
  - [G](g.md#g)
  - [Geometry](geometry.md#geometry)
  - [GeoNodes](geonodes.md#geonodes)
  - [GreasePencil](greasepencil.md#greasepencil)
  - [Group](group.md#group)
  - [GroupF](groupf.md#groupf)
  - [Image](image.md#image)
  - [Instance](instance.md#instance)
  - [Instances](instances.md#instances)
  - [Integer](integer.md#integer)
  - [Layer](layer.md#layer)
  - [Layout](layout.md#layout)
  - [Material](material.md#material)
  - [Matrix](matrix.md#matrix)
  - [Menu](menu.md#menu)
  - [Mesh](mesh.md#mesh)
  - [Node](node.md#node)
  - [Object](object.md#object)
  - [Panel](panel.md#panel)
  - [Point](point.md#point)
  - [Repeat](repeat.md#repeat)
  - [Rotation](rotation.md#rotation)
  - [Shader](shader.md#shader)
  - [ShaderNodes](shadernodes.md#shadernodes)
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
  - [VolumeShader](volumeshader.md#volumeshader)
  - [Zone](zone.md#zone)
  - [check_enum_arg](core.md#check_enum_arg)
  - [color_ramp_set_stops](core.md#color_ramp_set_stops)
  - [del_tree](core.md#del_tree)
  - [ensure_uniques](core.md#ensure_uniques)
  - [get_tree](core.md#get_tree)
- [Cross Reference](cross_reference.md#cross-reference)
- [demos](demos.md#demos)
  - [helloworld](helloworld.md#helloworld)
- [generation](generation.md#generation)
  - [gendoc](gendoc.md#gendoc)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)

## Modules



- [core](core.md#core)
- [demos](demos.md#demos)
- [generation](generation.md#generation)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>

## Miscellaneous



- [Cross Reference](cross_reference.md#cross-reference)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>