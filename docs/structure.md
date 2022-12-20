# API structure

## Scripting geometry

Geometry nodes are global functions operating on geometry passed through sockets.

**geonodes** presents the nodes sockets as classes and the nodes as methods.

Rather than thinking : _"What are the inputs of the 'Set Curve Tilt' node to change the tilt of spline #2?"_,
you take benefit of an object oriented language and simply write:

```python
curve.splines[2].tilt = 1
```

### Geometry classes

The geometry classes are:
- [Mesh](api/Mesh.md)
- [Curve](api/Curve.md)
- [Points](api/Points.md)
- [Instances](api/Instances.md)
- [Volume](api/Volume.md)

### Domains

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
