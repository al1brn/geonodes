# Nodes

## Alphabetical order:

| node | class | method name |
|------|-------|-------------|
| [Accumulate Field](#nodes) | [Domain](Domain.md) | [rotate_euler](Domain.md#rotate_euler) |
| [Align Euler to Vector](#nodes) | [Rotation](Rotation.md) | [rotate_euler](Rotation.md#rotate_euler) |
|      | [Vector](Vector.md) | [rotate_euler](Vector.md#rotate_euler) |
|      | [function](function.md) | [rotate_euler](function.md#rotate_euler) |
| [Arc](#nodes) | [Curve](Curve.md) | - [Arc](Curve.md#Arc-classmethod)<br>- [ArcFromPoints](Curve.md#ArcFromPoints-classmethod)|
| [Attribute Statistic](#nodes) | [Domain](Domain.md) | [attribute_statistic](Domain.md#attribute_statistic) / [attribute_mean](Domain.md#attribute_mean) / [attribute_median](Domain.md#attribute_median) / [attribute_sum](Domain.md#attribute_sum) / [attribute_min](Domain.md#attribute_min) / [attribute_max](Domain.md#attribute_max) / [attribute_range](Domain.md#attribute_range) / [attribute_std](Domain.md#attribute_std) / [attribute_var](Domain.md#attribute_var) / |
|      | [Geometry](Geometry.md) | [attribute_var](Geometry.md#attribute_var) |
| [Bezier Segment](#nodes) | [Curve](Curve.md) | [attribute_var](Curve.md#attribute_var) |
| [Boolean](#nodes) | [Boolean](Boolean.md) | [attribute_var](Boolean.md#attribute_var) |
| [Boolean Math](#nodes) | [Boolean](Boolean.md) | [b_and](Boolean.md#b_and) / [b_or](Boolean.md#b_or) / [b_not](Boolean.md#b_not) / [nand](Boolean.md#nand) / [nor](Boolean.md#nor) / [xnor](Boolean.md#xnor) / [xor](Boolean.md#xor) / [imply](Boolean.md#imply) / [nimply](Boolean.md#nimply) / |
|      | [function](function.md) | [b_and](function.md#b_and) / [b_or](function.md#b_or) / [b_not](function.md#b_not) / [nand](function.md#nand) / [nor](function.md#nor) / [xnor](function.md#xnor) / [xor](function.md#xor) / [imply](function.md#imply) / [nimply](function.md#nimply) / |
| [Bounding Box](#nodes) | [Geometry](Geometry.md) | - [bounding_box](Geometry.md#bounding_box-property)<br>- [bounding_box_min](Geometry.md#bounding_box_min-property)<br>- [bounding_box_min](Geometry.md#bounding_box_min-property)|
| [Brick Texture](#nodes) | [Texture](Texture.md) | [bounding_box_min](Texture.md#bounding_box_min-property) |
| [Capture Attribute](#nodes) | [Domain](Domain.md) | [bounding_box_min](Domain.md#bounding_box_min-property) |
|      | [Geometry](Geometry.md) | - [capture_attribute](Geometry.md#capture_attribute)<br>- [capture_attribute_node](Geometry.md#capture_attribute_node)|
| [Checker Texture](#nodes) | [Texture](Texture.md) | [capture_attribute_node](Texture.md#capture_attribute_node) |
| [Clamp](#nodes) | [Float](Float.md) | - [clamp](Float.md#clamp)<br>- [clamp_min_max](Float.md#clamp_min_max)<br>- [clamp_range](Float.md#clamp_range)|
|      | [function](function.md) | - [clamp](function.md#clamp)<br>- [clamp_min_max](function.md#clamp_min_max)<br>- [clamp_range](function.md#clamp_range)|
| [Collection Info](#nodes) | [Geometry](Geometry.md) | [clamp_range](Geometry.md#clamp_range) |
| [Color](#nodes) | [Color](Color.md) | [clamp_range](Color.md#clamp_range) |
| [ColorRamp](#nodes) | [Float](Float.md) | [clamp_range](Float.md#clamp_range) |
|      | [function](function.md) | [clamp_range](function.md#clamp_range) |
| [Combine Color](#nodes) | [Color](Color.md) | - [RGB](Color.md#RGB-classmethod)<br>- [HSV](Color.md#HSV-classmethod)<br>- [HSL](Color.md#HSL-classmethod)|
|      | [function](function.md) | - [combine_rgb](function.md#combine_rgb)<br>- [combine_hsv](function.md#combine_hsv)<br>- [combine_hsl](function.md#combine_hsl)|
| [Combine XYZ](#nodes) | [Vector](Vector.md) | [combine_hsl](Vector.md#combine_hsl) |
| [Compare](#nodes) | [Color](Color.md) | [compare](Color.md#compare) / [darker](Color.md#darker) / [brighter](Color.md#brighter) / [equal](Color.md#equal) / [equal](Color.md#equal) / |
|      | [Float](Float.md) | [compare](Float.md#compare) / [less_than](Float.md#less_than) / [less_equal](Float.md#less_equal) / [greater_than](Float.md#greater_than) / [greater_equal](Float.md#greater_equal) / [equal](Float.md#equal) / [not_equal](Float.md#not_equal) / |
|      | [Integer](Integer.md) | [compare](Integer.md#compare) / [less_than](Integer.md#less_than) / [less_equal](Integer.md#less_equal) / [greater_than](Integer.md#greater_than) / [greater_equal](Integer.md#greater_equal) / [equal](Integer.md#equal) / [not_equal](Integer.md#not_equal) / |
|      | [String](String.md) | - [equal](String.md#equal)<br>- [not_equal](String.md#not_equal)|
|      | [Vector](Vector.md) | [compare](Vector.md#compare) / [elements_less_than](Vector.md#elements_less_than) / [elements_less_equal](Vector.md#elements_less_equal) / [elements_greater_than](Vector.md#elements_greater_than) / [elements_greater_equal](Vector.md#elements_greater_equal) / [elements_equal](Vector.md#elements_equal) / [elements_not_equal](Vector.md#elements_not_equal) / [length_less_than](Vector.md#length_less_than) / [length_less_equal](Vector.md#length_less_equal) / [length_greater_than](Vector.md#length_greater_than) / [length_greater_equal](Vector.md#length_greater_equal) / [length_equal](Vector.md#length_equal) / [length_not_equal](Vector.md#length_not_equal) / [average_less_than](Vector.md#average_less_than) / [average_less_equal](Vector.md#average_less_equal) / [average_greater_than](Vector.md#average_greater_than) / [average_greater_equal](Vector.md#average_greater_equal) / [average_equal](Vector.md#average_equal) / [average_not_equal](Vector.md#average_not_equal) / [dot_product_less_than](Vector.md#dot_product_less_than) / [dot_product_less_equal](Vector.md#dot_product_less_equal) / [dot_product_greater_than](Vector.md#dot_product_greater_than) / [dot_product_greater_equal](Vector.md#dot_product_greater_equal) / [dot_product_equal](Vector.md#dot_product_equal) / [dot_product_not_equal](Vector.md#dot_product_not_equal) / [direction_less_than](Vector.md#direction_less_than) / [direction_less_equal](Vector.md#direction_less_equal) / [direction_greater_than](Vector.md#direction_greater_than) / [direction_greater_equal](Vector.md#direction_greater_equal) / [direction_equal](Vector.md#direction_equal) / [direction_not_equal](Vector.md#direction_not_equal) / |
|      | [function](function.md) | [direction_not_equal](function.md#direction_not_equal) |
| [Cone](#nodes) | [Mesh](Mesh.md) | [direction_not_equal](Mesh.md#direction_not_equal) |
| [Convex Hull](#nodes) | [Geometry](Geometry.md) | [direction_not_equal](Geometry.md#direction_not_equal) |
| [Cube](#nodes) | [Mesh](Mesh.md) | [direction_not_equal](Mesh.md#direction_not_equal) |
| [Curve Circle](#nodes) | [Curve](Curve.md) | - [Circle](Curve.md#Circle-classmethod)<br>- [CircleFromPoints](Curve.md#CircleFromPoints-classmethod)|
| [Curve Handle Positions](#nodes) | [ControlPoint](ControlPoint.md) | - [handle_positions](ControlPoint.md#handle_positions)<br>- [left_handle_positions](ControlPoint.md#left_handle_positions-property)<br>- [right_handle_positions](ControlPoint.md#right_handle_positions-property)|
| [Curve Length](#nodes) | [Curve](Curve.md) | [right_handle_positions](Curve.md#right_handle_positions-property) |
| [Curve Line](#nodes) | [Curve](Curve.md) | - [Line](Curve.md#Line-classmethod)<br>- [LineDirection](Curve.md#LineDirection-classmethod)|
| [Curve of Point](#nodes) | [ControlPoint](ControlPoint.md) | [LineDirection](ControlPoint.md#LineDirection-classmethod) |
|      | [Curve](Curve.md) | [LineDirection](Curve.md#LineDirection-classmethod) |
| [Curve Tangent](#nodes) | [ControlPoint](ControlPoint.md) | [LineDirection](ControlPoint.md#LineDirection-classmethod) |
| [Curve Tilt](#nodes) | [ControlPoint](ControlPoint.md) | [LineDirection](ControlPoint.md#LineDirection-classmethod) |
| [Curve to Mesh](#nodes) | [Curve](Curve.md) | [LineDirection](Curve.md#LineDirection-classmethod) |
| [Curve to Points](#nodes) | [Curve](Curve.md) | - [to_points](Curve.md#to_points)<br>- [to_points_count](Curve.md#to_points_count)<br>- [to_points_length](Curve.md#to_points_length)<br>- [to_points_evaluated](Curve.md#to_points_evaluated)|
| [Cylinder](#nodes) | [Mesh](Mesh.md) | [to_points_evaluated](Mesh.md#to_points_evaluated) |
| [Deform Curves on Surface](#nodes) | [Curve](Curve.md) | [to_points_evaluated](Curve.md#to_points_evaluated) |
| [Delete Geometry](#nodes) | [Domain](Domain.md) | [to_points_evaluated](Domain.md#to_points_evaluated) |
|      | [Edge](Edge.md) | - [delete_all](Edge.md#delete_all)<br>- [delete_edges](Edge.md#delete_edges)<br>- [delete_faces](Edge.md#delete_faces)|
|      | [Face](Face.md) | - [delete_all](Face.md#delete_all)<br>- [delete_edges](Face.md#delete_edges)<br>- [delete_faces](Face.md#delete_faces)|
|      | [Geometry](Geometry.md) | [delete_faces](Geometry.md#delete_faces) |
|      | [Mesh](Mesh.md) | - [delete_all](Mesh.md#delete_all)<br>- [delete_edges](Mesh.md#delete_edges)<br>- [delete_faces](Mesh.md#delete_faces)|
|      | [Vertex](Vertex.md) | - [delete_all](Vertex.md#delete_all)<br>- [delete_edges](Vertex.md#delete_edges)<br>- [delete_faces](Vertex.md#delete_faces)|
| [Distribute Points in Volume](#nodes) | [Volume](Volume.md) | - [distribute_points](Volume.md#distribute_points)<br>- [distribute_points_random](Volume.md#distribute_points_random)<br>- [distribute_points_grid](Volume.md#distribute_points_grid)|
| [Distribute Points on Faces](#nodes) | [Face](Face.md) | - [distribute_points_random](Face.md#distribute_points_random)<br>- [distribute_points_poisson](Face.md#distribute_points_poisson)|
|      | [Mesh](Mesh.md) | [distribute_points_poisson](Mesh.md#distribute_points_poisson) |
| [Domain Size](#nodes) | [CloudPoint](CloudPoint.md) | [distribute_points_poisson](CloudPoint.md#distribute_points_poisson) |
|      | [ControlPoint](ControlPoint.md) | [distribute_points_poisson](ControlPoint.md#distribute_points_poisson) |
|      | [Corner](Corner.md) | [distribute_points_poisson](Corner.md#distribute_points_poisson) |
|      | [Curve](Curve.md) | - [domain_size](Curve.md#domain_size-property)<br>- [point_count](Curve.md#point_count-property)<br>- [spline_count](Curve.md#spline_count-property)|
|      | [Edge](Edge.md) | [spline_count](Edge.md#spline_count-property) |
|      | [Face](Face.md) | [spline_count](Face.md#spline_count-property) |
|      | [Geometry](Geometry.md) | [spline_count](Geometry.md#spline_count-property) |
|      | [Instance](Instance.md) | [spline_count](Instance.md#spline_count-property) |
|      | [Instances](Instances.md) | [spline_count](Instances.md#spline_count-property) |
|      | [Mesh](Mesh.md) | [domain_size](Mesh.md#domain_size-property) / [point_count](Mesh.md#point_count-property) / [face_count](Mesh.md#face_count-property) / [edge_count](Mesh.md#edge_count-property) / [corner_count](Mesh.md#corner_count-property) / |
|      | [Points](Points.md) | [corner_count](Points.md#corner_count-property) |
|      | [Spline](Spline.md) | [corner_count](Spline.md#corner_count-property) |
|      | [Vertex](Vertex.md) | [corner_count](Vertex.md#corner_count-property) |
| [Dual Mesh](#nodes) | [Mesh](Mesh.md) | [corner_count](Mesh.md#corner_count-property) |
| [Duplicate Elements](#nodes) | [Domain](Domain.md) | [corner_count](Domain.md#corner_count-property) |
|      | [Geometry](Geometry.md) | [corner_count](Geometry.md#corner_count-property) |
| [Edge Angle](#nodes) | [Edge](Edge.md) | - [angle](Edge.md#angle-property)<br>- [unsigned_angle](Edge.md#unsigned_angle-property)<br>- [signed_angle](Edge.md#signed_angle-property)|
| [Edge Neighbors](#nodes) | [Edge](Edge.md) | [signed_angle](Edge.md#signed_angle-property) |
| [Edge Paths to Curves](#nodes) | [Edge](Edge.md) | [signed_angle](Edge.md#signed_angle-property) |
|      | [Mesh](Mesh.md) | [signed_angle](Mesh.md#signed_angle-property) |
| [Edge Paths to Selection](#nodes) | [Mesh](Mesh.md) | [signed_angle](Mesh.md#signed_angle-property) |
| [Edge Vertices](#nodes) | [Edge](Edge.md) | - [vertices](Edge.md#vertices-property)<br>- [vertices_index](Edge.md#vertices_index-property)<br>- [vertices_position](Edge.md#vertices_position-property)|
| [Endpoint Selection](#nodes) | [ControlPoint](ControlPoint.md) | [vertices_position](ControlPoint.md#vertices_position-property) |
| [Extrude Mesh](#nodes) | [Edge](Edge.md) | [vertices_position](Edge.md#vertices_position-property) |
|      | [Face](Face.md) | [vertices_position](Face.md#vertices_position-property) |
|      | [Mesh](Mesh.md) | [vertices_position](Mesh.md#vertices_position-property) |
|      | [Vertex](Vertex.md) | [vertices_position](Vertex.md#vertices_position-property) |
| [Face Area](#nodes) | [Face](Face.md) | [vertices_position](Face.md#vertices_position-property) |
| [Face is Planar](#nodes) | [Face](Face.md) | [vertices_position](Face.md#vertices_position-property) |
|      | [Mesh](Mesh.md) | [vertices_position](Mesh.md#vertices_position-property) |
| [Face Neighbors](#nodes) | [Face](Face.md) | - [neighbors](Face.md#neighbors-property)<br>- [neighbors_vertex_count](Face.md#neighbors_vertex_count-property)<br>- [neighbors_face_count](Face.md#neighbors_face_count-property)|
| [Face Set Boundaries](#nodes) | [Face](Face.md) | [neighbors_face_count](Face.md#neighbors_face_count-property) |
|      | [Mesh](Mesh.md) | [neighbors_face_count](Mesh.md#neighbors_face_count-property) |
| [Field at Index](#nodes) | [Domain](Domain.md) | [neighbors_face_count](Domain.md#neighbors_face_count-property) |
|      | [Geometry](Geometry.md) | [neighbors_face_count](Geometry.md#neighbors_face_count-property) |
| [Fill Curve](#nodes) | [Curve](Curve.md) | - [fill](Curve.md#fill)<br>- [fill_triangles](Curve.md#fill_triangles)<br>- [fill_ngons](Curve.md#fill_ngons)|
| [Fillet Curve](#nodes) | [Curve](Curve.md) | - [fillet](Curve.md#fillet)<br>- [fillet_bezier](Curve.md#fillet_bezier)<br>- [fillet_poly](Curve.md#fillet_poly)|
| [Flip Faces](#nodes) | [Face](Face.md) | [fillet_poly](Face.md#fillet_poly) |
|      | [Mesh](Mesh.md) | [fillet_poly](Mesh.md#fillet_poly) |
| [Float Curve](#nodes) | [Float](Float.md) | [fillet_poly](Float.md#fillet_poly) |
| [Float to Integer](#nodes) | [Float](Float.md) | [to_integer](Float.md#to_integer) / [round](Float.md#round) / [floor](Float.md#floor) / [ceiling](Float.md#ceiling) / [truncate](Float.md#truncate) / |
| [Geometry Proximity](#nodes) | [Geometry](Geometry.md) | - [proximity](Geometry.md#proximity)<br>- [proximity_points](Geometry.md#proximity_points)<br>- [proximity_edges](Geometry.md#proximity_edges)<br>- [proximity_facess](Geometry.md#proximity_facess)|
| [Geometry to Instance](#nodes) | [Geometry](Geometry.md) | [proximity_facess](Geometry.md#proximity_facess) |
|      | [function](function.md) | [proximity_facess](function.md#proximity_facess) |
| [Gradient Texture](#nodes) | [Texture](Texture.md) | [gradient](Texture.md#gradient-staticmethod) / [gradient_linear](Texture.md#gradient_linear-staticmethod) / [gradient_quadratic](Texture.md#gradient_quadratic-staticmethod) / [gradient_easing](Texture.md#gradient_easing-staticmethod) / [gradient_diagonal](Texture.md#gradient_diagonal-staticmethod) / [gradient_spherical](Texture.md#gradient_spherical-staticmethod) / [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere-staticmethod) / [gradient_radial](Texture.md#gradient_radial-staticmethod) / |
| [Grid](#nodes) | [Mesh](Mesh.md) | [gradient_radial](Mesh.md#gradient_radial-staticmethod) |
| [Handle Type Selection](#nodes) | [ControlPoint](ControlPoint.md) | [handle_type_selection_node](ControlPoint.md#handle_type_selection_node) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / |
| [ID](#nodes) | [Domain](Domain.md) | [ID](Domain.md#ID) |
|      | [Geometry](Geometry.md) | [ID](Geometry.md#ID) |
| [Ico Sphere](#nodes) | [Mesh](Mesh.md) | [ico_sphere](Mesh.md#ico_sphere) |
| [Image Texture](#nodes) | [Image](Image.md) | [image_texture](Image.md#image_texture) |
|      | [Texture](Texture.md) | [image_texture](Texture.md#image_texture) |
| [Index](#nodes) | [Domain](Domain.md) | - [index](Domain.md#index-property)<br>- [domain_index](Domain.md#domain_index-property)|
|      | [Geometry](Geometry.md) | [domain_index](Geometry.md#domain_index-property) |
| [Instance on Points](#nodes) | [CloudPoint](CloudPoint.md) | [domain_index](CloudPoint.md#domain_index-property) |
|      | [ControlPoint](ControlPoint.md) | [domain_index](ControlPoint.md#domain_index-property) |
|      | [Curve](Curve.md) | [domain_index](Curve.md#domain_index-property) |
|      | [Instances](Instances.md) | - [InstanceOnPoints](Instances.md#InstanceOnPoints-classmethod)<br>- [on_points](Instances.md#on_points)|
|      | [Mesh](Mesh.md) | [on_points](Mesh.md#on_points) |
|      | [Points](Points.md) | [on_points](Points.md#on_points) |
|      | [Vertex](Vertex.md) | [on_points](Vertex.md#on_points) |
| [Instance Rotation](#nodes) | [Instance](Instance.md) | [on_points](Instance.md#on_points) |
|      | [Instances](Instances.md) | [on_points](Instances.md#on_points) |
| [Instance Scale](#nodes) | [Instance](Instance.md) | [on_points](Instance.md#on_points) |
|      | [Instances](Instances.md) | [on_points](Instances.md#on_points) |
| [Instances to Points](#nodes) | [Instance](Instance.md) | [on_points](Instance.md#on_points) |
|      | [Instances](Instances.md) | [on_points](Instances.md#on_points) |
| [Integer](#nodes) | [Integer](Integer.md) | [on_points](Integer.md#on_points) |
| [Is Shade Smooth](#nodes) | [Face](Face.md) | [on_points](Face.md#on_points) |
|      | [Mesh](Mesh.md) | [on_points](Mesh.md#on_points) |
| [Is Spline Cyclic](#nodes) | [Spline](Spline.md) | [on_points](Spline.md#on_points) |
| [Is Viewport](#nodes) | [Geometry](Geometry.md) | [on_points](Geometry.md#on_points) |
| [Join Geometry](#nodes) | [Geometry](Geometry.md) | [on_points](Geometry.md#on_points) |
|      | [function](function.md) | [on_points](function.md#on_points) |
| [Join Strings](#nodes) | [String](String.md) | [on_points](String.md#on_points) |
|      | [function](function.md) | [on_points](function.md#on_points) |
| [Magic Texture](#nodes) | [Texture](Texture.md) | [on_points](Texture.md#on_points) |
| [Map Range](#nodes) | [Float](Float.md) | [map_range](Float.md#map_range) / [map_range_linear](Float.md#map_range_linear) / [map_range_stepped](Float.md#map_range_stepped) / [map_range_smooth](Float.md#map_range_smooth) / [map_range_smoother](Float.md#map_range_smoother) / |
|      | [Vector](Vector.md) | [map_range](Vector.md#map_range) / [map_range_linear](Vector.md#map_range_linear) / [map_range_stepped](Vector.md#map_range_stepped) / [map_range_smooth](Vector.md#map_range_smooth) / [map_range_smoother](Vector.md#map_range_smoother) / |
| [Material](#nodes) | [Material](Material.md) | [map_range_smoother](Material.md#map_range_smoother) |
| [Material Index](#nodes) | [Domain](Domain.md) | [map_range_smoother](Domain.md#map_range_smoother) |
|      | [Geometry](Geometry.md) | [map_range_smoother](Geometry.md#map_range_smoother) |
| [Material Selection](#nodes) | [Domain](Domain.md) | [map_range_smoother](Domain.md#map_range_smoother) |
|      | [Geometry](Geometry.md) | [map_range_smoother](Geometry.md#map_range_smoother) |
| [Math](#nodes) | [Float](Float.md) | [add](Float.md#add) / [subtract](Float.md#subtract) / [sub](Float.md#sub) / [multiply](Float.md#multiply) / [mul](Float.md#mul) / [divide](Float.md#divide) / [div](Float.md#div) / [multiply_add](Float.md#multiply_add) / [mul_add](Float.md#mul_add) / [power](Float.md#power) / [pow](Float.md#pow) / [logarithm](Float.md#logarithm) / [log](Float.md#log) / [sqrt](Float.md#sqrt) / [inverse_sqrt](Float.md#inverse_sqrt) / [absolute](Float.md#absolute) / [abs](Float.md#abs) / [exponent](Float.md#exponent) / [exp](Float.md#exp) / [minimum](Float.md#minimum) / [min](Float.md#min) / [maximum](Float.md#maximum) / [max](Float.md#max) / [math_less_than](Float.md#math_less_than) / [math_greater_than](Float.md#math_greater_than) / [sign](Float.md#sign) / [math_compare](Float.md#math_compare) / [smooth_minimum](Float.md#smooth_minimum) / [smooth_maximum](Float.md#smooth_maximum) / [math_round](Float.md#math_round) / [math_floor](Float.md#math_floor) / [math_ceil](Float.md#math_ceil) / [math_truncate](Float.md#math_truncate) / [math_trunc](Float.md#math_trunc) / [fraction](Float.md#fraction) / [fact](Float.md#fact) / [modulo](Float.md#modulo) / [wrap](Float.md#wrap) / [snap](Float.md#snap) / [ping_pong](Float.md#ping_pong) / [sine](Float.md#sine) / [sin](Float.md#sin) / [cosine](Float.md#cosine) / [cos](Float.md#cos) / [tangent](Float.md#tangent) / [tan](Float.md#tan) / [arcsine](Float.md#arcsine) / [arcsin](Float.md#arcsin) / [arccosine](Float.md#arccosine) / [arccos](Float.md#arccos) / [arctangent](Float.md#arctangent) / [arctan](Float.md#arctan) / [arctan2](Float.md#arctan2) / [sinh](Float.md#sinh) / [cosh](Float.md#cosh) / [tanh](Float.md#tanh) / [to_radians](Float.md#to_radians) / [to_degrees](Float.md#to_degrees) / |
|      | [Integer](Integer.md) | [add](Integer.md#add) / [subtract](Integer.md#subtract) / [sub](Integer.md#sub) / [multiply](Integer.md#multiply) / [mul](Integer.md#mul) / [divide](Integer.md#divide) / [div](Integer.md#div) / [multiply_add](Integer.md#multiply_add) / [mul_add](Integer.md#mul_add) / [power](Integer.md#power) / [pow](Integer.md#pow) / [logarithm](Integer.md#logarithm) / [log](Integer.md#log) / [sqrt](Integer.md#sqrt) / [inverse_sqrt](Integer.md#inverse_sqrt) / [absolute](Integer.md#absolute) / [abs](Integer.md#abs) / [exponent](Integer.md#exponent) / [exp](Integer.md#exp) / [minimum](Integer.md#minimum) / [min](Integer.md#min) / [maximum](Integer.md#maximum) / [max](Integer.md#max) / [math_less_than](Integer.md#math_less_than) / [math_greater_than](Integer.md#math_greater_than) / [sign](Integer.md#sign) / [math_compare](Integer.md#math_compare) / [smooth_minimum](Integer.md#smooth_minimum) / [smooth_maximum](Integer.md#smooth_maximum) / [math_round](Integer.md#math_round) / [math_floor](Integer.md#math_floor) / [math_ceil](Integer.md#math_ceil) / [math_truncate](Integer.md#math_truncate) / [math_trunc](Integer.md#math_trunc) / [fraction](Integer.md#fraction) / [fact](Integer.md#fact) / [modulo](Integer.md#modulo) / [wrap](Integer.md#wrap) / [snap](Integer.md#snap) / [ping_pong](Integer.md#ping_pong) / [sine](Integer.md#sine) / [sin](Integer.md#sin) / [cosine](Integer.md#cosine) / [cos](Integer.md#cos) / [tangent](Integer.md#tangent) / [tan](Integer.md#tan) / [arcsine](Integer.md#arcsine) / [arcsin](Integer.md#arcsin) / [arccosine](Integer.md#arccosine) / [arccos](Integer.md#arccos) / [arctangent](Integer.md#arctangent) / [arctan](Integer.md#arctan) / [arctan2](Integer.md#arctan2) / [sinh](Integer.md#sinh) / [cosh](Integer.md#cosh) / [tanh](Integer.md#tanh) / [to_radians](Integer.md#to_radians) / [to_degrees](Integer.md#to_degrees) / |
|      | [function](function.md) | [math](function.md#math) / [add](function.md#add) / [subtract](function.md#subtract) / [sub](function.md#sub) / [multiply](function.md#multiply) / [mul](function.md#mul) / [divide](function.md#divide) / [div](function.md#div) / [multiply_add](function.md#multiply_add) / [mul_add](function.md#mul_add) / [power](function.md#power) / [logarithm](function.md#logarithm) / [log](function.md#log) / [sqrt](function.md#sqrt) / [inverse_sqrt](function.md#inverse_sqrt) / [absolute](function.md#absolute) / [abs](function.md#abs) / [exponent](function.md#exponent) / [exp](function.md#exp) / [minimum](function.md#minimum) / [min](function.md#min) / [maximum](function.md#maximum) / [max](function.md#max) / [math_less_than](function.md#math_less_than) / [math_greater_than](function.md#math_greater_than) / [sign](function.md#sign) / [math_compare](function.md#math_compare) / [smooth_minimum](function.md#smooth_minimum) / [smooth_maximum](function.md#smooth_maximum) / [math_round](function.md#math_round) / [math_floor](function.md#math_floor) / [math_ceil](function.md#math_ceil) / [math_truncate](function.md#math_truncate) / [math_trun](function.md#math_trun) / [fraction](function.md#fraction) / [modulo](function.md#modulo) / [wrap](function.md#wrap) / [snap](function.md#snap) / [ping_pong](function.md#ping_pong) / [sine](function.md#sine) / [sin](function.md#sin) / [cosine](function.md#cosine) / [cos](function.md#cos) / [tangent](function.md#tangent) / [tan](function.md#tan) / [arcsine](function.md#arcsine) / [arcsin](function.md#arcsin) / [arccosine](function.md#arccosine) / [arccos](function.md#arccos) / [arctangent](function.md#arctangent) / [arctan](function.md#arctan) / [arctan2](function.md#arctan2) / [sinh](function.md#sinh) / [cosh](function.md#cosh) / [tanh](function.md#tanh) / [to_radians](function.md#to_radians) / [to_degrees](function.md#to_degrees) / |
| [Merge by Distance](#nodes) | [Geometry](Geometry.md) | [to_degrees](Geometry.md#to_degrees) |
|      | [Vertex](Vertex.md) | [to_degrees](Vertex.md#to_degrees) |
| [Mesh Boolean](#nodes) | [Mesh](Mesh.md) | - [boolean_intersect](Mesh.md#boolean_intersect)<br>- [boolean_union](Mesh.md#boolean_union)<br>- [boolean_difference](Mesh.md#boolean_difference)|
| [Mesh Circle](#nodes) | [Mesh](Mesh.md) | [boolean_difference](Mesh.md#boolean_difference) |
| [Mesh Island](#nodes) | [Face](Face.md) | - [island](Face.md#island-property)<br>- [island_index](Face.md#island_index-property)<br>- [island_count](Face.md#island_count-property)|
|      | [Mesh](Mesh.md) | - [island](Mesh.md#island-property)<br>- [island_index](Mesh.md#island_index-property)<br>- [island_count](Mesh.md#island_count-property)|
| [Mesh Line](#nodes) | [Mesh](Mesh.md) | [Line](Mesh.md#Line-classmethod) / [LineEndPoints](Mesh.md#LineEndPoints-classmethod) / [LineOffset](Mesh.md#LineOffset-classmethod) / [LineEndPointsResolution](Mesh.md#LineEndPointsResolution-classmethod) / [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) / |
| [Mesh to Curve](#nodes) | [Edge](Edge.md) | [LineOffsetResolution](Edge.md#LineOffsetResolution-classmethod) |
|      | [Mesh](Mesh.md) | [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) |
| [Mesh to Points](#nodes) | [Mesh](Mesh.md) | [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) |
|      | [Vertex](Vertex.md) | [LineOffsetResolution](Vertex.md#LineOffsetResolution-classmethod) |
| [Mesh to Volume](#nodes) | [Mesh](Mesh.md) | [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) |
|      | [Vertex](Vertex.md) | [LineOffsetResolution](Vertex.md#LineOffsetResolution-classmethod) |
| [Mix](#nodes) | [Color](Color.md) | [mix](Color.md#mix) / [mix_darken](Color.md#mix_darken) / [mix_multiply](Color.md#mix_multiply) / [mix_burn](Color.md#mix_burn) / [mix_lighten](Color.md#mix_lighten) / [mix_screen](Color.md#mix_screen) / [mix_dodge](Color.md#mix_dodge) / [mix_add](Color.md#mix_add) / [mix_overlay](Color.md#mix_overlay) / [mix_soft_light](Color.md#mix_soft_light) / [mix_linear_light](Color.md#mix_linear_light) / [mix_difference](Color.md#mix_difference) / [mix_subtract](Color.md#mix_subtract) / [mix_divide](Color.md#mix_divide) / [mix_hue](Color.md#mix_hue) / [mix_saturation](Color.md#mix_saturation) / [mix_color](Color.md#mix_color) / [mix_value](Color.md#mix_value) / |
|      | [Float](Float.md) | [mix_value](Float.md#mix_value) |
|      | [Vector](Vector.md) | - [mix](Vector.md#mix)<br>- [mix_uniform](Vector.md#mix_uniform)<br>- [mix_non_uniform](Vector.md#mix_non_uniform)|
|      | [function](function.md) | [float_mix](function.md#float_mix) / [vector_mix](function.md#vector_mix) / [color_mix](function.md#color_mix) / [color_darken](function.md#color_darken) / [color_multiply](function.md#color_multiply) / [color_burn](function.md#color_burn) / [color_lighten](function.md#color_lighten) / [color_screen](function.md#color_screen) / [color_dodge](function.md#color_dodge) / [color_add](function.md#color_add) / [color_overlay](function.md#color_overlay) / [color_soft_light](function.md#color_soft_light) / [color_linear_light](function.md#color_linear_light) / [color_difference](function.md#color_difference) / [color_subtract](function.md#color_subtract) / [color_divide](function.md#color_divide) / [color_hue](function.md#color_hue) / [color_saturation](function.md#color_saturation) / [color_color](function.md#color_color) / [color_value](function.md#color_value) / |
| [Musgrave Texture](#nodes) | [Texture](Texture.md) | [color_value](Texture.md#color_value) |
| [Named Attribute](#nodes) | [Domain](Domain.md) | [named_attribute](Domain.md#named_attribute) / [get_named_float](Domain.md#get_named_float) / [get_named_integer](Domain.md#get_named_integer) / [get_named_vector](Domain.md#get_named_vector) / [get_named_color](Domain.md#get_named_color) / [get_named_boolean](Domain.md#get_named_boolean) / |
|      | [Geometry](Geometry.md) | [named_attribute](Geometry.md#named_attribute) / [get_named_float](Geometry.md#get_named_float) / [get_named_integer](Geometry.md#get_named_integer) / [get_named_vector](Geometry.md#get_named_vector) / [get_named_color](Geometry.md#get_named_color) / [get_named_boolean](Geometry.md#get_named_boolean) / |
| [Noise Texture](#nodes) | [Texture](Texture.md) | [noise](Texture.md#noise-staticmethod) / [noise_1D](Texture.md#noise_1D-staticmethod) / [noise_2D](Texture.md#noise_2D-staticmethod) / [noise_3D](Texture.md#noise_3D-staticmethod) / [noise_4D](Texture.md#noise_4D-staticmethod) / |
| [Normal](#nodes) | [Domain](Domain.md) | [noise_4D](Domain.md#noise_4D-staticmethod) |
|      | [Geometry](Geometry.md) | [noise_4D](Geometry.md#noise_4D-staticmethod) |
|      | [Spline](Spline.md) | [noise_4D](Spline.md#noise_4D-staticmethod) |
| [Object Info](#nodes) | [Object](Object.md) | [info](Object.md#info) / [location](Object.md#location) / [rotation](Object.md#rotation) / [scale](Object.md#scale) / [geometry](Object.md#geometry) / |
| [Offset Point in Curve](#nodes) | [ControlPoint](ControlPoint.md) | [geometry](ControlPoint.md#geometry) |
|      | [Curve](Curve.md) | [geometry](Curve.md#geometry) |
| [Pack UV Islands](#nodes) | [Face](Face.md) | [geometry](Face.md#geometry) |
|      | [Mesh](Mesh.md) | [geometry](Mesh.md#geometry) |
| [Points](#nodes) | [Points](Points.md) | [geometry](Points.md#geometry) |
| [Points of Curve](#nodes) | [Curve](Curve.md) | [geometry](Curve.md#geometry) |
|      | [Spline](Spline.md) | [geometry](Spline.md#geometry) |
| [Points to Vertices](#nodes) | [CloudPoint](CloudPoint.md) | [geometry](CloudPoint.md#geometry) |
|      | [Points](Points.md) | [geometry](Points.md#geometry) |
| [Points to Volume](#nodes) | [Points](Points.md) | - [to_volume](Points.md#to_volume)<br>- [to_volume_size](Points.md#to_volume_size)<br>- [to_volume_amount](Points.md#to_volume_amount)|
| [Position](#nodes) | [Domain](Domain.md) | [to_volume_amount](Domain.md#to_volume_amount) |
|      | [Geometry](Geometry.md) | [to_volume_amount](Geometry.md#to_volume_amount) |
| [Quadratic Bezier](#nodes) | [Curve](Curve.md) | [to_volume_amount](Curve.md#to_volume_amount) |
| [Quadrilateral](#nodes) | [Curve](Curve.md) | [to_volume_amount](Curve.md#to_volume_amount) |
| [Radius](#nodes) | [CloudPoint](CloudPoint.md) | [to_volume_amount](CloudPoint.md#to_volume_amount) |
|      | [ControlPoint](ControlPoint.md) | [to_volume_amount](ControlPoint.md#to_volume_amount) |
|      | [Geometry](Geometry.md) | [to_volume_amount](Geometry.md#to_volume_amount) |
| [Random Value](#nodes) | [Domain](Domain.md) | - [random_float](Domain.md#random_float)<br>- [random_integer](Domain.md#random_integer)<br>- [random_vector](Domain.md#random_vector)<br>- [random_boolean](Domain.md#random_boolean)|
|      | [Geometry](Geometry.md) | - [random_float](Geometry.md#random_float)<br>- [random_integer](Geometry.md#random_integer)<br>- [random_vector](Geometry.md#random_vector)<br>- [random_boolean](Geometry.md#random_boolean)|
|      | [function](function.md) | - [random_float](function.md#random_float)<br>- [random_integer](function.md#random_integer)<br>- [random_vector](function.md#random_vector)<br>- [random_boolean](function.md#random_boolean)|
| [Raycast](#nodes) | [Geometry](Geometry.md) | - [raycast](Geometry.md#raycast)<br>- [raycast_interpolated](Geometry.md#raycast_interpolated)<br>- [raycast_nearest](Geometry.md#raycast_nearest)|
| [Realize Instances](#nodes) | [Instances](Instances.md) | [raycast_nearest](Instances.md#raycast_nearest) |
| [Remove Named Attribute](#nodes) | [Domain](Domain.md) | [raycast_nearest](Domain.md#raycast_nearest) |
|      | [Geometry](Geometry.md) | [raycast_nearest](Geometry.md#raycast_nearest) |
| [Replace Material](#nodes) | [Geometry](Geometry.md) | [raycast_nearest](Geometry.md#raycast_nearest) |
| [Replace String](#nodes) | [String](String.md) | [raycast_nearest](String.md#raycast_nearest) |
|      | [function](function.md) | [raycast_nearest](function.md#raycast_nearest) |
| [Resample Curve](#nodes) | [Curve](Curve.md) | - [resample](Curve.md#resample)<br>- [resample_count](Curve.md#resample_count)<br>- [resample_length](Curve.md#resample_length)<br>- [resample_evaluated](Curve.md#resample_evaluated)|
|      | [Spline](Spline.md) | - [resample](Spline.md#resample)<br>- [resample_count](Spline.md#resample_count)<br>- [resample_length](Spline.md#resample_length)<br>- [resample_evaluated](Spline.md#resample_evaluated)|
| [Reverse Curve](#nodes) | [Curve](Curve.md) | [resample_evaluated](Curve.md#resample_evaluated) |
| [RGB Curves](#nodes) | [Color](Color.md) | [resample_evaluated](Color.md#resample_evaluated) |
|      | [function](function.md) | [resample_evaluated](function.md#resample_evaluated) |
| [Rotate Euler](#nodes) | [Rotation](Rotation.md) | - [Euler](Rotation.md#Euler-classmethod)<br>- [AxisAngle](Rotation.md#AxisAngle-classmethod)<br>- [rotate_euler](Rotation.md#rotate_euler)<br>- [rotate_axis_angle](Rotation.md#rotate_axis_angle)|
|      | [function](function.md) | - [rotate_euler](function.md#rotate_euler)<br>- [rotate_axis_angle](function.md#rotate_axis_angle)|
| [Rotate Instances](#nodes) | [Instance](Instance.md) | [rotate_axis_angle](Instance.md#rotate_axis_angle) |
|      | [Instances](Instances.md) | [rotate_axis_angle](Instances.md#rotate_axis_angle) |
| [Sample Curve](#nodes) | [Curve](Curve.md) | [rotate_axis_angle](Curve.md#rotate_axis_angle) |
| [Sample Index](#nodes) | [Domain](Domain.md) | [rotate_axis_angle](Domain.md#rotate_axis_angle) |
|      | [Geometry](Geometry.md) | [rotate_axis_angle](Geometry.md#rotate_axis_angle) |
| [Sample Nearest](#nodes) | [Domain](Domain.md) | [rotate_axis_angle](Domain.md#rotate_axis_angle) |
|      | [Geometry](Geometry.md) | [rotate_axis_angle](Geometry.md#rotate_axis_angle) |
| [Sample Nearest Surface](#nodes) | [Mesh](Mesh.md) | [rotate_axis_angle](Mesh.md#rotate_axis_angle) |
| [Sample UV Surface](#nodes) | [Mesh](Mesh.md) | [rotate_axis_angle](Mesh.md#rotate_axis_angle) |
| [Scale Elements](#nodes) | [Edge](Edge.md) | - [scale_uniform](Edge.md#scale_uniform)<br>- [scale_single_axis](Edge.md#scale_single_axis)|
|      | [Face](Face.md) | - [scale_uniform](Face.md#scale_uniform)<br>- [scale_single_axis](Face.md#scale_single_axis)|
|      | [Mesh](Mesh.md) | - [scale_elements](Mesh.md#scale_elements)<br>- [scale_uniform](Mesh.md#scale_uniform)<br>- [scale_single_axis](Mesh.md#scale_single_axis)|
| [Scale Instances](#nodes) | [Instance](Instance.md) | [scale_single_axis](Instance.md#scale_single_axis) |
|      | [Instances](Instances.md) | [scale_single_axis](Instances.md#scale_single_axis) |
| [Scene Time](#nodes) | [Float](Float.md) | - [Seconds](Float.md#Seconds-classmethod)<br>- [Frame](Float.md#Frame-classmethod)|
| [Self Object](#nodes) | [Object](Object.md) | [Frame](Object.md#Frame-classmethod) |
| [Separate Color](#nodes) | [Color](Color.md) | [rgb](Color.md#rgb-property) / [hsv](Color.md#hsv-property) / [hsl](Color.md#hsl-property) / [alpha](Color.md#alpha-property) / [red](Color.md#red-property) / [green](Color.md#green-property) / [blue](Color.md#blue-property) / [hue](Color.md#hue-property) / [saturation](Color.md#saturation-property) / [value](Color.md#value-property) / [lightness](Color.md#lightness-property) / |
|      | [function](function.md) | - [separate_rgb](function.md#separate_rgb)<br>- [separate_hsv](function.md#separate_hsv)<br>- [separate_hsl](function.md#separate_hsl)|
| [Separate Components](#nodes) | [Geometry](Geometry.md) | [separate_components](Geometry.md#separate_components-property) / [mesh_component](Geometry.md#mesh_component-property) / [curve_component](Geometry.md#curve_component-property) / [points_component](Geometry.md#points_component-property) / [volume_component](Geometry.md#volume_component-property) / [instances_component](Geometry.md#instances_component-property) / |
| [Separate Geometry](#nodes) | [Domain](Domain.md) | [instances_component](Domain.md#instances_component-property) |
|      | [Geometry](Geometry.md) | [instances_component](Geometry.md#instances_component-property) |
| [Separate XYZ](#nodes) | [Vector](Vector.md) | [instances_component](Vector.md#instances_component-property) |
| [Set Curve Normal](#nodes) | [Spline](Spline.md) | - [set_normal](Spline.md#set_normal)<br>- [normal](Spline.md#normal)|
| [Set Curve Radius](#nodes) | [ControlPoint](ControlPoint.md) | - [set_radius](ControlPoint.md#set_radius)<br>- [radius](ControlPoint.md#radius)|
| [Set Curve Tilt](#nodes) | [ControlPoint](ControlPoint.md) | - [set_tilt](ControlPoint.md#set_tilt)<br>- [tilt](ControlPoint.md#tilt)|
| [Set Handle Positions](#nodes) | [ControlPoint](ControlPoint.md) | [set_handle_positions](ControlPoint.md#set_handle_positions) / [set_handle_positions_left](ControlPoint.md#set_handle_positions_left) / [set_handle_positions_right](ControlPoint.md#set_handle_positions_right) / [left_handle_positions](ControlPoint.md#left_handle_positions) / [right_handle_positions](ControlPoint.md#right_handle_positions) / |
| [Set Handle Type](#nodes) | [ControlPoint](ControlPoint.md) | - [set_handle_type_node](ControlPoint.md#set_handle_type_node)<br>- [set_handle_type](ControlPoint.md#set_handle_type)|
| [Set ID](#nodes) | [Domain](Domain.md) | - [set_ID](Domain.md#set_ID)<br>- [ID](Domain.md#ID)|
|      | [Geometry](Geometry.md) | [ID](Geometry.md#ID) |
| [Set Material](#nodes) | [Face](Face.md) | - [set_material](Face.md#set_material)<br>- [material](Face.md#material-property)<br>- [material](Face.md#material)|
|      | [Geometry](Geometry.md) | [material](Geometry.md#material) |
|      | [Spline](Spline.md) | - [set_material](Spline.md#set_material)<br>- [material](Spline.md#material-property)<br>- [material](Spline.md#material)|
| [Set Material Index](#nodes) | [Domain](Domain.md) | [material](Domain.md#material) |
|      | [Geometry](Geometry.md) | [material](Geometry.md#material) |
| [Set Point Radius](#nodes) | [CloudPoint](CloudPoint.md) | [material](CloudPoint.md#material) |
|      | [Points](Points.md) | [material](Points.md#material) |
| [Set Position](#nodes) | [Domain](Domain.md) | - [set_position](Domain.md#set_position)<br>- [position](Domain.md#position)|
|      | [Geometry](Geometry.md) | [position](Geometry.md#position) |
| [Set Shade Smooth](#nodes) | [Face](Face.md) | - [set_shade_smooth](Face.md#set_shade_smooth)<br>- [shade_smooth](Face.md#shade_smooth)|
|      | [Mesh](Mesh.md) | [shade_smooth](Mesh.md#shade_smooth) |
| [Set Spline Cyclic](#nodes) | [Spline](Spline.md) | - [set_cyclic](Spline.md#set_cyclic)<br>- [cyclic](Spline.md#cyclic)|
| [Set Spline Resolution](#nodes) | [Spline](Spline.md) | - [set_resolution](Spline.md#set_resolution)<br>- [resolution](Spline.md#resolution)|
| [Set Spline Type](#nodes) | [Spline](Spline.md) | - [set_type](Spline.md#set_type)<br>- [type](Spline.md#type-property)<br>- [type](Spline.md#type)|
| [Shortest Edge Paths](#nodes) | [Mesh](Mesh.md) | [type](Mesh.md#type) |
| [Slice String](#nodes) | [String](String.md) | [type](String.md#type) |
|      | [function](function.md) | [type](function.md#type) |
| [Special Characters](#nodes) | [String](String.md) | - [LineBreak](String.md#LineBreak-staticmethod)<br>- [Tab](String.md#Tab-staticmethod)|
| [Spiral](#nodes) | [Curve](Curve.md) | [Tab](Curve.md#Tab-staticmethod) |
| [Spline Length](#nodes) | [Spline](Spline.md) | [Tab](Spline.md#Tab-staticmethod) |
| [Spline Parameter](#nodes) | [ControlPoint](ControlPoint.md) | - [parameter](ControlPoint.md#parameter-property)<br>- [parameter_factor](ControlPoint.md#parameter_factor-property)<br>- [parameter_length](ControlPoint.md#parameter_length-property)<br>- [parameter_index](ControlPoint.md#parameter_index-property)|
| [Spline Resolution](#nodes) | [Spline](Spline.md) | [parameter_index](Spline.md#parameter_index-property) |
| [Split Edges](#nodes) | [Edge](Edge.md) | [parameter_index](Edge.md#parameter_index-property) |
|      | [Mesh](Mesh.md) | [parameter_index](Mesh.md#parameter_index-property) |
| [Star](#nodes) | [Curve](Curve.md) | [parameter_index](Curve.md#parameter_index-property) |
| [Store Named Attribute](#nodes) | [Domain](Domain.md) | [store_named_attribute](Domain.md#store_named_attribute) / [set_named_boolean](Domain.md#set_named_boolean) / [set_named_integer](Domain.md#set_named_integer) / [set_named_float](Domain.md#set_named_float) / [set_named_vector](Domain.md#set_named_vector) / [set_named_color](Domain.md#set_named_color) / |
|      | [Geometry](Geometry.md) | [store_named_attribute](Geometry.md#store_named_attribute) / [set_named_boolean](Geometry.md#set_named_boolean) / [set_named_integer](Geometry.md#set_named_integer) / [set_named_float](Geometry.md#set_named_float) / [set_named_vector](Geometry.md#set_named_vector) / [set_named_color](Geometry.md#set_named_color) / |
| [String](#nodes) | [String](String.md) | [set_named_color](String.md#set_named_color) |
| [String Length](#nodes) | [String](String.md) | [set_named_color](String.md#set_named_color) |
|      | [function](function.md) | [set_named_color](function.md#set_named_color) |
| [String to Curves](#nodes) | [String](String.md) | [set_named_color](String.md#set_named_color) |
|      | [function](function.md) | [set_named_color](function.md#set_named_color) |
| [Subdivide Curve](#nodes) | [Curve](Curve.md) | [set_named_color](Curve.md#set_named_color) |
| [Subdivide Mesh](#nodes) | [Mesh](Mesh.md) | [set_named_color](Mesh.md#set_named_color) |
| [Subdivision Surface](#nodes) | [Mesh](Mesh.md) | [set_named_color](Mesh.md#set_named_color) |
| [Switch](#nodes) | [Boolean](Boolean.md) | [set_named_color](Boolean.md#set_named_color) |
|      | [Collection](Collection.md) | [set_named_color](Collection.md#set_named_color) |
|      | [Color](Color.md) | [set_named_color](Color.md#set_named_color) |
|      | [Float](Float.md) | [set_named_color](Float.md#set_named_color) |
|      | [Geometry](Geometry.md) | [set_named_color](Geometry.md#set_named_color) |
|      | [Image](Image.md) | [set_named_color](Image.md#set_named_color) |
|      | [Integer](Integer.md) | [set_named_color](Integer.md#set_named_color) |
|      | [Material](Material.md) | [set_named_color](Material.md#set_named_color) |
|      | [Object](Object.md) | [set_named_color](Object.md#set_named_color) |
|      | [String](String.md) | [set_named_color](String.md#set_named_color) |
|      | [Texture](Texture.md) | [set_named_color](Texture.md#set_named_color) |
|      | [Vector](Vector.md) | [set_named_color](Vector.md#set_named_color) |
|      | [function](function.md) | [switch](function.md#switch) / [switch_float](function.md#switch_float) / [switch_integer](function.md#switch_integer) / [switch_boolean](function.md#switch_boolean) / [switch_vector](function.md#switch_vector) / [switch_string](function.md#switch_string) / [switch_color](function.md#switch_color) / [switch_object](function.md#switch_object) / [switch_image](function.md#switch_image) / [switch_geometry](function.md#switch_geometry) / [switch_collection](function.md#switch_collection) / [switch_texture](function.md#switch_texture) / [switch_material](function.md#switch_material) / |
| [Transform](#nodes) | [Geometry](Geometry.md) | [switch_material](Geometry.md#switch_material) |
| [Translate Instances](#nodes) | [Instance](Instance.md) | [switch_material](Instance.md#switch_material) |
|      | [Instances](Instances.md) | [switch_material](Instances.md#switch_material) |
| [Triangulate](#nodes) | [Face](Face.md) | [switch_material](Face.md#switch_material) |
|      | [Mesh](Mesh.md) | [switch_material](Mesh.md#switch_material) |
| [Trim Curve](#nodes) | [Curve](Curve.md) | - [trim](Curve.md#trim)<br>- [trim_factor](Curve.md#trim_factor)<br>- [trim_length](Curve.md#trim_length)|
| [UV Sphere](#nodes) | [Mesh](Mesh.md) | [trim_length](Mesh.md#trim_length) |
| [UV Unwrap](#nodes) | [Face](Face.md) | [trim_length](Face.md#trim_length) |
|      | [Mesh](Mesh.md) | [trim_length](Mesh.md#trim_length) |
| [Value](#nodes) | [Float](Float.md) | [trim_length](Float.md#trim_length) |
| [Value to String](#nodes) | [Float](Float.md) | [trim_length](Float.md#trim_length) |
|      | [Integer](Integer.md) | [trim_length](Integer.md#trim_length) |
|      | [function](function.md) | [trim_length](function.md#trim_length) |
| [Vector](#nodes) | [Vector](Vector.md) | [trim_length](Vector.md#trim_length) |
| [Vector Curves](#nodes) | [Vector](Vector.md) | [trim_length](Vector.md#trim_length) |
| [Vector Math](#nodes) | [Vector](Vector.md) | [add](Vector.md#add) / [subtract](Vector.md#subtract) / [sub](Vector.md#sub) / [multiply](Vector.md#multiply) / [mul](Vector.md#mul) / [divide](Vector.md#divide) / [div](Vector.md#div) / [multiply_add](Vector.md#multiply_add) / [mul_add](Vector.md#mul_add) / [cross_product](Vector.md#cross_product) / [cross](Vector.md#cross) / [project](Vector.md#project) / [reflect](Vector.md#reflect) / [refract](Vector.md#refract) / [face_forward](Vector.md#face_forward) / [dot_product](Vector.md#dot_product) / [dot](Vector.md#dot) / [distance](Vector.md#distance) / [length](Vector.md#length-property) / [scale](Vector.md#scale) / [normalize](Vector.md#normalize) / [absolute](Vector.md#absolute) / [abs](Vector.md#abs) / [minimum](Vector.md#minimum) / [min](Vector.md#min) / [maximum](Vector.md#maximum) / [max](Vector.md#max) / [floor](Vector.md#floor) / [ceil](Vector.md#ceil) / [fraction](Vector.md#fraction) / [fract](Vector.md#fract) / [modulo](Vector.md#modulo) / [wrap](Vector.md#wrap) / [snap](Vector.md#snap) / [sine](Vector.md#sine) / [sin](Vector.md#sin) / [cosine](Vector.md#cosine) / [cos](Vector.md#cos) / [tangent](Vector.md#tangent) / [tan](Vector.md#tan) / |
| [Vector Rotate](#nodes) | [Vector](Vector.md) | [rotate_euler](Vector.md#rotate_euler) / [rotate_axis_angle](Vector.md#rotate_axis_angle) / [rotate_x](Vector.md#rotate_x) / [rotate_y](Vector.md#rotate_y) / [rotate_z](Vector.md#rotate_z) / |
| [Vertex Neighbors](#nodes) | [Vertex](Vertex.md) | - [neighbors](Vertex.md#neighbors-property)<br>- [neighbors_vertex_count](Vertex.md#neighbors_vertex_count-property)<br>- [neighbors_face_count](Vertex.md#neighbors_face_count-property)|
| [Volume Cube](#nodes) | [Volume](Volume.md) | [neighbors_face_count](Volume.md#neighbors_face_count-property) |
| [Volume to Mesh](#nodes) | [Volume](Volume.md) | [neighbors_face_count](Volume.md#neighbors_face_count-property) |
| [Voronoi Texture](#nodes) | [Texture](Texture.md) | [voronoi](Texture.md#voronoi-staticmethod) / [voronoi_1D](Texture.md#voronoi_1D-staticmethod) / [voronoi_2D](Texture.md#voronoi_2D-staticmethod) / [voronoi_3D](Texture.md#voronoi_3D-staticmethod) / [voronoi_4D](Texture.md#voronoi_4D-staticmethod) / |
| [Wave Texture](#nodes) | [Texture](Texture.md) | [wave](Texture.md#wave-staticmethod) / [wave_bands](Texture.md#wave_bands-staticmethod) / [wave_rings](Texture.md#wave_rings-staticmethod) / [wave_bands_sine](Texture.md#wave_bands_sine-staticmethod) / [wave_bands_saw](Texture.md#wave_bands_saw-staticmethod) / [wave_bands_triangle](Texture.md#wave_bands_triangle-staticmethod) / [wave_rings_sine](Texture.md#wave_rings_sine-staticmethod) / [wave_rings_saw](Texture.md#wave_rings_saw-staticmethod) / [wave_rings_triangle](Texture.md#wave_rings_triangle-staticmethod) / |
| [White Noise Texture](#nodes) | [Texture](Texture.md) | [white_noise](Texture.md#white_noise-staticmethod) / [white_noise_1D](Texture.md#white_noise_1D-staticmethod) / [white_noise_2D](Texture.md#white_noise_2D-staticmethod) / [white_noise_3D](Texture.md#white_noise_3D-staticmethod) / [white_noise_4D](Texture.md#white_noise_4D-staticmethod) / |
