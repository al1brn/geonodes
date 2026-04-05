# geonodes : scripting Geometry Nodes

## Initialize a tree

- [GeoNodes](geonodes.md#geonodes) and [ShaderNodes](shadernodes.md#shadernodes) : scripting nodes starts by instantianting a [Tree](tree.md#tree)
- [Break](break.md#break) : exiting from a tree context can be done by raising this exception

## Create nodes

- [Layout](layout.md#layout) : to place nodes in a frame
- [Panel](panel.md#panel) : to place inputs into a panel
- [Group](group.md#group) : create a <*Node Group> node
- [G](g.md#g) : a different way to create a <*Node Group> node
- [Node](node.md#node) : base class to create any node in a tree (normally, no need to instantiate it directly)
- Specific node : [ColorRamp](color_ramp.md#colorramp)

## Libraries

- [gnmath](gnmath.md) : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- [nd](nd.md) (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- [snd](snd.md) (for _shader nodes_) : same as [nd](nd.md) for shader node

## Sockets

Rather than using [Node](node.md#node) class, scripting nodes is done by using [Socket](socket.md) classes:

- Data sockets:

  - Attributes: [Boolean](boolean.md), [Integer](integer.md), [Float](float.md), [Color](color.md), [Vector](vector.md), [Rotation](rotation.md), [Matrix](matrix.md)
  - Other: [String](string.md), [Menu](menu.md), [Bundle](bundle.md), [Closure](closure.md)

- Blender resources: [Collection](collection.md), [Object](object.md), [Image](image.md), [Material](material.md), 
  [Font](font.md), [Texture](texture.md)

- [Geometry](geometry.md) sockets: [Mesh](mesh.md), [Curve](curve.md), [GreasePencil](grease_pencil.md), [Cloud](cloud.md), [Instances](instances.md), [Volume](volume.md)
- Shaders specific: [Shader](shader.md), [VolumeShader](volume_shader.md)

### Domains

Geometries have specific [Domain](domain.md):

- [Mesh](mesh.md): [`Mesh.points`](vertex.md),  [`Mesh.edges`](edge.md), [`Mesh.faces`](face.md), [`Mesh.corners`](corner.md)
- [Curve](curve.md) : [`Curve.points`](spline_point.md),  [`Curve.splines`](spline.md)
- [Cloud](cloud.md) : [`Cloud.points`](cloud_point.md)
- [Instances](instances.md) : [`Instances.insts`](instance.md)
- [GreasePencil](grease_pencil.md) : [`GreasePencile.layers`](layer.md)
