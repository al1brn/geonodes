**Domain** is the root class for:
- [Vertex](Vertex.md), node domain *'POINT'*
- [Edge](Edge.md), node domain *'EDGE'*
- [Face](Face.md), node domain *'FACE'*
- [Corner](Corner.md), node domain *'CORNER'*
- [ControlPoint](ControlPoint.md), node domain *'POINT'*
- [Spline](Spline.md), node domain *'SPLINE' (or *'CURVE'*)
- [CloudPoint](CloudPoint.md), node domain *'POINT'*
- [Instance](Instance.md), node domain *'INSTANCE'*


**Domain** provide mechanism to keep the context, by maintaining:
- the `selection`
- the node domain value in *'POINT'*, *'EDGE'*, *'FACE'*, *'CORNER'*, *'SPLINE'*, *'INSTANCE'*
- the geometry it as a domain of

> By keeping the context geometry, it is not necessary to explicitly create **Capture Attribute**.
  **Domain** class determines if it is necessary or not to create this node.

**Domains** are not initialized directly but by geometries:
- [Mesh](Mesh.md) initializes 4 domains:
  - `verts` property of type [Vertex](Vertex.md)
  - `edges` property of type [Edge](Edge.md)
  - `faces` property of type [Face](Face.md)
  - `corners` property of type [Corner](Corner.md)
- [Curve](Curve.md) initializes 2 domains:
  - `points` property of type [ControlPoint](ControlPoint.md)
  - `splines` property of type [Spline](Spline.md)
- [Instances](Instances.md) initializes 1 domain: 
  - `insts` property of type [Instance](Instance.md)
- [Points](Points.md) initializes 1 domain: 
  - `points` property of type [CloudPoint](CloudPoint.md)

> Note that the node domain *`POINT`* is used by 3 **Domains**.




