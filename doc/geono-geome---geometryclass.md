# geometryclass

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : geometryclass
----------------------
- Implement geometry data socket

The Geometry base class for type 'GEOMETRY' has specialized children: Mesh, Curve, Cloud, Instances and Volume
each one implementing the node specific to their geometry.

In addition, nodes making use of a 'domain', parameter are implemented through Domain class.

``` python
# A node not specific to a geometry
Geometry().index_of_nearest()

# Nodes specific to geometries
Mesh().triangulate()
Curve().resample()

# Nodes requiring domain specification
Mesh().points.sample_index()
Mesh().faces.sample_index()
```

The domain specific to geometries are the followings:
    - Mesh:
        - points
        - faces
        - edges
        - corners
    - Curve:
        - points
        - splines
    - Instances
        - insts
    - Cloud
        - points
    - Volume

The components of a geometry can be separated with the following properties:

``` python
geo = Geometry()
mesh     = geo.mesh        # Node 'Separate Component', socket 'Mesh'
curve    = geo.curve       # Node 'Separate Component', socket 'Curve'
cloud    = geo.point_cloud # Node 'Separate Component', socket 'Point Cloud'
volume   = geo.volume      # Node 'Separate Component', socket 'Volume'
instance = geo.instances   # Node 'Separate Component', socket 'Instances'
```

classes
-------
- GeoBase       : Base class for Geometry and Domain
- Domain        : Domain base class
- Point         : POINT domain
- Vertex        : POINT domain for Mesh
- CloudPoint    : POINT domain for Points
- Face          : FACE domain
- Edge          : EDGE domain
- Corner        : CORNER domain
- Spline        : SPLINE domain
- Instance      : INSTANCE domain
- Geometry      : Socket of type 'Geometry'
- Mesh          : Subclass of Geometry specific to Mesh
- Curve         : Subclass of Geometry specific to Curve
- Instances     : Subclass of Geometry specific to Instances
- Cloud         : Subclass of Geometry specific to Cloud Points
- Volume        : Subclass of Geometry specific to Points

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- **C** : [Cloud](geono-geome-cloud.md) :black_small_square: [CloudPoint](geono-geome-cloudpoint.md) :black_small_square: [constants](geono-geome-const---constants.md) :black_small_square: [Corner](geono-geome-corner.md) :black_small_square: [Curve](geono-geome-curve.md)
- **D** : [Domain](geono-geome-domain.md)
- **E** : [Edge](geono-geome-edge.md)
- **F** : [Face](geono-geome-face.md)
- **G** : [GeoBase](geono-geome-geobase.md) :black_small_square: [Geometry](geono-geome-geometry.md)
- **I** : [Instance](geono-geome-instance.md) :black_small_square: [Instances](geono-geome-instances.md)
- **M** : [Mesh](geono-geome-mesh.md)
- **P** : [Point](geono-geome-point.md)
- **S** : [Spline](geono-geome-spline.md) :black_small_square: [SplinePoint](geono-geome-splinepoint.md)
- **U** : [utils](geono-geome-utils---utils.md)
- **V** : [Vertex](geono-geome-vertex.md) :black_small_square: [Volume](geono-geome-volume.md)

## Modules



- [constants](geono-geome-const---constants.md)
- [utils](geono-geome-utils---utils.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#geometryclass) :black_small_square: [Content](#content) :black_small_square: [geometryclass](geono-geome---geometryclass.md)</sub>

## Classes



- [Cloud](geono-geome-cloud.md)
- [CloudPoint](geono-geome-cloudpoint.md)
- [Corner](geono-geome-corner.md)
- [Curve](geono-geome-curve.md)
- [Domain](geono-geome-domain.md)
- [Edge](geono-geome-edge.md)
- [Face](geono-geome-face.md)
- [GeoBase](geono-geome-geobase.md)
- [Geometry](geono-geome-geometry.md)
- [Instance](geono-geome-instance.md)
- [Instances](geono-geome-instances.md)
- [Mesh](geono-geome-mesh.md)
- [Point](geono-geome-point.md)
- [Spline](geono-geome-spline.md)
- [SplinePoint](geono-geome-splinepoint.md)
- [Vertex](geono-geome-vertex.md)
- [Volume](geono-geome-volume.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#geometryclass) :black_small_square: [Content](#content) :black_small_square: [geometryclass](geono-geome---geometryclass.md)</sub>