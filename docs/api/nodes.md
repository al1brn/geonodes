# Nodes

## Alphabetical order:

| node | class | method name |
|------|-------|-------------|
| [AccumulateField](#nodes) | [Domain](Domain.md) | [rotate_euler](Domain.md#rotate_euler) |
| [AlignEulerToVector](#nodes) | [Rotation](Rotation.md) | [rotate_euler](Rotation.md#rotate_euler) |
|      | [Vector](Vector.md) | [rotate_euler](Vector.md#rotate_euler) |
|      | [function](function.md) | [rotate_euler](function.md#rotate_euler) |
| [Arc](#nodes) | [Curve](Curve.md) | - [Arc](Curve.md#Arc-classmethod)<br>- [ArcFromPoints](Curve.md#ArcFromPoints-classmethod)|
| [AttributeStatistic](#nodes) | [Domain](Domain.md) | - [attribute_statistic](Domain.md#attribute_statistic)<br>- [attribute_mean](Domain.md#attribute_mean)<br>- [attribute_median](Domain.md#attribute_median)<br>- [attribute_sum](Domain.md#attribute_sum)<br>- [attribute_min](Domain.md#attribute_min)<br>- [attribute_max](Domain.md#attribute_max)<br>- [attribute_range](Domain.md#attribute_range)<br>- [attribute_std](Domain.md#attribute_std)<br>- [attribute_var](Domain.md#attribute_var)|
|      | [Geometry](Geometry.md) | [attribute_var](Geometry.md#attribute_var) |
| [BezierSegment](#nodes) | [Curve](Curve.md) | [attribute_var](Curve.md#attribute_var) |
| [Boolean](#nodes) | [Boolean](Boolean.md) | [attribute_var](Boolean.md#attribute_var) |
| [BooleanMath](#nodes) | [Boolean](Boolean.md) | - [b_and](Boolean.md#b_and)<br>- [b_or](Boolean.md#b_or)<br>- [b_not](Boolean.md#b_not)<br>- [nand](Boolean.md#nand)<br>- [nor](Boolean.md#nor)<br>- [xnor](Boolean.md#xnor)<br>- [xor](Boolean.md#xor)<br>- [imply](Boolean.md#imply)<br>- [nimply](Boolean.md#nimply)|
|      | [function](function.md) | - [b_and](function.md#b_and)<br>- [b_or](function.md#b_or)<br>- [b_not](function.md#b_not)<br>- [nand](function.md#nand)<br>- [nor](function.md#nor)<br>- [xnor](function.md#xnor)<br>- [xor](function.md#xor)<br>- [imply](function.md#imply)<br>- [nimply](function.md#nimply)|
| [BoundingBox](#nodes) | [Geometry](Geometry.md) | - [bounding_box](Geometry.md#bounding_box-property)<br>- [bounding_box_min](Geometry.md#bounding_box_min-property)<br>- [bounding_box_min](Geometry.md#bounding_box_min-property)|
| [BrickTexture](#nodes) | [Texture](Texture.md) | [bounding_box_min](Texture.md#bounding_box_min-property) |
| [CaptureAttribute](#nodes) | [Domain](Domain.md) | [bounding_box_min](Domain.md#bounding_box_min-property) |
|      | [Geometry](Geometry.md) | - [capture_attribute](Geometry.md#capture_attribute)<br>- [capture_attribute_node](Geometry.md#capture_attribute_node)|
| [CheckerTexture](#nodes) | [Texture](Texture.md) | [capture_attribute_node](Texture.md#capture_attribute_node) |
| [Clamp](#nodes) | [Float](Float.md) | - [clamp](Float.md#clamp)<br>- [clamp_min_max](Float.md#clamp_min_max)<br>- [clamp_range](Float.md#clamp_range)|
|      | [function](function.md) | - [clamp](function.md#clamp)<br>- [clamp_min_max](function.md#clamp_min_max)<br>- [clamp_range](function.md#clamp_range)|
| [CollectionInfo](#nodes) | [Geometry](Geometry.md) | [clamp_range](Geometry.md#clamp_range) |
| [Color](#nodes) | [Color](Color.md) | [clamp_range](Color.md#clamp_range) |
| [ColorRamp](#nodes) | [Float](Float.md) | [clamp_range](Float.md#clamp_range) |
|      | [function](function.md) | [clamp_range](function.md#clamp_range) |
| [CombineColor](#nodes) | [Color](Color.md) | - [RGB](Color.md#RGB-classmethod)<br>- [HSV](Color.md#HSV-classmethod)<br>- [HSL](Color.md#HSL-classmethod)|
|      | [function](function.md) | - [combine_rgb](function.md#combine_rgb)<br>- [combine_hsv](function.md#combine_hsv)<br>- [combine_hsl](function.md#combine_hsl)|
| [CombineXyz](#nodes) | [Vector](Vector.md) | [combine_hsl](Vector.md#combine_hsl) |
| [Compare](#nodes) | [Color](Color.md) | - [compare](Color.md#compare)<br>- [darker](Color.md#darker)<br>- [brighter](Color.md#brighter)<br>- [equal](Color.md#equal)<br>- [equal](Color.md#equal)|
|      | [Float](Float.md) | - [compare](Float.md#compare)<br>- [less_than](Float.md#less_than)<br>- [less_equal](Float.md#less_equal)<br>- [greater_than](Float.md#greater_than)<br>- [greater_equal](Float.md#greater_equal)<br>- [equal](Float.md#equal)<br>- [not_equal](Float.md#not_equal)|
|      | [Integer](Integer.md) | - [compare](Integer.md#compare)<br>- [less_than](Integer.md#less_than)<br>- [less_equal](Integer.md#less_equal)<br>- [greater_than](Integer.md#greater_than)<br>- [greater_equal](Integer.md#greater_equal)<br>- [equal](Integer.md#equal)<br>- [not_equal](Integer.md#not_equal)|
|      | [String](String.md) | - [equal](String.md#equal)<br>- [not_equal](String.md#not_equal)|
|      | [Vector](Vector.md) | - [compare](Vector.md#compare)<br>- [elements_less_than](Vector.md#elements_less_than)<br>- [elements_less_equal](Vector.md#elements_less_equal)<br>- [elements_greater_than](Vector.md#elements_greater_than)<br>- [elements_greater_equal](Vector.md#elements_greater_equal)<br>- [elements_equal](Vector.md#elements_equal)<br>- [elements_not_equal](Vector.md#elements_not_equal)<br>- [length_less_than](Vector.md#length_less_than)<br>- [length_less_equal](Vector.md#length_less_equal)<br>- [length_greater_than](Vector.md#length_greater_than)<br>- [length_greater_equal](Vector.md#length_greater_equal)<br>- [length_equal](Vector.md#length_equal)<br>- [length_not_equal](Vector.md#length_not_equal)<br>- [average_less_than](Vector.md#average_less_than)<br>- [average_less_equal](Vector.md#average_less_equal)<br>- [average_greater_than](Vector.md#average_greater_than)<br>- [average_greater_equal](Vector.md#average_greater_equal)<br>- [average_equal](Vector.md#average_equal)<br>- [average_not_equal](Vector.md#average_not_equal)<br>- [dot_product_less_than](Vector.md#dot_product_less_than)<br>- [dot_product_less_equal](Vector.md#dot_product_less_equal)<br>- [dot_product_greater_than](Vector.md#dot_product_greater_than)<br>- [dot_product_greater_equal](Vector.md#dot_product_greater_equal)<br>- [dot_product_equal](Vector.md#dot_product_equal)<br>- [dot_product_not_equal](Vector.md#dot_product_not_equal)<br>- [direction_less_than](Vector.md#direction_less_than)<br>- [direction_less_equal](Vector.md#direction_less_equal)<br>- [direction_greater_than](Vector.md#direction_greater_than)<br>- [direction_greater_equal](Vector.md#direction_greater_equal)<br>- [direction_equal](Vector.md#direction_equal)<br>- [direction_not_equal](Vector.md#direction_not_equal)|
|      | [function](function.md) | [direction_not_equal](function.md#direction_not_equal) |
| [Cone](#nodes) | [Mesh](Mesh.md) | [direction_not_equal](Mesh.md#direction_not_equal) |
| [ConvexHull](#nodes) | [Geometry](Geometry.md) | [direction_not_equal](Geometry.md#direction_not_equal) |
| [Cube](#nodes) | [Mesh](Mesh.md) | [direction_not_equal](Mesh.md#direction_not_equal) |
| [CurveCircle](#nodes) | [Curve](Curve.md) | - [Circle](Curve.md#Circle-classmethod)<br>- [CircleFromPoints](Curve.md#CircleFromPoints-classmethod)|
| [CurveHandlePositions](#nodes) | [ControlPoint](ControlPoint.md) | - [handle_positions](ControlPoint.md#handle_positions)<br>- [left_handle_positions](ControlPoint.md#left_handle_positions-property)<br>- [right_handle_positions](ControlPoint.md#right_handle_positions-property)|
| [CurveLength](#nodes) | [Curve](Curve.md) | [right_handle_positions](Curve.md#right_handle_positions-property) |
| [CurveLine](#nodes) | [Curve](Curve.md) | - [Line](Curve.md#Line-classmethod)<br>- [LineDirection](Curve.md#LineDirection-classmethod)|
| [CurveOfPoint](#nodes) | [ControlPoint](ControlPoint.md) | [LineDirection](ControlPoint.md#LineDirection-classmethod) |
|      | [Curve](Curve.md) | [LineDirection](Curve.md#LineDirection-classmethod) |
| [CurveTangent](#nodes) | [ControlPoint](ControlPoint.md) | [LineDirection](ControlPoint.md#LineDirection-classmethod) |
| [CurveTilt](#nodes) | [ControlPoint](ControlPoint.md) | [LineDirection](ControlPoint.md#LineDirection-classmethod) |
| [CurveToMesh](#nodes) | [Curve](Curve.md) | [LineDirection](Curve.md#LineDirection-classmethod) |
| [CurveToPoints](#nodes) | [Curve](Curve.md) | - [to_points](Curve.md#to_points)<br>- [to_points_count](Curve.md#to_points_count)<br>- [to_points_length](Curve.md#to_points_length)<br>- [to_points_evaluated](Curve.md#to_points_evaluated)|
| [Cylinder](#nodes) | [Mesh](Mesh.md) | [to_points_evaluated](Mesh.md#to_points_evaluated) |
| [DeformCurvesOnSurface](#nodes) | [Curve](Curve.md) | [to_points_evaluated](Curve.md#to_points_evaluated) |
| [DeleteGeometry](#nodes) | [Domain](Domain.md) | [to_points_evaluated](Domain.md#to_points_evaluated) |
|      | [Edge](Edge.md) | - [delete_all](Edge.md#delete_all)<br>- [delete_edges](Edge.md#delete_edges)<br>- [delete_faces](Edge.md#delete_faces)|
|      | [Face](Face.md) | - [delete_all](Face.md#delete_all)<br>- [delete_edges](Face.md#delete_edges)<br>- [delete_faces](Face.md#delete_faces)|
|      | [Geometry](Geometry.md) | [delete_faces](Geometry.md#delete_faces) |
|      | [Mesh](Mesh.md) | - [delete_all](Mesh.md#delete_all)<br>- [delete_edges](Mesh.md#delete_edges)<br>- [delete_faces](Mesh.md#delete_faces)|
|      | [Vertex](Vertex.md) | - [delete_all](Vertex.md#delete_all)<br>- [delete_edges](Vertex.md#delete_edges)<br>- [delete_faces](Vertex.md#delete_faces)|
| [DistributePointsInVolume](#nodes) | [Volume](Volume.md) | - [distribute_points](Volume.md#distribute_points)<br>- [distribute_points_random](Volume.md#distribute_points_random)<br>- [distribute_points_grid](Volume.md#distribute_points_grid)|
| [DistributePointsOnFaces](#nodes) | [Face](Face.md) | - [distribute_points_random](Face.md#distribute_points_random)<br>- [distribute_points_poisson](Face.md#distribute_points_poisson)|
|      | [Mesh](Mesh.md) | [distribute_points_poisson](Mesh.md#distribute_points_poisson) |
| [DomainSize](#nodes) | [CloudPoint](CloudPoint.md) | [distribute_points_poisson](CloudPoint.md#distribute_points_poisson) |
|      | [ControlPoint](ControlPoint.md) | [distribute_points_poisson](ControlPoint.md#distribute_points_poisson) |
|      | [Corner](Corner.md) | [distribute_points_poisson](Corner.md#distribute_points_poisson) |
|      | [Curve](Curve.md) | - [domain_size](Curve.md#domain_size-property)<br>- [point_count](Curve.md#point_count-property)<br>- [spline_count](Curve.md#spline_count-property)|
|      | [Edge](Edge.md) | [spline_count](Edge.md#spline_count-property) |
|      | [Face](Face.md) | [spline_count](Face.md#spline_count-property) |
|      | [Geometry](Geometry.md) | [spline_count](Geometry.md#spline_count-property) |
|      | [Instance](Instance.md) | [spline_count](Instance.md#spline_count-property) |
|      | [Instances](Instances.md) | [spline_count](Instances.md#spline_count-property) |
|      | [Mesh](Mesh.md) | - [domain_size](Mesh.md#domain_size-property)<br>- [point_count](Mesh.md#point_count-property)<br>- [face_count](Mesh.md#face_count-property)<br>- [edge_count](Mesh.md#edge_count-property)<br>- [corner_count](Mesh.md#corner_count-property)|
|      | [Points](Points.md) | [corner_count](Points.md#corner_count-property) |
|      | [Spline](Spline.md) | [corner_count](Spline.md#corner_count-property) |
|      | [Vertex](Vertex.md) | [corner_count](Vertex.md#corner_count-property) |
| [DualMesh](#nodes) | [Mesh](Mesh.md) | [corner_count](Mesh.md#corner_count-property) |
| [DuplicateElements](#nodes) | [Domain](Domain.md) | [corner_count](Domain.md#corner_count-property) |
|      | [Geometry](Geometry.md) | [corner_count](Geometry.md#corner_count-property) |
| [EdgeAngle](#nodes) | [Edge](Edge.md) | - [angle](Edge.md#angle-property)<br>- [unsigned_angle](Edge.md#unsigned_angle-property)<br>- [signed_angle](Edge.md#signed_angle-property)|
| [EdgeNeighbors](#nodes) | [Edge](Edge.md) | [signed_angle](Edge.md#signed_angle-property) |
| [EdgePathsToCurves](#nodes) | [Edge](Edge.md) | [signed_angle](Edge.md#signed_angle-property) |
|      | [Mesh](Mesh.md) | [signed_angle](Mesh.md#signed_angle-property) |
| [EdgePathsToSelection](#nodes) | [Mesh](Mesh.md) | [signed_angle](Mesh.md#signed_angle-property) |
| [EdgeVertices](#nodes) | [Edge](Edge.md) | - [vertices](Edge.md#vertices-property)<br>- [vertices_index](Edge.md#vertices_index-property)<br>- [vertices_position](Edge.md#vertices_position-property)|
| [EndpointSelection](#nodes) | [ControlPoint](ControlPoint.md) | [vertices_position](ControlPoint.md#vertices_position-property) |
| [ExtrudeMesh](#nodes) | [Edge](Edge.md) | [vertices_position](Edge.md#vertices_position-property) |
|      | [Face](Face.md) | [vertices_position](Face.md#vertices_position-property) |
|      | [Mesh](Mesh.md) | [vertices_position](Mesh.md#vertices_position-property) |
|      | [Vertex](Vertex.md) | [vertices_position](Vertex.md#vertices_position-property) |
| [FaceArea](#nodes) | [Face](Face.md) | [vertices_position](Face.md#vertices_position-property) |
| [FaceIsPlanar](#nodes) | [Face](Face.md) | [vertices_position](Face.md#vertices_position-property) |
|      | [Mesh](Mesh.md) | [vertices_position](Mesh.md#vertices_position-property) |
| [FaceNeighbors](#nodes) | [Face](Face.md) | - [neighbors](Face.md#neighbors-property)<br>- [neighbors_vertex_count](Face.md#neighbors_vertex_count-property)<br>- [neighbors_face_count](Face.md#neighbors_face_count-property)|
| [FaceSetBoundaries](#nodes) | [Face](Face.md) | [neighbors_face_count](Face.md#neighbors_face_count-property) |
|      | [Mesh](Mesh.md) | [neighbors_face_count](Mesh.md#neighbors_face_count-property) |
| [FieldAtIndex](#nodes) | [Domain](Domain.md) | [neighbors_face_count](Domain.md#neighbors_face_count-property) |
|      | [Geometry](Geometry.md) | [neighbors_face_count](Geometry.md#neighbors_face_count-property) |
| [FillCurve](#nodes) | [Curve](Curve.md) | - [fill](Curve.md#fill)<br>- [fill_triangles](Curve.md#fill_triangles)<br>- [fill_ngons](Curve.md#fill_ngons)|
| [FilletCurve](#nodes) | [Curve](Curve.md) | - [fillet](Curve.md#fillet)<br>- [fillet_bezier](Curve.md#fillet_bezier)<br>- [fillet_poly](Curve.md#fillet_poly)|
| [FlipFaces](#nodes) | [Face](Face.md) | [fillet_poly](Face.md#fillet_poly) |
|      | [Mesh](Mesh.md) | [fillet_poly](Mesh.md#fillet_poly) |
| [FloatCurve](#nodes) | [Float](Float.md) | [fillet_poly](Float.md#fillet_poly) |
| [FloatToInteger](#nodes) | [Float](Float.md) | - [to_integer](Float.md#to_integer)<br>- [round](Float.md#round)<br>- [floor](Float.md#floor)<br>- [ceiling](Float.md#ceiling)<br>- [truncate](Float.md#truncate)|
| [GeometryProximity](#nodes) | [Geometry](Geometry.md) | - [proximity](Geometry.md#proximity)<br>- [proximity_points](Geometry.md#proximity_points)<br>- [proximity_edges](Geometry.md#proximity_edges)<br>- [proximity_facess](Geometry.md#proximity_facess)|
| [GeometryToInstance](#nodes) | [Geometry](Geometry.md) | [proximity_facess](Geometry.md#proximity_facess) |
|      | [function](function.md) | [proximity_facess](function.md#proximity_facess) |
| [GradientTexture](#nodes) | [Texture](Texture.md) | - [gradient](Texture.md#gradient-staticmethod)<br>- [gradient_linear](Texture.md#gradient_linear-staticmethod)<br>- [gradient_quadratic](Texture.md#gradient_quadratic-staticmethod)<br>- [gradient_easing](Texture.md#gradient_easing-staticmethod)<br>- [gradient_diagonal](Texture.md#gradient_diagonal-staticmethod)<br>- [gradient_spherical](Texture.md#gradient_spherical-staticmethod)<br>- [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere-staticmethod)<br>- [gradient_radial](Texture.md#gradient_radial-staticmethod)|
| [Grid](#nodes) | [Mesh](Mesh.md) | [gradient_radial](Mesh.md#gradient_radial-staticmethod) |
| [HandleTypeSelection](#nodes) | [ControlPoint](ControlPoint.md) | - [handle_type_selection_node](ControlPoint.md#handle_type_selection_node)<br>- [handle_type_selection](ControlPoint.md#handle_type_selection)<br>- [handle_type_selection](ControlPoint.md#handle_type_selection)<br>- [handle_type_selection](ControlPoint.md#handle_type_selection)<br>- [handle_type_selection](ControlPoint.md#handle_type_selection)<br>- [handle_type_selection](ControlPoint.md#handle_type_selection)|
| [ID](#nodes) | [Domain](Domain.md) | [ID](Domain.md#ID) |
|      | [Geometry](Geometry.md) | [ID](Geometry.md#ID) |
| [IcoSphere](#nodes) | [Mesh](Mesh.md) | [ico_sphere](Mesh.md#ico_sphere) |
| [ImageTexture](#nodes) | [Image](Image.md) | [image_texture](Image.md#image_texture) |
|      | [Texture](Texture.md) | [image_texture](Texture.md#image_texture) |
| [Index](#nodes) | [Domain](Domain.md) | - [index](Domain.md#index-property)<br>- [domain_index](Domain.md#domain_index-property)|
|      | [Geometry](Geometry.md) | [domain_index](Geometry.md#domain_index-property) |
| [InstanceOnPoints](#nodes) | [CloudPoint](CloudPoint.md) | [domain_index](CloudPoint.md#domain_index-property) |
|      | [ControlPoint](ControlPoint.md) | [domain_index](ControlPoint.md#domain_index-property) |
|      | [Curve](Curve.md) | [domain_index](Curve.md#domain_index-property) |
|      | [Instances](Instances.md) | - [InstanceOnPoints](Instances.md#InstanceOnPoints-classmethod)<br>- [on_points](Instances.md#on_points)|
|      | [Mesh](Mesh.md) | [on_points](Mesh.md#on_points) |
|      | [Points](Points.md) | [on_points](Points.md#on_points) |
|      | [Vertex](Vertex.md) | [on_points](Vertex.md#on_points) |
| [InstanceRotation](#nodes) | [Instance](Instance.md) | [on_points](Instance.md#on_points) |
|      | [Instances](Instances.md) | [on_points](Instances.md#on_points) |
| [InstanceScale](#nodes) | [Instance](Instance.md) | [on_points](Instance.md#on_points) |
|      | [Instances](Instances.md) | [on_points](Instances.md#on_points) |
| [InstancesToPoints](#nodes) | [Instance](Instance.md) | [on_points](Instance.md#on_points) |
|      | [Instances](Instances.md) | [on_points](Instances.md#on_points) |
| [Integer](#nodes) | [Integer](Integer.md) | [on_points](Integer.md#on_points) |
| [IsShadeSmooth](#nodes) | [Face](Face.md) | [on_points](Face.md#on_points) |
|      | [Mesh](Mesh.md) | [on_points](Mesh.md#on_points) |
| [IsSplineCyclic](#nodes) | [Spline](Spline.md) | [on_points](Spline.md#on_points) |
| [IsViewport](#nodes) | [Geometry](Geometry.md) | [on_points](Geometry.md#on_points) |
| [JoinGeometry](#nodes) | [Geometry](Geometry.md) | [on_points](Geometry.md#on_points) |
|      | [function](function.md) | [on_points](function.md#on_points) |
| [JoinStrings](#nodes) | [String](String.md) | [on_points](String.md#on_points) |
|      | [function](function.md) | [on_points](function.md#on_points) |
| [MagicTexture](#nodes) | [Texture](Texture.md) | [on_points](Texture.md#on_points) |
| [MapRange](#nodes) | [Float](Float.md) | - [map_range](Float.md#map_range)<br>- [map_range_linear](Float.md#map_range_linear)<br>- [map_range_stepped](Float.md#map_range_stepped)<br>- [map_range_smooth](Float.md#map_range_smooth)<br>- [map_range_smoother](Float.md#map_range_smoother)|
|      | [Vector](Vector.md) | - [map_range](Vector.md#map_range)<br>- [map_range_linear](Vector.md#map_range_linear)<br>- [map_range_stepped](Vector.md#map_range_stepped)<br>- [map_range_smooth](Vector.md#map_range_smooth)<br>- [map_range_smoother](Vector.md#map_range_smoother)|
| [Material](#nodes) | [Material](Material.md) | [map_range_smoother](Material.md#map_range_smoother) |
| [MaterialIndex](#nodes) | [Domain](Domain.md) | [map_range_smoother](Domain.md#map_range_smoother) |
|      | [Geometry](Geometry.md) | [map_range_smoother](Geometry.md#map_range_smoother) |
| [MaterialSelection](#nodes) | [Domain](Domain.md) | [map_range_smoother](Domain.md#map_range_smoother) |
|      | [Geometry](Geometry.md) | [map_range_smoother](Geometry.md#map_range_smoother) |
| [Math](#nodes) | [Float](Float.md) | - [add](Float.md#add)<br>- [subtract](Float.md#subtract)<br>- [sub](Float.md#sub)<br>- [multiply](Float.md#multiply)<br>- [mul](Float.md#mul)<br>- [divide](Float.md#divide)<br>- [div](Float.md#div)<br>- [multiply_add](Float.md#multiply_add)<br>- [mul_add](Float.md#mul_add)<br>- [power](Float.md#power)<br>- [pow](Float.md#pow)<br>- [logarithm](Float.md#logarithm)<br>- [log](Float.md#log)<br>- [sqrt](Float.md#sqrt)<br>- [inverse_sqrt](Float.md#inverse_sqrt)<br>- [absolute](Float.md#absolute)<br>- [abs](Float.md#abs)<br>- [exponent](Float.md#exponent)<br>- [exp](Float.md#exp)<br>- [minimum](Float.md#minimum)<br>- [min](Float.md#min)<br>- [maximum](Float.md#maximum)<br>- [max](Float.md#max)<br>- [math_less_than](Float.md#math_less_than)<br>- [math_greater_than](Float.md#math_greater_than)<br>- [sign](Float.md#sign)<br>- [math_compare](Float.md#math_compare)<br>- [smooth_minimum](Float.md#smooth_minimum)<br>- [smooth_maximum](Float.md#smooth_maximum)<br>- [math_round](Float.md#math_round)<br>- [math_floor](Float.md#math_floor)<br>- [math_ceil](Float.md#math_ceil)<br>- [math_truncate](Float.md#math_truncate)<br>- [math_trunc](Float.md#math_trunc)<br>- [fraction](Float.md#fraction)<br>- [fact](Float.md#fact)<br>- [modulo](Float.md#modulo)<br>- [wrap](Float.md#wrap)<br>- [snap](Float.md#snap)<br>- [ping_pong](Float.md#ping_pong)<br>- [sine](Float.md#sine)<br>- [sin](Float.md#sin)<br>- [cosine](Float.md#cosine)<br>- [cos](Float.md#cos)<br>- [tangent](Float.md#tangent)<br>- [tan](Float.md#tan)<br>- [arcsine](Float.md#arcsine)<br>- [arcsin](Float.md#arcsin)<br>- [arccosine](Float.md#arccosine)<br>- [arccos](Float.md#arccos)<br>- [arctangent](Float.md#arctangent)<br>- [arctan](Float.md#arctan)<br>- [arctan2](Float.md#arctan2)<br>- [sinh](Float.md#sinh)<br>- [cosh](Float.md#cosh)<br>- [tanh](Float.md#tanh)<br>- [to_radians](Float.md#to_radians)<br>- [to_degrees](Float.md#to_degrees)|
|      | [Integer](Integer.md) | - [add](Integer.md#add)<br>- [subtract](Integer.md#subtract)<br>- [sub](Integer.md#sub)<br>- [multiply](Integer.md#multiply)<br>- [mul](Integer.md#mul)<br>- [divide](Integer.md#divide)<br>- [div](Integer.md#div)<br>- [multiply_add](Integer.md#multiply_add)<br>- [mul_add](Integer.md#mul_add)<br>- [power](Integer.md#power)<br>- [pow](Integer.md#pow)<br>- [logarithm](Integer.md#logarithm)<br>- [log](Integer.md#log)<br>- [sqrt](Integer.md#sqrt)<br>- [inverse_sqrt](Integer.md#inverse_sqrt)<br>- [absolute](Integer.md#absolute)<br>- [abs](Integer.md#abs)<br>- [exponent](Integer.md#exponent)<br>- [exp](Integer.md#exp)<br>- [minimum](Integer.md#minimum)<br>- [min](Integer.md#min)<br>- [maximum](Integer.md#maximum)<br>- [max](Integer.md#max)<br>- [math_less_than](Integer.md#math_less_than)<br>- [math_greater_than](Integer.md#math_greater_than)<br>- [sign](Integer.md#sign)<br>- [math_compare](Integer.md#math_compare)<br>- [smooth_minimum](Integer.md#smooth_minimum)<br>- [smooth_maximum](Integer.md#smooth_maximum)<br>- [math_round](Integer.md#math_round)<br>- [math_floor](Integer.md#math_floor)<br>- [math_ceil](Integer.md#math_ceil)<br>- [math_truncate](Integer.md#math_truncate)<br>- [math_trunc](Integer.md#math_trunc)<br>- [fraction](Integer.md#fraction)<br>- [fact](Integer.md#fact)<br>- [modulo](Integer.md#modulo)<br>- [wrap](Integer.md#wrap)<br>- [snap](Integer.md#snap)<br>- [ping_pong](Integer.md#ping_pong)<br>- [sine](Integer.md#sine)<br>- [sin](Integer.md#sin)<br>- [cosine](Integer.md#cosine)<br>- [cos](Integer.md#cos)<br>- [tangent](Integer.md#tangent)<br>- [tan](Integer.md#tan)<br>- [arcsine](Integer.md#arcsine)<br>- [arcsin](Integer.md#arcsin)<br>- [arccosine](Integer.md#arccosine)<br>- [arccos](Integer.md#arccos)<br>- [arctangent](Integer.md#arctangent)<br>- [arctan](Integer.md#arctan)<br>- [arctan2](Integer.md#arctan2)<br>- [sinh](Integer.md#sinh)<br>- [cosh](Integer.md#cosh)<br>- [tanh](Integer.md#tanh)<br>- [to_radians](Integer.md#to_radians)<br>- [to_degrees](Integer.md#to_degrees)|
|      | [function](function.md) | - [math](function.md#math)<br>- [add](function.md#add)<br>- [subtract](function.md#subtract)<br>- [sub](function.md#sub)<br>- [multiply](function.md#multiply)<br>- [mul](function.md#mul)<br>- [divide](function.md#divide)<br>- [div](function.md#div)<br>- [multiply_add](function.md#multiply_add)<br>- [mul_add](function.md#mul_add)<br>- [power](function.md#power)<br>- [logarithm](function.md#logarithm)<br>- [log](function.md#log)<br>- [sqrt](function.md#sqrt)<br>- [inverse_sqrt](function.md#inverse_sqrt)<br>- [absolute](function.md#absolute)<br>- [abs](function.md#abs)<br>- [exponent](function.md#exponent)<br>- [exp](function.md#exp)<br>- [minimum](function.md#minimum)<br>- [min](function.md#min)<br>- [maximum](function.md#maximum)<br>- [max](function.md#max)<br>- [math_less_than](function.md#math_less_than)<br>- [math_greater_than](function.md#math_greater_than)<br>- [sign](function.md#sign)<br>- [math_compare](function.md#math_compare)<br>- [smooth_minimum](function.md#smooth_minimum)<br>- [smooth_maximum](function.md#smooth_maximum)<br>- [math_round](function.md#math_round)<br>- [math_floor](function.md#math_floor)<br>- [math_ceil](function.md#math_ceil)<br>- [math_truncate](function.md#math_truncate)<br>- [math_trun](function.md#math_trun)<br>- [fraction](function.md#fraction)<br>- [modulo](function.md#modulo)<br>- [wrap](function.md#wrap)<br>- [snap](function.md#snap)<br>- [ping_pong](function.md#ping_pong)<br>- [sine](function.md#sine)<br>- [sin](function.md#sin)<br>- [cosine](function.md#cosine)<br>- [cos](function.md#cos)<br>- [tangent](function.md#tangent)<br>- [tan](function.md#tan)<br>- [arcsine](function.md#arcsine)<br>- [arcsin](function.md#arcsin)<br>- [arccosine](function.md#arccosine)<br>- [arccos](function.md#arccos)<br>- [arctangent](function.md#arctangent)<br>- [arctan](function.md#arctan)<br>- [arctan2](function.md#arctan2)<br>- [sinh](function.md#sinh)<br>- [cosh](function.md#cosh)<br>- [tanh](function.md#tanh)<br>- [to_radians](function.md#to_radians)<br>- [to_degrees](function.md#to_degrees)|
| [MergeByDistance](#nodes) | [Geometry](Geometry.md) | [to_degrees](Geometry.md#to_degrees) |
|      | [Vertex](Vertex.md) | [to_degrees](Vertex.md#to_degrees) |
| [MeshBoolean](#nodes) | [Mesh](Mesh.md) | - [boolean_intersect](Mesh.md#boolean_intersect)<br>- [boolean_union](Mesh.md#boolean_union)<br>- [boolean_difference](Mesh.md#boolean_difference)|
| [MeshCircle](#nodes) | [Mesh](Mesh.md) | [boolean_difference](Mesh.md#boolean_difference) |
| [MeshIsland](#nodes) | [Face](Face.md) | - [island](Face.md#island-property)<br>- [island_index](Face.md#island_index-property)<br>- [island_count](Face.md#island_count-property)|
|      | [Mesh](Mesh.md) | - [island](Mesh.md#island-property)<br>- [island_index](Mesh.md#island_index-property)<br>- [island_count](Mesh.md#island_count-property)|
| [MeshLine](#nodes) | [Mesh](Mesh.md) | - [Line](Mesh.md#Line-classmethod)<br>- [LineEndPoints](Mesh.md#LineEndPoints-classmethod)<br>- [LineOffset](Mesh.md#LineOffset-classmethod)<br>- [LineEndPointsResolution](Mesh.md#LineEndPointsResolution-classmethod)<br>- [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod)|
| [MeshToCurve](#nodes) | [Edge](Edge.md) | [LineOffsetResolution](Edge.md#LineOffsetResolution-classmethod) |
|      | [Mesh](Mesh.md) | [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) |
| [MeshToPoints](#nodes) | [Mesh](Mesh.md) | [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) |
|      | [Vertex](Vertex.md) | [LineOffsetResolution](Vertex.md#LineOffsetResolution-classmethod) |
| [MeshToVolume](#nodes) | [Mesh](Mesh.md) | [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) |
|      | [Vertex](Vertex.md) | [LineOffsetResolution](Vertex.md#LineOffsetResolution-classmethod) |
| [Mix](#nodes) | [Color](Color.md) | - [mix](Color.md#mix)<br>- [mix_darken](Color.md#mix_darken)<br>- [mix_multiply](Color.md#mix_multiply)<br>- [mix_burn](Color.md#mix_burn)<br>- [mix_lighten](Color.md#mix_lighten)<br>- [mix_screen](Color.md#mix_screen)<br>- [mix_dodge](Color.md#mix_dodge)<br>- [mix_add](Color.md#mix_add)<br>- [mix_overlay](Color.md#mix_overlay)<br>- [mix_soft_light](Color.md#mix_soft_light)<br>- [mix_linear_light](Color.md#mix_linear_light)<br>- [mix_difference](Color.md#mix_difference)<br>- [mix_subtract](Color.md#mix_subtract)<br>- [mix_divide](Color.md#mix_divide)<br>- [mix_hue](Color.md#mix_hue)<br>- [mix_saturation](Color.md#mix_saturation)<br>- [mix_color](Color.md#mix_color)<br>- [mix_value](Color.md#mix_value)|
|      | [Float](Float.md) | [mix_value](Float.md#mix_value) |
|      | [Vector](Vector.md) | - [mix](Vector.md#mix)<br>- [mix_uniform](Vector.md#mix_uniform)<br>- [mix_non_uniform](Vector.md#mix_non_uniform)|
|      | [function](function.md) | - [float_mix](function.md#float_mix)<br>- [vector_mix](function.md#vector_mix)<br>- [color_mix](function.md#color_mix)<br>- [color_darken](function.md#color_darken)<br>- [color_multiply](function.md#color_multiply)<br>- [color_burn](function.md#color_burn)<br>- [color_lighten](function.md#color_lighten)<br>- [color_screen](function.md#color_screen)<br>- [color_dodge](function.md#color_dodge)<br>- [color_add](function.md#color_add)<br>- [color_overlay](function.md#color_overlay)<br>- [color_soft_light](function.md#color_soft_light)<br>- [color_linear_light](function.md#color_linear_light)<br>- [color_difference](function.md#color_difference)<br>- [color_subtract](function.md#color_subtract)<br>- [color_divide](function.md#color_divide)<br>- [color_hue](function.md#color_hue)<br>- [color_saturation](function.md#color_saturation)<br>- [color_color](function.md#color_color)<br>- [color_value](function.md#color_value)|
| [MusgraveTexture](#nodes) | [Texture](Texture.md) | [color_value](Texture.md#color_value) |
| [NamedAttribute](#nodes) | [Domain](Domain.md) | - [named_attribute](Domain.md#named_attribute)<br>- [get_named_float](Domain.md#get_named_float)<br>- [get_named_integer](Domain.md#get_named_integer)<br>- [get_named_vector](Domain.md#get_named_vector)<br>- [get_named_color](Domain.md#get_named_color)<br>- [get_named_boolean](Domain.md#get_named_boolean)|
|      | [Geometry](Geometry.md) | - [named_attribute](Geometry.md#named_attribute)<br>- [get_named_float](Geometry.md#get_named_float)<br>- [get_named_integer](Geometry.md#get_named_integer)<br>- [get_named_vector](Geometry.md#get_named_vector)<br>- [get_named_color](Geometry.md#get_named_color)<br>- [get_named_boolean](Geometry.md#get_named_boolean)|
| [NoiseTexture](#nodes) | [Texture](Texture.md) | - [noise](Texture.md#noise-staticmethod)<br>- [noise_1D](Texture.md#noise_1D-staticmethod)<br>- [noise_2D](Texture.md#noise_2D-staticmethod)<br>- [noise_3D](Texture.md#noise_3D-staticmethod)<br>- [noise_4D](Texture.md#noise_4D-staticmethod)|
| [Normal](#nodes) | [Domain](Domain.md) | [noise_4D](Domain.md#noise_4D-staticmethod) |
|      | [Geometry](Geometry.md) | [noise_4D](Geometry.md#noise_4D-staticmethod) |
|      | [Spline](Spline.md) | [noise_4D](Spline.md#noise_4D-staticmethod) |
| [ObjectInfo](#nodes) | [Object](Object.md) | - [info](Object.md#info)<br>- [location](Object.md#location)<br>- [rotation](Object.md#rotation)<br>- [scale](Object.md#scale)<br>- [geometry](Object.md#geometry)|
| [OffsetPointInCurve](#nodes) | [ControlPoint](ControlPoint.md) | [geometry](ControlPoint.md#geometry) |
|      | [Curve](Curve.md) | [geometry](Curve.md#geometry) |
| [PackUvIslands](#nodes) | [Face](Face.md) | [geometry](Face.md#geometry) |
|      | [Mesh](Mesh.md) | [geometry](Mesh.md#geometry) |
| [Points](#nodes) | [Points](Points.md) | [geometry](Points.md#geometry) |
| [PointsOfCurve](#nodes) | [Curve](Curve.md) | [geometry](Curve.md#geometry) |
|      | [Spline](Spline.md) | [geometry](Spline.md#geometry) |
| [PointsToVertices](#nodes) | [CloudPoint](CloudPoint.md) | [geometry](CloudPoint.md#geometry) |
|      | [Points](Points.md) | [geometry](Points.md#geometry) |
| [PointsToVolume](#nodes) | [Points](Points.md) | - [to_volume](Points.md#to_volume)<br>- [to_volume_size](Points.md#to_volume_size)<br>- [to_volume_amount](Points.md#to_volume_amount)|
| [Position](#nodes) | [Domain](Domain.md) | [to_volume_amount](Domain.md#to_volume_amount) |
|      | [Geometry](Geometry.md) | [to_volume_amount](Geometry.md#to_volume_amount) |
| [QuadraticBezier](#nodes) | [Curve](Curve.md) | [to_volume_amount](Curve.md#to_volume_amount) |
| [Quadrilateral](#nodes) | [Curve](Curve.md) | [to_volume_amount](Curve.md#to_volume_amount) |
| [Radius](#nodes) | [CloudPoint](CloudPoint.md) | [to_volume_amount](CloudPoint.md#to_volume_amount) |
|      | [ControlPoint](ControlPoint.md) | [to_volume_amount](ControlPoint.md#to_volume_amount) |
|      | [Geometry](Geometry.md) | [to_volume_amount](Geometry.md#to_volume_amount) |
| [RandomValue](#nodes) | [Domain](Domain.md) | - [random_float](Domain.md#random_float)<br>- [random_integer](Domain.md#random_integer)<br>- [random_vector](Domain.md#random_vector)<br>- [random_boolean](Domain.md#random_boolean)|
|      | [Geometry](Geometry.md) | - [random_float](Geometry.md#random_float)<br>- [random_integer](Geometry.md#random_integer)<br>- [random_vector](Geometry.md#random_vector)<br>- [random_boolean](Geometry.md#random_boolean)|
|      | [function](function.md) | - [random_float](function.md#random_float)<br>- [random_integer](function.md#random_integer)<br>- [random_vector](function.md#random_vector)<br>- [random_boolean](function.md#random_boolean)|
| [Raycast](#nodes) | [Geometry](Geometry.md) | - [raycast](Geometry.md#raycast)<br>- [raycast_interpolated](Geometry.md#raycast_interpolated)<br>- [raycast_nearest](Geometry.md#raycast_nearest)|
| [RealizeInstances](#nodes) | [Instances](Instances.md) | [raycast_nearest](Instances.md#raycast_nearest) |
| [RemoveNamedAttribute](#nodes) | [Domain](Domain.md) | [raycast_nearest](Domain.md#raycast_nearest) |
|      | [Geometry](Geometry.md) | [raycast_nearest](Geometry.md#raycast_nearest) |
| [ReplaceMaterial](#nodes) | [Geometry](Geometry.md) | [raycast_nearest](Geometry.md#raycast_nearest) |
| [ReplaceString](#nodes) | [String](String.md) | [raycast_nearest](String.md#raycast_nearest) |
|      | [function](function.md) | [raycast_nearest](function.md#raycast_nearest) |
| [ResampleCurve](#nodes) | [Curve](Curve.md) | - [resample](Curve.md#resample)<br>- [resample_count](Curve.md#resample_count)<br>- [resample_length](Curve.md#resample_length)<br>- [resample_evaluated](Curve.md#resample_evaluated)|
|      | [Spline](Spline.md) | - [resample](Spline.md#resample)<br>- [resample_count](Spline.md#resample_count)<br>- [resample_length](Spline.md#resample_length)<br>- [resample_evaluated](Spline.md#resample_evaluated)|
| [ReverseCurve](#nodes) | [Curve](Curve.md) | [resample_evaluated](Curve.md#resample_evaluated) |
| [RgbCurves](#nodes) | [Color](Color.md) | [resample_evaluated](Color.md#resample_evaluated) |
|      | [function](function.md) | [resample_evaluated](function.md#resample_evaluated) |
| [RotateEuler](#nodes) | [Rotation](Rotation.md) | - [Euler](Rotation.md#Euler-classmethod)<br>- [AxisAngle](Rotation.md#AxisAngle-classmethod)<br>- [rotate_euler](Rotation.md#rotate_euler)<br>- [rotate_axis_angle](Rotation.md#rotate_axis_angle)|
|      | [function](function.md) | - [rotate_euler](function.md#rotate_euler)<br>- [rotate_axis_angle](function.md#rotate_axis_angle)|
| [RotateInstances](#nodes) | [Instance](Instance.md) | [rotate_axis_angle](Instance.md#rotate_axis_angle) |
|      | [Instances](Instances.md) | [rotate_axis_angle](Instances.md#rotate_axis_angle) |
| [SampleCurve](#nodes) | [Curve](Curve.md) | [rotate_axis_angle](Curve.md#rotate_axis_angle) |
| [SampleIndex](#nodes) | [Domain](Domain.md) | [rotate_axis_angle](Domain.md#rotate_axis_angle) |
|      | [Geometry](Geometry.md) | [rotate_axis_angle](Geometry.md#rotate_axis_angle) |
| [SampleNearest](#nodes) | [Domain](Domain.md) | [rotate_axis_angle](Domain.md#rotate_axis_angle) |
|      | [Geometry](Geometry.md) | [rotate_axis_angle](Geometry.md#rotate_axis_angle) |
| [SampleNearestSurface](#nodes) | [Mesh](Mesh.md) | [rotate_axis_angle](Mesh.md#rotate_axis_angle) |
| [SampleUvSurface](#nodes) | [Mesh](Mesh.md) | [rotate_axis_angle](Mesh.md#rotate_axis_angle) |
| [ScaleElements](#nodes) | [Edge](Edge.md) | - [scale_uniform](Edge.md#scale_uniform)<br>- [scale_single_axis](Edge.md#scale_single_axis)|
|      | [Face](Face.md) | - [scale_uniform](Face.md#scale_uniform)<br>- [scale_single_axis](Face.md#scale_single_axis)|
|      | [Mesh](Mesh.md) | - [scale_elements](Mesh.md#scale_elements)<br>- [scale_uniform](Mesh.md#scale_uniform)<br>- [scale_single_axis](Mesh.md#scale_single_axis)|
| [ScaleInstances](#nodes) | [Instance](Instance.md) | [scale_single_axis](Instance.md#scale_single_axis) |
|      | [Instances](Instances.md) | [scale_single_axis](Instances.md#scale_single_axis) |
| [SceneTime](#nodes) | [Float](Float.md) | - [Seconds](Float.md#Seconds-classmethod)<br>- [Frame](Float.md#Frame-classmethod)|
| [SelfObject](#nodes) | [Object](Object.md) | [Frame](Object.md#Frame-classmethod) |
| [SeparateColor](#nodes) | [Color](Color.md) | - [rgb](Color.md#rgb-property)<br>- [hsv](Color.md#hsv-property)<br>- [hsl](Color.md#hsl-property)<br>- [alpha](Color.md#alpha-property)<br>- [red](Color.md#red-property)<br>- [green](Color.md#green-property)<br>- [blue](Color.md#blue-property)<br>- [hue](Color.md#hue-property)<br>- [saturation](Color.md#saturation-property)<br>- [value](Color.md#value-property)<br>- [lightness](Color.md#lightness-property)|
|      | [function](function.md) | - [separate_rgb](function.md#separate_rgb)<br>- [separate_hsv](function.md#separate_hsv)<br>- [separate_hsl](function.md#separate_hsl)|
| [SeparateComponents](#nodes) | [Geometry](Geometry.md) | - [separate_components](Geometry.md#separate_components-property)<br>- [mesh_component](Geometry.md#mesh_component-property)<br>- [curve_component](Geometry.md#curve_component-property)<br>- [points_component](Geometry.md#points_component-property)<br>- [volume_component](Geometry.md#volume_component-property)<br>- [instances_component](Geometry.md#instances_component-property)|
| [SeparateGeometry](#nodes) | [Domain](Domain.md) | [instances_component](Domain.md#instances_component-property) |
|      | [Geometry](Geometry.md) | [instances_component](Geometry.md#instances_component-property) |
| [SeparateXyz](#nodes) | [Vector](Vector.md) | [instances_component](Vector.md#instances_component-property) |
| [SetCurveNormal](#nodes) | [Spline](Spline.md) | - [set_normal](Spline.md#set_normal)<br>- [normal](Spline.md#normal)|
| [SetCurveRadius](#nodes) | [ControlPoint](ControlPoint.md) | - [set_radius](ControlPoint.md#set_radius)<br>- [radius](ControlPoint.md#radius)|
| [SetCurveTilt](#nodes) | [ControlPoint](ControlPoint.md) | - [set_tilt](ControlPoint.md#set_tilt)<br>- [tilt](ControlPoint.md#tilt)|
| [SetHandlePositions](#nodes) | [ControlPoint](ControlPoint.md) | - [set_handle_positions](ControlPoint.md#set_handle_positions)<br>- [set_handle_positions_left](ControlPoint.md#set_handle_positions_left)<br>- [set_handle_positions_right](ControlPoint.md#set_handle_positions_right)<br>- [left_handle_positions](ControlPoint.md#left_handle_positions)<br>- [right_handle_positions](ControlPoint.md#right_handle_positions)|
| [SetHandleType](#nodes) | [ControlPoint](ControlPoint.md) | - [set_handle_type_node](ControlPoint.md#set_handle_type_node)<br>- [set_handle_type](ControlPoint.md#set_handle_type)|
| [SetID](#nodes) | [Domain](Domain.md) | - [set_ID](Domain.md#set_ID)<br>- [ID](Domain.md#ID)|
|      | [Geometry](Geometry.md) | [ID](Geometry.md#ID) |
| [SetMaterial](#nodes) | [Face](Face.md) | - [set_material](Face.md#set_material)<br>- [material](Face.md#material-property)<br>- [material](Face.md#material)|
|      | [Geometry](Geometry.md) | [material](Geometry.md#material) |
|      | [Spline](Spline.md) | - [set_material](Spline.md#set_material)<br>- [material](Spline.md#material-property)<br>- [material](Spline.md#material)|
| [SetMaterialIndex](#nodes) | [Domain](Domain.md) | [material](Domain.md#material) |
|      | [Geometry](Geometry.md) | [material](Geometry.md#material) |
| [SetPointRadius](#nodes) | [CloudPoint](CloudPoint.md) | [material](CloudPoint.md#material) |
|      | [Points](Points.md) | [material](Points.md#material) |
| [SetPosition](#nodes) | [Domain](Domain.md) | - [set_position](Domain.md#set_position)<br>- [position](Domain.md#position)|
|      | [Geometry](Geometry.md) | [position](Geometry.md#position) |
| [SetShadeSmooth](#nodes) | [Face](Face.md) | - [set_shade_smooth](Face.md#set_shade_smooth)<br>- [shade_smooth](Face.md#shade_smooth)|
|      | [Mesh](Mesh.md) | [shade_smooth](Mesh.md#shade_smooth) |
| [SetSplineCyclic](#nodes) | [Spline](Spline.md) | - [set_cyclic](Spline.md#set_cyclic)<br>- [cyclic](Spline.md#cyclic)|
| [SetSplineResolution](#nodes) | [Spline](Spline.md) | - [set_resolution](Spline.md#set_resolution)<br>- [resolution](Spline.md#resolution)|
| [SetSplineType](#nodes) | [Spline](Spline.md) | - [set_type](Spline.md#set_type)<br>- [type](Spline.md#type-property)<br>- [type](Spline.md#type)|
| [ShortestEdgePaths](#nodes) | [Mesh](Mesh.md) | [type](Mesh.md#type) |
| [SliceString](#nodes) | [String](String.md) | [type](String.md#type) |
|      | [function](function.md) | [type](function.md#type) |
| [SpecialCharacters](#nodes) | [String](String.md) | - [LineBreak](String.md#LineBreak-staticmethod)<br>- [Tab](String.md#Tab-staticmethod)|
| [Spiral](#nodes) | [Curve](Curve.md) | [Tab](Curve.md#Tab-staticmethod) |
| [SplineLength](#nodes) | [Spline](Spline.md) | [Tab](Spline.md#Tab-staticmethod) |
| [SplineParameter](#nodes) | [ControlPoint](ControlPoint.md) | - [parameter](ControlPoint.md#parameter-property)<br>- [parameter_factor](ControlPoint.md#parameter_factor-property)<br>- [parameter_length](ControlPoint.md#parameter_length-property)<br>- [parameter_index](ControlPoint.md#parameter_index-property)|
| [SplineResolution](#nodes) | [Spline](Spline.md) | [parameter_index](Spline.md#parameter_index-property) |
| [SplitEdges](#nodes) | [Edge](Edge.md) | [parameter_index](Edge.md#parameter_index-property) |
|      | [Mesh](Mesh.md) | [parameter_index](Mesh.md#parameter_index-property) |
| [Star](#nodes) | [Curve](Curve.md) | [parameter_index](Curve.md#parameter_index-property) |
| [StoreNamedAttribute](#nodes) | [Domain](Domain.md) | - [store_named_attribute](Domain.md#store_named_attribute)<br>- [set_named_boolean](Domain.md#set_named_boolean)<br>- [set_named_integer](Domain.md#set_named_integer)<br>- [set_named_float](Domain.md#set_named_float)<br>- [set_named_vector](Domain.md#set_named_vector)<br>- [set_named_color](Domain.md#set_named_color)|
|      | [Geometry](Geometry.md) | - [store_named_attribute](Geometry.md#store_named_attribute)<br>- [set_named_boolean](Geometry.md#set_named_boolean)<br>- [set_named_integer](Geometry.md#set_named_integer)<br>- [set_named_float](Geometry.md#set_named_float)<br>- [set_named_vector](Geometry.md#set_named_vector)<br>- [set_named_color](Geometry.md#set_named_color)|
| [String](#nodes) | [String](String.md) | [set_named_color](String.md#set_named_color) |
| [StringLength](#nodes) | [String](String.md) | [set_named_color](String.md#set_named_color) |
|      | [function](function.md) | [set_named_color](function.md#set_named_color) |
| [StringToCurves](#nodes) | [String](String.md) | [set_named_color](String.md#set_named_color) |
|      | [function](function.md) | [set_named_color](function.md#set_named_color) |
| [SubdivideCurve](#nodes) | [Curve](Curve.md) | [set_named_color](Curve.md#set_named_color) |
| [SubdivideMesh](#nodes) | [Mesh](Mesh.md) | [set_named_color](Mesh.md#set_named_color) |
| [SubdivisionSurface](#nodes) | [Mesh](Mesh.md) | [set_named_color](Mesh.md#set_named_color) |
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
|      | [function](function.md) | - [switch](function.md#switch)<br>- [switch_float](function.md#switch_float)<br>- [switch_integer](function.md#switch_integer)<br>- [switch_boolean](function.md#switch_boolean)<br>- [switch_vector](function.md#switch_vector)<br>- [switch_string](function.md#switch_string)<br>- [switch_color](function.md#switch_color)<br>- [switch_object](function.md#switch_object)<br>- [switch_image](function.md#switch_image)<br>- [switch_geometry](function.md#switch_geometry)<br>- [switch_collection](function.md#switch_collection)<br>- [switch_texture](function.md#switch_texture)<br>- [switch_material](function.md#switch_material)|
| [Transform](#nodes) | [Geometry](Geometry.md) | [switch_material](Geometry.md#switch_material) |
| [TranslateInstances](#nodes) | [Instance](Instance.md) | [switch_material](Instance.md#switch_material) |
|      | [Instances](Instances.md) | [switch_material](Instances.md#switch_material) |
| [Triangulate](#nodes) | [Face](Face.md) | [switch_material](Face.md#switch_material) |
|      | [Mesh](Mesh.md) | [switch_material](Mesh.md#switch_material) |
| [TrimCurve](#nodes) | [Curve](Curve.md) | - [trim](Curve.md#trim)<br>- [trim_factor](Curve.md#trim_factor)<br>- [trim_length](Curve.md#trim_length)|
| [UvSphere](#nodes) | [Mesh](Mesh.md) | [trim_length](Mesh.md#trim_length) |
| [UvUnwrap](#nodes) | [Face](Face.md) | [trim_length](Face.md#trim_length) |
|      | [Mesh](Mesh.md) | [trim_length](Mesh.md#trim_length) |
| [Value](#nodes) | [Float](Float.md) | [trim_length](Float.md#trim_length) |
| [ValueToString](#nodes) | [Float](Float.md) | [trim_length](Float.md#trim_length) |
|      | [Integer](Integer.md) | [trim_length](Integer.md#trim_length) |
|      | [function](function.md) | [trim_length](function.md#trim_length) |
| [Vector](#nodes) | [Vector](Vector.md) | [trim_length](Vector.md#trim_length) |
| [VectorCurves](#nodes) | [Vector](Vector.md) | [trim_length](Vector.md#trim_length) |
| [VectorMath](#nodes) | [Vector](Vector.md) | - [add](Vector.md#add)<br>- [subtract](Vector.md#subtract)<br>- [sub](Vector.md#sub)<br>- [multiply](Vector.md#multiply)<br>- [mul](Vector.md#mul)<br>- [divide](Vector.md#divide)<br>- [div](Vector.md#div)<br>- [multiply_add](Vector.md#multiply_add)<br>- [mul_add](Vector.md#mul_add)<br>- [cross_product](Vector.md#cross_product)<br>- [cross](Vector.md#cross)<br>- [project](Vector.md#project)<br>- [reflect](Vector.md#reflect)<br>- [refract](Vector.md#refract)<br>- [face_forward](Vector.md#face_forward)<br>- [dot_product](Vector.md#dot_product)<br>- [dot](Vector.md#dot)<br>- [distance](Vector.md#distance)<br>- [length](Vector.md#length-property)<br>- [scale](Vector.md#scale)<br>- [normalize](Vector.md#normalize)<br>- [absolute](Vector.md#absolute)<br>- [abs](Vector.md#abs)<br>- [minimum](Vector.md#minimum)<br>- [min](Vector.md#min)<br>- [maximum](Vector.md#maximum)<br>- [max](Vector.md#max)<br>- [floor](Vector.md#floor)<br>- [ceil](Vector.md#ceil)<br>- [fraction](Vector.md#fraction)<br>- [fract](Vector.md#fract)<br>- [modulo](Vector.md#modulo)<br>- [wrap](Vector.md#wrap)<br>- [snap](Vector.md#snap)<br>- [sine](Vector.md#sine)<br>- [sin](Vector.md#sin)<br>- [cosine](Vector.md#cosine)<br>- [cos](Vector.md#cos)<br>- [tangent](Vector.md#tangent)<br>- [tan](Vector.md#tan)|
| [VectorRotate](#nodes) | [Vector](Vector.md) | - [rotate_euler](Vector.md#rotate_euler)<br>- [rotate_axis_angle](Vector.md#rotate_axis_angle)<br>- [rotate_x](Vector.md#rotate_x)<br>- [rotate_y](Vector.md#rotate_y)<br>- [rotate_z](Vector.md#rotate_z)|
| [VertexNeighbors](#nodes) | [Vertex](Vertex.md) | - [neighbors](Vertex.md#neighbors-property)<br>- [neighbors_vertex_count](Vertex.md#neighbors_vertex_count-property)<br>- [neighbors_face_count](Vertex.md#neighbors_face_count-property)|
| [VolumeCube](#nodes) | [Volume](Volume.md) | [neighbors_face_count](Volume.md#neighbors_face_count-property) |
| [VolumeToMesh](#nodes) | [Volume](Volume.md) | [neighbors_face_count](Volume.md#neighbors_face_count-property) |
| [VoronoiTexture](#nodes) | [Texture](Texture.md) | - [voronoi](Texture.md#voronoi-staticmethod)<br>- [voronoi_1D](Texture.md#voronoi_1D-staticmethod)<br>- [voronoi_2D](Texture.md#voronoi_2D-staticmethod)<br>- [voronoi_3D](Texture.md#voronoi_3D-staticmethod)<br>- [voronoi_4D](Texture.md#voronoi_4D-staticmethod)|
| [WaveTexture](#nodes) | [Texture](Texture.md) | - [wave](Texture.md#wave-staticmethod)<br>- [wave_bands](Texture.md#wave_bands-staticmethod)<br>- [wave_rings](Texture.md#wave_rings-staticmethod)<br>- [wave_bands_sine](Texture.md#wave_bands_sine-staticmethod)<br>- [wave_bands_saw](Texture.md#wave_bands_saw-staticmethod)<br>- [wave_bands_triangle](Texture.md#wave_bands_triangle-staticmethod)<br>- [wave_rings_sine](Texture.md#wave_rings_sine-staticmethod)<br>- [wave_rings_saw](Texture.md#wave_rings_saw-staticmethod)<br>- [wave_rings_triangle](Texture.md#wave_rings_triangle-staticmethod)|
| [WhiteNoiseTexture](#nodes) | [Texture](Texture.md) | - [white_noise](Texture.md#white_noise-staticmethod)<br>- [white_noise_1D](Texture.md#white_noise_1D-staticmethod)<br>- [white_noise_2D](Texture.md#white_noise_2D-staticmethod)<br>- [white_noise_3D](Texture.md#white_noise_3D-staticmethod)<br>- [white_noise_4D](Texture.md#white_noise_4D-staticmethod)|
