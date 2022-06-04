
# Class Geometry

> Inherits from: ***dsock.Geometry***

## Static methods



- is_viewport : is_viewport (Boolean)



## Properties



- bound_box : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
- components : Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]



## Attribute capture



- capture_ID : ID (Integer)
- capture_index : index (Integer)
- capture_normal : normal (Vector)
- capture_position : position (Vector)
- capture_radius : radius (Float)



## Attributes



- ID : Integer = capture_ID(domain='POINT')
- index : Integer = capture_index(domain='POINT')
- normal : Vector = capture_normal(domain='FACE')
- position : Vector = capture_position(domain='POINT')
- radius : Float = capture_radius(domain='POINT')



## Methods



- attribute_domain_size : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
- attribute_remove : geometry (Geometry)
- components : Sockets      [selection (Geometry), inverted (Geometry)]
- convex_hull : convex_hull (Geometry)
- join : geometry (Geometry)
- proximity : Sockets      [position (Vector), distance (Float)]
- switch : output (Geometry)
- to_instance : instances (Instances)
- transfer_boolean : attribute (Boolean)
- transfer_color : attribute (Color)
- transfer_float : attribute (Float)
- transfer_integer : attribute (Integer)
- transfer_vector : attribute (Vector)



## Stacked methods



- delete_geometry : Geometry
- merge_by_distance : Geometry
- realize_instances : Geometry
- replace_material : Geometry
- scale_elements : Geometry
- set_ID : Geometry
- set_material : Geometry
- set_material_index : Geometry
- set_position : Geometry
- set_shade_smooth : Geometry
- transform : Geometry


