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

- [Cloud](geono-geome-cloud.md#cloud)
  - [FromCurve](geono-geome-cloud.md#fromcurve)
  - [FromInstances](geono-geome-cloud.md#frominstances)
  - [FromMesh](geono-geome-cloud.md#frommesh)
  - [Points](geono-geome-cloud.md#points)
  - [to_curves](geono-geome-cloud.md#to_curves)
  - [to_vertices](geono-geome-cloud.md#to_vertices)
  - [to_volume](geono-geome-cloud.md#to_volume)
- [constants](geono-geome-const---constants.md#constants)
- [Curve](geono-geome-curve.md#curve)
  - [length](geono-geome-curve.md#length)
  - [radius](geono-geome-curve.md#radius)
  - [tilt](geono-geome-curve.md#tilt)
  - [Arc](geono-geome-curve.md#arc)
  - [BezierSegment](geono-geome-curve.md#beziersegment)
  - [Circle](geono-geome-curve.md#circle)
  - [curve_of_point](geono-geome-curve.md#curve_of_point)
  - [deform_on_surface](geono-geome-curve.md#deform_on_surface)
  - [endpoint_selection](geono-geome-curve.md#endpoint_selection)
  - [fill](geono-geome-curve.md#fill)
  - [fillet](geono-geome-curve.md#fillet)
  - [FromEdgePaths](geono-geome-curve.md#fromedgepaths)
  - [FromMesh](geono-geome-curve.md#frommesh)
  - [FromPoints](geono-geome-curve.md#frompoints)
  - [interpolate](geono-geome-curve.md#interpolate)
  - [Kite](geono-geome-curve.md#kite)
  - [Line](geono-geome-curve.md#line)
  - [offset_point_in_curve](geono-geome-curve.md#offset_point_in_curve)
  - [Parallelogram](geono-geome-curve.md#parallelogram)
  - [Points](geono-geome-curve.md#points)
  - [points_of_curve](geono-geome-curve.md#points_of_curve)
  - [QuadraticBezier](geono-geome-curve.md#quadraticbezier)
  - [Quadrilateral](geono-geome-curve.md#quadrilateral)
  - [Rectangle](geono-geome-curve.md#rectangle)
  - [resample](geono-geome-curve.md#resample)
  - [reverse](geono-geome-curve.md#reverse)
  - [sample](geono-geome-curve.md#sample)
  - [set_normal](geono-geome-curve.md#set_normal)
  - [set_normal_free](geono-geome-curve.md#set_normal_free)
  - [set_normal_z_up](geono-geome-curve.md#set_normal_z_up)
  - [Spiral](geono-geome-curve.md#spiral)
  - [Star](geono-geome-curve.md#star)
  - [subdivide](geono-geome-curve.md#subdivide)
  - [to_mesh](geono-geome-curve.md#to_mesh)
  - [to_points](geono-geome-curve.md#to_points)
  - [Trapezoid](geono-geome-curve.md#trapezoid)
  - [trim](geono-geome-curve.md#trim)
  - [trim_factor](geono-geome-curve.md#trim_factor)
  - [trim_length](geono-geome-curve.md#trim_length)
- [Geometry](geono-geome-geometry.md#geometry)
  - [bounding_box](geono-geome-geometry.md#bounding_box)
  - [convex_hull](geono-geome-geometry.md#convex_hull)
  - [curve](geono-geome-geometry.md#curve)
  - [id](geono-geome-geometry.md#id)
  - [instances](geono-geome-geometry.md#instances)
  - [material_index](geono-geome-geometry.md#material_index)
  - [mesh](geono-geome-geometry.md#mesh)
  - [point_cloud](geono-geome-geometry.md#point_cloud)
  - [position](geono-geome-geometry.md#position)
  - [separate_components](geono-geome-geometry.md#separate_components)
  - [volume](geono-geome-geometry.md#volume)
  - [index_of_nearest](geono-geome-geometry.md#index_of_nearest)
  - [join](geono-geome-geometry.md#join)
  - [merge_by_distance](geono-geome-geometry.md#merge_by_distance)
  - [raycast](geono-geome-geometry.md#raycast)
  - [remove_named_attribute](geono-geome-geometry.md#remove_named_attribute)
  - [replace_material](geono-geome-geometry.md#replace_material)
  - [set_id](geono-geome-geometry.md#set_id)
  - [set_material](geono-geome-geometry.md#set_material)
  - [set_position](geono-geome-geometry.md#set_position)
  - [set_shade_smooth](geono-geome-geometry.md#set_shade_smooth)
  - [to_instance](geono-geome-geometry.md#to_instance)
  - [transform](geono-geome-geometry.md#transform)
  - [viewer](geono-geome-geometry.md#viewer)
- [Instances](geono-geome-instances.md#instances)
  - [FromGeometry](geono-geome-instances.md#fromgeometry)
  - [FromString](geono-geome-instances.md#fromstring)
  - [on_points](geono-geome-instances.md#on_points)
  - [realize](geono-geome-instances.md#realize)
  - [rotate](geono-geome-instances.md#rotate)
  - [scale](geono-geome-instances.md#scale)
  - [to_points](geono-geome-instances.md#to_points)
  - [translate](geono-geome-instances.md#translate)
- [Mesh](geono-geome-mesh.md#mesh)
  - [island](geono-geome-mesh.md#island)
  - [island_count](geono-geome-mesh.md#island_count)
  - [island_index](geono-geome-mesh.md#island_index)
  - [boolean](geono-geome-mesh.md#boolean)
  - [Circle](geono-geome-mesh.md#circle)
  - [Cone](geono-geome-mesh.md#cone)
  - [Cube](geono-geome-mesh.md#cube)
  - [Cylinder](geono-geome-mesh.md#cylinder)
  - [difference](geono-geome-mesh.md#difference)
  - [Disk](geono-geome-mesh.md#disk)
  - [distribute_points_on_faces](geono-geome-mesh.md#distribute_points_on_faces)
  - [dual](geono-geome-mesh.md#dual)
  - [FromCurve](geono-geome-mesh.md#fromcurve)
  - [FromPoints](geono-geome-mesh.md#frompoints)
  - [FromVolume](geono-geome-mesh.md#fromvolume)
  - [Grid](geono-geome-mesh.md#grid)
  - [IcoSphere](geono-geome-mesh.md#icosphere)
  - [intersect](geono-geome-mesh.md#intersect)
  - [Line](geono-geome-mesh.md#line)
  - [LineOffset](geono-geome-mesh.md#lineoffset)
  - [LineTo](geono-geome-mesh.md#lineto)
  - [pack_uv_islands](geono-geome-mesh.md#pack_uv_islands)
  - [Plane](geono-geome-mesh.md#plane)
  - [sample_nearest_surface](geono-geome-mesh.md#sample_nearest_surface)
  - [sample_uv_surface](geono-geome-mesh.md#sample_uv_surface)
  - [subdivide](geono-geome-mesh.md#subdivide)
  - [subdivision_surface](geono-geome-mesh.md#subdivision_surface)
  - [to_curve](geono-geome-mesh.md#to_curve)
  - [to_volume](geono-geome-mesh.md#to_volume)
  - [triangulate](geono-geome-mesh.md#triangulate)
  - [union](geono-geome-mesh.md#union)
  - [UVSphere](geono-geome-mesh.md#uvsphere)
  - [uv_unwrap](geono-geome-mesh.md#uv_unwrap)
- [utils](geono-geome-utils---utils.md#utils)
  - [constants](geono-geome-utils-const---constants.md#constants)
  - [del_tree](geono-geome-utils---utils.md#del_tree)
  - [get_tree](geono-geome-utils---utils.md#get_tree)
- [Volume](geono-geome-volume.md#volume)
  - [Cube](geono-geome-volume.md#cube)
  - [distribute_grid](geono-geome-volume.md#distribute_grid)
  - [distribute_points](geono-geome-volume.md#distribute_points)
  - [distribute_random](geono-geome-volume.md#distribute_random)
  - [FromMesh](geono-geome-volume.md#frommesh)
  - [FromPoints](geono-geome-volume.md#frompoints)
  - [to_mesh](geono-geome-volume.md#to_mesh)
  - [to_mesh_amount](geono-geome-volume.md#to_mesh_amount)
  - [to_mesh_grid](geono-geome-volume.md#to_mesh_grid)
  - [to_mesh_size](geono-geome-volume.md#to_mesh_size)

## Modules



- [constants](geono-geome-const---constants.md#constants)
- [utils](geono-geome-utils---utils.md#utils)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass) :black_small_square: [Content](geono-geome---geometryclass.md#content) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass)</sub>

## Classes



- [Cloud](geono-geome-cloud.md#cloud)
- [Curve](geono-geome-curve.md#curve)
- [Geometry](geono-geome-geometry.md#geometry)
- [Instances](geono-geome-instances.md#instances)
- [Mesh](geono-geome-mesh.md#mesh)
- [Volume](geono-geome-volume.md#volume)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass) :black_small_square: [Content](geono-geome---geometryclass.md#content) :black_small_square: [geometryclass](geono-geome---geometryclass.md#geometryclass)</sub>