# geonodes

> Scripting nodes


### Tree

Scripting nodes starts by instantianting a [Tree](geono-tree.md#tree), either a [Geometry nodes tree](geono-geono-geonodes.md#geonodes) or
a [Shader nodes tree](shade-shade1-shadernodes.md#shadernodes):

``` python
with GeoNodes("Geometry Nodes"):
    pass
```

Exiting from a tree context can be done by raising the [Break](geono-break.md#break) exception.

### Node class

Once the current tree instantiated, nodes can be created by instancianting a [Node](geono-node.md#node) class, for instance:

``` python
with GeoNodes("Geometry Nodes"):
    node = Node('Set Position', {'Geometry': ..., 'Selection': ..., 'Offset': ...})
    result = node.geometry
```

#### Special nodes

[Group](geono-group.md#group) is used to call a group. [GroupF](geono-groupf.md#groupf) does the same by exposing the **snake_name** name of
the called group.

Use [Layout](geono-layout.md#layout) class to group nodes in a Layout:

``` python
with Layout("This a description"):
    # Nodes created in the context blocks are placed in the layout
    pass
```

#### Zones

Zones are create using [Repeat](geono-zones-repeat.md#repeat) and [Simulation](geono-zones-simulation.md#simulation).

#### nd et snd classes

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

``` python
geometry = Geometry()
# Create a 'Set Position' node by calling the method of Geometry
moved_geometry = geometry.set_position(...)
```

#### Domains

Geometries have specific [Domain](geono-domain.md#domain):
- [Vertex](geono-vertex.md#vertex) ([Mesh](geono-mesh.md#mesh) [impossible to find the section 'points' in page 'Mesh'](geono-mesh.md#mesh) property)
- [Edge](geono-edge.md#edge)  ([Mesh](geono-mesh.md#mesh) [impossible to find the section 'edges' in page 'Mesh'](geono-mesh.md#mesh) property)
- [Face](geono-face.md#face)  ([Mesh](geono-mesh.md#mesh) [impossible to find the section 'faces' in page 'Mesh'](geono-mesh.md#mesh) property)
- [Corner](geono-corner.md#corner)  ([Mesh](geono-mesh.md#mesh) [impossible to find the section 'corners' in page 'Mesh'](geono-mesh.md#mesh) property)
- [SplinePoint](geono-splinepoint.md#splinepoint) ([Curve](geono-curve.md#curve) [impossible to find the section 'points' in page 'Curve'](geono-curve.md#curve) property)
- [Spline](geono-spline.md#spline) ([Curve](geono-curve.md#curve) [impossible to find the section 'splines' in page 'Curve'](geono-curve.md#curve) property)
- [CloudPoint](geono-cloudpoint.md#cloudpoint) ([Cloud](geono-cloud.md#cloud) [impossible to find the section 'points' in page 'Cloud'](geono-cloud.md#cloud) property)
- [Instance](geono-instance.md#instance) ([Instances](geono-instances.md#instances) [impossible to find the section 'insts' in page 'Instances'](geono-instances.md#instances) property)

> [!NOTE]
> Domains are never instancied directly but by their geometry.

``` python
# A Mesh is instantiated with four domains
cube = Mesh.Cube()
# Extrusion of faces
extruded_cube = cube.faces.extrude()
```

#### maths

The module [gnmath](geono-gnmat---gnmath.md#gnmath) provides math functions and be uses as standard python **math** library.

## Content

- [Cross Reference](cross_reference.md#cross-reference)
- [geonodes](geono---geonodes.md#geonodes)
  - [geonodes](geono-geono---geonodes.md#geonodes)
  - [gnmath](geono-gnmat---gnmath.md#gnmath)
  - [zones](geono-zones---zones.md#zones)
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
  - [Mesh](geono-mesh.md#mesh)
  - [nd](geono-nd.md#nd)
  - [Node](geono-node.md#node)
  - [Object](geono-object.md#object)
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

- [Cross Reference](cross_reference.md#cross-reference)