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
  - [verts](https://al1brn.github.io/geonodes/domains/vertex.html)
  - [faces](https://al1brn.github.io/geonodes/domains/face.html)
  - [edges](https://al1brn.github.io/geonodes/domains/edge.html)
  - [corners](https://al1brn.github.io/geonodes/domains/corner.html)
- Curve
  - [points](https://al1brn.github.io/geonodes/domains/controlpoint.html)
  - [splines](https://al1brn.github.io/geonodes/domains/spline.html)
- Points cloud
  - [points](https://al1brn.github.io/geonodes/domains/cloudpoint.html)
- Instances
  - [insts](https://al1brn.github.io/geonodes/domains/instance.html)
