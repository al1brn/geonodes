# geonodes

> Scripting nodes

$ DOC toc_max_depth = 1

### Initialize a tree

- [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) : scripting nodes starts by instantianting a [Tree](tree.md#tree)
- [Break](break.md#break) : exiting from a tree context can be done by raising this exception

### Create nodes

- [Node](node.md#node) : base class to create any node in a tree
- [Group](group.md#group) : create a <*Node Group> node
- [G](g.md#g) : a different way to create a <*Node Group> node
- [Layout](layout.md#layout) : to place nodes in a frame
- [Panel](panel.md#panel) : to place inputs into a panel
- Specific node : [ColorRamp](core-color.md#colorramp)

### Libraries

- [gnmath](gnmath.md#gnmath) : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- [nd](generated.md#nd) (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- [snd](generated.md#snd) (for _shader nodes_) : same as [nd](generated.md#nd) for shader node

### Sockets

Rather than using [Node](node.md#node) class, scripting nodes is done by using [Socket](core-socket.md#socket) classes:

- Data sockets:
  - [Attributes](core-color.md#attribute):
    - [Boolean](core-gener-boole-boolean.md#boolean)
    - [Integer](core-gener-integ-integer.md#integer)
    - [Float](core-gener-float-float.md#float)
    - [Color](core-gener-color-color.md#color)
    - [Vector](core-gener-vecto-vector.md#vector)
    - [Rotation](core-gener-rotat-rotation.md#rotation)
    - [Matrix](core-gener-matri-matrix.md#matrix)
  - [String](core-gener-strin-string.md#string)
  - [Menu](core-gener-menu-menu.md#menu)
- Blender resources:
  - [Collection](core-gener-colle-collection.md#collection)
  - [Object](core-gener-objec-object.md#object)
  - [Image](core-gener-image-image.md#image)
  - [Material](core-gener-mater-material.md#material)
  - [Texture](core-gener-textu-texture.md#texture)
- [Geometry](core-gener-geome-geometry.md#geometry) socket:
  - [Mesh](core-gener-mesh-mesh.md#mesh)
  - [Curve](core-gener-curve-curve.md#curve)
  - [GreasePencil](greasepencil.md#greasepencil)
  - [Cloud](core-gener-cloud-cloud.md#cloud)
  - [Instances](core-gener-insta-instances.md#instances)
  - [Volume](volume.md#volume)
- Shaders specific:
  - [Shader](core-gener-shade-shader.md#shader)
  - [VolumeShader](core-gener-volum-volumeshader.md#volumeshader)

#### Domains

Geometries have specific [Domain](domain.md#domain):
- [Mesh](core-gener-mesh-mesh.md#mesh) :
  - [Vertex](vertex.md#vertex) : property [Impossible to find the section 'points' in page 'Mesh'](core-gener-mesh-mesh.md#mesh)
  - [Edge](edge.md#edge) : property [Impossible to find the section 'edges' in page 'Mesh'](core-gener-mesh-mesh.md#mesh)
  - [Face](face.md#face) : property [Impossible to find the section 'faces' in page 'Mesh'](core-gener-mesh-mesh.md#mesh)
  - [Corner](corner.md#corner) : property [Impossible to find the section 'corners' in page 'Mesh'](core-gener-mesh-mesh.md#mesh)
- [Curve](core-gener-curve-curve.md#curve) :
  - [SplinePoint](splinepoint.md#splinepoint) : property [Impossible to find the section 'points' in page 'Curve'](core-gener-curve-curve.md#curve)
  - [Spline](spline.md#spline) : property [Impossible to find the section 'splines' in page 'Curve'](core-gener-curve-curve.md#curve)
- [GreasePencil](greasepencil.md#greasepencil) :
  - [Layer](layer.md#layer) : property [Impossible to find the section 'layers' in page 'GreasePencil'](greasepencil.md#greasepencil)
- [Cloud](core-gener-cloud-cloud.md#cloud) :
  - [CloudPoint](cloudpoint.md#cloudpoint) : property [Impossible to find the section 'points' in page 'Cloud'](core-gener-cloud-cloud.md#cloud)
- [Instances](core-gener-insta-instances.md#instances) :
  - [Instance](instance.md#instance) : property [Impossible to find the section 'insts' in page 'Instances'](core-gener-insta-instances.md#instances)

#### Demos
- Of course, start with [page 'demos' not found in '!demos#helloworld']()

#### Cross reference

- [Cross Reference](cross_reference.md#cross-reference) : to see how each Geometry Node can be scripted
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference) : to see how each Shader Node can be scripted

## Content

- [core](core.md#core)
  - [generated](generated.md#generated)
  - [Boolean](core-boolean.md#boolean)
  - [Break](break.md#break)
  - [Bundle](core-bundle.md#bundle)
  - [Closure](core-closure.md#closure)
  - [Cloud](core-cloud.md#cloud)
  - [CloudPoint](cloudpoint.md#cloudpoint)
  - [Collection](core-collection.md#collection)
  - [Color](core-color.md#color)
  - [ColorRamp](colorramp.md#colorramp)
  - [Corner](corner.md#corner)
  - [Curve](core-curve.md#curve)
  - [Domain](domain.md#domain)
  - [Edge](edge.md#edge)
  - [Face](face.md#face)
  - [Float](core-float.md#float)
  - [Font](core-font.md#font)
  - [G](g.md#g)
  - [Geometry](core-geometry.md#geometry)
  - [GeoNodes](geonodes.md#geonodes)
  - [GreasePencil](greasepencil.md#greasepencil)
  - [Group](group.md#group)
  - [Image](core-image.md#image)
  - [Input](input.md#input)
  - [Instance](instance.md#instance)
  - [Instances](core-instances.md#instances)
  - [Integer](core-integer.md#integer)
  - [Layer](layer.md#layer)
  - [Layout](layout.md#layout)
  - [Material](core-material.md#material)
  - [Matrix](core-matrix.md#matrix)
  - [Menu](core-menu.md#menu)
  - [Mesh](core-mesh.md#mesh)
  - [Node](node.md#node)
  - [Object](core-object.md#object)
  - [Panel](panel.md#panel)
  - [Point](point.md#point)
  - [Rotation](core-rotation.md#rotation)
  - [Shader](core-shader.md#shader)
  - [ShaderNodes](shadernodes.md#shadernodes)
  - [Socket](core-socket.md#socket)
  - [Socket](core-socket.md#socket)
  - [Socket](core-socket.md#socket)
  - [Spline](spline.md#spline)
  - [SplinePoint](splinepoint.md#splinepoint)
  - [String](core-string.md#string)
  - [Texture](core-texture.md#texture)
  - [Tree](tree.md#tree)
  - [Vector](core-vector.md#vector)
  - [Vertex](vertex.md#vertex)
  - [Volume](volume.md#volume)
  - [VolumeShader](core-volumeshader.md#volumeshader)
  - [check_enum_arg](core.md#check_enum_arg)
  - [check_zones](core.md#check_zones)
  - [color_ramp_set_stops](core.md#color_ramp_set_stops)
  - [del_tree](core.md#del_tree)
  - [ensure_uniques](core.md#ensure_uniques)
  - [fed_nodes](core.md#fed_nodes)
  - [feeding_nodes](core.md#feeding_nodes)
  - [find_snake_case_name](core.md#find_snake_case_name)
  - [get_data_type_from_argument](core.md#get_data_type_from_argument)
  - [get_enum_param_users](core.md#get_enum_param_users)
  - [get_items_socket_type](core.md#get_items_socket_type)
  - [get_tree](core.md#get_tree)
  - [repeat](core.md#repeat)
  - [request_empty](core.md#request_empty)
  - [simulation](core.md#simulation)
  - [str_to_color_tuple](core.md#str_to_color_tuple)
  - [zone_inner_nodes](core.md#zone_inner_nodes)
- [Cross Reference](cross_reference.md#cross-reference)
- [generation](generation.md#generation)
  - [gendoc](gendoc.md#gendoc)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)

## Modules



- [core](core.md#core)
- [generation](generation.md#generation)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>

## Miscellaneous



- [Cross Reference](cross_reference.md#cross-reference)
- [Shader Cross Reference](shader_cross_reference.md#shader-cross-reference)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geonodes](index.md#geonodes) :black_small_square: [Content](index.md#content) :black_small_square: [geonodes](index.md#geonodes)</sub>