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

- **C** : [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [CloudPoint](geono-geome-cloudpoint.md#cloudpoint) :black_small_square: [constants](geono-geome-const---constants.md#constants) :black_small_square: [Curve](geono-geome-curve.md#curve)
- **F** : [Face](geono-geome-face.md#face)
- **G** : [GeoBase](geono-geome-geobase.md#geobase) :black_small_square: [Geometry](geono-geome-geometry.md#geometry)
- **I** : [Instances](geono-geome-instances.md#instances)
- **M** : [Mesh](geono-geome-mesh.md#mesh)
- **P** : [Point](geono-geome-point.md#point)
- **S** : [SplinePoint](geono-geome-splinepoint.md#splinepoint)
- **U** : [utils](geono-geome-utils---utils.md#utils)
- **V** : [Volume](geono-geome-volume.md#volume)

## Modules



- [constants](geono-geome-const---constants.md#constants)
- [utils](geono-geome-utils---utils.md#utils)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass) :black_small_square: [Content](geono-geome---geometryclass.md#content) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass)</sub>

## Classes



- [Cloud](geono-geome-cloud.md#cloud)
- [CloudPoint](geono-geome-cloudpoint.md#cloudpoint)
- [Curve](geono-geome-curve.md#curve)
- [Face](geono-geome-face.md#face)
- [GeoBase](geono-geome-geobase.md#geobase)
- [Geometry](geono-geome-geometry.md#geometry)
- [Instances](geono-geome-instances.md#instances)
- [Mesh](geono-geome-mesh.md#mesh)
- [Point](geono-geome-point.md#point)
- [SplinePoint](geono-geome-splinepoint.md#splinepoint)
- [Volume](geono-geome-volume.md#volume)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass) :black_small_square: [Content](geono-geome---geometryclass.md#content) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass)</sub>