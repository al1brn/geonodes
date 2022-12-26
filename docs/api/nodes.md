# Nodes in alphabetical order

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Accumulate Field](GeometryNodeAccumulateField.md) | [Domain](Domain.md) | [accumulate_field](Domain.md#accumulate_field) |
| [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Vector](Vector.md) | - [align_euler_to_vector](Vector.md#align_euler_to_vector)<br>- [AlignToVector](Vector.md#AlignToVector)|
|      | [functions](functions.md) | [align_euler_to_vector](functions.md#align_euler_to_vector) |
| [Arc](GeometryNodeCurveArc.md) | [Curve](Curve.md) | - [Arc](Curve.md#Arc)<br>- [ArcFromPoints](Curve.md#ArcFromPoints)|
| [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Domain](Domain.md) | [attribute_statistic](Domain.md#attribute_statistic) / [attribute_mean](Domain.md#attribute_mean) / [attribute_median](Domain.md#attribute_median) / [attribute_sum](Domain.md#attribute_sum) / [attribute_min](Domain.md#attribute_min) / [attribute_max](Domain.md#attribute_max) / [attribute_range](Domain.md#attribute_range) / [attribute_std](Domain.md#attribute_std) / [attribute_var](Domain.md#attribute_var) / |
|      | [Geometry](Geometry.md) | [attribute_statistic](Geometry.md#attribute_statistic) |
| [Bezier Segment](GeometryNodeCurvePrimitiveBezierSegment.md) | [Curve](Curve.md) | [BezierSegment](Curve.md#BezierSegment) |
| [Boolean](FunctionNodeInputBool.md) | [Boolean](Boolean.md) | [Boolean](Boolean.md#Boolean) |
| [Boolean Math](FunctionNodeBooleanMath.md) | [Boolean](Boolean.md) | [b_and](Boolean.md#b_and) / [b_or](Boolean.md#b_or) / [b_not](Boolean.md#b_not) / [nand](Boolean.md#nand) / [nor](Boolean.md#nor) / [xnor](Boolean.md#xnor) / [xor](Boolean.md#xor) / [imply](Boolean.md#imply) / [nimply](Boolean.md#nimply) / |
|      | [functions](functions.md) | [b_and](functions.md#b_and) / [b_or](functions.md#b_or) / [b_not](functions.md#b_not) / [nand](functions.md#nand) / [nor](functions.md#nor) / [xnor](functions.md#xnor) / [xor](functions.md#xor) / [imply](functions.md#imply) / [nimply](functions.md#nimply) / |
| [Bounding Box](GeometryNodeBoundBox.md) | [Geometry](Geometry.md) | - [bounding_box](Geometry.md#bounding_box)<br>- [bounding_box_min](Geometry.md#bounding_box_min)<br>- [bounding_box_min](Geometry.md#bounding_box_min)|
| [Brick Texture](ShaderNodeTexBrick.md) | [Texture](Texture.md) | [brick](Texture.md#brick) |
| [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Domain](Domain.md) | [capture_attribute](Domain.md#capture_attribute) |
|      | [Geometry](Geometry.md) | - [capture_attribute](Geometry.md#capture_attribute)<br>- [capture_attribute_node](Geometry.md#capture_attribute_node)|
| [Checker Texture](ShaderNodeTexChecker.md) | [Texture](Texture.md) | [checker](Texture.md#checker) |
| [Clamp](ShaderNodeClamp.md) | [Float](Float.md) | - [clamp](Float.md#clamp)<br>- [clamp_min_max](Float.md#clamp_min_max)<br>- [clamp_range](Float.md#clamp_range)|
|      | [functions](functions.md) | - [clamp](functions.md#clamp)<br>- [clamp_min_max](functions.md#clamp_min_max)<br>- [clamp_range](functions.md#clamp_range)|
| [Collection Info](GeometryNodeCollectionInfo.md) | [Geometry](Geometry.md) | [Collection](Geometry.md#Collection) |
| [Color](FunctionNodeInputColor.md) | [Color](Color.md) | [Color](Color.md#Color) |
| [ColorRamp](ShaderNodeValToRGB.md) | [Float](Float.md) | [color_ramp](Float.md#color_ramp) |
|      | [functions](functions.md) | [color_ramp](functions.md#color_ramp) |
| [Combine Color](FunctionNodeCombineColor.md) | [Color](Color.md) | - [RGB](Color.md#RGB)<br>- [HSV](Color.md#HSV)<br>- [HSL](Color.md#HSL)|
|      | [functions](functions.md) | - [combine_rgb](functions.md#combine_rgb)<br>- [combine_hsv](functions.md#combine_hsv)<br>- [combine_hsl](functions.md#combine_hsl)|
| [Combine XYZ](ShaderNodeCombineXYZ.md) | [Vector](Vector.md) | [Combine](Vector.md#Combine) |
| [Compare](FunctionNodeCompare.md) | [Color](Color.md) | - [darker](Color.md#darker)<br>- [brighter](Color.md#brighter)<br>- [equal](Color.md#equal)<br>- [equal](Color.md#equal)|
|      | [Float](Float.md) | [compare](Float.md#compare) / [less_than](Float.md#less_than) / [less_equal](Float.md#less_equal) / [greater_than](Float.md#greater_than) / [greater_equal](Float.md#greater_equal) / [equal](Float.md#equal) / [not_equal](Float.md#not_equal) / |
|      | [Integer](Integer.md) | [compare](Integer.md#compare) / [less_than](Integer.md#less_than) / [less_equal](Integer.md#less_equal) / [greater_than](Integer.md#greater_than) / [greater_equal](Integer.md#greater_equal) / [equal](Integer.md#equal) / [not_equal](Integer.md#not_equal) / |
|      | [String](String.md) | - [equal](String.md#equal)<br>- [not_equal](String.md#not_equal)|
|      | [Vector](Vector.md) | [compare](Vector.md#compare) / [elements_less_than](Vector.md#elements_less_than) / [elements_less_equal](Vector.md#elements_less_equal) / [elements_greater_than](Vector.md#elements_greater_than) / [elements_greater_equal](Vector.md#elements_greater_equal) / [elements_equal](Vector.md#elements_equal) / [elements_not_equal](Vector.md#elements_not_equal) / [length_less_than](Vector.md#length_less_than) / [length_less_equal](Vector.md#length_less_equal) / [length_greater_than](Vector.md#length_greater_than) / [length_greater_equal](Vector.md#length_greater_equal) / [length_equal](Vector.md#length_equal) / [length_not_equal](Vector.md#length_not_equal) / [average_less_than](Vector.md#average_less_than) / [average_less_equal](Vector.md#average_less_equal) / [average_greater_than](Vector.md#average_greater_than) / [average_greater_equal](Vector.md#average_greater_equal) / [average_equal](Vector.md#average_equal) / [average_not_equal](Vector.md#average_not_equal) / [dot_product_less_than](Vector.md#dot_product_less_than) / [dot_product_less_equal](Vector.md#dot_product_less_equal) / [dot_product_greater_than](Vector.md#dot_product_greater_than) / [dot_product_greater_equal](Vector.md#dot_product_greater_equal) / [dot_product_equal](Vector.md#dot_product_equal) / [dot_product_not_equal](Vector.md#dot_product_not_equal) / [direction_less_than](Vector.md#direction_less_than) / [direction_less_equal](Vector.md#direction_less_equal) / [direction_greater_than](Vector.md#direction_greater_than) / [direction_greater_equal](Vector.md#direction_greater_equal) / [direction_equal](Vector.md#direction_equal) / [direction_not_equal](Vector.md#direction_not_equal) / |
|      | [functions](functions.md) | [compare](functions.md#compare) |
| [Cone](GeometryNodeMeshCone.md) | [Mesh](Mesh.md) | [Cone](Mesh.md#Cone) |
| [Convex Hull](GeometryNodeConvexHull.md) | [Geometry](Geometry.md) | [convex_hull](Geometry.md#convex_hull) |
| [Corners of Face](GeometryNodeCornersOfFace.md) | [Face](Face.md) | - [corners](Face.md#corners)<br>- [corners_index](Face.md#corners_index)<br>- [corners_total](Face.md#corners_total)|
|      | [Mesh](Mesh.md) | [corners_of_face](Mesh.md#corners_of_face) |
| [Corners of Vertex](GeometryNodeCornersOfVertex.md) | [Mesh](Mesh.md) | [corners_of_vertex](Mesh.md#corners_of_vertex) |
|      | [Vertex](Vertex.md) | - [corners](Vertex.md#corners)<br>- [corners_index](Vertex.md#corners_index)<br>- [corners_total](Vertex.md#corners_total)|
| [Cube](GeometryNodeMeshCube.md) | [Mesh](Mesh.md) | [Cube](Mesh.md#Cube) |
| [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) | [Curve](Curve.md) | - [Circle](Curve.md#Circle)<br>- [CircleFromPoints](Curve.md#CircleFromPoints)|
| [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [ControlPoint](ControlPoint.md) | - [handle_positions](ControlPoint.md#handle_positions)<br>- [left_handle_positions](ControlPoint.md#left_handle_positions)<br>- [right_handle_positions](ControlPoint.md#right_handle_positions)|
| [Curve Length](GeometryNodeCurveLength.md) | [Curve](Curve.md) | [length](Curve.md#length) |
| [Curve Line](GeometryNodeCurvePrimitiveLine.md) | [Curve](Curve.md) | - [Line](Curve.md#Line)<br>- [LineDirection](Curve.md#LineDirection)|
| [Curve of Point](GeometryNodeCurveOfPoint.md) | [ControlPoint](ControlPoint.md) | [curve](ControlPoint.md#curve) |
|      | [Curve](Curve.md) | [curve_of_point](Curve.md#curve_of_point) |
| [Curve Tangent](GeometryNodeInputTangent.md) | [ControlPoint](ControlPoint.md) | [tangent](ControlPoint.md#tangent) |
| [Curve Tilt](GeometryNodeInputCurveTilt.md) | [ControlPoint](ControlPoint.md) | [tilt](ControlPoint.md#tilt) |
| [Curve to Mesh](GeometryNodeCurveToMesh.md) | [Curve](Curve.md) | [to_mesh](Curve.md#to_mesh) |
| [Curve to Points](GeometryNodeCurveToPoints.md) | [Curve](Curve.md) | - [to_points](Curve.md#to_points)<br>- [to_points_count](Curve.md#to_points_count)<br>- [to_points_length](Curve.md#to_points_length)<br>- [to_points_evaluated](Curve.md#to_points_evaluated)|
| [Cylinder](GeometryNodeMeshCylinder.md) | [Mesh](Mesh.md) | [Cylinder](Mesh.md#Cylinder) |
| [Deform Curves on Surface](GeometryNodeDeformCurvesOnSurface.md) | [Curve](Curve.md) | [deform_on_surface](Curve.md#deform_on_surface) |
| [Delete Geometry](GeometryNodeDeleteGeometry.md) | [CloudPoint](CloudPoint.md) | [delete](CloudPoint.md#delete) |
|      | [ControlPoint](ControlPoint.md) | [delete](ControlPoint.md#delete) |
|      | [Edge](Edge.md) | - [delete](Edge.md#delete)<br>- [delete_all](Edge.md#delete_all)<br>- [delete_edges](Edge.md#delete_edges)<br>- [delete_faces](Edge.md#delete_faces)|
|      | [Face](Face.md) | - [delete](Face.md#delete)<br>- [delete_all](Face.md#delete_all)<br>- [delete_edges](Face.md#delete_edges)<br>- [delete_faces](Face.md#delete_faces)|
|      | [Geometry](Geometry.md) | [delete](Geometry.md#delete) |
|      | [Instance](Instance.md) | [delete](Instance.md#delete) |
|      | [Mesh](Mesh.md) | - [delete_all](Mesh.md#delete_all)<br>- [delete_edges](Mesh.md#delete_edges)<br>- [delete_faces](Mesh.md#delete_faces)|
|      | [Spline](Spline.md) | [delete](Spline.md#delete) |
|      | [Vertex](Vertex.md) | - [delete](Vertex.md#delete)<br>- [delete_all](Vertex.md#delete_all)<br>- [delete_edges](Vertex.md#delete_edges)<br>- [delete_faces](Vertex.md#delete_faces)|
| [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Volume](Volume.md) | - [distribute_points](Volume.md#distribute_points)<br>- [distribute_points_random](Volume.md#distribute_points_random)<br>- [distribute_points_grid](Volume.md#distribute_points_grid)|
| [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Face](Face.md) | - [distribute_points_random](Face.md#distribute_points_random)<br>- [distribute_points_poisson](Face.md#distribute_points_poisson)|
|      | [Mesh](Mesh.md) | [distribute_points_on_faces](Mesh.md#distribute_points_on_faces) |
| [Domain Size](GeometryNodeAttributeDomainSize.md) | [CloudPoint](CloudPoint.md) | [count](CloudPoint.md#count) |
|      | [ControlPoint](ControlPoint.md) | [count](ControlPoint.md#count) |
|      | [Corner](Corner.md) | [count](Corner.md#count) |
|      | [Curve](Curve.md) | - [domain_size](Curve.md#domain_size)<br>- [point_count](Curve.md#point_count)<br>- [spline_count](Curve.md#spline_count)|
|      | [Edge](Edge.md) | [count](Edge.md#count) |
|      | [Face](Face.md) | [count](Face.md#count) |
|      | [Geometry](Geometry.md) | [domain_size](Geometry.md#domain_size) |
|      | [Instance](Instance.md) | [count](Instance.md#count) |
|      | [Instances](Instances.md) | [domain_size](Instances.md#domain_size) |
|      | [Mesh](Mesh.md) | [domain_size](Mesh.md#domain_size) / [point_count](Mesh.md#point_count) / [face_count](Mesh.md#face_count) / [edge_count](Mesh.md#edge_count) / [corner_count](Mesh.md#corner_count) / |
|      | [Points](Points.md) | [domain_size](Points.md#domain_size) |
|      | [Spline](Spline.md) | [count](Spline.md#count) |
|      | [Vertex](Vertex.md) | [count](Vertex.md#count) |
| [Dual Mesh](GeometryNodeDualMesh.md) | [Mesh](Mesh.md) | [dual_mesh](Mesh.md#dual_mesh) |
| [Duplicate Elements](GeometryNodeDuplicateElements.md) | [CloudPoint](CloudPoint.md) | [duplicate](CloudPoint.md#duplicate) |
|      | [ControlPoint](ControlPoint.md) | [duplicate](ControlPoint.md#duplicate) |
|      | [Edge](Edge.md) | [duplicate](Edge.md#duplicate) |
|      | [Face](Face.md) | [duplicate](Face.md#duplicate) |
|      | [Geometry](Geometry.md) | [duplicate](Geometry.md#duplicate) |
|      | [Instance](Instance.md) | [duplicate](Instance.md#duplicate) |
|      | [Spline](Spline.md) | [duplicate](Spline.md#duplicate) |
|      | [Vertex](Vertex.md) | [duplicate](Vertex.md#duplicate) |
| [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) | [Edge](Edge.md) | - [angle](Edge.md#angle)<br>- [unsigned_angle](Edge.md#unsigned_angle)<br>- [signed_angle](Edge.md#signed_angle)|
| [Edge Neighbors](GeometryNodeInputMeshEdgeNeighbors.md) | [Edge](Edge.md) | [neighbors](Edge.md#neighbors) |
| [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) | [Edge](Edge.md) | [edge_paths_to_curves](Edge.md#edge_paths_to_curves) |
|      | [Mesh](Mesh.md) | [edge_paths_to_curves](Mesh.md#edge_paths_to_curves) |
| [Edge Paths to Selection](GeometryNodeEdgePathsToSelection.md) | [Mesh](Mesh.md) | [edge_paths_to_selection](Mesh.md#edge_paths_to_selection) |
| [Edge Vertices](GeometryNodeInputMeshEdgeVertices.md) | [Edge](Edge.md) | - [vertices](Edge.md#vertices)<br>- [vertices_index](Edge.md#vertices_index)<br>- [vertices_position](Edge.md#vertices_position)|
| [Edges of Corner](GeometryNodeEdgesOfCorner.md) | [Corner](Corner.md) | - [edges](Corner.md#edges)<br>- [previous_vertex](Corner.md#previous_vertex)<br>- [next_vertex](Corner.md#next_vertex)|
|      | [Mesh](Mesh.md) | [edges_of_corner](Mesh.md#edges_of_corner) |
| [Edges of Vertex](GeometryNodeEdgesOfVertex.md) | [Mesh](Mesh.md) | [edges_of_vertex](Mesh.md#edges_of_vertex) |
|      | [Vertex](Vertex.md) | - [edges](Vertex.md#edges)<br>- [edges_index](Vertex.md#edges_index)<br>- [edges_total](Vertex.md#edges_total)|
| [Endpoint Selection](GeometryNodeCurveEndpointSelection.md) | [ControlPoint](ControlPoint.md) | [endpoint_selection](ControlPoint.md#endpoint_selection) |
| [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Edge](Edge.md) | [extrude](Edge.md#extrude) |
|      | [Face](Face.md) | [extrude](Face.md#extrude) |
|      | [Mesh](Mesh.md) | [extrude](Mesh.md#extrude) |
|      | [Vertex](Vertex.md) | [extrude](Vertex.md#extrude) |
| [Face Area](GeometryNodeInputMeshFaceArea.md) | [Face](Face.md) | [area](Face.md#area) |
| [Face is Planar](GeometryNodeInputMeshFaceIsPlanar.md) | [Face](Face.md) | [is_planar](Face.md#is_planar) |
|      | [Mesh](Mesh.md) | [face_is_planar](Mesh.md#face_is_planar) |
| [Face Neighbors](GeometryNodeInputMeshFaceNeighbors.md) | [Face](Face.md) | - [neighbors](Face.md#neighbors)<br>- [neighbors_vertex_count](Face.md#neighbors_vertex_count)<br>- [neighbors_face_count](Face.md#neighbors_face_count)|
| [Face of Corner](GeometryNodeFaceOfCorner.md) | [Corner](Corner.md) | - [face](Corner.md#face)<br>- [face_index](Corner.md#face_index)<br>- [index_in_face](Corner.md#index_in_face)|
|      | [Mesh](Mesh.md) | [face_of_corner](Mesh.md#face_of_corner) |
| [Face Set Boundaries](GeometryNodeMeshFaceSetBoundaries.md) | [Face](Face.md) | [face_set_boundaries](Face.md#face_set_boundaries) |
|      | [Mesh](Mesh.md) | [face_set_boundaries](Mesh.md#face_set_boundaries) |
| [Field at Index](GeometryNodeFieldAtIndex.md) | [Domain](Domain.md) | [field_at_index](Domain.md#field_at_index) |
|      | [Geometry](Geometry.md) | [field_at_index](Geometry.md#field_at_index) |
| [Fill Curve](GeometryNodeFillCurve.md) | [Curve](Curve.md) | - [fill](Curve.md#fill)<br>- [fill_triangles](Curve.md#fill_triangles)<br>- [fill_ngons](Curve.md#fill_ngons)|
| [Fillet Curve](GeometryNodeFilletCurve.md) | [Curve](Curve.md) | - [fillet](Curve.md#fillet)<br>- [fillet_bezier](Curve.md#fillet_bezier)<br>- [fillet_poly](Curve.md#fillet_poly)|
| [Flip Faces](GeometryNodeFlipFaces.md) | [Face](Face.md) | [flip](Face.md#flip) |
|      | [Mesh](Mesh.md) | [flip_faces](Mesh.md#flip_faces) |
| [Float Curve](ShaderNodeFloatCurve.md) | [Float](Float.md) | [float_curve](Float.md#float_curve) |
| [Float to Integer](FunctionNodeFloatToInt.md) | [Float](Float.md) | [to_integer](Float.md#to_integer) / [round](Float.md#round) / [floor](Float.md#floor) / [ceiling](Float.md#ceiling) / [truncate](Float.md#truncate) / |
| [Geometry Proximity](GeometryNodeProximity.md) | [CloudPoint](CloudPoint.md) | [proximity](CloudPoint.md#proximity) |
|      | [ControlPoint](ControlPoint.md) | [proximity](ControlPoint.md#proximity) |
|      | [Edge](Edge.md) | [proximity](Edge.md#proximity) |
|      | [Face](Face.md) | [proximity](Face.md#proximity) |
|      | [Geometry](Geometry.md) | - [proximity](Geometry.md#proximity)<br>- [proximity_points](Geometry.md#proximity_points)<br>- [proximity_edges](Geometry.md#proximity_edges)<br>- [proximity_faces](Geometry.md#proximity_faces)|
|      | [Vertex](Vertex.md) | [proximity](Vertex.md#proximity) |
| [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Geometry](Geometry.md) | [to_instance](Geometry.md#to_instance) |
|      | [functions](functions.md) | [geometry_to_instance](functions.md#geometry_to_instance) |
| [Gradient Texture](ShaderNodeTexGradient.md) | [Texture](Texture.md) | [gradient](Texture.md#gradient) / [gradient_linear](Texture.md#gradient_linear) / [gradient_quadratic](Texture.md#gradient_quadratic) / [gradient_easing](Texture.md#gradient_easing) / [gradient_diagonal](Texture.md#gradient_diagonal) / [gradient_spherical](Texture.md#gradient_spherical) / [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere) / [gradient_radial](Texture.md#gradient_radial) / |
| [Grid](GeometryNodeMeshGrid.md) | [Mesh](Mesh.md) | [Grid](Mesh.md#Grid) |
| [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [ControlPoint](ControlPoint.md) | [handle_type_selection_node](ControlPoint.md#handle_type_selection_node) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / |
| [ID](GeometryNodeInputID.md) | [Domain](Domain.md) | [ID](Domain.md#ID) |
|      | [Geometry](Geometry.md) | [ID](Geometry.md#ID) |
| [Ico Sphere](GeometryNodeMeshIcoSphere.md) | [Mesh](Mesh.md) | [IcoSphere](Mesh.md#IcoSphere) |
| [Image Texture](GeometryNodeImageTexture.md) | [Image](Image.md) | [texture](Image.md#texture) |
|      | [Texture](Texture.md) | [image](Texture.md#image) |
| [Index](GeometryNodeInputIndex.md) | [Domain](Domain.md) | - [index](Domain.md#index)<br>- [domain_index](Domain.md#domain_index)|
|      | [Geometry](Geometry.md) | [index](Geometry.md#index) |
| [Instance on Points](GeometryNodeInstanceOnPoints.md) | [CloudPoint](CloudPoint.md) | [instance_on_points](CloudPoint.md#instance_on_points) |
|      | [ControlPoint](ControlPoint.md) | [instance_on_points](ControlPoint.md#instance_on_points) |
|      | [Curve](Curve.md) | [instance_on_points](Curve.md#instance_on_points) |
|      | [Instances](Instances.md) | - [InstanceOnPoints](Instances.md#InstanceOnPoints)<br>- [on_points](Instances.md#on_points)|
|      | [Mesh](Mesh.md) | [instance_on_points](Mesh.md#instance_on_points) |
|      | [Points](Points.md) | [instance_on_points](Points.md#instance_on_points) |
|      | [Vertex](Vertex.md) | [instance_on_points](Vertex.md#instance_on_points) |
| [Instance Rotation](GeometryNodeInputInstanceRotation.md) | [Instance](Instance.md) | [rotation](Instance.md#rotation) |
|      | [Instances](Instances.md) | [rotation](Instances.md#rotation) |
| [Instance Scale](GeometryNodeInputInstanceScale.md) | [Instance](Instance.md) | [scale](Instance.md#scale) |
|      | [Instances](Instances.md) | [scale](Instances.md#scale) |
| [Instances to Points](GeometryNodeInstancesToPoints.md) | [Instance](Instance.md) | [to_points](Instance.md#to_points) |
|      | [Instances](Instances.md) | [to_points](Instances.md#to_points) |
| [Integer](FunctionNodeInputInt.md) | [Integer](Integer.md) | [Integer](Integer.md#Integer) |
| [Interpolate Domain](GeometryNodeFieldOnDomain.md) | [Domain](Domain.md) | [interpolate](Domain.md#interpolate) |
|      | [Geometry](Geometry.md) | [interpolate_domain](Geometry.md#interpolate_domain) |
| [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) | [Face](Face.md) | [shade_smooth](Face.md#shade_smooth) |
|      | [Mesh](Mesh.md) | [is_shade_smooth](Mesh.md#is_shade_smooth) |
| [Is Spline Cyclic](GeometryNodeInputSplineCyclic.md) | [Spline](Spline.md) | [cyclic](Spline.md#cyclic) |
| [Is Viewport](GeometryNodeIsViewport.md) | [Geometry](Geometry.md) | [is_viewport](Geometry.md#is_viewport) |
| [Join Geometry](GeometryNodeJoinGeometry.md) | [Geometry](Geometry.md) | [join](Geometry.md#join) |
|      | [functions](functions.md) | [join_geometry](functions.md#join_geometry) |
| [Join Strings](GeometryNodeStringJoin.md) | [String](String.md) | - [join](String.md#join)<br>- [string_join](String.md#string_join)|
|      | [functions](functions.md) | [join_strings](functions.md#join_strings) |
| [Magic Texture](ShaderNodeTexMagic.md) | [Texture](Texture.md) | [magic](Texture.md#magic) |
| [Map Range](ShaderNodeMapRange.md) | [Float](Float.md) | [map_range](Float.md#map_range) / [map_range_linear](Float.md#map_range_linear) / [map_range_stepped](Float.md#map_range_stepped) / [map_range_smooth](Float.md#map_range_smooth) / [map_range_smoother](Float.md#map_range_smoother) / |
|      | [Vector](Vector.md) | [map_range](Vector.md#map_range) / [map_range_linear](Vector.md#map_range_linear) / [map_range_stepped](Vector.md#map_range_stepped) / [map_range_smooth](Vector.md#map_range_smooth) / [map_range_smoother](Vector.md#map_range_smoother) / |
| [Material](GeometryNodeInputMaterial.md) | [Material](Material.md) | [Material](Material.md#Material) |
| [Material Index](GeometryNodeInputMaterialIndex.md) | [Face](Face.md) | [material_index](Face.md#material_index) |
|      | [Geometry](Geometry.md) | [material_index](Geometry.md#material_index) |
|      | [Spline](Spline.md) | [material_index](Spline.md#material_index) |
| [Material Selection](GeometryNodeMaterialSelection.md) | [Domain](Domain.md) | [material_selection](Domain.md#material_selection) |
|      | [Geometry](Geometry.md) | [material_selection](Geometry.md#material_selection) |
| [Math](ShaderNodeMath.md) | [Float](Float.md) | [multiply_add](Float.md#multiply_add) / [mul_add](Float.md#mul_add) / [power](Float.md#power) / [pow](Float.md#pow) / [logarithm](Float.md#logarithm) / [log](Float.md#log) / [sqrt](Float.md#sqrt) / [inverse_sqrt](Float.md#inverse_sqrt) / [absolute](Float.md#absolute) / [abs](Float.md#abs) / [exponent](Float.md#exponent) / [exp](Float.md#exp) / [minimum](Float.md#minimum) / [min](Float.md#min) / [maximum](Float.md#maximum) / [max](Float.md#max) / [math_less_than](Float.md#math_less_than) / [math_greater_than](Float.md#math_greater_than) / [sign](Float.md#sign) / [math_compare](Float.md#math_compare) / [smooth_minimum](Float.md#smooth_minimum) / [smooth_maximum](Float.md#smooth_maximum) / [math_round](Float.md#math_round) / [math_floor](Float.md#math_floor) / [math_ceil](Float.md#math_ceil) / [math_truncate](Float.md#math_truncate) / [math_trunc](Float.md#math_trunc) / [fraction](Float.md#fraction) / [fact](Float.md#fact) / [modulo](Float.md#modulo) / [wrap](Float.md#wrap) / [snap](Float.md#snap) / [ping_pong](Float.md#ping_pong) / [sine](Float.md#sine) / [sin](Float.md#sin) / [cosine](Float.md#cosine) / [cos](Float.md#cos) / [tangent](Float.md#tangent) / [tan](Float.md#tan) / [arcsine](Float.md#arcsine) / [arcsin](Float.md#arcsin) / [arccosine](Float.md#arccosine) / [arccos](Float.md#arccos) / [arctangent](Float.md#arctangent) / [arctan](Float.md#arctan) / [arctan2](Float.md#arctan2) / [sinh](Float.md#sinh) / [cosh](Float.md#cosh) / [tanh](Float.md#tanh) / [to_radians](Float.md#to_radians) / [to_degrees](Float.md#to_degrees) / |
|      | [Integer](Integer.md) | [multiply_add](Integer.md#multiply_add) / [mul_add](Integer.md#mul_add) / [power](Integer.md#power) / [pow](Integer.md#pow) / [logarithm](Integer.md#logarithm) / [log](Integer.md#log) / [sqrt](Integer.md#sqrt) / [inverse_sqrt](Integer.md#inverse_sqrt) / [absolute](Integer.md#absolute) / [abs](Integer.md#abs) / [exponent](Integer.md#exponent) / [exp](Integer.md#exp) / [minimum](Integer.md#minimum) / [min](Integer.md#min) / [maximum](Integer.md#maximum) / [max](Integer.md#max) / [math_less_than](Integer.md#math_less_than) / [math_greater_than](Integer.md#math_greater_than) / [sign](Integer.md#sign) / [math_compare](Integer.md#math_compare) / [smooth_minimum](Integer.md#smooth_minimum) / [smooth_maximum](Integer.md#smooth_maximum) / [math_round](Integer.md#math_round) / [math_floor](Integer.md#math_floor) / [math_ceil](Integer.md#math_ceil) / [math_truncate](Integer.md#math_truncate) / [math_trunc](Integer.md#math_trunc) / [fraction](Integer.md#fraction) / [fact](Integer.md#fact) / [modulo](Integer.md#modulo) / [wrap](Integer.md#wrap) / [snap](Integer.md#snap) / [ping_pong](Integer.md#ping_pong) / [sine](Integer.md#sine) / [sin](Integer.md#sin) / [cosine](Integer.md#cosine) / [cos](Integer.md#cos) / [tangent](Integer.md#tangent) / [tan](Integer.md#tan) / [arcsine](Integer.md#arcsine) / [arcsin](Integer.md#arcsin) / [arccosine](Integer.md#arccosine) / [arccos](Integer.md#arccos) / [arctangent](Integer.md#arctangent) / [arctan](Integer.md#arctan) / [arctan2](Integer.md#arctan2) / [sinh](Integer.md#sinh) / [cosh](Integer.md#cosh) / [tanh](Integer.md#tanh) / [to_radians](Integer.md#to_radians) / [to_degrees](Integer.md#to_degrees) / |
|      | [functions](functions.md) | [math](functions.md#math) / [multiply_add](functions.md#multiply_add) / [mul_add](functions.md#mul_add) / [power](functions.md#power) / [logarithm](functions.md#logarithm) / [log](functions.md#log) / [sqrt](functions.md#sqrt) / [inverse_sqrt](functions.md#inverse_sqrt) / [absolute](functions.md#absolute) / [abs](functions.md#abs) / [exponent](functions.md#exponent) / [exp](functions.md#exp) / [minimum](functions.md#minimum) / [min](functions.md#min) / [maximum](functions.md#maximum) / [max](functions.md#max) / [math_less_than](functions.md#math_less_than) / [math_greater_than](functions.md#math_greater_than) / [sign](functions.md#sign) / [math_compare](functions.md#math_compare) / [smooth_minimum](functions.md#smooth_minimum) / [smooth_maximum](functions.md#smooth_maximum) / [math_round](functions.md#math_round) / [math_floor](functions.md#math_floor) / [math_ceil](functions.md#math_ceil) / [math_truncate](functions.md#math_truncate) / [math_trun](functions.md#math_trun) / [fraction](functions.md#fraction) / [modulo](functions.md#modulo) / [wrap](functions.md#wrap) / [snap](functions.md#snap) / [ping_pong](functions.md#ping_pong) / [sine](functions.md#sine) / [sin](functions.md#sin) / [cosine](functions.md#cosine) / [cos](functions.md#cos) / [tangent](functions.md#tangent) / [tan](functions.md#tan) / [arcsine](functions.md#arcsine) / [arcsin](functions.md#arcsin) / [arccosine](functions.md#arccosine) / [arccos](functions.md#arccos) / [arctangent](functions.md#arctangent) / [arctan](functions.md#arctan) / [arctan2](functions.md#arctan2) / [sinh](functions.md#sinh) / [cosh](functions.md#cosh) / [tanh](functions.md#tanh) / [to_radians](functions.md#to_radians) / [to_degrees](functions.md#to_degrees) / |
| [Merge by Distance](GeometryNodeMergeByDistance.md) | [Geometry](Geometry.md) | [merge_by_distance](Geometry.md#merge_by_distance) |
|      | [Vertex](Vertex.md) | - [merge_by_distance](Vertex.md#merge_by_distance)<br>- [merge_by_distance_connected](Vertex.md#merge_by_distance_connected)|
| [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Mesh](Mesh.md) | - [boolean_intersect](Mesh.md#boolean_intersect)<br>- [boolean_union](Mesh.md#boolean_union)<br>- [boolean_difference](Mesh.md#boolean_difference)|
| [Mesh Circle](GeometryNodeMeshCircle.md) | [Mesh](Mesh.md) | [Circle](Mesh.md#Circle) |
| [Mesh Island](GeometryNodeInputMeshIsland.md) | [Face](Face.md) | - [island](Face.md#island)<br>- [island_index](Face.md#island_index)<br>- [island_count](Face.md#island_count)|
|      | [Mesh](Mesh.md) | - [island](Mesh.md#island)<br>- [island_index](Mesh.md#island_index)<br>- [island_count](Mesh.md#island_count)|
| [Mesh Line](GeometryNodeMeshLine.md) | [Mesh](Mesh.md) | - [Line](Mesh.md#Line)<br>- [LineEndPoints](Mesh.md#LineEndPoints)<br>- [LineEndPointsResolution](Mesh.md#LineEndPointsResolution)<br>- [LineOffset](Mesh.md#LineOffset)|
| [Mesh to Curve](GeometryNodeMeshToCurve.md) | [Edge](Edge.md) | [to_curve](Edge.md#to_curve) |
|      | [Mesh](Mesh.md) | [to_curve](Mesh.md#to_curve) |
| [Mesh to Points](GeometryNodeMeshToPoints.md) | [Mesh](Mesh.md) | [to_points](Mesh.md#to_points) |
|      | [Vertex](Vertex.md) | [to_points](Vertex.md#to_points) |
| [Mesh to Volume](GeometryNodeMeshToVolume.md) | [Mesh](Mesh.md) | [to_volume](Mesh.md#to_volume) |
|      | [Vertex](Vertex.md) | [to_volume](Vertex.md#to_volume) |
| [Mix](ShaderNodeMix.md) | [Color](Color.md) | [mix](Color.md#mix) / [mix_darken](Color.md#mix_darken) / [mix_multiply](Color.md#mix_multiply) / [mix_burn](Color.md#mix_burn) / [mix_lighten](Color.md#mix_lighten) / [mix_screen](Color.md#mix_screen) / [mix_dodge](Color.md#mix_dodge) / [mix_add](Color.md#mix_add) / [mix_overlay](Color.md#mix_overlay) / [mix_soft_light](Color.md#mix_soft_light) / [mix_linear_light](Color.md#mix_linear_light) / [mix_difference](Color.md#mix_difference) / [mix_subtract](Color.md#mix_subtract) / [mix_divide](Color.md#mix_divide) / [mix_hue](Color.md#mix_hue) / [mix_saturation](Color.md#mix_saturation) / [mix_color](Color.md#mix_color) / [mix_value](Color.md#mix_value) / |
|      | [Float](Float.md) | [mix](Float.md#mix) |
|      | [Vector](Vector.md) | - [mix](Vector.md#mix)<br>- [mix_uniform](Vector.md#mix_uniform)<br>- [mix_non_uniform](Vector.md#mix_non_uniform)|
|      | [functions](functions.md) | [float_mix](functions.md#float_mix) / [vector_mix](functions.md#vector_mix) / [color_mix](functions.md#color_mix) / [color_darken](functions.md#color_darken) / [color_multiply](functions.md#color_multiply) / [color_burn](functions.md#color_burn) / [color_lighten](functions.md#color_lighten) / [color_screen](functions.md#color_screen) / [color_dodge](functions.md#color_dodge) / [color_add](functions.md#color_add) / [color_overlay](functions.md#color_overlay) / [color_soft_light](functions.md#color_soft_light) / [color_linear_light](functions.md#color_linear_light) / [color_difference](functions.md#color_difference) / [color_subtract](functions.md#color_subtract) / [color_divide](functions.md#color_divide) / [color_hue](functions.md#color_hue) / [color_saturation](functions.md#color_saturation) / [color_color](functions.md#color_color) / [color_value](functions.md#color_value) / |
| [Musgrave Texture](ShaderNodeTexMusgrave.md) | [Texture](Texture.md) | [musgrave](Texture.md#musgrave) |
| [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Domain](Domain.md) | [named_attribute](Domain.md#named_attribute) / [named_float](Domain.md#named_float) / [named_integer](Domain.md#named_integer) / [named_vector](Domain.md#named_vector) / [named_color](Domain.md#named_color) / [named_boolean](Domain.md#named_boolean) / |
|      | [Geometry](Geometry.md) | [named_attribute](Geometry.md#named_attribute) / [named_float](Geometry.md#named_float) / [named_integer](Geometry.md#named_integer) / [named_vector](Geometry.md#named_vector) / [named_color](Geometry.md#named_color) / [named_boolean](Geometry.md#named_boolean) / |
| [Noise Texture](ShaderNodeTexNoise.md) | [Texture](Texture.md) | [noise](Texture.md#noise) / [noise_1D](Texture.md#noise_1D) / [noise_2D](Texture.md#noise_2D) / [noise_3D](Texture.md#noise_3D) / [noise_4D](Texture.md#noise_4D) / |
| [Normal](GeometryNodeInputNormal.md) | [Domain](Domain.md) | [normal](Domain.md#normal) |
|      | [Geometry](Geometry.md) | [normal](Geometry.md#normal) |
|      | [Spline](Spline.md) | [normal](Spline.md#normal) |
| [Object Info](GeometryNodeObjectInfo.md) | [Object](Object.md) | [info](Object.md#info) / [location](Object.md#location) / [rotation](Object.md#rotation) / [scale](Object.md#scale) / [geometry](Object.md#geometry) / |
| [Offset Corner in Face](GeometryNodeOffsetCornerInFace.md) | [Corner](Corner.md) | [offset_in_face](Corner.md#offset_in_face) |
|      | [Mesh](Mesh.md) | [offset_corner_in_face](Mesh.md#offset_corner_in_face) |
| [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) | [ControlPoint](ControlPoint.md) | [offset](ControlPoint.md#offset) |
|      | [Curve](Curve.md) | [offset_point](Curve.md#offset_point) |
| [Pack UV Islands](GeometryNodeUVPackIslands.md) | [Face](Face.md) | [pack_uv_islands](Face.md#pack_uv_islands) |
|      | [Mesh](Mesh.md) | [pack_uv_islands](Mesh.md#pack_uv_islands) |
| [Points](GeometryNodePoints.md) | [Points](Points.md) | [Points](Points.md#Points) |
| [Points of Curve](GeometryNodePointsOfCurve.md) | [Curve](Curve.md) | [points_of_curve](Curve.md#points_of_curve) |
|      | [Spline](Spline.md) | [points](Spline.md#points) |
| [Points to Vertices](GeometryNodePointsToVertices.md) | [CloudPoint](CloudPoint.md) | [to_vertices](CloudPoint.md#to_vertices) |
|      | [Points](Points.md) | [to_vertices](Points.md#to_vertices) |
| [Points to Volume](GeometryNodePointsToVolume.md) | [Points](Points.md) | - [to_volume](Points.md#to_volume)<br>- [to_volume_size](Points.md#to_volume_size)<br>- [to_volume_amount](Points.md#to_volume_amount)|
| [Position](GeometryNodeInputPosition.md) | [Domain](Domain.md) | [position](Domain.md#position) |
|      | [Geometry](Geometry.md) | [position](Geometry.md#position) |
| [Quadratic Bezier](GeometryNodeCurveQuadraticBezier.md) | [Curve](Curve.md) | [QuadraticBezier](Curve.md#QuadraticBezier) |
| [Quadrilateral](GeometryNodeCurvePrimitiveQuadrilateral.md) | [Curve](Curve.md) | [Quadrilateral](Curve.md#Quadrilateral) |
| [Radius](GeometryNodeInputRadius.md) | [CloudPoint](CloudPoint.md) | [radius](CloudPoint.md#radius) |
|      | [ControlPoint](ControlPoint.md) | [radius](ControlPoint.md#radius) |
|      | [Geometry](Geometry.md) | [radius](Geometry.md#radius) |
| [Random Value](FunctionNodeRandomValue.md) | [Boolean](Boolean.md) | [Random](Boolean.md#Random) |
|      | [Domain](Domain.md) | - [random_float](Domain.md#random_float)<br>- [random_integer](Domain.md#random_integer)<br>- [random_vector](Domain.md#random_vector)<br>- [random_boolean](Domain.md#random_boolean)|
|      | [Float](Float.md) | [Random](Float.md#Random) |
|      | [Geometry](Geometry.md) | - [random_float](Geometry.md#random_float)<br>- [random_integer](Geometry.md#random_integer)<br>- [random_vector](Geometry.md#random_vector)<br>- [random_boolean](Geometry.md#random_boolean)|
|      | [Integer](Integer.md) | [Random](Integer.md#Random) |
|      | [Vector](Vector.md) | [Random](Vector.md#Random) |
|      | [functions](functions.md) | - [random_float](functions.md#random_float)<br>- [random_integer](functions.md#random_integer)<br>- [random_vector](functions.md#random_vector)<br>- [random_boolean](functions.md#random_boolean)|
| [Raycast](GeometryNodeRaycast.md) | [Geometry](Geometry.md) | - [raycast](Geometry.md#raycast)<br>- [raycast_interpolated](Geometry.md#raycast_interpolated)<br>- [raycast_nearest](Geometry.md#raycast_nearest)|
| [Realize Instances](GeometryNodeRealizeInstances.md) | [Instances](Instances.md) | [realize](Instances.md#realize) |
| [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Domain](Domain.md) | [remove_named_attribute](Domain.md#remove_named_attribute) |
|      | [Geometry](Geometry.md) | [remove_named_attribute](Geometry.md#remove_named_attribute) |
| [Replace Material](GeometryNodeReplaceMaterial.md) | [Geometry](Geometry.md) | [replace_material](Geometry.md#replace_material) |
| [Replace String](FunctionNodeReplaceString.md) | [String](String.md) | [replace](String.md#replace) |
|      | [functions](functions.md) | [replace_string](functions.md#replace_string) |
| [Resample Curve](GeometryNodeResampleCurve.md) | [Curve](Curve.md) | - [resample](Curve.md#resample)<br>- [resample_count](Curve.md#resample_count)<br>- [resample_length](Curve.md#resample_length)<br>- [resample_evaluated](Curve.md#resample_evaluated)|
|      | [Spline](Spline.md) | - [resample](Spline.md#resample)<br>- [resample_count](Spline.md#resample_count)<br>- [resample_length](Spline.md#resample_length)<br>- [resample_evaluated](Spline.md#resample_evaluated)|
| [Reverse Curve](GeometryNodeReverseCurve.md) | [Curve](Curve.md) | [reverse](Curve.md#reverse) |
| [RGB Curves](ShaderNodeRGBCurve.md) | [Color](Color.md) | [rgb_curves](Color.md#rgb_curves) |
|      | [functions](functions.md) | [rgb_curves](functions.md#rgb_curves) |
| [Rotate Euler](FunctionNodeRotateEuler.md) | [functions](functions.md) | - [rotate_euler](functions.md#rotate_euler)<br>- [rotate_axis_angle](functions.md#rotate_axis_angle)|
| [Rotate Instances](GeometryNodeRotateInstances.md) | [Instance](Instance.md) | [rotate](Instance.md#rotate) |
|      | [Instances](Instances.md) | [rotate](Instances.md#rotate) |
| [Sample Curve](GeometryNodeSampleCurve.md) | [Curve](Curve.md) | [sample](Curve.md#sample) |
| [Sample Index](GeometryNodeSampleIndex.md) | [Domain](Domain.md) | [sample_index](Domain.md#sample_index) |
|      | [Geometry](Geometry.md) | [sample_index](Geometry.md#sample_index) |
| [Sample Nearest](GeometryNodeSampleNearest.md) | [Corner](Corner.md) | [sample_nearest](Corner.md#sample_nearest) |
|      | [Edge](Edge.md) | [sample_nearest](Edge.md#sample_nearest) |
|      | [Face](Face.md) | [sample_nearest](Face.md#sample_nearest) |
|      | [Geometry](Geometry.md) | [sample_nearest](Geometry.md#sample_nearest) |
|      | [Vertex](Vertex.md) | [sample_nearest](Vertex.md#sample_nearest) |
| [Sample Nearest Surface](GeometryNodeSampleNearestSurface.md) | [Mesh](Mesh.md) | [sample_nearest_surface](Mesh.md#sample_nearest_surface) |
| [Sample UV Surface](GeometryNodeSampleUVSurface.md) | [Mesh](Mesh.md) | [sample_uv_surface](Mesh.md#sample_uv_surface) |
| [Scale Elements](GeometryNodeScaleElements.md) | [Edge](Edge.md) | - [scale_uniform](Edge.md#scale_uniform)<br>- [scale_single_axis](Edge.md#scale_single_axis)|
|      | [Face](Face.md) | - [scale_uniform](Face.md#scale_uniform)<br>- [scale_single_axis](Face.md#scale_single_axis)|
|      | [Mesh](Mesh.md) | - [scale_elements](Mesh.md#scale_elements)<br>- [scale_uniform](Mesh.md#scale_uniform)<br>- [scale_single_axis](Mesh.md#scale_single_axis)|
| [Scale Instances](GeometryNodeScaleInstances.md) | [Instance](Instance.md) | [set_scale](Instance.md#set_scale) |
|      | [Instances](Instances.md) | [set_scale](Instances.md#set_scale) |
| [Scene Time](GeometryNodeInputSceneTime.md) | [Float](Float.md) | - [Seconds](Float.md#Seconds)<br>- [Frame](Float.md#Frame)|
| [Self Object](GeometryNodeSelfObject.md) | [Object](Object.md) | [Self](Object.md#Self) |
| [Separate Color](FunctionNodeSeparateColor.md) | [Color](Color.md) | [separate_color](Color.md#separate_color) |
|      | [functions](functions.md) | - [separate_rgb](functions.md#separate_rgb)<br>- [separate_hsv](functions.md#separate_hsv)<br>- [separate_hsl](functions.md#separate_hsl)|
| [Separate Components](GeometryNodeSeparateComponents.md) | [Geometry](Geometry.md) | [separate_components](Geometry.md#separate_components) / [mesh_component](Geometry.md#mesh_component) / [curve_component](Geometry.md#curve_component) / [points_component](Geometry.md#points_component) / [volume_component](Geometry.md#volume_component) / [instances_component](Geometry.md#instances_component) / |
| [Separate Geometry](GeometryNodeSeparateGeometry.md) | [ControlPoint](ControlPoint.md) | [separate](ControlPoint.md#separate) |
|      | [Edge](Edge.md) | [separate](Edge.md#separate) |
|      | [Face](Face.md) | [separate](Face.md#separate) |
|      | [Geometry](Geometry.md) | [separate](Geometry.md#separate) |
|      | [Instance](Instance.md) | [separate](Instance.md#separate) |
|      | [Spline](Spline.md) | [separate](Spline.md#separate) |
|      | [Vertex](Vertex.md) | [separate](Vertex.md#separate) |
| [Separate XYZ](ShaderNodeSeparateXYZ.md) | [Vector](Vector.md) | [separate](Vector.md#separate) |
| [Set Curve Normal](GeometryNodeSetCurveNormal.md) | [Spline](Spline.md) | - [set_normal](Spline.md#set_normal)<br>- [normal](Spline.md#normal)|
| [Set Curve Radius](GeometryNodeSetCurveRadius.md) | [ControlPoint](ControlPoint.md) | - [set_radius](ControlPoint.md#set_radius)<br>- [radius](ControlPoint.md#radius)|
| [Set Curve Tilt](GeometryNodeSetCurveTilt.md) | [ControlPoint](ControlPoint.md) | - [set_tilt](ControlPoint.md#set_tilt)<br>- [tilt](ControlPoint.md#tilt)|
| [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [ControlPoint](ControlPoint.md) | [set_handle_positions](ControlPoint.md#set_handle_positions) / [set_handle_positions_left](ControlPoint.md#set_handle_positions_left) / [set_handle_positions_right](ControlPoint.md#set_handle_positions_right) / [left_handle_positions](ControlPoint.md#left_handle_positions) / [right_handle_positions](ControlPoint.md#right_handle_positions) / |
| [Set Handle Type](GeometryNodeCurveSetHandles.md) | [ControlPoint](ControlPoint.md) | - [set_handle_type_node](ControlPoint.md#set_handle_type_node)<br>- [set_handle_type](ControlPoint.md#set_handle_type)|
| [Set ID](GeometryNodeSetID.md) | [Domain](Domain.md) | - [set_ID](Domain.md#set_ID)<br>- [ID](Domain.md#ID)|
|      | [Geometry](Geometry.md) | [set_ID](Geometry.md#set_ID) |
| [Set Material](GeometryNodeSetMaterial.md) | [Face](Face.md) | - [set_material](Face.md#set_material)<br>- [material](Face.md#material)<br>- [material](Face.md#material)|
|      | [Geometry](Geometry.md) | [set_material](Geometry.md#set_material) |
|      | [Spline](Spline.md) | - [set_material](Spline.md#set_material)<br>- [material](Spline.md#material)<br>- [material](Spline.md#material)|
| [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Face](Face.md) | - [set_material_index](Face.md#set_material_index)<br>- [material_index](Face.md#material_index)|
|      | [Geometry](Geometry.md) | [set_material_index](Geometry.md#set_material_index) |
|      | [Spline](Spline.md) | - [set_material_index](Spline.md#set_material_index)<br>- [material_index](Spline.md#material_index)|
| [Set Point Radius](GeometryNodeSetPointRadius.md) | [CloudPoint](CloudPoint.md) | [radius](CloudPoint.md#radius) |
|      | [Points](Points.md) | [set_point_radius](Points.md#set_point_radius) |
| [Set Position](GeometryNodeSetPosition.md) | [Domain](Domain.md) | - [set_position](Domain.md#set_position)<br>- [position](Domain.md#position)|
|      | [Geometry](Geometry.md) | [set_position](Geometry.md#set_position) |
| [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Face](Face.md) | - [set_shade_smooth](Face.md#set_shade_smooth)<br>- [shade_smooth](Face.md#shade_smooth)|
|      | [Mesh](Mesh.md) | [set_shade_smooth](Mesh.md#set_shade_smooth) |
| [Set Spline Cyclic](GeometryNodeSetSplineCyclic.md) | [Spline](Spline.md) | - [set_cyclic](Spline.md#set_cyclic)<br>- [cyclic](Spline.md#cyclic)|
| [Set Spline Resolution](GeometryNodeSetSplineResolution.md) | [Spline](Spline.md) | - [set_resolution](Spline.md#set_resolution)<br>- [resolution](Spline.md#resolution)|
| [Set Spline Type](GeometryNodeCurveSplineType.md) | [Spline](Spline.md) | - [set_type](Spline.md#set_type)<br>- [type](Spline.md#type)<br>- [type](Spline.md#type)|
| [Shortest Edge Paths](GeometryNodeInputShortestEdgePaths.md) | [Mesh](Mesh.md) | [shortest_edge_paths](Mesh.md#shortest_edge_paths) |
| [Slice String](FunctionNodeSliceString.md) | [String](String.md) | [slice](String.md#slice) |
|      | [functions](functions.md) | [slice_string](functions.md#slice_string) |
| [Special Characters](FunctionNodeInputSpecialCharacters.md) | [String](String.md) | - [LineBreak](String.md#LineBreak)<br>- [Tab](String.md#Tab)|
| [Spiral](GeometryNodeCurveSpiral.md) | [Curve](Curve.md) | [Spiral](Curve.md#Spiral) |
| [Spline Length](GeometryNodeSplineLength.md) | [Spline](Spline.md) | [length](Spline.md#length) |
| [Spline Parameter](GeometryNodeSplineParameter.md) | [ControlPoint](ControlPoint.md) | - [parameter](ControlPoint.md#parameter)<br>- [parameter_factor](ControlPoint.md#parameter_factor)<br>- [parameter_length](ControlPoint.md#parameter_length)<br>- [parameter_index](ControlPoint.md#parameter_index)|
| [Spline Resolution](GeometryNodeInputSplineResolution.md) | [Spline](Spline.md) | [resolution](Spline.md#resolution) |
| [Split Edges](GeometryNodeSplitEdges.md) | [Edge](Edge.md) | [split](Edge.md#split) |
|      | [Mesh](Mesh.md) | [split_edges](Mesh.md#split_edges) |
| [Star](GeometryNodeCurveStar.md) | [Curve](Curve.md) | [Star](Curve.md#Star) |
| [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Domain](Domain.md) | [store_named_attribute_no_selection](Domain.md#store_named_attribute_no_selection) |
|      | [Geometry](Geometry.md) | [store_named_attribute](Geometry.md#store_named_attribute) / [store_named_boolean](Geometry.md#store_named_boolean) / [store_named_integer](Geometry.md#store_named_integer) / [store_named_float](Geometry.md#store_named_float) / [store_named_vector](Geometry.md#store_named_vector) / [store_named_color](Geometry.md#store_named_color) / |
| [String](FunctionNodeInputString.md) | [String](String.md) | [String](String.md#String) |
| [String Length](FunctionNodeStringLength.md) | [String](String.md) | [length](String.md#length) |
|      | [functions](functions.md) | [string_length](functions.md#string_length) |
| [String to Curves](GeometryNodeStringToCurves.md) | [String](String.md) | [to_curves](String.md#to_curves) |
|      | [functions](functions.md) | [string_to_curves](functions.md#string_to_curves) |
| [Subdivide Curve](GeometryNodeSubdivideCurve.md) | [Curve](Curve.md) | [subdivide](Curve.md#subdivide) |
| [Subdivide Mesh](GeometryNodeSubdivideMesh.md) | [Mesh](Mesh.md) | [subdivide](Mesh.md#subdivide) |
| [Subdivision Surface](GeometryNodeSubdivisionSurface.md) | [Mesh](Mesh.md) | [subdivision_surface](Mesh.md#subdivision_surface) |
| [Switch](GeometryNodeSwitch.md) | [Boolean](Boolean.md) | [switch](Boolean.md#switch) |
|      | [Collection](Collection.md) | [switch](Collection.md#switch) |
|      | [Color](Color.md) | [switch](Color.md#switch) |
|      | [Float](Float.md) | [switch](Float.md#switch) |
|      | [Geometry](Geometry.md) | [switch](Geometry.md#switch) |
|      | [Image](Image.md) | [switch](Image.md#switch) |
|      | [Integer](Integer.md) | [switch](Integer.md#switch) |
|      | [Material](Material.md) | [switch](Material.md#switch) |
|      | [Object](Object.md) | [switch](Object.md#switch) |
|      | [String](String.md) | [switch](String.md#switch) |
|      | [Texture](Texture.md) | [switch](Texture.md#switch) |
|      | [Vector](Vector.md) | [switch](Vector.md#switch) |
|      | [functions](functions.md) | [switch](functions.md#switch) / [switch_float](functions.md#switch_float) / [switch_integer](functions.md#switch_integer) / [switch_boolean](functions.md#switch_boolean) / [switch_vector](functions.md#switch_vector) / [switch_string](functions.md#switch_string) / [switch_color](functions.md#switch_color) / [switch_object](functions.md#switch_object) / [switch_image](functions.md#switch_image) / [switch_geometry](functions.md#switch_geometry) / [switch_collection](functions.md#switch_collection) / [switch_texture](functions.md#switch_texture) / [switch_material](functions.md#switch_material) / |
| [Transform](GeometryNodeTransform.md) | [Geometry](Geometry.md) | [transform](Geometry.md#transform) |
| [Translate Instances](GeometryNodeTranslateInstances.md) | [Instance](Instance.md) | [translate](Instance.md#translate) |
|      | [Instances](Instances.md) | [translate](Instances.md#translate) |
| [Triangulate](GeometryNodeTriangulate.md) | [Face](Face.md) | [triangulate](Face.md#triangulate) |
|      | [Mesh](Mesh.md) | [triangulate](Mesh.md#triangulate) |
| [Trim Curve](GeometryNodeTrimCurve.md) | [Curve](Curve.md) | - [trim](Curve.md#trim)<br>- [trim_factor](Curve.md#trim_factor)<br>- [trim_length](Curve.md#trim_length)|
| [UV Sphere](GeometryNodeMeshUVSphere.md) | [Mesh](Mesh.md) | [UVSphere](Mesh.md#UVSphere) |
| [UV Unwrap](GeometryNodeUVUnwrap.md) | [Face](Face.md) | [uv_unwrap](Face.md#uv_unwrap) |
|      | [Mesh](Mesh.md) | [uv_unwrap](Mesh.md#uv_unwrap) |
| [Value](ShaderNodeValue.md) | [Float](Float.md) | [Value](Float.md#Value) |
| [Value to String](FunctionNodeValueToString.md) | [Float](Float.md) | [to_string](Float.md#to_string) |
|      | [Integer](Integer.md) | [to_string](Integer.md#to_string) |
|      | [functions](functions.md) | [value_to_string](functions.md#value_to_string) |
| [Vector](FunctionNodeInputVector.md) | [Vector](Vector.md) | [Vector](Vector.md#Vector) |
| [Vector Curves](ShaderNodeVectorCurve.md) | [Vector](Vector.md) | [curves](Vector.md#curves) |
| [Vector Math](ShaderNodeVectorMath.md) | [Vector](Vector.md) | [add](Vector.md#add) / [subtract](Vector.md#subtract) / [sub](Vector.md#sub) / [multiply](Vector.md#multiply) / [mul](Vector.md#mul) / [divide](Vector.md#divide) / [div](Vector.md#div) / [multiply_add](Vector.md#multiply_add) / [mul_add](Vector.md#mul_add) / [cross_product](Vector.md#cross_product) / [cross](Vector.md#cross) / [project](Vector.md#project) / [reflect](Vector.md#reflect) / [refract](Vector.md#refract) / [face_forward](Vector.md#face_forward) / [dot_product](Vector.md#dot_product) / [dot](Vector.md#dot) / [distance](Vector.md#distance) / [length](Vector.md#length) / [scale](Vector.md#scale) / [normalize](Vector.md#normalize) / [absolute](Vector.md#absolute) / [abs](Vector.md#abs) / [minimum](Vector.md#minimum) / [min](Vector.md#min) / [maximum](Vector.md#maximum) / [max](Vector.md#max) / [floor](Vector.md#floor) / [ceil](Vector.md#ceil) / [fraction](Vector.md#fraction) / [fract](Vector.md#fract) / [modulo](Vector.md#modulo) / [wrap](Vector.md#wrap) / [snap](Vector.md#snap) / [sine](Vector.md#sine) / [sin](Vector.md#sin) / [cosine](Vector.md#cosine) / [cos](Vector.md#cos) / [tangent](Vector.md#tangent) / [tan](Vector.md#tan) / |
| [Vector Rotate](ShaderNodeVectorRotate.md) | [Vector](Vector.md) | [rotate_euler](Vector.md#rotate_euler) / [rotate_axis_angle](Vector.md#rotate_axis_angle) / [rotate_x](Vector.md#rotate_x) / [rotate_y](Vector.md#rotate_y) / [rotate_z](Vector.md#rotate_z) / |
| [Vertex Neighbors](GeometryNodeInputMeshVertexNeighbors.md) | [Vertex](Vertex.md) | - [neighbors](Vertex.md#neighbors)<br>- [neighbors_vertex_count](Vertex.md#neighbors_vertex_count)<br>- [neighbors_face_count](Vertex.md#neighbors_face_count)|
| [Vertex of Corner](GeometryNodeVertexOfCorner.md) | [Corner](Corner.md) | [vertex_index](Corner.md#vertex_index) |
|      | [Mesh](Mesh.md) | [vertex_of_corner](Mesh.md#vertex_of_corner) |
| [Viewer](GeometryNodeViewer.md) | [Domain](Domain.md) | - [viewer](Domain.md#viewer)<br>- [view](Domain.md#view)|
|      | [Geometry](Geometry.md) | - [viewer](Geometry.md#viewer)<br>- [view](Geometry.md#view)|
| [Volume Cube](GeometryNodeVolumeCube.md) | [Volume](Volume.md) | [Cube](Volume.md#Cube) |
| [Volume to Mesh](GeometryNodeVolumeToMesh.md) | [Volume](Volume.md) | [to_mesh](Volume.md#to_mesh) |
| [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Texture](Texture.md) | [voronoi](Texture.md#voronoi) / [voronoi_1D](Texture.md#voronoi_1D) / [voronoi_2D](Texture.md#voronoi_2D) / [voronoi_3D](Texture.md#voronoi_3D) / [voronoi_4D](Texture.md#voronoi_4D) / |
| [Wave Texture](ShaderNodeTexWave.md) | [Texture](Texture.md) | [wave](Texture.md#wave) / [wave_bands](Texture.md#wave_bands) / [wave_rings](Texture.md#wave_rings) / [wave_bands_sine](Texture.md#wave_bands_sine) / [wave_bands_saw](Texture.md#wave_bands_saw) / [wave_bands_triangle](Texture.md#wave_bands_triangle) / [wave_rings_sine](Texture.md#wave_rings_sine) / [wave_rings_saw](Texture.md#wave_rings_saw) / [wave_rings_triangle](Texture.md#wave_rings_triangle) / |
| [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Texture](Texture.md) | [white_noise](Texture.md#white_noise) / [white_noise_1D](Texture.md#white_noise_1D) / [white_noise_2D](Texture.md#white_noise_2D) / [white_noise_3D](Texture.md#white_noise_3D) / [white_noise_4D](Texture.md#white_noise_4D) / |

