
# API structure

## Tree

- [Tree](api/Tree.md)
- [Trees](api/Trees.md)

## Root for types

- [DataSocket](api/DataSocket.md)

## Basic types

- [Boolean](api/Boolean.md)
- [Integer](api/Integer.md)
- [Float](api/Float.md)
- [Vector](api/Vector.md)
- [Color](api/Color.md)
- [String](api/String.md)

## Geometry types

The geometry classes are:
- [Mesh](api/Mesh.md)
- [Curve](api/Curve.md)
- [Points](api/Points.md)
- [Instances](api/Instances.md)
- [Volume](api/Volume.md)

## Domain types

In geometry nodes, attributes refer to [domains](https://al1brn.github.io/geonodes/domains.html) such as Point, Corner, Face, Spline... 

**geonodes** implement [domains](https://al1brn.github.io/geonodes/domains.html) as properties of geometry classes.
- Mesh
  - verts [Vertex](api/Vertex.md)
  - faces [Face](api/Face.md)
  - edges [Edge](api/Edge.md)
  - corners [Corner](api/Corner.md)
- Curve
  - points [ControlPoint]api/ControlPoint.md)
  - spline [Spline](api/Spline.md)
- Points cloud
  - points [CloudPoint](api/CloudPoint.md)
- Instances
  - inst [Instance](api/Instance.md)

## Blender types

- [Collection](api/Collection.md)
- [Object](api/Object.md)
- [Texture](api/Texture.md)
- [Image](api/Image.md)
- [Material](api/Material.md)





