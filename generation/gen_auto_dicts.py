from pathlib import Path
import bpy

from . node_explore import NodeInfo

f            = 'func'
name         = 'func_name'
ret          = 'ret'
klass        = 'class_name'
cache        = 'cache'
parameters   = 'parameters'
domain_param = 'domain_param'
param_loop   = 'param_loop'
prefix       = 'prefix'
suffix       = 'suffix'
operation    = 'operation'
self_        = 'self_'
domain       = 'domain_value'
only_enabled = 'only_enabled'
rename       = 'rename'
is_cm        = 'is_class_method'
check        = 'check_existing'
ign_sock     = 'ignore_sockets'
jump         = 'jump_method'

setter       = 'setter'
getter       = 'getter'
in_socket    = 'in_socket'
in_prm       = 'in_parameter'
out_socket   = 'out_socket'
set_prm      = 'setter_params'
get_prm      = 'getter_params'
set_sock     = 'setter_sockets'
get_sock     = 'getter_sockets'


GEONODES = {
'Align Rotation to Vector' :    [{f: 'C', name: 'AlignToVector',  ign_sock: {'Rotation'}},
                                 {f: 'C', name: 'AlignXToVector', ign_sock: {'Rotation'}, parameters: {'axis': 'X'}},
                                 {f: 'C', name: 'AlignYToVector', ign_sock: {'Rotation'}, parameters: {'axis': 'Y'}},
                                 {f: 'C', name: 'AlignZToVector', ign_sock: {'Rotation'}, parameters: {'axis': 'Z'}},
                                 {name: 'align_toVector'},
                                 {name: 'align_x_to_vector', parameters: {'axis': 'X'}},
                                 {name: 'align_y_to_vector', parameters: {'axis': 'Y'}},
                                 {name: 'align_z_to_vector', parameters: {'axis': 'Z'}},
                                ],
'Axes to Rotation'   :          [{f: 'C',   name: 'FromAxes'},
                                 {f: 'C', name: 'FromXYAxes', parameters: {'primary_axis': 'X', 'secondary_axis': 'Y'}},
                                 {f: 'C', name: 'FromYXAxes', parameters: {'primary_axis': 'Y', 'secondary_axis': 'X'}},
                                 {f: 'C', name: 'FromXZAxes', parameters: {'primary_axis': 'X', 'secondary_axis': 'Z'}},
                                 {f: 'C', name: 'FromZXAxes', parameters: {'primary_axis': 'Z', 'secondary_axis': 'X'}},
                                 {f: 'C', name: 'FromYZAxes', parameters: {'primary_axis': 'Y', 'secondary_axis': 'Z'}},
                                 {f: 'C', name: 'FromZYAxes', parameters: {'primary_axis': 'Z', 'secondary_axis': 'Y'}},
                                ],
'Axis Angle to Rotation' :      [{f: 'C', name: 'FromAxisAngle'}],
'Boolean Math'       :          [{f: 'op', rename: {
                                        'and'      : 'band',
                                        'or'       : 'bor',
                                        'not'      : 'bnot',
                                        'nand'     : 'not_and',
                                }},
                                {f: 'math', rename: {
                                        'and'      : 'band',
                                        'or'       : 'bor',
                                        'not'      : 'bnot',
                                        'nand'     : 'not_and',
                                }},
                                ],
'Combine Color'      :          [{f: 'C', name: 'Combine', 'mode_loop': True}],
'Combine Matrix'     :          [{f: 'C', name: 'Combine'}],
'Combine Transform'  :          [{f: 'C', name: 'CombineTransform'}],
'Compare'            :          [{f: 'op', parameters: {'data_type': 'FLOAT',  'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'INT',    'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'VECTOR', 'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'STRING', 'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'RGBA',   'mode': 'ELEMENT'}},
                                ],
'Euler to Rotation'  :          [{f: 'C', name: 'FromEuler'}, {f: 'method', name: 'to_rotation'}],
'Find in String'     :          [{}, {name: 'find'}],
'Float to Integer'   :          [{name: 'to_integer'}],
'Hash Value'         :          [{}],
'Boolean'            :          [{f: 'INIT'}],
'Color'              :          [{f: 'INIT'}],
'Integer'            :          [{f: 'INIT'}],
'Rotation'           :          [{f: 'INIT'}],
'Special Characters' :          [{f: 'get', klass: 'String', ret: 'NODE'},
                                 {f: 'get', name: 'line_break', klass: 'String'},
                                 {f: 'get', name: 'tab', klass: 'String', ret: 'tab'},
                                ],
'String'             :          [{f: 'INIT'}],
'Vector'             :          [{f: 'INIT'}],
'Integer Math'       :          [{f: 'op', rename: {
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'absolute'     : 'abs',
                                }},
                                {f: 'math', rename: {
                                        'minimum'      : 'imin',
                                        'maximum'      : 'imax',
                                        'absolute'     : 'iabs',
                                        'add'          : 'iadd',
                                        'subtract'     : 'isubtract',
                                        'multiply'     : 'imultiply',
                                        'divide'       : 'idivide',
                                        'multiply_add' : 'imultiply_add',
                                        'power'        : 'ipower',
                                        'sign'         : 'isign',
                                        'modulo'       : 'imodulo',
                                        'floored_modulo' : 'ifloored_modulo',
                                }},
                                ],
'Invert Matrix'      :          [{name: 'invert'}],
'Invert Rotation'    :          [{name: 'invert'}],
'Matrix Determinant' :          [{f: 'get',    name: 'determinant'}],
'Multiply Matrices'  :          [{name: 'multiply'}],
'Project Point'      :          [{self_: 'Transform'}],
'Quaternion to Rotation' :      [{f: 'C', name: 'FromQuaternion'}],
'Random Value'       :          [{f: 'C', name: 'Random'}],
'Replace String'     :          [{name: 'replace'}],
'Rotate Rotation'    :          [{name: 'rotate'},
                                 {param_loop: 'rotation_space', prefix: 'rotate_'},
                                ],
'Rotate Vector'      :          [{self_: 'Rotation'}],
'Rotation to Axis Angle' :      [{name: 'to_axis_angle'},
                                 {f: 'get', name: 'axis_angle', ret: 'TUPLE'},
                                ],
'Rotation to Euler'  :          [{name: 'to_euler'}],
'Rotation to Quaternion' :      [{name: 'to_quaternion'},
                                 {f: 'get', name: 'wxyz', ret: 'TUPLE'},
                                ],
'Separate Color'     :          [{f: 'get', name: 'separate', cache: True, check: False},
                                 {f: 'get', name:'rgb', ret: 'TUPLE', cache: True, parameters: {'mode': 'RGB'}, check: False},
                                 {f: 'get', name:'hsv', ret: 'TUPLE', cache: True, parameters: {'mode': 'HSV'}, check: False},
                                 {f: 'get', name:'hsv', ret: 'TUPLE', cache: True, parameters: {'mode': 'HSL'}, check: False},
                                 {f: 'get_out_loop', parameters: {'mode': 'HSL'}, check: False},
                                 {f: 'get_out_loop', parameters: {'mode': 'HSV'}, check: False},
                                 {f: 'get_out_loop', parameters: {'mode': 'RGB'}, check: False},
                                ],
'Separate Matrix'    :          [{f: 'get', name: 'separate', cache: True, ret: 'TUPLE'},
                                 {f: 'get_out_loop', prefix: ''},
                                ],
'Separate Transform' :          [{f: 'get', name: 'trs', ret: 'TUPLE'},
                                 {f: 'get_out_loop', prefix: ''},
                                ],
'Slice String'       :          [{name: 'slice'}],
'String Length'      :          [{f: 'get', name: 'length'}],
'Transform Direction' :         [{self_: 'Transform'}],
'Transform Point'    :          [{self_: 'Transform'}],
'Transpose Matrix'   :          [{name: 'transpose'}],
'Value to String'    :          [{name: 'to_string'}],
'Accumulate Field'   :          [{'data_type_loop': False}],
'Domain Size'        :          [{f: 'get', cache: True, ret: 'NODE', klass: 'Mesh',         parameters: {'component': 'MESH'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'Curve',        parameters: {'component': 'CURVE'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'Cloud',        parameters: {'component': 'POINTCLOUD'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'Instances',    parameters: {'component': 'INSTANCES'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'GreasePencil', parameters: {'component': 'GREASEPENCIL'}},
                                ],
'Attribute Statistic' :         [{ret: 'NODE'}],
'Bake'               :          [{f: 'MANUAL'}],
'Blur Attribute'     :          [{name: 'blur'}],
'Bounding Box'       :          [{f: 'get'}],
'Capture Attribute'  :          [{f: 'MANUAL'}],
'Collection Info'    :          [{name: 'info', cache: True}],
'Convex Hull'        :          [{f: 'get'}],
'Corners of Edge'    :          [{klass: 'Mesh'}, {f: 'get_out_loop', klass: 'Edge',   name: 'corners', rename: {'total': 'corners_total'}}],
'Corners of Face'    :          [{klass: 'Mesh'}, {f: 'get_out_loop', klass: 'Face',   name: 'corners', rename: {'total': 'corners_total'}}],
'Corners of Vertex'  :          [{klass: 'Mesh'}, {f: 'get_out_loop', klass: 'Vertex', name: 'corners', rename: {'total': 'corners_total'}}],
'Arc'                :          [{f: 'C', name: 'Arc'}],
'Endpoint Selection' :          [{klass: 'Curve'}],
'Handle Type Selection' :       [{klass: 'Curve'}],
'Curve Length'       :          [{name: 'length'}],
'Curve of Point'     :          [{klass: 'Curve'}, {f: 'get_out_loop', klass: 'SplinePoint'}],
'Bézier Segment'     :          [{f: 'C', name: 'BezierSegment'}],
'Curve Circle'       :          [{f: 'C', name: 'Circle'}],
'Curve Line'         :          [{f: 'C', name: 'Line'}],
'Quadrilateral'      :          [{f: 'C'}],
'Quadratic Bézier'   :          [{f: 'C', name: 'QuadraticBezier'}],
'Set Handle Type'    :          [{},
                                 {name: 'set_left_handle_type',  parameters: {'mode': {'LEFT'}}},
                                 {name: 'set_right_handle_type', parameters: {'mode': {'RIGHT'}}},
                                 {name: 'set_both_handle_type',  parameters: {'mode': {'LEFT', 'RIGHT'}}},
                                ],
'Spiral'             :          [{f: 'C'}],
'Set Spline Type'    :          [{}],
'Star'               :          [{f: 'C'}],
'Curve to Mesh'      :          [{name: 'to_mesh'}],
'Curve to Points'    :          [{name: 'to_points'}, {name: 'to_points', klass: 'SplinePoint'}],
'Curves to Grease Pencil' :     [{name: 'to_grease_pencil'}],
'Deform Curves on Surface' :    [{name: 'deform_on_surface'}],
'Delete Geometry'    :          [{}, {name: 'delete'}],
'Distribute Points in Grid' :   [{f: 'C', name: 'DistributeInGrid'}],
'Distribute Points in Volume' : [{name: 'distribute_points'}],
'Distribute Points on Faces' :  [{},
                                 {param_loop: 'distribute_method', prefix: 'distribute_points_on_faces_'},
                                 {name: 'distribute_points', klass: 'Face'},
                                 {param_loop: 'distribute_method', 'domain_value': 'FACE', prefix: 'distribute_points_'},
                                ],
'Dual Mesh'          :          [{name: 'dual'}],
'Duplicate Elements' :          [{name: 'duplicate'}],
'Edge Paths to Curves' :        [{}, {name: 'paths_to_curves', klass: 'Edge'}],
'Edge Paths to Selection' :     [{klass: 'Mesh'}, {name: 'paths_to_selection', klass: 'Edge'}],
'Edges of Corner'    :          [{klass: 'Mesh'}, {f: 'get_out_loop', klass: 'Corner', name: 'edges'}],
'Edges of Vertex'    :          [{klass: 'Mesh'}, {f: 'get_out_loop', klass: 'Vertex', name: 'edges', rename: {'total': 'edges_total'}}],
'Edges to Face Groups' :        [{klass: 'Mesh'}, {name: 'to_face_groups', klass: 'Edge'}],
'Extrude Mesh'       :          [{name: 'extrude'},
                                 {name: 'extrude', klass: 'Vertex', parameters: {'mode': 'VERTICES'}},
                                 {name: 'extrude', klass: 'Edge',   parameters: {'mode': 'EDGES'}},
                                 {name: 'extrude', klass: 'Face',   parameters: {'mode': 'FACES'}},
                                ],
'Face of Corner'     :          [{klass: 'Mesh'}, {f: 'get_out_loop', name: 'face', klass: 'Corner'}],
'Evaluate at Index'  :          [{'data_type_loop': False}],
'Evaluate on Domain' :          [{'data_type_loop': False}],
'Fill Curve'         :          [{name: 'fill'}],
'Fillet Curve'       :          [{name: 'fillet'}],
'Flip Faces'         :          [{}],
'For Each Geometry Element Input'  : [{f: 'MANUAL'}],
'For Each Geometry Element Output' : [{f: 'MANUAL'}],
'Geometry to Instance' :        [{name: 'to_instance'},
                                 {f: 'C', name: 'FromGeometry'}
                                ],
'Get Named Grid'     :          [{},
                                 {parameters: {'data_type': 'FLOAT'},  name: 'named_float_grid' },
                                 {parameters: {'data_type': 'VECTOR'}, name: 'named_vector_grid'},
                                ],
'Dial Gizmo'         :          [{}],
'Linear Gizmo'       :          [{}],
'Transform Gizmo'    :          [{}],
'Grease Pencil to Curves' :     [{name: 'to_curves'}],
'Grid to Mesh'       :          [{name: 'to_mesh'}],
'Group'              :          [{f: 'MANUAL'}],
'Image Info'         :          [{f: 'get_out_loop', name: 'info'}],
'Image Texture'      :          [{f: 'C'}],
'Import OBJ'         :          [{f: 'C', name: 'ImportOBJ'}],
'Import PLY'         :          [{f: 'C', name: 'ImportPLY'}],
'Import STL'         :          [{f: 'C', name: 'ImportSTL'}],
'Index of Nearest'   :          [{f: 'get', klass: 'Geometry'}],
'Index Switch'       :          [{f: 'MANUAL'}],
'Active Camera'      :          [{f: 'C'}],
'Collection'         :          [{f: 'INIT'}],
'Curve Handle Positions' :      [{name: 'handle_positions', is_cm: True, klass: 'Curve'}],
'Curve Tilt'         :          [{f: 'PROP'}],
'Is Edge Smooth'     :          [{f: 'PROP'}],
'ID'                 :          [{f: 'STATIC'}],
'Image'              :          [{f: 'INIT'}],
'Index'              :          [{klass: 'Geometry'}],
'Instance Rotation'  :          [{name: 'rotation', klass: 'Instances'}],
'Instance Scale'     :          [{name: 'instance_scale', klass: 'Instances'}],
'Material'           :          [{f: 'PROP'}],
'Material Index'     :          [{f: 'PROP'}],
'Edge Angle'         :          [{f: 'get_out_loop', name: 'edge_angle', klass: 'Mesh', prefix: '',
                                        rename: {'unsigned_angle': 'unsigned_edge_angle', 'signed_angle': 'signed_edge_angle'}},
                                 {f: 'get_out_loop', klass: 'Edge'},
                                ],
'Edge Neighbors'     :          [{klass: 'Mesh'}, {name: 'face_count', klass: 'Edge'}],
'Edge Vertices'      :          [{f: 'get', klass: 'Mesh', ret: 'NODE'}, {f:'get_out_loop', klass: 'Edge'}],
'Face Area'          :          [{klass: 'Mesh'}, {name: 'area', klass: 'Face'}],
'Is Face Planar'     :          [{klass: 'Mesh'}, {name: 'is_planar', klass: 'Face'}],
'Face Neighbors'     :          [{f: 'get', klass: 'Mesh', ret: 'NODE'}, {f: 'get_out_loop', klass: 'Face', name: 'neighbors', prefix: 'neighbors_'}],
'Mesh Island'        :          [{f: 'get_out_loop', klass: 'Mesh'}],
'Vertex Neighbors'   :          [{f: 'get', klass: 'Mesh', ret: 'NODE'}, {f: 'get_out_loop', klass: 'Vertex', name: 'neighbors', prefix: 'neighbors_'}],
'Named Attribute'    :          [{f: 'C', name: 'Named'}, {f: 'C', name: 'NamedAttribute'}, ],
'Named Layer Selection' :       [{klass: 'GreasePencil'}, {name: 'named_selection', klass: 'Layer'}],
'Normal'             :          [{klass: 'Mesh'}, {klass: 'Face'}],
'Object'             :          [{f: 'INIT'}],
'Position'           :          [{f: 'PROP'}],
'Radius'             :          [{f: 'PROP'}],
'Scene Time'         :          [{f: 'get', klass: 'Float', ret: 'NODE'},
                                 {f: 'get', name: 'seconds', klass: 'Float', ret: 'seconds'},
                                 {f: 'get', name: 'frame',   klass: 'Float', ret: 'frame'},
                                ],
'Is Face Smooth'     :          [{f: 'PROP'}],
'Shortest Edge Paths' :         [{klass: 'Mesh'}, {name: 'shortest_paths', klass: 'Edge'}],
'Is Spline Cyclic'   :          [{f: 'PROP'}],
'Spline Resolution'  :          [{f: 'PROP'}],
'Curve Tangent'      :          [{name: 'tangent', klass: 'Curve'}],
'Instance on Points' :          [{klass: 'Geometry'},
                                 {name: 'instance_on', klass:'Cloud'},
                                 {name: 'instance_on', klass:'Point'},
                                ],
'Instance Transform' :          [{f: 'PROP'}],
'Instances to Points' :         [{name: 'to_points'}],
'Interpolate Curves' :          [{f: 'C', name: 'Interpolate'}, {name: 'interpolate'}, {self_: 'Points'}],
'Is Viewport'        :          [{f: 'get', klass: 'Boolean'}],
'Join Geometry'      :          [{name: 'join'}, {f: 'C', name: 'Join'}],
'Material Selection' :          [{klass: 'Mesh'}, {klass: 'Curve'}],
'Menu Switch'        :          [{f: 'MANUAL'}],
'Merge by Distance'  :          [{'mode_loop': False}, {name: 'merge'}],
'Merge Layers'       :          [{rename: {'merge_by_name': 'by_name', 'merge_by_id': 'by_id'}}],
'Mesh Boolean'       :          [{name: 'boolean'}, {f: 'C', name: 'Boolean'},
                                 {param_loop: 'operation'}, {f: 'C', param_loop: 'operation'},
                                ],
'Mesh Circle'        :          [{f: 'C', name: 'Circle'}],
'Cone'               :          [{f: 'C'}],
'Cube'               :          [{f: 'C'}],
'Cylinder'           :          [{f: 'C'}],
'Face Group Boundaries' :       [{klass: 'Mesh'}],
'Grid'               :          [{f: 'C'}],
'Ico Sphere'         :          [{f: 'C'}],
'Mesh Line'          :          [{f: 'C', name: 'Line'}],
'Mesh to Curve'      :          [{name: 'to_curve'}],
'Mesh to Density Grid' :        [{name: 'to_density_grid'}],
'Mesh to Points'     :          [{name: 'to_points', 'mode_loop': False},
                                 {param_loop: 'mode', suffix: '_to_points'},
                                 {name: 'to_points', parameters: {'mode': 'VERTICES'}, klass: 'Vertex'},
                                 {name: 'to_points', parameters: {'mode': 'FACES'},    klass: 'Face'},
                                 {name: 'to_points', parameters: {'mode': 'EDGES'},    klass: 'Edge'},
                                 {name: 'to_points', parameters: {'mode': 'CORNERS'},  klass: 'Corner'},
                                ],
'Mesh to SDF Grid'   :          [{name: 'to_sdf_grid'}],
'Mesh to Volume'     :          [{name: 'to_volume'}],
'UV Sphere'          :          [{f: 'C', name: 'UVSphere'}],
'Object Info'        :          [{f: 'get', name: 'info', ret: 'NODE'}],
'Offset Corner in Face' :       [{klass: 'Mesh'},  {name: 'offset_in_face', klass: 'Corner'}],
'Offset Point in Curve' :       [{klass: 'Curve'}, {name: 'offset_in_curve', klass: 'SplinePoint'}],
'Points'             :          [{f: 'C'}],
'Points of Curve'    :          [{klass: 'Curve'}, {f: 'get_out_loop', klass: 'Spline', rename: {'total': 'points_total'}}],
'Points to Curves'   :          [{name: 'to_curves'}],
'Points to SDF Grid' :          [{name: 'to_sdf_grid'}],
'Points to Vertices' :          [{name: 'to_vertices'}],
'Points to Volume'   :          [{name: 'to_volume'}],
'Geometry Proximity' :          [{name: 'proximity'}, {param_loop: 'target_element', prefix: 'proximity_'}],
'Raycast'            :          [{ret: 'NODE'}, {param_loop: 'mapping', prefix: 'raycast_', ret: 'NODE'}],
'Realize Instances'  :          [{name: 'realize', jump: False}],
'Remove Named Attribute' :      [{},
                                 {name: 'remove_names', parameters: {'pattern_mode': 'WILDCARD'}}
                                ],
'Repeat Input'       :          [{f: 'MANUAL'}],
'Repeat Output'      :          [{f: 'MANUAL'}],
'Replace Material'   :          [{}],
'Resample Curve'     :          [{name: 'resample'}],
'Reverse Curve'      :          [{name: 'reverse'}],
'Rotate Instances'   :          [{name: 'rotate'}],
'SDF Grid Boolean'   :          [{name: 'grid_boolean'}, {param_loop: 'operation', 'prefix': 'sdf_'}],
'Sample Curve'       :          [{name: 'sample'}],
'Sample Grid'        :          [{}],
'Sample Grid Index'  :          [{}],
'Sample Index'       :          [{}],
'Sample Nearest'     :          [{}],
'Sample Nearest Surface' :      [{}],
'Sample UV Surface'  :          [{}],
'Scale Elements'     :          [{name: 'scale'}, {param_loop: 'scale_mode', prefix: 'scale_'}],
'Scale Instances'    :          [{name: 'scale'}],
'Self Object'        :          [{f: 'C', name: 'Self'}],
'Separate Components' :         [{f: 'get_out_loop'}],
'Separate Geometry'  :          [{name: 'separate'}],
'Set Handle Positions' :        [{'mode_loop': False}, {param_loop: 'mode', prefix: 'set_', suffix: '_handle_positions'}],
'Set Curve Normal'   :          [{name: 'set_normal'}],
'Set Curve Radius'   :          [{name: 'set_radius'}],
'Set Curve Tilt'     :          [{name: 'set_tilt'}],
'Set Geometry Name'  :          [{name: 'set_name'}],
'Set ID'             :          [{name: 'set_id'}],
'Set Instance Transform' :      [{name: 'set_transform'}],
'Set Material'       :          [{}],
'Set Material Index' :          [{}],
'Set Point Radius'   :          [{name: 'set_radius', domain: 'POINT'}],
'Set Position'       :          [{}],
'Set Shade Smooth'   :          [{}],
'Set Spline Cyclic'  :          [{}],
'Set Spline Resolution' :       [{}],
'Simulation Input'   :          [{f: 'MANUAL'}],
'Simulation Output'  :          [{f: 'MANUAL'}],
'Sort Elements'      :          [{name: 'sort'}],
'Spline Length'      :          [{klass: 'Curve'}, {f: 'get_out_loop', klass: 'Spline'}],
'Spline Parameter'   :          [{klass: 'Curve'}, {f: 'get_out_loop', klass: 'Spline', name: 'parameter', prefix: 'parameter_'}],
'Split Edges'        :          [{}, {name: 'split', klass: 'Edge'}],
'Split to Instances' :          [{}],
'Store Named Attribute' :       [{}, {name: 'store'}, {name: 'store_uv', parameters: {'domain': 'CORNER', 'data_type': 'FLOAT2'}}],
'Store Named Grid'   :          [{}],
'Join Strings'       :          [{name: 'join'}, {f: 'C', name: 'Join'}],
'String to Curves'   :          [{name: 'to_curves'}],
'Subdivide Curve'    :          [{name: 'subdivide'}],
'Subdivide Mesh'     :          [{name: 'subdivide'}],
'Subdivision Surface' :         [{}],
'Switch'             :          [{f: 'MANUAL'}],
'3D Cursor'          :          [{f: 'STATIC'}],
'Active Element'     :          [{}],
'Face Set'           :          [{f: 'STATIC'}],
'Mouse Position'     :          [{f: 'STATIC'}],
'Selection'          :          [{f: 'STATIC'}],
'Set Face Set'       :          [{}],
'Set Selection'      :          [{}],
'Transform Geometry' :          [{only_enabled: False, name: 'transform'}], #, 'mode_loop': False}], #, {name: 'transform'}],
'Translate Instances' :         [{name: 'translate'}],
'Triangulate'        :          [{}],
'Trim Curve'         :          [{name: 'trim'}],
'Pack UV Islands'    :          [{}, {domain: 'CORNER'}],
'UV Unwrap'          :          [{}, {domain: 'CORNER'}],
'Vertex of Corner'   :          [{klass: 'Mesh'}, {name: 'vertex_index', klass: 'Corner'}],
'Viewer'             :          [{ret: None}],
'Viewport Transform' :          [{f: 'STATIC'}],
'Volume Cube'        :          [{f: 'C', name: 'Cube'}],
'Volume to Mesh'     :          [{name: 'to_mesh'}, {param_loop: 'resolution_mode', prefix: 'to_mesh_'}],
'Warning'            :          [{parameters: {'warning_type': 'ERROR'},   name: 'error'},
                                 {parameters: {'warning_type': 'WARNING'}, name: 'warning'},
                                 {parameters: {'warning_type': 'INFO'},    name: 'info'},
                                ],
'Frame'              :          [{f: 'MANUAL'}],
'Group Input'        :          [{f: 'MANUAL'}],
'Group Output'       :          [{f: 'MANUAL'}],
'Reroute'            :          [{f: 'MANUAL'}],
'Blackbody'          :          [{f: 'C'}],
'Clamp'              :          [{},
                                 {parameters: {'clamp_type': 'MINMAX'}, name: 'clamp_minmax'},
                                 {parameters: {'clamp_type': 'RANGE'},  name: 'clamp_range'},
                                ],
'Combine XYZ'        :          [{f: 'C', name: 'CombineXYZ'}],
'Float Curve'        :          [{f: 'MANUAL'}],
'Map Range'          :          [{},
                                 {param_loop: 'interpolation_type', prefix: 'map_range_', rename: {'smoothstep': 'smooth_step', 'smootherstep': 'smoother_step'}},
                                ],
'Math'               :          [{f: 'op', rename: {
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'logarithm'    : 'log',
                                        'absolute'     : 'abs',
                                        'exponent'     : 'exp',
                                        'sine'         : 'sin',
                                        'cosine'       : 'cos',
                                        'tangent'      : 'tan',
                                        'arcsine'      : 'asin',
                                        'arccosine'    : 'acos',
                                        'arctan'       : 'atan',
                                        'arctan2'      : 'atan2',
                                        'less_than'    : 'mless_than',
                                        'greater_than' : 'mgreater_than',
                                }},
                                {f: 'math', rename: {
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'logarithm'    : 'log',
                                        'absolute'     : 'abs',
                                        'exponent'     : 'exp',
                                        'sine'         : 'sin',
                                        'cosine'       : 'cos',
                                        'tangent'      : 'tan',
                                        'arcsine'      : 'asin',
                                        'arccosine'    : 'acos',
                                        'arctan'       : 'atan',
                                        'arctan2'      : 'atan2',
                                        'less_than'    : 'mless_than',
                                        'greater_than' : 'mgreater_than',
                                }},
                                ],
'Mix'                :          [{parameters: {'data_type': 'FLOAT', 'blend_type': 'MIX', 'factor_mode': 'UNIFORM', 'clamp_result': False}},
                                 {parameters: {'data_type': 'ROTATION', 'blend_type': 'MIX', 'factor_mode': 'UNIFORM', 'clamp_result': False}},
                                 {param_loop: 'factor_mode', prefix: 'mix_', parameters: {'data_type': 'VECTOR', 'blend_type': 'MIX', 'clamp_result': False}},
                                 {param_loop: 'blend_type',  prefix: 'mix_', parameters: {'data_type': 'RGBA', 'factor_mode': 'UNIFORM'}},
                                 {name: 'mix', parameters: {'data_type': 'RGBA', 'blend_type': 'MIX'}}, #, 'factor_mode': 'UNIFORM'}},
                                ],
'RGB Curves'         :          [{f: 'MANUAL'}],
'Separate XYZ'       :          [{f: 'get', name: 'xyz', cache: True, ret: 'TUPLE'}, {f: 'get_out_loop'}],
'Brick Texture'      :          [{f: 'C', name: 'Brick'},      {is_cm: True, name: 'Brick',      klass: 'Texture'}],
'Checker Texture'    :          [{f: 'C', name: 'Checker'},    {is_cm: True, name: 'Checked',    klass: 'Texture'}],
'Gabor Texture'      :          [{f: 'C', name: 'Gabor'},      {is_cm: True, name: 'Gabor',      klass: 'Texture'}],
'Gradient Texture'   :          [{f: 'C', name: 'Gradient'},   {is_cm: True, name: 'Gradient',   klass: 'Texture'}],
'Magic Texture'      :          [{f: 'C', name: 'Magic'},      {is_cm: True, name: 'Magic',      klass: 'Texture'}],
'Noise Texture'      :          [{f: 'C', name: 'Noise'},      {is_cm: True, name: 'Noise',      klass: 'Texture'}],
'Voronoi Texture'    :          [{f: 'C', name: 'Voronoi'},    {is_cm: True, name: 'Voronoi',    klass: 'Texture'}],
'Wave Texture'       :          [{f: 'C', name: 'Wave'},       {is_cm: True, name: 'Wave',       klass: 'Texture'}],
'White Noise Texture' :         [{f: 'C', name: 'WhiteNoise'}, {is_cm: True, name: 'WhiteNoise', klass: 'Texture'}],
'Color Ramp'         :          [{f: 'MANUAL'}],
'Value'              :          [{f: 'INPUT'}],
'Vector Curves'      :          [{f: 'MANUAL'}],
'Vector Math'        :          [{f: 'op', rename: {
                                        'cross_product': 'cross',
                                        'dot_product'  : 'dot',
                                        'absolute'     : 'abs',
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'sine'         : 'sin',
                                        'cosine'       : 'cos',
                                        'tangent'      : 'tan',
                                }},
                                {f: 'math', rename: {
                                        'add'           : 'vadd',
                                        'subtract'      : 'vsubtract',
                                        'multiply'      : 'vmultiply',
                                        'divide'        : 'vdivide',
                                        'multiply_add'  : 'vmultiply_add',
                                        'cross_product' : 'cross',
                                        'dot_product'   : 'dot',
                                        'absolute'      : 'vabs',
                                        'minimum'       : 'vmin',
                                        'maximum'       : 'vmax',
                                        'floor'         : 'vfloor',
                                        'ceil'          : 'vceil',
                                        'fraction'      : 'vfraction',
                                        'wrap'          : 'vwrap',
                                        'snap'          : 'vsnap',
                                        'sine'          : 'vsin',
                                        'cosine'        : 'vcos',
                                        'tangent'       : 'vtan',
                                        'modulo'        : 'vmodulo',
                                }},
                                ],
'Vector Rotate'      :          [{name: 'rotate'},
                                 {param_loop: 'rotation_type', prefix: 'rotate_'},
                                ],
}

GEONODES_PROPS = [
    {name: 'position', setter: 'Set Position', getter: 'Position',  in_socket: 'Position'},
    {name: 'position', setter: 'Set Position', getter: 'Position',  in_socket: 'Position', klass: 'Point'},
    {name: 'offset',   setter: 'Set Position', getter:  None,       in_socket: 'Offset'},
    {name: 'offset',   setter: 'Set Position', getter:  None,       in_socket: 'Offset', klass: 'Point'},

    {name: 'id',       setter: 'Set ID',       getter: 'ID'},

    {name: 'material', setter: 'Set Material'},
    {name: 'material', setter: 'Set Material', klass: 'Face'},
    {name: 'material', setter: 'Set Material', klass: 'Edge'},

    {name: 'name',     setter: 'Set Geometry Name'},

    {name: 'material_index', setter: 'Set Material Index', getter: 'Material Index'},
    {name: 'material_index', setter: 'Set Material Index', getter: 'Material Index', klass: 'Face'},
    {name: 'material_index', setter: 'Set Material Index', getter: 'Material Index', klass: 'Spline'},

    {name: 'radius', setter: 'Set Point Radius', getter: 'Radius', klass: 'Cloud'},
    {name: 'radius', setter: 'Set Point Radius', getter: 'Radius', klass: 'CloudPoint'},
    {name: 'radius', setter: 'Set Curve Radius', getter: 'Radius', klass: 'Curve'},
    {name: 'radius', setter: 'Set Curve Radius', getter: 'Radius', klass: 'SplinePoint'},

    {name: 'shade_smooth', setter: 'Set Shade Smooth', getter: {'Edge': 'Is Edge Smooth', 'Face': 'Is Face Smooth'}},
    {name: 'smooth',       setter: 'Set Shade Smooth', getter: {'Edge': 'Is Edge Smooth', 'Face': 'Is Face Smooth'}},

    {name: 'left_handle_position',  setter: 'Set Handle Positions', set_prm: {'mode': 'LEFT'},
        getter: 'Curve Handle Positions', get_sock: {'Relative': False}, out_socket: 'left'},
    {name: 'right_handle_position', setter: 'Set Handle Positions', set_prm: {'mode': 'RIGHT'},
        getter: 'Curve Handle Positions', get_sock: {'Relative': False}, out_socket: 'right'},
    {name: 'left_handle_offset',    setter: 'Set Handle Positions', set_prm: {'mode': 'LEFT'},  in_socket: 'Offset',
        getter: 'Curve Handle Positions', get_sock: {'Relative': True}, out_socket: 'left'},
    {name: 'right_handle_offset',   setter: 'Set Handle Positions', set_prm: {'mode': 'RIGHT'}, in_socket: 'Offset',
        getter: 'Curve Handle Positions', get_sock: {'Relative': True}, out_socket: 'right'},

    {name: 'handle_type',       setter: 'Set Handle Type', set_prm: {'mode': {'LEFT', 'RIGHT'}}},
    {name: 'left_handle_type',  setter: 'Set Handle Type', set_prm: {'mode': {'LEFT'}}},
    {name: 'right_handle_type', setter: 'Set Handle Type', set_prm: {'mode': {'RIGHT'}}},

    {name: 'transform', setter: 'Set Instance Transform', getter: 'Instance Transform'},

    {name: 'tilt',       setter: 'Set Curve Tilt', getter: 'Curve Tilt', klass: 'Curve'},
    {name: 'tilt',       setter: 'Set Curve Tilt', getter: 'Curve Tilt', klass: 'Spline'},
    {name: 'normal',     setter: 'Set Curve Normal', klass: 'Curve'},
    {name: 'normal',     setter: 'Set Curve Normal', klass: 'Spline'},
    {name: 'is_cyclic',  setter: 'Set Spline Cyclic', getter: 'Is Spline Cyclic', klass: 'Curve'},
    {name: 'is_cyclic',  setter: 'Set Spline Cyclic', getter: 'Is Spline Cyclic', klass: 'Spline'},
    {name: 'resolution', setter: 'Set Spline Resolution', getter: 'Spline Resolution', klass: 'Curve'},
    {name: 'resolution', setter: 'Set Spline Resolution', getter: 'Spline Resolution', klass: 'Spline'},
    {name: 'type',       setter: 'Set Spline Type', klass: 'Curve'},
    {name: 'type',       setter: 'Set Spline Type', klass: 'Spline'},
]

SHADERNODES = {
'Add Shader'                : [{name: 'add'}],
'Ambient Occlusion'         : [{}],
'Attribute'                 : [{f: 'STATIC'}],
'Background'                : [{}],
'Bevel'                     : [{}],
'Brightness/Contrast'       : [{}],
'Glossy BSDF'               : [{f: 'C', name: 'Glossy'}],
'Diffuse BSDF'              : [{f: 'C', name: 'Diffuse'}],
'Glass BSDF'                : [{f: 'C', name: 'Glass'}],
'Hair BSDF'                 : [{f: 'C', name: 'Hair'}],
'Principled Hair BSDF'      : [{f: 'C', name: 'PrincipledHair'}],
'Metallic BSDF'             : [{f: 'C', name: 'Metallic'}],
'Principled BSDF'           : [{f: 'C', name: 'Principled'}],
'Ray Portal BSDF'           : [{f: 'C', name: 'RayPortal'}],
'Refraction BSDF'           : [{f: 'C', name: 'Refraction'}],
'Sheen BSDF'                : [{f: 'C', name: 'Sheen'}],
'Toon BSDF'                 : [{f: 'C', name: 'Toon'}],
'Translucent BSDF'          : [{f: 'C', name: 'Translucent'}],
'Transparent BSDF'          : [{f: 'C', name: 'Transparent'}],
'Bump'                      : [{}],
'Camera Data'               : [{f: 'STATIC'}],
'Combine Color'             : [{}],
'Displacement'              : [{}],
'Specular BSDF'             : [{f: 'C', name: 'Specular'}],
'Emission'                  : [{f: 'C'}],
'Fresnel'                   : [{}],
'Gamma'                     : [{}],
'Group'                     : [{f: 'STATIC'}],
'Curves Info'               : [{f: 'STATIC'}],
'Holdout'                   : [{f: 'C'}],
'Hue/Saturation/Value'      : [{}, {klass: 'Color', self_: 'Color'}],
'Invert Color'              : [{}],
'Layer Weight'              : [{}],
'Light Falloff'             : [{}],
'Light Path'                : [{f: 'STATIC'}],
'Mapping'                   : [{}],
'Mix Shader'                : [{name: 'mix'}],
'Geometry'                  : [{f: 'STATIC'}],
'Normal'                    : [{}],
'Normal Map'                : [{}],
'Object Info'               : [{f: 'STATIC'}],
'AOV Output'                : [{}],
'Light Output'              : [{}],
'Line Style Output'         : [{}],
'Material Output'           : [{}],
'World Output'              : [{}],
'Particle Info'             : [{f: 'STATIC'}],
'Point Info'                : [{f: 'STATIC'}],
'RGB'                       : [{f: 'C'}],
'RGB to BW'                 : [{}],
'Script'                    : [{f: 'STATIC'}],
'Separate Color'            : [{name: 'separate_col'}], # Homonym
'Shader to RGB'             : [{name: 'to_rgb'}],
'Subsurface Scattering'     : [{f: 'C'}],
'Tangent'                   : [{f: "C"}],
'Texture Coordinate'        : [{f: 'STATIC'}],
'Environment Texture'       : [{}],
'IES Texture'               : [{}],
'Image Texture'             : [{}],
'Point Density'             : [{}],
'Sky Texture'               : [{f: 'C'}],
'UV Along Stroke'           : [{f: 'STATIC'}],
'UV Map'                    : [{f: 'C'}],
'Vector Displacement'       : [{}],
'Vector Transform'          : [{}],
'Color Attribute'           : [{f: 'C'}],
'Volume Absorption'         : [{f: 'C', name : 'Absorption'}],
'Volume Info'               : [{f: 'get', ret: 'NODE', name: 'info', klass: 'VolumeShader'}],
'Principled Volume'         : [{f: 'C', name: 'Principled'}],
'Volume Scatter'            : [{f: 'C', name: 'Scatter'}],
'Wavelength'                : [{}],
'Wireframe'                 : [{}],
}
